# AI-Agents

Cada subcarpeta es un **agente** usable desde Cursor (skill) o desde la línea de comandos (scripts).

## Agentes

| Agente | Descripción |
|--------|-------------|
| [sprint-health-check](sprint-health-check/) | Validación de salud del sprint en curso (Jira) |
| [po-expert-user-stories](po-expert-user-stories/) | Product Owner: épicas y documentos de negocio → historias detalladas (MD + CSV) |
| [jira-load-user-stories](jira-load-user-stories/) | SM/PO: carga en Jira las historias del MD de po-expert (tras validación manual) |

## Convenciones

- `SKILL.md` — instrucciones para el agente de Cursor
- `config.json` — configuración del proyecto (tablero, estados, umbrales), cuando aplica
- `scripts/` — pipeline ejecutable, cuando aplica
- `references/` o archivos `*.md` hermanos — criterios, esquemas y documentación de apoyo

### Git sync (repo)

Al crear un agente nuevo o generar archivos en `AI-Outputs/`, respetá [`../config.json`](../config.json) → `git_sync` (`manual` | `automatic`). Ver [`../docs/git-sync.md`](../docs/git-sync.md).

## Instalación en Cursor (opcional)

Para invocar el agente por nombre en cualquier proyecto, copiá o enlazá el skill en:

```
~/.agents/skills/<nombre-del-agente>/
```

Ejemplos:

```
~/.agents/skills/sprint-health-check/
~/.agents/skills/po-expert-user-stories/
~/.agents/skills/jira-load-user-stories/
```

O pedile al agente de Cursor: *"usá el skill jira-load-user-stories del repo AI-Guideline"*.
