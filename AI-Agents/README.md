# AI-Agents

Cada subcarpeta es un **agente** usable desde Cursor (skill) o desde la línea de comandos (scripts).

## Agentes

| Agente | Descripción |
|--------|-------------|
| [sprint-health-check](sprint-health-check/) | Validación de salud del sprint en curso (Jira) |
| [sm-mass-clone](sm-mass-clone/) | Scrum Master: clonado masivo de issues (épica / sprint / backlog) + reporte MD |
| [po-expert-user-stories](po-expert-user-stories/) | Product Owner: épicas y documentos de negocio → historias detalladas (MD + CSV) |
| [po-architect-agent](po-architect-agent/) | Alex — PO + Arquitecto SR: menú y persona dual |
| [jira-stories-to-architecture](jira-stories-to-architecture/) | Workflow: historias Jira → arquitectura FE/BFF/BE (Mermaid + PNG) |

## Convenciones

- `SKILL.md` — instrucciones para el agente de Cursor
- `config.json` — configuración del proyecto (tablero, estados, umbrales), cuando aplica
- `scripts/` — pipeline ejecutable (fetch → analyze → render), cuando aplica
- `references/` o archivos `*.md` hermanos — criterios, esquemas y documentación de apoyo

## Instalación en Cursor (opcional)

Para invocar el agente por nombre en cualquier proyecto, copiá o enlazá el skill en:

```
~/.agents/skills/<nombre-del-agente>/
```

Ejemplos:

```
~/.agents/skills/sprint-health-check/
~/.agents/skills/sm-mass-clone/
~/.agents/skills/po-expert-user-stories/
~/.agents/skills/po-architect-agent/
~/.agents/skills/jira-stories-to-architecture/
```

O pedile al agente de Cursor: *"usá el skill po-architect-agent del repo AI-Guideline"*.

**Nota:** `po-architect-agent` y `jira-stories-to-architecture` se usan juntos. Instalá ambos si querés el menú completo de Alex.


-------------------------------------------------------------------------------------------------
DOCUMENTACIÓN


`po-expert-user-stories`

1. Qué hace el skill
Lee docs de negocio, story maps, diagramas y épicas.
Actúa como Product Owner senior.
Parte épicas en historias de tamaño de sprint.
Asigna IDs HU-{CÓDIGO}.{NN} (ej. HU-GF.01).
Redacta COMO / QUIERO / PARA, NECESIDAD y CONTEXTO.
Arma tabla ESCENARIOS (títulos) + Escenarios BDD (Gherkin) por ID.
Escribe criterios como “Que …” (sin Feliz/Alternativo/Error).
Agrega Fuera de alcance y Notas después del Gherkin.
Genera un .md completo con todas las HU.
Genera un .csv (;, una fila por HU).
Guarda ambos en AI-Outputs/po-expert-user-stories/.
En el chat solo confirma rutas y conteo.

2. Estructura de archivos
AI-Agents/po-expert-user-stories/
├── SKILL.md              ← Instrucciones del agente (punto de entrada en Cursor)
├── csv-schema.md         ← Plantilla y reglas del CSV (4 columnas, `;`, Description)
├── reference.md          ← Guía corta INVEST, criterios y story map
└── README.md             ← Esta documentación de estructura
AI-Outputs/po-expert-user-stories/
└── po-historias-usuario-{fecha}-{slug}.md|.csv   ← Resultados al ejecutar


Archivo	        | Qué hace
SKILL.md        | Orquestador: rol PO, entradas, flujo, plantilla de HU, checklist y rutas de salida.
csv-schema.md   | Contrato del CSV: cabeceras, orden del cuerpo en Description, reglas de importación.
reference.md    | Apoyo opcional (INVEST, partir épicas, criterios, story map).
README.md       | Documentación de estructura y uso.


-------------------------------------------------------------------------------------------------

`po-architect-agent` y `jira-stories-to-architecture`

Agente de Diagramas — Estructura
scripts/diagrams/
├── run_pipeline.sh              ← Orchestrador (punto de entrada)
├── config/
│   ├── issues.json              ← ✏️ Editar por proyecto (issue keys, BFFs)
│   └── pipeline.config.json    ← ✏️ Editar rutas output y nombre proyecto
└── skills/
    ├── 01_jira_fetcher.js       ← Descarga historias de Jira
    ├── 02_extract_mermaid.py    ← Extrae bloques Mermaid del .md del agente
    ├── 03_render_svg.sh         ← Mermaid → SVG (mermaid-cli)
    ├── 04_svg_to_png.js         ← SVG → PNG @2x (Puppeteer)
    └── 05_build_outputs.py      ← PNGs finales + .drawio

EJECUCIÓN
Solo 3 pasos:

1. Editar scripts/diagrams/config/issues.json con los nuevos issue keys y BFFs:

{
  "issues": ["NUEVO-1", "NUEVO-2", "NUEVO-3"],
  "projectName": "Nombre del nuevo proyecto",
  "bffs": { "BFF NUEVO": ["Dominio1", "Dominio2"] },
  "microservicio_be": "API NUEVO"
}
2. Decirle al agente en un nuevo chat:

"Generar diagramas de arquitectura desde Jira para los issues en scripts/diagrams/config/issues.json"

La regla Cursor (.cursor/rules/architecture-diagrams.mdc) guía automáticamente al agente para que:

Llame al skill 01 para bajar las historias
Analice y genere los diagramas Mermaid correctos
Ejecute los skills 02–05 para renderizar PNGs y .drawio
Haga commit y push
3. En ~5 minutos tenés los 16+ PNGs y el .drawio en assets/diagramas/.