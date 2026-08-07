# Plantilla Markdown — 13 secciones obligatorias

Referencia de **estructura** para el entregable `.md` del skill `po-expert-user-stories`.  
Basada en el formato de tarjetas de backlog (ejemplo: `AI-Outputs/po-expert-user-stories/historias-usuario-login_v2.0.0.md`).

**Regla:** todo output `.md` **debe** incluir las secciones **0 a 13**, en este orden, **sin excepción**. Si una sección no aplica al input, incluirla igual con una nota explícita (p. ej. «No aplica — sin Excel de origen»).

---

## Cabecera del documento

```markdown
# Historias de Usuario — {título descriptivo de la épica o producto}

> **Versión:** v{MAJOR}.{MINOR}.{PATCH} · **Fecha:** {YYYY-MM-DD}
> **Fuente única de requerimientos:** {lista breve de documentos, planillas, diagramas}
> **Autor:** PO (elaboración de historias) · **Producto:** {nombre del producto}
> **POC / referencia de diseño:** {URL o «pendiente»} *(opcional)*
> **Generado con:** skill `po-expert-user-stories`

---

## Tabla de contenidos

0. [Qué cambia respecto de versión anterior](#0-qué-cambia-respecto-de-versión-anterior)
1. [Criterio de elaboración y alcance](#1-criterio-de-elaboración-y-alcance)
2. [Matriz de inclusión / desestimación](#2-matriz-de-inclusión--desestimación)
3. [Contexto de solución, actores y supuestos](#3-contexto-de-solución-actores-y-supuestos)
4. [Reglas de negocio transversales (RN)](#4-reglas-de-negocio-transversales-rn)
5. [Catálogo de mensajes de UI](#5-catálogo-de-mensajes-de-ui)
6. [Historias de usuario funcionales (tarjetas de backlog)](#6-historias-de-usuario-funcionales-tarjetas-de-backlog)
7. [Historias técnicas — Endpoints BFF / BE (enablers)](#7-historias-técnicas--endpoints-bff--be-enablers)
8. [Tareas técnicas / habilitadores](#8-tareas-técnicas--habilitadores)
9. [Spikes y decisiones pendientes (columna DUDAS)](#9-spikes-y-decisiones-pendientes-columna-dudas)
10. [Recomendaciones del PO — historias faltantes](#10-recomendaciones-del-po--historias-faltantes)
11. [Observaciones sobre la consistencia del input](#11-observaciones-sobre-la-consistencia-del-input)
12. [Matriz de trazabilidad HU ↔ endpoint ↔ pantalla](#12-matriz-de-trazabilidad-hu--endpoint--pantalla)
13. [Definition of Ready / Definition of Done](#13-definition-of-ready--definition-of-done)
```

---

## 0. Qué cambia respecto de versión anterior

Documentar cambios de **forma** y/o **alcance** respecto del `.md` previo del mismo producto/épica.

- **Primera elaboración:** indicar «Primera versión — no hay documento anterior» y listar criterios de forma adoptados (tarjetas, AC numerados, Gherkin en español, etc.).
- **Regeneración:** listar qué cambió (nuevas historias, supuestos confirmados, spikes resueltos, etc.).

---

## 1. Criterio de elaboración y alcance

Tabla de decisiones aplicadas al input:

| Criterio | Decisión aplicada |
|----------|-------------------|
| **Filas tachadas** (Excel) | Desestimadas; registradas en §2 |
| **Filas puntuadas / detalladas** | Elaboradas como tarjeta completa |
| **Escenarios del input** | Transcritos en *Escenarios fuente*; expandidos a AC + Gherkin |
| **Historias faltantes** | Solo en §10, no mezcladas con las del input |
| **Identificadores** | Conservar `issue_key` del input si existe; si no, generar `{CÓDIGO}-{NN}` |
| **Idioma y formato** | Español; Gherkin con palabras clave en español |

**Convención de tipos** (adaptar según dominio):

| Tipo | Significado |
|------|-------------|
| `HU-FE` | Historia de usuario con impacto principal en Front End |
| `HU-BE` | Historia cuyo valor se entrega vía backend/notificación |
| `HT` | Historia técnica (endpoint BFF/BE) |
| `TAREA` | Habilitador de infraestructura o configuración |

---

## 2. Matriz de inclusión / desestimación

Una fila por ítem del input (Excel: fila por fila; otros orígenes: capacidad por capacidad).

| Fila | Key | Summary | Tipo | Estado | Motivo |
|-----:|-----|---------|------|--------|--------|
| {n} | {KEY} | {título} | {HU-FE / HT / TAREA / —} | ✅ Incluida / ❌ Desestimada | {motivo} |

Cerrar con **Resumen** numérico (incluidas / desestimadas / HU / HT / tareas).

---

## 3. Contexto de solución, actores y supuestos

### 3.1 Perfiles de usuario (actores / dominios)

| {Dimensión 1} | {Dimensión 2} | … |
|---------------|---------------|---|

### 3.2 Componentes involucrados

Lista o tabla de sistemas, capas (FE, BFF, BE), integraciones externas.

### 3.3 Supuestos (a confirmar con el equipo técnico)

| # | Supuesto | Confirmación *(post HITL)* |
|---|----------|---------------------------|
| SUP-01 | {texto del supuesto} | {respuesta del usuario / «pendiente» / «confirmado — sin cambios»} |

> **Pausa obligatoria (skill):** tras redactar esta tabla, el agente **detiene** el flujo y ofrece al usuario responder o skipear **cada** supuesto antes de continuar con §4 en adelante.

---

## 4. Reglas de negocio transversales (RN)

