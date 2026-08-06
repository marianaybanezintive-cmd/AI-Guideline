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
- Listar en el informe final (cabecera o anexo breve) cuántas filas se omitieron por tachado.

### 2. Separar por capa BE / FE / BFF

- Redactar y organizar las historias según capa cuando el Excel lo indique o el contenido lo requiera:
  - **FE**: UI, pantallas, validaciones de formulario visibles, UX.
  - **BFF**: orquestación, contratos front↔back, agregación de APIs.
  - **BE**: dominio, persistencia, reglas de negocio server-side, jobs, integraciones.
- Si una fila mezcla capas: **partir** en HUs distintas (una por capa), compartiendo objetivo de negocio y enlazando dependencias.
- Si la fila ya es de una sola capa: una HU; poner **Capa:** `FE` | `BFF` | `BE` en Metadatos.
- En el `.md`, agrupar bajo subtítulos `# FE` / `# BFF` / `# BE` (dentro de la épica) cuando haya varias capas.

> Esto **prioriza** la separación por capa del Excel frente a la heurística general “no partir por capa técnica” de `reference.md`.

### 3. `issue_key` vacío → crear igual

- Si `issue_key` está vacío: **igual** generar la historia.
- Asignar ID temporal nuevo `HU-{CÓDIGO}.{NN}` (siguiente libre en el lote).
- En Metadatos: `ID Historia` = el generado; nota breve “issue_key vacío en Excel”.

### 4. `escenarios` vacío → derivar de Summary + Objetivo

- Si `escenarios` está vacío o es “N/A”:
  - Inferir al menos: **1 escenario feliz** y **1 de error/validación** a partir de `summary` + `objetivo`.
  - Documentar en Notas: “Escenarios derivados de Summary/Objetivo (columna Escenarios vacía)”.

### 5. Escenarios del Excel → Gherkin completo

- Cada ítem/título en `escenarios` va a la tabla ESCENARIOS.
- Por cada título: bloque `**ID n-Escenario {título}**` con lógica Gherkin (`Dado` / `cuando` / `entonces`, ramas `SI` si aplica).
- Incluir validaciones, errores, mensajes y aclaraciones **cuando el escenario lo requiera** (no inventar capas de error genéricas si el título es claramente solo feliz).
- No dejar la columna Escenarios como viñetas crudas sin expandir.

### 6. Dudas del Excel

- Llevar la columna `dudas` a **Notas / preguntas abiertas** de la HU correspondiente.
- Si está vacía: `Ninguna por ahora.` (salvo notas propias del agente).

### 7. Recomendaciones de escenarios faltantes (sección aparte)

Al **final del `.md`**, sección separada (no mezclar dentro de cada HU):

```markdown
## Recomendaciones de escenarios faltantes

### {ID o Summary de la HU}
- {escenario sugerido y por qué}
```

- Listar, a criterio PO, escenarios que **faltarían** (error, vacío, permisos, timeout, duplicados, etc.) no cubiertos por el Excel.
- No inventarlos dentro de Escenarios BDD como si vinieran del Excel; van **solo** en esta sección de recomendaciones.
- Si no hay sugerencias: `Sin recomendaciones adicionales.`

## Mapeo fila Excel → plantilla HU

| Excel | Destino en HU |
|-------|----------------|
| `issue_key` (o generado) | Metadatos → ID Historia / Issue Key CSV |
| `issue_type` | Metadatos + Issue Type CSV (`Story`/`Task`) |
| `summary` | Título tras `### ID — ` y QUIERO (ajustado) |
| `objetivo` | PARA + aporte a NECESIDAD |
| `escenarios` | Tabla ESCENARIOS + bloques Gherkin |
| `dudas` | Notas / preguntas abiertas |
| Capa / BE-FE-BFF | Metadatos → **Capa** + agrupación en el MD |

## Si el formato del Excel cambia

1. Mapear columnas por semántica (no exigir nombres exactos).
2. Si faltan columnas clave (`summary` u objetivo): pedir aclaración o declarar supuestos.
3. Anotar en cabecera del `.md`: columnas detectadas y reglas Excel aplicadas / no aplicadas.
