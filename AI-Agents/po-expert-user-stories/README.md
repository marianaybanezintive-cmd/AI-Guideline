# Agente PO Expert User Stories — Estructura

```
AI-Agents/po-expert-user-stories/
├── SKILL.md              ← Instrucciones del agente (punto de entrada en Cursor)
├── md-template.md        ← Plantilla obligatoria: 13 secciones del .md de salida
├── excel-input.md        ← Reglas cuando el input es Excel (columnas canónicas)
├── csv-schema.md         ← Plantilla y reglas del CSV (4 columnas, `;`, Description)
└── reference.md          ← Guía INVEST, criterios, catálogo MSG, HITL

AI-Outputs/po-expert-user-stories/
├── README.md             ← Destino de resultados (no es parte del skill)
└── po-historias-usuario-{fecha}-{slug}.md|.csv   ← Generados al ejecutar
```

## Qué hace el skill (resumen)

- Lee documentos de negocio, story maps, diagramas, épicas o **Excel**.
- Actúa como Product Owner senior (valor, independencia, trazabilidad).
- Genera un **`.md` con 13 secciones fijas** (0–13): contexto, RN, catálogo MSG, tarjetas HU/HT, spikes, trazabilidad, DoR/DoD.
- **Pausa interactiva** en §3.3 (supuestos) y §9 (dudas/spikes) para que el usuario confirme o skipee cada ítem.
- Tarjetas de backlog con Connextra, AC numerados (`[Feliz]`/`[Error]`/…), Gherkin en **español**.
- Mensajes UI: catálogo en §5 + **texto inline** en escenarios BDD (no solo el código MSG).
- Desestima filas tachadas (Excel); recomendaciones faltantes solo en §10.
- Genera `.md` + `.csv` en `AI-Outputs/po-expert-user-stories/`.

## Qué hace cada archivo

| Archivo | Rol |
|---------|-----|
| **SKILL.md** | Orquestador: rol PO, flujo con pausas HITL, 13 secciones, reglas MSG inline, checklist. |
| **md-template.md** | Estructura detallada de las 13 secciones y formato de tarjetas HU/HT. |
| **excel-input.md** | Reglas Excel: tachadas, BE/FE/BFF, issue_key vacío, escenarios vacíos, dudas → §9. |
| **csv-schema.md** | Contrato CSV (extracto por tarjeta para Jira). |
| **reference.md** | INVEST, criterios, catálogo MSG, supuestos/spikes. |

## Ejemplo de referencia (solo estructura)

`AI-Outputs/po-expert-user-stories/historias-usuario-login_v2.0.0.md` ilustra el formato de las **13 secciones** y tarjetas. El agente **no** reutiliza el contenido LOGIN: aplica la misma estructura a **cualquier** épica.

## Cómo usarlo en Cursor

1. Abrí el workspace del repo `AI-Guideline` (o un proyecto que lo tenga).
2. Pedí: *«usá el skill po-expert-user-stories»* y adjuntá épicas / docs / planillas.
3. Respondé o skipeá supuestos (§3.3) y dudas (§9) cuando el agente pause.
4. Revisá los archivos en `AI-Outputs/po-expert-user-stories/`.

Instalación opcional: copiar o enlazar esta carpeta a `~/.agents/skills/po-expert-user-stories/`.
