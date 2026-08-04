"""Descarga el sprint activo de un tablero Jira con issues, changelog y cambios de alcance.

Uso:
    python fetch_sprint_data.py --board-id 1607 --output out/raw.json
    python fetch_sprint_data.py --board-id 1607 --sprint-id 1769 --output out/raw.json
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from jira_client import JiraClient, JiraError, adf_to_text, fail, resolve_field_id

STORY_POINT_FIELD_NAMES = [
    "Story Points",
    "Story point estimate",
    "Story Point Estimate",
    "Puntos de historia",
    "Puntos de Historia",
    "Story Points Estimate",
]
FLAGGED_FIELD_NAMES = ["Flagged", "Marcado", "Impediment"]
SPRINT_FIELD_NAMES = ["Sprint"]

BASE_FIELDS = [
    "summary",
    "status",
    "issuetype",
    "assignee",
    "reporter",
    "creator",
    "created",
    "updated",
    "resolutiondate",
    "priority",
    "labels",
    "parent",
    "subtasks",
    "description",
    "duedate",
    "timeoriginalestimate",
    "timeestimate",
    "aggregatetimeoriginalestimate",
    "issuelinks",
    "components",
    "status",
]


def load_config(config_path):
    if config_path and pathlib.Path(config_path).exists():
        return json.loads(pathlib.Path(config_path).read_text(encoding="utf-8"))
    default = pathlib.Path(__file__).resolve().parent.parent / "config.json"
    if default.exists():
        return json.loads(default.read_text(encoding="utf-8"))
    return {}


def pick_active_sprint(client, board_id, sprint_id=None):
    if sprint_id:
        return client.get(f"/rest/agile/1.0/sprint/{sprint_id}")

    sprints = client.paginate(
        f"/rest/agile/1.0/board/{board_id}/sprint",
        params={"state": "active"},
        items_key="values",
    )
    if not sprints:
        fail(f"El tablero {board_id} no tiene ningún sprint activo.")
    if len(sprints) > 1:
        print(
            f"AVISO: {len(sprints)} sprints activos; se usa el más reciente por startDate.",
            file=sys.stderr,
        )
        sprints.sort(key=lambda s: s.get("startDate") or "", reverse=True)
    return sprints[0]


def fetch_sprint_issues(client, sprint_id, field_ids):
    """Trae todos los issues del sprint (incluidas subtareas) con su changelog."""
    fields = ",".join(dict.fromkeys(BASE_FIELDS + field_ids))
    issues = []
    start_at = 0
    while True:
        payload = client.get(
            f"/rest/agile/1.0/sprint/{sprint_id}/issue",
            params={
                "startAt": start_at,
                "maxResults": 50,
                "fields": fields,
                "expand": "changelog",
            },
        )
        batch = payload.get("issues") or []
        issues.extend(batch)
        total = payload.get("total", 0)
        if not batch or len(issues) >= total:
            break
        start_at += len(batch)
    return issues


def backfill_changelog(client, issue):
    """El expand=changelog viene paginado; completa el historial si quedó truncado."""
    changelog = issue.get("changelog") or {}
    histories = changelog.get("histories") or []
    total = changelog.get("total", len(histories))
    if total <= len(histories):
        return histories

    full = client.paginate(
        f"/rest/api/3/issue/{issue['key']}/changelog",
        items_key="values",
        page_size=100,
    )
    return full or histories


def normalize_issue(issue, story_points_field, flagged_field):
    fields = issue.get("fields") or {}
    status = fields.get("status") or {}
    status_category = (status.get("statusCategory") or {}).get("name")
    issue_type = fields.get("issuetype") or {}
    assignee = fields.get("assignee") or {}
    parent = fields.get("parent") or {}
    flagged_value = fields.get(flagged_field) if flagged_field else None

    return {
        "key": issue.get("key"),
        "id": issue.get("id"),
        "summary": fields.get("summary") or "",
        "description": adf_to_text(fields.get("description")).strip(),
        "status": status.get("name"),
        "statusCategory": status_category,
        "issueType": issue_type.get("name"),
        "isSubtask": bool(issue_type.get("subtask")),
        "assignee": assignee.get("displayName"),
        "assigneeAccountId": assignee.get("accountId"),
        "reporter": (fields.get("reporter") or {}).get("displayName"),
        "priority": (fields.get("priority") or {}).get("name"),
        "storyPoints": fields.get(story_points_field) if story_points_field else None,
        "parentKey": parent.get("key"),
        "parentSummary": (parent.get("fields") or {}).get("summary"),
        "subtaskKeys": [s.get("key") for s in (fields.get("subtasks") or [])],
        "labels": fields.get("labels") or [],
        "components": [c.get("name") for c in (fields.get("components") or [])],
        "created": fields.get("created"),
        "updated": fields.get("updated"),
        "resolutionDate": fields.get("resolutiondate"),
        "dueDate": fields.get("duedate"),
        "originalEstimateSeconds": fields.get("timeoriginalestimate"),
        "flagged": bool(flagged_value),
        "changelog": issue.get("_changelog") or [],
    }


def fetch_scope_changes(client, board_id, sprint_id):
    """Sprint report de Greenhopper: única fuente de issues agregados/removidos del sprint."""
    payload = client.get_optional(
        "/rest/greenhopper/1.0/rapid/charts/sprintreport",
        params={"rapidViewId": board_id, "sprintId": sprint_id},
    )
    if not payload:
        return {"available": False, "addedDuringSprint": [], "punted": [], "completed": []}

    contents = payload.get("contents") or {}
    added = contents.get("issueKeysAddedDuringSprint") or {}
    return {
        "available": True,
        "addedDuringSprint": sorted(added.keys()) if isinstance(added, dict) else [],
        "punted": [i.get("key") for i in (contents.get("puntedIssues") or [])],
        "completed": [i.get("key") for i in (contents.get("completedIssues") or [])],
        "notCompleted": [i.get("key") for i in (contents.get("issuesNotCompletedInCurrentSprint") or [])],
    }


def main():
    parser = argparse.ArgumentParser(description="Descarga datos del sprint activo desde Jira")
    parser.add_argument("--board-id", type=int, help="ID del tablero Scrum")
    parser.add_argument("--sprint-id", type=int, default=None, help="Sprint puntual (default: activo)")
    parser.add_argument("--config", default=None, help="Ruta a config.json")
    parser.add_argument("-o", "--output", required=True, help="Archivo JSON de salida")
    args = parser.parse_args()

    config = load_config(args.config)
    board_id = args.board_id or config.get("board_id")
    if not board_id:
        fail("Indicá --board-id o definí board_id en config.json")

    try:
        client = JiraClient()
    except JiraError as exc:
        fail(str(exc))

    print("Resolviendo campos personalizados...", file=sys.stderr)
    field_map = client.discover_fields()
    story_points_field = resolve_field_id(field_map, STORY_POINT_FIELD_NAMES)
    flagged_field = resolve_field_id(field_map, FLAGGED_FIELD_NAMES)
    sprint_field = resolve_field_id(field_map, SPRINT_FIELD_NAMES)
    if not story_points_field:
        print("AVISO: no se encontró el campo de story points.", file=sys.stderr)

    extra_fields = [f for f in (story_points_field, flagged_field, sprint_field) if f]

    sprint = pick_active_sprint(client, board_id, args.sprint_id)
    print(f"Sprint: {sprint.get('name')} (id {sprint.get('id')})", file=sys.stderr)

    raw_issues = fetch_sprint_issues(client, sprint["id"], extra_fields)
    print(f"Issues en el sprint: {len(raw_issues)}", file=sys.stderr)

    for index, issue in enumerate(raw_issues, start=1):
        issue["_changelog"] = backfill_changelog(client, issue)
        if index % 25 == 0:
            print(f"  changelog {index}/{len(raw_issues)}", file=sys.stderr)

    issues = [normalize_issue(i, story_points_field, flagged_field) for i in raw_issues]
    scope = fetch_scope_changes(client, board_id, sprint["id"])

    payload = {
        "generatedAt": __import__("datetime").datetime.now().astimezone().isoformat(),
        "boardId": board_id,
        "sprint": {
            "id": sprint.get("id"),
            "name": sprint.get("name"),
            "state": sprint.get("state"),
            "startDate": sprint.get("startDate"),
            "endDate": sprint.get("endDate"),
            "completeDate": sprint.get("completeDate"),
            "goal": sprint.get("goal") or "",
        },
        "fieldIds": {
            "storyPoints": story_points_field,
            "flagged": flagged_field,
            "sprint": sprint_field,
        },
        "scopeChanges": scope,
        "issues": issues,
    }

    output = pathlib.Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK -> {output}", file=sys.stderr)


if __name__ == "__main__":
    main()
