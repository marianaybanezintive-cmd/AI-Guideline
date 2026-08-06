# Playbook — Clonado masivo (Scrum Master Senior)

## Cuándo usar este agente

- Preparar un set de historias/tareas espejo (p. ej. QA) desde una épica o sprint.
- Duplicar trabajo técnico pendiente del backlog con nomenclatura uniforme.
- Acelerar armado de sprints sin perder trazabilidad al issue de origen.

## Principios

1. **Transparencia:** el equipo debe poder ver original ↔ clon en Jira (vínculo Relacionar).
2. **No pérdida de contexto:** descripción y Principal se preservan.
3. **Planificación consciente:** clonar al mismo sprint aumenta alcance; confirmá con el equipo.
4. **Nomenclatura:** el prefijo debe permitir filtros JQL (`summary ~ "QA -"`).

## Orígenes y JQL (referencia)

| Origen | Criterio |
|--------|----------|
| Épica | `parent = KEY` (y/o Epic Link según proyecto) |
| Sprint | `sprint = ID` o `sprint = "Nombre"` |
| Backlog | `project = KEY AND sprint is EMPTY` |

Siempre se añaden: `issuetype = …` y `status = …`.

## Campos que el clon debe respetar

| Campo | Regla |
|-------|--------|
| Summary | `{nomenclatura}{summary}` |
| Description | Copia del ADF original |
| Parent / Principal | Igual al original (si tenía) |
| Assignee | El indicado por el usuario (si hubo) |
| Sprint | Igual al original; si vacío → backlog |
| Issue links | Clon *está relacionado a* Original (tipo Relacionar) |

## Anti-patrones

- Clonar sin dry-run / sin confirmación de cantidad.
- Reclonar issues que ya tienen el prefijo de nomenclatura.
- Cambiar el tipo de issue respecto del original (rompe flujos y boards).
- Asignar a alguien sin validar que exista en el directorio Atlassian.

## Definición de terminado del proceso

- Todos los candidatos confirmados tienen clon o error explícito en el reporte.
- El `.md` en `AI-Outputs/sm-mass-clone/` lista la relación original → clon.
- El SM comunicó al equipo si hubo impacto de scope en el sprint activo.