| ID | Regla | Fuente |
|----|-------|--------|
| **RN-01** | {regla verificable} | {historia o documento} |

Referenciadas desde AC y Gherkin para no repetir texto.

---

## 5. Catálogo de mensajes de UI

**Fuente unificada** de textos de interfaz. Referenciados por código (`MSG-XX`) desde AC y BDD.

| Código | Contexto | Mensaje |
|--------|----------|---------|
| MSG-01 | {contexto} | "{texto literal del mensaje}" |

> Si no hay mensajes de UI en el alcance: incluir la sección con la nota «No aplica — sin impacto en pantalla».

---

## 6. Historias de usuario funcionales (tarjetas de backlog)

### {KEY} — {Título corto verificable}

| | |
|---|---|
| **Tipo** | HU-FE / HU-BE |
| **Épica** | {CÓDIGO} |
| **Actor** | {rol} |
| **Dominios** | {si aplica} |
| **Prioridad sugerida** | Must / Should / Could |
| **Depende de** | {keys o —} |
| **Habilita** | {keys o —} |
| **Pantalla POC** | {ruta o —} |

#### Historia
```
Como {rol}
quiero {necesidad}
para {beneficio}
```

#### Valor de negocio
{1–3 oraciones}

#### Escenarios fuente
> Transcripción literal del input *(si existe)*:

```text
{contenido literal}
```

#### Criterios de aceptación
1. **[Feliz]** {criterio binario verificable}
2. **[Alternativo]** {…}
3. **[Error]** {…}
4. **[Validación]** {…}

#### Escenarios BDD
```gherkin
Característica: {nombre}
  Como {rol} quiero {…} para {…}.

  Escenario: {título}
    Dado {…}
    Cuando {…}
    Entonces veo el mensaje MSG-01: "{texto literal copiado de §5}"
    Y {…}
```

**Regla mensajes UI:** al citar un `MSG-XX` en Gherkin, incluir **siempre** el texto del mensaje inline (desde §5), no solo el código.

#### Fuera de alcance
- {…}

#### Notas / preguntas abiertas
- {…}

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| {✅/⚠️/❌} | … | … | … | … | … |

---

## 7. Historias técnicas — Endpoints BFF / BE (enablers)

### {KEY} — {Verbo HTTP} · {Resumen}

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Épica** | {CÓDIGO} |
| **Habilita** | {HU keys} |
| **Contrato** | `{MÉTODO} {ruta BFF}` → BE `{ruta interna}` |
| **Prioridad sugerida** | … |
| **Depende de** | … |

#### Objetivo técnico
{…}

#### Criterios de aceptación
1. {criterio técnico verificable — HTTP, códigos, body}

#### Escenarios BDD
```gherkin
Característica: {nombre técnico}
  Escenario: {…}
    …
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 200 | — | … |

---

## 8. Tareas técnicas / habilitadores

| ID | Key Excel | Tarea | Objetivo | Definition of Done |
|----|-----------|-------|----------|--------------------|
| **T-01** | {key} | {nombre} | {objetivo} | {DoD concreto} |

---

## 9. Spikes y decisiones pendientes (columna DUDAS)

| ID | Origen | Pregunta abierta | Impacto si no se resuelve | Propuesta del PO | Respuesta *(post HITL)* |
|----|--------|------------------|---------------------------|------------------|-------------------------|
| **S-01** | {key/doc} | {pregunta} | {impacto} | {propuesta} | {respuesta / skip / pendiente} |

> **Pausa obligatoria (skill):** tras redactar esta tabla, el agente **detiene** el flujo y ofrece al usuario aclarar o skipear **cada** ítem antes de continuar con §10 en adelante.

---

## 10. Recomendaciones del PO — historias faltantes

> Historias **no** presentes en el input. No mezclar con §6/§7.

### 10.1 Imprescindibles antes de salir a producción

| ID | Historia propuesta | Por qué falta / riesgo | Prioridad |
|----|--------------------|------------------------|-----------|

### 10.2 Recomendadas para completar la experiencia

| ID | Historia propuesta | Por qué falta / riesgo | Prioridad |
|----|--------------------|------------------------|-----------|

---

## 11. Observaciones sobre la consistencia del input

Lista numerada de hallazgos (contradicciones, keys duplicados, métodos HTTP inconsistentes, etc.).

---

## 12. Matriz de trazabilidad HU ↔ endpoint ↔ pantalla

| HU | Historias técnicas | Endpoints BFF | Pantalla / paso |
|----|--------------------|---------------|-----------------|
| {KEY} | {HT keys} | `{MÉTODO} {ruta}` | {pantalla} |

---

## 13. Definition of Ready / Definition of Done

**Definition of Ready (por historia)**

- [ ] Objetivo y valor en formato Como / quiero / para
- [ ] Criterios de aceptación numerados (binarios) con tags de camino, referenciando MSG/RN
- [ ] Escenarios BDD en Gherkin (español), alineados a los AC
- [ ] Mensajes de UI identificados (§5) y validados con UX
- [ ] Contrato de endpoints identificado (§7) y acordado con el equipo técnico
- [ ] Dependencias y spikes bloqueantes resueltos o acotados
- [ ] Diseño o pantalla de referencia disponible
- [ ] Chequeo INVEST completo (o spike marcado si falla)

**Definition of Done (por historia)**

- [ ] Criterios de aceptación cumplidos y demostrables
- [ ] Escenarios BDD automatizados o ejecutados manualmente según acuerdo del equipo
- [ ] Mensajes UI implementados según §5
- [ ] Documentación de API actualizada (si HT)
- [ ] Sin deuda técnica bloqueante conocida sin ticket
