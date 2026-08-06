# AI-Agents

Cada subcarpeta es un **agente** usable desde Cursor (skill) o desde la línea de comandos (scripts).

## Agentes

| Agente | Descripción |
|--------|-------------|
| [sprint-health-check](sprint-health-check/) | Validación de salud del sprint en curso (Jira) |
| [po-expert-user-stories](po-expert-user-stories/) | Product Owner: épicas y documentos de negocio → historias detalladas (MD + CSV) |

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
~/.agents/skills/po-expert-user-stories/
```

O pedile al agente de Cursor: *"usá el skill po-expert-user-stories del repo AI-Guideline"*.
