"""Genera el informe Markdown del clonado masivo a partir de last-run.json.

Uso:
  python render_report.py AI-Outputs/sm-mass-clone/last-run.json -o "AI-Outputs/sm-mass-clone/20260406-clone-report.md"
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


def esc(value) -> str:
    if value is None:
        return "—"
    text = str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")
    return text.strip() or "—"


def short(text, limit=80) -> str:
    text = (text or "").strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"


def md_link(key: str | None, url: str | None) -> str:
    if not key:
        return "—"
    if url:
        return f"[{key}]({url})"
    return key


def fmt_sprint(ids) -> str:
    if not ids:
        return "Backlog"
    return ", ".join(str(i) for i in ids)


def render(payload: dict) -> str:
    filters = payload.get("filters") or {}
    counts = payload.get("counts") or {}
    config = payload.get("config") or {}
    results = payload.get("results") or []
    dry = payload.get("dry_run")
    generated = payload.get("generated_at") or ""
    try:
        generated_local = datetime.fromisoformat(generated.replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M UTC")
    except ValueError:
        generated_local = generated or "—"

    project = config.get("project_key") or "—"
    base = (config.get("jira_base_url") or "").rstrip("/")

    lines = [
        f"# SM Mass Clone — Reporte ({project})",
        "",
        f"_Generado: {generated_local}_",
        "",
        "## Resumen",
        "",
        f"- **Modo:** {'dry-run (sin clonar)' if dry else 'clonado real'}",
        f"- **Origen:** `{filters.get('origin_type')}` = `{filters.get('origin_value') or '—'}`",
        f"- **Tipo:** `{filters.get('issue_type')}` → {filters.get('issue_types_resolved')}",
        f"- **Estado:** `{filters.get('status')}` → {filters.get('statuses_resolved')}",
        f"- **Nomenclatura título:** `{filters.get('title_prefix') or '(sin prefijo)'}`",
        f"- **Asignado:** {filters.get('assignee') or '— (sin asignar)'}",
        f"- **JQL:** `{filters.get('jql')}`",
        "",
        "## Conteos",
        "",
        f"| Métrica | Valor |",
        f"|---------|-------|",
        f"| Matched (JQL) | {counts.get('matched', 0)} |",
        f"| Candidatos | {counts.get('candidates', 0)} |",
        f"| Omitidos (ya tenían prefijo) | {counts.get('skipped_prefix', 0)} |",
        f"| OK | {counts.get('ok', 0)} |",
        f"| Fail | {counts.get('fail', 0)} |",
        "",
    ]

    skipped = payload.get("skipped_keys") or []
    if skipped:
        lines.append("### Omitidos por nomenclatura")
        lines.append("")
        lines.append(", ".join(f"`{k}`" for k in skipped))
        lines.append("")

    lines.extend(
        [
            "## Relación original → clonado",
            "",
            "| Original | Título original | Clonado | Título clonado | Sprint | Asignado | Resultado |",
            "|----------|-----------------|---------|----------------|--------|----------|-----------|",
        ]
    )

    for row in results:
        orig_key = row.get("original_key")
        clone_key = row.get("clone_key")
        orig_url = row.get("original_url") or (f"{base}/browse/{orig_key}" if base and orig_key else None)
        clone_url = row.get("clone_url") or (f"{base}/browse/{clone_key}" if base and clone_key else None)
        status = "dry-run" if row.get("dry_run") else ("OK" if row.get("ok") else f"FAIL: {short(row.get('error') or '', 60)}")
        lines.append(
            "| "
            + " | ".join(
                [
                    md_link(orig_key, orig_url),
                    esc(short(row.get("original_summary"), 60)),
                    md_link(clone_key, clone_url) if clone_key else "—",
                    esc(short(row.get("clone_summary"), 60)),
                    esc(fmt_sprint(row.get("sprint_ids"))),
                    esc(row.get("assignee")),
                    esc(status),
                ]
            )
            + " |"
        )

    if not results:
        lines.append("| — | — | — | — | — | — | Sin candidatos |")

    lines.extend(
        [
            "",
            "## Criterios aplicados",
            "",
            "- Descripción copiada del original (ADF).",
            "- Principal = parent del original.",
            "- Vínculo tipo Relacionar: clon *está relacionado a* original.",
            "- Sprint del original reutilizado; si no había → backlog.",
            "- Issues cuyo título ya empezaba con la nomenclatura no se reclonan.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Renderiza reporte MD de sm-mass-clone")
    parser.add_argument("input", help="JSON de resultado (last-run.json)")
    parser.add_argument("-o", "--output", required=True, help="Ruta del .md de salida")
    args = parser.parse_args()

    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    md = render(payload)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    print(f"Reporte: {out}")


if __name__ == "__main__":
    main()
