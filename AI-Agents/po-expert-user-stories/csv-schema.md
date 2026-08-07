# Esquema CSV — historias de usuario (skill `po-expert-user-stories`)

Formato **canónico**: 4 columnas, **un registro lógico por historia elaborada** (tarjetas de §6 HU y §7 HT; opcionalmente §8 TAREA). Description = celda multilínea (LF reales dentro de comillas = Alt+Enter).

## Fila 1 — encabezados

```
Issue Type;Issue Key;Summary;Description
```

Separador: **`;`**.

## Mapeo por columna

| Columna | Contenido |
|---------|-----------|
| **Issue Type** | `Story` (HU) o `Task` (HT / TAREA) según tipo de tarjeta |
| **Issue Key** | Key estable del documento (`LO-xx`, `HU-{CÓDIGO}.{NN}`, etc.) |
| **Summary** | Título corto (tras `### {KEY} — ` en el `.md`) |
| **Description** | Cuerpo de la tarjeta **sin** la tabla de metadatos del `.md` |

## Orden obligatorio dentro de Description

La celda **empieza con la historia Connextra** (bloque `Como / quiero / para`). No anteponer metadatos ni título «Descripción».

1. **Historia** (Connextra multilínea)
2. **Valor de negocio** (HU) u **Objetivo técnico** (HT)
3. **Escenarios fuente** *(si existen)*
4. **Criterios de aceptación** (numerados, con tags `[Feliz]` / `[Alternativo]` / `[Error]` / `[Validación]`)
5. **Escenarios BDD** (bloque Gherkin en español; mensajes UI con texto inline desde §5 del `.md`)
6. **Fuera de alcance** (HU) o **Errores esperados** (HT)
7. **Notas / preguntas abiertas**
8. **Chequeo INVEST** (solo HU, si aplica)

Las secciones globales del `.md` (§0–§5, §8–§13) **no** van en el CSV — solo el contenido exportable por historia.

## Plantilla Description (HU)

```
Como {rol}
quiero {necesidad}
para {beneficio}

Valor de negocio: {texto breve}

Escenarios fuente:
{transcripción literal del input}

Criterios de aceptación:
1. [Feliz] {criterio}
2. [Error] MSG-01 — "{texto inline del catálogo §5}"

Escenarios BDD (Gherkin):
Característica: {nombre}
  Escenario: {título}
    Dado {…}
    Cuando {…}
    Entonces veo el mensaje MSG-01: "{texto literal}"

Fuera de alcance:
- {…}

Notas / preguntas abiertas:
- {…}
```

## Plantilla Description (HT)

```
Objetivo técnico: {…}

Criterios de aceptación:
1. {criterio HTTP/contrato}

Escenarios BDD (Gherkin):
Característica: {nombre}
  Escenario: {…}

Errores esperados:
| Código HTTP | Código negocio | Cuándo |
| 400 | VALIDATION_ERROR | … |

Notas / preguntas abiertas:
- {…}
```

## Reglas técnicas

| Regla | Valor |
|-------|-------|
| Separador columnas | `;` |
| Separador registros | LF fuera de comillas |
| Campos | Todos entre `"…"` |
| LF en Description | LF real dentro de `"…"` |
| No usar | `\n` literal como texto |
| Comillas internas | `"` → `""` |
| Codificación | UTF-8; BOM opcional |

## Mensajes UI en Description

Misma regla que en el `.md`: al citar `MSG-XX`, incluir el **texto del mensaje** inline (copiado del §5 del documento Markdown), no solo el código.

## Importar en Google Sheets

**Archivo → Importar → Subir** → delimitador **punto y coma** → texto entre `"`.

## Importar en Excel (Windows)

**Datos → Desde texto/CSV** → delimitador **punto y coma** → UTF-8.

## Relación con el `.md`

- El `.md` es el entregable **canónico completo** (13 secciones).
- El CSV es un **extracto por historia** para importación a Jira/backlog.
- La columna Description = cuerpo de la tarjeta §6/§7, alineado en contenido y orden con el `.md`.
