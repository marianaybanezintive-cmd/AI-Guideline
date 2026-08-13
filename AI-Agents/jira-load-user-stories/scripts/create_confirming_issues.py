#!/usr/bin/env python3
"""Fase 1: crear issues Jira desde el JSON parseado (sin Description final)."""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from jira_rest import JiraError, JiraRest  # noqa: E402

PARSED = Path(
    r"C:\Users\mariana.ybanez\Projects\AI-Guideline\AI-Outputs\jira-load-user-stories\jira-load-2026-08-13-confirming-parsed.json"
)
MAP_OUT = Path(
    r"C:\Users\mariana.ybanez\Projects\AI-Guideline\AI-Outputs\jira-load-user-stories\jira-load-2026-08-13-confirming-map.json"
)
PLACEHOLDER = "Pendiente de descripción."


def create_issue(client: JiraRest, item: dict) -> str:
    fields = {
        "project": {"key": "MAGIA"},
        "issuetype": {"name": item["issue_type"]},
        "summary": item["summary"],
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": PLACEHOLDER}],
                }
            ],
        },
        # Team-managed parent + company-managed Epic Link
        "parent": {"key": item["epic_key"]},
        "customfield_10014": item["epic_key"],
    }
    data = client._request("POST", "/rest/api/3/issue", {"fields": fields})
    return data["key"]


def main() -> int:
    parsed = json.loads(PARSED.read_text(encoding="utf-8"))
    items = parsed["items"]
    client = JiraRest()
    results = []
    for i, item in enumerate(items, 1):
        temp = item["temp_id"]
        try:
            key = create_issue(client, item)
            print(f"OK  [{i}/{len(items)}] {temp} -> {key}")
            results.append({**item, "issue_key": key, "fase1": "ok", "error": None})
        except JiraError as exc:
            # retry without parent if parent fails (keep epic link)
            msg = str(exc)
            try:
                fields = {
                    "project": {"key": "MAGIA"},
                    "issuetype": {"name": item["issue_type"]},
                    "summary": item["summary"],
                    "description": {
                        "type": "doc",
                        "version": 1,
                        "content": [
                            {
                                "type": "paragraph",
                                "content": [{"type": "text", "text": PLACEHOLDER}],
                            }
                        ],
                    },
                    "customfield_10014": item["epic_key"],
                }
                data = client._request("POST", "/rest/api/3/issue", {"fields": fields})
                key = data["key"]
                print(f"OK* [{i}/{len(items)}] {temp} -> {key} (epic link only; parent failed: {msg[:120]})")
                results.append(
                    {
                        **item,
                        "issue_key": key,
                        "fase1": "ok_epic_link_only",
                        "error": msg[:300],
                    }
                )
            except JiraError as exc2:
                print(f"FAIL [{i}/{len(items)}] {temp}: {exc2}")
                results.append(
                    {
                        **item,
                        "issue_key": None,
                        "fase1": "fail",
                        "error": str(exc2)[:500],
                    }
                )
        time.sleep(0.35)

    MAP_OUT.write_text(json.dumps({"results": results}, ensure_ascii=False, indent=2), encoding="utf-8")
    ok = sum(1 for r in results if r.get("issue_key"))
    print(f"Done: {ok}/{len(results)} created. Map -> {MAP_OUT}")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
