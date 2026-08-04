# AI-Agents

Cada subcarpeta es un **agente** usable desde Cursor (skill) o desde la línea de comandos (scripts).

## Convenciones

- `SKILL.md` — instrucciones para el agente de Cursor
- `config.json` — configuración del proyecto (tablero, estados, umbrales)
- `scripts/` — pipeline ejecutable (fetch → analyze → render)
- `references/` — criterios de interpretación y documentación de apoyo

## Instalación en Cursor (opcional)

Para invocar el agente por nombre en cualquier proyecto, copiá o enlazá el skill en:

```
~/.agents/skills/sprint-health-check/
```

O pedile al agente de Cursor: *"usá el skill sprint-health-check del repo AI-Guideline"*.
