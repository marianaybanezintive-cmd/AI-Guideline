# Agente PO Expert User Stories — Estructura

```
AI-Agents/po-expert-user-stories/
├── SKILL.md              ← Instrucciones del agente (punto de entrada en Cursor)
├── excel-input.md        ← Reglas cuando el input es Excel (columnas canónicas)
├── csv-schema.md         ← Plantilla y reglas del CSV (4 columnas, `;`, Description)
└── reference.md          ← Guía corta INVEST, criterios y story map

AI-Outputs/po-expert-user-stories/
├── README.md             ← Destino de resultados (no es parte del skill)
└── po-historias-usuario-{fecha}-{slug}.md|.csv   ← Generados al ejecutar
```

## Qué hace el skill (resumen)

- Lee documentos de negocio, story maps, diagramas, épicas o **Excel**.
- Actúa como Product Owner senior (valor, independencia, trazabilidad).
- Parte cada épica en historias de tamaño de sprint (con Excel: **BE / FE / BFF**).
- Asigna IDs `HU-{CÓDIGO}.{NN}` (crea aunque `issue_key` Excel venga vacío).
- **Desestima filas/celdas tachadas** en Excel.
- Redacta COMO / QUIERO / PARA, NECESIDAD, CONTEXTO.
- Escenarios del Excel → tabla + Gherkin completo (validaciones/errores si aplica).
- Si `escenarios` vacío → deriva de `summary` + `objetivo`.
- Criterios “Que …”; Fuera de alcance y Notas **después** del Gherkin.
- Sección aparte: **Recomendaciones de escenarios faltantes**.
- Genera `.md` + `.csv` en `AI-Outputs/po-expert-user-stories/`.
- En el chat solo confirma rutas y conteo.

## Qué hace cada archivo

| Archivo | Rol |
|---------|-----|
| **SKILL.md** | Orquestador del agente: rol PO, entradas, flujo, plantilla de HU, checklist y rutas de salida. |
| **excel-input.md** | Reglas Excel: tachadas, BE/FE/BFF, issue_key vacío, escenarios vacíos, Gherkin desde títulos, recomendaciones aparte. |
| **csv-schema.md** | Contrato del CSV (4 columnas, `;`, Description multilínea). |
| **reference.md** | INVEST, partir épicas, criterios, story map (excepción Excel para capas). |

## Outputs (fuera del skill)

| Destino | Rol |
|---------|-----|
| **AI-Outputs/po-expert-user-stories/** | Carpeta de resultados. El agente escribe aquí el `.md` y el `.csv` de cada ejecución. |

## Cómo usarlo en Cursor

1. Abrí el workspace del repo `AI-Guideline` (o un proyecto que lo tenga).
2. Pedí: *“usá el skill po-expert-user-stories”* y adjuntá épicas / docs / planillas.
3. Revisá los archivos generados en `AI-Outputs/po-expert-user-stories/`.

Instalación opcional en cualquier máquina: copiar o enlazar esta carpeta a `~/.agents/skills/po-expert-user-stories/`.
