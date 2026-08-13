#!/usr/bin/env python3
"""Parse OPUS5 Confirming MD into jira-load items (Phase 0)."""
from __future__ import annotations

import json
import re
from pathlib import Path

SRC = Path(
    r"C:\Users\mariana.ybanez\Projects\AI-Guideline\AI-Outputs\po-expert-user-stories\OPUS5-historias-usuario-confirming_v1.0.0.md"
)
OUT = Path(
    r"C:\Users\mariana.ybanez\Projects\AI-Guideline\AI-Outputs\jira-load-user-stories\jira-load-2026-08-13-confirming-parsed.json"
)

EPIC_MAP = {
    "FAC": "MAGIA-347",
    "CON": "MAGIA-346",
    "SIM": "MAGIA-348",
    "TAR": "MAGIA-346",  # transversal → épica Confirming (CON)
}

HEADING_RE = re.compile(
    r"^###\s+((?:FAC|CON|SIM)-[0-9]+(?:\.[0-9]+)?[a-z]?)\s+[—–-]\s+(.+?)\s*$",
    re.M,
)
TAR_ROW_RE = re.compile(
    r"^\|\s*`?(TAR-C\d+)`?\s*\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$",
    re.M,
)

META_SKIP = re.compile(
    r"metadatos y alcance|chequeo invest|^identificaci[oó]n",
    re.I,
)


def epic_for(temp_id: str) -> str:
    prefix = temp_id.split("-")[0]
    return EPIC_MAP[prefix]


def issue_type_from_block(block: str, temp_id: str) -> str:
    m = re.search(r"\|\s*\*\*Tipo\*\*\s*\|\s*([^|]+)\|", block)
    tipo = (m.group(1).strip() if m else "").lower()
    # Proyecto MAGIA usa nombres en español
    if temp_id.startswith("TAR"):
        return "Tarea"
    if "tarea" in tipo or "task" in tipo:
        return "Tarea"
    return "Historia"  # HU-FE y HT (enabler)


def clean_summary(title: str) -> str:
    # remove leading temp codes / issue keys if any slipped in
    t = title.strip()
    t = re.sub(r"^(?:FAC|CON|SIM|TAR|HU|HT|TA)-[A-Z0-9.]+[a-z]?\s*[—–:-]\s*", "", t)
    t = re.sub(r"\bMAGIA-\d+\b", "", t).strip(" -—–")
    # Normalize middle-dot titles for HT: keep functional text
    return t.strip()


def extract_body(block: str, kind: str) -> str:
    """Build Description body without metadata table / INVEST."""
    lines = block.splitlines()
    # drop heading line
    if lines and lines[0].startswith("###"):
        lines = lines[1:]

    # Drop metadata table at start (pipe table until blank after)
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].strip().startswith("|"):
        while i < len(lines) and (lines[i].strip().startswith("|") or not lines[i].strip()):
            # stop after table ends (blank following non-pipe already handled)
            if not lines[i].strip():
                # peek: if next is still table continue else break after blank
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and lines[j].strip().startswith("|"):
                    i = j
                    continue
                i += 1
                break
            i += 1

    rest = "\n".join(lines[i:]).strip()

    # Remove INVEST section
    rest = re.split(r"\n####\s+Chequeo INVEST\b", rest, maxsplit=1, flags=re.I)[0].strip()

    # Prefer from #### Historia / Objetivo técnico
    for marker in (
        r"####\s+Historia\b",
        r"####\s+Objetivo t[eé]cnico\b",
        r"(?m)^Como\b",
        r"(?m)^COMO\b",
    ):
        m = re.search(marker, rest, flags=re.I)
        if m:
            rest = rest[m.start() :].strip()
            break

    # Normalize Como/quiero/para → COMO/QUIERO/PARA for Jira consistency
    rest = re.sub(r"(?m)^####\s+Historia\s*$", "", rest).lstrip()
    rest = re.sub(r"(?m)^Como\b", "COMO", rest)
    rest = re.sub(r"(?m)^quiero\b", "QUIERO", rest)
    rest = re.sub(r"(?m)^para\b", "PARA", rest)

    # For HT: keep Objetivo técnico heading as context
    if kind == "ht" and not re.match(r"(?i)^(COMO|Como)", rest):
        if not rest.lower().startswith("#### objetivo"):
            # already may start with #### Objetivo
            pass

    # Strip trailing horizontal rules
    rest = re.sub(r"\n---+\s*$", "", rest).strip()
    return rest


