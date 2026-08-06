#!/usr/bin/env python3
"""Reorder MAGIA-155 Backlog descriptions: drop CONTEXTO/metadatos; AC/Fuera/Notas after BDD."""

from __future__ import annotations

import base64
import json
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://bancoatlaspy.atlassian.net"
EMAIL = "mariana.ybanez@atlas.com.py"
MCP = pathlib.Path(r"C:\Users\mariana.ybanez\.cursor\mcp.json")
OUT = pathlib.Path(
    r"C:\Users\mariana.ybanez\OneDrive - intive\Desktop\atlas-confirming-poc\docs\architecture-output\_update-backlog-desc-result.json"
)


def auth_header() -> str:
    mcp = json.loads(MCP.read_text(encoding="utf-8"))
    token = mcp["mcpServers"]["jira"]["env"]["ATLASSIAN_API_TOKEN"]
    return "Basic " + base64.b64encode(f"{EMAIL}:{token}".encode()).decode()


def api(method: str, path: str, body: dict | None = None) -> dict:
    data = None if body is None else json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        BASE + path,
        data=data,
        method=method,
        headers={
            "Authorization": auth_header(),
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as r:
            raw = r.read().decode()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        err = e.read().decode(errors="replace")
        raise RuntimeError(f"{method} {path} -> {e.code}: {err}") from e


def node_text(node: dict) -> str:
    parts: list[str] = []

    def walk(n):
        if not isinstance(n, dict):
            return
        if n.get("type") == "text":
            parts.append(n.get("text") or "")
        elif n.get("type") == "hardBreak":
            parts.append("\n")
        for c in n.get("content") or []:
            walk(c)

    walk(node)
    return "".join(parts)


def strong_labels(node: dict) -> list[str]:
    labels = []
    for c in node.get("content") or []:
        if c.get("type") == "text" and any(
            m.get("type") == "strong" for m in (c.get("marks") or [])
        ):
            labels.append((c.get("text") or "").strip().rstrip(":"))
    return labels


def classify_section(node: dict) -> str | None:
    """Return section key if this node starts a known section."""
    t = node.get("type")
    if t != "paragraph":
        return None
    labels = [x.upper() for x in strong_labels(node)]
    text = node_text(node).strip()
    text_up = text.upper()

    if "DESCRIPCIÓN" in labels or text_up == "DESCRIPCIÓN" or text_up == "DESCRIPCION":
        return "descripcion"
    if "COMO" in labels and "QUIERO" in labels:
        return "connextra"
    if any(l.startswith("NECESIDAD") for l in labels) or text_up.startswith("NECESIDAD"):
        return "necesidad"
    if "ESCENARIOS" in labels and "BDD" not in text_up and "GHERKIN" not in text_up:
        # bare ESCENARIOS header (table follows)
        if text_up.strip() in {"ESCENARIOS", "*ESCENARIOS*"} or labels == ["ESCENARIOS"]:
            return "escenarios_header"
    if "CRITERIOS DE ACEPTACIÓN" in labels or "CRITERIOS DE ACEPTACION" in text_up.replace(
        "Ó", "O"
    ):
        return "criterios_header"
    if any(l.startswith("CRITERIO ") for l in labels) or re.match(
        r"(?i)^criterio\s+\d+", text
    ):
        return "criterio_item"
    if "FUERA DE ALCANCE" in labels or text_up.startswith("FUERA DE ALCANCE"):
        return "fuera_header"
    if "NOTAS" in text_up and "PREGUNTAS" in text_up:
        return "notas_header"
    if "ESCENARIOS BDD" in text_up or ("BDD" in text_up and "GHERKIN" in text_up):
        return "bdd_header"
    return None


def strip_contexto_from_necesidad(node: dict) -> dict:
    """Keep NECESIDAD text; drop CONTEXTO and anything after it in the same paragraph."""
    content = node.get("content") or []
    new_content = []
    i = 0
    while i < len(content):
        c = content[i]
        if c.get("type") == "text":
            raw = c.get("text") or ""
            # cut at CONTEXTO if embedded in same text node
            if re.search(r"CONTEXTO\s*:", raw, re.I):
                before = re.split(r"CONTEXTO\s*:", raw, maxsplit=1, flags=re.I)[0]
                before = before.rstrip()
                if before:
                    nc = dict(c)
                    nc["text"] = before + (" " if not before.endswith(" ") else "")
                    # ensure NECESIDAD strong preserved on first part only
                    new_content.append(nc)
                break
            marks = c.get("marks") or []
            is_strong = any(m.get("type") == "strong" for m in marks)
            if is_strong and re.match(r"(?i)^contexto\s*:?\s*$", raw.strip()):
                break
            new_content.append(c)
        elif c.get("type") == "hardBreak":
            # peek next for CONTEXTO
            nxt = content[i + 1] if i + 1 < len(content) else None
            if nxt and nxt.get("type") == "text":
                nt = (nxt.get("text") or "").strip()
                if re.match(r"(?i)^contexto\s*:?", nt):
                    break
            new_content.append(c)
        else:
            new_content.append(c)
        i += 1

    # trim trailing hardBreaks / spaces
    while new_content and new_content[-1].get("type") == "hardBreak":
        new_content.pop()
    if new_content and new_content[-1].get("type") == "text":
        new_content[-1] = dict(new_content[-1])
        new_content[-1]["text"] = (new_content[-1].get("text") or "").rstrip()

    out = dict(node)
    out["content"] = new_content
    return out


def is_metadata_bullet_list(node: dict) -> bool:
    if node.get("type") != "bulletList":
        return False
    text = node_text(node).lower()
    hits = sum(
        1
        for k in (
            "fuente:",
            "id excel:",
            "tipo:",
            "actor:",
            "dominios:",
            "prioridad sugerida:",
            "depende de:",
            "habilita:",
            "pantalla poc:",
            "contrato:",
            "objetivo técnico:",
            "key excel:",
        )
        if k in text
    )
    return hits >= 2


def transform_description(desc: dict) -> tuple[dict | None, str]:
    if not desc or desc.get("type") != "doc":
        return None, "no_doc"

    content = list(desc.get("content") or [])
    raw_json = json.dumps(desc, ensure_ascii=False)
    if "CONTEXTO" not in raw_json and "Metadatos" not in raw_json:
        # not our template — skip
        return None, "skip_no_template"

    # Partition into buckets while streaming
    buckets: dict[str, list] = {
        "preamble": [],  # descripcion + connextra + necesidad (cleaned)
        "escenarios": [],  # header + table (+ any loose scenario bits)
        "criterios": [],
        "fuera": [],
        "notas": [],
        "bdd": [],
        "other_tail": [],
    }

    mode = "preamble"
    i = 0
    skipped_meta_list = False

    while i < len(content):
        node = content[i]
        section = classify_section(node)

        # Drop metadata bullet list that follows NECESIDAD/CONTEXTO
        if is_metadata_bullet_list(node):
            skipped_meta_list = True
            i += 1
            continue

        if section == "necesidad":
            buckets["preamble"].append(strip_contexto_from_necesidad(node))
            mode = "preamble"
            i += 1
            continue

        if section == "descripcion" or section == "connextra":
            buckets["preamble"].append(node)
            mode = "preamble"
            i += 1
            continue

        if section == "escenarios_header":
            mode = "escenarios"
            buckets["escenarios"].append(node)
            i += 1
            # absorb following table
            if i < len(content) and content[i].get("type") == "table":
                buckets["escenarios"].append(content[i])
                i += 1
            continue

        if section == "criterios_header":
            mode = "criterios"
            buckets["criterios"].append(node)
            i += 1
            continue

        if section == "criterio_item":
            mode = "criterios"
            buckets["criterios"].append(node)
            i += 1
            continue

        if section == "fuera_header":
            mode = "fuera"
            buckets["fuera"].append(node)
            i += 1
            continue

        if section == "notas_header":
            mode = "notas"
            buckets["notas"].append(node)
            i += 1
            continue

        if section == "bdd_header":
            mode = "bdd"
            buckets["bdd"].append(node)
            i += 1
            # absorb following codeBlock
            if i < len(content) and content[i].get("type") == "codeBlock":
                buckets["bdd"].append(content[i])
                i += 1
            continue

        # continuation nodes for current mode
        if mode == "preamble":
            # stray nodes before escenarios — keep unless empty paragraph
            if node.get("type") == "paragraph" and not node_text(node).strip():
                i += 1
                continue
            buckets["preamble"].append(node)
        elif mode == "escenarios":
            buckets["escenarios"].append(node)
        elif mode == "criterios":
            buckets["criterios"].append(node)
        elif mode == "fuera":
            buckets["fuera"].append(node)
        elif mode == "notas":
            buckets["notas"].append(node)
        elif mode == "bdd":
            buckets["bdd"].append(node)
        else:
            buckets["other_tail"].append(node)
        i += 1

    # Rebuild: preamble → escenarios → bdd → criterios → fuera → notas → other
    new_content: list = []
    new_content.extend(buckets["preamble"])
    new_content.extend(buckets["escenarios"])
    new_content.extend(buckets["bdd"])
    new_content.extend(buckets["criterios"])
    new_content.extend(buckets["fuera"])
    new_content.extend(buckets["notas"])
    new_content.extend(buckets["other_tail"])

    if not new_content:
        return None, "empty_result"

    new_desc = {"type": "doc", "version": 1, "content": new_content}
    note = "updated"
    if skipped_meta_list:
        note += "+dropped_meta_list"
    if buckets["bdd"]:
        note += "+bdd_before_ac"
    else:
        note += "+no_bdd"
    return new_desc, note


def list_backlog_issues() -> list[dict]:
    jql = urllib.parse.quote('parent = MAGIA-155 AND status = Backlog ORDER BY key ASC')
    issues: list[dict] = []
    start = 0
    while True:
        data = api(
            "GET",
            f"/rest/api/3/search/jql?jql={jql}&maxResults=50"
            f"&fields=summary,status,issuetype,description&startAt={start}",
        )
        batch = data.get("issues", [])
        issues.extend(batch)
        total = data.get("total")
        if total is not None:
            if start + len(batch) >= total or not batch:
                break
            start += len(batch)
        else:
            if data.get("isLast", True) or not batch:
                break
            start += len(batch)
    return issues


def verify_order(desc: dict) -> dict:
    """Return positions of key sections for verification."""
    pos = {}
    for idx, node in enumerate(desc.get("content") or []):
        sec = classify_section(node)
        if sec and sec not in pos:
            pos[sec] = idx
        if node.get("type") == "codeBlock" and "bdd_code" not in pos:
            # code after bdd header
            if "bdd_header" in pos:
                pos["bdd_code"] = idx
    return pos


def main() -> None:
    issues = list_backlog_issues()
    results = []
    for issue in issues:
        key = issue["key"]
        summary = issue["fields"].get("summary") or ""
        desc = issue["fields"].get("description")
        new_desc, note = transform_description(desc)
        if new_desc is None:
            results.append(
                {
                    "key": key,
                    "summary": summary,
                    "action": "skipped",
                    "reason": note,
                }
            )
            print(f"SKIP {key}: {note}")
            continue

        api("PUT", f"/rest/api/3/issue/{key}", {"fields": {"description": new_desc}})
        # re-fetch verify
        time.sleep(0.2)
        fresh = api("GET", f"/rest/api/3/issue/{key}?fields=description")
        fdesc = fresh["fields"]["description"]
        fjson = json.dumps(fdesc, ensure_ascii=False)
        positions = verify_order(fdesc)
        ok_no_meta = "Metadatos y alcance" not in fjson and (
            "CONTEXTO" not in fjson
            or "CONTEXTO" not in fjson.split("NECESIDAD")[-1][:80]
            if "NECESIDAD" in fjson
            else "CONTEXTO" not in fjson
        )
        # simpler checks
        has_contexto_label = bool(re.search(r'"text"\s*:\s*"CONTEXTO', fjson))
        has_metadatos = "Metadatos y alcance" in fjson
        bdd_pos = positions.get("bdd_header")
        ac_pos = positions.get("criterios_header")
        order_ok = True
        if bdd_pos is not None and ac_pos is not None:
            order_ok = bdd_pos < ac_pos

        results.append(
            {
                "key": key,
                "summary": summary,
                "action": "updated",
                "note": note,
                "has_contexto_label": has_contexto_label,
                "has_metadatos": has_metadatos,
                "order_ok": order_ok,
                "positions": positions,
            }
        )
        print(
            f"OK {key}: {note} | contexto={has_contexto_label} meta={has_metadatos} order_ok={order_ok}"
        )
        time.sleep(0.15)

    OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    updated = sum(1 for r in results if r["action"] == "updated")
    skipped = sum(1 for r in results if r["action"] == "skipped")
    print(f"Done updated={updated} skipped={skipped} -> {OUT}")


if __name__ == "__main__":
    main()
