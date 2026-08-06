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
| [po-expert-user-stories](AI-Agents/po-expert-user-stories/) | Product Owner: documentos de negocio y épicas → historias detalladas (MD + CSV) | [`AI-Outputs/po-expert-user-stories/`](AI-Outputs/po-expert-user-stories/) |
| [po-architect-agent](AI-Agents/po-architect-agent/) + [jira-stories-to-architecture](AI-Agents/jira-stories-to-architecture/) | PO + Arquitecto SR: historias Jira → diagramas C4, BD, FE/BFF/BE, secuencias y user flows (Mermaid + PNG) | [`AI-Outputs/po-architect-agent/`](AI-Outputs/po-architect-agent/) |

## Primer uso — credenciales de Jira (una sola vez)

Los agentes que consultan Jira necesitan un **API token** personal. No va en este repo.
Generalo en https://id.atlassian.com/manage-profile/security/api-tokens

Abrí la **terminal integrada de Cursor** (Ctrl+`) en la raíz del repo.

### ¿El pegado falla o solo guarda 1 carácter?

En Cursor, `Read-Host -AsSecureString` solo captura 1 carácter al pegar. Usá una de estas opciones:

**Opción A — archivo de texto (recomendada):**
1. Pegá el token en un `.txt` (Bloc de notas)
2. Ejecutá:

```powershell
powershell -ExecutionPolicy Bypass -File "AI-Agents/sprint-health-check/scripts/set_credentials.ps1" -TokenFile "C:\Users\tu_usuario\token-jira.txt"
```

3. Borrá el `.txt` después

**Opción B — pegado visible:**

```powershell
powershell -ExecutionPolicy Bypass -File "AI-Agents/sprint-health-check/scripts/set_credentials.ps1"
```

El script pide el token en texto visible (se ve un instante, pero pega completo).

Eso guarda las variables en tu perfil de Windows. Los scripts las leen automáticamente en futuras ejecuciones.

## Generar un informe de sprint

Desde la raíz del repo:

```powershell
powershell -ExecutionPolicy Bypass -File "AI-Agents/sprint-health-check/scripts/run_health_check.ps1"
```

El informe queda en `AI-Outputs/sprint-health-check/` listo para commitear.

## Generar arquitectura desde historias Jira

En Cursor, desde este repo:

```
Activa el skill po-architect-agent
```

O directamente:

```
Usa jira-stories-to-architecture con PROJ-101, PROJ-102
```

El paquete (Mermaid + PNG + APIs) queda en `AI-Outputs/po-architect-agent/{fecha}-{slug}/`.
