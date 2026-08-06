# Agente PO Expert User Stories — Estructura

```
AI-Agents/po-expert-user-stories/
├── SKILL.md              ← Instrucciones del agente (punto de entrada en Cursor)
├── csv-schema.md         ← Plantilla y reglas del CSV (4 columnas, `;`, Description)
└── reference.md          ← Guía corta INVEST, criterios y story map

AI-Outputs/po-expert-user-stories/
├── README.md             ← Destino de resultados (no es parte del skill)
└── po-historias-usuario-{fecha}-{slug}.md|.csv   ← Generados al ejecutar
```

## Qué hace el skill (resumen)

- Lee documentos de negocio, story maps, diagramas y descripciones de épicas.
- Actúa como Product Owner senior (valor, independencia, trazabilidad).
- Parte cada épica en historias de tamaño de sprint.
- Asigna IDs `HU-{CÓDIGO}.{NN}` (ej. `HU-GF.01`) coherentes entre MD y CSV.
- Redacta cada HU con plantilla fija: COMO / QUIERO / PARA, NECESIDAD, CONTEXTO.
- Arma tabla ESCENARIOS (solo títulos) + Escenarios BDD (Gherkin) por ID.
- Escribe criterios de aceptación como “Que …” (sin etiquetas Feliz/Alternativo/Error).
- Agrega Fuera de alcance y Notas / preguntas abiertas **después** del Gherkin.
- Genera un `.md` completo con todas las historias (entregable canónico).
- Genera un `.csv` (`;`, una fila por HU, Description multilínea desde COMO).
- Guarda ambos en `AI-Outputs/po-expert-user-stories/`.
- En el chat solo confirma rutas y conteo (no vuelve a pegar todo el documento).

## Qué hace cada archivo

| Archivo | Rol |
|---------|-----|
| **SKILL.md** | Orquestador del agente: rol PO, entradas, flujo, plantilla de HU, checklist y rutas de salida. Cursor lo carga al invocar el skill. |
| **csv-schema.md** | Contrato del CSV: cabeceras `Issue Type;Issue Key;Summary;Description`, orden del cuerpo en Description, reglas RFC 4180 / Alt+Enter, ejemplos de importación en Sheets/Excel. |
| **reference.md** | Apoyo opcional: INVEST, cómo partir épicas, criterios sólidos, tips de story map y diagramas. Se lee cuando el backlog es grande o controvertido. |

## Outputs (fuera del skill)

| Destino | Rol |
|---------|-----|
| **AI-Outputs/po-expert-user-stories/** | Carpeta de resultados. El agente escribe aquí el `.md` y el `.csv` de cada ejecución. |

## Cómo usarlo en Cursor

1. Abrí el workspace del repo `AI-Guideline` (o un proyecto que lo tenga).
2. Pedí: *“usá el skill po-expert-user-stories”* y adjuntá épicas / docs / planillas.
3. Revisá los archivos generados en `AI-Outputs/po-expert-user-stories/`.

Instalación opcional en cualquier máquina: copiar o enlazar esta carpeta a `~/.agents/skills/po-expert-user-stories/`.
