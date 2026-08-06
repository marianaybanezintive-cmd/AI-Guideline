# Esquema CSV — historias de usuario (skill `po-expert-user-stories`)

Formato **canónico**: 4 columnas, **un registro lógico por HU**. Description = celda multilínea (LF reales dentro de comillas = Alt+Enter).

## Fila 1 — encabezados

```
Issue Type;Issue Key;Summary;Description
```

Separador: **`;`**.

## Mapeo por columna

| Columna | Contenido |
|---------|-----------|
| **Issue Type** | `Story` |
| **Issue Key** | `HU-{CÓDIGO}.{NN}` |
| **Summary** | Título corto (tras `### HU-… — `) |
| **Description** | Cuerpo desde **COMO** (primera línea) hasta Notas/DOD. **Sin** metadatos y **sin** título “Descripción”. |

## Orden obligatorio dentro de Description

La celda **empieza con `COMO`**. No anteponer `Descripción` / `Description`.

1. COMO / QUIERO / PARA  
2. NECESIDAD / CONTEXTO  
3. Tabla ESCENARIOS  
4. **Escenarios BDD (Gherkin)** (todos los `**ID n-Escenario …**`)  
5. **Criterios de aceptación** (líneas `Que …` sin etiquetas `[Feliz]`/`[Alternativo]`/`[Error]`/`[Validación]`)  
6. **Fuera de alcance**  
7. **Notas / preguntas abiertas**  
8. DOD / DOR (si aplican)

Criterios, Fuera de alcance y Notas van **después** de cerrar Escenarios BDD (Gherkin). Nunca antes ni intercalados con Gherkin.

## Plantilla Description

```
COMO {rol}
QUIERO {requisito}
PARA {objetivo}


NECESIDAD: {…}
CONTEXTO: {…}

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | {título} |
| 4  | {título error} |

### Escenarios BDD (Gherkin)

**ID 1-Escenario {título}**

Dado {…}, cuando {…},
- entonces {…}
- SI {…},
  - {efecto}

**ID 4-Escenario {título}**

Dado {…}, cuando {…},
- entonces {…}

### Criterios de aceptación

Que {criterio verificable — sin etiquetas de tipo de escenario}
Que {criterio verificable}

### Fuera de alcance

- {…}

### Notas / preguntas abiertas

- {…}

DOD pendiente
DOR pendiente
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

## Importar en Google Sheets

**Archivo → Importar → Subir** → delimitador **punto y coma** → texto entre `"`.

## Importar en Excel (Windows)

**Datos → Desde texto/CSV** → delimitador **punto y coma** → UTF-8. Las celdas con LF internos se muestran multilínea automáticamente.

## Relación con el `.md`

La columna Description contiene el **mismo cuerpo** que la historia en el `.md`, desde `COMO` y sin el bloque de metadatos.
