"""Cliente REST mínimo de Jira Cloud (sin dependencias externas).

Variables de entorno (mismas que sprint-health-check):
    JIRA_BASE_URL   https://bancoatlaspy.atlassian.net
    JIRA_EMAIL      correo Atlassian
    JIRA_API_TOKEN  token de API
"""

from __future__ import annotations

import base64
import json
import os
import ssl
import time
import urllib.error
import urllib.request

DEFAULT_TIMEOUT = 60
MAX_RETRIES = 4


class JiraError(RuntimeError):
    pass


class JiraRest:
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
                "Faltan credenciales: "
                + ", ".join(missing)
                + "\nEjecutá AI-Agents/sprint-health-check/scripts/set_credentials.ps1"
            )

        token = base64.b64encode(f"{self.email}:{self.api_token}".encode()).decode()
        self._headers = {
            "Authorization": f"Basic {token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "jira-load-user-stories/1.0",
        }
        self._ssl = ssl.create_default_context()

    def _request(self, method: str, path: str, payload: dict | None = None) -> dict | None:
        url = f"{self.base_url}{path}"
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        last_error = None
        for attempt in range(MAX_RETRIES):
            req = urllib.request.Request(url, data=data, headers=self._headers, method=method)
            try:
                with urllib.request.urlopen(req, timeout=self.timeout, context=self._ssl) as resp:
                    raw = resp.read()
                    if not raw:
                        return None
                    return json.loads(raw.decode("utf-8"))
            except urllib.error.HTTPError as exc:
                body = exc.read().decode("utf-8", errors="replace")[:800]
                if exc.code in (429,) or exc.code >= 500:
                    wait = float(exc.headers.get("Retry-After") or 2**attempt)
                    last_error = JiraError(f"HTTP {exc.code} {method} {url}: {body}")
                    time.sleep(wait)
                    continue
                raise JiraError(f"HTTP {exc.code} {method} {url}: {body}") from exc
            except urllib.error.URLError as exc:
                last_error = JiraError(f"Red {method} {url}: {exc}")
                time.sleep(2**attempt)
        raise last_error or JiraError(f"Fallo {method} {url}")

    def update_description_adf(self, issue_key: str, markdown_text: str) -> None:
        """Actualiza description en ADF (doc) con un único bloque de texto multilínea.

        Jira Cloud API v3 espera ADF. Usamos un paragraph por línea no vacía
        y hardBreak implícito vía paragraphs separados — suficiente para el cuerpo PO.
        """
        lines = markdown_text.replace("\r\n", "\n").split("\n")
        content = []
        for line in lines:
            if line == "":
                content.append({"type": "paragraph"})
            else:
                content.append(
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": line}],
                    }
                )
        if not content:
            content = [{"type": "paragraph"}]

        adf = {"type": "doc", "version": 1, "content": content}
        self._request("PUT", f"/rest/api/3/issue/{issue_key}", {"fields": {"description": adf}})
