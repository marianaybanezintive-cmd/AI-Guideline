# Input Excel — reglas específicas

Aplicar **solo** cuando el input principal sea un Excel/Sheets con columnas reconocibles (o equivalentes).  
Si el origen es Mural, Figma, POC, diagrama, etc., o el Excel tiene **otro formato de columnas**, estas reglas **no** se fuerzan: usar el flujo general del `SKILL.md` e indicar en la cabecera del `.md` el origen y las limitaciones.

## Columnas canónicas (nombres flexibles)

| Columna esperada | Alias aceptados | Uso |
|------------------|-----------------|-----|
| `issue_key` | Issue Key, ID, Código, HU | ID temporal (`HU-…`, `LO-…`, etc.) |
| `issue_type` | Tipo, Type | `Story` / `Historia` / `Task` / `Tarea` |
| `summary` | Título, Resumen | Título de la historia |
| `objetivo` | Objetivo, PARA, Goal | Valor / para qué |
| `escenarios` | Escenarios, Scenarios | Títulos o lista de escenarios |
| `dudas` | Dudas, Notas, Preguntas | Notas / preguntas abiertas |

Otras columnas (capa, BE/FE/BFF, prioridad, dependencia) se usan si existen.

## Reglas obligatorias (Excel)

### 1. Desestimar tachadas

- Ignorar filas o celdas con **texto tachado** (strikethrough).
- Si solo parte de una celda está tachada, omitir ese fragmento.
- Si toda la fila está tachada o marcada como desestimada/cancelada: **no** generar HU.
- Registrar **cada fila** en §2 (Matriz de inclusión / desestimación) con motivo. Cerrar §2 con resumen numérico.

### 2. Separar por capa BE / FE / BFF

- Redactar y organizar las historias según capa cuando el Excel lo indique o el contenido lo requiera:
  - **FE**: UI, pantallas, validaciones de formulario visibles, UX.
  - **BFF**: orquestación, contratos front↔back, agregación de APIs.
  - **BE**: dominio, persistencia, reglas de negocio server-side, jobs, integraciones.
- Si una fila mezcla capas: **partir** en HUs distintas (una por capa), compartiendo objetivo de negocio y enlazando dependencias.
- Si la fila ya es de una sola capa: una HU; poner **Capa:** `FE` | `BFF` | `BE` en Metadatos.
- En §6/§7, etiquetar tipo `HU-FE`, `HU-BE` o `HT` según capa. Agrupar tarjetas por capa si mejora la lectura.

> Esto **prioriza** la separación por capa del Excel frente a la heurística general “no partir por capa técnica” de `reference.md`.

### 3. `issue_key` vacío → crear igual

- Si `issue_key` está vacío: **igual** generar la historia.
- Asignar ID temporal nuevo `HU-{CÓDIGO}.{NN}` (siguiente libre en el lote).
- En la tarjeta y §2: marcar key como *propuesto*; nota en §11 si aplica.

### 4. `escenarios` vacío → derivar de Summary + Objetivo

- Si `escenarios` está vacío o es “N/A”:
  - Inferir al menos: **1 escenario feliz** y **1 de error/validación** a partir de `summary` + `objetivo`.
  - Documentar en Notas de la tarjeta: “Escenarios derivados de Summary/Objetivo (columna Escenarios vacía)”.

### 5. Escenarios del Excel → Gherkin completo

- Transcribir `escenarios` literalmente en **Escenarios fuente** de la tarjeta.
- Expandir a **AC numerados** y bloque **Escenarios BDD** en Gherkin **español** (`Característica`, `Dado`, `Cuando`, `Entonces`, `Y`).
- Incluir validaciones, errores y mensajes UI (**MSG-XX con texto inline** desde §5) cuando el escenario lo requiera.
- No dejar la columna Escenarios como viñetas crudas sin expandir.

### 6. Dudas del Excel → §9

- Consolidar la columna `dudas` (y contradicciones detectadas) en **§9 Spikes y decisiones pendientes** con IDs `S-01`, `S-02`, …
- Dudas puntuales de una HU pueden repetirse brevemente en **Notas** de la tarjeta, pero la tabla §9 es el registro maestro.
- Tras redactar §9, aplicar **pausa HITL** (responder o skip por ítem) según `SKILL.md`.

### 7. Supuestos → §3.3

- Supuestos técnicos o de negocio inferidos del Excel/documentos van a **§3.3** (`SUP-01`, …), no dispersos en Notas.
- Tras redactar §3.3, aplicar **pausa HITL** según `SKILL.md`.

### 8. Recomendaciones → §10 (sección aparte)

En **§10 Recomendaciones del PO — historias faltantes** (no mezclar con tarjetas §6/§7):

- Historias que **no están** en el Excel pero el PO considera necesarias (`R-01`, …).
- Subsecciones 10.1 (imprescindibles) y 10.2 (recomendadas) con prioridad sugerida.
- Escenarios faltantes de una HU existente pueden citarse en §10 o en Notas de la tarjeta, **no** inventados dentro de BDD como si vinieran del Excel.

## Mapeo fila Excel → documento `.md`

| Excel | Destino |
|-------|---------|
| Cada fila | §2 matriz inclusión/desestimación |
| `issue_key` (o generado) | Key de tarjeta §6/§7 + Issue Key CSV |
| `issue_type` | Tipo tarjeta + Issue Type CSV |
| `summary` | Título tarjeta + Summary CSV |
| `objetivo` | Connextra «para» + Valor de negocio |
| `escenarios` | Escenarios fuente + AC + Gherkin |
| `dudas` | §9 (+ Notas tarjeta si aplica) |
| Capa / BE-FE-BFF | Tipo `HU-FE` / `HU-BE` / `HT` |
| Inconsistencias | §11 Observaciones |
| Trazabilidad HU-endpoint | §12 Matriz |

## Si el formato del Excel cambia

1. Mapear columnas por semántica (no exigir nombres exactos).
2. Si faltan columnas clave (`summary` u objetivo): pedir aclaración o declarar supuestos.
3. Anotar en cabecera del `.md`: columnas detectadas y reglas Excel aplicadas / no aplicadas.
