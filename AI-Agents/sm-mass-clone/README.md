# sm-mass-clone

Agente **Scrum Master Senior** para **clonado masivo** de issues en Jira (épica, sprint o backlog).

## Qué hace el skill

- Guarda (la primera vez) la URL del proyecto/tablero Jira en `config.json`
- Filtra issues por origen: **épica**, **sprint** o **backlog**
- Filtra por tipo de issue (Historia, Tarea, Spike, Bug, Subtarea, etc.)
- Filtra por estado (ej. Tareas por hacer, Backlog, En Curso)
- Aplica nomenclatura especial al título del clon (ej. `QA - `)
- Asigna la persona indicada al issue clonado (si se informó)
- Clona los issues filtrados en Jira (mismo tipo que el original)
- Copia la **Descripción** del issue original al clon
- Copia el campo **Principal** (parent/épica) del original
- Vincula clon ↔ original con tipo **Relacionar** (*está relacionado a*)
- Replica el **Sprint** del original; si no tenía, deja el clon en backlog
- Omite issues cuyo título ya empieza con la nomenclatura (evita reclonar)
- Ejecuta **dry-run** y pide confirmación antes de clonar de verdad
- Genera un reporte `.md` en `AI-Outputs/sm-mass-clone/` con la tabla original → clonado

## SM Mass Clone — Estructura

```
AI-Agents/sm-mass-clone/
├── SKILL.md                 ← Instrucciones del agente Cursor (punto de entrada)
├── README.md                ← Esta documentación
├── config.json              ← ✏️ Proyecto, board, aliases de tipo/estado
├── references/
│   └── clone-playbook.md    ← Criterios SM y reglas de clonado
└── scripts/
    ├── run_mass_clone.ps1   ← Orchestrador (punto de entrada CLI)
    ├── set_credentials.ps1  ← ✏️ Guarda JIRA_EMAIL / JIRA_API_TOKEN (una vez)
    ├── jira_client.py       ← Cliente REST Jira Cloud (auth, search, CRUD)
    ├── clone_issues.py      ← Filtra por JQL + clona + link + assign + sprint
    └── render_report.py     ← Genera el reporte Markdown del resultado

AI-Outputs/sm-mass-clone/
├── last-run.json            ← Última corrida (JSON de resultados)
└── <yyyyMMdd-HHmm>-clone-report.md   ← Reporte MD (tabla original ↔ clon)
```

| Archivo | Qué hace |
|---------|----------|
| `SKILL.md` | Orquestador en Cursor: rol SM, inputs, dry-run, checklist y rutas de salida |
| `config.json` | Contrato del proyecto: URL, `project_key`, `board_id`, aliases |
| `clone-playbook.md` | Apoyo SM: cuándo clonar, anti-patrones, impacto de alcance |
| `run_mass_clone.ps1` | Pipeline: credenciales → clone → render del `.md` |
| `set_credentials.ps1` | Configura variables de entorno de usuario para la API de Jira |
| `jira_client.py` | Auth Basic, GET/POST/PUT, `search/jql`, descubrimiento de campos |
| `clone_issues.py` | Arma JQL, dry-run o clonado real, vínculo Relacionar, sprint y assignee |
| `render_report.py` | Transforma `last-run.json` en reporte Markdown con tabla de relación |

## Requisitos

```powershell
powershell -ExecutionPolicy Bypass -File "AI-Agents/sm-mass-clone/scripts/set_credentials.ps1"
```

Token: https://id.atlassian.com/manage-profile/security/api-tokens

## Uso rápido (CLI)

```powershell
# Dry-run: lista candidatos sin clonar
powershell -ExecutionPolicy Bypass -File "AI-Agents/sm-mass-clone/scripts/run_mass_clone.ps1" `
  -OriginType epic -OriginValue MAGIA-5 `
  -IssueType Historia -Status "Tareas por hacer" `
  -TitlePrefix "QA - " -Assignee "Alexis Alvarez" -DryRun

# Clonado real + reporte
powershell -ExecutionPolicy Bypass -File "AI-Agents/sm-mass-clone/scripts/run_mass_clone.ps1" `
  -OriginType epic -OriginValue MAGIA-5 `
  -IssueType Historia -Status "Tareas por hacer" `
  -TitlePrefix "QA - " -Assignee "Alexis Alvarez"
```

## Uso desde Cursor

Decí: *“usá el skill sm-mass-clone”* o *“cloná masivamente historias del sprint”*.  
El agente sigue `SKILL.md`, pide los inputs y ejecuta los scripts.
