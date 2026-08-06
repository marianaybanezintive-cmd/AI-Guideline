"""Busca issues por origen/tipo/estado y los clona masivamente en Jira.

Ejemplos:
  python clone_issues.py --config ../config.json --origin-type epic --origin-value MAGIA-5 \\
      --issue-type Historia --status "Tareas por hacer" --title-prefix "QA - " --dry-run

  python clone_issues.py ... --assignee "Alexis Alvarez" -o ../../AI-Outputs/sm-mass-clone/last-run.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from jira_client import JiraClient, JiraError, load_user_env_fallback, resolve_field_id

SPRINT_FIELD_NAMES = ["Sprint", "sprint"]


def load_config(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def resolve_alias(value: str, alias_map: dict) -> list[str]:
    """Devuelve lista de nombres canónicos a usar en JQL."""
    raw = (value or "").strip()
    if not raw:
        return []
    key = raw.lower()
    for alias, names in (alias_map or {}).items():
        if key == alias.lower() or key in [n.lower() for n in names]:
            return list(names)
    return [raw]


def parse_board_url(url: str) -> dict:
    """Extrae base, project_key y board_id de una URL de board Jira."""
    out = {"jira_base_url": "", "project_key": "", "board_id": None, "project_url": url}
    m = re.match(r"(https?://[^/]+)", url or "")
    if m:
        out["jira_base_url"] = m.group(1)
    m = re.search(r"/projects/([A-Za-z0-9_]+)/", url or "")
    if m:
        out["project_key"] = m.group(1)
    m = re.search(r"/boards/(\d+)", url or "")
    if m:
        out["board_id"] = int(m.group(1))
    return out


def jql_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def build_jql(config: dict, origin_type: str, origin_value: str, issue_types: list[str], statuses: list[str]) -> str:
    project = config["project_key"]
    parts = [f"project = {project}"]

    otype = (origin_type or "").strip().lower()
    if otype in ("epica", "épica", "epic"):
        if not origin_value:
            raise SystemExit("ERROR: --origin-value es obligatorio para origen épica (ej. MAGIA-5)")
        key = origin_value.strip()
        parts.append(f'(parent = {key} OR "Epic Link" = {key})')
    elif otype == "sprint":
        if not origin_value:
            raise SystemExit("ERROR: --origin-value es obligatorio para origen sprint (nombre o id)")
        val = origin_value.strip()
        if val.isdigit():
            parts.append(f"sprint = {val}")
        else:
            parts.append(f"sprint = {jql_quote(val)}")
    elif otype == "backlog":
        parts.append("sprint is EMPTY")
    else:
        raise SystemExit("ERROR: --origin-type debe ser epica | sprint | backlog")

    if issue_types:
        if len(issue_types) == 1:
            parts.append(f"issuetype = {jql_quote(issue_types[0])}")
        else:
            joined = ", ".join(jql_quote(t) for t in issue_types)
            parts.append(f"issuetype in ({joined})")

    if statuses:
        if len(statuses) == 1:
            parts.append(f"status = {jql_quote(statuses[0])}")
        else:
            joined = ", ".join(jql_quote(s) for s in statuses)
            parts.append(f"status in ({joined})")

    parts.append("ORDER BY key ASC")
    return " AND ".join(parts[:-1]) + " " + parts[-1]


def extract_sprint_ids(fields: dict, sprint_field_id: str | None) -> list[int]:
    ids = []
    raw = None
    if sprint_field_id:
        raw = fields.get(sprint_field_id)
    if raw is None:
        raw = fields.get("sprint")
    if not raw:
        return ids
    items = raw if isinstance(raw, list) else [raw]
    for item in items:
        if isinstance(item, dict) and item.get("id") is not None:
            try:
                ids.append(int(item["id"]))
            except (TypeError, ValueError):
                pass
        elif isinstance(item, str):
            # greenhopper string form: ...id=1770,...
            m = re.search(r"id=(\d+)", item)
            if m:
                ids.append(int(m.group(1)))
    return ids


def build_clone_summary(original_summary: str, title_prefix: str) -> str:
    prefix = title_prefix or ""
    summary = (original_summary or "").strip()
    if prefix and summary.lower().startswith(prefix.lower()):
        return summary
    return f"{prefix}{summary}".strip()


def find_user_account_id(client: JiraClient, name_or_email: str) -> tuple[str | None, str | None]:
    if not name_or_email or not name_or_email.strip():
        return None, None
    query = name_or_email.strip()
    users = client.get("/rest/api/3/user/search", {"query": query}) or []
    if not users:
        return None, None
    # Prefer exact displayName / email match
    q_lower = query.lower()
    for user in users:
        display = (user.get("displayName") or "").lower()
        email = (user.get("emailAddress") or "").lower()
        if q_lower == display or q_lower == email:
            return user.get("accountId"), user.get("displayName")
    user = users[0]
    return user.get("accountId"), user.get("displayName")


def create_issue(client: JiraClient, project_key: str, issue_type: str, summary: str, description) -> dict:
    fields = {
        "project": {"key": project_key},
        "issuetype": {"name": issue_type},
        "summary": summary,
    }
    if description is not None:
        fields["description"] = description
    return client.post("/rest/api/3/issue", {"fields": fields})


def _flatten_adf(node) -> str:
    if node is None:
        return ""
    if isinstance(node, str):
        return node
    if isinstance(node, list):
        return "".join(_flatten_adf(n) for n in node)
    if not isinstance(node, dict):
        return ""
    if node.get("type") == "text":
        return node.get("text") or ""
    if node.get("type") == "hardBreak":
        return "\n"
    return _flatten_adf(node.get("content"))


def update_description(client: JiraClient, issue_key: str, description) -> None:
    if description is None:
        return
    try:
        client.put(f"/rest/api/3/issue/{issue_key}", {"fields": {"description": description}})
    except JiraError:
        text = _flatten_adf(description).strip() or "(sin descripcion)"
        plain = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": text[:32000]}],
                }
            ],
        }
        client.put(f"/rest/api/3/issue/{issue_key}", {"fields": {"description": plain}})


def set_parent(client: JiraClient, issue_key: str, parent_key: str) -> None:
    client.put(f"/rest/api/3/issue/{issue_key}", {"fields": {"parent": {"key": parent_key}}})


def assign_issue(client: JiraClient, issue_key: str, account_id: str) -> None:
    client.put(f"/rest/api/3/issue/{issue_key}/assignee", {"accountId": account_id})


def link_relates(client: JiraClient, clone_key: str, original_key: str, link_type_name: str) -> None:
    # Clon (outward) "está relacionado a" original (inward) según tipología Relacionar
    client.post(
        "/rest/api/3/issueLink",
        {
            "type": {"name": link_type_name},
            "outwardIssue": {"key": clone_key},
            "inwardIssue": {"key": original_key},
        },
    )


def add_to_sprint(client: JiraClient, sprint_id: int, issue_key: str) -> None:
    client.post(f"/rest/agile/1.0/sprint/{sprint_id}/issue", {"issues": [issue_key]})


def clone_one(
    client: JiraClient,
    config: dict,
    issue: dict,
    title_prefix: str,
    assignee_account_id: str | None,
    assignee_name: str | None,
    sprint_field_id: str | None,
) -> dict:
    fields = issue.get("fields") or {}
    original_key = issue["key"]
    original_summary = fields.get("summary") or ""
    issue_type = (fields.get("issuetype") or {}).get("name") or "Task"
    description = fields.get("description")
    parent = fields.get("parent") or {}
    parent_key = parent.get("key")
    sprint_ids = extract_sprint_ids(fields, sprint_field_id)
    project_key = config["project_key"]
    link_type = config.get("link_type_name") or "Relacionar"

    new_summary = build_clone_summary(original_summary, title_prefix)
    result = {
        "original_key": original_key,
        "original_summary": original_summary,
        "original_url": f"{client.base_url}/browse/{original_key}",
        "clone_key": None,
        "clone_summary": new_summary,
        "clone_url": None,
        "sprint_ids": sprint_ids,
        "assignee": assignee_name,
        "parent_key": parent_key,
        "ok": False,
        "error": None,
    }

    try:
        created = create_issue(client, project_key, issue_type, new_summary, description)
        clone_key = created["key"]
        result["clone_key"] = clone_key
        result["clone_url"] = f"{client.base_url}/browse/{clone_key}"

        # Reaplicar descripción (algunos proyectos pisan el template al crear)
        update_description(client, clone_key, description)

        if parent_key:
            try:
                set_parent(client, clone_key, parent_key)
            except JiraError as exc:
                result["error"] = f"clon ok; parent falló: {exc}"

        if assignee_account_id:
            assign_issue(client, clone_key, assignee_account_id)

        link_relates(client, clone_key, original_key, link_type)

        for sid in sprint_ids:
            add_to_sprint(client, sid, clone_key)

        result["ok"] = True
        if result["error"]:
            # partial success still ok=True with warning in error
            pass
    except Exception as exc:  # noqa: BLE001
        result["error"] = str(exc)[:500]
        result["ok"] = False

    return result


def main() -> None:
    load_user_env_fallback()

    parser = argparse.ArgumentParser(description="Clonado masivo de issues Jira (SM Mass Clone)")
    parser.add_argument("--config", required=True, help="Ruta a config.json del agente")
    parser.add_argument("--origin-type", required=True, choices=["epica", "epic", "sprint", "backlog"])
    parser.add_argument("--origin-value", default="", help="Key de épica, id/nombre de sprint (vacío si backlog)")
    parser.add_argument("--issue-type", required=True, help="Historia, Tarea, Spike, Bug, …")
    parser.add_argument("--status", required=True, help="Estado Jira a filtrar")
    parser.add_argument("--title-prefix", default="", help='Nomenclatura de título, ej. "QA - "')
    parser.add_argument("--assignee", default="", help="Nombre o email del asignado (opcional)")
    parser.add_argument("--dry-run", action="store_true", help="Solo lista candidatos, no clona")
    parser.add_argument("-o", "--output", required=True, help="JSON de resultado (last-run.json)")
    args = parser.parse_args()

    config = load_config(args.config)
    if not config.get("project_key"):
        raise SystemExit("ERROR: config.json sin project_key. Pedí la URL del proyecto y guardala.")

    if not os.environ.get("JIRA_BASE_URL") and config.get("jira_base_url"):
        os.environ["JIRA_BASE_URL"] = config["jira_base_url"]

    client = JiraClient()
    field_map = client.discover_fields()
    sprint_field_id = resolve_field_id(field_map, SPRINT_FIELD_NAMES)

    issue_types = resolve_alias(args.issue_type, config.get("issue_type_aliases") or {})
    statuses = resolve_alias(args.status, config.get("status_aliases") or {})
    jql = build_jql(config, args.origin_type, args.origin_value, issue_types, statuses)

    print(f"JQL: {jql}", file=sys.stderr)
    issues = client.search_jql(
        jql,
        fields=[
            "summary",
            "description",
            "status",
            "issuetype",
            "parent",
            "assignee",
            "project",
            sprint_field_id or "customfield_10020",
        ],
    )

    prefix = args.title_prefix or ""
    # Excluir ya clonados con la misma nomenclatura
    candidates = []
    skipped = []
    for issue in issues:
        summary = (issue.get("fields") or {}).get("summary") or ""
        if prefix and summary.lower().startswith(prefix.lower()):
            skipped.append(issue["key"])
            continue
        candidates.append(issue)

    print(f"Encontrados: {len(issues)} | candidatos: {len(candidates)} | omitidos(prefijo): {len(skipped)}", file=sys.stderr)

    assignee_account_id = None
    assignee_name = None
    if args.assignee.strip():
        assignee_account_id, assignee_name = find_user_account_id(client, args.assignee)
        if not assignee_account_id:
            raise SystemExit(f"ERROR: no se encontró usuario para assignee '{args.assignee}'")
        print(f"Assignee: {assignee_name} ({assignee_account_id})", file=sys.stderr)

    results = []
    if args.dry_run:
        for issue in candidates:
            fields = issue.get("fields") or {}
            results.append(
                {
                    "original_key": issue["key"],
                    "original_summary": fields.get("summary"),
                    "clone_summary": build_clone_summary(fields.get("summary") or "", prefix),
                    "status": (fields.get("status") or {}).get("name"),
                    "issuetype": (fields.get("issuetype") or {}).get("name"),
                    "ok": True,
                    "dry_run": True,
                }
            )
    else:
        for idx, issue in enumerate(candidates, 1):
            print(f"[{idx}/{len(candidates)}] Clonando {issue['key']}…", file=sys.stderr)
            row = clone_one(
                client,
                config,
                issue,
                prefix,
                assignee_account_id,
                assignee_name,
                sprint_field_id,
            )
            results.append(row)
            time.sleep(0.2)

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dry_run": bool(args.dry_run),
        "filters": {
            "origin_type": args.origin_type,
            "origin_value": args.origin_value,
            "issue_type": args.issue_type,
            "issue_types_resolved": issue_types,
            "status": args.status,
            "statuses_resolved": statuses,
            "title_prefix": prefix,
            "assignee": assignee_name or args.assignee or None,
            "jql": jql,
        },
        "counts": {
            "matched": len(issues),
            "candidates": len(candidates),
            "skipped_prefix": len(skipped),
            "ok": sum(1 for r in results if r.get("ok") and not r.get("dry_run")),
            "fail": sum(1 for r in results if not r.get("ok")),
        },
        "skipped_keys": skipped,
        "results": results,
        "config": {
            "project_key": config.get("project_key"),
            "board_id": config.get("board_id"),
            "jira_base_url": config.get("jira_base_url") or client.base_url,
        },
    }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Escrito: {out_path}", file=sys.stderr)


if __name__ == "__main__":
    # local flatten helper used above — ensure available if import fails
    try:
        main()
    except JiraError as exc:
        print(f"ERROR Jira: {exc}", file=sys.stderr)
        raise SystemExit(1)
