# Modo degradado: sin credenciales REST

Si no están definidas `JIRA_BASE_URL` / `JIRA_EMAIL` / `JIRA_API_TOKEN`, el informe se
puede armar parcialmente con el MCP `user-jira`. **Avisar siempre al usuario que el
informe está incompleto y por qué.**

## Estado de las herramientas del MCP

| Herramienta | Estado | Uso |
|-------------|--------|-----|
| `list_agile_boards` | Funciona | Resolver el tablero del proyecto |
| `list_sprints_for_board` | Funciona | Sprint activo (`state: "active"`) |
| `get_sprint_details` | Funciona | Lista completa de issues: clave, título, estado, asignado |
| `read_jira_issue` | Funciona parcial | Tipo, prioridad, descripción, `created`, `updated`. **Sin** changelog, story points ni padre/subtarea |
| `search_jira_issues` | **Roto** | Falla con `Cannot read properties of undefined (reading 'map')` |
| `get_user_activity_history` | **Roto** | Falla con `response.data.issues is not iterable` |

Las dos últimas fallan porque el MCP llama al endpoint `/rest/api/3/search`, retirado por
Atlassian en favor de `/rest/api/3/search/jql`. No hay workaround desde el MCP.

## Qué se puede y qué no

| Sección del informe | Con MCP solo |
|---------------------|--------------|
| 1. Estado del sprint | Parcial — conteos por estado sí, puntos no |
| 2. Avance de principales | Parcial — sin puntos ni rollup de subtareas |
| 3. Ítems estancados | **Aproximado** — sólo `updated`, no la última transición de estado |
| 4. Sin estimación | **No disponible** — el MCP no devuelve story points |
| 5. Sin asignación | Completo |
| 6. Puntos por persona | **No disponible** |
| 7. Evolución diaria | **No disponible** — requiere changelog |
| 8. Cambios de alcance | **No disponible** — requiere changelog |
| 9. Consistencia de QA | Parcial — la relación padre/subtarea se infiere por el orden de `get_sprint_details`, sin fechas de QA |
| 10. Goals vs tareas | Completo (el goal viene en `get_sprint_details`) |
| 11–15 (burndown, WIP, scope creep, bloqueantes, calidad) | **No disponible** |

## Inferencia de padre/subtarea sin REST

`get_sprint_details` devuelve los issues en orden de rank del tablero, que agrupa las
subtareas debajo de su historia. Se puede inferir la jerarquía tomando cada ítem cuyo
título coincida con un patrón de subtarea (`desarrollo`, `QA Automation`,
`Ejecucion de tests`) y asociándolo a la última historia previa de la lista.

Es una heurística frágil: sirve para señalar casos a revisar, **no** para afirmar que
falta una subtarea. Marcar estos hallazgos como "a confirmar".

## Recomendación

El modo degradado sirve para un vistazo rápido. Para el informe completo, configurar el
token de API — es un paso único y habilita las 15 secciones.
