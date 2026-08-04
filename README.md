# AI-Guideline

Repositorio de **agentes de IA** y **artefactos generados** para el equipo MAGIA / Banco Atlas.

| Carpeta | Contenido |
|---------|-----------|
| [`AI-Agents/`](AI-Agents/) | Definición de agentes (skills, scripts, configuración) |
| [`AI-Outputs/`](AI-Outputs/) | Informes y outputs generados por cada agente |

## Agentes disponibles

| Agente | Descripción | Output |
|--------|-------------|--------|
| [sprint-health-check](AI-Agents/sprint-health-check/) | Validación de salud del sprint en curso (Jira MAGIA) | [`AI-Outputs/sprint-health-check/`](AI-Outputs/sprint-health-check/) |

## Primer uso — credenciales de Jira (una sola vez)

Los agentes que consultan Jira necesitan un **API token** personal. No va en este repo.

1. Abrí la **terminal integrada de Cursor**: `` Ctrl+` `` (o *Terminal → New Terminal*).
2. Ejecutá:

```powershell
powershell -ExecutionPolicy Bypass -File "AI-Agents/sprint-health-check/scripts/set_credentials.ps1"
```

3. Ingresá tu correo de Atlassian y el token generado en  
   https://id.atlassian.com/manage-profile/security/api-tokens

Eso guarda las variables en tu perfil de Windows. Los scripts las leen automáticamente en futuras ejecuciones.

## Generar un informe de sprint

Desde la raíz del repo:

```powershell
powershell -ExecutionPolicy Bypass -File "AI-Agents/sprint-health-check/scripts/run_health_check.ps1"
```

El informe queda en `AI-Outputs/sprint-health-check/` listo para commitear.
