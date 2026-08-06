# Git sync — commit y push configurables

Controla si, al **crear un agente** o al **generar outputs**, el agente de Cursor hace commit/push a GitHub solo o espera tu OK.

## Archivo

[`config.json`](../config.json) en la raíz de `AI-Guideline`:

```json
{
  "git_sync": {
    "mode": "manual",
    "apply_to": {
      "new_agents": true,
      "agent_outputs": true
    },
    "remote": "origin"
  }
}
```

## Modos

| Valor | Qué hace |
|-------|----------|
| `"manual"` | Default. Deja archivos listos y pregunta antes de commit/push. |
| `"automatic"` | Al terminar, commit + push a `origin` (rama actual) sin preguntar. |

## Alcances (`apply_to`)

| Flag | Carpeta | Ejemplo |
|------|---------|---------|
| `new_agents` | `AI-Agents/` | Nuevo skill, cambios a `SKILL.md`, scripts |
| `agent_outputs` | `AI-Outputs/` | Informe de sprint, paquete de arquitectura, reportes |

Poné un flag en `false` si ese alcance nunca debe ir automático (aunque `mode` sea `automatic`).

## Cómo cambiarlo

Editá `mode` en `config.json`:

```json
"mode": "automatic"
```

o volvé a:

```json
"mode": "manual"
```

La regla de Cursor [`.cursor/rules/git-sync.mdc`](../.cursor/rules/git-sync.mdc) hace que todos los agentes lean esta config.

## Override puntual

En el chat podés forzar una corrida:

- *«generá el informe y subilo a GitHub»* → commit + push aunque esté en `manual`
- *«generá pero no hagas commit»* → no git aunque esté en `automatic`
