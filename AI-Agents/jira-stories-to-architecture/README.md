# Jira Stories → Architecture — Estructura

```
AI-Agents/jira-stories-to-architecture/
├── SKILL.md                         ← Orquestador (punto de entrada)
├── reference.md                     ← Plantillas Mermaid + convenciones API/ER
└── scripts/
    └── render_mermaid.py            ← Mermaid (.mmd) → PNG (mermaid-cli vía npx)

AI-Outputs/po-architect-agent/
└── {YYYY-MM-DD}-{slug}/             ← Paquete generado por cada ejecución
    ├── README.md                    ← Índice de artefactos + historias fuente
    ├── 00-summary.md                ← Síntesis PO + decisiones de arquitectura
    ├── 01-c4-context.mmd / .png     ← C4 contexto
    ├── 02-c4-containers.mmd / .png  ← C4 contenedores FE / BFF / BE
    ├── 03-component-fe.mmd / .png   ← Componentes Frontend
    ├── 04-component-bff.mmd / .png  ← Componentes BFF
    ├── 05-component-be.mmd / .png   ← Componentes Backend
    ├── 06-er-database.mmd / .png    ← Modelo de datos (ER)
    ├── 07-sequence-{flow}.mmd / .png ← Secuencias por flujo principal
    ├── 08-user-flow-entes.mmd / .png
    ├── 09-user-flow-usuarios.mmd / .png
    ├── 10-user-flow-notificaciones.mmd / .png
    ├── 11-api-rest-bff.md           ← Contratos REST del BFF (UI)
    ├── 12-api-rest-be.md            ← Contratos REST del BE (dominio)
    └── 13-traceability.md           ← Matriz HU ↔ endpoint ↔ entidad ↔ diagrama
```

## Qué hace el skill

- Lee historias de usuario desde **Jira** (MCP `user-jira`) o texto pegado (modo manual)
- Extrae título, descripción, criterios de aceptación, subtareas, épica, labels y comentarios
- Analiza como **PO**: actores, entidades, capacidades, flujos, notificaciones, NFR y dependencias
- Declara **supuestos** cuando falta info crítica (no bloquea el diseño)
- Diseña arquitectura en capas **FE → BFF → BE** (+ DB y servicios externos)
- Genera diagramas **C4** (contexto y contenedores)
- Genera diagramas de **componentes** por capa (FE, BFF, BE)
- Genera **modelo ER** de base de datos
- Genera **secuencias** por flujo principal de negocio
- Genera **user flows** de Entes, Usuarios y Notificaciones
- Documenta **APIs REST** BFF (orientadas a UI) y BE (dominio), estilo OpenAPI
- Construye matriz de **trazabilidad** HU ↔ endpoint ↔ entidad ↔ diagrama
- Escribe todo en `AI-Outputs/po-architect-agent/{fecha}-{slug}/`
- Renderiza cada `.mmd` a **PNG** con `scripts/render_mermaid.py`
- En el chat solo resume rutas, decisiones y supuestos (no vuelca diagramas enteros)

## Qué hace cada archivo

| Archivo | Rol |
|---------|-----|
| **SKILL.md** | Orquestador: entrada Jira/manual, análisis PO, diseño, checklist de artefactos y cierre |
| **reference.md** | Plantillas Mermaid (C4, ER, secuencia, flows) y convenciones REST/nomenclatura |
| **scripts/render_mermaid.py** | Convierte uno o todos los `.mmd` de una carpeta a `.png` con `@mermaid-js/mermaid-cli` |

## Cómo usarlo

```
Usa jira-stories-to-architecture con PROJ-101, PROJ-102
```

O con JQL / historias pegadas (modo AR).

### Regenerar PNG

```powershell
python AI-Agents/jira-stories-to-architecture/scripts/render_mermaid.py "AI-Outputs/po-architect-agent/{YYYY-MM-DD}-{slug}"
```

Requiere **Node.js / npx**.
