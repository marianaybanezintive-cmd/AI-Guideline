"""Cliente REST de Jira Cloud (stdlib) para sm-mass-clone."""

from __future__ import annotations

import base64
import json
import os
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_TIMEOUT = 90
MAX_RETRIES = 4


class JiraError(RuntimeError):
    pass


class JiraClient:
    def __init__(self, base_url=None, email=None, api_token=None, timeout=DEFAULT_TIMEOUT):
        self.base_url = (base_url or os.environ.get("JIRA_BASE_URL", "")).rstrip("/")
        self.email = email or os.environ.get("JIRA_EMAIL", "")
        self.api_token = api_token or os.environ.get("JIRA_API_TOKEN", "")
        self.timeout = timeout

        missing = [
            name
            for name, value in (
                ("JIRA_BASE_URL", self.base_url),
                ("JIRA_EMAIL", self.email),
                ("JIRA_API_TOKEN", self.api_token),
            )
            if not value
        ]
        if missing:
            raise JiraError(
                "Faltan credenciales de Jira: "
                + ", ".join(missing)
                + "\nEjecutá AI-Agents/sm-mass-clone/scripts/set_credentials.ps1"
            )

        token = base64.b64encode(f"{self.email}:{self.api_token}".encode()).decode()
        self._headers = {
            "Authorization": f"Basic {token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "sm-mass-clone/1.0",
        }
        self._ssl_context = ssl.create_default_context()

    def request(self, method, path, params=None, body=None, raw=False):
        url = f"{self.base_url}{path}"
        if params:
            clean = {k: v for k, v in params.items() if v is not None}
            url = f"{url}?{urllib.parse.urlencode(clean)}"

        data = None
        if body is not None:
            data = body if isinstance(body, (bytes, bytearray)) else json.dumps(body).encode("utf-8")

        last_error = None
        for attempt in range(MAX_RETRIES):
            request = urllib.request.Request(url, data=data, headers=self._headers, method=method)
            try:
                with urllib.request.urlopen(
                    request, timeout=self.timeout, context=self._ssl_context
                ) as response:
                    payload = response.read()
                    if raw:
                        return response.status, payload
                    if not payload:
                        return response.status, None
                    return response.status, json.loads(payload.decode("utf-8"))
            except urllib.error.HTTPError as exc:
                err_body = exc.read().decode("utf-8", errors="replace")[:800]
                if exc.code in (429,) or exc.code >= 500:
                    wait = float(exc.headers.get("Retry-After") or 2 ** attempt)
                    last_error = JiraError(f"HTTP {exc.code} {method} {url}: {err_body}")
                    time.sleep(wait)
                    continue
                if exc.code == 401:
                    raise JiraError(
                        f"HTTP 401. Revisá JIRA_EMAIL / JIRA_API_TOKEN.\n{err_body}"
                    ) from exc
                raise JiraError(f"HTTP {exc.code} {method} {url}: {err_body}") from exc
            except (urllib.error.URLError, TimeoutError) as exc:
                last_error = JiraError(f"Error de red {method} {url}: {exc}")
                time.sleep(2 ** attempt)

        raise last_error or JiraError(f"Fallo {method} {url}")

    def get(self, path, params=None):
        _, data = self.request("GET", path, params=params)
        return data

    def post(self, path, body=None, params=None):
        _, data = self.request("POST", path, params=params, body=body)
        return data

    def put(self, path, body=None, params=None):
        status, data = self.request("PUT", path, params=params, body=body)
        return status, data

    def search_jql(self, jql, fields=None, max_results=100):
        """Usa /rest/api/3/search/jql (API actual)."""
        issues = []
        next_token = None
        field_list = fields or [
            "summary",
            "description",
            "status",
            "issuetype",
            "parent",
            "assignee",
            "sprint",
            "project",
        ]
        while True:
            params = {
                "jql": jql,
                "maxResults": max_results,
                "fields": ",".join(field_list),
            }
            if next_token:
                params["nextPageToken"] = next_token
            payload = self.get("/rest/api/3/search/jql", params)
            batch = payload.get("issues") or []
            issues.extend(batch)
            if payload.get("isLast", True):
                break
            next_token = payload.get("nextPageToken")
            if not next_token:
                break
        return issues

    def discover_fields(self):
        fields = self.get("/rest/api/3/field")
        return {f.get("name", ""): f.get("id", "") for f in fields if isinstance(f, dict)}


def resolve_field_id(field_map, candidate_names):
    lowered = {name.lower(): field_id for name, field_id in field_map.items()}
    for candidate in candidate_names:
        field_id = lowered.get(candidate.lower())
        if field_id:
            return field_id
    return None


def load_user_env_fallback():
    """En Windows, carga User env si el proceso no las tiene (Cursor a veces no hereda)."""
    if os.name != "nt":
        return
    try:
        import winreg

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as key:
            for name in ("JIRA_BASE_URL", "JIRA_EMAIL", "JIRA_API_TOKEN"):
                if os.environ.get(name):
                    continue
                try:
                    value, _ = winreg.QueryValueEx(key, name)
                    if value:
                        os.environ[name] = str(value)
                except FileNotFoundError:
                    pass
    except Exception:
        pass
