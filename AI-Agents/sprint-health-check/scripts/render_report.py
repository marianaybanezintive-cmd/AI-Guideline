"""Genera el informe Markdown de salud del sprint a partir de metrics.json.

Uso:
    python render_report.py out/metrics.json -o "Sprint 4 - Health Check.md"
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
import pathlib
import sys

BUCKET_LABEL = {
    "todo": "Por hacer",
    "in_progress": "En curso",
    "qa": "En QA",
    "done": "Finalizado",
    "cancelled": "Cancelado",
}


def esc(value):
    """Escapa el contenido de una celda de tabla Markdown."""
    if value is None:
        return "—"
    text = str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")
    return text.strip() or "—"


def num(value, suffix=""):
    if value is None:
        return "—"
    if isinstance(value, float) and value.is_integer():
        value = int(value)
    return f"{value}{suffix}"


def short(text, limit=70):
    text = (text or "").strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"


def fmt_date(value, with_time=False):
    if not value:
        return "—"
    try:
        parsed = dt.datetime.fromisoformat(str(value))
    except ValueError:
        return str(value)[:10]
    return parsed.strftime("%d/%m %H:%M") if with_time else parsed.strftime("%d/%m/%Y")


def table(headers, rows):
    if not rows:
        return "_Sin registros._\n"
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    out.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(out) + "\n"


def link(key, base_url):
    return f"[{key}]({base_url}/browse/{key})" if base_url else key


def diff_summary(before, after):
    """Resume el cambio de descripción: líneas agregadas y quitadas."""
    before_lines = [l.strip() for l in (before or "").splitlines() if l.strip()]
    after_lines = [l.strip() for l in (after or "").splitlines() if l.strip()]
    added, removed = [], []
    for line in difflib.unified_diff(before_lines, after_lines, lineterm="", n=0):
        if line.startswith("+") and not line.startswith("+++"):
            added.append(line[1:].strip())
        elif line.startswith("-") and not line.startswith("---"):
            removed.append(line[1:].strip())
    return added, removed


class ReportRenderer:
    def __init__(self, metrics, config):
        self.m = metrics
        self.base_url = (config.get("jira_base_url") or "").rstrip("/")
        self.config = config

    def k(self, key):
        return link(key, self.base_url)

    # ---------- encabezado ----------

    def header(self):
        s = self.m["sprintStatus"]
        h = self.m["health"]
        generated = fmt_date(self.m.get("generatedAt"), with_time=True)
        lines = [
            f"# Sprint Health Check — {s.get('name')}",
            "",
            f"**Estado general: {h['verdict']}**",
            "",
            f"- Periodo: {fmt_date(s.get('startDate'))} → {fmt_date(s.get('endDate'))}  "
            f"({s.get('elapsedDays')} de {s.get('totalDays')} días transcurridos, "
            f"{num(s.get('timeElapsedPct'), '%')} del tiempo)",
            f"- Días hábiles: {s.get('workingDaysElapsed')} de {s.get('workingDaysTotal')} — "
            f"restan {num(s.get('remainingDays'))} días corridos",
            f"- Avance: {num(s.get('donePoints'))} de {num(s.get('totalPoints'))} pts "
            f"({num(s.get('completionPctByPoints'), '%')}) — "
            f"{s.get('parentsByBucket', {}).get('done', 0)} de {s.get('activeParents')} ítems principales "
            f"({num(s.get('completionPctByCount'), '%')})",
            f"- Alcance: {s.get('totalParents')} ítems principales + {s.get('totalSubtasks')} subtareas"
            + (f" — {num(s.get('cancelledPoints'))} pts cancelados, excluidos del total"
               if s.get("cancelledPoints") else ""),
            f"- Informe generado: {generated}",
            "",
        ]

        if h["signals"]:
            lines.append("## Señales de riesgo detectadas")
            lines.append("")
            for signal in h["signals"]:
                lines.append(f"- **[{signal['level'].upper()}]** {signal['text']}")
            lines.append("")
        else:
            lines.append("_Sin señales de riesgo detectadas._\n")
        return "\n".join(lines)

    # ---------- 1 ----------

    def sprint_status(self):
        s = self.m["sprintStatus"]
        rows = [[esc(status), str(count)] for status, count in
                sorted(s.get("parentsByStatus", {}).items(), key=lambda kv: -kv[1])]
        sub_rows = [[esc(status), str(count)] for status, count in
                    sorted(s.get("issuesByStatus", {}).items(), key=lambda kv: -kv[1])]

        pace = ""
        time_pct, done_pct = s.get("timeElapsedPct"), s.get("completionPctByPoints")
        if time_pct is not None and done_pct is not None:
            delta = round(done_pct - time_pct, 1)
            pace = (f"\nEl sprint consumió **{time_pct}%** del tiempo y completó **{done_pct}%** de los puntos "
                    f"(**{delta:+} pp** respecto del ritmo lineal esperado).\n")

        return ("\n## 1. Estado actual del sprint\n" + pace +
                "\n**Ítems principales por estado**\n\n" + table(["Estado", "Ítems"], rows) +
                "\n**Todos los ítems (incluye subtareas)**\n\n" + table(["Estado", "Ítems"], sub_rows))

    # ---------- 2 ----------

    def parent_progress(self):
        rows = []
        for r in self.m["parentProgress"]:
            subtasks = (f"{r['subtaskDone']}/{r['subtaskTotal']} ({r['subtaskPct']}%)"
                        if r["subtaskTotal"] else "—")
            rows.append([
                self.k(r["key"]), esc(short(r["summary"])), esc(r["status"]),
                esc(r["assignee"]), num(r["points"]), subtasks, num(r["daysInStatus"]),
            ])
        return ("\n## 2. Avance de historias y tareas principales\n\n" +
                table(["Clave", "Resumen", "Estado", "Asignado", "Pts", "Subtareas", "Días en estado"], rows))

    # ---------- 3 ----------

    def stale(self):
        data = self.m["stale"]
        rows = []
        for r in data["items"]:
            rows.append([
                self.k(r["key"]), esc(short(r["summary"], 55)),
                "Subtarea" if r["isSubtask"] else esc(r["issueType"]),
                esc(r["status"]), esc(r["assignee"]),
                f"**{num(r['daysInStatus'])}**", num(r["daysSinceUpdate"]),
                "Nunca se movió" if r["neverMoved"] else fmt_date(r["lastStatusChange"]),
            ])
        intro = (f"\n## 3. Ítems sin cambio de estado (≥ {data['thresholdDays']} días)\n\n"
                 f"Se mide desde la **última transición de estado** registrada en el historial, "
                 f"no desde la última edición del ticket.\n\n")
        return intro + table(
            ["Clave", "Resumen", "Tipo", "Estado", "Asignado", "Días en estado", "Días sin editar", "Último cambio"],
            rows)

    # ---------- 4 ----------

    def missing_estimate(self):
        rows = [[self.k(r["key"]), esc(short(r["summary"])), esc(r["issueType"]),
                 esc(r["status"]), esc(r["assignee"])] for r in self.m["missingEstimate"]]
        return (f"\n## 4. Ítems sin estimación ({len(rows)})\n\n" +
                table(["Clave", "Resumen", "Tipo", "Estado", "Asignado"], rows))

    # ---------- 5 ----------

    def missing_assignee(self):
        rows = [[self.k(r["key"]), esc(short(r["summary"])),
                 "Subtarea" if r["isSubtask"] else esc(r["issueType"]),
                 esc(r["status"])] for r in self.m["missingAssignee"]]
        return (f"\n## 5. Ítems sin asignación ({len(rows)})\n\n" +
                table(["Clave", "Resumen", "Tipo", "Estado"], rows))

    # ---------- 6 ----------

    def points_by_assignee(self):
        rows = []
        for r in self.m["pointsByAssignee"]:
            rows.append([
                esc(r["assignee"]), str(r["issues"]), num(r["totalPoints"]),
                num(r["donePoints"]), num(r["qaPoints"]), num(r["inProgressPoints"]),
                num(r["todoPoints"]), num(r["completionPct"], "%"), str(r["unestimatedIssues"]),
            ])
        return ("\n## 6. Puntos de historia por persona asignada\n\n" +
                "Sólo ítems principales (las subtareas no llevan estimación).\n\n" +
                table(["Persona", "Ítems", "Pts total", "Pts hechos", "Pts en QA",
                       "Pts en curso", "Pts por hacer", "% completado", "Sin estimar"], rows))

    # ---------- 7 ----------

    def daily_progress(self):
        data = self.m["dailyProgress"]
        days = data["days"]
        if not days:
            return "\n## 7. Evolución del avance por persona y día\n\n_Sin datos._\n"

        labels = [dt.date.fromisoformat(d).strftime("%d/%m") for d in days]
        headers = ["Persona"] + labels + ["Total"]

        points_rows = []
        items_rows = []
        for r in data["byAssignee"]:
            points_rows.append([esc(r["assignee"])] +
                               [num(v) if v else "·" for v in r["dailyPoints"]] +
                               [f"**{num(r['totalPoints'])}**"])
            items_rows.append([esc(r["assignee"])] +
                              [str(v) if v else "·" for v in r["dailyItems"]] +
                              [f"**{r['totalItems']}**"])

        cumulative_rows = []
        for r in data["byAssignee"]:
            cumulative_rows.append([esc(r["assignee"])] + [num(v) for v in r["cumulativePoints"]])

        return ("\n## 7. Evolución del avance por persona y día\n\n"
                "Cuenta sólo el trabajo que sigue cerrado hoy, en la fecha de su último cierre; "
                "lo reabierto no suma.\n\n"
                "**Puntos completados por día** (fecha en que el ítem principal pasó a Finalizado)\n\n" +
                table(headers, points_rows) +
                "\n**Ítems cerrados por día** (incluye subtareas)\n\n" +
                table(headers, items_rows) +
                "\n**Puntos acumulados por persona**\n\n" +
                table(["Persona"] + labels, cumulative_rows))

    # ---------- 8 ----------

    def description_changes(self):
        rows = self.m["descriptionChanges"]
        out = [f"\n## 8. Historias que cambiaron de alcance ({len(rows)})\n",
               "Cambios en el campo *Description* posteriores al inicio del sprint.\n"]

        if not rows:
            out.append("_Sin cambios de descripción durante el sprint._\n")
            return "\n".join(out)

        summary_rows = [[
            self.k(r["key"]), esc(short(r["summary"], 45)), esc(r["status"]),
            fmt_date(r["changedAt"], with_time=True), esc(r["author"]),
            f"{r['deltaChars']:+} car.",
        ] for r in rows]
        out.append(table(["Clave", "Resumen", "Estado", "Modificado", "Autor", "Δ tamaño"], summary_rows))

        out.append("\n### Detalle antes / después\n")
        for r in rows:
            added, removed = diff_summary(r["beforeExcerpt"], r["afterExcerpt"])
            out.append(f"\n**{self.k(r['key'])} — {short(r['summary'], 80)}**  ")
            out.append(f"Modificado por {r['author']} el {fmt_date(r['changedAt'], with_time=True)} "
                       f"({r['beforeChars']} → {r['afterChars']} caracteres).\n")
            if removed:
                out.append("_Se quitó:_\n")
                out.extend(f"> - {short(line, 200)}" for line in removed[:6])
                out.append("")
            if added:
                out.append("_Se agregó:_\n")
                out.extend(f"> + {short(line, 200)}" for line in added[:6])
                out.append("")
            if not added and not removed:
                out.append("_Cambio menor de formato, sin variación de texto relevante._\n")
        return "\n".join(out)

    # ---------- 9 ----------

    def qa_analysis(self):
        rows = self.m["qaAnalysis"]
        out = [f"\n## 9. Consistencia de QA vs subtareas ({len(rows)} historias con hallazgos)\n",
               "Reglas verificadas: toda historia con subtarea de **desarrollo** debe tener "
               "**1 QA Automation** y **1 Ejecución de Tests**; ninguna historia en "
               "**Pruebas QA** debería tener subtareas de QA sin cerrar.\n"]

        if not rows:
            out.append("_Sin inconsistencias de QA detectadas._\n")
            return "\n".join(out)

        summary_rows = []
        for r in rows:
            counts = r["counts"]
            summary_rows.append([
                self.k(r["key"]), esc(short(r["summary"], 45)), esc(r["status"]),
                str(counts.get("dev", 0)), str(counts.get("qa_automation", 0)),
                str(counts.get("qa_execution", 0)),
                num(r["daysWaitingQa"]),
                esc("; ".join(r["findings"]) or "—"),
            ])
        out.append(table(["Clave", "Resumen", "Estado", "Dev", "QA Auto", "Ejec. Tests",
                          "Días esperando QA", "Hallazgos"], summary_rows))

        pending_rows = []
        for r in rows:
            for p in r["pendingQaSubtasks"]:
                pending_rows.append([
                    self.k(r["key"]), self.k(p["key"]), esc(short(p["summary"], 40)),
                    esc(p["family"]), esc(p["status"]), esc(p["assignee"]),
                    num(p["daysInStatus"]), num(p["daysSinceDevDone"]), num(p["daysSinceParentInQa"]),
                ])
        out.append("\n### Subtareas de QA pendientes y antigüedad\n")
        out.append("`Días desde dev` cuenta desde que se finalizó la última subtarea de desarrollo; "
                   "`Días en QA` desde que la historia principal pasó a Pruebas QA.\n")
        out.append(table(["Historia", "Subtarea", "Resumen", "Familia", "Estado", "Asignado",
                          "Días en estado", "Días desde dev", "Días en QA"], pending_rows))
        return "\n".join(out)

    # ---------- 10 ----------

    def goals(self):
        goals = self.m["goals"]
        out = ["\n## 10. Goals del sprint vs estado de las tareas\n",
               "Criterio de prioridad: **CRITICO** no debe caer del sprint · "
               "**ALTA** debe hacerse, tolerable que sólo caiga el QA · "
               "**MEDIA/BAJA** pueden caer.\n"]

        if not goals:
            out.append("_El sprint no tiene goals definidos._\n")
            return "\n".join(out)

        overview = [[
            esc(g["priority"]), esc(short(g["text"], 60)), esc(g["verdict"]),
            f"{g['counts'].get('done', 0)}/{len(g['issues'])}",
            num(g["completionPct"], "%"),
        ] for g in goals]
        out.append(table(["Prioridad", "Goal", "Veredicto", "Ítems hechos", "% pts"], overview))

        out.append("\n### Detalle por goal\n")
        for index, g in enumerate(goals, start=1):
            out.append(f"\n**{index}. [{g['priority']}] {g['text']}**  ")
            out.append(f"Veredicto: **{g['verdict']}** — "
                       f"{g['counts'].get('done', 0)} de {len(g['issues'])} ítems finalizados"
                       f"{'' if g['matchMethod'] == 'override' else ' (vinculación automática por palabras clave)'}\n")
            if not g["issues"]:
                out.append("_No se identificaron tickets asociados a este goal._\n")
                continue
            rows = [[self.k(i["key"]), esc(short(i["summary"], 60)), esc(i["status"]),
                     esc(i["assignee"]), num(i["points"])] for i in g["issues"]]
            out.append(table(["Clave", "Resumen", "Estado", "Asignado", "Pts"], rows))
        return "\n".join(out)

    # ---------- 11 ----------

    def burndown(self):
        b = self.m["burndown"]
        if not b.get("days"):
            return "\n## 11. Burndown y proyección de cierre\n\n_Sin datos._\n"

        rows = []
        for index, day in enumerate(b["days"]):
            actual = b["actual"][index]
            rows.append([
                dt.date.fromisoformat(day).strftime("%d/%m"),
                num(b["ideal"][index]),
                num(actual) if actual is not None else "—",
                num(round(actual - b["ideal"][index], 1)) if actual is not None else "—",
            ])

        verdict = ("El sprint **cierra completo** al ritmo actual."
                   if b.get("willFinish")
                   else f"Al ritmo actual **quedarían {num(b.get('projectedGap'))} pts sin cerrar**.")

        return ("\n## 11. Burndown y proyección de cierre\n\n"
                f"- Velocidad diaria observada: **{num(b.get('dailyVelocity'))} pts/día hábil**\n"
                f"- Completado: {num(b.get('completedPoints'))} de {num(b.get('totalPoints'))} pts\n"
                f"- Días hábiles restantes: {b.get('remainingWorkingDays')}\n"
                f"- Proyección de cierre: {num(b.get('projectedCompletion'))} pts\n"
                f"- {verdict}\n\n" +
                table(["Día", "Ideal (pts rest.)", "Real (pts rest.)", "Desvío"], rows))

    # ---------- 12 ----------

    def wip(self):
        w = self.m["wip"]
        wip_rows = [[
            esc(r["assignee"]), str(r["wipCount"]),
            "SOBRE LÍMITE" if r["overLimit"] else "OK",
            esc(", ".join(i["key"] for i in r["issues"])),
        ] for r in w["byAssignee"]]

        aging_rows = [[esc(r["status"]), str(r["count"]), num(r["avgDays"]), num(r["maxDays"])]
                      for r in w["agingByStatus"]]

        return (f"\n## 12. WIP por persona y cuellos de botella\n\n"
                f"Límite de WIP considerado: **{w['wipLimit']}** ítems simultáneos por persona.\n\n" +
                table(["Persona", "WIP", "Estado", "Ítems"], wip_rows) +
                "\n**Antigüedad promedio por estado (ítems abiertos)**\n\n" +
                table(["Estado", "Ítems", "Días promedio", "Días máximo"], aging_rows))

    # ---------- 13 ----------

    def scope_creep(self):
        s = self.m["scopeCreep"]
        rows = [[
            self.k(r["key"]), esc(short(r["summary"], 55)),
            "Subtarea" if r.get("isSubtask") else esc(r.get("issueType")),
            esc(r.get("status")), esc(r.get("assignee")), num(r.get("points")),
        ] for r in s["addedDuringSprint"]]

        removed = ", ".join(self.k(k) for k in s.get("removedFromSprint", [])) or "—"

        return ("\n## 13. Scope creep (alcance agregado durante el sprint)\n\n"
                f"- Fuente: {s['source']}\n"
                f"- Puntos de base al inicio: {num(s.get('baselinePoints'))}\n"
                f"- Puntos agregados: {num(s.get('addedPoints'))} "
                f"({num(s.get('scopeCreepPct'), '%')} sobre la base)\n"
                f"- Ítems removidos del sprint: {removed}\n\n" +
                table(["Clave", "Resumen", "Tipo", "Estado", "Asignado", "Pts"], rows))

    # ---------- 14 ----------

    def blockers(self):
        b = self.m["blockers"]
        flagged = [[self.k(r["key"]), esc(short(r["summary"])), esc(r["status"]),
                    esc(r["assignee"]), num(r["daysInStatus"])] for r in b["flagged"]]
        idle = [[self.k(r["key"]), esc(short(r["summary"])), esc(r["status"]),
                 esc(r["assignee"]), num(r["daysSinceUpdate"])] for r in b["idleInProgress"]]
        never = [[self.k(r["key"]), esc(short(r["summary"])), esc(r["assignee"]), num(r["points"])]
                 for r in b["neverStarted"]]

        return ("\n## 14. Bloqueantes e inactividad\n\n"
                "**Ítems marcados como bloqueados (flagged)**\n\n" +
                table(["Clave", "Resumen", "Estado", "Asignado", "Días en estado"], flagged) +
                f"\n**En curso sin actividad hace ≥ {b['idleThresholdDays']} días**\n\n" +
                table(["Clave", "Resumen", "Estado", "Asignado", "Días sin actividad"], idle) +
                "\n**Ítems principales que nunca se movieron del estado inicial**\n\n" +
                table(["Clave", "Resumen", "Asignado", "Pts"], never))

    # ---------- 15 ----------

    def quality(self):
        q = self.m["quality"]
        bugs = [[self.k(r["key"]), esc(short(r["summary"])), esc(r["status"]),
                 esc(r["assignee"]), esc(r["priority"])] for r in q["openBugs"]]
        reopened = [[self.k(r["key"]), esc(short(r["summary"], 50)), esc(r["from"]),
                     esc(r["to"]), fmt_date(r["at"], with_time=True), esc(r["author"])]
                    for r in q["reopened"]]
        rejections = [[self.k(r["key"]), esc(short(r["summary"], 50)), esc(r["from"]),
                       esc(r["to"]), fmt_date(r["at"], with_time=True), esc(r["author"])]
                      for r in q["qaRejections"]]

        return ("\n## 15. Calidad: bugs, reaperturas y rechazos de QA\n\n"
                f"- Bugs en el sprint: **{q['bugCount']}** (abiertos: {len(q['openBugs'])})\n"
                f"- Reaperturas (volvieron desde Finalizado): **{len(q['reopened'])}**\n"
                f"- Rechazos de QA (volvieron desde Pruebas QA): **{len(q['qaRejections'])}** "
                f"— tasa de rechazo {num(q.get('qaRejectionRatePct'), '%')}\n\n"
                "**Bugs abiertos**\n\n" +
                table(["Clave", "Resumen", "Estado", "Asignado", "Prioridad"], bugs) +
                "\n**Reaperturas**\n\n" +
                table(["Clave", "Resumen", "Desde", "Hacia", "Fecha", "Autor"], reopened) +
                "\n**Rechazos de QA**\n\n" +
                table(["Clave", "Resumen", "Desde", "Hacia", "Fecha", "Autor"], rejections))

    def render(self):
        parts = [
            self.header(), self.sprint_status(), self.parent_progress(), self.stale(),
            self.missing_estimate(), self.missing_assignee(), self.points_by_assignee(),
            self.daily_progress(), self.description_changes(), self.qa_analysis(),
            self.goals(), self.burndown(), self.wip(), self.scope_creep(),
            self.blockers(), self.quality(),
        ]
        parts.append("\n## 16. Acciones recomendadas\n\n"
                     "<!-- El agente completa esta sección con el análisis de Scrum Master. -->\n")
        return "\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Renderiza el informe Markdown del sprint")
    parser.add_argument("metrics", help="Archivo metrics.json")
    parser.add_argument("--config", default=None, help="Ruta a config.json")
    parser.add_argument("-o", "--output", required=True, help="Archivo .md de salida")
    args = parser.parse_args()

    metrics = json.loads(pathlib.Path(args.metrics).read_text(encoding="utf-8"))
    config_path = pathlib.Path(args.config) if args.config else pathlib.Path(__file__).resolve().parent.parent / "config.json"
    config = json.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}

    output = pathlib.Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ReportRenderer(metrics, config).render(), encoding="utf-8")
    print(f"OK -> {output}", file=sys.stderr)


if __name__ == "__main__":
    main()
