#!/usr/bin/env python3
"""Build Phase-2 payload: replace temp IDs with Issue Keys in descriptions."""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

MAP = Path(
    r"C:\Users\mariana.ybanez\Projects\AI-Guideline\AI-Outputs\jira-load-user-stories\jira-load-2026-08-13-confirming-map.json"
)
PAYLOAD = Path(
    r"C:\Users\mariana.ybanez\Projects\AI-Guideline\AI-Outputs\jira-load-user-stories\jira-load-2026-08-13-confirming-payload.json"
)


def replace_temp_ids(text: str, id_to_key: dict[str, str]) -> str:
    # Longest first to avoid FAC-01 eating FAC-01.1
    keys = sorted(id_to_key.keys(), key=len, reverse=True)
    out = text
    for tid in keys:
        jira = id_to_key[tid]
        # word-ish boundary: not preceded/followed by alnum or '.' that continues the id
        pattern = re.compile(rf"(?<![A-Za-z0-9.]){re.escape(tid)}(?![A-Za-z0-9.])")
        out = pattern.sub(jira, out)
    return out


def main() -> None:
    results = json.loads(MAP.read_text(encoding="utf-8"))["results"]
    id_to_key = {r["temp_id"]: r["issue_key"] for r in results if r.get("issue_key")}
    issues = []
    for r in results:
        if not r.get("issue_key"):
            continue
        desc = replace_temp_ids(r.get("description") or "", id_to_key)
        issues.append(
            {
                "issue_key": r["issue_key"],
                "temp_id": r["temp_id"],
                "epic_key": r["epic_key"],
                "issue_type": r["issue_type"],
                "summary": r["summary"],
                "description": desc,
            }
        )
    PAYLOAD.write_text(
        json.dumps(
            {
                "source_md": "AI-Outputs/po-expert-user-stories/OPUS5-historias-usuario-confirming_v1.0.0.md",
                "created_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "id_map": id_to_key,
                "issues": issues,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Payload {len(issues)} issues -> {PAYLOAD}")
    # sanity: first description starts with COMO or Objetivo
    sample = issues[0]["description"].splitlines()[0]
    print("sample0:", sample[:80])
    # check a replacement happened
    fac = next(i for i in issues if i["temp_id"] == "FAC-01.1")
    if "FAC-05a" in fac["description"] and id_to_key.get("FAC-05a"):
        print("WARN: FAC-05a still present in FAC-01.1 body")
    elif id_to_key.get("FAC-05a") and id_to_key["FAC-05a"] in fac["description"]:
        print("OK: FAC-05a replaced by", id_to_key["FAC-05a"])


if __name__ == "__main__":
    main()
