#!/usr/bin/env python3
"""Actualiza Description de issues Jira a partir de un payload JSON.

Uso (desde la raíz del repo AI-Guideline):

    python AI-Agents/jira-load-user-stories/scripts/update_descriptions.py \\
        AI-Outputs/jira-load-user-stories/jira-load-YYYY-MM-DD-slug-payload.json

Payload esperado:
{
  "issues": [
    {
      "issue_key": "MAGIA-101",
      "temp_id": "HU-GF.01",
      "description": "COMO ...\\nQUIERO ..."
    }
  ]
}

Requiere JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN en el entorno.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from jira_rest import JiraError, JiraRest  # noqa: E402


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2

    payload_path = Path(sys.argv[1])
    if not payload_path.is_file():
        print(f"No existe: {payload_path}", file=sys.stderr)
        return 2

    data = json.loads(payload_path.read_text(encoding="utf-8"))
    issues = data.get("issues") or []
    if not issues:
        print("Payload sin issues.", file=sys.stderr)
        return 2

    client = JiraRest()
    ok = 0
    fail = 0
    for item in issues:
        key = item.get("issue_key")
        desc = item.get("description") or ""
        temp = item.get("temp_id", "")
        if not key:
            print(f"SKIP sin issue_key (temp={temp})")
            fail += 1
            continue
        if not desc.strip():
            print(f"SKIP {key}: description vacía")
            fail += 1
            continue
        # Guardrail: no subir metadatos ni título Descripción
        first = next((ln.strip() for ln in desc.splitlines() if ln.strip()), "")
        if first.lower() in {"descripción", "descripcion", "description", "**descripción**", "**description**"}:
            print(f"ERROR {key}: description no debe empezar con 'Descripción'")
            fail += 1
            continue
        if "metadatos y alcance" in desc.lower()[:400]:
            print(f"WARN {key}: parece incluir Metadatos; revisá el payload")

        try:
            client.update_description_adf(key, desc)
            print(f"OK  {key}  ({temp})")
            ok += 1
        except JiraError as exc:
            print(f"FAIL {key}  ({temp}): {exc}", file=sys.stderr)
            fail += 1

    print(f"\nListo: {ok} ok, {fail} fail")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