def parse_cards(text: str) -> list[dict]:
    # Only sections 7 and 8 (stories), not TOC etc. Cut before §9 tasks table handled separately
    cut = re.search(r"^##\s+9\.\s+Tareas t[eé]cnicas", text, flags=re.M)
    main = text[: cut.start()] if cut else text

    matches = list(HEADING_RE.finditer(main))
    items = []
    for idx, m in enumerate(matches):
        temp_id = m.group(1)
        title = m.group(2).strip()
        start = m.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(main)
        block = main[start:end]
        itype = issue_type_from_block(block, temp_id)
        tipo_m = re.search(r"\|\s*\*\*Tipo\*\*\s*\|\s*([^|]+)\|", block)
        tipo_raw = tipo_m.group(1).strip() if tipo_m else ""
        kind = "ht" if "ht" in tipo_raw.lower() or "enabler" in tipo_raw.lower() else "hu"
        # Section 8 headings are HT even if table says HT
        if re.search(r"^##\s+8\.\s", main[:start], flags=re.M):
            # crude: if after section 8 header
            sec8 = re.search(r"^##\s+8\.\s", main, flags=re.M)
            if sec8 and start >= sec8.start():
                kind = "ht"
                itype = "Historia"

        body = extract_body(block, kind)
        items.append(
            {
                "temp_id": temp_id,
                "summary": clean_summary(title),
                "issue_type": itype,
                "epic_key": epic_for(temp_id),
                "kind": kind,
                "description": body,
            }
        )
    return items


def parse_tasks(text: str) -> list[dict]:
    sec = re.search(
        r"^##\s+9\.\s+Tareas t[eé]cnicas.*?(?=^##\s+10\.|\Z)",
        text,
        flags=re.M | re.S,
    )
    if not sec:
        return []
    items = []
    row_re = re.compile(
        r"^\|\s*`?(TAR-C\d+)`?\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$",
        re.M,
    )
    for m in row_re.finditer(sec.group(0)):
        temp_id = m.group(1)
        if temp_id == "ID":
            continue
        raw_title = m.group(2).strip()
        if raw_title.startswith("---") or raw_title.lower() == "tarea":
            continue
        title = re.sub(r"^\*\*|\*\*$", "", raw_title)
        title = re.sub(r"^\*\*(.+?)\*\*", r"\1", raw_title).strip()
        # Prefer bold lead as short summary
        bm = re.match(r"^\*\*(.+?)\*\*\s*:?\s*(.*)$", raw_title)
        if bm:
            summary = bm.group(1).strip()
            detail = (bm.group(1) + (": " + bm.group(2) if bm.group(2).strip() else "")).strip()
        else:
            summary = title.split(":")[0].strip()
            detail = title
        why = m.group(3).strip()
        impacts = m.group(4).strip()
        desc = (
            f"COMO equipo de Confirming\n"
            f"QUIERO {summary[0].lower() + summary[1:] if summary else summary}\n"
            f"PARA habilitar las historias impactadas sin bloqueos técnicos.\n\n"
            f"#### Detalle\n{detail}\n\n"
            f"#### Necesidad\n{why}\n\n"
            f"#### Historias impactadas\n{impacts}\n"
        )
        items.append(
            {
                "temp_id": temp_id,
                "summary": clean_summary(summary),
                "issue_type": "Tarea",
                "epic_key": epic_for(temp_id),
                "kind": "task",
                "description": desc,
            }
        )
    return items


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    items = parse_cards(text) + parse_tasks(text)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"source": str(SRC), "items": items}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(items)} items -> {OUT}")
    by_epic: dict[str, int] = {}
    by_type: dict[str, int] = {}
    for it in items:
        by_epic[it["epic_key"]] = by_epic.get(it["epic_key"], 0) + 1
        by_type[it["issue_type"]] = by_type.get(it["issue_type"], 0) + 1
    print("by epic:", by_epic)
    print("by type:", by_type)
    for it in items:
        first = next((ln for ln in it["description"].splitlines() if ln.strip()), "")
        print(
            f"  {it['temp_id']:10} -> {it['epic_key']} | {it['issue_type']:5} | "
            f"{it['summary'][:60]!r} | body0={first[:50]!r}"
        )


if __name__ == "__main__":
    main()
