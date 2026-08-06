# Agente PO + Arquitecto SR (Alex)

Agente dual **Product Owner senior** + **Arquitecto de Software SR** (APIs REST). Lee historias de usuario (Jira o texto) y genera un paquete de arquitectura completo en Mermaid y PNG.

**Output:** `AI-Outputs/po-architect-agent/{YYYY-MM-DD}-{slug}/`

---

## Qué hace

- Lee historias de usuario desde **Jira** (MCP `user-jira`) o desde texto pegado manualmente
- Analiza como **PO**: actores, entidades, flujos, notificaciones, dependencias y supuestos
- Diseña arquitectura con capas **FE / BFF / BE** separadas
- Genera diagramas **C4** (contexto y contenedores)
- Genera diagramas de **componentes** por capa (FE, BFF, BE)
- Genera **modelo de base de datos** (ER en Mermaid)
- Genera **diagramas de secuencia** por flujo principal
- Genera **user flows** de Entes, Usuarios y Notificaciones
- Documenta **contratos API REST** (BFF orientado a UI + BE de dominio)
- Construye matriz de **trazabilidad** HU ↔ endpoint ↔ entidad ↔ diagrama
- Exporta cada diagrama a **`.mmd` (Mermaid)** y **`.png`**
- Guarda todos los resultados en **`AI-Outputs/po-architect-agent/`** (nunca en `AI-Agents/`)

### Menú del agente

| Code | Acción |
|------|--------|
| **JA** | Paquete completo desde historias Jira |
| **AR** | Paquete completo desde historias pegadas (sin Jira) |
| **DG** | Un diagrama Mermaid puntual + PNG |
| **JR** | Solo lectura/síntesis de Jira (sin arquitectura) |

---

## Estructura

```
AI-Agents/
├── po-architect-agent/                      ← Persona y menú del agente (Alex)
│   ├── SKILL.md                             ← Activación, rol PO+Arquitecto, dispatch del menú
│   ├── customize.toml                       ← ✏️ Persona, principios, facts y menú (JA/AR/DG/JR)
│   ├── examples.md                          ← Ejemplos de invocación (Jira, JQL, manual, DG)
│   └── README.md                            ← Este archivo
│
├── jira-stories-to-architecture/            ← Workflow de generación de arquitectura
│   ├── SKILL.md                             ← Orquestador: Jira → análisis → artefactos → PNG
│   ├── reference.md                         ← Plantillas Mermaid (C4, ER, secuencia, flows, REST)
│   └── scripts/
│       └── render_mermaid.py                ← Mermaid (.mmd) → PNG (mermaid-cli vía npx)
│
AI-Outputs/
└── po-architect-agent/                      ← Resultados de cada ejecución (no editar el skill aquí)
    ├── README.md                            ← Convención de nombres de output
    └── {YYYY-MM-DD}-{slug}/                 ← Paquete generado por corrida
        ├── README.md                        ← Índice del paquete
        ├── 00-summary.md                    ← Síntesis PO + decisiones de arquitectura
        ├── 01-c4-context.mmd / .png         ← C4 contexto
        ├── 02-c4-containers.mmd / .png      ← C4 contenedores FE / BFF / BE
        ├── 03-component-fe.mmd / .png       ← Componentes Frontend
        ├── 04-component-bff.mmd / .png      ← Componentes BFF
        ├── 05-component-be.mmd / .png       ← Componentes Backend
        ├── 06-er-database.mmd / .png        ← Modelo de datos (ER)
        ├── 07-sequence-{flow}.mmd / .png    ← Secuencias por flujo
        ├── 08-user-flow-entes.mmd / .png    ← User flow Entes
        ├── 09-user-flow-usuarios.mmd / .png ← User flow Usuarios
        ├── 10-user-flow-notificaciones…     ← User flow Notificaciones
        ├── 11-api-rest-bff.md               ← Contratos REST del BFF
        ├── 12-api-rest-be.md                ← Contratos REST del BE
        └── 13-traceability.md               ← Matriz HU ↔ API ↔ entidad ↔ diagrama
```

### Detalle de archivos del skill

| Archivo | Rol |
|---------|-----|
| `po-architect-agent/SKILL.md` | Punto de entrada del agente: saluda como Alex, carga persona y enruta al menú o al workflow |
| `po-architect-agent/customize.toml` | Configuración editable: nombre, icono, principios, facts persistentes y códigos de menú |
| `po-architect-agent/examples.md` | Casos de uso listos para copiar (claves Jira, JQL, modo manual, diagrama puntual) |
| `jira-stories-to-architecture/SKILL.md` | Pipeline completo: fetch Jira → análisis PO → diseño → escritura de artefactos → render PNG |
| `jira-stories-to-architecture/reference.md` | Plantillas y convenciones Mermaid/REST/ER para mantener diagramas consistentes |
| `jira-stories-to-architecture/scripts/render_mermaid.py` | Convierte uno o todos los `.mmd` de una carpeta a `.png` con `@mermaid-js/mermaid-cli` |

---

## Cómo usarlo

Desde la raíz del repo **AI-Guideline**, en Cursor:

```
Activa el skill po-architect-agent
```

O directo al workflow:

```
Usa jira-stories-to-architecture con PROJ-101, PROJ-102
```

### Regenerar PNG

```powershell
python AI-Agents/jira-stories-to-architecture/scripts/render_mermaid.py AI-Outputs/po-architect-agent/{YYYY-MM-DD}-{slug}
```

Requiere **Node.js / npx** (el script usa `npx -y @mermaid-js/mermaid-cli`).

---

## Instalación opcional en Cursor

Para invocar los skills por nombre en cualquier proyecto, copiá o enlazá **ambos** folders:

```
~/.agents/skills/po-architect-agent/
~/.agents/skills/jira-stories-to-architecture/
```
