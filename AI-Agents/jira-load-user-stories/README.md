# Agente Jira Load User Stories — Estructura

```
AI-Agents/jira-load-user-stories/
├── SKILL.md                         ← Orquestador SM/PO (punto de entrada en Cursor)
├── config.json                      ← ✏️ Proyecto Jira, tipos de issue, rutas output
├── reference.md                     ← Parseo del MD, códigos temporales, vínculo a épica
└── scripts/
    ├── update_descriptions.py       ← Fase 2: actualiza Description vía REST
    └── jira_rest.py                 ← Cliente Jira Cloud (credenciales de entorno)

AI-Outputs/jira-load-user-stories/
├── README.md
├── jira-load-{fecha}-{slug}.md                 ← Informe de ejecución
└── jira-load-{fecha}-{slug}-payload.json       ← Mapa + descriptions para el update
```

## Qué hace el skill (resumen)

- Se invoca **después** de validar el `.md` de `po-expert-user-stories`.
- Lee el Markdown (no regenera historias).
- Resuelve `projectKey` + épica Jira (del MD o preguntando).
- Crea **todas** las issues (Story/Task según el MD) vía MCP `user-jira` **sin** Description final.
- Asocia cada issue a la épica indicada.
- Arma Description: COMO/QUIERO/PARA → escenarios → BDD → criterios → fuera de alcance → notas.
- **Excluye** “Metadatos y alcance de la historia”.
- Quita códigos temporales del **summary**.
- Sustituye `HU-…` / `LO-xx` / `RN-xx` por Issue Keys en la Description.
- Actualiza Descriptions con el script REST (el MCP no tiene update de issue).
- Escribe informe + payload en `AI-Outputs/jira-load-user-stories/`.

## Qué hace cada archivo

| Archivo | Rol |
|---------|-----|
| **SKILL.md** | Flujo en 2 fases, reglas SM/PO, checklist, integración MCP + script. |
| **config.json** | Defaults: proyecto MAGIA, tipos Story/Task, carpeta de output. |
| **reference.md** | Cómo parsear el MD, patrones de códigos temporales, Epic Link / parent. |
| **scripts/update_descriptions.py** | Lee el payload JSON y hace `PUT` de description en cada issue. |
| **scripts/jira_rest.py** | Auth Basic + PUT `/rest/api/3/issue/{key}` (ADF). |

## Credenciales

Mismas que `sprint-health-check`:

```powershell
powershell -ExecutionPolicy Bypass -File "AI-Agents/sprint-health-check/scripts/set_credentials.ps1"
```

## Cómo usarlo

1. Generá y validá el `.md` con `po-expert-user-stories`.
2. En Cursor: *“usá jira-load-user-stories con AI-Outputs/po-expert-user-stories/….md”*.
3. Indicá épica Jira si no está en el MD.
4. Revisá el informe en `AI-Outputs/jira-load-user-stories/`.
