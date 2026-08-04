"""Calcula todas las métricas de salud del sprint a partir del raw.json.

Uso:
    python analyze_sprint.py out/raw.json -o out/metrics.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys
import unicodedata
from collections import Counter, defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

BUCKET_RANK = {"cancelled": -1, "todo": 0, "in_progress": 1, "qa": 2, "done": 3}

STOPWORDS = {
    # Conectores y verbos genéricos que no identifican ningún ticket en particular.
    "para", "como", "desde", "hasta", "sobre", "entre", "todos", "todas", "cada",
    "este", "esta", "esos", "esas", "pero", "porque", "cuando", "donde", "sino",
    "debe", "puede", "pueden", "hacer", "tener", "sean", "modo", "mas", "son",
    "ser", "con", "sin", "por", "del", "las", "los", "una", "uno", "que", "sus",
    "fin", "end", "100", "sprint", "poder", "sumar", "siguiente", "avanzar",
    "inicio", "habilitado", "habilitar", "finalizado", "definicion", "quedar",
}


def strip_accents(text):
    return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))


def norm(text):
    return strip_accents((text or "").lower()).strip()


def parse_dt(value):
    if not value:
        return None
    text = value.strip()
    # Jira devuelve offsets sin dos puntos (-0300); fromisoformat los acepta desde 3.11.
    try:
        return dt.datetime.fromisoformat(text)
    except ValueError:
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d"):
        try:
            parsed = dt.datetime.strptime(text, fmt)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=dt.timezone.utc)
            return parsed
        except ValueError:
            continue
    return None


def days_between(later, earlier):
    if not later or not earlier:
        return None
    return round((later - earlier).total_seconds() / 86400, 1)


class SprintAnalyzer:
    def __init__(self, raw, config):
        self.raw = raw
        self.config = config
        self.sprint = raw.get("sprint") or {}
        self.issues = raw.get("issues") or []
        self.by_key = {i["key"]: i for i in self.issues}

        self.start = parse_dt(self.sprint.get("startDate"))
        self.end = parse_dt(self.sprint.get("endDate"))
        self.tz = self.start.tzinfo if self.start else dt.timezone.utc
        self.now = dt.datetime.now(self.tz)

        self.status_buckets = self._build_status_buckets()
        self.thresholds = config.get("thresholds", {})
        self.patterns = {
            name: [re.compile(p, re.IGNORECASE) for p in patterns]
            for name, patterns in config.get("subtask_patterns", {}).items()
        }

        for issue in self.issues:
            self._enrich(issue)

    # ---------- preparación ----------

    def _build_status_buckets(self):
        mapping = {}
        for bucket, names in (self.config.get("statuses") or {}).items():
            for name in names:
                mapping[norm(name)] = bucket
        return mapping

    def bucket(self, issue):
        explicit = self.status_buckets.get(norm(issue.get("status")))
        if explicit:
            return explicit
        category = norm(issue.get("statusCategory"))
        if category in {"done", "listo", "finalizada"}:
            return "done"
        if category in {"in progress", "en curso"}:
            return "in_progress"
        return "todo"

    def _enrich(self, issue):
        """Deriva del changelog: transiciones de estado, última actividad y cambios de descripción."""
        transitions = []
        description_changes = []
        assignee_changes = []
        point_changes = []
        sprint_changes = []

        for entry in issue.get("changelog") or []:
            when = parse_dt(entry.get("created"))
            author = ((entry.get("author") or {}).get("displayName")) or "desconocido"
            for item in entry.get("items") or []:
                field = norm(item.get("field"))
                record = {
                    "at": when.isoformat() if when else None,
                    "_at": when,
                    "author": author,
                    "from": item.get("fromString"),
                    "to": item.get("toString"),
                }
                if field == "status":
                    transitions.append(record)
                elif field == "description":
                    description_changes.append(record)
                elif field == "assignee":
                    assignee_changes.append(record)
                elif "story point" in field or "punto" in field:
                    point_changes.append(record)
                elif field == "sprint":
                    sprint_changes.append(record)

        transitions.sort(key=lambda r: r["_at"] or dt.datetime.min.replace(tzinfo=dt.timezone.utc))

        issue["_transitions"] = transitions
        issue["_descriptionChanges"] = description_changes
        issue["_assigneeChanges"] = assignee_changes
        issue["_pointChanges"] = point_changes
        issue["_sprintChanges"] = sprint_changes
        issue["_bucket"] = self.bucket(issue)

        last_status_change = transitions[-1]["_at"] if transitions else parse_dt(issue.get("created"))
        issue["_lastStatusChange"] = last_status_change
        issue["_daysInStatus"] = days_between(self.now, last_status_change)
        issue["_daysSinceUpdate"] = days_between(self.now, parse_dt(issue.get("updated")))

        issue["_doneAt"] = None
        for record in reversed(transitions):
            if self.status_buckets.get(norm(record["to"])) == "done":
                issue["_doneAt"] = record["_at"]
                break

        issue["_qaEnteredAt"] = None
        for record in transitions:
            if self.status_buckets.get(norm(record["to"])) == "qa":
                issue["_qaEnteredAt"] = record["_at"]
                break

        issue["_startedAt"] = None
        for record in transitions:
            if self.status_buckets.get(norm(record["to"])) == "in_progress":
                issue["_startedAt"] = record["_at"]
                break

    # ---------- helpers ----------

    @property
    def parents(self):
        return [i for i in self.issues if not i.get("isSubtask")]

    def subtasks_of(self, key):
        return [i for i in self.issues if i.get("parentKey") == key]

    def points(self, issue):
        value = issue.get("storyPoints")
        return float(value) if isinstance(value, (int, float)) else 0.0

    def classify_subtask(self, issue):
        text = issue.get("summary") or ""
        for name, patterns in self.patterns.items():
            if any(p.search(text) for p in patterns):
                return name
        return "otro"

    def sprint_days(self):
        if not self.start:
            return []
        last = min(self.now, self.end) if self.end else self.now
        days = []
        cursor = self.start.date()
        while cursor <= last.date():
            days.append(cursor)
            cursor += dt.timedelta(days=1)
        return days

    def is_working_day(self, day):
        return day.weekday() < 5

    # ---------- 1. estado del sprint ----------

    def sprint_status(self):
        parents = self.parents
        # El trabajo cancelado no forma parte del compromiso: se reporta aparte.
        active = [i for i in parents if i["_bucket"] != "cancelled"]
        total_points = sum(self.points(i) for i in active)
        done_points = sum(self.points(i) for i in active if i["_bucket"] == "done")
        cancelled_points = sum(self.points(i) for i in parents if i["_bucket"] == "cancelled")

        by_status = Counter(i.get("status") for i in self.issues)
        parents_by_status = Counter(i.get("status") for i in parents)
        by_bucket = Counter(i["_bucket"] for i in parents)

        total_days = (self.end.date() - self.start.date()).days if self.start and self.end else None
        elapsed_days = (min(self.now, self.end).date() - self.start.date()).days if self.start and self.end else None
        remaining_days = (self.end - self.now).total_seconds() / 86400 if self.end else None

        working_total = sum(1 for d in self._all_days() if self.is_working_day(d))
        working_elapsed = sum(1 for d in self.sprint_days() if self.is_working_day(d))

        return {
            "name": self.sprint.get("name"),
            "state": self.sprint.get("state"),
            "startDate": self.sprint.get("startDate"),
            "endDate": self.sprint.get("endDate"),
            "goalRaw": self.sprint.get("goal"),
            "totalDays": total_days,
            "elapsedDays": elapsed_days,
            "remainingDays": round(remaining_days, 1) if remaining_days is not None else None,
            "workingDaysTotal": working_total,
            "workingDaysElapsed": working_elapsed,
            "timeElapsedPct": round(100 * elapsed_days / total_days, 1) if total_days else None,
            "totalIssues": len(self.issues),
            "totalParents": len(parents),
            "activeParents": len(active),
            "totalSubtasks": len(self.issues) - len(parents),
            "totalPoints": total_points,
            "donePoints": done_points,
            "cancelledPoints": cancelled_points,
            "completionPctByPoints": round(100 * done_points / total_points, 1) if total_points else None,
            "completionPctByCount": round(100 * by_bucket["done"] / len(active), 1) if active else None,
            "issuesByStatus": dict(by_status),
            "parentsByStatus": dict(parents_by_status),
            "parentsByBucket": dict(by_bucket),
        }

    def _all_days(self):
        if not (self.start and self.end):
            return []
        days = []
        cursor = self.start.date()
        while cursor <= self.end.date():
            days.append(cursor)
            cursor += dt.timedelta(days=1)
        return days

    # ---------- 2. avance de historias principales ----------

    def parent_progress(self):
        rows = []
        for issue in self.parents:
            subtasks = self.subtasks_of(issue["key"])
            done_subtasks = [s for s in subtasks if s["_bucket"] == "done"]
            active_subtasks = [s for s in subtasks if s["_bucket"] not in {"done", "cancelled"}]
            rows.append({
                "key": issue["key"],
                "summary": issue["summary"],
                "issueType": issue.get("issueType"),
                "status": issue.get("status"),
                "bucket": issue["_bucket"],
                "assignee": issue.get("assignee"),
                "points": self.points(issue) or None,
                "priority": issue.get("priority"),
                "subtaskTotal": len(subtasks),
                "subtaskDone": len(done_subtasks),
                "subtaskPct": round(100 * len(done_subtasks) / len(subtasks)) if subtasks else None,
                "pendingSubtasks": [s["key"] for s in active_subtasks],
                "daysInStatus": issue["_daysInStatus"],
                "flagged": issue.get("flagged"),
            })
        order = {"done": 3, "qa": 2, "in_progress": 1, "todo": 0, "cancelled": 4}
        rows.sort(key=lambda r: (order.get(r["bucket"], 9), -(r["daysInStatus"] or 0)))
        return rows

    # ---------- 3. estancados ----------

    def stale_issues(self):
        limit = self.thresholds.get("stale_days", 5)
        rows = []
        for issue in self.issues:
            if issue["_bucket"] in {"done", "cancelled"}:
                continue
            days = issue["_daysInStatus"]
            if days is not None and days >= limit:
                rows.append({
                    "key": issue["key"],
                    "summary": issue["summary"],
                    "issueType": issue.get("issueType"),
                    "isSubtask": issue.get("isSubtask"),
                    "status": issue.get("status"),
                    "assignee": issue.get("assignee"),
                    "daysInStatus": days,
                    "daysSinceUpdate": issue["_daysSinceUpdate"],
                    "lastStatusChange": issue["_lastStatusChange"].isoformat() if issue["_lastStatusChange"] else None,
                    "neverMoved": not issue["_transitions"],
                })
        rows.sort(key=lambda r: -(r["daysInStatus"] or 0))
        return {"thresholdDays": limit, "items": rows}

    # ---------- 4 y 5. faltantes de estimación y asignación ----------

    def missing_data(self):
        require_types = {norm(t) for t in self.config.get("estimation_required_types", [])}
        estimate_subtasks = self.config.get("estimate_subtasks", False)

        missing_estimate = []
        missing_assignee = []
        for issue in self.issues:
            if issue["_bucket"] == "cancelled":
                continue
            is_subtask = issue.get("isSubtask")

            needs_estimate = (not is_subtask) if not require_types else norm(issue.get("issueType")) in require_types
            if is_subtask and not estimate_subtasks:
                needs_estimate = False
            if needs_estimate and not self.points(issue):
                missing_estimate.append({
                    "key": issue["key"],
                    "summary": issue["summary"],
                    "issueType": issue.get("issueType"),
                    "status": issue.get("status"),
                    "assignee": issue.get("assignee"),
                })

            if not issue.get("assignee"):
                missing_assignee.append({
                    "key": issue["key"],
                    "summary": issue["summary"],
                    "issueType": issue.get("issueType"),
                    "isSubtask": is_subtask,
                    "status": issue.get("status"),
                    "bucket": issue["_bucket"],
                })

        return {"missingEstimate": missing_estimate, "missingAssignee": missing_assignee}

    # ---------- 6. puntos por persona ----------

    def points_by_assignee(self):
        buckets = defaultdict(lambda: {
            "assignee": None, "totalPoints": 0.0, "donePoints": 0.0, "qaPoints": 0.0,
            "inProgressPoints": 0.0, "todoPoints": 0.0, "issues": 0, "doneIssues": 0,
            "unestimatedIssues": 0,
        })
        for issue in self.parents:
            if issue["_bucket"] == "cancelled":
                continue
            name = issue.get("assignee") or "SIN ASIGNAR"
            row = buckets[name]
            row["assignee"] = name
            points = self.points(issue)
            row["issues"] += 1
            row["totalPoints"] += points
            if not points:
                row["unestimatedIssues"] += 1
            bucket = issue["_bucket"]
            if bucket == "done":
                row["donePoints"] += points
                row["doneIssues"] += 1
            elif bucket == "qa":
                row["qaPoints"] += points
            elif bucket == "in_progress":
                row["inProgressPoints"] += points
            else:
                row["todoPoints"] += points

        rows = sorted(buckets.values(), key=lambda r: -r["totalPoints"])
        for row in rows:
            row["completionPct"] = (
                round(100 * row["donePoints"] / row["totalPoints"], 1) if row["totalPoints"] else None
            )
        return rows

    # ---------- 7. evolución diaria por persona ----------

    def daily_progress(self):
        days = self.sprint_days()
        day_keys = [d.isoformat() for d in days]

        points_by_day = defaultdict(lambda: defaultdict(float))
        items_by_day = defaultdict(lambda: defaultdict(int))

        last_day = days[-1] if days else None
        for issue in self.issues:
            # Sólo lo que sigue cerrado hoy, en la fecha de su último cierre.
            if issue["_bucket"] != "done" or not issue["_doneAt"] or not self.start:
                continue
            day = issue["_doneAt"].astimezone(self.tz).date()
            if day < self.start.date() or (last_day and day > last_day):
                continue

            name = issue.get("assignee") or "SIN ASIGNAR"
            items_by_day[name][day.isoformat()] += 1
            if not issue.get("isSubtask"):
                points_by_day[name][day.isoformat()] += self.points(issue)

        people = sorted(set(list(points_by_day.keys()) + list(items_by_day.keys())))
        matrix = []
        for person in people:
            daily_points = [round(points_by_day[person].get(d, 0.0), 1) for d in day_keys]
            daily_items = [items_by_day[person].get(d, 0) for d in day_keys]
            cumulative, running = [], 0.0
            for value in daily_points:
                running += value
                cumulative.append(round(running, 1))
            matrix.append({
                "assignee": person,
                "dailyPoints": daily_points,
                "dailyItems": daily_items,
                "cumulativePoints": cumulative,
                "totalPoints": round(sum(daily_points), 1),
                "totalItems": sum(daily_items),
            })
        matrix.sort(key=lambda r: -r["totalPoints"])
        return {"days": day_keys, "byAssignee": matrix}

    # ---------- 8. cambios de alcance en la descripción ----------

    def description_changes(self):
        rows = []
        for issue in self.issues:
            for record in issue["_descriptionChanges"]:
                when = record["_at"]
                if self.start and when and when < self.start:
                    continue
                before = (record.get("from") or "").strip()
                after = (record.get("to") or "").strip()
                rows.append({
                    "key": issue["key"],
                    "summary": issue["summary"],
                    "issueType": issue.get("issueType"),
                    "status": issue.get("status"),
                    "assignee": issue.get("assignee"),
                    "changedAt": record["at"],
                    "author": record["author"],
                    "beforeChars": len(before),
                    "afterChars": len(after),
                    "deltaChars": len(after) - len(before),
                    "beforeExcerpt": before[:600],
                    "afterExcerpt": after[:600],
                })
        rows.sort(key=lambda r: r["changedAt"] or "", reverse=True)
        return rows

    # ---------- 9. consistencia QA ----------

    def qa_analysis(self):
        qa_families = {"qa_automation", "qa_execution", "qa_manual"}
        rows = []
        for issue in self.parents:
            subtasks = self.subtasks_of(issue["key"])
            if not subtasks and issue["_bucket"] != "qa":
                continue

            grouped = defaultdict(list)
            for subtask in subtasks:
                grouped[self.classify_subtask(subtask)].append(subtask)

            has_dev = bool(grouped.get("dev"))
            findings = []

            if has_dev:
                if not grouped.get("qa_automation"):
                    findings.append("Falta subtarea de QA Automation")
                elif len(grouped["qa_automation"]) > 1:
                    findings.append(f"{len(grouped['qa_automation'])} subtareas de QA Automation (se espera 1)")
                if not grouped.get("qa_execution"):
                    findings.append("Falta subtarea de Ejecución de Tests")
                elif len(grouped["qa_execution"]) > 1:
                    findings.append(f"{len(grouped['qa_execution'])} subtareas de Ejecución de Tests (se espera 1)")

            pending_qa = [
                s for family in qa_families for s in grouped.get(family, [])
                if s["_bucket"] not in {"done", "cancelled"}
            ]
            if issue["_bucket"] == "qa" and pending_qa:
                findings.append(f"Historia en Pruebas QA con {len(pending_qa)} subtarea(s) de QA sin cerrar")

            dev_done_at = None
            for subtask in grouped.get("dev", []):
                if subtask["_doneAt"] and (dev_done_at is None or subtask["_doneAt"] > dev_done_at):
                    dev_done_at = subtask["_doneAt"]

            qa_entered_at = issue["_qaEnteredAt"]
            reference = qa_entered_at or dev_done_at

            pending_detail = []
            for subtask in pending_qa:
                pending_detail.append({
                    "key": subtask["key"],
                    "summary": subtask["summary"],
                    "family": self.classify_subtask(subtask),
                    "status": subtask.get("status"),
                    "assignee": subtask.get("assignee"),
                    "daysInStatus": subtask["_daysInStatus"],
                    "daysSinceDevDone": days_between(self.now, dev_done_at),
                    "daysSinceParentInQa": days_between(self.now, qa_entered_at),
                })

            if not findings and not pending_detail:
                continue

            rows.append({
                "key": issue["key"],
                "summary": issue["summary"],
                "status": issue.get("status"),
                "assignee": issue.get("assignee"),
                "hasDev": has_dev,
                "counts": {family: len(items) for family, items in grouped.items()},
                "devDoneAt": dev_done_at.isoformat() if dev_done_at else None,
                "qaEnteredAt": qa_entered_at.isoformat() if qa_entered_at else None,
                "daysWaitingQa": days_between(self.now, reference),
                "findings": findings,
                "pendingQaSubtasks": pending_detail,
            })

        rows.sort(key=lambda r: -(r["daysWaitingQa"] or 0))
        return rows

    # ---------- 10. goals vs tareas ----------

    def goals(self):
        raw_goal = self.sprint.get("goal") or ""
        overrides = self.config.get("goal_overrides") or {}
        # La prioridad se marca al final de la línea ("- CRITICO", "(ALTA)"). Anclar al final
        # evita confundirla con la palabra "Alta" usada como sustantivo ("Alta de EGP").
        priority_pattern = re.compile(
            r"[\s\-–—]*\(?\s*(CRITICO|CRÍTICO|ALTA|MEDIA|BAJA)\s*\)?\s*$",
            re.IGNORECASE,
        )

        parsed = []
        for line in raw_goal.splitlines():
            text = line.strip().lstrip("-•*").strip()
            if not text:
                continue
            match = priority_pattern.search(text)
            priority = strip_accents(match.group(1).upper()) if match else "SIN PRIORIDAD"
            # Sólo se recorta el separador final; strip("()") rompería paréntesis balanceados.
            clean = priority_pattern.sub("", text).strip().strip("-–—").strip() if match else text
            parsed.append({"text": clean, "rawText": text, "priority": priority})

        for index, goal in enumerate(parsed):
            keys = overrides.get(str(index)) or overrides.get(goal["text"])
            if keys:
                matched = [self.by_key[k] for k in keys if k in self.by_key]
                goal["matchMethod"] = "override"
            else:
                matched = self._match_goal_issues(goal["text"])
                goal["matchMethod"] = "keywords"

            buckets = Counter(i["_bucket"] for i in matched)
            total_points = sum(self.points(i) for i in matched)
            done_points = sum(self.points(i) for i in matched if i["_bucket"] == "done")

            goal["issues"] = [{
                "key": i["key"],
                "summary": i["summary"],
                "status": i.get("status"),
                "bucket": i["_bucket"],
                "assignee": i.get("assignee"),
                "points": self.points(i) or None,
            } for i in matched]
            goal["counts"] = dict(buckets)
            goal["totalPoints"] = total_points
            goal["donePoints"] = done_points
            goal["completionPct"] = round(100 * done_points / total_points, 1) if total_points else None
            goal["verdict"] = self._goal_verdict(goal, buckets, len(matched))

        return parsed

    def _match_goal_issues(self, goal_text):
        """Vincula tickets al goal ponderando por rareza del término (estilo IDF).

        Un término que aparece en casi todos los tickets (p. ej. "desarrollo") no
        identifica nada; uno que aparece en dos o tres ("gobernanza", "flipt") sí.
        """
        keywords = {
            w for w in re.findall(r"[a-z0-9]{3,}", norm(goal_text))
            if w not in STOPWORDS
        }
        if not keywords:
            return []

        haystacks = {
            issue["key"]: norm(f"{issue['summary']} {issue.get('description', '')[:400]}")
            for issue in self.parents
        }
        total = len(haystacks) or 1
        generic_limit = max(2, int(0.4 * total))

        document_freq = {
            kw: sum(1 for text in haystacks.values() if kw in text) for kw in keywords
        }
        useful = {kw: df for kw, df in document_freq.items() if 0 < df <= generic_limit}
        if not useful:
            return []

        scored = []
        for issue in self.parents:
            text = haystacks[issue["key"]]
            matched = [kw for kw in useful if kw in text]
            if not matched:
                continue
            rarest = min(useful[kw] for kw in matched)
            # Un único término muy distintivo alcanza; si no, se exigen dos coincidencias.
            if len(matched) >= 2 or rarest <= 3:
                scored.append((len(matched), -rarest, issue))

        scored.sort(key=lambda t: (-t[0], -t[1]))
        return [issue for _, _, issue in scored[:12]]

    def _goal_verdict(self, goal, buckets, total):
        if not total:
            return "SIN TICKETS IDENTIFICADOS"
        done = buckets.get("done", 0)
        if done == total:
            return "CUMPLIDO"
        pending_dev = buckets.get("todo", 0) + buckets.get("in_progress", 0)
        if done + buckets.get("qa", 0) == total:
            return "EN RIESGO - SOLO QA PENDIENTE"
        if pending_dev == total:
            return "NO INICIADO / EN RIESGO ALTO"
        return "PARCIAL"

    # ---------- extras Scrum ----------

    def burndown(self):
        days = self._all_days()
        if not days:
            return {"days": [], "ideal": [], "actual": [], "projection": None}

        total_points = sum(self.points(i) for i in self.parents if i["_bucket"] != "cancelled")
        working_total = sum(1 for d in days if self.is_working_day(d))

        # Línea ideal: puntos restantes al CIERRE de cada día, consumo lineal sobre
        # días hábiles. Así el último día llega a 0 y es comparable con la línea real.
        ideal, worked = [], 0
        for day in days:
            if self.is_working_day(day):
                worked += 1
            remaining = total_points * (1 - worked / working_total) if working_total else total_points
            ideal.append(round(max(remaining, 0), 1))

        # Sólo cuenta el trabajo que sigue terminado hoy: si un ítem se reabrió, sus
        # puntos no se acreditan (se usa la última transición a Finalizado, no la primera).
        done_by_day = defaultdict(float)
        for issue in self.parents:
            if issue["_bucket"] == "done" and issue["_doneAt"]:
                done_by_day[issue["_doneAt"].astimezone(self.tz).date()] += self.points(issue)

        actual, running = [], 0.0
        today = self.now.date()
        for day in days:
            running += done_by_day.get(day, 0.0)
            actual.append(round(total_points - running, 1) if day <= today else None)

        elapsed_working = sum(1 for d in days if self.is_working_day(d) and d <= today) or 1
        remaining_working = sum(1 for d in days if self.is_working_day(d) and d > today)
        velocity = running / elapsed_working if elapsed_working else 0
        projected = running + velocity * remaining_working
        gap = total_points - projected

        return {
            "days": [d.isoformat() for d in days],
            "ideal": ideal,
            "actual": actual,
            "totalPoints": total_points,
            "completedPoints": round(running, 1),
            "dailyVelocity": round(velocity, 2),
            "remainingWorkingDays": remaining_working,
            "projectedCompletion": round(projected, 1),
            "projectedGap": round(gap, 1),
            "willFinish": gap <= 0,
        }

    def wip_analysis(self):
        limit = self.thresholds.get("wip_limit_per_person", 3)
        per_person = defaultdict(list)
        for issue in self.issues:
            if issue["_bucket"] in {"in_progress", "qa"}:
                per_person[issue.get("assignee") or "SIN ASIGNAR"].append(issue)

        wip_rows = []
        for person, items in sorted(per_person.items(), key=lambda kv: -len(kv[1])):
            wip_rows.append({
                "assignee": person,
                "wipCount": len(items),
                "overLimit": len(items) > limit,
                "issues": [{"key": i["key"], "status": i.get("status"), "daysInStatus": i["_daysInStatus"]} for i in items],
            })

        aging = defaultdict(list)
        for issue in self.issues:
            if issue["_bucket"] not in {"done", "cancelled"} and issue["_daysInStatus"] is not None:
                aging[issue.get("status")].append(issue["_daysInStatus"])

        aging_rows = [{
            "status": status,
            "count": len(values),
            "avgDays": round(sum(values) / len(values), 1),
            "maxDays": max(values),
        } for status, values in aging.items()]
        aging_rows.sort(key=lambda r: -r["avgDays"])

        return {"wipLimit": limit, "byAssignee": wip_rows, "agingByStatus": aging_rows}

    def scope_creep(self):
        scope = self.raw.get("scopeChanges") or {}
        added_keys = set(scope.get("addedDuringSprint") or [])

        # Fallback: si el sprint report no está disponible, usar fecha de creación.
        created_after_start = [
            i["key"] for i in self.issues
            if self.start and parse_dt(i.get("created")) and parse_dt(i.get("created")) > self.start
        ]
        if not scope.get("available"):
            added_keys = set(created_after_start)

        added = []
        for key in sorted(added_keys):
            issue = self.by_key.get(key)
            if not issue:
                added.append({"key": key, "summary": "(fuera del sprint actual)", "points": None})
                continue
            added.append({
                "key": key,
                "summary": issue["summary"],
                "issueType": issue.get("issueType"),
                "isSubtask": issue.get("isSubtask"),
                "status": issue.get("status"),
                "assignee": issue.get("assignee"),
                "points": self.points(issue) or None,
                "createdAfterStart": key in created_after_start,
            })

        added_points = sum(a["points"] or 0 for a in added if not a.get("isSubtask"))
        total_points = sum(self.points(i) for i in self.parents if i["_bucket"] != "cancelled")
        baseline = total_points - added_points

        return {
            "source": "sprint report" if scope.get("available") else "fecha de creación (fallback)",
            "addedDuringSprint": added,
            "addedPoints": added_points,
            "removedFromSprint": scope.get("punted") or [],
            "baselinePoints": round(baseline, 1),
            "scopeCreepPct": round(100 * added_points / baseline, 1) if baseline else None,
        }

    def blockers(self):
        idle_limit = self.thresholds.get("idle_days", 3)
        flagged = [{
            "key": i["key"], "summary": i["summary"], "status": i.get("status"),
            "assignee": i.get("assignee"), "daysInStatus": i["_daysInStatus"],
        } for i in self.issues if i.get("flagged")]

        idle = [{
            "key": i["key"], "summary": i["summary"], "status": i.get("status"),
            "assignee": i.get("assignee"), "daysSinceUpdate": i["_daysSinceUpdate"],
        } for i in self.issues
            if i["_bucket"] == "in_progress" and (i["_daysSinceUpdate"] or 0) >= idle_limit]
        idle.sort(key=lambda r: -(r["daysSinceUpdate"] or 0))

        never_started = [{
            "key": i["key"], "summary": i["summary"], "assignee": i.get("assignee"),
            "points": self.points(i) or None,
        } for i in self.parents if i["_bucket"] == "todo" and not i["_transitions"]]

        return {
            "idleThresholdDays": idle_limit,
            "flagged": flagged,
            "idleInProgress": idle,
            "neverStarted": never_started,
        }

    def quality(self):
        bug_types = {norm(t) for t in self.config.get("bug_issue_types", ["Bug", "Error", "Defecto"])}
        bugs = [i for i in self.issues if norm(i.get("issueType")) in bug_types]

        reopened, qa_rejections = [], []
        for issue in self.issues:
            for record in issue["_transitions"]:
                from_bucket = self.status_buckets.get(norm(record["from"]))
                to_bucket = self.status_buckets.get(norm(record["to"]))
                if not from_bucket or not to_bucket:
                    continue
                if BUCKET_RANK.get(to_bucket, 0) < BUCKET_RANK.get(from_bucket, 0):
                    entry = {
                        "key": issue["key"], "summary": issue["summary"],
                        "from": record["from"], "to": record["to"],
                        "at": record["at"], "author": record["author"],
                    }
                    if from_bucket == "done":
                        reopened.append(entry)
                    elif from_bucket == "qa":
                        qa_rejections.append(entry)

        parents_reaching_qa = [i for i in self.parents if i["_qaEnteredAt"]]
        return {
            "bugCount": len(bugs),
            "openBugs": [{
                "key": i["key"], "summary": i["summary"], "status": i.get("status"),
                "assignee": i.get("assignee"), "priority": i.get("priority"),
            } for i in bugs if i["_bucket"] not in {"done", "cancelled"}],
            "reopened": reopened,
            "qaRejections": qa_rejections,
            "qaRejectionRatePct": (
                round(100 * len(qa_rejections) / len(parents_reaching_qa), 1)
                if parents_reaching_qa else None
            ),
        }

    def health_score(self, sections):
        """Semáforo agregado: penaliza cada señal de riesgo detectada."""
        signals = []
        status = sections["sprintStatus"]
        burndown = sections["burndown"]

        time_pct = status.get("timeElapsedPct") or 0
        done_pct = status.get("completionPctByPoints") or 0
        if time_pct - done_pct > 25:
            signals.append(("Avance muy por detrás del tiempo transcurrido", "alto"))
        elif time_pct - done_pct > 10:
            signals.append(("Avance por detrás del tiempo transcurrido", "medio"))

        if burndown.get("willFinish") is False:
            signals.append((f"Proyección: quedan {burndown.get('projectedGap')} pts sin cerrar", "alto"))
        if sections["missingEstimate"]:
            signals.append((f"{len(sections['missingEstimate'])} ítems sin estimar", "medio"))
        if sections["missingAssignee"]:
            signals.append((f"{len(sections['missingAssignee'])} ítems sin asignar", "medio"))
        if sections["stale"]["items"]:
            signals.append((f"{len(sections['stale']['items'])} ítems estancados", "alto"))
        if sections["qaAnalysis"]:
            signals.append((f"{len(sections['qaAnalysis'])} historias con inconsistencias de QA", "alto"))
        if sections["quality"]["reopened"]:
            signals.append((f"{len(sections['quality']['reopened'])} reaperturas", "medio"))
        creep = sections["scopeCreep"].get("scopeCreepPct")
        if creep and creep > 10:
            signals.append((f"Scope creep del {creep}%", "medio"))
        over_wip = [r for r in sections["wip"]["byAssignee"] if r["overLimit"]]
        if over_wip:
            signals.append((f"{len(over_wip)} persona(s) sobre el límite de WIP", "medio"))

        high = sum(1 for _, level in signals if level == "alto")
        medium = sum(1 for _, level in signals if level == "medio")
        if high >= 3:
            verdict = "CRITICO"
        elif high >= 1:
            verdict = "EN RIESGO"
        elif medium >= 3:
            verdict = "ATENCION"
        else:
            verdict = "SALUDABLE"

        return {"verdict": verdict, "signals": [{"text": t, "level": l} for t, l in signals]}

    def run(self):
        missing = self.missing_data()
        sections = {
            "sprintStatus": self.sprint_status(),
            "parentProgress": self.parent_progress(),
            "stale": self.stale_issues(),
            "missingEstimate": missing["missingEstimate"],
            "missingAssignee": missing["missingAssignee"],
            "pointsByAssignee": self.points_by_assignee(),
            "dailyProgress": self.daily_progress(),
            "descriptionChanges": self.description_changes(),
            "qaAnalysis": self.qa_analysis(),
            "goals": self.goals(),
            "burndown": self.burndown(),
            "wip": self.wip_analysis(),
            "scopeCreep": self.scope_creep(),
            "blockers": self.blockers(),
            "quality": self.quality(),
        }
        sections["health"] = self.health_score(sections)
        sections["generatedAt"] = self.now.isoformat()
        return sections


def main():
    parser = argparse.ArgumentParser(description="Calcula métricas de salud del sprint")
    parser.add_argument("raw", help="Archivo raw.json de fetch_sprint_data.py")
    parser.add_argument("--config", default=None, help="Ruta a config.json")
    parser.add_argument("-o", "--output", required=True, help="Archivo JSON de métricas")
    args = parser.parse_args()

    raw = json.loads(pathlib.Path(args.raw).read_text(encoding="utf-8"))

    config_path = pathlib.Path(args.config) if args.config else pathlib.Path(__file__).resolve().parent.parent / "config.json"
    config = json.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}

    metrics = SprintAnalyzer(raw, config).run()

    output = pathlib.Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(metrics, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    print(f"OK -> {output}", file=sys.stderr)


if __name__ == "__main__":
    main()
