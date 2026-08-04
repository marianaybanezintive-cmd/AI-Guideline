"""Cliente REST de Jira Cloud sin dependencias externas.

Autenticación por variables de entorno:
    JIRA_BASE_URL   https://bancoatlaspy.atlassian.net
    JIRA_EMAIL      correo de la cuenta Atlassian
    JIRA_API_TOKEN  token generado en id.atlassian.com/manage-profile/security/api-tokens
"""

from __future__ import annotations

import base64
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_TIMEOUT = 60
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
                + "\nGenerá un token en https://id.atlassian.com/manage-profile/security/api-tokens"
            )

        token = base64.b64encode(f"{self.email}:{self.api_token}".encode()).decode()
        self._headers = {
            "Authorization": f"Basic {token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "sprint-health-check/1.0",
        }
        self._ssl_context = ssl.create_default_context()

    def get(self, path, params=None):
        """GET con reintentos ante 429 y errores transitorios de red."""
        url = f"{self.base_url}{path}"
        if params:
            clean = {k: v for k, v in params.items() if v is not None}
            url = f"{url}?{urllib.parse.urlencode(clean)}"

        last_error = None
        for attempt in range(MAX_RETRIES):
            request = urllib.request.Request(url, headers=self._headers, method="GET")
            try:
                with urllib.request.urlopen(request, timeout=self.timeout, context=self._ssl_context) as response:
                    return json.loads(response.read().decode("utf-8"))
            except urllib.error.HTTPError as exc:
                body = exc.read().decode("utf-8", errors="replace")[:500]
                # 429/5xx son transitorios: back-off exponencial respetando Retry-After.
                if exc.code == 429 or exc.code >= 500:
                    wait = float(exc.headers.get("Retry-After") or 2 ** attempt)
                    last_error = JiraError(f"HTTP {exc.code} en {url}: {body}")
                    time.sleep(wait)
                    continue
                if exc.code == 401:
                    raise JiraError(
                        f"HTTP 401 no autorizado. Revisá JIRA_EMAIL y JIRA_API_TOKEN.\n{body}"
                    ) from exc
                if exc.code == 403:
                    raise JiraError(f"HTTP 403 sin permisos sobre {url}.\n{body}") from exc
                raise JiraError(f"HTTP {exc.code} en {url}: {body}") from exc
            except (urllib.error.URLError, TimeoutError) as exc:
                last_error = JiraError(f"Error de red en {url}: {exc}")
                time.sleep(2 ** attempt)

        raise last_error or JiraError(f"Fallo la petición a {url}")

    def get_optional(self, path, params=None):
        """Igual que get() pero devuelve None si el endpoint no está disponible."""
        try:
            return self.get(path, params)
        except JiraError:
            return None

    def paginate(self, path, params=None, items_key="values", page_size=50, max_items=None):
        """Recorre endpoints paginados con startAt/maxResults."""
        params = dict(params or {})
        start_at = 0
        collected = []
        while True:
            params.update({"startAt": start_at, "maxResults": page_size})
            payload = self.get(path, params)
            batch = payload.get(items_key) or []
            collected.extend(batch)

            if max_items is not None and len(collected) >= max_items:
                return collected[:max_items]

            total = payload.get("total")
            is_last = payload.get("isLast")
            if is_last is True or not batch:
                return collected
            if total is not None and len(collected) >= total:
                return collected
            start_at += len(batch)

    def discover_fields(self):
        """Mapea nombre de campo -> id para resolver custom fields por nombre."""
        fields = self.get("/rest/api/3/field")
        return {f.get("name", ""): f.get("id", "") for f in fields if isinstance(f, dict)}


def resolve_field_id(field_map, candidate_names):
    """Devuelve el id del primer campo cuyo nombre coincida (case-insensitive)."""
    lowered = {name.lower(): field_id for name, field_id in field_map.items()}
    for candidate in candidate_names:
        field_id = lowered.get(candidate.lower())
        if field_id:
            return field_id
    return None


def adf_to_text(node):
    """Aplana un documento ADF (Atlassian Document Format) a texto plano."""
    if node is None:
        return ""
    if isinstance(node, str):
        return node
    if isinstance(node, list):
        return "".join(adf_to_text(item) for item in node)
    if not isinstance(node, dict):
        return str(node)

    node_type = node.get("type")
    if node_type == "text":
        return node.get("text", "")
    if node_type == "hardBreak":
        return "\n"

    inner = adf_to_text(node.get("content"))
    if node_type in {"paragraph", "heading", "listItem", "codeBlock", "blockquote"}:
        return inner + "\n"
    if node_type in {"bulletList", "orderedList", "table", "tableRow"}:
        return inner
    return inner


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)
