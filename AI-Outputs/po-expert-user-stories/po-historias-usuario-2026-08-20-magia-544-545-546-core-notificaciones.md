# Historias de Usuario — Integración CORE y notificaciones post-préstamo (MAGIA-544 / 545 / 546)

> **Versión:** v1.0.0 · **Fecha:** 2026-08-20
> **Fuente única de requerimientos:** issues Jira [MAGIA-544](https://bancoatlaspy.atlassian.net/browse/MAGIA-544), [MAGIA-545](https://bancoatlaspy.atlassian.net/browse/MAGIA-545), [MAGIA-546](https://bancoatlaspy.atlassian.net/browse/MAGIA-546) (plantilla vacía); flujo de negocio tomado del resto de las épicas [MAGIA-348](https://bancoatlaspy.atlassian.net/browse/MAGIA-348) Simulación de Adelantos, [MAGIA-347](https://bancoatlaspy.atlassian.net/browse/MAGIA-347) Gestión de Facturas y [MAGIA-346](https://bancoatlaspy.atlassian.net/browse/MAGIA-346) Confirming.
> **Autor:** PO (elaboración de historias) · **Producto:** Portal de Confirming (Atlas Trade)
> **POC / referencia de diseño:** https://marianaintive.github.io/atlas-confirming-poc/ — pantalla Confirming
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

---

## 0. Qué cambia respecto de versión anterior

Primera versión de este recorte: **no hay documento anterior** específico de MAGIA-544 / 545 / 546.

Criterios de forma adoptados:

- Tarjetas de backlog con metadatos, Connextra (HU) u objetivo técnico (HT), AC numerados con tags y Gherkin en español.
- Mensajes UI/notificación definidos una sola vez en §5 y citados **inline** en AC y BDD.
- Flujo de usuario reconstruido desde las historias ya cargadas en MAGIA-346 / 347 / 348 (en especial `MAGIA-493`, `MAGIA-480`, `MAGIA-502`, `MAGIA-494`, `MAGIA-484`, `MAGIA-488`).
- Aclaración de PO (2026-08-20): cuando CORE **devuelve número de préstamo** (generación OK), la/s factura/s pasan a estado final **`Financiada`**.

---

## 1. Criterio de elaboración y alcance

| Criterio | Decisión aplicada |
|----------|-------------------|
| **Filas tachadas** (Excel) | No aplica — origen Jira, no Excel |
| **Issues a elaborar** | Solo MAGIA-544, MAGIA-545 y MAGIA-546 |
| **Resto de las épicas** | Referencia de flujo y RN; no se reescriben |
| **Escenarios del input** | Las tres issues tenían plantilla vacía; los escenarios se derivan del flujo Confirming ya especificado y de los supuestos confirmados |
| **Historias faltantes** | Solo en §10 (recorte de `MAGIA-494`, callback CORE, etc.) |
| **Identificadores** | Se conservan las keys Jira `MAGIA-544`, `MAGIA-545`, `MAGIA-546` |
| **Idioma y formato** | Español; Gherkin con palabras clave en español |

**Convención de tipos**

| Tipo | Significado |
|------|-------------|
| `HU-BE` | Valor entregado vía proceso/notificación (sin pantalla nueva) |
| `HT` | Historia técnica (contrato CORE / BFF-BE) |
| `TAREA` | Habilitador de infraestructura o configuración |

**Recorte de valor de esta corrida:** tramo **post-aprobación EGP → solicitud de crédito a CORE → préstamo generado → avisos**.

```text
Proveedor simula y solicita (MAGIA-493)
        → factura(s) en Pendiente aprobación EGP + freeze
EGP aprueba (MAGIA-480)
        → Pendiente de desembolso (T-07)
MAGIA-544 envía solicitud de crédito a CORE
        → CORE OK (devuelve nro. préstamo) → Financiada
        → CORE error → vuelve a Pendiente aprobación EGP (RN-C12)
MAGIA-545 notifica al EGP el préstamo generado
MAGIA-546 notifica al Proveedor las facturas asociadas al préstamo
```

---

## 2. Matriz de inclusión / desestimación

| Fila | Key | Summary | Tipo | Estado | Motivo |
|-----:|-----|---------|------|--------|--------|
| 1 | MAGIA-544 | API Integración CORE Banking - Solicitud de Crédito | HT | ✅ Incluida | Issue a refinar; integración real con CORE |
| 2 | MAGIA-545 | Notificación al EGP del préstamo generado | HU-BE | ✅ Incluida | Issue a refinar; aviso post-CORE OK |
| 3 | MAGIA-546 | Notificación al Proveedor de la factura generada | HU-BE | ✅ Incluida | Issue a refinar; aviso post-CORE OK al Proveedor |
| — | MAGIA-493 | POST · Generar adelanto de factura | HT | 📎 Referencia | Crea la solicitud interna; **no** llama a CORE |
| — | MAGIA-480 | Aprobar como EGP la solicitud de adelanto | HU-FE | 📎 Referencia | Dispara T-07 y el envío a CORE |
| — | MAGIA-502 | PATCH · Envío al CORE (mock Fase 1) | HT | 📎 Referencia | Orquestación/mock; no se reescribe |
| — | MAGIA-494 | POST · Notificación de adelanto | HT | 📎 Referencia | Pedido de adelanto; no se mezcla con 545/546 |
| — | MAGIA-484 | POST · Notificación de nueva factura | HT | 📎 Referencia | Alta de factura → EGP; fuera de este recorte |

**Resumen:** 3 incluidas (1 HT + 2 HU-BE) · 0 desestimadas · 5 issues de referencia.

---

## 3. Contexto de solución, actores y supuestos

### 3.1 Perfiles de usuario (actores / dominios)

| Actor | Dominio | Qué hace en este recorte |
|-------|---------|--------------------------|
| **Aprobador del EGP** | EGP | Ya aprobó el adelanto (`MAGIA-480`). Recibe MAGIA-545 cuando el préstamo existe en CORE. |
| **Usuario Proveedor** | Proveedor | Ya solicitó el adelanto (`MAGIA-493`). Recibe MAGIA-546 con las facturas asociadas al préstamo. |
| **Operador / Supervisor Banco** | Banco | Observa en la grilla el paso a `Financiada` o el error CORE (`MSG-C54` / `MSG-C53`). |
| **BFF / BE Confirming** | Sistema | Orquesta MAGIA-544 y dispara MAGIA-545 / MAGIA-546 solo si CORE devolvió nro. de préstamo. |
| **CORE BANKING** | Sistema | Recibe la solicitud de crédito, genera el préstamo, guarda la relación cuenta préstamo ↔ nros. de factura y devuelve nro. de préstamo o error. |
| **Servicio de Notificaciones** | Sistema | Entrega mails/avisos según ABM (dominio, rol, destinatarios). El template lo define CORE. |

### 3.2 Componentes involucrados

| Componente | Rol en MAGIA-544 / 545 / 546 |
|------------|------------------------------|
| **FE — Pantalla Confirming** | No hay pantalla nueva. Refresca grilla: `Pendiente de desembolso` → `Financiada` (pestaña FNV) o reversión a `Pendiente aprobación EGP`. Indicador de desembolso en curso mientras espera a CORE. |
| **BFF Confirming** | Expone/orquesta el envío a CORE tras la aprobación EGP; no bloquea al usuario si el mail falla. |
| **BE Confirming** | Persiste nro. de préstamo, relación préstamo–factura, transición de estado, auditoría e idempotencia. |
| **API CORE BANKING** | Contrato de **solicitud de crédito**. Respuesta OK = número de préstamo. |
| **ABM de notificaciones** | Resuelve destinatarios EGP / Proveedor. |
| **Máquina de estados** (`MAGIA-488`) | T-07, T-11 (`Financiada`) y T-12 (error CORE). |

### 3.3 Supuestos (a confirmar con el equipo técnico)

| # | Supuesto | Confirmación *(post HITL)* |
|---|----------|---------------------------|
| SUP-01 | MAGIA-544, 545 y 546 cubren el tramo **después de la aprobación del EGP**: Atlas envía la solicitud de crédito al CORE; si el CORE genera el préstamo, se notifica al EGP; si el CORE registra las facturas del préstamo, se notifica al Proveedor. | **Confirmado** — usuario 2026-08-20 |
| SUP-02 | MAGIA-544 es la **integración real** con CORE (contrato, relación cuenta préstamo ↔ nros. de factura, idempotencia y reversión). `MAGIA-502` queda como orquestación/mock de Fase 1. No se duplican segregación de funciones ni corte 17 hs (siguen en `MAGIA-493` / `MAGIA-502`). | **Confirmado** — usuario 2026-08-20 |
| SUP-03 | El disparo de MAGIA-544 es la transición T-07: factura(s) en `Pendiente de desembolso` tras aprobación EGP (`MAGIA-480`). **No** se llama al CORE en `POST /generarAdelantoFactura` (`MAGIA-493`). | **Confirmado** — usuario 2026-08-20 |
| SUP-04 | MAGIA-545 notifica al EGP el **préstamo ya generado en CORE**, no el pedido de aprobación. Ese pedido sigue en `MAGIA-494`. | **Confirmado** — usuario 2026-08-20 |
| SUP-05 | MAGIA-546 notifica al Proveedor las **facturas que el CORE dejó asociadas al préstamo** (nro. de factura, cuenta préstamo, monto neto), no el alta de `MAGIA-483` / `MAGIA-484`. | **Confirmado** — usuario 2026-08-20 |
| SUP-06 | Si CORE responde error (`RN-C12`), **no** se envían MAGIA-545 ni MAGIA-546. El fallo del mail **no** revierte el préstamo: se registra y se reintenta. | **Confirmado** — usuario 2026-08-20 |
| SUP-07 | En adelanto múltiple hay **una** solicitud de crédito al CORE, **una** notificación al EGP y **una** al Proveedor con el detalle de las facturas. | **Confirmado** — usuario 2026-08-20 |
| SUP-08 | Destinatarios y canal salen del ABM de notificaciones. El **template de mail lo define CORE**; Atlas Trade envía identificadores y payload, no el HTML del correo. | **Confirmado** — usuario 2026-08-20 |
| SUP-09 | CORE en esta historia es **solicitud de crédito + relación préstamo–factura**. El acreditamiento en cuenta del Proveedor puede ser asíncrono. | **Confirmado, con aclaración:** el estado Atlas pasa a `Financiada` cuando CORE **devuelve el número de préstamo** (generación OK), no cuando llega el dinero a la cuenta. |

---

## 4. Reglas de negocio transversales (RN)

Solo las reglas que este recorte debe cumplir o disparar. El resto del catálogo Confirming (`RN-C01` …) permanece en las épicas de origen.

| ID | Regla | Fuente |
|----|-------|--------|
| **RN-C11** | Resolución de la aprobación del EGP: **Aprueba** → `Pendiente de desembolso` (aprobación bancaria automática). Es el disparador de MAGIA-544. | MAGIA-480 · POC |
| **RN-C12** | Respuesta de CORE: **éxito = CORE devuelve número de préstamo** → la/s factura/s de la solicitud pasan a `Financiada` (estado final, T-11). **Error** → la/s factura/s vuelven a `Pendiente aprobación EGP` para reintentar (T-12); se libera o se mantiene el freeze según `MAGIA-479` / política vigente; **no** hay MAGIA-545 ni MAGIA-546. | MAGIA-480 · Excel SIM-03 · **aclaración PO 2026-08-20** |
| **RN-C19** | El freeze del límite del EGP se concreta al crear la solicitud (`MAGIA-493` / `MAGIA-479`). MAGIA-544 no vuelve a freezear. Si CORE confirma el préstamo (`Financiada`), el freeze se convierte en uso definitivo de línea. Si CORE falla, aplica la reversión de `RN-C12`. | MAGIA-479 · MAGIA-493 |
| **RN-CORE-01** | Condición de éxito de MAGIA-544: el CORE responde con un **número de préstamo** no vacío. Ese identificador se persiste en Atlas (solicitud + cada factura componente) y es la clave de MAGIA-545 / MAGIA-546. | MAGIA-544 · PO 2026-08-20 |
| **RN-CORE-02** | En el CORE queda registrada la **relación cuenta préstamo ↔ número(s) de factura** que componen el crédito. Una operación (individual o múltiple) = **un** préstamo. | Excel SIM-03-E1 · SUP-07 |
| **RN-CORE-03** | MAGIA-544 es **idempotente** respecto de la clave de idempotencia de la solicitud: un reintento no genera un segundo préstamo ni un segundo nro. de préstamo. | MAGIA-493 / MAGIA-502 |
| **RN-CORE-04** | MAGIA-545 y MAGIA-546 se disparan **solo** si se cumplió `RN-CORE-01`. Se disparan en paralelo; el fallo de una no bloquea la otra ni revierte `Financiada`. | SUP-06 |
| **RN-CORE-05** | Destinatarios según ABM de notificaciones (ente, dominio, rol). Si no hay destinatario configurado, se registra `NOTIF_DESTINATARIO_NO_CONFIGURADO` y se reintenta/alerta; la factura permanece `Financiada`. | MAGIA-484 · MAGIA-494 · SUP-08 |
| **RN-CORE-06** | Operación múltiple: un payload CORE, un nro. de préstamo, una notificación EGP y una notificación Proveedor con el listado de facturas. 1 cuota (misma fecha de pago) o N cuotas (fechas distintas) según `MAGIA-476` / `MAGIA-477`. | SUP-07 · MAGIA-477 |

---

## 5. Catálogo de mensajes de UI

Textos visibles en pantalla Confirming (reuso POC) y textos de notificación (propuestos; el HTML lo arma CORE).

| Código | Contexto | Mensaje |
|--------|----------|---------|
| MSG-C19 | Indicador de fila mientras CORE procesa | "CORE BANKING desembolsando…" |
| MSG-C48 | FE tras aprobación EGP (ya cubierto por MAGIA-480; se cita por trazabilidad) | "EGP aprobó el adelanto. La aprobación bancaria es automática: la factura {id} pasa a \"Pendiente de desembolso\"." |
| MSG-C53 | Error CORE / reversión | "La API CORE BANKING reportó un ERROR al desembolsar la factura {id}. La factura vuelve a \"Pendiente aprobación EGP\" para reintentar." |
| MSG-C54 | Éxito: nro. de préstamo recibido | "Desembolso completado por CORE BANKING. La factura {id} pasa a estado \"Financiada\"." |
| MSG-N01 | Notificación EGP — asunto (propuesto; validar UX / CORE) | "Préstamo {nroPrestamo} generado — adelanto Confirming" |
| MSG-N02 | Notificación EGP — cuerpo (payload / placeholders a CORE) | "Se generó el préstamo {nroPrestamo} por el adelanto de {n} factura(s) del Proveedor {proveedor}. Monto bruto {montoBruto} {moneda}. Las facturas pasaron a estado Financiada." |
| MSG-N03 | Notificación Proveedor — asunto (propuesto) | "Factura(s) asociada(s) al préstamo {nroPrestamo}" |
| MSG-N04 | Notificación Proveedor — cuerpo (payload / placeholders a CORE) | "El préstamo {nroPrestamo} quedó generado en CORE. Facturas incluidas: {listaFacturas}. Monto neto a acreditar (estimativo de simulación): {montoNeto} {moneda}." |
| MSG-N05 | Log / alerta operativa sin destinatario | "No hay destinatarios configurados para notificar el préstamo {nroPrestamo} al ente {ente}." |

> MSG-N01 a MSG-N04 son **placeholders de contenido** para el template CORE (SUP-08). El FE no los muestra; sí debe mostrar MSG-C53 / MSG-C54 / MSG-C19.

---

## 6. Historias de usuario funcionales (tarjetas de backlog)

### MAGIA-545 — Notificar al EGP el préstamo generado en CORE

| | |
|---|---|
| **Tipo** | HU-BE |
| **Épica** | MAGIA-348 — Simulación de Adelantos |
| **Actor** | Aprobador / operadores del EGP (destinatarios ABM) |
| **Dominios** | Recurso: EGP · Dominio: EGP |
| **Prioridad sugerida** | Must |
| **Depende de** | MAGIA-544 (`RN-CORE-01`) |
| **Habilita** | Cierre operativo del adelanto para el EGP |
| **Pantalla POC** | Sin pantalla nueva; el EGP ve `Financiada` en grilla (pestaña FNV) |

#### Historia
```
Como aprobador o operador del EGP
quiero recibir una notificación cuando CORE genera el préstamo del adelanto que aprobé
para confirmar que la operación quedó formalizada en el banco y que las facturas pasaron a Financiada
```

#### Valor de negocio

Cierra el ciclo de control del EGP: no basta con haber aprobado en Atlas; el EGP necesita evidencia de que el **préstamo existe en CORE** (número de préstamo) y de qué facturas quedaron financiadas. Distinto del aviso de *pedido* de adelanto (`MAGIA-494`).

#### Escenarios fuente

> Input Jira MAGIA-545: plantilla vacía. Escenarios derivados del flujo Confirming y de supuestos confirmados (SUP-01, SUP-04, SUP-06, SUP-07).

```text
1. Feliz — CORE devolvió nro. de préstamo: se notifica al EGP el préstamo generado (facturas, montos, proveedor).
2. Feliz — Operación múltiple: una sola notificación al EGP con el detalle de las N facturas y un único nro. de préstamo.
3. Alternativo — Fallo del canal de notificación: el préstamo y el estado Financiada no se revierten; se registra y se reintenta.
4. Error — CORE no devolvió nro. de préstamo (error o timeout de negocio): no se notifica al EGP.
5. Error — EGP sin destinatarios en el ABM: no se envía mail; se registra NOTIF_DESTINATARIO_NO_CONFIGURADO; facturas siguen Financiada.
```

#### Criterios de aceptación

1. **[Feliz]** Se dispara **únicamente** cuando MAGIA-544 persistió un número de préstamo (`RN-CORE-01`, `RN-CORE-04`).
2. **[Feliz]** El payload enviado al servicio de notificaciones / CORE incluye: `{nroPrestamo}`, EGP, Proveedor, lista de facturas (número, monto, moneda, fecha de pago), monto bruto de la operación y marca temporal. El mail resultante usa el template CORE con MSG-N01: "Préstamo {nroPrestamo} generado — adelanto Confirming" y MSG-N02: "Se generó el préstamo {nroPrestamo} por el adelanto de {n} factura(s) del Proveedor {proveedor}. Monto bruto {montoBruto} {moneda}. Las facturas pasaron a estado Financiada."
3. **[Feliz]** Los destinatarios se resuelven por ABM de notificaciones para el ente EGP (`RN-CORE-05`).
4. **[Feliz]** En operación múltiple se envía **una** notificación al EGP con todas las facturas del préstamo (`RN-CORE-06`).
5. **[Alternativo]** Si el envío falla (timeout, 503), las facturas permanecen `Financiada` y el error queda registrado para reintento; no se llama a reversión CORE.
6. **[Error]** Si CORE no generó el préstamo, **no** se envía MAGIA-545.
7. **[Error]** Si no hay destinatarios configurados, se registra el evento con MSG-N05: "No hay destinatarios configurados para notificar el préstamo {nroPrestamo} al ente {ente}." y código `NOTIF_DESTINATARIO_NO_CONFIGURADO`.
8. **[Validación]** Cada intento (éxito o fallo) queda auditado: destinatarios, `{nroPrestamo}`, resultado, timestamp.

#### Escenarios BDD

```gherkin
Característica: Notificación al EGP del préstamo generado
  Como aprobador o operador del EGP
  quiero recibir una notificación cuando CORE genera el préstamo
  para confirmar que las facturas quedaron Financiada.

  Antecedentes:
    Dado que el EGP ya aprobó la solicitud de adelanto
    Y las facturas estaban en "Pendiente de desembolso"

  Escenario: Préstamo generado se notifica al EGP
    Dado que CORE devolvió el número de préstamo "PREST-1001"
    Y las facturas de la solicitud pasaron a "Financiada"
    Cuando se dispara la notificación al EGP
    Entonces el EGP recibe el aviso MSG-N01: "Préstamo {nroPrestamo} generado — adelanto Confirming"
    Y el contenido corresponde a MSG-N02: "Se generó el préstamo {nroPrestamo} por el adelanto de {n} factura(s) del Proveedor {proveedor}. Monto bruto {montoBruto} {moneda}. Las facturas pasaron a estado Financiada."
    Y el payload incluye el número de préstamo "PREST-1001" y las facturas asociadas

  Escenario: Operación múltiple — una sola notificación
    Dado un préstamo "PREST-1002" que agrupa cuatro facturas del mismo EGP-Proveedor-moneda
    Cuando se dispara la notificación al EGP
    Entonces el EGP recibe una única notificación con las cuatro facturas y el número "PREST-1002"

  Escenario: Fallo de envío no revierte el préstamo
    Dado que CORE devolvió el número de préstamo "PREST-1001"
    Y las facturas están en "Financiada"
    Y el servicio de notificaciones no responde
    Cuando se intenta notificar al EGP
    Entonces las facturas permanecen en "Financiada"
    Y el error de envío queda registrado para reintento

  Escenario: CORE con error no notifica al EGP
    Dado que CORE no devolvió número de préstamo
    Y las facturas volvieron a "Pendiente aprobación EGP"
    Entonces no se envía notificación MAGIA-545 al EGP

  Escenario: EGP sin destinatarios configurados
    Dado que CORE devolvió el número de préstamo "PREST-1001"
    Y el ABM de notificaciones no tiene destinatarios para ese EGP
    Cuando se evalúa el envío
    Entonces no se envía el mail
    Y queda registrado MSG-N05: "No hay destinatarios configurados para notificar el préstamo {nroPrestamo} al ente {ente}."
```

#### Fuera de alcance

- Pedido de adelanto al EGP (antes de aprobar): `MAGIA-494`.
- Notificación al Proveedor: `MAGIA-546`.
- Diseño HTML del mail (CORE, SUP-08).
- Pantalla nueva o bandeja in-app.

#### Notas / preguntas abiertas

- Copy de MSG-N01 / MSG-N02 pendiente de validación UX y de plantilla CORE (`S-03`).
- Recorte de `MAGIA-494` para que no vuelva a avisar “crédito generado” al EGP (`S-02`).

#### Chequeo INVEST

| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ⚠️ Depende de MAGIA-544 | ✅ | ✅ Evidencia de préstamo real | ✅ | ✅ | ✅ |

---

### MAGIA-546 — Notificar al Proveedor las facturas asociadas al préstamo generado

| | |
|---|---|
| **Tipo** | HU-BE |
| **Épica** | MAGIA-348 — Simulación de Adelantos |
| **Actor** | Usuario / operadores del Proveedor (destinatarios ABM) |
| **Dominios** | Recurso: PROVEEDOR · Dominio: PROVEEDOR |
| **Prioridad sugerida** | Must |
| **Depende de** | MAGIA-544 (`RN-CORE-01`) |
| **Habilita** | Cierre operativo del adelanto para el Proveedor |
| **Pantalla POC** | Sin pantalla nueva; el Proveedor ve `Financiada` en grilla (pestaña FNV) |

#### Historia
```
Como usuario o operador del Proveedor
quiero recibir una notificación con las facturas que CORE asoció al préstamo generado
para saber qué documentos quedaron financiados y con qué número de préstamo
```

#### Valor de negocio

El Proveedor no opera la aprobación del EGP; su necesidad es saber **cuáles de sus facturas** quedaron en el préstamo CORE (números de factura persistidos en el core, `RN-CORE-02`) y el identificador del crédito. No cubre el alta de factura (`MAGIA-484`).

#### Escenarios fuente

> Input Jira MAGIA-546: plantilla vacía. Título: «Notificación al Proveedor de la factura generada». Interpretación confirmada (SUP-05): factura(s) **generadas/asociadas en CORE** como componente del préstamo.

```text
1. Feliz — CORE devolvió nro. de préstamo: se notifica al Proveedor las facturas asociadas (nro. factura, nro. préstamo, monto neto).
2. Feliz — Operación múltiple: una sola notificación al Proveedor con las N facturas.
3. Alternativo — Fallo del canal: Financiada se mantiene; se registra y se reintenta.
4. Error — CORE no devolvió nro. de préstamo: no se notifica al Proveedor.
5. Error — Proveedor sin destinatarios en el ABM: se registra; facturas siguen Financiada.
```

#### Criterios de aceptación

1. **[Feliz]** Se dispara **únicamente** cuando MAGIA-544 persistió un número de préstamo (`RN-CORE-01`, `RN-CORE-04`).
2. **[Feliz]** El payload incluye: `{nroPrestamo}`, Proveedor, EGP, lista de facturas (número, timbrado si aplica, monto, moneda, fecha de pago) y monto neto de la simulación. El mail usa el template CORE con MSG-N03: "Factura(s) asociada(s) al préstamo {nroPrestamo}" y MSG-N04: "El préstamo {nroPrestamo} quedó generado en CORE. Facturas incluidas: {listaFacturas}. Monto neto a acreditar (estimativo de simulación): {montoNeto} {moneda}."
3. **[Feliz]** Los destinatarios se resuelven por ABM para el ente Proveedor (`RN-CORE-05`).
4. **[Feliz]** En operación múltiple se envía **una** notificación con todas las facturas (`RN-CORE-06`).
5. **[Alternativo]** El fallo de MAGIA-546 no revierte `Financiada` ni bloquea MAGIA-545.
6. **[Error]** Si CORE no generó el préstamo, **no** se envía MAGIA-546.
7. **[Error]** Sin destinatarios: se registra MSG-N05: "No hay destinatarios configurados para notificar el préstamo {nroPrestamo} al ente {ente}." con código `NOTIF_DESTINATARIO_NO_CONFIGURADO`.
8. **[Validación]** Cada intento queda auditado: destinatarios, `{nroPrestamo}`, facturas incluidas, resultado, timestamp.
9. **[Validación]** El aviso **no** promete que el dinero ya está en la cuenta del Proveedor (SUP-09): informa facturas financiadas y nro. de préstamo.

#### Escenarios BDD

```gherkin
Característica: Notificación al Proveedor de las facturas asociadas al préstamo
  Como usuario o operador del Proveedor
  quiero recibir las facturas asociadas al préstamo generado en CORE
  para saber qué documentos quedaron financiados.

  Antecedentes:
    Dado que el Proveedor solicitó el adelanto
    Y el EGP ya aprobó la solicitud

  Escenario: Préstamo generado notifica las facturas al Proveedor
    Dado que CORE devolvió el número de préstamo "PREST-1001"
    Y asoció la factura "001-001-0004001" a ese préstamo
    Y la factura pasó a "Financiada"
    Cuando se dispara la notificación al Proveedor
    Entonces el Proveedor recibe el aviso MSG-N03: "Factura(s) asociada(s) al préstamo {nroPrestamo}"
    Y el contenido corresponde a MSG-N04: "El préstamo {nroPrestamo} quedó generado en CORE. Facturas incluidas: {listaFacturas}. Monto neto a acreditar (estimativo de simulación): {montoNeto} {moneda}."
    Y el payload incluye "PREST-1001" y la factura "001-001-0004001"

  Escenario: Operación múltiple — una sola notificación al Proveedor
    Dado un préstamo "PREST-1002" con cuatro facturas
    Cuando se dispara la notificación al Proveedor
    Entonces el Proveedor recibe una única notificación con las cuatro facturas

  Escenario: Fallo de envío no revierte Financiada
    Dado que las facturas están en "Financiada" con préstamo "PREST-1001"
    Y el servicio de notificaciones no responde
    Cuando se intenta notificar al Proveedor
    Entonces las facturas permanecen en "Financiada"
    Y el error queda registrado para reintento

  Escenario: CORE con error no notifica al Proveedor
    Dado que CORE no devolvió número de préstamo
    Entonces no se envía notificación MAGIA-546 al Proveedor

  Escenario: Proveedor sin destinatarios configurados
    Dado que CORE devolvió el número de préstamo "PREST-1001"
    Y el ABM no tiene destinatarios para ese Proveedor
    Cuando se evalúa el envío
    Entonces no se envía el mail
    Y queda registrado MSG-N05: "No hay destinatarios configurados para notificar el préstamo {nroPrestamo} al ente {ente}."
```

#### Fuera de alcance

- Notificación de **alta** de factura al EGP: `MAGIA-484`.
- Notificación al EGP del préstamo: `MAGIA-545`.
- Aviso de rechazo EGP: `MAGIA-481`.
- Confirmación de acreditamiento en cuenta (tesorería / extracto).
- Diseño HTML del mail (CORE).

#### Notas / preguntas abiertas

- El título Jira dice «factura generada»; en AC se operacionaliza como facturas **asociadas en CORE al préstamo** (SUP-05).
- Copy MSG-N03 / MSG-N04 pendiente de UX / plantilla CORE (`S-03`).

#### Chequeo INVEST

| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ⚠️ Depende de MAGIA-544 | ✅ | ✅ El Proveedor sabe qué se financió | ✅ | ✅ | ✅ |

---

## 7. Historias técnicas — Endpoints BFF / BE (enablers)

### MAGIA-544 — POST · Solicitud de crédito a CORE BANKING

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Épica** | MAGIA-348 — Simulación de Adelantos |
| **Habilita** | MAGIA-545, MAGIA-546, T-11 (`Financiada`), visibilidad FE `MSG-C54` |
| **Contrato** | BFF/BE Atlas: `POST /adelantos/{idSolicitud}/solicitud-credito-core` *(propuesto)* → CORE `POST /creditos/solicitudes` *(propuesto, S-01)* |
| **Prioridad sugerida** | Must |
| **Depende de** | MAGIA-480 (T-07), MAGIA-493 (solicitud + freeze), MAGIA-488 (motor de estados). `MAGIA-502` = mock/orquestación Fase 1, no duplicar validaciones RN-C20 / RN-C21. |
| **Actor** | Sistema Confirming |

#### Objetivo técnico

Enviar a CORE BANKING la **solicitud de crédito** de un adelanto ya aprobado por el EGP, persistir la relación cuenta préstamo ↔ facturas y, cuando CORE **devuelva el número de préstamo**, dejar la/s factura/s en estado final **`Financiada`**. Ante error de CORE, revertir a `Pendiente aprobación EGP` sin disparar notificaciones 545/546.

#### Escenarios fuente

> Input Jira MAGIA-544: plantilla vacía. Escenarios derivados de Excel SIM-03-E1/E2/E5, MAGIA-502, MAGIA-480 AC 5 y aclaración PO 2026-08-20.

```text
1. Feliz — CORE acepta y devuelve nro. de préstamo: se persiste la relación préstamo-factura; facturas → Financiada.
2. Feliz — Operación de una o N cuotas / N facturas: un préstamo, un nro., N facturas asociadas.
3. Alternativo — Reintento idempotente: no se genera un segundo préstamo.
4. Error — CORE rechaza o no devuelve nro. de préstamo: no queda préstamo; facturas vuelven a Pendiente aprobación EGP; no hay 545/546.
5. Error — Timeout / servicio no disponible: misma reversión de negocio que error CORE (RN-C12).
```

#### Criterios de aceptación

1. **[Feliz / Validación]** Solo se invoca si la solicitud está aprobada por el EGP y las facturas están en `Pendiente de desembolso` (T-07, SUP-03). Si el estado no es válido, responde `409 FACTURA_ESTADO_INVALIDO` y **no** llama a CORE.
2. **[Feliz]** El payload a CORE incluye: identificador de solicitud Atlas, EGP, Proveedor, moneda, plan de cuotas (1 o N), importe, y el **número de cada factura** que compone el préstamo (`RN-CORE-02`).
3. **[Feliz]** **Condición de éxito:** CORE responde con un **número de préstamo** no vacío (`RN-CORE-01`). Atlas persiste `{nroPrestamo}` en la solicitud y en cada factura componente.
4. **[Feliz]** Al cumplirse el criterio 3, **todas** las facturas de la solicitud pasan a `Financiada` (estado final, T-11, `RN-C12` aclarado). El FE, al refrescar, muestra MSG-C54: "Desembolso completado por CORE BANKING. La factura {id} pasa a estado \"Financiada\"." Mientras tanto la fila puede mostrar MSG-C19: "CORE BANKING desembolsando…".
5. **[Feliz]** Tras el criterio 3 se disparan MAGIA-545 y MAGIA-546 (`RN-CORE-04`).
6. **[Feliz]** Operación múltiple: un llamado CORE, un `{nroPrestamo}`, N facturas `Financiada` (`RN-CORE-06`).
7. **[Alternativo]** Reintento con la misma clave de idempotencia: CORE/Atlas **no** generan un segundo préstamo; se reutiliza el `{nroPrestamo}` ya persistido (`RN-CORE-03`).
8. **[Error]** Si CORE responde error, o responde OK **sin** número de préstamo, o hay timeout de negocio: **no** se persiste préstamo; las facturas vuelven a `Pendiente aprobación EGP` (T-12); el FE puede mostrar MSG-C53: "La API CORE BANKING reportó un ERROR al desembolsar la factura {id}. La factura vuelve a \"Pendiente aprobación EGP\" para reintentar."; **no** se envían MAGIA-545 ni MAGIA-546.
9. **[Error]** La reversión no deja estados intermedios inconsistentes: no puede quedar un subconjunto de facturas `Financiada` y otro no (`RN-C12`).
10. **[Validación]** Auditoría: usuario/sistema, timestamp, id solicitud, facturas, importes, plan de cuotas, `{nroPrestamo}` o código de error CORE, resultado.
11. **[Validación]** No reimplementa segregación de funciones ni corte 17 hs (SUP-02).

#### Escenarios BDD

```gherkin
Característica: Solicitud de crédito a CORE BANKING
  Como sistema de Confirming
  quiero enviar al CORE la solicitud de crédito del adelanto aprobado
  para persistir el préstamo y dejar las facturas en Financiada.

  Antecedentes:
    Dado que existe la solicitud de adelanto "SOL-9001" creada por MAGIA-493
    Y el EGP la aprobó
    Y las facturas de "SOL-9001" están en "Pendiente de desembolso"

  Escenario: CORE devuelve número de préstamo y las facturas pasan a Financiada
    Cuando Atlas envía la solicitud de crédito de "SOL-9001" al CORE
    Y CORE responde OK con número de préstamo "PREST-1001"
    Entonces Atlas persiste "PREST-1001" en la solicitud y en cada factura componente
    Y queda registrada la relación cuenta préstamo "PREST-1001" con los números de factura
    Y todas las facturas de "SOL-9001" pasan a "Financiada"
    Y se habilitan las notificaciones MAGIA-545 y MAGIA-546
    Y al refrescar la grilla el operador puede ver MSG-C54: "Desembolso completado por CORE BANKING. La factura {id} pasa a estado \"Financiada\"."

  Escenario: Adelanto múltiple — un préstamo y N facturas Financiada
    Dado que "SOL-9002" agrupa cuatro facturas del mismo EGP-Proveedor-moneda
    Cuando CORE responde OK con número de préstamo "PREST-1002"
    Entonces las cuatro facturas pasan a "Financiada"
    Y las cuatro quedan asociadas a "PREST-1002"
    Y no se genera un segundo número de préstamo

  Escenario: Idempotencia ante reintento
    Dado que "SOL-9001" ya tiene persistido el préstamo "PREST-1001"
    Cuando se reenvía la misma solicitud de crédito con la misma clave de idempotencia
    Entonces no se crea un segundo préstamo
    Y las facturas permanecen en "Financiada"

  Escenario: CORE responde error — reversión y sin notificaciones
    Cuando Atlas envía la solicitud de crédito de "SOL-9001" al CORE
    Y CORE responde error
    Entonces no se persiste número de préstamo
    Y las facturas de "SOL-9001" vuelven a "Pendiente aprobación EGP"
    Y no se dispara MAGIA-545
    Y no se dispara MAGIA-546
    Y el FE puede mostrar MSG-C53: "La API CORE BANKING reportó un ERROR al desembolsar la factura {id}. La factura vuelve a \"Pendiente aprobación EGP\" para reintentar."

  Escenario: CORE OK sin número de préstamo se trata como error
    Cuando CORE responde OK pero sin número de préstamo
    Entonces no se persiste préstamo
    Y las facturas vuelven a "Pendiente aprobación EGP"
    Y no se disparan MAGIA-545 ni MAGIA-546

  Escenario: Estado inválido no llama a CORE
    Dado que una factura de la solicitud no está en "Pendiente de desembolso"
    Cuando se intenta enviar la solicitud de crédito
    Entonces Atlas no llama a CORE
    Y responde 409 con código FACTURA_ESTADO_INVALIDO
```

#### Errores esperados

| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 409 | `FACTURA_ESTADO_INVALIDO` | La solicitud no está en `Pendiente de desembolso` / EGP no aprobó |
| 404 | `SOLICITUD_NO_ENCONTRADA` | `{idSolicitud}` inexistente |
| 409 | `PRESTAMO_YA_GENERADO` | Idempotencia: ya existe `{nroPrestamo}` (respuesta de negocio, no error de usuario) |
| 422 | `PLAN_CUOTAS_NO_SOPORTADO` | El plan de cuotas no es admitido por CORE |
| 502 | `CORE_ERROR` | CORE rechazó o no devolvió nro. de préstamo; se ejecuta reversión T-12 |
| 504 | `CORE_TIMEOUT` | Sin respuesta a tiempo; misma reversión que `CORE_ERROR` |
| 503 | `SERVICIO_NO_DISPONIBLE` | Error de dependencia Atlas previo al llamado CORE |

#### Fuera de alcance

- Mock de latencia/error de Fase 1: `MAGIA-502`.
- Creación de la solicitud interna y freeze: `MAGIA-493` / `MAGIA-479`.
- UI de aprobación EGP: `MAGIA-480`.
- Validaciones RN-C20 / RN-C21.
- Acreditación efectiva en cuenta corriente del Proveedor.

#### Notas / preguntas abiertas

- Path y autenticación reales de CORE: `S-01`.
- Si CORE es asíncrono, el **callback que trae `{nroPrestamo}`** es el que dispara T-11 y 545/546; `Pendiente de desembolso` se mantiene hasta ese evento.

---

## 8. Tareas técnicas / habilitadores

No aplica como issues nuevas de este recorte: la infraestructura de notificaciones y el ABM ya están supuestos en `MAGIA-484` / `MAGIA-494` / `TAR-C01`–`TAR-C03`.

| ID | Key | Tarea | Objetivo | Definition of Done |
|----|-----|-------|----------|--------------------|
| **T-CORE-01** | — (recomendación) | Parametrizar timeout y política de reintentos del llamado CORE | Evitar facturas colgadas en `Pendiente de desembolso` | Timeout y reintentos documentados; T-12 se dispara al agotarlos |
| **T-CORE-02** | — (recomendación) | Mapear campos Atlas → contrato CORE (nro. factura, ente, cuotas) | Un solo préstamo con N facturas | Contrato revisado con el dueño de CORE |

Estas tareas **no** se cargan como historias de esta corrida; van a §10 si el equipo las quiere en Jira.

---

## 9. Spikes y decisiones pendientes (columna DUDAS)

Las issues de origen no traían columna `dudas`. Los ítems salen del cruce con las épicas y de lo que CORE todavía no tiene contrato publicado.

| ID | Origen | Pregunta abierta | Impacto si no se resuelve | Propuesta del PO | Respuesta *(post HITL)* |
|----|--------|------------------|---------------------------|------------------|-------------------------|
| **S-01** | MAGIA-544 | ¿El CORE responde el nro. de préstamo en el mismo POST (síncrono) o por callback/evento? ¿Path, auth y ambiente? | Sin esto el equipo estima contra un contrato inventado | Diseñar Atlas para **ambos**: si la respuesta inmediata trae `{nroPrestamo}` → T-11 ahora; si no, permanecer en `Pendiente de desembolso` (MSG-C19) hasta el callback que trae el número. Paths propuestos en la tarjeta MAGIA-544. | **Propuesta PO aplicada** — usuario pidió avanzar con la escritura de HUs (2026-08-20). Ajustar paths cuando CORE entregue el contrato. |
| **S-02** | MAGIA-494 vs 545/546 | `MAGIA-494` hoy notifica al EGP el pedido **y** al Proveedor el crédito generado. ¿Se recorta para no duplicar 545/546? | Doble mail al EGP/Proveedor en go-live | `MAGIA-494` = solo pedido de adelanto al EGP (y opcionalmente al Proveedor de “solicitud enviada”). Crédito/facturas generadas = 545 y 546. | **Propuesta PO aplicada** — ver §10.1 REC-01. |
| **S-03** | MAGIA-545 / 546 | ¿Los literales MSG-N01…N04 son los definitivos o CORE ya tiene plantillas? | Copy incorrecto en producción | Atlas envía payload; CORE define HTML. MSG-N\* son placeholders de contenido mínimo a validar con UX. | **Propuesta PO aplicada** (SUP-08). Validación UX no bloquea el desarrollo del disparo. |
| **S-04** | RN-C19 / T-12 | Ante error CORE, ¿el freeze se libera o se mantiene hasta reintento del EGP? `MAGIA-480` mantiene freeze; Excel SIM-03-E5 tiende a revertir. | Límite del EGP mal calculado | Mantener freeze mientras la solicitud exista y las facturas estén en `Pendiente aprobación EGP` (reintento). Liberar si el EGP rechaza (`MAGIA-481`). | **Propuesta PO aplicada** — coherente con MAGIA-480 AC 5. |

> Pausa §9: el usuario pidió **avanzar con la escritura de HUs** tras confirmar supuestos; las propuestas PO quedaron aplicadas en las tarjetas. Si hay que cambiar S-01 (contrato CORE) o S-04 (freeze), se actualiza este documento.

---

## 10. Recomendaciones del PO — historias faltantes

No forman parte de MAGIA-544 / 545 / 546.

### 10.1 Imprescindibles antes de salir a producción

| ID | Historia propuesta | Por qué falta / riesgo | Prioridad |
|----|--------------------|------------------------|-----------|
| **REC-01** | Recortar `MAGIA-494` para que no notifique “crédito generado” | Duplicaría MAGIA-545 / MAGIA-546 | Must |
| **REC-02** | Callback / listener CORE (`{nroPrestamo}` asíncrono) si el contrato no es síncrono | Sin esto MAGIA-544 queda a medias en un CORE real | Must si CORE es async |
| **REC-03** | Ajuste FE de `MAGIA-480` AC 5: `Financiada` se confirma al **recibir nro. de préstamo**, no por un mock a 2,5 s | El mock de `MAGIA-502` no es la fuente de verdad | Must |

### 10.2 Recomendadas para completar la experiencia

| ID | Historia propuesta | Por qué falta / riesgo | Prioridad |
|----|--------------------|------------------------|-----------|
| **REC-04** | Notificación al Proveedor cuando el dinero **se acredita** (tesorería), distinta de MAGIA-546 | SUP-09: Financiada ≠ acreditado | Should |
| **REC-05** | Bandeja in-app de avisos (además del mail CORE) | Operadores que no miran correo | Could |
| **REC-06** | Reintento manual Banco de MAGIA-545 / 546 desde un monitor operativo | Destinatario mal cargado en ABM | Should |

---

## 11. Observaciones sobre la consistencia del input

1. MAGIA-544 / 545 / 546 se crearon el 2026-08-20 con **plantilla Connextra vacía**; todo el detalle de esta versión es elaboración PO a partir de las épicas y de los supuestos confirmados.
2. `MAGIA-493` (generar adelanto) y el Excel SIM-03-E1 hablan de enviar al CORE **al crear** la solicitud; `MAGIA-480` / `MAGIA-502` y SUP-03 colocan el envío **después** de la aprobación EGP. Este documento sigue SUP-03.
3. `MAGIA-502` BDD deja la factura en `Pendiente de desembolso` al enviar al CORE; MAGIA-480 AC 5 y la aclaración PO ponen `Financiada` cuando CORE confirma. MAGIA-544 unifica: **nro. de préstamo = Financiada**.
4. El título MAGIA-546 dice «factura generada»; MAGIA-494 dice «crédito generado» al Proveedor. SUP-05 unifica: facturas **asociadas al préstamo en CORE**.
5. `MAGIA-502` menciona mock «por dependencia del core»: MAGIA-544 es el reemplazo de esa dependencia, no un segundo mock.
6. MSG-C54 de la POC habla de «Desembolso completado»; el disparador de negocio ahora es **número de préstamo**. Se reutiliza el copy para no inventar un tercer mensaje de FE hasta validación UX.

---

## 12. Matriz de trazabilidad HU ↔ endpoint ↔ pantalla

| HU / HT | Historias técnicas | Endpoints BFF / CORE | Pantalla / paso |
|---------|--------------------|----------------------|-----------------|
| MAGIA-544 | — (esta HT) | `POST /adelantos/{idSolicitud}/solicitud-credito-core` → CORE `POST /creditos/solicitudes` *(propuestos)* | Grilla Confirming: `Pendiente de desembolso` → `Financiada` (FNV) o reversión a `Pendiente aprobación EGP`; MSG-C19 / MSG-C54 / MSG-C53 |
| MAGIA-545 | MAGIA-544 | `POST /notificaciones/prestamo-generado` *(propuesto, destinatario EGP)* o evento interno post-CORE OK | Mail/template CORE; grilla FNV para el EGP |
| MAGIA-546 | MAGIA-544 | `POST /notificaciones/facturas-prestamo` *(propuesto, destinatario Proveedor)* o evento interno post-CORE OK | Mail/template CORE; grilla FNV para el Proveedor |
| MAGIA-480 *(ref)* | MAGIA-544 | Aprobación EGP (ya especificada) | Modal aprobación EGP |
| MAGIA-493 *(ref)* | MAGIA-544 | `POST /generarAdelantoFactura` | Modal simulación — **no** llama CORE |
| MAGIA-488 *(ref)* | MAGIA-544 | Motor de estados T-07 / T-11 / T-12 | Columna estado de la grilla |
| MAGIA-494 *(ref)* | — | `POST /notificacionAdelantoFactura` | Pedido de adelanto; recortar según REC-01 |

---

## 13. Definition of Ready / Definition of Done

**Definition of Ready (por historia)**

- [x] Objetivo y valor en formato Como / quiero / para (HU) u objetivo técnico (HT)
- [x] Criterios de aceptación numerados (binarios) con tags de camino, referenciando MSG/RN
- [x] Escenarios BDD en Gherkin (español), alineados a los AC
- [x] Mensajes UI/notificación identificados en §5 (MSG-N\* sujetos a template CORE)
- [ ] Contrato real de endpoints CORE acordado con el equipo técnico (`S-01`)
- [ ] Recorte de `MAGIA-494` acotado (REC-01) para no duplicar mails
- [x] Dependencias documentadas (MAGIA-480, MAGIA-493, MAGIA-488, MAGIA-502)
- [x] Pantalla de referencia: POC Confirming (sin pantalla nueva)
- [x] Chequeo INVEST completo (dependencia 544→545/546 explícita)

**Definition of Done (por historia)**

- [ ] Criterios de aceptación cumplidos y demostrables en ambiente integrado con CORE (o stub que **devuelva nro. de préstamo**)
- [ ] Escenarios BDD ejecutados (automatizados o checklist QA)
- [ ] Transición a `Financiada` **solo** si existe `{nroPrestamo}` persistido
- [ ] MAGIA-545 y MAGIA-546 no se envían si CORE falló
- [ ] Fallo de notificación no revierte `Financiada`
- [ ] MSG-C53 / MSG-C54 / MSG-C19 coherentes con el estado en grilla
- [ ] Auditoría de llamado CORE y de cada envío de notificación
- [ ] Documentación de API Atlas actualizada (MAGIA-544)
- [ ] Sin deuda técnica bloqueante conocida sin ticket
