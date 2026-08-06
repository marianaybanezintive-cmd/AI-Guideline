# Referencia — parseo MD y publicación Jira

## Cómo partir el Markdown de po-expert-user-stories

1. Cabecera global (`# Historias…` + tabla): extraer Origen, Alcance, Épica Jira si existe.
2. Cada historia empieza en un heading `###` que matchee:
   - `HU-{CODE}.{NN} — {Título}`
   - o `TA-{CODE}.{NN} — {Título}` / `Task …`
3. Dentro del bloque, hasta el próximo `### HU-` / `### TA-` o fin de épica:
   - Sección `#### Metadatos y alcance de la historia` (o Identificación) → **solo metadatos**, no va a Jira.
   - Cuerpo desde la primera línea que sea `COMO` (case-insensitive al inicio de línea).

### Issue type

| Señal en MD | issueType Jira |
|-------------|----------------|
| `Tipo: Tarea` / `Issue Type: Task` / heading `TA-` | `Task` (o `Tarea` si el proyecto usa ese nombre — probar y ajustar) |
| Default / `Story` / `Historia` / `HU-` | `Story` (o `Historia` según `config.json`) |

### Summary limpio (sin IDs)

Del heading `### HU-GF.01 — Carga manual de facturas` → summary = `Carga manual de facturas`.

- **Eliminar** del título cualquier `HU-…`, `LO-…`, `RN-…`, `TA-…`.
- **No** poner el Issue Key de Jira en el título (tampoco como reemplazo).
- El título es solo el nombre funcional de la historia/tarea.

### Description — incluir / excluir

**Incluir** (en este orden, si existen): COMO/QUIERO/PARA → NECESIDAD/CONTEXTO → ESCENARIOS (tabla) → Escenarios BDD (Gherkin) → Criterios de aceptación → Fuera de alcance → Notas / preguntas abiertas → DOD/DOR.

**Excluir:** Metadatos y alcance; Identificación; cabecera global; glosario; checklist; línea `Descripción`.

## Códigos temporales → Issue Key

Patrones típicos (token completo, no substring):

- `HU-[A-Z0-9]{2,4}\.\d{2}`
- `LO-\d{1,3}` / `LO-\d{2}`
- `RN-\d{1,3}`
- `TA-[A-Z0-9]{2,4}\.\d{2}`

Aliases: si metadatos dicen ID `HU-LO.03` y el Excel usaba `LO-03`, mapear ambos al mismo Issue Key.

**Solo en Description:** al reemplazar, usar el Issue Key (ej. `MAGIA-456`). No eliminar la referencia: **sustituir** el código temporal por la clave Jira.  
No aplicar esta sustitución al summary: ahí los IDs se quitan, no se cambian por Issue Key.

## Vínculo a la épica (`customFields`)

Probar en orden:

1. Team-managed: `"parent": { "key": "MAGIA-12" }`
2. Company-managed Epic Link: leer una Story hija existente con `read_jira_issue` y copiar el custom field (a menudo `customfield_10014` = string `"MAGIA-12"`).
3. Si falla: crear sin parent, reportar, pedir el field ID al usuario.

## Por qué dos fases

Automatización de Jira al **create** sobrescribe Description. Crear sin cuerpo; actualizar con REST (`scripts/update_descriptions.py`) cuando el MCP no expone update.
