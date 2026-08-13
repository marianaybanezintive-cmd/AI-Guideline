# Historias de Usuario — Épica CONFIRMING (Portal de Confirming · Banco Atlas)

| | |
|---|---|
| **Versión del documento** | v1.0.0 |
| **Fecha** | 12-08-2026 |
| **Épica** | CONFIRMING |
| **Elaborado con** | skill `po-expert-user-stories` |
| **Fuente funcional** | `Confirming.xlsx` · hoja `CONFIRMING` · 23 filas con contenido (filas 3 a 25), columnas `Issue Type`, `Issue Key`, `STACK`, `Summary`, `OBJETIVO`, `ESCENARIOS`, `DUDAS` |
| **Fuente de comportamiento FE** | POC `https://marianaintive.github.io/atlas-confirming-poc/` · pantalla **Confirming** · versión `POC v2.11.3` (`version.js`) |
| **Alcance** | Carga de facturas (FAC), consulta y gestión de facturas (CON), simulación y adelanto (SIM) |
| **Total** | **25 HU funcionales** · **13 HT (enablers)** · **3 tareas técnicas** · **24 reglas de negocio** · **55 mensajes de UI** · **23 spikes** |

---

## Tabla de contenidos

1. [Criterio de elaboración y alcance](#1-criterio-de-elaboración-y-alcance)
2. [Matriz de inclusión / desestimación (fila por fila del Excel)](#2-matriz-de-inclusión--desestimación-fila-por-fila-del-excel)
3. [Contexto de solución, actores y supuestos](#3-contexto-de-solución-actores-y-supuestos)
4. [Reglas de negocio transversales (RN)](#4-reglas-de-negocio-transversales-rn)
5. [Catálogo de mensajes de UI (MSG)](#5-catálogo-de-mensajes-de-ui-msg)
6. [Máquina de estados de facturas (referencia)](#6-máquina-de-estados-de-facturas-referencia)
7. [Historias de usuario funcionales (tarjetas de backlog)](#7-historias-de-usuario-funcionales-tarjetas-de-backlog)
8. [Historias técnicas — endpoints BFF / BE (enablers)](#8-historias-técnicas--endpoints-bff--be-enablers)
9. [Tareas técnicas / habilitadores](#9-tareas-técnicas--habilitadores)
10. [Spikes y decisiones pendientes](#10-spikes-y-decisiones-pendientes)
11. [Recomendaciones del PO — historias faltantes (no están en el Excel)](#11-recomendaciones-del-po--historias-faltantes-no-están-en-el-excel)
12. [Observaciones sobre la consistencia del Excel](#12-observaciones-sobre-la-consistencia-del-excel)
13. [Matriz de trazabilidad HU ↔ endpoint ↔ pantalla de la POC](#13-matriz-de-trazabilidad-hu--endpoint--pantalla-de-la-poc)
14. [Definition of Ready / Definition of Done](#14-definition-of-ready--definition-of-done)

---

## 1. Criterio de elaboración y alcance

### 1.1 Fuentes y jerarquía entre ellas

| Fuente | Qué aporta | Qué NO aporta |
|--------|------------|---------------|
| **`Confirming.xlsx`** | El **alcance comprometido**: 23 filas, cada una con `OBJETIVO` y `ESCENARIOS`. Es la única fuente que define *qué entra*. | Detalle de UX, textos, validaciones finas. |
| **POC Confirming** | El **comportamiento observable ya definido**: flujos, transiciones, validaciones, textos literales de mensajes, estados vacíos, tooltips y tabla de acciones por estado. | Alcance. Lo que la POC hace de más se marca como recomendación; lo que la POC no hace y el Excel pide se marca como *gap de POC*. |

Regla aplicada en todo el documento: **el Excel manda sobre el alcance; la POC manda sobre el detalle del front end.** Cuando ambos difieren, la divergencia se explicita en «Notas / preguntas abiertas» de la historia y se escala al bloque de spikes (§10). Nada se da por resuelto por decisión del redactor.

### 1.2 Cómo se derivó cada historia

1. Se clasificó **fila por fila** del Excel (§2). No hay filas ni escenarios tachados en la planilla: **las 23 filas entran al backlog**.
2. Cada `ESCENARIO` de cada fila quedó **cubierto por al menos un criterio de aceptación numerado y su escenario BDD**. La trazabilidad escenario → historia está en la matriz de §2 y en el bloque «Escenarios fuente» de cada tarjeta.
3. Se partió una fila en varias historias **solo cuando los escenarios describen flujos materialmente distintos** (por ejemplo `FAC-02`: descargar template, cargar archivo y escanear son tres flujos independientes y desplegables por separado). Cuando los escenarios son facetas del mismo entregable (por ejemplo la botonera de la grilla de `CON-02`), se mantuvo **una sola historia con un criterio de aceptación por escenario**, para no romper INVEST por el lado de *Valuable*.
4. Las filas de stack `BE/BFF` y `BFF` se escribieron como **HT (enablers)** con contrato de endpoint y tabla de errores, tal como exige la skill: una fila que mezcla pantalla y endpoint se separa en HU + HT.
5. Los textos de mensajes **no se inventaron**: los `MSG-Cxx` de §5 son transcripción literal del código de la POC. Los mensajes que el Excel exige y la POC **no** tiene (por ejemplo la leyenda de valores estimativos de `SIM-01`) están marcados como *pendiente de redacción* y no se dan por implementados.

### 1.3 Nomenclatura de identificadores

- Se conservan **los `Issue Key` originales del Excel** (`FAC-xx`, `CON-xx`, `SIM-xx`) para que la trazabilidad con la planilla y con Jira sea directa.
- Cuando una fila se parte en varias historias se usa sufijo numérico: `FAC-02.1`, `FAC-02.2`, `FAC-02.3`.
- Cuando **dos filas distintas del Excel comparten el mismo `Issue Key`** se desambigua con sufijo alfabético y se deja constancia en §12:
  - `FAC-05a` = fila 7 (`POST/cargarFactura`) · `FAC-05b` = fila 8 (`POST/notificaciónNuevarFactura`)
  - `CON-03a` = fila 10 (`GET/grillafacturas`) · `CON-03b` = fila 12 (`Grilla accion Eliminar`)
- `RN-Cxx` = regla de negocio transversal · `MSG-Cxx` = mensaje de UI · `SPK-Cxx` = spike.

### 1.4 Qué queda explícitamente fuera de este documento

- Épica **LOGIN** y épica **ABM** (entes, usuarios, roles, notificaciones): tienen su propio backlog.
- Reportes, dashboard y centro de ayuda: no aparecen en la planilla `CONFIRMING`.
- Todo lo que aparece en §11 (recomendaciones del PO): **no está comprometido**, es propuesta para priorizar aparte.

---

## 2. Matriz de inclusión / desestimación (fila por fila del Excel)

Leyenda de la decisión: **Incluida** = pasa a backlog tal cual · **Incluida (partida)** = genera más de una historia · **Incluida (reuso)** = el propio Excel indica que ya está desarrollada.

| Fila | Issue Key | STACK | Summary (Excel) | Escenarios de la fila | Decisión | Historias resultantes |
|------|-----------|-------|-----------------|------------------------|----------|------------------------|
| 3 | `FAC-01` | FE | Pantalla CONFIRMING - Botonera Cargar Factura | 2 (carga individual · validación EGP y Proveedor existen y activos) | Incluida (partida) | `FAC-01.1`, `FAC-01.2` |
| 4 | `FAC-02` | FE | Pantalla CONFIRMING - Botonera Cargar Factura | 4 (descargar template · cargar desde archivo · escanear facturas? · validación EGP y Proveedor) | Incluida (partida) | `FAC-02.1`, `FAC-02.2`, `FAC-02.3` (+ validación en `FAC-01.2`) |
| 5 | `FAC-03` | BE/BFF | API CONFIRMING - GET/obtenerInfoEnte | 1 (`MAGIA-120 / MAGIA-122 Ya desarrollado`) | Incluida (reuso) | `FAC-03` (HT) |
| 6 | `FAC-04` | FE | Pantalla CONFIRMING - Cargar Factura Multimoneda USD o PYG | 1 (selector de moneda USD / PYG) | Incluida | `FAC-04` |
| 7 | `FAC-05a` | BE/BFF | API CONFIRMING - POST/cargarFactura | 2 (creación OK · creación con ERROR) | Incluida | `FAC-05a` (HT) |
| 8 | `FAC-05b` | BFF | API CONFIRMING - POST/notificaciónNuevarFactura | 2 (OK → notifica al EGP · ERROR → no notifica) | Incluida | `FAC-05b` (HT) |
| 9 | `CON-01` | FE | Pantalla CONFIRMING - Filtros / Grilla / pestañas FV / FNV / FNO | 3 (filtros de búsqueda · campos de la grilla · pestañas por estado) | Incluida (partida) | `CON-01.1`, `CON-01.2`, `CON-01.3` |
| 10 | `CON-03a` | BE/BFF | API CONFIRMING - GET/grillafacturas | 1 (FE/BFF/BE consulta las facturas de la grilla) | Incluida | `CON-03a` (HT) |
| 11 | `CON-02` | FE | Pantalla CONFIRMING - Grilla acciones | 4 (botón Eliminar · botón Editar Fecha de Pago · botón Aprobar EGP condicional · mensaje «Desembolso en curso…») | Incluida | `CON-02` (1 AC por escenario) |
| 12 | `CON-03b` | FE | Pantalla CONFIRMING - Grilla accion Eliminar | 1 (modal de confirmación con datos de la factura) | Incluida | `CON-03b` |
| 13 | `CON-04` | FE | Pantalla CONFIRMING - Grilla accion Editar | 1 (modal Editar Fecha de Pago con warning de días para NO Elegible) | Incluida | `CON-04` |
| 14 | `CON-05` | FE | Pantalla CONFIRMING - Grilla accion Aprobar EGP | 1 (modal con datos bloqueados y opciones Aprobar / Rechazar con o sin motivo) | Incluida | `CON-05` |
| 15 | `CON-06` | BE/BFF | API CONFIRMING - PATCH/actualizarfactura | 1 (texto del escenario copiado de `CON-03a`, ver §12) | Incluida | `CON-06` (HT) |
| 16 | `CON-07` | *(vacío)* | Pantalla Información EGP · Recurso: EGP · Dominio: EGP | 3 (cabecera financiera EGP · cabecera financiera Proveedor · cálculo de límite = límite API − límite freezado) | Incluida (partida) | `CON-07.1`, `CON-07.2`, `CON-07.3` |
| 17 | `CON-08` | BE/BFF | API CONFIRMING - GET/obtenerInfoEnte | 1 (`MAGIA-120 / MAGIA-122 Ya desarrollado`) | Incluida (reuso) | `CON-08` (HT) |
| 18 | `CON-09` | BE/BFF? | Implementar maquina de estados de Facturas | 3 bloques (estados manual/automático con previo y posterior · Vencida automática · NO elegible + modal de corrección de fecha) | Incluida (partida) | `CON-09.1`, `CON-09.2`, `CON-09.3` (HT) |
| 19 | `CON-10` | BE/BFF | API CONFIRMING - GET/estados de facturas | 1 (condiciones de cambio de estado) | Incluida | `CON-10` (HT) |
| 20 | `CON-11` | FE | Pantalla CONFIRMING - Botonera Hablitar / Bloquear | 2 (habilitar múltiples · bloquear múltiples) | Incluida (partida) | `CON-11.1`, `CON-11.2` |
| 21 | `SIM-01` | FE | Pantalla CONFIRMING - Simular Múltiples / Simular Individual | 5 + nota (múltiple misma fecha de pago · múltiple fecha distinta · individual · validación de límite · confirmación con freeze · leyenda de valores estimativos) | Incluida (partida) | `SIM-01.1`, `SIM-01.2`, `SIM-01.3`, `SIM-01.4`, `SIM-01.5` |
| 22 | `SIM-02` | BE/BFF | API CONFIRMING - GET/simularAdelantoFactura | 3 (cálculo OK · error · validación de expiración en n días desde la aprobación del EGP) | Incluida | `SIM-02` (HT) |
| 23 | `SIM-03` | BE/BFF | API CONFIRMING - POST/generarAdelantoFactura | 6 (OK + envío al CORE · ERROR sin envío · usuario solicitante ≠ usuario que cargó · corte 17 hs · reversión automática · re-cálculo y freeze de límite) | Incluida | `SIM-03` (HT) |
| 24 | `SIM-04` | BFF | API CONFIRMING - POST/notificaciónAdelantoFactura | 4 (OK→EGP · ERROR→no EGP · OK→Proveedor crédito generado · ERROR→no Proveedor) | Incluida | `SIM-04` (HT) |
| 25 | `SIM-05` | FE | Pantalla CONFIRMING - Aprobación / Rechazo de Simulación de Adelante de Factura | 2 (aprobación por EGP · rechazo por EGP con o sin motivo) | Incluida (partida) | `SIM-05.1`, `SIM-05.2` |

**Filas desestimadas: ninguna.** La columna `DUDAS` está vacía en las 23 filas; las dudas detectadas en el análisis se abren como spikes en §10 y no se mezclan con el alcance comprometido.

---

## 3. Contexto de solución, actores y supuestos

### 3.1 Actores

| Actor | Dominio | Qué hace en la épica CONFIRMING |
|-------|---------|--------------------------------|
| **Operador de carga (EGP)** | EGP | Carga facturas individualmente, por archivo o por escaneo; habilita y bloquea facturas. |
| **Aprobador del EGP** | EGP | Aprueba o rechaza la solicitud de adelanto; consulta la información crediticia del EGP y del Proveedor; corrige la fecha de pago al rechazar con motivo. |
| **Usuario Proveedor** | Proveedor | Consulta sus facturas y solicita el adelanto (simulación individual o múltiple). |
| **Operador del Banco** | Banco | Opera la pantalla Confirming sobre cualquier ente (carga, habilitación, bloqueo, consulta). |
| **Supervisor del Banco** | Banco | Supervisa y opera excepciones; en el catálogo de permisos de la POC tiene también reversión. |
| **API ERP** | Sistema | Origen de facturas para el arribo automático en estado `Pendiente`. |
| **CORE BANKING** | Sistema | Ejecuta el desembolso y devuelve OK o error. |
| **Servicio de Notificaciones** | Sistema | Envía las notificaciones de nueva factura y de adelanto. |

> El Excel marca `Recurso: todos | dominio: todos` en casi todas las filas FE, salvo `CON-07` (`Recurso: EGP | Dominio: EGP`) y `SIM-04` (`Recurso: EGP/PROVEEDOR`). Ese marcado se respeta en el campo **Dominios** de cada tarjeta.

### 3.2 Componentes involucrados

| Componente | Rol |
|------------|-----|
| **FE — Pantalla Confirming** | Barra de filtros, cabecera de información financiera del ente, pestañas FV/FNV/FNO, grilla seleccionable, botonera global (Habilitar / Bloquear / Simular / Cargar Factura), botonera por fila, modales (alta, carga masiva y su resultado, editar fecha de pago, simulación / aprobación EGP, confirmaciones y avisos). |
| **BFF** | Orquesta las llamadas del FE, compone la grilla, dispara notificaciones. |
| **BE / Core de negocio** | Persistencia de facturas, máquina de estados, cálculo financiero, límites crediticios. |
| **API CORE BANKING** | Desembolso del adelanto y relación cuenta préstamo ↔ factura. |
| **API Entes (`MAGIA-120 / MAGIA-122`)** | Datos de existencia, estado y condiciones financieras del ente. Reutilizada por `FAC-03` y `CON-08`. |

### 3.3 Estados y pestañas (implementado en la POC)

| Pestaña | Estados que agrupa |
|---------|--------------------|
| **Facturas Vigentes (FV)** | `Pendiente`, `Habilitada`, `Bloqueada`, `Pendiente aprobación EGP`, `Pendiente de desembolso` |
| **Facturas No Vigentes (FNV)** | `Financiada`, `Vencida` |
| **Facturas No Operables (FNO)** | `NO ELEGIBLE` |

### 3.4 Supuestos (a confirmar con el equipo técnico y con el PO del cliente)

| # | Supuesto | Impacto si es falso |
|---|----------|---------------------|
| S-01 | La factura se identifica de forma única por `Nro. Factura`; no se admiten duplicados dentro del mismo EGP–Proveedor. | La POC no valida duplicados: hoy se puede cargar dos veces el mismo número. Ver `SPK-C05`. |
| S-02 | El parámetro de 30 días (fecha de pago mínima) es **configurable**, no una constante de código. | Cambia el contrato de `CON-09.3` y `CON-10`. |
| S-03 | El corte horario de las 17 hs (`SIM-03`) es hora local Paraguay y aplica solo a la generación del adelanto, no a la simulación. | Ver `SPK-C06`. |
| S-04 | «Baja» de factura (`CON-06`) es **lógica** y auditable. El Excel lo deja como pregunta abierta. | Ver `SPK-C04`. |
| S-05 | La aprobación bancaria posterior a la aprobación del EGP es automática (así lo implementa la POC y así lo comunica su leyenda). | Si vuelve a existir aprobación bancaria manual, reaparecen los botones «Banco Aprueba / Banco Rechaza» que hoy están comentados en la POC. Ver `SPK-C07`. |
| S-06 | El límite crediticio a mostrar y a validar es el del **EGP**, no el del Proveedor. | `CON-07.3`, `SIM-01.4` y `SIM-01.5` cambian de sujeto. |

---

## 4. Reglas de negocio transversales (RN)

| ID | Regla | Origen | ¿Implementada en la POC? |
|----|-------|--------|--------------------------|
| **RN-C01** | La **fecha de pago** debe estar a **30 días calendario o más desde hoy** para que la factura sea operable. Si no, la factura queda en `NO ELEGIBLE`. | Excel `CON-09` + POC (`PAYMENT_DATE_MIN_DAYS = 30`) | Sí |
| **RN-C02** | Si el usuario no indica fecha de pago, se toma por defecto la **fecha de vencimiento**. El vínculo se rompe en cuanto el usuario edita la fecha de pago manualmente. | POC | Sí |
| **RN-C03** | Los estados iniciales admitidos al dar de alta son `Pendiente`, `Habilitada` y `Bloqueada`. Cualquier otro valor (o vacío) en carga masiva se normaliza a `Pendiente`. `RN-C01` puede forzar `NO ELEGIBLE` por encima del estado solicitado. | Excel `CON-09` + POC | Sí |
| **RN-C04** | **Habilitar** solo es válido desde `Pendiente` o `Bloqueada`. | Excel `CON-11` + POC | Sí |
| **RN-C05** | **Bloquear** solo es válido desde `Pendiente` o `Habilitada`. El Excel agrega además `Pendiente de aprobación EGP` como origen válido; la POC **no** lo permite → `SPK-C02`. | Excel `CON-11` | Parcial |
| **RN-C06** | **Simular adelanto** solo es válido desde `Habilitada`. | Excel `SIM-01` + POC | Sí |
| **RN-C07** | La **simulación múltiple** exige: 2 o más facturas, todas en `Habilitada`, y **mismo EGP + mismo Proveedor + misma moneda**. Si no se cumple, la acción no se habilita. | Excel `SIM-01` + POC | Sí |
| **RN-C08** | La primera factura tildada fija la *combinatoria ancla* (EGP + Proveedor + Moneda). Las facturas que no coinciden quedan con el check deshabilitado mientras exista selección. | POC | Sí |
| **RN-C09** | Cálculo del adelanto: `interés = monto × TNA × díasAAdelantar / 365`; `comisión = monto × %comisión`; `IVA = (interés + comisión) × %IVA`; `neto = monto − interés − comisión − IVA`. `díasAAdelantar` nunca es negativo (piso 0). Las tasas salen de la configuración del EGP. | POC | Sí |
| **RN-C10** | El **monto a adelantar** no puede superar el monto de la factura. En simulación múltiple el monto es la **suma de la selección** y es de solo lectura. | POC | Sí |
| **RN-C11** | Resolución de la aprobación del EGP: **Aprueba** → `Pendiente de desembolso` (la aprobación bancaria es automática) · **Rechaza con motivo** → se pide nueva fecha de pago y la factura vuelve a `Habilitada` o cae en `NO ELEGIBLE` según `RN-C01` · **Rechaza sin motivo** → `Bloqueada`. | POC | Sí |
| **RN-C12** | Respuesta de CORE BANKING: éxito → `Financiada`; error → la factura **vuelve a `Pendiente aprobación EGP`** para reintentar (reversión automática). | Excel `SIM-03` + POC | Sí (mock: 2,5 s de latencia y 15 % de error) |
| **RN-C13** | La grilla se agrupa en tres pestañas por estado (ver §3.3). Una factura aparece en una sola pestaña. | Excel `CON-01` + POC | Sí |
| **RN-C14** | La **fecha de pago** solo es editable en los estados `NO ELEGIBLE`, `Pendiente`, `Habilitada` y `Bloqueada`. | POC | Sí (el Excel pide el botón «siempre visible y activo» → `SPK-C03`) |
| **RN-C15** | **Eliminar** exige confirmación explícita y es irreversible desde la UI. | Excel `CON-02` / `CON-03b` + POC | Sí |
| **RN-C16** | Carga masiva: son obligatorios `Nro. Factura`, `Empresa (EGP)`, `Proveedor`, `Fecha emisión`, `Fecha vencimiento`, `Moneda` y `Monto` (numérico > 0). La `Fecha de pago` ausente se completa con el vencimiento. Las filas que incumplen **no se cargan** y se informan agrupadas por motivo; el resto sí se carga (procesamiento parcial). | POC | Sí |
| **RN-C17** | Monedas operables: **GS** (guaraníes) y **USD**. En carga masiva se aceptan alias (`PYG`, `GUARANIES`, `GUARANÍES` → `GS`; `DOLAR`, `DÓLAR`, `DOLARES`, `DÓLARES` → `USD`). La moneda de la fila debe estar habilitada para el EGP. | Excel `FAC-04` + POC | Sí |
| **RN-C18** | Formato de fecha en toda la pantalla: **`dd-mm-yyyy`**. Se aceptan además `dd/mm/yyyy` y `dd.mm.yyyy` en la entrada; el almacenamiento es ISO `yyyy-mm-dd`. | POC | Sí |
| **RN-C19** | El **límite de crédito a mostrar** es `límite de crédito de la API − límite freezado`. Al crear una simulación se **freeza** el importe correspondiente y se descuenta del límite total del EGP. | Excel `CON-07` y `SIM-01` | **No** — la POC muestra el límite estático y no freeza nada → `CON-07.3`, `SIM-01.4`, `SIM-01.5` |
| **RN-C20** | El usuario que **solicita** el adelanto no puede ser el mismo que **cargó** la factura (segregación de funciones). | Excel `SIM-03` | **No** implementada en la POC |
| **RN-C21** | La generación del adelanto solo se admite **antes de las 17 hs**. | Excel `SIM-03` | **No** implementada en la POC |
| **RN-C22** | Existe un **límite de tiempo** (n días configurables) entre la aprobación del EGP y la solicitud del adelanto; superado, el adelanto se bloquea por expiración. | Excel `SIM-02` | **No** implementada en la POC |
| **RN-C23** | El EGP y el Proveedor asociados a la factura deben **existir y estar activos** al momento de guardar. | Excel `FAC-01` y `FAC-02` | **No** implementada en la POC |
| **RN-C24** | En todo cálculo mostrado en el modal de simulación debe figurar una leyenda de que **los valores simulados son estimativos**. | Excel `SIM-01` (nota al pie) | **No** implementada en la POC |

---

## 5. Catálogo de mensajes de UI (MSG)

Todos los textos marcados como **literal POC** están transcriptos exactamente como los emite la POC. Los marcados como **pendiente** son requeridos por el Excel y todavía no existen: deben redactarse y aprobarse antes del desarrollo.

### 5.1 Carga de facturas

| ID | Tipo | Título | Texto | Origen |
|----|------|--------|-------|--------|
| `MSG-C01` | Éxito | Éxito | `Factura leída correctamente desde código QR.` | literal POC |
| `MSG-C02` | Error | Aviso | `Por favor complete todos los campos obligatorios.` | literal POC |
| `MSG-C03` | Advertencia | Factura no elegible | `La factura fue registrada en estado NO ELEGIBLE: la fecha de pago debe estar a 30 días o más desde hoy.` | literal POC |
| `MSG-C04` | Éxito | Factura Registrada | `La factura ha sido registrada exitosamente.` | literal POC |
| `MSG-C05` | Ayuda en línea | — | `Por defecto coincide con el vencimiento. Si queda a menos de 30 días, la factura será NO ELEGIBLE.` | literal POC |
| `MSG-C06` | Ayuda en línea | — | `Use estos botones para procesar varias facturas a la vez desde un archivo .xls, .xlsx o .csv.` | literal POC |
| `MSG-C07` | Error | Descarga fallida | `No se pudo generar el template (librería de Excel no disponible).` | literal POC |
| `MSG-C08` | Error | Carga fallida | `No se pudo procesar el archivo (librería de Excel no disponible).` | literal POC |
| `MSG-C09` | Error | Carga fallida | `No se pudo leer el archivo: {detalle}` | literal POC |
| `MSG-C10` | Resultado | Carga masiva exitosa / Carga masiva con observaciones / Carga masiva sin facturas registradas | `Se procesaron {n} filas:` + píldoras `{n} cargadas`, `{n} incompletas`, `{n} con moneda inválida` | literal POC |
| `MSG-C11` | Resultado — bloque OK | — | `Facturas cargadas ({n})` · corte visual a 15 ítems con `… y {n} facturas más` | literal POC |
| `MSG-C12` | Resultado — bloque error | — | `No cargadas — información incompleta ({n})` | literal POC |
| `MSG-C13` | Resultado — bloque error | — | `No cargadas — moneda no habilitada por el ente ({n})` · detalle por fila: `{id} — moneda {moneda} no habilitada para {ente} (permitidas: {lista})` | literal POC |
| `MSG-C14` | Resultado — vacío | — | `El archivo no contiene filas para procesar.` | literal POC |
| `MSG-C15` | Error | Aviso | Mensaje de EGP/Proveedor inexistente o inactivo al guardar la factura. | **pendiente** (`RN-C23`) |

### 5.2 Consulta y gestión de la grilla

| ID | Tipo | Título | Texto | Origen |
|----|------|--------|-------|--------|
| `MSG-C16` | Estado vacío | — | `No se encontraron facturas con los filtros aplicados.` | literal POC |
| `MSG-C17` | Tooltip | — | `Seleccionar todas las facturas visibles ({n})` / `Deseleccionar todas las facturas ({n} seleccionadas)` / `No hay facturas visibles para seleccionar` | literal POC |
| `MSG-C18` | Tooltip | — | `No coincide con EGP / Proveedor / Moneda de la selección` | literal POC |
| `MSG-C19` | Indicador de fila | — | Por estado: `Use Habilitar / Bloquear` (Pendiente) · `No operable` (Bloqueada) · `CORE BANKING desembolsando…` (Pendiente de desembolso) · `Vencida` · `Financiada` | literal POC |
| `MSG-C20` | Confirmación | Eliminar factura | `¿Confirma eliminar la factura {id} ({egp} – {proveedor})? Esta acción no se puede deshacer.` | literal POC |
| `MSG-C21` | Éxito | Factura eliminada | `La factura fue eliminada correctamente.` | literal POC |

### 5.3 Fecha de pago

| ID | Tipo | Título | Texto | Origen |
|----|------|--------|-------|--------|
| `MSG-C22` | Ayuda en modal | — | `Factura {id}. Si la nueva fecha está a 30 días o más desde hoy, la factura vuelve a Habilitada (Vigentes).` *(cuando la factura está en `NO ELEGIBLE`)* | literal POC |
| `MSG-C23` | Ayuda en modal | — | `Factura {id} ({estado}). Si la fecha de pago queda a menos de 30 días desde hoy, la factura pasará a No Operables (NO ELEGIBLE) y dejará de figurar en Vigentes.` | literal POC |
| `MSG-C24` | Error | Fecha inválida | `Indique una fecha de pago válida (dd-mm-yyyy).` | literal POC |
| `MSG-C25` | Confirmación | Advertencia — factura no vigente | `La fecha de pago indicada ({fecha}) está a menos de 30 días desde hoy.` · `La factura {id} quedará No Operable (NO ELEGIBLE) y dejará de estar en Vigentes.` · `¿Desea guardar de todos modos?` | literal POC |
| `MSG-C26` | Advertencia | Fecha de pago actualizada | `La fecha de pago quedó en {fecha}. La factura {id} pasó a No Operables (NO ELEGIBLE) y ya no figura en Vigentes.` | literal POC |
| `MSG-C27` | Advertencia | Fecha de pago actualizada | `La fecha de pago quedó en {fecha}. La factura {id} sigue en No Operables (NO ELEGIBLE): se requieren al menos 30 días desde hoy.` | literal POC |
| `MSG-C28` | Éxito | Fecha de pago actualizada | `La fecha de pago quedó en {fecha}. La factura {id} volvió a Habilitada (Vigentes).` | literal POC |
| `MSG-C29` | Éxito | Fecha de pago actualizada | `La fecha de pago de la factura {id} quedó en {fecha}.` | literal POC |

### 5.4 Habilitar / Bloquear

| ID | Tipo | Título | Texto | Origen |
|----|------|--------|-------|--------|
| `MSG-C30` | Tooltip | — | `Seleccione facturas en estado Bloqueada o Pendiente para habilitar` (sin selección) · `Solo pueden habilitarse facturas en estado Bloqueada o Pendiente` (selección inválida) · `Habilitar {n} facturas seleccionadas` (activo) | literal POC |
| `MSG-C31` | Confirmación | Habilitar facturas | `¿Confirma habilitar la factura {id}? Pasará al estado "Habilitada".` · plural: `¿Confirma habilitar {n} facturas seleccionadas ({ids} y {m} más)? Todas pasarán al estado "Habilitada".` | literal POC |
| `MSG-C32` | Éxito | Habilitación exitosa | `La factura fue habilitada correctamente.` · `{n} facturas fueron habilitadas correctamente.` | literal POC |
| `MSG-C33` | Tooltip | — | `Seleccione facturas en estado Habilitada o Pendiente para bloquear` · `Solo pueden bloquearse facturas en estado Habilitada o Pendiente` · `Bloquear {n} facturas seleccionadas` | literal POC |
| `MSG-C34` | Confirmación | Bloquear facturas | `¿Confirma bloquear la factura {id}? Pasará al estado "Bloqueada".` · plural equivalente | literal POC |
| `MSG-C35` | Éxito | Bloqueo exitoso | `La factura fue bloqueada correctamente.` · `{n} facturas fueron bloqueadas correctamente.` | literal POC |

### 5.5 Simulación y adelanto

| ID | Tipo | Título | Texto | Origen |
|----|------|--------|-------|--------|
| `MSG-C36` | Tooltip | — | `Seleccione al menos 2 facturas Habilitada (misma combinatoria) para simular` · `Seleccione 2 o más facturas Habilitada con mismo EGP, Proveedor y Moneda` · `Simular adelanto de {n} facturas ({egp} – {proveedor} – {moneda})` | literal POC |
| `MSG-C37` | Ayuda en modal | — | `Revise el cálculo del adelanto. Al ejecutar, la solicitud pasa a Pendiente aprobación EGP.` (individual) · `Revise el cálculo. Al ejecutar, todas las facturas seleccionadas pasan a Pendiente aprobación EGP.` (masiva) · `Al aprobar, el banco aprueba la TX automáticamente y la factura pasa a Pendiente de desembolso.` (aprobación EGP) | literal POC |
| `MSG-C38` | Leyenda del ticket | — | `Días a adelantar` · `Intereses a descontar` · `Comisiones operativas` · `I.V.A.` · `Monto Neto a Acreditar` · subtexto `Vto ref.: {fecha}` | literal POC |
| `MSG-C39` | Confirmación | Confirmar adelanto / Confirmar adelanto masivo | `¿Confirma solicitar el adelanto de la factura {id}?` · `Monto neto estimado: {neto}` · `Pasará a "Pendiente aprobación EGP".` (y su variante masiva con `{n}` facturas) | literal POC |
| `MSG-C40` | Éxito | Solicitud enviada al EGP / Simulación masiva | `La solicitud de adelanto para la factura {id} fue enviada al EGP. Estado: "Pendiente aprobación EGP".` · `{n} facturas enviadas a aprobación EGP.` | literal POC |
| `MSG-C41` | Error | Error | `No se pudo abrir el modal de simulación.` | literal POC |
| `MSG-C42` | Tooltip | — | `Moneda definida en la factura` · `Monto total de la selección` · `Monto del adelanto` · `Este EGP opera en múltiples monedas` · `Moneda única habilitada para este participante` | literal POC |
| `MSG-C43` | Leyenda obligatoria | — | Leyenda de que los importes del modal de simulación **son estimativos**. | **pendiente** (`RN-C24`) |
| `MSG-C44` | Advertencia | — | Aviso de que una o más facturas quedaron deshabilitadas por **exceder el límite de crédito del EGP**. | **pendiente** (`RN-C19`) |
| `MSG-C45` | Error | — | Aviso de **expiración**: pasaron más de *n* días desde la aprobación del EGP. | **pendiente** (`RN-C22`) |
| `MSG-C46` | Error | — | Aviso de **segregación de funciones**: el solicitante del adelanto es quien cargó la factura. | **pendiente** (`RN-C20`) |
| `MSG-C47` | Error | — | Aviso de **corte horario**: no se admiten solicitudes de adelanto después de las 17 hs. | **pendiente** (`RN-C21`) |

### 5.6 Aprobación / rechazo del EGP y desembolso

| ID | Tipo | Título | Texto | Origen |
|----|------|--------|-------|--------|
| `MSG-C48` | Éxito | EGP aprobó — desembolso automático | `EGP aprobó el adelanto. La aprobación bancaria es automática: la factura {id} pasa a "Pendiente de desembolso".` | literal POC |
| `MSG-C49` | Entrada de dato | — | `EGP rechaza con motivo. Indique la nueva fecha de pago (dd-mm-yyyy) para la factura {id}:` | literal POC |
| `MSG-C50` | Error | Fecha inválida | `Formato de fecha inválido. Use dd-mm-yyyy.` | literal POC |
| `MSG-C51` | Éxito | EGP rechazó con motivo | `El EGP rechazó con motivo. La factura {id} vuelve a Habilitada (fecha de pago: {fecha}).` · variante: `… queda en NO ELEGIBLE (fecha de pago menor a 30 días) …` | literal POC |
| `MSG-C52` | Éxito | EGP rechazó | `El EGP rechazó sin motivo. La factura {id} pasa a estado Bloqueada.` | literal POC |
| `MSG-C53` | Error | Error de desembolso | `La API CORE BANKING reportó un ERROR al desembolsar la factura {id}. La factura vuelve a "Pendiente aprobación EGP" para reintentar.` | literal POC |
| `MSG-C54` | Éxito | Adelanto acreditado | `Desembolso completado por CORE BANKING. La factura {id} pasa a estado "Financiada".` | literal POC |
| `MSG-C55` | Campo de captura | — | Campo de **motivo de rechazo** del EGP (texto). | **pendiente** — el Excel pide «Rechazar (con o sin motivo)» y la POC solo pide la nueva fecha de pago; ver `SPK-C08` |

---

## 6. Máquina de estados de facturas (referencia)

Tabla de transiciones que sirve de base a `CON-09.1`, `CON-09.2`, `CON-09.3` y `CON-10`. «M» = ejecución manual (la dispara una persona), «A» = ejecución automática (la dispara el sistema).

| # | Estado previo | Estado posterior | Disparador | M/A | Regla |
|---|---------------|------------------|------------|-----|-------|
| T-01 | — (alta) | `Pendiente` | Alta manual, carga masiva o arribo desde API ERP | A | `RN-C03` |
| T-02 | — (alta) | `Habilitada` / `Bloqueada` | Alta con estado inicial elegido por el usuario | M | `RN-C03` |
| T-03 | — (alta) | `NO ELEGIBLE` | Fecha de pago a menos de 30 días | A | `RN-C01` |
| T-04 | `Pendiente`, `Bloqueada` | `Habilitada` | Acción **Habilitar** | M | `RN-C04` |
| T-05 | `Pendiente`, `Habilitada` | `Bloqueada` | Acción **Bloquear** | M | `RN-C05` |
| T-06 | `Habilitada` | `Pendiente aprobación EGP` | Ejecutar adelanto (individual o múltiple) | M | `RN-C06`, `RN-C07` |
| T-07 | `Pendiente aprobación EGP` | `Pendiente de desembolso` | EGP aprueba (aprobación bancaria automática) | M → A | `RN-C11` |
| T-08 | `Pendiente aprobación EGP` | `Habilitada` | EGP rechaza con motivo y la nueva fecha de pago cumple `RN-C01` | M | `RN-C11` |
| T-09 | `Pendiente aprobación EGP` | `NO ELEGIBLE` | EGP rechaza con motivo y la nueva fecha de pago **no** cumple `RN-C01` | M | `RN-C01`, `RN-C11` |
| T-10 | `Pendiente aprobación EGP` | `Bloqueada` | EGP rechaza sin motivo | M | `RN-C11` |
| T-11 | `Pendiente de desembolso` | `Financiada` | CORE BANKING confirma el desembolso | A | `RN-C12` |
| T-12 | `Pendiente de desembolso` | `Pendiente aprobación EGP` | CORE BANKING devuelve error (reversión automática) | A | `RN-C12` |
| T-13 | `Pendiente`, `Habilitada`, `Bloqueada` | `NO ELEGIBLE` | Edición de la fecha de pago a menos de 30 días | M → A | `RN-C01`, `RN-C14` |
| T-14 | `NO ELEGIBLE` | `Habilitada` | Edición de la fecha de pago a 30 días o más | M → A | `RN-C01` |
| T-15 | Cualquier estado operable | `Vencida` | Fecha de vencimiento documental dentro del umbral definido por el Excel | A | `CON-09.2` · **no implementado en la POC** · ver `SPK-C01` |

> **Estados terminales:** `Financiada` y `Vencida` no tienen transición de salida. `NO ELEGIBLE` es el único estado no operable con salida (T-14).

---

## 7. Historias de usuario funcionales (tarjetas de backlog)

### 7.1 Grupo FAC — Carga de facturas

### FAC-01.1 — Cargar una factura individual desde la pantalla Confirming

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador de carga del EGP (también Operador del Banco) |
| **Dominios** | Todos (`Recurso: todos \| dominio: todos`) |
| **Prioridad sugerida** | Must |
| **Depende de** | `FAC-05a` (POST/cargarFactura), `CON-01.1` (grilla donde se ve el resultado) |
| **Habilita** | `CON-11.1`, `CON-11.2`, `SIM-01.1` |
| **Pantalla POC** | Confirming → botón **Cargar Factura** → modal **Cargar Nueva Factura** → bloque «Carga individual» |

#### Historia
Como **operador de carga del EGP**
quiero **registrar una factura de a una desde la pantalla Confirming**
para **incorporarla al circuito de confirming sin depender del archivo masivo ni del ERP**.

#### Valor de negocio
Es la puerta de entrada del negocio: sin factura cargada no hay habilitación, ni simulación, ni adelanto. Habilita la operación manual y la carga de excepciones que el ERP no envía.

#### Escenarios fuente
> `OBJETIVO`: Botonera global de la pantalla: botón cargar factura
> Flujo de Crear factura individual
> `ESCENARIOS`: -Escenario Cargar facturas individual

#### Criterios de aceptación
1. **[Feliz]** Con la botonera global visible, al pulsar **Cargar Factura** se abre el modal «Cargar Nueva Factura» con el bloque de carga individual y los campos `Nro. Factura`, `Empresa (EGP)`, `Proveedor`, `Fecha Emisión`, `Fecha Vencimiento`, `Fecha de Pago`, `Moneda`, `Monto` y `Estado Inicial`.
2. **[Feliz]** Al guardar con todos los campos obligatorios completos, la factura se registra, el modal se cierra, el formulario se limpia, la grilla se refresca respetando filtros y pestaña activos, y se muestra `MSG-C04`.
3. **[Alternativo]** `Estado Inicial` ofrece únicamente `Pendiente` (por defecto), `Habilitada` y `Bloqueada` (`RN-C03`), y la factura queda en el estado elegido.
4. **[Alternativo]** Al informar la `Fecha Vencimiento`, la `Fecha de Pago` se autocompleta con ese mismo valor mientras el usuario no la haya editado manualmente (`RN-C02`); el campo muestra la ayuda `MSG-C05`.
5. **[Error / validación]** Si falta `Nro. Factura`, `Fecha Emisión`, `Fecha Vencimiento`, `Fecha de Pago` o `Monto`, no se registra nada y se muestra `MSG-C02`.
6. **[Error / validación]** Si la `Fecha de Pago` está a menos de 30 días de hoy, la factura **se registra igual** pero en estado `NO ELEGIBLE` y se informa con `MSG-C03` (`RN-C01`); queda visible en la pestaña **Facturas No Operables**.
7. **[Alternativo]** Las fechas se ingresan y se muestran en formato `dd-mm-yyyy` (`RN-C18`).
8. **[Alternativo]** Al cancelar o cerrar el modal no se registra ninguna factura y la grilla queda intacta.

#### Escenarios BDD
```gherkin
Característica: Carga individual de facturas
  Antecedentes:
    Dado que ingresé al Portal de Confirming con un usuario habilitado para cargar facturas
    Y estoy en la pantalla "Confirming"

  Escenario: Alta exitosa en estado Pendiente
    Cuando pulso "Cargar Factura"
    Y completo el número "001-001-0001234", el EGP, el proveedor, la emisión, un vencimiento a 60 días, el monto y dejo el estado inicial en "Pendiente"
    Y pulso "Guardar Factura"
    Entonces el modal se cierra
    Y veo el mensaje MSG-C04
    Y la factura "001-001-0001234" aparece en la pestaña "Facturas Vigentes" con estado "Pendiente"

  Escenario: La fecha de pago se hereda del vencimiento
    Dado que abrí el modal de carga individual
    Cuando informo la fecha de vencimiento "15-12-2026"
    Y no edito la fecha de pago
    Entonces el campo "Fecha de Pago" muestra "15-12-2026"

  Escenario: Falta un campo obligatorio
    Dado que abrí el modal de carga individual
    Cuando dejo el monto vacío
    Y pulso "Guardar Factura"
    Entonces veo el mensaje MSG-C02
    Y no se registra ninguna factura

  Escenario: Alta con fecha de pago a menos de 30 días
    Dado que abrí el modal de carga individual
    Cuando completo todos los campos con una fecha de pago a 10 días de hoy
    Y pulso "Guardar Factura"
    Entonces veo el mensaje MSG-C03
    Y la factura queda en estado "NO ELEGIBLE"
    Y se lista en la pestaña "Facturas No Operables"
```

#### Fuera de alcance
- Carga masiva (`FAC-02.2`) y escaneo (`FAC-02.3`).
- Validación de existencia y estado del EGP y del Proveedor: es `FAC-01.2`.
- Adjuntar documentos a la factura.

#### Notas / preguntas abiertas
- En la POC los selectores de EGP y Proveedor tienen una lista fija de opciones y no están vinculados entre sí. En producción deben alimentarse del ABM y el Proveedor debe filtrarse por el EGP elegido → `SPK-C09`.
- La POC no valida duplicidad de `Nro. Factura` → `SPK-C05`.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### FAC-01.2 — Validar que el EGP y el Proveedor de la factura existan y estén activos

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador de carga del EGP (también Operador del Banco) |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `FAC-03` (GET/obtenerInfoEnte) |
| **Habilita** | `FAC-01.1`, `FAC-02.2` |
| **Pantalla POC** | Confirming → modal **Cargar Nueva Factura** *(validación no implementada en la POC)* |

#### Historia
Como **operador de carga**
quiero **que el sistema me impida registrar facturas contra un EGP o un Proveedor inexistente o inactivo**
para **no ensuciar la cartera con facturas que nunca van a poder operarse**.

#### Valor de negocio
Evita facturas huérfanas que bloquean el circuito más adelante (al simular o al desembolsar) y que obligan a depuraciones manuales. Es la única validación de integridad que el Excel pide de forma explícita y repetida (aparece en `FAC-01` y en `FAC-02`).

#### Escenarios fuente
> `FAC-01` · `ESCENARIOS`: -Escenario de VALIDACION que el EGP y PROVEEDOR asociados a la factura a guardar exista y esté activo
> `FAC-02` · `ESCENARIOS`: -Escenario de VALIDACION que el EGP y PROVEEDOR asociados a la factura a guardar exista y esté activo

#### Criterios de aceptación
1. **[Feliz]** Al guardar una factura, el sistema consulta el estado del EGP y del Proveedor (`FAC-03`); si ambos existen y están activos, la carga continúa con normalidad.
2. **[Error / validación]** Si el EGP no existe o no está activo, la factura **no** se registra y se muestra `MSG-C15` indicando el ente y el motivo.
3. **[Error / validación]** Si el Proveedor no existe o no está activo, la factura **no** se registra y se muestra `MSG-C15` indicando el ente y el motivo.
4. **[Error / validación]** Si ambos entes son inválidos, el mensaje enumera los dos.
5. **[Alternativo]** En carga masiva la validación se aplica **por fila**: las filas con ente inválido no se cargan y se informan en un bloque propio del modal de resultado, junto a «incompletas» y «moneda no habilitada» (`RN-C16`).
6. **[Error / validación]** Si el servicio de entes no responde, la carga se rechaza con un mensaje de error de servicio y la operación queda reintentable; nunca se registra la factura «a ciegas».

#### Escenarios BDD
```gherkin
Característica: Validación de EGP y Proveedor al guardar una factura
  Antecedentes:
    Dado que estoy en la pantalla "Confirming"

  Escenario: EGP inactivo en carga individual
    Dado que el EGP "Tigo Paraguay" está en estado "Bloqueado"
    Cuando cargo una factura individual para ese EGP
    Y pulso "Guardar Factura"
    Entonces veo el mensaje MSG-C15
    Y la factura no se registra

  Escenario: Proveedor inexistente en carga individual
    Cuando cargo una factura individual con un proveedor que no existe en el ABM
    Y pulso "Guardar Factura"
    Entonces veo el mensaje MSG-C15
    Y la factura no se registra

  Esquema del escenario: Validación por fila en carga masiva
    Dado que subo un archivo con 3 filas
    Y la fila <fila> tiene el ente <ente> en estado <estado>
    Cuando se procesa el archivo
    Entonces esa fila se informa como no cargada por ente inválido
    Y las filas restantes sí se cargan

    Ejemplos:
      | fila | ente        | estado     |
      | 2    | EGP         | Bloqueado  |
      | 3    | Proveedor   | Inexistente|
```

#### Fuera de alcance
- Alta o modificación de entes: pertenece a la épica ABM.
- Bloqueo preventivo de la pantalla completa cuando el EGP o el Proveedor están inactivos.

#### Notas / preguntas abiertas
- «Activo» debe mapearse contra los estados del ABM (`Pendiente de Autorización`, `Autorizado`, `Activo`, `Bloqueado`): ¿un ente `Autorizado` pero no `Activo` habilita la carga? → `SPK-C10`.
- Definir si la validación se resuelve en FE (bloqueando el guardado) o en BE (`FAC-05a` devolviendo error de negocio). Recomendación del PO: **en ambos**, con el BE como fuente de verdad.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ⚠️ depende de `FAC-03` | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### FAC-02.1 — Descargar el template de carga masiva de facturas

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador de carga del EGP |
| **Dominios** | Todos |
| **Prioridad sugerida** | Should |
| **Depende de** | — |
| **Habilita** | `FAC-02.2` |
| **Pantalla POC** | Confirming → modal **Cargar Nueva Factura** → panel «Carga masiva de facturas» → botón **Descargar Template** |

#### Historia
Como **operador de carga del EGP**
quiero **descargar una planilla modelo con las columnas exactas que el portal espera**
para **preparar la carga masiva sin errores de formato ni de nombres de columna**.

#### Valor de negocio
Reduce drásticamente el rechazo de filas en la carga masiva y elimina el ida y vuelta con soporte por columnas mal nombradas.

#### Escenarios fuente
> `OBJETIVO`: Flujo de Crear factura
> `ESCENARIOS`: -Escenario Cargar facturas masivo: descargar template

#### Criterios de aceptación
1. **[Feliz]** Desde el modal de carga, el botón **Descargar Template** descarga un archivo `.xlsx` llamado `template-facturas.xlsx` con una hoja `Facturas`.
2. **[Feliz]** La primera fila contiene exactamente las cabeceras: `Nro. Factura`, `Empresa (EGP)`, `Proveedor`, `Fecha emisión`, `Fecha vencimiento`, `Fecha de pago`, `Moneda`, `Monto`, `Estado inicial`.
3. **[Alternativo]** El archivo incluye una fila de ejemplo válida que sirve de guía de formato (fechas, moneda y monto).
4. **[Alternativo]** El panel muestra la ayuda `MSG-C06` con las extensiones admitidas.
5. **[Error / validación]** Si la generación del archivo falla, se muestra `MSG-C07` y no se descarga nada.

#### Escenarios BDD
```gherkin
Característica: Template de carga masiva
  Antecedentes:
    Dado que abrí el modal "Cargar Nueva Factura"

  Escenario: Descarga del template
    Cuando pulso "Descargar Template"
    Entonces se descarga el archivo "template-facturas.xlsx"
    Y su hoja "Facturas" tiene las 9 cabeceras esperadas en la primera fila
    Y contiene una fila de ejemplo

  Escenario: Falla la generación del archivo
    Dado que el generador de planillas no está disponible
    Cuando pulso "Descargar Template"
    Entonces veo el mensaje MSG-C07
```

#### Fuera de alcance
- Template por EGP con sus monedas pre-cargadas.
- Descarga de la grilla de facturas (es otra funcionalidad, ver §11).

#### Notas / preguntas abiertas
- ¿La fila de ejemplo debe venir o confunde al usuario que la deja y termina cargando una factura de prueba? La POC la incluye. Recomendación del PO: mantenerla pero marcarla visualmente (fila gris con la leyenda «EJEMPLO — borrar antes de cargar»).

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### FAC-02.2 — Cargar facturas de forma masiva desde un archivo

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador de carga del EGP |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `FAC-02.1`, `FAC-05a`, `FAC-01.2` |
| **Habilita** | `CON-11.1`, `SIM-01.2` |
| **Pantalla POC** | Confirming → modal **Cargar Nueva Factura** → **Cargar desde archivo** → modal **Resultado de carga masiva** |

#### Historia
Como **operador de carga del EGP**
quiero **subir un archivo con muchas facturas y ver con claridad cuáles entraron y cuáles no**
para **cargar el lote del período en una sola operación y corregir solo lo que falló**.

#### Valor de negocio
Es el modo de carga real del volumen del negocio. El informe de resultado por motivo evita reprocesar el lote completo cuando fallan pocas filas.

#### Escenarios fuente
> `OBJETIVO`: Flujo de Crear factura
> `ESCENARIOS`: -Escenario Cargar facturas masico: cargar desde archivo

#### Criterios de aceptación
1. **[Feliz]** El botón **Cargar desde archivo** abre el selector de archivos y admite `.xls`, `.xlsx` y `.csv`.
2. **[Feliz]** Se procesa la primera hoja del archivo; cada fila válida se registra como factura y la grilla se refresca al finalizar.
3. **[Alternativo]** Las cabeceras se reconocen sin distinguir mayúsculas, tildes ni signos de puntuación, y se aceptan alias equivalentes (por ejemplo `Nro Factura`, `Empresa`, `EGP`, `Vencimiento`, `Fecha pago`, `Estado`).
4. **[Alternativo]** La `Fecha de pago` ausente se completa con la `Fecha vencimiento` (`RN-C02`); el `Estado inicial` distinto de `Habilitada` o `Bloqueada` se normaliza a `Pendiente` (`RN-C03`).
5. **[Alternativo]** Se aceptan montos con separadores en formato español (`1.500.000,50`) e inglés (`1,500,000.50`), y fechas en `dd-mm-yyyy`, `dd/mm/yyyy` e ISO.
6. **[Error / validación]** Las filas sin alguno de los campos obligatorios, o con monto no numérico o menor o igual a cero, **no se cargan** y se listan en el bloque `MSG-C12`; se identifican por número de factura o, si no lo tienen, por número de fila (`RN-C16`).
7. **[Error / validación]** Las filas cuya moneda no está habilitada para el EGP **no se cargan** y se listan en el bloque `MSG-C13`, indicando la moneda enviada y las permitidas (`RN-C17`).
8. **[Error / validación]** Las filas con EGP o Proveedor inexistente o inactivo no se cargan (`FAC-01.2`).
9. **[Feliz]** Al terminar se abre el modal de resultado con el título correspondiente y el resumen `MSG-C10`: total de filas procesadas y cantidad de cargadas, incompletas y con moneda inválida.
10. **[Alternativo]** El bloque de cargadas lista hasta 15 números de factura y resume el resto con `… y {n} facturas más` (`MSG-C11`); los bloques de error listan todas las filas con scroll.
11. **[Error / validación]** Si el archivo no tiene filas procesables se muestra `MSG-C14`; si no se puede leer, `MSG-C09`; si el procesador de planillas no está disponible, `MSG-C08`.
12. **[Alternativo]** Las filas que sí cumplen se cargan aunque otras fallen (procesamiento parcial), y `RN-C01` puede dejar alguna de ellas en `NO ELEGIBLE`.

#### Escenarios BDD
```gherkin
Característica: Carga masiva de facturas desde archivo
  Antecedentes:
    Dado que abrí el modal "Cargar Nueva Factura"

  Escenario: Lote totalmente válido
    Cuando subo un archivo con 20 filas válidas
    Entonces se registran 20 facturas
    Y el modal de resultado se titula "Carga masiva exitosa"
    Y el resumen indica "20 cargadas"
    Y el bloque de cargadas muestra 15 números y la leyenda "… y 5 facturas más"

  Escenario: Lote con filas incompletas
    Cuando subo un archivo con 10 filas de las cuales 2 no tienen monto
    Entonces se registran 8 facturas
    Y el modal se titula "Carga masiva con observaciones"
    Y el bloque MSG-C12 lista las 2 filas rechazadas

  Escenario: Moneda no habilitada para el ente
    Dado que el EGP "Tigo Paraguay" solo opera en "GS"
    Cuando subo un archivo con una fila de ese EGP en moneda "USD"
    Entonces esa fila no se carga
    Y el bloque MSG-C13 indica la moneda enviada y las permitidas

  Escenario: Archivo vacío
    Cuando subo un archivo sin filas de datos
    Entonces veo el mensaje MSG-C14
    Y no se registra ninguna factura
```

#### Fuera de alcance
- Previsualización de las filas antes de confirmar la carga.
- Deshacer un lote ya cargado.
- Límite máximo de filas por archivo (hoy no existe) → ver §11.

#### Notas / preguntas abiertas
- Falta definir el **límite de filas por archivo** y el comportamiento ante archivos muy grandes → `SPK-C11`.
- La POC no informa cuáles de las filas cargadas quedaron en `NO ELEGIBLE`. Recomendación del PO: agregar un cuarto bloque informativo «cargadas como NO ELEGIBLE».

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ⚠️ tamaño grande, considerar partir el informe de resultado | ⚠️ | ✅ |

---

### FAC-02.3 — Cargar una factura escaneando el documento

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador de carga del EGP |
| **Dominios** | Todos |
| **Prioridad sugerida** | Could |
| **Depende de** | `SPK-C12` (definición de la fuente de datos del escaneo) |
| **Habilita** | `FAC-01.1` (acelera el mismo alta) |
| **Pantalla POC** | Confirming → modal **Cargar Nueva Factura** → ícono de escaneo (overlay «Escaneando documento...») |

#### Historia
Como **operador de carga del EGP**
quiero **escanear el documento de la factura y que el formulario se complete solo**
para **cargar más rápido y con menos errores de tipeo**.

#### Valor de negocio
Reduce el tiempo de carga por factura y los errores de transcripción de número, fechas y monto, que hoy derivan en facturas rechazadas o no elegibles.

#### Escenarios fuente
> `ESCENARIOS`: -Escenario scanear facturas?

> ⚠️ El escenario está redactado **con signo de pregunta** en el Excel: el propio requerimiento lo plantea como una posibilidad, no como un compromiso cerrado. Se incorpora como historia priorizada `Could` y **condicionada al spike `SPK-C12`**.

#### Criterios de aceptación
1. **[Feliz]** En el encabezado del modal de carga hay una acción de escaneo identificada con el rótulo «Escanear Factura».
2. **[Feliz]** Durante la lectura se muestra un overlay bloqueante con la leyenda «Escaneando documento...».
3. **[Feliz]** Al finalizar con éxito se completan `Nro. Factura`, `Empresa (EGP)`, `Proveedor`, `Fecha Emisión`, `Fecha Vencimiento`, `Moneda` y `Monto`, la `Fecha de Pago` se sincroniza con el vencimiento (`RN-C02`) y se muestra `MSG-C01`.
4. **[Alternativo]** Los datos cargados por escaneo son **editables** antes de guardar; el alta se confirma con el mismo flujo y validaciones de `FAC-01.1`.
5. **[Error / validación]** Si el documento no se puede leer, se cierra el overlay, se informa el error y el formulario queda como estaba.
6. **[Error / validación]** Los datos leídos se validan igual que en la carga manual (obligatorios, `RN-C01`, `FAC-01.2`).

#### Escenarios BDD
```gherkin
Característica: Alta de factura por escaneo
  Antecedentes:
    Dado que abrí el modal "Cargar Nueva Factura"

  Escenario: Lectura exitosa
    Cuando pulso la acción "Escanear Factura"
    Entonces veo el overlay "Escaneando documento..."
    Y al finalizar el formulario queda completo con los datos del documento
    Y veo el mensaje MSG-C01

  Escenario: Corrección manual posterior al escaneo
    Dado que escaneé una factura y el formulario quedó completo
    Cuando corrijo el monto
    Y pulso "Guardar Factura"
    Entonces la factura se registra con el monto corregido

  Escenario: Documento ilegible
    Cuando escaneo un documento que no puede interpretarse
    Entonces se cierra el overlay
    Y se informa que no se pudo leer el documento
    Y el formulario conserva los valores previos
```

#### Fuera de alcance
- Adjuntar la imagen escaneada al legajo de la factura.
- Validación del documento contra la SET / timbrado.

#### Notas / preguntas abiertas
- En la POC el escaneo es **simulado**: rellena datos aleatorios tras 2 segundos. No hay definición de la tecnología real (QR de la factura electrónica, OCR, cámara del dispositivo, lectora externa) → `SPK-C12`.
- Si el origen es el **QR de la factura electrónica**, el alcance y el esfuerzo son muy distintos a los de un OCR: conviene decidirlo antes de estimar.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ⚠️ no estimable hasta cerrar `SPK-C12` | ✅ | ✅ |

---

### FAC-04 — Cargar facturas en más de una moneda (USD / GS)

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador de carga del EGP |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `FAC-01.1`, `FAC-03` (monedas habilitadas del ente) |
| **Habilita** | `SIM-01.1`, `SIM-01.2` (la moneda condiciona la combinatoria de la simulación múltiple) |
| **Pantalla POC** | Confirming → modal **Cargar Nueva Factura** → campo **Moneda** |

#### Historia
Como **operador de carga del EGP**
quiero **elegir la moneda de la factura entre las que el ente tiene habilitadas**
para **operar el confirming tanto en guaraníes como en dólares con los mismos circuitos**.

#### Valor de negocio
Los EGP del portafolio operan en más de una moneda (la propia POC modela EGP con `GS` y `USD`). Sin selector de moneda quedaría fuera del producto una parte del volumen.

#### Escenarios fuente
> `OBJETIVO`: Flujo de Crear factura en diferentes monedas
> `ESCENARIOS`: -Escenario selector de moneda USD / PYG

#### Criterios de aceptación
1. **[Feliz]** El formulario de carga individual tiene un selector de `Moneda` con las opciones `GS (Guaraníes)` y `USD (Dólares)`.
2. **[Feliz]** La factura se registra con la moneda elegida y la grilla la muestra formateada según esa moneda.
3. **[Alternativo]** El selector solo ofrece las monedas **habilitadas para el ente**; si el ente tiene una sola moneda habilitada, queda preseleccionada y de solo lectura.
4. **[Error / validación]** En carga masiva, una fila con moneda no habilitada para el EGP no se carga y se informa con `MSG-C13` (`RN-C17`).
5. **[Alternativo]** Se aceptan los alias de moneda en carga masiva (`PYG`/`GUARANIES`/`GUARANÍES` → `GS`; `DOLAR`/`DOLARES` → `USD`).
6. **[Alternativo]** La cabecera de información del ente muestra las monedas habilitadas del EGP (`CON-07.1`).
7. **[Alternativo]** En el modal de simulación, la moneda se toma de la factura y no es editable salvo que el EGP opere en varias monedas (`MSG-C42`).

#### Escenarios BDD
```gherkin
Característica: Carga de facturas multimoneda
  Antecedentes:
    Dado que estoy en la pantalla "Confirming"

  Esquema del escenario: Alta en la moneda seleccionada
    Cuando cargo una factura del EGP <egp> con moneda <moneda> y monto <monto>
    Entonces la factura se registra en <moneda>
    Y la grilla muestra el monto formateado como <formato>

    Ejemplos:
      | egp          | moneda | monto    | formato        |
      | Retail S.A.  | GS     | 12000000 | guaraníes      |
      | Retail S.A.  | USD    | 2500     | dólares        |

  Escenario: Moneda no habilitada para el ente
    Dado que el EGP "Tigo Paraguay" solo tiene habilitada la moneda "GS"
    Cuando intento cargar una factura de ese EGP en "USD"
    Entonces la carga se rechaza
    Y se informa la moneda enviada y las permitidas
```

#### Fuera de alcance
- Conversión de moneda y cotización.
- Facturas con más de una moneda en el mismo documento.

#### Notas / preguntas abiertas
- El Excel dice «USD o PYG» y la POC rotula la moneda local como **`GS`**. Hay que unificar el rótulo del producto → `SPK-C13`.
- La POC **no** restringe el selector del alta individual a las monedas del ente (sí lo hace en la carga masiva). La restricción del AC 3 es una consolidación de ambos comportamientos y debe validarse con el PO del cliente.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### 7.2 Grupo CON — Consulta y gestión de facturas

### CON-01.1 — Ver la grilla de facturas con los datos operativos de cada una

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Usuario Proveedor, Operador y Aprobador del EGP, Operador del Banco |
| **Dominios** | Todos (`Recurso: todos \| dominio: todos`) |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-03a` (GET/grillafacturas) |
| **Habilita** | `CON-01.2`, `CON-01.3`, `CON-02`, `CON-11.1`, `CON-11.2`, `SIM-01.x` |
| **Pantalla POC** | Confirming → tabla principal |

#### Historia
Como **usuario del portal**
quiero **ver en una grilla todas las facturas que me corresponden con sus datos clave**
para **saber en qué situación está cada factura y decidir la próxima acción**.

#### Valor de negocio
Es la pantalla de trabajo diaria del producto: concentra la visión de cartera de EGP, Proveedor y Banco en una sola vista y es la base sobre la que se apoyan todas las demás acciones.

#### Escenarios fuente
> `OBJETIVO`: Crear la pantalla Confirming, su grilla y filtros, con las pestañas correspondientes a los estados de las facturas Facturas Vigentes (estados pendiente, habilitada, bloqueada, pendiente de aprobación EGP, pendiente de desembolso), Facturas No Vigentes (financiada, vencida) y Facturas No Operables (No elegible)
> `ESCENARIOS`: -Escenario de campos a Mostrar en la Grilla

#### Criterios de aceptación
1. **[Feliz]** La grilla muestra, por factura y en este orden: casilla de selección, `Nro. Factura`, `EGP (Empresa)`, `Proveedor`, `Emisión`, `Vencimiento`, `Fecha de Pago`, `Monto`, `Estado`, acción de eliminar y columna `Acciones`.
2. **[Feliz]** Las fechas se muestran en `dd-mm-yyyy` (`RN-C18`) y el monto se formatea según la moneda de la factura (`RN-C17`).
3. **[Feliz]** El estado se muestra como etiqueta con el literal exacto del estado (`Pendiente`, `Habilitada`, `Bloqueada`, `Pendiente aprobación EGP`, `Pendiente de desembolso`, `Financiada`, `Vencida`, `NO ELEGIBLE`) y con un color distintivo por estado.
4. **[Alternativo]** Si no hay resultados para la combinación de pestaña y filtros aplicados, la grilla muestra `MSG-C16` en lugar de filas.
5. **[Alternativo]** El usuario solo ve las facturas que le corresponden según su ente y su dominio: la visibilidad la resuelve el backend (`CON-03a`, AC 3) y no un selector de la pantalla.
6. **[Alternativo]** Tras cualquier acción que cambie una factura (alta, habilitar, bloquear, editar fecha, eliminar, avance de estado), la grilla se refresca conservando la pestaña, los filtros y la búsqueda vigentes.
7. **[Alternativo]** La selección de facturas se conserva al cambiar filtros o búsqueda, y se depura automáticamente de las facturas que ya no existen.

#### Escenarios BDD
```gherkin
Característica: Grilla de facturas
  Antecedentes:
    Dado que estoy en la pantalla "Confirming"

  Escenario: Columnas visibles
    Cuando se carga la grilla
    Entonces veo las columnas "Nro. Factura", "EGP (Empresa)", "Proveedor", "Emisión", "Vencimiento", "Fecha de Pago", "Monto", "Estado" y "Acciones"
    Y cada fila tiene una casilla de selección y una acción de eliminar

  Escenario: Sin resultados
    Cuando aplico un filtro que no coincide con ninguna factura
    Entonces veo el mensaje MSG-C16
    Y la grilla no muestra filas

  Escenario: Visibilidad acotada al ente del usuario
    Dado que soy un usuario del EGP "Retail S.A."
    Cuando se carga la grilla
    Entonces solo veo facturas cuyo EGP es "Retail S.A."
```

#### Fuera de alcance
- Paginación y ordenamiento por columna (no están en la POC ni en el Excel) → §11.
- Exportación de la grilla → §11.
- Enmascaramiento de información sensible por rol.

#### Notas / preguntas abiertas
- La POC no pagina: renderiza todas las facturas que pasan el filtro. Con volumen real hay que definir paginación y su contrato en `CON-03a` → `SPK-C14`.
- No hay columna de moneda: la moneda se infiere del formato del monto. Con carteras multimoneda conviene una columna propia → recomendación en §11.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CON-01.2 — Filtrar y buscar facturas en la grilla

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Usuario Proveedor, Operador y Aprobador del EGP, Operador del Banco |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-01.1` |
| **Habilita** | `CON-11.1`, `CON-11.2`, `SIM-01.2` |
| **Pantalla POC** | Confirming → barra de filtros (Buscar, Fecha de Vencimiento, Fecha de Pago, Estado) |

#### Historia
Como **usuario del portal**
quiero **filtrar y buscar facturas por número, ente, fechas y estado**
para **encontrar rápido las facturas sobre las que tengo que operar**.

#### Valor de negocio
Con carteras de cientos de facturas, el filtrado es lo que hace usable la pantalla y lo que permite armar lotes coherentes para habilitar, bloquear o simular.

#### Escenarios fuente
> `ESCENARIOS`: -Escenario de Filtros de Busqueda

#### Criterios de aceptación
1. **[Feliz]** El campo **Buscar** filtra a medida que se escribe por `Nro. Factura`, razón social del **EGP** o razón social del **Proveedor**, con coincidencia parcial e indiferente a mayúsculas y minúsculas en los nombres.
2. **[Feliz]** El filtro **Estado** ofrece `Todos los Estados` más los ocho estados de la máquina y deja solo las facturas en el estado elegido.
3. **[Feliz]** Los filtros **Fecha de Vencimiento** y **Fecha de Pago** aceptan `dd-mm-yyyy` y dejan solo las facturas con esa fecha exacta.
4. **[Alternativo]** Los filtros se combinan entre sí y **se combinan además con la pestaña activa**.
5. **[Alternativo]** Al vaciar un filtro, ese criterio deja de aplicarse sin necesidad de recargar la pantalla.
6. **[Alternativo]** Si la combinación no arroja resultados se muestra `MSG-C16`.
7. **[Error / validación]** Una fecha mal escrita no rompe la grilla: simplemente no arroja coincidencias.

#### Escenarios BDD
```gherkin
Característica: Filtros de búsqueda de la grilla de facturas
  Antecedentes:
    Dado que estoy en la pantalla "Confirming"
    Y la pestaña activa es "Facturas Vigentes"

  Escenario: Búsqueda por número de factura
    Cuando escribo "0002001" en el buscador
    Entonces la grilla solo muestra facturas cuyo número contiene "0002001"

  Escenario: Búsqueda por proveedor sin distinguir mayúsculas
    Cuando escribo "tech" en el buscador
    Entonces veo las facturas del proveedor "Tech Solutions S.A."

  Escenario: Filtro por estado
    Cuando selecciono el estado "Habilitada"
    Entonces solo veo facturas en estado "Habilitada"

  Escenario: Combinación de filtros sin resultados
    Cuando selecciono el estado "Financiada"
    Y la pestaña activa es "Facturas Vigentes"
    Entonces veo el mensaje MSG-C16
```

#### Fuera de alcance
- Filtro por rango de fechas (hoy es fecha exacta) → §11.
- Filtro por moneda o por monto → §11.
- Guardar filtros favoritos.

#### Notas / preguntas abiertas
- El filtro de estado incluye estados que no pertenecen a la pestaña activa, con lo cual es posible dejar la grilla vacía por una combinación contradictoria. Recomendación del PO: acotar las opciones del selector a los estados de la pestaña activa → `SPK-C15`.
- La búsqueda por número exige coincidencia respetando mayúsculas y minúsculas; en los otros dos campos no. Unificar el criterio.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CON-01.3 — Separar las facturas en pestañas Vigentes / No Vigentes / No Operables

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Usuario Proveedor, Operador y Aprobador del EGP, Operador del Banco |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-01.1`, `CON-09.1` (estados) |
| **Habilita** | `CON-04` (la corrección de fecha mueve la factura de pestaña) |
| **Pantalla POC** | Confirming → pestañas **Facturas Vigentes**, **Facturas No Vigentes**, **Facturas No Operables** |

#### Historia
Como **usuario del portal**
quiero **que las facturas estén agrupadas en pestañas según si son operables, si ya salieron del circuito o si están fuera de condiciones**
para **concentrarme en lo que puedo gestionar hoy sin ruido de lo que ya está cerrado**.

#### Valor de negocio
Separa la cartera accionable de la histórica y de la que requiere corrección, que es exactamente la distinción con la que trabaja el negocio.

#### Escenarios fuente
> `OBJETIVO`: … las pestañas correspondientes a los estados de las facturas Facturas Vigentes (estados pendiente, habilitada, bloqueada, pendiente de aprobación EGP, pendiente de desembolso), Facturas No Vigentes (financiada, vencida) y Facturas No Operables (No elegible)
> `ESCENARIOS`: -Escenario de pestañas FV/FNV/FNO de la grilla según estado de la facturas

#### Criterios de aceptación
1. **[Feliz]** La pantalla presenta tres pestañas: **Facturas Vigentes**, **Facturas No Vigentes** y **Facturas No Operables**, con **Facturas Vigentes** activa por defecto al entrar.
2. **[Feliz]** **Facturas Vigentes** lista exclusivamente `Pendiente`, `Habilitada`, `Bloqueada`, `Pendiente aprobación EGP` y `Pendiente de desembolso`.
3. **[Feliz]** **Facturas No Vigentes** lista exclusivamente `Financiada` y `Vencida`.
4. **[Feliz]** **Facturas No Operables** lista exclusivamente `NO ELEGIBLE`.
5. **[Alternativo]** Una factura aparece en **una sola** pestaña a la vez (`RN-C13`).
6. **[Alternativo]** Al cambiar de pestaña se conservan los filtros y la búsqueda, y se recalcula el contenido de la grilla.
7. **[Alternativo]** Cuando una acción cambia el estado de una factura y esa factura deja de pertenecer a la pestaña activa, la pantalla lleva al usuario a la pestaña donde la factura quedó, de modo que pueda verificar el resultado (por ejemplo al pasar a `NO ELEGIBLE` por edición de fecha de pago).
8. **[Alternativo]** La pestaña activa se indica visualmente y es accesible por teclado con el rol de pestaña correspondiente.

#### Escenarios BDD
```gherkin
Característica: Pestañas de la grilla de facturas
  Antecedentes:
    Dado que estoy en la pantalla "Confirming"

  Escenario: Pestaña por defecto
    Cuando entro a la pantalla
    Entonces la pestaña activa es "Facturas Vigentes"

  Esquema del escenario: Cada estado se lista en su pestaña
    Cuando abro la pestaña <pestaña>
    Entonces solo veo facturas en los estados <estados>

    Ejemplos:
      | pestaña                | estados                                                                                      |
      | Facturas Vigentes      | Pendiente, Habilitada, Bloqueada, Pendiente aprobación EGP, Pendiente de desembolso          |
      | Facturas No Vigentes   | Financiada, Vencida                                                                          |
      | Facturas No Operables  | NO ELEGIBLE                                                                                  |

  Escenario: La factura sigue al usuario al cambiar de pestaña
    Dado que estoy en "Facturas Vigentes" con una factura "Habilitada"
    Cuando edito su fecha de pago a menos de 30 días y confirmo
    Entonces la pantalla me lleva a "Facturas No Operables"
    Y veo la factura con estado "NO ELEGIBLE"
```

#### Fuera de alcance
- Contador de facturas por pestaña.
- Pestaña de facturas eliminadas / auditoría.

#### Notas / preguntas abiertas
- Falta definir si `Vencida` debe convivir con `Financiada` en la misma pestaña: son situaciones de negocio opuestas (una cerrada con éxito, la otra perdida). El Excel las agrupa; se respeta, pero conviene revisarlo con el PO del cliente.
- Un contador por pestaña ayudaría a la gestión diaria → §11.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CON-02 — Disponer de la botonera de acciones por factura en la grilla

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador y Aprobador del EGP, Operador del Banco, Usuario Proveedor |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-01.1` |
| **Habilita** | `CON-03b`, `CON-04`, `CON-05` |
| **Pantalla POC** | Confirming → columna **Acciones** y columna de eliminar de cada fila |

#### Historia
Como **usuario del portal**
quiero **tener en cada fila las acciones que puedo ejecutar sobre esa factura y saber cuándo está en proceso**
para **operar factura por factura sin abrir pantallas intermedias ni equivocarme de acción**.

#### Valor de negocio
Concentra la operación en la grilla y evita errores: el usuario solo ve habilitado lo que el estado de la factura permite. El Excel es explícito en que esta historia **solo entrega la botonera**; cada flujo se desarrolla en su propia historia.

#### Escenarios fuente
> `OBJETIVO`: Tiene como objetivo SOLO agregar la Botonera de la grilla por factura, cada flujo luego se desarrollara en otras historias
> `ESCENARIOS`:
> -Escenario de boton Eliminar Factura, siempre visible y activo
> -Escenario de booón Editar Fecha de Pago, siempre visible y activo
> -Escenario de botón Aprobar EGP, solo se muestra para facturas en estado Pendiente de Aprobación EGP
> -Escenario de Mensaje de Espera en desembolso: cuando e desembolso está en curso se muestra un msj dentro de la columna de acciones "Desembolso en curso..." con ruedita animada, solo se muestra para facturas en estado "Pendiente de Desembolso"

#### Criterios de aceptación
1. **[Feliz — escenario Eliminar]** Toda fila, sea cual sea el estado de la factura, presenta la acción **Eliminar factura** visible y activa, con rótulo accesible «Eliminar factura». El flujo se resuelve en `CON-03b`.
2. **[Feliz — escenario Editar Fecha de Pago]** Toda fila presenta la acción **Editar fecha de pago** visible y activa. El flujo se resuelve en `CON-04`.
3. **[Feliz — escenario Aprobar EGP]** La acción **Aprobar EGP** se muestra **únicamente** en facturas en estado `Pendiente aprobación EGP`; en el resto de los estados no aparece. El flujo se resuelve en `CON-05`.
4. **[Feliz — escenario Mensaje de espera]** En facturas en estado `Pendiente de desembolso` la columna `Acciones` muestra, en lugar de botones, un indicador de proceso en curso con animación giratoria y el texto de espera de desembolso (`MSG-C19`).
5. **[Alternativo]** En facturas en estado `Habilitada` se ofrece además la acción **Simular**, que abre el flujo de `SIM-01.1`.
6. **[Alternativo]** En los estados sin acción propia se muestra un indicador de situación en lugar de botones: `Use Habilitar / Bloquear` en `Pendiente`, `No operable` en `Bloqueada`, `Vencida` y `Financiada` en los estados terminales (`MSG-C19`).
7. **[Alternativo]** Cuando hay una selección múltiple válida para simular, la acción **Simular** de cada fila se deshabilita y explica por tooltip que debe usarse la acción de la cabecera (`RN-C07`).
8. **[Alternativo]** Las acciones que el rol del usuario no tiene permitidas no se muestran.

#### Escenarios BDD
```gherkin
Característica: Botonera de acciones por factura
  Antecedentes:
    Dado que estoy en la pantalla "Confirming"

  Esquema del escenario: Acciones disponibles según estado
    Dado una factura en estado <estado>
    Cuando observo su columna "Acciones"
    Entonces veo <contenido>
    Y siempre veo la acción de eliminar y la de editar fecha de pago

    Ejemplos:
      | estado                     | contenido                                  |
      | Pendiente                  | el indicador "Use Habilitar / Bloquear"    |
      | Habilitada                 | el botón "Simular"                         |
      | Bloqueada                  | el indicador "No operable"                 |
      | Pendiente aprobación EGP   | el botón "Aprobar EGP"                     |
      | Pendiente de desembolso    | el indicador de desembolso en curso        |
      | Financiada                 | el indicador "Financiada"                  |
      | Vencida                    | el indicador "Vencida"                     |

  Escenario: Aprobar EGP no aparece fuera de su estado
    Dado una factura en estado "Habilitada"
    Entonces no veo el botón "Aprobar EGP"

  Escenario: Indicador de desembolso en curso
    Dado una factura en estado "Pendiente de desembolso"
    Entonces la columna "Acciones" muestra un indicador animado de desembolso en curso
    Y no ofrece botones de acción sobre esa factura
```

#### Fuera de alcance
- Los flujos que abren los botones: `CON-03b`, `CON-04`, `CON-05`, `SIM-01.1`.
- Acción de reversión de factura (aparece en el catálogo de permisos pero no en el Excel) → §11.

#### Notas / preguntas abiertas
- **Divergencia con la POC:** el Excel pide **Editar Fecha de Pago siempre visible y activo**; la POC solo lo ofrece en `NO ELEGIBLE`, `Pendiente`, `Habilitada` y `Bloqueada` (`RN-C14`). Hay que decidir si en `Pendiente aprobación EGP`, `Pendiente de desembolso`, `Financiada` y `Vencida` el botón se oculta, se muestra deshabilitado con motivo, o se habilita → `SPK-C03`.
- **Divergencia de texto:** el Excel pide el literal `"Desembolso en curso..."`; la POC muestra `CORE BANKING desembolsando…`. Definir el texto definitivo del producto.
- El Excel pide Eliminar «siempre visible y activo», lo que incluye facturas `Financiada`. Confirmar que el negocio realmente quiere permitir eliminar una factura ya desembolsada → `SPK-C04`.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CON-03b — Eliminar una factura con confirmación previa

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador de carga del EGP, Operador del Banco |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-02`, `CON-06` (PATCH/actualizarfactura para la baja) |
| **Habilita** | — |
| **Pantalla POC** | Confirming → acción de eliminar de la fila → modal de confirmación **Eliminar factura** |

#### Historia
Como **operador de carga**
quiero **eliminar una factura cargada por error confirmando antes qué factura estoy dando de baja**
para **depurar la cartera sin riesgo de borrar la factura equivocada**.

#### Valor de negocio
La carga manual y masiva genera errores; sin baja, la cartera se ensucia y se distorsionan los indicadores. La confirmación con datos identificatorios evita bajas accidentales de una acción irreversible.

#### Escenarios fuente
> `OBJETIVO`: Flujo de Eliminar factura
> `ESCENARIOS`: -Escenario modal de confirmación del boton Eliminar Factura, con los datos de la factura y boton de confirmar

#### Criterios de aceptación
1. **[Feliz]** Al pulsar la acción de eliminar de una fila se abre un modal titulado «Eliminar factura» que identifica la factura por **número, EGP y Proveedor** y advierte que la acción no se puede deshacer (`MSG-C20`).
2. **[Feliz]** Al confirmar, la factura desaparece de la grilla, se quita de la selección múltiple si estaba tildada, la grilla se refresca respetando filtros y pestaña, y se muestra `MSG-C21`.
3. **[Alternativo]** Al cancelar o cerrar el modal, la factura permanece intacta y no se ejecuta ninguna acción.
4. **[Alternativo]** La acción está disponible en toda la grilla, independientemente de la pestaña y del estado de la factura (`CON-02`, AC 1).
5. **[Error / validación]** Si la factura ya no existe (por ejemplo, eliminada en otra sesión), se informa el error y la grilla se refresca sin romper la pantalla.
6. **[Alternativo]** La eliminación se registra en auditoría con usuario, fecha y hora (`RN-C15`).

#### Escenarios BDD
```gherkin
Característica: Eliminar factura
  Antecedentes:
    Dado que estoy en la pantalla "Confirming"
    Y existe la factura "001-001-0001001" del EGP "Retail S.A." y el proveedor "Tech Solutions S.A."

  Escenario: Eliminación confirmada
    Cuando pulso la acción de eliminar de esa factura
    Entonces veo el mensaje de confirmación MSG-C20 con el número, el EGP y el proveedor
    Cuando confirmo
    Entonces la factura ya no aparece en la grilla
    Y veo el mensaje MSG-C21

  Escenario: Eliminación cancelada
    Cuando pulso la acción de eliminar de esa factura
    Y cancelo la confirmación
    Entonces la factura sigue en la grilla

  Escenario: La factura eliminada sale de la selección
    Dado que la factura está tildada para una acción masiva
    Cuando la elimino y confirmo
    Entonces la selección se actualiza y ya no la incluye
```

#### Fuera de alcance
- Eliminación masiva de varias facturas seleccionadas → §11.
- Recuperación / papelera de facturas eliminadas.

#### Notas / preguntas abiertas
- El Excel deja abierto en `CON-06` si la baja es **lógica o física**. El AC 6 asume baja lógica auditable (supuesto S-04) → `SPK-C04`.
- ¿Se puede eliminar una factura ya `Financiada` o en `Pendiente de desembolso`? Hoy la POC lo permite. Recomendación del PO: prohibirlo a partir de `Pendiente aprobación EGP`.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CON-04 — Editar la fecha de pago de una factura con aviso de impacto

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador / Aprobador del EGP |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-02`, `CON-06`, `CON-09.3` |
| **Habilita** | `SIM-01.1` (recupera facturas que estaban fuera de condiciones) |
| **Pantalla POC** | Confirming → acción **Editar fecha de pago** → modal **Editar fecha de pago** |

#### Historia
Como **aprobador del EGP**
quiero **corregir la fecha de pago de una factura sabiendo de antemano cómo va a afectar su estado**
para **recuperar para el circuito facturas que quedaron fuera de condiciones, o postergar un pago con conocimiento del impacto**.

#### Valor de negocio
Es el único mecanismo que devuelve al circuito una factura `NO ELEGIBLE`. Sin él, cada error de fecha obliga a eliminar y volver a cargar la factura.

#### Escenarios fuente
> `OBJETIVO`: Flujo de Editar Factura
> `ESCENARIOS`: -Escenario modal de confirmación del boton Editar Fecha de Pago de Factura, con los datos de la factura y boton de confirmar (con warning de cantidad de dias para que pase a NO Elegible)

#### Criterios de aceptación
1. **[Feliz]** Al pulsar **Editar fecha de pago** se abre un modal que identifica la factura por número y muestra la fecha de pago actual en `dd-mm-yyyy`.
2. **[Feliz]** El modal muestra un texto de advertencia que explica el umbral de 30 días: `MSG-C23` en facturas operables y `MSG-C22` cuando la factura está en `NO ELEGIBLE`.
3. **[Feliz]** Al guardar una fecha a **30 días o más** de hoy, la fecha se actualiza y se informa `MSG-C29`.
4. **[Feliz]** Si la factura estaba en `NO ELEGIBLE` y la nueva fecha cumple el umbral, la factura pasa a `Habilitada`, la pantalla lleva al usuario a **Facturas Vigentes** y se informa `MSG-C28` (`RN-C01`, T-14).
5. **[Error / validación]** Si la nueva fecha queda a **menos de 30 días** y la factura **no** estaba en `NO ELEGIBLE`, antes de guardar se pide una confirmación explícita que advierte que la factura quedará No Operable (`MSG-C25`); solo si el usuario acepta se aplica el cambio.
6. **[Error / validación]** Al confirmar ese caso, la factura pasa a `NO ELEGIBLE`, la pantalla lleva al usuario a **Facturas No Operables** y se informa `MSG-C26` (T-13).
7. **[Alternativo]** Si la factura ya estaba en `NO ELEGIBLE` y la nueva fecha sigue sin cumplir el umbral, se guarda sin confirmación adicional y se informa `MSG-C27`.
8. **[Error / validación]** Si la fecha está vacía o mal formada, no se guarda nada y se muestra `MSG-C24`.
9. **[Alternativo]** Al cancelar, la fecha de pago original se mantiene.
10. **[Alternativo]** La acción está disponible en los estados definidos por `RN-C14` (ver la divergencia con el Excel en `SPK-C03`).

#### Escenarios BDD
```gherkin
Característica: Edición de la fecha de pago
  Antecedentes:
    Dado que estoy en la pantalla "Confirming"

  Escenario: Recuperar una factura NO ELEGIBLE
    Dado una factura en estado "NO ELEGIBLE" en la pestaña "Facturas No Operables"
    Cuando edito su fecha de pago a 60 días desde hoy
    Y guardo
    Entonces la factura pasa a estado "Habilitada"
    Y la pantalla me lleva a "Facturas Vigentes"
    Y veo el mensaje MSG-C28

  Escenario: Advertencia antes de dejar la factura fuera de condiciones
    Dado una factura en estado "Habilitada"
    Cuando edito su fecha de pago a 10 días desde hoy
    Y guardo
    Entonces veo la confirmación MSG-C25
    Cuando acepto
    Entonces la factura pasa a estado "NO ELEGIBLE"
    Y la pantalla me lleva a "Facturas No Operables"
    Y veo el mensaje MSG-C26

  Escenario: Cancelar la advertencia
    Dado una factura en estado "Habilitada" con fecha de pago a 60 días
    Cuando edito la fecha a 10 días y guardo
    Y cancelo la confirmación
    Entonces la factura conserva su fecha de pago original
    Y sigue en estado "Habilitada"

  Escenario: Fecha inválida
    Cuando dejo la fecha de pago vacía y guardo
    Entonces veo el mensaje MSG-C24
    Y no se modifica la factura
```

#### Fuera de alcance
- Edición del resto de los datos de la factura (número, montos, fechas de emisión y vencimiento) → §11 y permiso «Editar Factura — datos cargados».
- Edición masiva de fechas de pago.

#### Notas / preguntas abiertas
- El Excel pide «warning de **cantidad de días** para que pase a NO Elegible». Los mensajes de la POC nombran el umbral (30 días) pero **no muestran cuántos días faltan** para el caso concreto. Definir si el texto debe incluir el conteo exacto (por ejemplo «faltan 12 días para el umbral»).
- La POC alinea también la fecha de vencimiento cuando el rechazo del EGP cambia la fecha de pago, pero **no** lo hace en esta edición. Confirmar cuál es el comportamiento correcto → `SPK-C16`.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CON-05 — Abrir desde la grilla el modal de aprobación del EGP con los datos bloqueados

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Aprobador del EGP |
| **Dominios** | Todos (acción visible según permiso de aprobación) |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-02`, `SIM-02` (datos del cálculo) |
| **Habilita** | `SIM-05.1`, `SIM-05.2` |
| **Pantalla POC** | Confirming → acción **Aprobar EGP** → modal **Aprobación EGP** |

#### Historia
Como **aprobador del EGP**
quiero **abrir desde la grilla el detalle del adelanto solicitado, con los mismos números de la simulación y sin poder alterarlos**
para **decidir con la información exacta que se le mostró al solicitante**.

#### Valor de negocio
Garantiza que quien aprueba ve el mismo cálculo que se generó al solicitar el adelanto y que no puede modificarlo, lo que da trazabilidad y evita disputas posteriores sobre el importe.

#### Escenarios fuente
> `OBJETIVO`: Flujo de Aprobacion del EGP por el desembolso de una factura
> `ESCENARIOS`: -Escenario modal de confirmación del boton Aprobar EGP, con los datos de la factura y boton de confirmar (misma información que el modal de Simulación, con datos bloqueados) y opciones Aprobar, Rechazar (con o sin motivo)

#### Criterios de aceptación
1. **[Feliz]** La acción **Aprobar EGP** solo está disponible en facturas en estado `Pendiente aprobación EGP` (`CON-02`, AC 3).
2. **[Feliz]** Al pulsarla se abre el modal titulado **Aprobación EGP**, con el subtítulo «Adelanto pendiente de aprobación por el EGP».
3. **[Feliz]** El modal presenta **la misma información que el modal de simulación**: factura, moneda, monto a adelantar, días a adelantar con la fecha de referencia, intereses, comisiones, IVA y monto neto a acreditar (`MSG-C38`, `RN-C09`).
4. **[Feliz]** Los campos **moneda y monto están bloqueados**, con el tooltip que explica el motivo (`MSG-C42`).
5. **[Feliz]** El pie del modal ofrece exactamente tres opciones: **aprobar**, **rechazar con motivo** y **rechazar sin motivo**.
6. **[Alternativo]** El modal muestra la leyenda que anticipa la consecuencia de aprobar (`MSG-C37`, variante de aprobación EGP).
7. **[Alternativo]** Al cerrar o cancelar el modal no se produce ningún cambio de estado y la factura sigue en `Pendiente aprobación EGP`.
8. **[Error / validación]** Si no se puede componer el modal se muestra `MSG-C41` y no se ejecuta ninguna acción.

#### Escenarios BDD
```gherkin
Característica: Modal de aprobación del EGP
  Antecedentes:
    Dado que soy aprobador del EGP
    Y existe una factura en estado "Pendiente aprobación EGP"

  Escenario: Apertura del modal con datos bloqueados
    Cuando pulso "Aprobar EGP" en esa factura
    Entonces se abre el modal "Aprobación EGP"
    Y veo el detalle del cálculo del adelanto
    Y los campos "Moneda" y "Monto a adelantar" están deshabilitados
    Y veo las opciones de aprobar, rechazar con motivo y rechazar sin motivo

  Escenario: Cierre sin decidir
    Dado que abrí el modal "Aprobación EGP"
    Cuando lo cierro sin elegir ninguna opción
    Entonces la factura sigue en estado "Pendiente aprobación EGP"
```

#### Fuera de alcance
- El resultado de aprobar y de rechazar: `SIM-05.1` y `SIM-05.2`.
- La información crediticia del EGP y del Proveedor: `CON-07.1` y `CON-07.2`.

#### Notas / preguntas abiertas
- El Excel pide que el modal muestre «los datos de la factura»; el modal de la POC muestra el cálculo pero **no** las fechas de emisión, vencimiento y pago. Definir si deben incluirse.
- ¿El modal debe mostrar también la información crediticia del EGP (`CON-07.1`) para decidir sin salir de la pantalla? Recomendación del PO: sí, al menos el límite disponible.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CON-07.1 — Ver la información financiera del EGP para decidir el adelanto

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Aprobador del EGP |
| **Dominios** | EGP (`Recurso: EGP \| Dominio: EGP`) |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-08` (GET/obtenerInfoEnte — información financiera) |
| **Habilita** | `CON-07.3`, `SIM-01.4`, `SIM-05.1` |
| **Pantalla POC** | Confirming → cabecera de información del ente |

#### Historia
Como **aprobador del EGP**
quiero **ver la cabecera con la información financiera de mi empresa**
para **aprobar o rechazar adelantos sabiendo con qué límite y con qué condiciones estoy operando**.

#### Valor de negocio
Sin límite y tasas a la vista, la aprobación se hace a ciegas y se aprueban operaciones que después el core rechaza por límite. Es el dato que convierte la aprobación en una decisión informada.

#### Escenarios fuente
> `OBJETIVO`: Mostrar la información crediticia para facilitar al oprobador del EGP, aprobar o rechazar adelantos
> `ESCENARIOS`: -Escenario cabecera de información financiera del EGP: RUC, Razón Social, Limites, Tasas

#### Criterios de aceptación
1. **[Feliz]** La pantalla Confirming presenta una **cabecera de información financiera del EGP** al que pertenecen las facturas que el usuario está gestionando.
2. **[Feliz]** La cabecera muestra, como mínimo: **Razón Social**, **RUC**, **Límite Crediticio**, **Tasa de Interés (TNA)**, **Comisión** e **IVA**, más la indicación de que el ente es un EGP.
3. **[Feliz]** La cabecera muestra las **monedas habilitadas** del EGP.
4. **[Alternativo]** El límite crediticio se muestra formateado como importe; si el EGP no tiene línea asignada se muestra un guion.
5. **[Alternativo]** La misma información está disponible al evaluar un adelanto concreto, tomando el EGP de la factura en cuestión (`CON-05`).
6. **[Alternativo]** Los datos provienen del servicio de entes (`CON-08`) y se refrescan cada vez que se recarga la información del EGP.
7. **[Error / validación]** Si el servicio no responde, la cabecera informa que la información financiera no está disponible en lugar de mostrar valores en cero.

#### Escenarios BDD
```gherkin
Característica: Cabecera de información financiera del EGP
  Antecedentes:
    Dado que soy aprobador del EGP "Retail S.A."
    Y estoy en la pantalla "Confirming"

  Escenario: Información financiera del EGP
    Cuando se carga la pantalla
    Entonces veo la cabecera de información financiera de "Retail S.A."
    Y muestra la razón social, el RUC, el límite crediticio, la TNA, la comisión y el IVA
    Y muestra las monedas habilitadas del EGP

  Escenario: Información no disponible
    Dado que el servicio de entes no responde
    Cuando se carga la pantalla
    Entonces la cabecera informa que la información financiera no está disponible
    Y no muestra importes en cero
```

#### Fuera de alcance
- Información del Proveedor: `CON-07.2`.
- Cálculo del límite disponible descontando lo freezado: `CON-07.3`.

#### Notas / preguntas abiertas
- La POC formatea el límite **siempre en guaraníes**, incluso para EGP que operan en USD. Hay que definir si el límite es único en moneda local o si hay un límite por moneda → `SPK-C17`.
- El Excel habla de «Limites» en plural: confirmar si además del límite global hay límite por operación (el mock de la POC tiene un EGP con la condición «Límite USD 50,000 por operación» como texto libre).

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CON-07.2 — Ver la información financiera del Proveedor de la factura

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Aprobador del EGP |
| **Dominios** | EGP |
| **Prioridad sugerida** | Should |
| **Depende de** | `CON-08` |
| **Habilita** | `SIM-05.1`, `SIM-05.2` |
| **Pantalla POC** | Confirming → cabecera de información del ente *(los datos de créditos activos y morosidad no existen en la POC)* |

#### Historia
Como **aprobador del EGP**
quiero **ver la situación crediticia del Proveedor al que voy a adelantarle fondos**
para **detectar morosidad o sobreendeudamiento antes de aprobar el adelanto**.

#### Valor de negocio
Traslada al momento de la decisión información de riesgo que hoy no está en pantalla. Es el dato que permite rechazar fundadamente un adelanto.

#### Escenarios fuente
> `ESCENARIOS`: -Escenario cabecera de información financiera del Proveedor: RUC, Razón Social, creditos activos, estado de morosidad

#### Criterios de aceptación
1. **[Feliz]** Al evaluar el adelanto de una factura, se muestra la **cabecera de información financiera del Proveedor de esa factura** con **Razón Social**, **RUC**, **créditos activos** y **estado de morosidad**.
2. **[Feliz]** El **estado de morosidad** se muestra de forma destacada y con un indicador visual que permita identificarlo de un vistazo.
3. **[Alternativo]** Los créditos activos se expresan como cantidad y monto total.
4. **[Alternativo]** La información se obtiene del Proveedor de la factura en cuestión, sin que el usuario tenga que cambiar de contexto ni salir de la pantalla.
5. **[Alternativo]** Si el Proveedor no tiene créditos activos, se muestra explícitamente «sin créditos activos» en lugar de un espacio vacío.
6. **[Error / validación]** Si el servicio no devuelve la información de riesgo, la cabecera lo indica y **no** se asume que el proveedor está al día.

#### Escenarios BDD
```gherkin
Característica: Cabecera de información financiera del Proveedor
  Antecedentes:
    Dado que soy aprobador del EGP
    Y estoy en la pantalla "Confirming"

  Escenario: Información del Proveedor de la factura
    Cuando evalúo el adelanto de una factura del proveedor "Tech Solutions S.A."
    Entonces veo su razón social y su RUC
    Y veo la cantidad y el monto de sus créditos activos
    Y veo su estado de morosidad

  Escenario: Proveedor en mora
    Dado que el proveedor "Limpieza Total SRL" está en mora
    Cuando evalúo el adelanto de una de sus facturas
    Entonces el estado de morosidad se muestra destacado
```

#### Fuera de alcance
- Bloqueo automático del adelanto por morosidad (no está pedido en el Excel) → §11.
- Historial de créditos del Proveedor.

#### Notas / preguntas abiertas
- **Gap de POC:** la cabecera actual muestra para el Proveedor los mismos campos que para el EGP (límite, TNA, comisión, IVA) y **no** tiene créditos activos ni morosidad. Hay que definir el origen de esos dos datos (¿CORE? ¿buró?) → `SPK-C18`.
- Definir qué se considera «crédito activo»: solo adelantos del confirming o toda la exposición del cliente con el banco.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ⚠️ depende de `SPK-C18` | ✅ | ✅ | ⚠️ | ✅ | ✅ |

---

### CON-07.3 — Ver el límite de crédito disponible descontando lo freezado

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Aprobador del EGP |
| **Dominios** | EGP |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-08`, `SIM-01.5` (origen del freeze), `SIM-03` (re-cálculo del límite) |
| **Habilita** | `SIM-01.4` |
| **Pantalla POC** | Confirming → cabecera de información del ente *(cálculo no implementado en la POC)* |

#### Historia
Como **aprobador del EGP**
quiero **ver el límite de crédito realmente disponible, ya descontadas las simulaciones en curso**
para **no aprobar adelantos que van a ser rechazados por falta de línea**.

#### Valor de negocio
Un límite «bruto» que ignora las operaciones ya comprometidas produce sobre-aprobaciones y rechazos tardíos del core. Mostrar el disponible real es lo que hace confiable el número de la pantalla.

#### Escenarios fuente
> `OBJETIVO`: Calculo de Limite de credito a mostrar = limite de credito obtenido desde la API - Limite freezado
> `ESCENARIOS`: -Escenario Calculo de Limite de credito a mostrar = limite de credito obtenido desde la API - Limite freezado

#### Criterios de aceptación
1. **[Feliz]** El **límite de crédito a mostrar** se calcula como `límite de crédito devuelto por la API − límite freezado` (`RN-C19`).
2. **[Feliz]** La cabecera muestra los tres valores de forma diferenciada: **límite total**, **freezado** y **disponible**, de modo que el usuario entienda de dónde sale el número.
3. **[Alternativo]** El disponible se recalcula y se refresca **inmediatamente después** de crear una simulación de adelanto (`SIM-01.5`) y después de que el core resuelva la operación (`SIM-03`).
4. **[Alternativo]** Si el disponible llega a cero o queda por debajo de un umbral configurable, se muestra un indicador de alerta.
5. **[Error / validación]** El disponible nunca se muestra negativo: si el freezado supera al límite se muestra cero y se marca la inconsistencia para revisión.
6. **[Error / validación]** Si la API no devuelve el límite freezado, se muestra el límite total marcado como «sin descontar operaciones en curso» y **no** se presenta ese valor como disponible.

#### Escenarios BDD
```gherkin
Característica: Límite de crédito disponible del EGP
  Antecedentes:
    Dado que soy aprobador del EGP "Retail S.A."

  Escenario: Cálculo del disponible
    Dado que la API informa un límite de crédito de 500.000.000 GS
    Y hay 120.000.000 GS freezados por simulaciones en curso
    Cuando se muestra la información financiera del EGP
    Entonces el límite disponible es 380.000.000 GS
    Y se muestran también el límite total y el importe freezado

  Escenario: Actualización tras una simulación
    Dado que el límite disponible es 380.000.000 GS
    Cuando se confirma una simulación de adelanto por 80.000.000 GS
    Entonces el límite disponible pasa a 300.000.000 GS

  Escenario: Sin información de freeze
    Dado que la API no informa el límite freezado
    Cuando se muestra la información financiera del EGP
    Entonces el importe se presenta como límite total sin descontar operaciones en curso
```

#### Fuera de alcance
- La mecánica de freeze en sí (`SIM-01.5`) y su liberación (`SIM-03`).
- Límite por operación o por proveedor.

#### Notas / preguntas abiertas
- **Gap de POC:** hoy el panel muestra el límite estático del ente; no existe el concepto de freezado. Todo este cálculo es desarrollo nuevo.
- Definir **cuándo se libera** el freeze: al rechazar el EGP, al vencer el plazo de `RN-C22`, al fallar el core (`RN-C12`) y al eliminar la factura → `SPK-C19`.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ⚠️ acoplada a `SIM-01.5` | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CON-11.1 — Habilitar varias facturas en una sola acción

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador del EGP, Operador del Banco |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-01.1`, `CON-06`, `CON-09.1` |
| **Habilita** | `SIM-01.1`, `SIM-01.2`, `SIM-01.3` |
| **Pantalla POC** | Confirming → botón global **Habilitar** |

#### Historia
Como **operador del EGP**
quiero **habilitar de una sola vez todas las facturas que seleccioné**
para **dejar operable el lote del período sin repetir la misma acción factura por factura**.

#### Valor de negocio
La habilitación es el paso previo obligatorio a cualquier adelanto. Hacerla en lote es lo que vuelve viable operar carteras grandes.

#### Escenarios fuente
> `OBJETIVO`: Botonera global de la pantalla: botón habilitar / bloquear
> `ESCENARIOS`: -Escenario Habiliar Factura: cambio de estado de multiples facturas en estados válidos para la transicion (pendiente/bloqueado)

#### Criterios de aceptación
1. **[Feliz]** La barra de acciones ofrece el botón **Habilitar**, deshabilitado mientras la selección no sea válida.
2. **[Feliz]** El botón se habilita cuando hay **al menos una** factura seleccionada y **todas** las seleccionadas están en `Pendiente` o `Bloqueada` (`RN-C04`).
3. **[Feliz]** Al pulsarlo se pide confirmación identificando las facturas afectadas: el número si es una, o la cantidad con hasta cinco números y el resto resumido (`MSG-C31`).
4. **[Feliz]** Al confirmar, todas las facturas seleccionadas pasan a `Habilitada`, la selección se limpia, la grilla se refresca y se informa el resultado con el mensaje singular o plural correspondiente (`MSG-C32`).
5. **[Error / validación]** Si la selección incluye alguna factura en un estado no válido, el botón queda deshabilitado y el tooltip explica el motivo (`MSG-C30`).
6. **[Error / validación]** Sin selección, el tooltip indica qué hay que seleccionar (`MSG-C30`).
7. **[Alternativo]** Al cancelar la confirmación no se modifica ninguna factura y la selección se conserva.
8. **[Alternativo]** La cabecera de la grilla permite seleccionar y deseleccionar todas las facturas visibles, respetando la combinatoria ancla (`RN-C08`).

#### Escenarios BDD
```gherkin
Característica: Habilitación masiva de facturas
  Antecedentes:
    Dado que estoy en la pantalla "Confirming"
    Y la pestaña activa es "Facturas Vigentes"

  Escenario: Habilitar tres facturas pendientes
    Cuando selecciono tres facturas en estado "Pendiente"
    Entonces el botón "Habilitar" se activa
    Cuando lo pulso y confirmo
    Entonces las tres facturas quedan en estado "Habilitada"
    Y veo el mensaje MSG-C32 en su variante plural
    Y la selección queda vacía

  Escenario: Selección con una factura en estado inválido
    Cuando selecciono una factura "Pendiente" y otra "Financiada"
    Entonces el botón "Habilitar" permanece deshabilitado
    Y su tooltip indica que solo pueden habilitarse facturas en estado Bloqueada o Pendiente

  Escenario: Cancelar la confirmación
    Dado que seleccioné dos facturas "Bloqueada"
    Cuando pulso "Habilitar" y cancelo
    Entonces las facturas siguen en estado "Bloqueada"
```

#### Fuera de alcance
- Bloquear: `CON-11.2`.
- Habilitación automática por reglas de negocio.

#### Notas / preguntas abiertas
- Confirmar si debe existir habilitación **individual** desde la fila. Hoy tanto el Excel como la POC resuelven habilitar y bloquear solo desde la botonera global, y la fila `Pendiente` muestra el indicador «Use Habilitar / Bloquear».

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CON-11.2 — Bloquear varias facturas en una sola acción

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador del EGP, Operador del Banco |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-01.1`, `CON-06`, `CON-09.1` |
| **Habilita** | — |
| **Pantalla POC** | Confirming → botón global **Bloquear** |

#### Historia
Como **operador del EGP**
quiero **bloquear de una sola vez todas las facturas que seleccioné**
para **sacar rápido del circuito operable las facturas observadas o en disputa**.

#### Valor de negocio
Es el mecanismo de contención: permite frenar en bloque facturas con problemas antes de que alguien solicite un adelanto sobre ellas.

#### Escenarios fuente
> `ESCENARIOS`: -Escenario Bloquear Factura: cambio de estado de multiples facturas en estados válidos para la transicion (pendiente/habilitado/pendiente de aprobacion de EGP)

#### Criterios de aceptación
1. **[Feliz]** La barra de acciones ofrece el botón **Bloquear**, deshabilitado mientras la selección no sea válida.
2. **[Feliz]** El botón se habilita cuando hay al menos una factura seleccionada y **todas** están en un estado válido de origen (`RN-C05`).
3. **[Feliz]** Al pulsarlo se pide confirmación identificando las facturas afectadas (`MSG-C34`).
4. **[Feliz]** Al confirmar, todas pasan a `Bloqueada`, la selección se limpia, la grilla se refresca y se informa `MSG-C35`.
5. **[Error / validación]** Con selección inválida o vacía, el botón queda deshabilitado y el tooltip explica el motivo (`MSG-C33`).
6. **[Alternativo]** Al cancelar la confirmación no se modifica ninguna factura.
7. **[Alternativo]** Una factura bloqueada puede volver a `Habilitada` mediante `CON-11.1` (T-04).

#### Escenarios BDD
```gherkin
Característica: Bloqueo masivo de facturas
  Antecedentes:
    Dado que estoy en la pantalla "Confirming"

  Escenario: Bloquear facturas habilitadas
    Cuando selecciono dos facturas en estado "Habilitada"
    Y pulso "Bloquear" y confirmo
    Entonces ambas quedan en estado "Bloqueada"
    Y veo el mensaje MSG-C35 en su variante plural

  Escenario: Selección inválida
    Cuando selecciono una factura en estado "Financiada"
    Entonces el botón "Bloquear" permanece deshabilitado
    Y su tooltip explica los estados válidos

  Escenario: Reversión del bloqueo
    Dado una factura en estado "Bloqueada"
    Cuando la selecciono y pulso "Habilitar" y confirmo
    Entonces la factura vuelve a estado "Habilitada"
```

#### Fuera de alcance
- Motivo de bloqueo y su registro (no está pedido en el Excel) → §11.
- Bloqueo automático por reglas de riesgo.

#### Notas / preguntas abiertas
- **Divergencia con la POC:** el Excel admite bloquear también desde `Pendiente de aprobación EGP`; la POC solo admite `Pendiente` y `Habilitada` (`RN-C05`). Si se acepta el origen adicional hay que definir qué pasa con la solicitud de adelanto ya enviada al EGP y con el eventual freeze de límite → `SPK-C02`.
- Recomendación del PO: registrar **motivo de bloqueo**, porque hoy la factura queda bloqueada sin explicación para el resto de los usuarios.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### 7.3 Grupo SIM — Simulación y adelanto de facturas

### SIM-01.1 — Simular el adelanto de una factura individual

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Usuario Proveedor (también Operador del EGP y del Banco) |
| **Dominios** | Todos (`Recurso: todos \| dominio: todos`) |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-11.1` (la factura debe estar `Habilitada`), `SIM-02`, `SIM-03` |
| **Habilita** | `CON-05`, `SIM-05.1`, `SIM-05.2` |
| **Pantalla POC** | Confirming → acción **Simular** de la fila → modal **Simulación de Adelanto** |

#### Historia
Como **usuario Proveedor**
quiero **ver cuánto voy a cobrar si adelanto una factura habilitada y poder solicitar ese adelanto**
para **decidir con el número neto a la vista y disparar la solicitud en el mismo paso**.

#### Valor de negocio
Es el corazón del producto: el momento en que el proveedor ve el beneficio concreto del confirming. La transparencia del desglose (intereses, comisiones, IVA) es lo que sostiene la adopción.

#### Escenarios fuente
> `OBJETIVO`: Botonera global de la pantalla: botón simular
> `ESCENARIOS`: -Escenario Simular Adelanto de factura individual: abrir modal de Simulación de Adelanto para la factura seleccionada en un estado valido (Habilitada), con los calculo individual, genera la solicitud de un prestamo en 1 cuota
> `**Para todos los calculos en el modal de simulacion siempre debera figurar "los valores simulados son estimativos... " o algo por el estilo`

#### Criterios de aceptación
1. **[Feliz]** La acción **Simular** solo se ofrece en facturas en estado `Habilitada` (`RN-C06`).
2. **[Feliz]** Al pulsarla se abre el modal **Simulación de Adelanto** con la moneda de la factura y el monto a adelantar precargado con el monto de la factura.
3. **[Feliz]** El ticket de cálculo muestra: factura de origen con EGP y Proveedor, **días a adelantar** con su fecha de referencia, **intereses a descontar** con la TNA aplicada, **comisiones operativas** con su porcentaje, **I.V.A.** con su porcentaje y **Monto Neto a Acreditar** (`MSG-C38`, `RN-C09`).
4. **[Feliz]** El cálculo se recalcula en vivo al modificar el monto a adelantar.
5. **[Error / validación]** El monto a adelantar no puede superar el monto de la factura: si se excede, se ajusta al máximo permitido (`RN-C10`).
6. **[Feliz]** El modal muestra de forma **permanente y visible** la leyenda de que los valores son estimativos (`MSG-C43`, `RN-C24`).
7. **[Feliz]** Al ejecutar el adelanto se pide confirmación con el monto neto estimado y el estado destino (`MSG-C39`); al aceptar, la factura pasa a `Pendiente aprobación EGP`, se cierra el modal, se refresca la grilla y se informa `MSG-C40` (T-06).
8. **[Feliz]** La solicitud generada corresponde a **un préstamo en una sola cuota**.
9. **[Alternativo]** La moneda es de solo lectura salvo que el EGP opere en varias monedas, en cuyo caso puede elegirse entre las habilitadas (`MSG-C42`).
10. **[Alternativo]** Al cancelar el modal no se genera ninguna solicitud y la factura sigue `Habilitada`.
11. **[Error / validación]** Si el cálculo no puede obtenerse, se informa el error (`MSG-C41` o el error devuelto por `SIM-02`) y no se habilita la ejecución.

#### Escenarios BDD
```gherkin
Característica: Simulación individual de adelanto
  Antecedentes:
    Dado que estoy en la pantalla "Confirming"
    Y existe la factura "001-001-0002001" en estado "Habilitada"

  Escenario: Simular y solicitar el adelanto
    Cuando pulso "Simular" en esa factura
    Entonces se abre el modal "Simulación de Adelanto"
    Y veo los días a adelantar, los intereses, las comisiones, el IVA y el monto neto a acreditar
    Y veo la leyenda de que los valores son estimativos
    Cuando pulso "Ejecutar Adelanto"
    Y confirmo
    Entonces la factura pasa a estado "Pendiente aprobación EGP"
    Y veo el mensaje MSG-C40

  Escenario: El monto a adelantar no puede superar la factura
    Dado que abrí la simulación de una factura de 15.000.000 GS
    Cuando ingreso un monto a adelantar de 20.000.000 GS
    Entonces el monto se ajusta a 15.000.000 GS
    Y el cálculo se recalcula con ese importe

  Escenario: Cancelar la simulación
    Dado que abrí el modal de simulación
    Cuando lo cierro sin ejecutar
    Entonces la factura sigue en estado "Habilitada"
```

#### Fuera de alcance
- Simulación de más de una factura: `SIM-01.2` y `SIM-01.3`.
- Validación de límite de crédito: `SIM-01.4`.
- Freeze del límite: `SIM-01.5`.

#### Notas / preguntas abiertas
- **Gap de POC:** la leyenda de valores estimativos que exige el Excel **no existe** en la POC. Hay que redactar y aprobar `MSG-C43` antes del desarrollo.
- La POC calcula los días a adelantar contra la **fecha de vencimiento**, mientras que el criterio de elegibilidad (`RN-C01`) usa la **fecha de pago**. Hay que definir cuál es la fecha correcta para el devengamiento → `SPK-C20`.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### SIM-01.2 — Simular el adelanto de varias facturas con la misma fecha de pago

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Usuario Proveedor |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `SIM-01.1`, `CON-01.2`, `SIM-02`, `SIM-03` |
| **Habilita** | `SIM-05.1` |
| **Pantalla POC** | Confirming → selección múltiple + botón global **Simular** → modal **Simulación de Adelanto (masiva)** |

#### Historia
Como **usuario Proveedor**
quiero **adelantar en una sola operación varias facturas que vencen el mismo día**
para **obtener un único préstamo en una cuota en vez de gestionar una operación por factura**.

#### Valor de negocio
Reduce la cantidad de operaciones de crédito a generar y a administrar, tanto para el proveedor como para el banco, y da un neto agregado que es el que realmente se acredita.

#### Escenarios fuente
> `ESCENARIOS`: -Escenario Simular Adelanto de múltiples factura-misma fecha de pago: abrir modal de Simulación de Adelanto para multiples facturas en estados válidos (Habilitada), con los calculos unificados, VALIDACION: si múltiples facturas correspondan a mismo EGP-Proveedor Y misma moneda, entonces permite simular multiple y genera la solicitud de un mismo prestamo en 1 cuota, sino error

#### Criterios de aceptación
1. **[Feliz]** Con **dos o más** facturas seleccionadas, todas en `Habilitada` y con **mismo EGP, mismo Proveedor y misma moneda**, el botón global **Simular** se habilita (`RN-C07`).
2. **[Feliz]** Al pulsarlo se abre el modal **Simulación de Adelanto (masiva)**, con el subtítulo que indica la cantidad de facturas incluidas.
3. **[Feliz]** El monto a adelantar es la **suma de los montos** de las facturas seleccionadas y es de **solo lectura** (`RN-C10`).
4. **[Feliz]** El ticket muestra el cálculo unificado (intereses, comisiones, IVA y neto) sobre el monto agregado (`RN-C09`) y la leyenda de valores estimativos (`MSG-C43`).
5. **[Feliz]** Cuando todas las facturas tienen la **misma fecha de pago**, la solicitud generada corresponde a **un único préstamo en una cuota**.
6. **[Feliz]** Al ejecutar y confirmar (`MSG-C39` en variante masiva), **todas** las facturas seleccionadas pasan a `Pendiente aprobación EGP`, la selección se limpia y se informa `MSG-C40` en variante masiva.
7. **[Error / validación]** Si las facturas seleccionadas no comparten EGP, Proveedor y moneda, la acción **no** se habilita y el tooltip lo explica (`MSG-C36`).
8. **[Error / validación]** Si alguna de las facturas seleccionadas no está en `Habilitada`, la acción no se habilita.
9. **[Alternativo]** Al haber una selección múltiple válida, la acción **Simular** de cada fila se deshabilita y se indica que debe usarse la de la cabecera.
10. **[Alternativo]** La primera factura tildada fija la combinatoria: las facturas que no coinciden quedan con la casilla deshabilitada y el tooltip `MSG-C18` (`RN-C08`).

#### Escenarios BDD
```gherkin
Característica: Simulación múltiple con misma fecha de pago
  Antecedentes:
    Dado que estoy en la pantalla "Confirming"
    Y existen tres facturas "Habilitada" del mismo EGP, mismo proveedor y misma moneda, con igual fecha de pago

  Escenario: Simulación agregada de tres facturas
    Cuando selecciono las tres facturas
    Entonces el botón "Simular" se activa
    Cuando lo pulso
    Entonces se abre el modal "Simulación de Adelanto (masiva)" indicando 3 facturas
    Y el monto a adelantar es la suma de las tres y no es editable
    Cuando ejecuto el adelanto y confirmo
    Entonces las tres facturas pasan a "Pendiente aprobación EGP"
    Y se genera una única solicitud de préstamo en una cuota

  Escenario: Combinatoria inválida
    Cuando selecciono dos facturas de proveedores distintos
    Entonces el botón "Simular" permanece deshabilitado
    Y su tooltip indica que deben compartir EGP, Proveedor y Moneda

  Escenario: Bloqueo de la selección por combinatoria
    Dado que tildé una factura del EGP "Retail S.A." en moneda "GS"
    Cuando observo una factura del mismo EGP en moneda "USD"
    Entonces su casilla está deshabilitada
    Y su tooltip es MSG-C18
```

#### Fuera de alcance
- Facturas con fechas de pago distintas: `SIM-01.3`.
- Validación de límite: `SIM-01.4`.

#### Notas / preguntas abiertas
- La POC no distingue entre selección con la misma fecha de pago y con fechas distintas: siempre genera una operación agregada. La distinción en cuotas que pide el Excel es desarrollo nuevo (ver `SIM-01.3`).
- El ticket agregado no desglosa por factura. Recomendación del PO: incluir el detalle por factura dentro del modal para que el proveedor pueda auditar el neto.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### SIM-01.3 — Simular el adelanto de varias facturas con fechas de pago distintas

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Usuario Proveedor |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `SIM-01.2`, `SIM-02`, `SIM-03` |
| **Habilita** | `SIM-05.1` |
| **Pantalla POC** | Confirming → selección múltiple + botón global **Simular** *(el fraccionamiento en cuotas no está implementado en la POC)* |

#### Historia
Como **usuario Proveedor**
quiero **adelantar en una sola operación facturas que vencen en fechas distintas y que el préstamo se arme en cuotas según esas fechas**
para **agrupar mi financiamiento en una sola operación sin perder la correspondencia entre cada factura y su vencimiento**.

#### Valor de negocio
Permite consolidar el financiamiento del proveedor en una sola operación de crédito respetando el calendario real de cobros del EGP, que es lo que determina la devolución.

#### Escenarios fuente
> `ESCENARIOS`: -Escenario Simular Adelanto de múltiples factura-fecha de pago distinta: abrir modal de Simulación de Adelanto para multiples facturas en estados válidos (Habilitada), con los calculos unificados, VALIDACION: si múltiples facturas correspondan a mismo EGP-Proveedor Y misma moneda, entonces permite simular multiple y genera la solicitud de un mismo prestamo en n cuotas segun fecha de pago, sino error

#### Criterios de aceptación
1. **[Feliz]** Con dos o más facturas `Habilitada` del mismo EGP, Proveedor y moneda pero con **fechas de pago distintas**, el botón **Simular** se habilita igual que en `SIM-01.2` (`RN-C07`).
2. **[Feliz]** La solicitud generada corresponde a **un único préstamo en n cuotas**, donde **n es la cantidad de fechas de pago distintas** presentes en la selección.
3. **[Feliz]** Cada cuota queda asociada a su fecha de pago y a las facturas que comparten esa fecha.
4. **[Feliz]** El modal muestra el **cuadro de cuotas**: fecha de cada cuota, facturas incluidas e importe, además del cálculo unificado y del neto total.
5. **[Feliz]** Los intereses se calculan según los **días a adelantar de cada cuota**, no con un plazo único para toda la operación (`RN-C09`).
6. **[Feliz]** El modal muestra la leyenda de valores estimativos (`MSG-C43`).
7. **[Feliz]** Al ejecutar y confirmar, todas las facturas pasan a `Pendiente aprobación EGP` y se genera una única solicitud con su plan de cuotas.
8. **[Error / validación]** Si la combinatoria EGP + Proveedor + moneda no se cumple, la acción no se habilita (`MSG-C36`).
9. **[Alternativo]** Si todas las fechas de pago coinciden, la operación se resuelve en una sola cuota y el comportamiento es el de `SIM-01.2`.

#### Escenarios BDD
```gherkin
Característica: Simulación múltiple con fechas de pago distintas
  Antecedentes:
    Dado que estoy en la pantalla "Confirming"
    Y existen cuatro facturas "Habilitada" del mismo EGP, proveedor y moneda

  Escenario: Préstamo en tres cuotas
    Dado que dos facturas tienen fecha de pago "30-10-2026" y las otras dos "30-11-2026" y "30-12-2026"
    Cuando las selecciono y pulso "Simular"
    Entonces el modal muestra un plan de 3 cuotas
    Y cada cuota indica su fecha, las facturas incluidas y su importe
    Cuando ejecuto el adelanto y confirmo
    Entonces las cuatro facturas pasan a "Pendiente aprobación EGP"
    Y se genera una única solicitud de préstamo con 3 cuotas

  Escenario: Intereses por plazo de cada cuota
    Dado un plan con cuotas a 30 y a 90 días
    Cuando se calcula el ticket
    Entonces los intereses de cada cuota se calculan con los días que le corresponden

  Escenario: Todas las fechas iguales
    Dado que las cuatro facturas tienen la misma fecha de pago
    Cuando las selecciono y pulso "Simular"
    Entonces el plan resultante tiene una sola cuota
```

#### Fuera de alcance
- Que el usuario elija manualmente el armado de cuotas.
- Refinanciación o reprogramación de cuotas.

#### Notas / preguntas abiertas
- **Gap de POC:** la POC genera siempre una operación agregada, sin cuotas y calculando los días con el vencimiento de la primera factura de la selección. Todo el fraccionamiento es desarrollo nuevo.
- Definir si las cuotas se arman por **fecha de pago** o por **fecha de vencimiento** — se relaciona con `SPK-C20`.
- Definir el tope de cuotas admitido por el core → `SPK-C21`.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ⚠️ acoplada a `SIM-01.2` | ✅ | ✅ | ⚠️ depende de `SPK-C21` | ✅ | ✅ |

---

### SIM-01.4 — Impedir simular facturas que excedan el límite de crédito del EGP

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Usuario Proveedor, Aprobador del EGP |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-07.3`, `CON-08`, `SIM-02` |
| **Habilita** | `SIM-01.5` |
| **Pantalla POC** | Confirming → grilla y modal de simulación *(no implementado en la POC)* |

#### Historia
Como **usuario Proveedor**
quiero **que el portal me impida seleccionar para adelanto facturas que superan el límite disponible del EGP**
para **no perder tiempo en solicitudes que van a ser rechazadas más adelante**.

#### Valor de negocio
Evita el rechazo tardío (después de la aprobación del EGP o ya en el core), que es el que genera reclamos y retrabajo. Traslada el control de límite al momento de la selección.

#### Escenarios fuente
> `ESCENARIOS`: -Escenario VALIDACION que el EGP tenga limite suficiente para realizar el adelanto (se grisan/bloquean las facturas que excedan del limite de credito del cEGP)

#### Criterios de aceptación
1. **[Feliz]** Al abrir la pantalla, el sistema conoce el **límite disponible** del EGP (`CON-07.3`, `RN-C19`).
2. **[Feliz]** Las facturas cuyo monto **excede** el límite disponible del EGP se muestran **deshabilitadas para la selección** (grisadas) y con un tooltip que explica el motivo (`MSG-C44`).
3. **[Feliz]** En selección múltiple, la validación se aplica sobre el **acumulado** de la selección: al alcanzar el límite disponible, el resto de las facturas del mismo EGP queda deshabilitado.
4. **[Feliz]** El modal de simulación muestra el límite disponible del EGP y el importe que la operación consumiría.
5. **[Error / validación]** Si aun así se intenta ejecutar un adelanto que excede el disponible, la ejecución se rechaza con `MSG-C44` y la factura no cambia de estado.
6. **[Alternativo]** Al liberarse límite (por resolución de otra operación), las facturas antes grisadas vuelven a estar disponibles tras refrescar la grilla.
7. **[Error / validación]** Si no se puede obtener el límite disponible, la simulación queda bloqueada con un mensaje explícito; **no** se permite operar asumiendo límite infinito.

#### Escenarios BDD
```gherkin
Característica: Validación de límite de crédito del EGP
  Antecedentes:
    Dado que el EGP "Retail S.A." tiene un límite disponible de 20.000.000 GS

  Escenario: Factura que excede el límite
    Dado una factura "Habilitada" de ese EGP por 50.000.000 GS
    Cuando observo la grilla
    Entonces la casilla de selección de esa factura está deshabilitada
    Y su tooltip indica que excede el límite de crédito del EGP

  Escenario: Límite acumulado en selección múltiple
    Dado tres facturas "Habilitada" de ese EGP por 8.000.000 GS cada una
    Cuando selecciono las dos primeras
    Entonces la tercera queda deshabilitada porque el acumulado supera el disponible

  Escenario: Sin información de límite
    Dado que el servicio de límites no responde
    Cuando intento simular
    Entonces la simulación queda bloqueada con un mensaje explícito
```

#### Fuera de alcance
- El freeze del límite al confirmar: `SIM-01.5`.
- Ampliación o gestión de la línea de crédito (pertenece al ABM del ente).

#### Notas / preguntas abiertas
- **Gap de POC:** la POC no valida límite en ningún punto del flujo.
- Definir si el control es solo del EGP o también hay un tope por Proveedor (supuesto S-06).
- Definir el comportamiento con facturas en **USD** contra un límite expresado en guaraníes → `SPK-C17`.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ⚠️ depende de `CON-07.3` | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### SIM-01.5 — Freezar el límite de crédito al confirmar la simulación

| | |
|---|---|
| **Tipo** | HU-FE + HU-BE |
| **Épica** | CONFIRMING |
| **Actor** | Usuario Proveedor (efecto observado por el Aprobador del EGP) |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `SIM-01.4`, `SIM-03`, `CON-07.3` |
| **Habilita** | `CON-07.3` (el disponible que muestra el panel) |
| **Pantalla POC** | Confirming → modal de simulación → confirmación *(no implementado en la POC)* |

#### Historia
Como **aprobador del EGP**
quiero **que al confirmarse una simulación se reserve el importe correspondiente de mi línea de crédito**
para **que dos solicitudes simultáneas no consuman dos veces el mismo límite disponible**.

#### Valor de negocio
Es el control que evita la sobre-utilización de la línea. Sin freeze, varias solicitudes concurrentes pueden aprobarse contra el mismo saldo y el core termina rechazando operaciones ya comprometidas con el proveedor.

#### Escenarios fuente
> `ESCENARIOS`: -Escenario de CONFIRMACIÓN, al crearse una simulación se freeza el limite de credito correspondiente y se descuenta del limite crediticio total del EGP

#### Criterios de aceptación
1. **[Feliz]** Al confirmarse la ejecución del adelanto (individual o múltiple), el importe de la operación se **freeza** contra la línea del EGP y se descuenta del límite disponible (`RN-C19`).
2. **[Feliz]** La cabecera de información financiera del EGP refleja el nuevo disponible inmediatamente después de la confirmación (`CON-07.3`).
3. **[Feliz]** El freeze queda asociado a la solicitud de adelanto y es trazable: importe, moneda, facturas incluidas, usuario, fecha y hora.
4. **[Alternativo]** Si el EGP **rechaza** la solicitud (con o sin motivo), el importe freezado se **libera** y vuelve al disponible.
5. **[Alternativo]** Si CORE BANKING devuelve error y la factura vuelve a `Pendiente aprobación EGP` (`RN-C12`), el freeze **se mantiene** hasta que la operación se resuelva o expire.
6. **[Alternativo]** Al concretarse el desembolso (`Financiada`), el freeze se convierte en utilización efectiva de la línea.
7. **[Error / validación]** Si al confirmar el disponible ya no alcanza (porque otra operación consumió el saldo entre la simulación y la confirmación), la operación se rechaza con `MSG-C44` y no se genera solicitud ni freeze.
8. **[Error / validación]** El freeze es **atómico** con la creación de la solicitud: no puede quedar solicitud sin freeze ni freeze sin solicitud.

#### Escenarios BDD
```gherkin
Característica: Freeze del límite de crédito al confirmar la simulación
  Antecedentes:
    Dado que el EGP "Retail S.A." tiene un límite disponible de 100.000.000 GS

  Escenario: Freeze al confirmar
    Cuando confirmo un adelanto por 30.000.000 GS
    Entonces se freezan 30.000.000 GS de la línea del EGP
    Y el límite disponible pasa a 70.000.000 GS

  Escenario: Liberación por rechazo del EGP
    Dado un adelanto confirmado por 30.000.000 GS con su límite freezado
    Cuando el EGP rechaza la solicitud
    Entonces los 30.000.000 GS se liberan
    Y el límite disponible vuelve a 100.000.000 GS

  Escenario: Concurrencia sobre el mismo saldo
    Dado que el disponible es 30.000.000 GS
    Y otra operación consumió el saldo antes de mi confirmación
    Cuando confirmo mi adelanto por 30.000.000 GS
    Entonces la operación se rechaza con MSG-C44
    Y no se genera solicitud ni freeze
```

#### Fuera de alcance
- Reglas de expiración del freeze en el tiempo (se relaciona con `RN-C22` y `SIM-02`).
- Gestión de la línea de crédito en el ABM del ente.

#### Notas / preguntas abiertas
- **Gap de POC:** no existe ningún mecanismo de freeze en la POC.
- Definir el **evento exacto de freeze**: ¿al ejecutar el adelanto (paso a `Pendiente aprobación EGP`) o recién al aprobar el EGP? El Excel dice «al crearse una simulación», lo que apunta al primer caso; se adopta ese criterio y se marca `SPK-C19` para confirmarlo junto con las reglas de liberación.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ⚠️ acoplada a `SIM-03` | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### SIM-05.1 — Aprobar como EGP la solicitud de adelanto

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Aprobador del EGP |
| **Dominios** | Todos (`Recurso: todos \| dominio: todos`) |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-05`, `CON-06`, `SIM-03`, `SIM-04` |
| **Habilita** | Desembolso por CORE BANKING (`CON-09.1`, T-11 y T-12) |
| **Pantalla POC** | Confirming → modal **Aprobación EGP** → **EGP Aprueba** |

#### Historia
Como **aprobador del EGP**
quiero **aprobar la solicitud de adelanto que hizo el proveedor**
para **habilitar el desembolso y que el proveedor cobre anticipadamente su factura**.

#### Valor de negocio
Es el punto de control del EGP sobre su propia deuda: sin su aprobación no hay desembolso. Es también el disparador de todo el tramo automático (aprobación bancaria y core).

#### Escenarios fuente
> `OBJETIVO`: Flujos de Aprobación y Rechazos de simulación de adelanto por parte del usuario aprobador EGP
> `ESCENARIOS`: -Escenario de Aprobación del adelanto por parte del EGP para avanzar con el desembolso solicitado por el usuario Proveedor

#### Criterios de aceptación
1. **[Feliz]** En el modal de aprobación (`CON-05`), la opción de aprobar está disponible únicamente para facturas en `Pendiente aprobación EGP`.
2. **[Feliz]** El modal anticipa la consecuencia de aprobar: la aprobación bancaria es automática y la factura pasa a `Pendiente de desembolso` (`MSG-C37`).
3. **[Feliz]** Al aprobar, la factura pasa a `Pendiente de desembolso` (T-07), el modal se cierra, la grilla se refresca y se informa `MSG-C48`.
4. **[Feliz]** La fila de la factura muestra el indicador de desembolso en curso mientras el core procesa (`CON-02`, AC 4).
5. **[Feliz]** Al resolver CORE BANKING: si el desembolso se concreta, la factura pasa a `Financiada` y se informa `MSG-C54`; si devuelve error, la factura vuelve a `Pendiente aprobación EGP` y se informa `MSG-C53` (`RN-C12`, T-11 y T-12).
6. **[Alternativo]** Al aprobar se dispara la notificación al EGP y al Proveedor (`SIM-04`).
7. **[Alternativo]** En una solicitud múltiple, la aprobación aplica a **todas** las facturas que integran la operación.
8. **[Error / validación]** Si la factura cambió de estado mientras el modal estaba abierto, la aprobación se rechaza informando la situación y la grilla se refresca.

#### Escenarios BDD
```gherkin
Característica: Aprobación del adelanto por el EGP
  Antecedentes:
    Dado que soy aprobador del EGP
    Y la factura "001-001-0004001" está en estado "Pendiente aprobación EGP"

  Escenario: Aprobación con desembolso exitoso
    Cuando abro el modal "Aprobación EGP" y apruebo
    Entonces veo el mensaje MSG-C48
    Y la factura pasa a estado "Pendiente de desembolso"
    Y su fila muestra el indicador de desembolso en curso
    Cuando CORE BANKING confirma el desembolso
    Entonces la factura pasa a estado "Financiada"
    Y veo el mensaje MSG-C54

  Escenario: Aprobación con error del core
    Cuando apruebo el adelanto
    Y CORE BANKING devuelve error
    Entonces veo el mensaje MSG-C53
    Y la factura vuelve a estado "Pendiente aprobación EGP"

  Escenario: Aprobación de una solicitud múltiple
    Dado un adelanto que agrupa tres facturas
    Cuando lo apruebo
    Entonces las tres facturas pasan a "Pendiente de desembolso"
```

#### Fuera de alcance
- El rechazo: `SIM-05.2`.
- La aprobación bancaria manual (hoy es automática, supuesto S-05).

#### Notas / preguntas abiertas
- En la POC la aprobación del EGP se ejecuta **sin confirmación adicional**: el cambio de estado es inmediato al pulsar. Al ser una acción con impacto financiero, la recomendación del PO es pedir confirmación explícita.
- La POC aplica la aprobación **solo a la factura desde la que se abrió el modal**, incluso si el adelanto agrupó varias. El AC 7 corrige ese comportamiento y debe validarse → `SPK-C22`.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### SIM-05.2 — Rechazar como EGP la solicitud de adelanto, con o sin motivo

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Aprobador del EGP |
| **Dominios** | Todos |
| **Prioridad sugerida** | Must |
| **Depende de** | `CON-05`, `CON-06`, `CON-09.3` |
| **Habilita** | `CON-04` (corrección posterior), `CON-11.1` (rehabilitación) |
| **Pantalla POC** | Confirming → modal **Aprobación EGP** → **Rechazar c/ motivo** / **Rechazar s/ motivo** |

#### Historia
Como **aprobador del EGP**
quiero **rechazar una solicitud de adelanto, informando o no un motivo**
para **frenar operaciones que no corresponden y, cuando aplique, dejar la factura corregida para un nuevo intento**.

#### Valor de negocio
Cierra el circuito de control del EGP. El rechazo con motivo permite corregir la fecha de pago en el mismo acto y recuperar la factura, en lugar de descartarla.

#### Escenarios fuente
> `ESCENARIOS`: -Escenario de Rechazo del adelanto por parte del EGP para avanzar con el desembolso solicitado por el usuario Proveedor, con o sin motivo.

#### Criterios de aceptación
1. **[Feliz]** El modal de aprobación ofrece dos opciones de rechazo diferenciadas: **rechazar con motivo** y **rechazar sin motivo**.
2. **[Feliz — sin motivo]** Al rechazar sin motivo, la factura pasa a `Bloqueada` (T-10), el modal se cierra, la grilla se refresca y se informa `MSG-C52`.
3. **[Feliz — con motivo]** Al rechazar con motivo se solicita la **nueva fecha de pago** en formato `dd-mm-yyyy` (`MSG-C49`), partiendo de la fecha de pago actual como valor propuesto.
4. **[Feliz — con motivo]** Si la nueva fecha cumple `RN-C01`, la factura vuelve a `Habilitada` (T-08) y se informa `MSG-C51` en su variante de habilitada.
5. **[Alternativo — con motivo]** Si la nueva fecha **no** cumple `RN-C01`, la factura queda en `NO ELEGIBLE` (T-09), pasa a la pestaña **Facturas No Operables** y se informa `MSG-C51` en su variante de no elegible.
6. **[Error / validación]** Si la fecha ingresada tiene formato inválido, no se aplica ningún cambio y se muestra `MSG-C50`.
7. **[Alternativo]** Si se cancela la captura del motivo, la factura permanece en `Pendiente aprobación EGP`.
8. **[Feliz]** El **motivo del rechazo** se registra y queda visible para el solicitante (`MSG-C55`).
9. **[Alternativo]** El rechazo libera el límite freezado de la operación (`SIM-01.5`, AC 4).
10. **[Alternativo]** El rechazo dispara la notificación correspondiente al Proveedor (`SIM-04`).

#### Escenarios BDD
```gherkin
Característica: Rechazo del adelanto por el EGP
  Antecedentes:
    Dado que soy aprobador del EGP
    Y la factura "001-003-0004002" está en estado "Pendiente aprobación EGP"

  Escenario: Rechazo sin motivo
    Cuando abro el modal "Aprobación EGP" y rechazo sin motivo
    Entonces la factura pasa a estado "Bloqueada"
    Y veo el mensaje MSG-C52

  Escenario: Rechazo con motivo y fecha válida
    Cuando rechazo con motivo e indico la nueva fecha de pago a 60 días desde hoy
    Entonces la factura vuelve a estado "Habilitada"
    Y veo el mensaje MSG-C51

  Escenario: Rechazo con motivo y fecha fuera de condiciones
    Cuando rechazo con motivo e indico una fecha de pago a 10 días desde hoy
    Entonces la factura queda en estado "NO ELEGIBLE"
    Y pasa a la pestaña "Facturas No Operables"

  Escenario: Fecha con formato inválido
    Cuando rechazo con motivo e ingreso "2026/13/45"
    Entonces veo el mensaje MSG-C50
    Y la factura sigue en estado "Pendiente aprobación EGP"
```

#### Fuera de alcance
- Reintento automático del adelanto tras el rechazo.
- Flujo de reversión con doble aprobación (operador / supervisor) → §11.

#### Notas / preguntas abiertas
- **Gap de POC:** el «motivo» del rechazo en la POC es en realidad **solo la nueva fecha de pago**; no hay campo de texto donde el EGP explique por qué rechaza, ni el proveedor puede verlo. El AC 8 incorpora ese campo, que hay que redactar y modelar → `SPK-C08`.
- La POC además **sobrescribe la fecha de vencimiento** con la nueva fecha de pago en este flujo, cosa que no hace en `CON-04`. Hay que unificar el criterio → `SPK-C16`.
- Rechazar sin motivo deja la factura `Bloqueada`, sin trazabilidad de quién ni por qué. Recomendación del PO: registrar siempre autor y fecha del rechazo aunque no haya motivo.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## 8. Historias técnicas — endpoints BFF / BE (enablers)

### FAC-03 — GET · Información de existencia y estado del ente

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | `FAC-01.1`, `FAC-01.2`, `FAC-02.2`, `FAC-04` |
| **Contrato** | `GET /obtenerInfoEnte` |
| **Reuso** | El Excel indica `MAGIA-120 / MAGIA-122 Ya desarrollado`: se reutiliza el servicio existente; el trabajo se limita a integrarlo y validar que expone lo necesario. |

#### Objetivo técnico
Exponer al FE, para un ente identificado por RUC o por id, su **existencia**, su **estado** y sus **monedas habilitadas**, de modo que la carga de facturas pueda validar el EGP y el Proveedor antes de persistir (`RN-C23`) y ofrecer solo las monedas admitidas (`RN-C17`).

#### Criterios de aceptación
1. Devuelve, para un ente existente: identificador, tipo (`EGP` / `Proveedor`), RUC, razón social, estado y monedas habilitadas.
2. Devuelve el vínculo `Proveedor → EGP padre`, necesario para acotar el selector de Proveedor al EGP elegido.
3. Ante un ente inexistente responde con el código de negocio correspondiente, sin exponer detalles internos.
4. El contrato distingue explícitamente **inexistente** de **existente pero inactivo**: son dos mensajes distintos para el usuario.
5. Tiempo de respuesta compatible con una validación en línea al guardar la factura (objetivo: p95 por debajo de 500 ms).
6. Es idempotente y cacheable por un período corto y configurable.
7. Queda documentado en el catálogo de APIs con ejemplos de request y response.

#### Escenarios BDD
```gherkin
Característica: Consulta de existencia y estado del ente
  Escenario: Ente activo
    Dado un EGP existente y activo
    Cuando el BFF consulta su información
    Entonces recibe su estado activo y sus monedas habilitadas

  Escenario: Ente inactivo
    Dado un EGP existente pero bloqueado
    Cuando el BFF consulta su información
    Entonces recibe el estado bloqueado
    Y el FE bloquea la carga de la factura con MSG-C15

  Escenario: Ente inexistente
    Cuando el BFF consulta un RUC que no existe
    Entonces recibe el error de ente no encontrado
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 400 | `ENTE_PARAM_INVALIDO` | Falta el identificador o el RUC tiene formato inválido |
| 404 | `ENTE_NO_ENCONTRADO` | El ente no existe |
| 409 | `ENTE_INACTIVO` | El ente existe pero no está en condiciones de operar |
| 503 | `SERVICIO_ENTES_NO_DISPONIBLE` | El servicio de entes no responde |

---

### FAC-05a — POST · Crear factura

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | `FAC-01.1`, `FAC-02.2`, `FAC-04` |
| **Contrato** | `POST /cargarFactura` |

#### Objetivo técnico
Persistir la factura enviada desde el FE (alta individual, masiva o por escaneo), aplicando las reglas de estado inicial y devolviendo el resultado con el estado resuelto por el motor de estados.

#### Criterios de aceptación
1. Recibe: número de factura, EGP, Proveedor, fecha de emisión, fecha de vencimiento, fecha de pago, moneda, monto y estado inicial solicitado.
2. Valida obligatoriedad y tipos: monto numérico mayor a cero, fechas válidas, moneda dentro de las habilitadas para el EGP (`RN-C17`).
3. Valida que EGP y Proveedor existan y estén activos (`RN-C23`), apoyándose en `FAC-03`.
4. Aplica `RN-C01`: si la fecha de pago está a menos del umbral configurado, persiste la factura en `NO ELEGIBLE` **por encima** del estado solicitado.
5. Si no se envía fecha de pago, toma la fecha de vencimiento (`RN-C02`).
6. Normaliza el estado inicial a `Pendiente`, `Habilitada` o `Bloqueada`; cualquier otro valor se persiste como `Pendiente` (`RN-C03`).
7. Devuelve la factura creada con su identificador y su **estado efectivo**, para que el FE pueda mostrar `MSG-C03` o `MSG-C04` según corresponda.
8. Rechaza el alta duplicada según la clave que se defina en `SPK-C05`.
9. Admite **invocación por lote** para la carga masiva, devolviendo el resultado fila por fila con su motivo de rechazo, de modo que el FE pueda componer `MSG-C10` a `MSG-C13` sin lógica de negocio propia.
10. Registra en auditoría usuario, fecha, hora y origen del alta (manual / masiva / escaneo).

#### Escenarios BDD
```gherkin
Característica: Alta de factura
  Escenario: Alta simple exitosa
    Cuando se envía una factura válida con fecha de pago a 60 días
    Entonces se persiste con el estado inicial solicitado
    Y la respuesta incluye el identificador y el estado efectivo

  Escenario: Alta forzada a NO ELEGIBLE
    Cuando se envía una factura con fecha de pago a 10 días
    Entonces se persiste en estado "NO ELEGIBLE"
    Y la respuesta informa que el estado fue resuelto por la regla de fecha de pago

  Escenario: Alta por lote con filas inválidas
    Cuando se envía un lote de 10 facturas de las cuales 2 no tienen monto
    Entonces se persisten 8
    Y la respuesta detalla las 2 rechazadas con su motivo
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 400 | `FACTURA_DATOS_INCOMPLETOS` | Falta un campo obligatorio o el monto no es válido |
| 400 | `FACTURA_MONEDA_NO_HABILITADA` | La moneda no está habilitada para el EGP |
| 409 | `FACTURA_DUPLICADA` | Ya existe una factura con la misma clave |
| 409 | `ENTE_INACTIVO` | El EGP o el Proveedor no están activos |
| 422 | `FACTURA_FECHAS_INCONSISTENTES` | Emisión posterior al vencimiento u otra inconsistencia de fechas |
| 503 | `SERVICIO_NO_DISPONIBLE` | Error de dependencia al persistir |

---

### FAC-05b — POST · Notificación de nueva factura

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | `FAC-01.1`, `FAC-02.2` |
| **Contrato** | `POST /notificacionNuevaFactura` |

#### Objetivo técnico
Notificar al EGP la solicitud de carga de una factura cuando el alta se concreta con éxito, y **no** notificar cuando el alta falla.

#### Criterios de aceptación
1. Se invoca **únicamente** cuando `FAC-05a` devolvió alta exitosa.
2. La notificación identifica la factura (número, Proveedor, monto, moneda, fechas) y se dirige al **EGP** de la factura, según la configuración de destinatarios del ABM de notificaciones.
3. Si el alta falló, **no** se emite ninguna notificación.
4. En alta masiva, la notificación se agrupa por EGP en un único envío por lote en lugar de una notificación por factura.
5. El fallo del envío **no** revierte el alta de la factura: se registra el error y se reintenta según la política de reintentos.
6. Cada envío queda registrado con su resultado para trazabilidad.

#### Escenarios BDD
```gherkin
Característica: Notificación de carga de factura
  Escenario: Alta exitosa notifica al EGP
    Dado que la factura se creó correctamente
    Cuando se ejecuta la notificación
    Entonces el EGP recibe el aviso de pedido de carga de factura

  Escenario: Alta fallida no notifica
    Dado que la creación de la factura falló
    Entonces no se envía ninguna notificación

  Escenario: Fallo de envío no revierte el alta
    Dado que la factura se creó correctamente
    Y el servicio de notificaciones no responde
    Entonces la factura permanece creada
    Y el error de envío queda registrado para reintento
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 400 | `NOTIF_DATOS_INVALIDOS` | Falta el identificador de factura o el destinatario |
| 404 | `NOTIF_DESTINATARIO_NO_CONFIGURADO` | El EGP no tiene destinatarios configurados |
| 503 | `NOTIF_SERVICIO_NO_DISPONIBLE` | El servicio de notificaciones no responde |

---

### CON-03a — GET · Grilla de facturas

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | `CON-01.1`, `CON-01.2`, `CON-01.3` |
| **Contrato** | `GET /grillaFacturas` |

#### Objetivo técnico
Devolver al FE el conjunto de facturas del EGP o del Proveedor según el contexto del usuario, con los campos que la grilla necesita y con soporte de los filtros de la pantalla.

#### Criterios de aceptación
1. Devuelve por factura: número, EGP, Proveedor, fecha de emisión, fecha de vencimiento, fecha de pago, moneda, monto y estado.
2. Acepta como filtros: texto de búsqueda (número, EGP o Proveedor), estado, fecha de vencimiento, fecha de pago y agrupación por pestaña (vigentes / no vigentes / no operables).
3. La visibilidad se resuelve en el backend según el ente y el dominio del usuario: un Proveedor **nunca** recibe facturas de otro Proveedor.
4. Soporta paginación y ordenamiento, con valores por defecto documentados (ver `SPK-C14`).
5. Devuelve el total de resultados para poder mostrar contadores por pestaña.
6. Los importes se devuelven con su moneda; el formateo es responsabilidad del FE.
7. Rendimiento objetivo: p95 por debajo de 1 s con la paginación por defecto.

#### Escenarios BDD
```gherkin
Característica: Consulta de la grilla de facturas
  Escenario: Facturas de un EGP
    Dado un usuario del EGP "Retail S.A."
    Cuando el FE consulta la grilla
    Entonces recibe únicamente facturas cuyo EGP es "Retail S.A."

  Escenario: Filtro por pestaña
    Cuando el FE consulta con la agrupación "no-operables"
    Entonces recibe únicamente facturas en estado "NO ELEGIBLE"

  Escenario: Aislamiento entre proveedores
    Dado un usuario del proveedor "Tech Solutions S.A."
    Cuando consulta la grilla
    Entonces no recibe facturas de otros proveedores
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 400 | `FILTRO_INVALIDO` | Fecha mal formada o estado inexistente |
| 401 | `NO_AUTENTICADO` | Sesión inválida o expirada |
| 403 | `SIN_PERMISO_VER_GRILLA` | El rol no tiene permiso sobre la pestaña solicitada |
| 503 | `SERVICIO_NO_DISPONIBLE` | Error de dependencia |

---

### CON-06 — PATCH · Actualizar factura

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | `CON-03b`, `CON-04`, `CON-11.1`, `CON-11.2`, `SIM-05.1`, `SIM-05.2` |
| **Contrato** | `PATCH /actualizarFactura` |

#### Objetivo técnico
Concentrar en un único endpoint las modificaciones sobre una factura existente: baja, cambio de fecha de pago y cambio de estado, delegando siempre la validez de la transición en el motor de estados (`CON-09.1`).

#### Criterios de aceptación
1. Permite actualizar la **fecha de pago** de una factura y devuelve el estado resultante después de aplicar `RN-C01` (puede pasar a `NO ELEGIBLE` o volver a `Habilitada`).
2. Permite ejecutar un **cambio de estado** solicitando la transición; el motor de estados valida que la transición sea legal y la rechaza si no lo es (`RN-C04`, `RN-C05`, `RN-C11`).
3. Permite **dar de baja** una factura; el tipo de baja (lógica o física) queda definido por `SPK-C04` y el contrato debe soportar la opción elegida.
4. Admite **actualización por lote** para las acciones masivas de habilitar y bloquear, devolviendo el resultado por factura.
5. Es idempotente: repetir la misma transición ya aplicada no produce error ni doble efecto.
6. Registra en auditoría usuario, fecha, hora, estado previo, estado posterior y campo modificado.
7. Devuelve la factura actualizada completa, para que el FE refresque la fila sin una consulta adicional.
8. Controla concurrencia: si la factura cambió desde que el FE la leyó, la operación se rechaza con el código correspondiente.

#### Escenarios BDD
```gherkin
Característica: Actualización de factura
  Escenario: Cambio de fecha de pago que deja la factura no elegible
    Cuando se actualiza la fecha de pago a 10 días desde hoy
    Entonces la factura queda en estado "NO ELEGIBLE"
    Y la respuesta devuelve el estado resultante

  Escenario: Transición inválida
    Dado una factura en estado "Financiada"
    Cuando se solicita la transición a "Habilitada"
    Entonces la operación se rechaza con transición no permitida

  Escenario: Habilitación por lote
    Cuando se solicita habilitar 5 facturas en estado "Pendiente"
    Entonces las 5 quedan en estado "Habilitada"
    Y la respuesta detalla el resultado por factura

  Escenario: Conflicto de concurrencia
    Dado que otro usuario ya cambió el estado de la factura
    Cuando se envía la actualización con la versión anterior
    Entonces la operación se rechaza por conflicto
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 400 | `PAYLOAD_INVALIDO` | Fecha mal formada o campo no soportado |
| 403 | `SIN_PERMISO_ACTUALIZAR` | El rol no puede ejecutar la acción solicitada |
| 404 | `FACTURA_NO_ENCONTRADA` | La factura no existe o ya fue dada de baja |
| 409 | `TRANSICION_NO_PERMITIDA` | La transición no es válida para el estado actual |
| 409 | `CONFLICTO_CONCURRENCIA` | La factura fue modificada por otro usuario |
| 503 | `SERVICIO_NO_DISPONIBLE` | Error de dependencia |

---

### CON-08 — GET · Información financiera del ente

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | `CON-07.1`, `CON-07.2`, `CON-07.3`, `SIM-01.4` |
| **Contrato** | `GET /obtenerInfoEnte` *(vista financiera)* |
| **Reuso** | El Excel indica `MAGIA-120 / MAGIA-122 Ya desarrollado`: se reutiliza el servicio y se evalúa si ya expone límite freezado, créditos activos y morosidad. |

#### Objetivo técnico
Proveer la información crediticia que alimenta la cabecera de información financiera y las validaciones de límite: límite de crédito, límite freezado, tasas y, para Proveedores, créditos activos y estado de morosidad.

#### Criterios de aceptación
1. Para un **EGP** devuelve: RUC, razón social, límite de crédito, **límite freezado**, tasa de interés (TNA), comisión, IVA y monedas habilitadas.
2. El **límite disponible** se puede calcular como `límite − freezado` (`RN-C19`); el contrato debe exponer los dos valores por separado, no solo el resultado.
3. Para un **Proveedor** devuelve: RUC, razón social, **créditos activos** (cantidad e importe) y **estado de morosidad**.
4. Indica la moneda en la que están expresados el límite y el freezado (ver `SPK-C17`).
5. Diferencia «sin información disponible» de «valor cero»: el FE debe poder mostrar `—` en lugar de un cero engañoso.
6. Los datos son de solo lectura desde esta pantalla.
7. Rendimiento objetivo: p95 por debajo de 800 ms.

#### Escenarios BDD
```gherkin
Característica: Información financiera del ente
  Escenario: Datos financieros de un EGP
    Cuando el FE consulta la información financiera de un EGP
    Entonces recibe límite de crédito, límite freezado, TNA, comisión, IVA y monedas

  Escenario: Datos de riesgo de un Proveedor
    Cuando el FE consulta la información financiera de un Proveedor
    Entonces recibe la cantidad y el importe de sus créditos activos
    Y su estado de morosidad

  Escenario: Información de riesgo no disponible
    Dado que la fuente de riesgo no responde
    Cuando el FE consulta la información del Proveedor
    Entonces recibe la marca de información no disponible
    Y no un estado de morosidad por defecto
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 403 | `SIN_PERMISO_INFO_SENSIBLE` | El rol no tiene permiso para ver información financiera del ente |
| 404 | `ENTE_NO_ENCONTRADO` | El ente no existe |
| 424 | `FUENTE_RIESGO_NO_DISPONIBLE` | No se pudo obtener créditos activos o morosidad |
| 503 | `SERVICIO_NO_DISPONIBLE` | Error de dependencia |

---

### CON-09.1 — Motor de la máquina de estados de facturas

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | Todas las HU que cambian el estado de una factura: `FAC-01.1`, `FAC-02.2`, `CON-04`, `CON-11.1`, `CON-11.2`, `SIM-01.x`, `SIM-05.x` |
| **Contrato** | Componente de dominio invocado por `FAC-05a`, `CON-06` y `SIM-03`; expuesto para consulta por `CON-10` |

#### Objetivo técnico
Implementar de forma centralizada la máquina de estados de facturas: qué estados existen, qué transiciones son legales, cuál es su estado previo y posterior, y si se ejecutan de forma manual o automática. Ninguna capa debe poder cambiar el estado de una factura salteando este componente.

#### Criterios de aceptación
1. Implementa los ocho estados del producto: `Pendiente`, `Habilitada`, `Bloqueada`, `Pendiente aprobación EGP`, `Pendiente de desembolso`, `Financiada`, `Vencida` y `NO ELEGIBLE`.
2. Implementa las transiciones T-01 a T-15 de §6, cada una con su **estado previo**, su **estado posterior**, su **disparador** y su marca de ejecución **manual o automática**.
3. Toda factura **nace en `Pendiente`** de forma automática cuando el alta no especifica otro estado o cuando el arribo es desde la API ERP (T-01).
4. `Habilitada` y `Bloqueada` se alcanzan por **acción manual** del usuario (T-04, T-05).
5. Rechaza cualquier transición no declarada, devolviendo el error de transición no permitida sin modificar la factura.
6. Cada transición ejecutada genera un registro de auditoría con estado previo, estado posterior, disparador, usuario o proceso y marca temporal.
7. Las transiciones automáticas están identificadas como tales en la auditoría, con el proceso que las originó.
8. El conjunto de estados y transiciones está expuesto de forma consultable para `CON-10`, sin necesidad de desplegar código para conocerlo.
9. Los umbrales de negocio (30 días de fecha de pago, umbral de vencimiento) son **parámetros de configuración**, no constantes de código (supuesto S-02).

#### Escenarios BDD
```gherkin
Característica: Motor de la máquina de estados de facturas
  Esquema del escenario: Transiciones válidas
    Dado una factura en estado <previo>
    Cuando se ejecuta el disparador <disparador>
    Entonces la factura queda en estado <posterior>
    Y la transición se registra como <tipo>

    Ejemplos:
      | previo                   | disparador               | posterior                | tipo       |
      | (alta)                   | arribo desde API ERP     | Pendiente                | automática |
      | Pendiente                | habilitar                | Habilitada               | manual     |
      | Bloqueada                | habilitar                | Habilitada               | manual     |
      | Pendiente                | bloquear                 | Bloqueada                | manual     |
      | Habilitada               | bloquear                 | Bloqueada                | manual     |
      | Habilitada               | ejecutar adelanto        | Pendiente aprobación EGP | manual     |
      | Pendiente aprobación EGP | aprobación del EGP       | Pendiente de desembolso  | manual     |
      | Pendiente de desembolso  | desembolso confirmado    | Financiada               | automática |
      | Pendiente de desembolso  | error de CORE BANKING    | Pendiente aprobación EGP | automática |

  Escenario: Transición no declarada
    Dado una factura en estado "Financiada"
    Cuando se intenta la transición a "Pendiente"
    Entonces la operación se rechaza
    Y el estado de la factura no cambia
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 409 | `TRANSICION_NO_PERMITIDA` | El disparador no es válido para el estado actual |
| 422 | `DISPARADOR_DESCONOCIDO` | El disparador solicitado no existe en la máquina |
| 500 | `ESTADO_INCONSISTENTE` | La factura está en un estado no declarado |

---

### CON-09.2 — Transición automática a Vencida

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | `CON-01.3` (pestaña No Vigentes), `CON-10` |
| **Contrato** | Proceso programado + `CON-09.1` (T-15) |

#### Objetivo técnico
Ejecutar de forma automática y periódica el pase a `Vencida` de las facturas cuya fecha de vencimiento documental entra en la condición definida por el negocio, dejándolas fuera del circuito operable.

#### Criterios de aceptación
1. Existe un proceso programado que evalúa periódicamente las facturas operables contra la regla de vencimiento documental.
2. Las facturas que cumplen la condición pasan a `Vencida` mediante `CON-09.1` (T-15), de forma **automática**, sin intervención del usuario.
3. Una factura `Vencida` **no es operable**: no puede habilitarse, bloquearse ni simularse, y se lista en la pestaña **Facturas No Vigentes**.
4. La frecuencia de ejecución y el umbral son **configurables**.
5. Cada pase queda auditado indicando que el disparador fue el proceso automático.
6. El proceso es **idempotente**: reejecutarlo no vuelve a procesar facturas ya vencidas ni genera efectos duplicados.
7. El proceso registra métricas de ejecución: cantidad evaluada, cantidad transicionada y duración.
8. Las facturas ya `Financiada` no se ven afectadas.

#### Escenarios BDD
```gherkin
Característica: Pase automático a Vencida
  Escenario: Factura que cumple la condición de vencimiento
    Dado una factura operable cuya fecha de vencimiento cumple la condición configurada
    Cuando se ejecuta el proceso programado
    Entonces la factura pasa a estado "Vencida"
    Y se lista en la pestaña "Facturas No Vigentes"
    Y ya no admite acciones operativas

  Escenario: Idempotencia del proceso
    Dado que el proceso ya marcó una factura como "Vencida"
    Cuando se ejecuta nuevamente
    Entonces esa factura no se vuelve a procesar

  Escenario: Factura financiada no se vence
    Dado una factura en estado "Financiada"
    Cuando se ejecuta el proceso
    Entonces su estado no cambia
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| — | `PROCESO_VENCIMIENTO_FALLIDO` | El proceso no pudo completarse; se registra y se reintenta en la siguiente ventana |
| 409 | `TRANSICION_NO_PERMITIDA` | La factura está en un estado que no admite el pase a `Vencida` |

> ⚠️ **Ambigüedad del requerimiento.** El Excel dice: *«Si la fecha de Vencimiento (documental) es menor a 30 dias pasa automaticamente a estado Vencida y ya no es operable»*. La redacción admite al menos dos lecturas: (a) faltan menos de 30 días para el vencimiento, o (b) el vencimiento ya ocurrió. Además convive con `RN-C01`, que usa el mismo número 30 pero sobre la **fecha de pago**. La POC no implementa ninguna de las dos. Esta HT **no puede desarrollarse** hasta resolver `SPK-C01`.

---

### CON-09.3 — Transición automática a NO ELEGIBLE y retorno por corrección de fecha

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | `CON-04`, `FAC-01.1`, `FAC-02.2`, `SIM-05.2` |
| **Contrato** | Regla de dominio en `CON-09.1` (T-03, T-13, T-14) + proceso programado |

#### Objetivo técnico
Aplicar de forma automática la regla de fecha de pago mínima: llevar la factura a `NO ELEGIBLE` cuando la fecha de pago queda dentro del umbral, y devolverla a `Habilitada` cuando el EGP la corrige.

#### Criterios de aceptación
1. Al **crear** una factura cuya fecha de pago está a menos del umbral configurado, el estado resultante es `NO ELEGIBLE`, cualquiera sea el estado solicitado (T-03, `RN-C01`).
2. Al **modificar** la fecha de pago de una factura operable a un valor dentro del umbral, la factura pasa a `NO ELEGIBLE` (T-13).
3. Al **modificar** la fecha de pago de una factura `NO ELEGIBLE` a un valor fuera del umbral, la factura vuelve **automáticamente** a `Habilitada` (T-14), tal como pide el Excel: *«mediante modal, la EGP puede modificar fecha de Pago y se actualiza automaticamente el estado a Habilitada»*.
4. La misma regla se aplica cuando la fecha de pago cambia por un **rechazo con motivo** del EGP (`SIM-05.2`, T-08 y T-09).
5. Un proceso programado reevalúa periódicamente las facturas operables: las que quedaron dentro del umbral por el mero paso del tiempo pasan a `NO ELEGIBLE`.
6. El umbral es **configurable** y su valor vigente es consultable por `CON-10` (supuesto S-02).
7. Cada pase queda auditado con el valor del umbral aplicado en ese momento.
8. Una factura `NO ELEGIBLE` no puede simularse ni habilitarse mientras no se corrija su fecha de pago.

#### Escenarios BDD
```gherkin
Característica: Regla de elegibilidad por fecha de pago
  Escenario: Alta dentro del umbral
    Cuando se crea una factura con fecha de pago a 10 días
    Entonces queda en estado "NO ELEGIBLE"

  Escenario: Corrección que devuelve la factura al circuito
    Dado una factura en estado "NO ELEGIBLE"
    Cuando el EGP corrige la fecha de pago a 60 días
    Entonces la factura pasa automáticamente a "Habilitada"

  Escenario: Caída por paso del tiempo
    Dado una factura "Habilitada" con fecha de pago a 31 días
    Cuando transcurren dos días y se ejecuta el proceso de reevaluación
    Entonces la factura pasa a "NO ELEGIBLE"
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 409 | `FACTURA_NO_ELEGIBLE` | Se intenta operar (habilitar, simular, adelantar) una factura en `NO ELEGIBLE` |
| 422 | `FECHA_PAGO_INVALIDA` | La fecha de pago enviada no es una fecha válida |

> **Pregunta abierta:** el AC 5 (reevaluación por paso del tiempo) es una consecuencia lógica de `RN-C01` pero **no está escrito en el Excel** ni implementado en la POC: hoy una factura habilitada nunca cae sola a `NO ELEGIBLE`. Se incluye porque sin él la regla es inconsistente, pero requiere confirmación del PO del cliente → `SPK-C23`.

---

### CON-10 — GET · Estados de facturas y condiciones de cambio

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | `CON-01.2` (opciones del filtro), `CON-01.3`, `CON-02` |
| **Contrato** | `GET /estadosDeFacturas` |

#### Objetivo técnico
Exponer el catálogo de estados y las condiciones de cambio de la máquina de estados, para que el FE no tenga que replicar en código las reglas de transición ni la lista de estados.

#### Criterios de aceptación
1. Devuelve el catálogo de estados con su identificador, su etiqueta para mostrar y la pestaña a la que pertenece (`RN-C13`).
2. Devuelve, por estado, las **transiciones posibles** con su disparador y su tipo de ejecución (manual o automática).
3. Devuelve los **parámetros vigentes** que condicionan las transiciones automáticas: umbral de fecha de pago y umbral de vencimiento.
4. El FE puede armar con esta respuesta las opciones del filtro de estado y las acciones disponibles por fila, sin lógica duplicada.
5. Es cacheable: el catálogo cambia con muy baja frecuencia.
6. Refleja siempre la configuración real de `CON-09.1`; si un estado o transición se agrega, aparece sin desplegar el FE.

#### Escenarios BDD
```gherkin
Característica: Catálogo de estados de facturas
  Escenario: Consulta del catálogo
    Cuando el FE consulta el catálogo de estados
    Entonces recibe los ocho estados con su etiqueta y su pestaña
    Y recibe las transiciones posibles de cada estado con su tipo de ejecución

  Escenario: Parámetros vigentes
    Cuando el FE consulta el catálogo
    Entonces recibe el umbral de días de fecha de pago vigente

  Escenario: Sincronía con el motor
    Dado que se agrega una transición en el motor de estados
    Cuando el FE consulta el catálogo
    Entonces la nueva transición aparece en la respuesta
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 401 | `NO_AUTENTICADO` | Sesión inválida |
| 503 | `SERVICIO_NO_DISPONIBLE` | Error de dependencia |

---

### SIM-02 — GET · Simulación de adelanto de factura

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | `SIM-01.1`, `SIM-01.2`, `SIM-01.3`, `SIM-01.4`, `CON-05` |
| **Contrato** | `GET /simularAdelantoFactura` |

#### Objetivo técnico
Devolver el cálculo financiero del adelanto (intereses, comisiones, IVA y neto a acreditar) y los límites crediticios actualizados, para alimentar el modal de simulación y el de aprobación del EGP.

#### Criterios de aceptación
1. Recibe la o las facturas a adelantar y el monto a adelantar, y devuelve: días a adelantar, tasa aplicada, intereses, comisión, IVA, **monto neto a acreditar** y la moneda de la operación (`RN-C09`).
2. Devuelve además el **límite de crédito actualizado** del EGP: total, freezado y disponible (`RN-C19`), para alimentar `CON-07.3` y `SIM-01.4`.
3. En simulación múltiple devuelve el cálculo agregado y el **plan de cuotas** cuando las fechas de pago difieren (`SIM-01.3`).
4. Las tasas provienen de la configuración del EGP; el cálculo **no** se resuelve en el FE.
5. Valida el **límite de tiempo** entre la aprobación del EGP y la solicitud del adelanto (`RN-C22`): si se superaron los *n* días configurados, devuelve el error de expiración y el FE muestra `MSG-C45`.
6. Ante error de cálculo devuelve un código de negocio interpretable por el FE y **no** un neto parcial o en cero.
7. Es una operación de solo lectura: no persiste nada ni cambia estados.
8. El número de días configurable de la validación de expiración es un parámetro, no una constante.

#### Escenarios BDD
```gherkin
Característica: Cálculo de la simulación de adelanto
  Escenario: Cálculo correcto
    Cuando se solicita la simulación de una factura habilitada
    Entonces se reciben días a adelantar, intereses, comisión, IVA y monto neto
    Y se recibe el límite disponible del EGP

  Escenario: Error de cálculo
    Dado que falta la configuración de tasas del EGP
    Cuando se solicita la simulación
    Entonces se recibe un error de cálculo
    Y no se devuelve ningún importe neto

  Escenario: Adelanto expirado
    Dado que pasaron más días de los configurados desde la aprobación del EGP
    Cuando se solicita la simulación
    Entonces se recibe el error de expiración
    Y el FE muestra MSG-C45
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 400 | `SIMULACION_PARAMETROS_INVALIDOS` | Falta la factura o el monto no es válido |
| 409 | `FACTURA_ESTADO_INVALIDO` | La factura no está en un estado simulable |
| 409 | `ADELANTO_EXPIRADO` | Se superó el plazo entre la aprobación del EGP y la solicitud (`RN-C22`) |
| 422 | `CONFIGURACION_TASAS_INCOMPLETA` | El EGP no tiene tasas configuradas |
| 424 | `LIMITE_NO_DISPONIBLE` | No se pudo obtener el límite crediticio del EGP |

---

### SIM-03 — POST · Generar adelanto de factura

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | `SIM-01.1`, `SIM-01.2`, `SIM-01.3`, `SIM-01.5`, `SIM-05.1` |
| **Contrato** | `POST /generarAdelantoFactura` |

#### Objetivo técnico
Crear la solicitud de adelanto, enviarla al CORE, mantener la relación cuenta préstamo ↔ facturas, aplicar las validaciones de negocio del Excel y revertir automáticamente ante error del servicio.

#### Criterios de aceptación
1. Crea la solicitud de adelanto con las facturas que la integran y devuelve su identificador y el nuevo estado de cada factura (`Pendiente aprobación EGP`).
2. **Escenario OK:** envía la solicitud al CORE y persiste la **relación cuenta préstamo ↔ facturas**; en el core queda registrado el número de cada factura que compone el préstamo.
3. **Escenario ERROR:** si la creación falla, **no** se envía nada al CORE y ninguna factura cambia de estado.
4. **Validación de segregación de funciones** (`RN-C20`): rechaza la solicitud cuando el usuario que la genera es el mismo que cargó la factura, devolviendo el código correspondiente para que el FE muestre `MSG-C46`.
5. **Validación de corte horario** (`RN-C21`): rechaza la solicitud fuera del horario permitido (antes de las 17 hs), devolviendo el código correspondiente para `MSG-C47`. La hora de corte es configurable.
6. **Reversión automática:** ante respuesta de error del servicio del core, revierte la operación completa y deja las facturas en su estado anterior, sin estados intermedios inconsistentes (`RN-C12`).
7. **Re-cálculo y freeze de límite:** al crearse la solicitud, freeza el importe correspondiente contra la línea del EGP y recalcula el disponible (`SIM-01.5`, `RN-C19`). El freeze y la creación de la solicitud son **atómicos**.
8. Si el límite disponible no alcanza al momento de la creación, rechaza la operación y no freeza nada.
9. Soporta operaciones **de una o de varias cuotas** según el plan recibido (`SIM-01.3`).
10. Registra en auditoría usuario, fecha, hora, facturas, importes, plan de cuotas y resultado.
11. Es idempotente frente a reintentos con la misma clave de idempotencia: no genera dos préstamos por un doble envío.

#### Escenarios BDD
```gherkin
Característica: Generación del adelanto de factura
  Escenario: Adelanto generado correctamente
    Cuando se genera el adelanto de una factura habilitada
    Entonces se crea la solicitud y se envía al CORE
    Y queda registrada la relación entre la cuenta préstamo y la factura
    Y la factura pasa a "Pendiente aprobación EGP"

  Escenario: Error de creación
    Dado que la creación de la solicitud falla
    Entonces no se envía nada al CORE
    Y las facturas conservan su estado anterior

  Escenario: Solicitante igual al cargador de la factura
    Dado que la factura fue cargada por el mismo usuario que solicita el adelanto
    Cuando se genera el adelanto
    Entonces la operación se rechaza por segregación de funciones

  Escenario: Solicitud fuera del horario permitido
    Dado que son las 18:30
    Cuando se genera el adelanto
    Entonces la operación se rechaza por corte horario

  Escenario: Reversión automática ante error del servicio
    Dado que el servicio del core responde con error
    Cuando se genera el adelanto
    Entonces la operación se revierte por completo
    Y el límite freezado se libera

  Escenario: Idempotencia
    Cuando se reenvía la misma solicitud con la misma clave de idempotencia
    Entonces no se crea un segundo préstamo
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 400 | `ADELANTO_PARAMETROS_INVALIDOS` | Faltan facturas, monto o plan de cuotas inválido |
| 403 | `SEGREGACION_FUNCIONES` | El solicitante es quien cargó la factura (`RN-C20`) |
| 409 | `FUERA_DE_HORARIO` | Solicitud posterior a la hora de corte (`RN-C21`) |
| 409 | `FACTURA_ESTADO_INVALIDO` | Alguna factura no está en `Habilitada` |
| 409 | `LIMITE_INSUFICIENTE` | El disponible del EGP no alcanza (`RN-C19`) |
| 422 | `PLAN_CUOTAS_NO_SOPORTADO` | La cantidad de cuotas excede lo admitido por el core |
| 502 | `CORE_ERROR` | El core respondió con error; se ejecuta la reversión automática |
| 503 | `SERVICIO_NO_DISPONIBLE` | Error de dependencia |

---

### SIM-04 — POST · Notificación de adelanto de factura

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | `SIM-01.1`, `SIM-01.2`, `SIM-01.3`, `SIM-05.1` |
| **Contrato** | `POST /notificacionAdelantoFactura` |
| **Dominios** | `Recurso: EGP/PROVEEDOR · Dominio: EGP/PROVEEDOR` |

#### Objetivo técnico
Notificar al EGP el pedido de adelanto y al Proveedor el crédito generado, únicamente cuando la operación fue exitosa.

#### Criterios de aceptación
1. **Adelanto OK → EGP:** se envía la notificación del pedido de adelanto al EGP de la factura.
2. **Adelanto con ERROR → EGP:** no se envía ninguna notificación al EGP.
3. **Adelanto OK → Proveedor:** se envía al Proveedor la notificación del **crédito generado**, con el monto neto acreditado y las facturas incluidas.
4. **Adelanto con ERROR → Proveedor:** no se envía ninguna notificación al Proveedor.
5. Los destinatarios se resuelven según la configuración del ABM de notificaciones (dominio, rol y correos).
6. El fallo de una notificación **no** revierte la operación de adelanto: se registra el error y se reintenta según la política definida.
7. En operaciones múltiples se envía una sola notificación por destinatario, con el detalle de las facturas incluidas.
8. Cada envío queda registrado con destinatario, contenido y resultado.

#### Escenarios BDD
```gherkin
Característica: Notificaciones de adelanto de factura
  Escenario: Adelanto exitoso
    Dado que el adelanto se generó correctamente
    Entonces el EGP recibe la notificación del pedido de adelanto
    Y el Proveedor recibe la notificación del crédito generado

  Escenario: Adelanto con error
    Dado que el adelanto falló
    Entonces no se envía notificación al EGP
    Y no se envía notificación al Proveedor

  Escenario: Operación múltiple
    Dado un adelanto que agrupa cuatro facturas
    Entonces el Proveedor recibe una única notificación con las cuatro facturas
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 400 | `NOTIF_DATOS_INVALIDOS` | Falta el identificador de la operación o el destinatario |
| 404 | `NOTIF_DESTINATARIO_NO_CONFIGURADO` | El ente no tiene destinatarios configurados |
| 503 | `NOTIF_SERVICIO_NO_DISPONIBLE` | El servicio de notificaciones no responde |

---

## 9. Tareas técnicas / habilitadores

Estas tareas no entregan valor por sí solas, pero **bloquean o degradan** varias historias si no se resuelven. Se listan aparte para que se prioricen explícitamente.

| ID | Tarea | Por qué es necesaria | Historias impactadas |
|----|-------|----------------------|----------------------|
| `TAR-C01` | **Parametrizar los umbrales de negocio**: días mínimos de fecha de pago, umbral de vencimiento, hora de corte del adelanto, días de expiración del adelanto y frecuencia de los procesos programados. Deben ser configuración, no constantes de código. | Hoy en la POC el umbral de 30 días es una constante. Los umbrales cambian por política comercial y no pueden requerir despliegue. | `CON-09.1`, `CON-09.2`, `CON-09.3`, `CON-10`, `SIM-02`, `SIM-03` |
| `TAR-C02` | **Aplicar los permisos de la pantalla Confirming** en FE y BE. El catálogo de permisos ya existe (ver pantalla, filtros, pestañas, cargar manual, cargar masivo, editar datos, editar fecha de pago, habilitar, bloquear, simular, aprobar desembolso EGP, aprobar desembolso banco, revertir, ver información sensible, ver y descargar documentos, descargar grilla) pero **no se aplica**: hoy cualquier usuario ve y ejecuta todo. | Sin enforcement, un Proveedor podría ver facturas de otro ente o aprobar en nombre del EGP. Es un riesgo funcional y de seguridad. | Todas las HU de §7, en especial `CON-01.1`, `CON-02`, `CON-05`, `CON-07.x`, `SIM-05.x` |
| `TAR-C03` | **Auditoría y trazabilidad** de todas las acciones sobre facturas: alta, baja, cambio de fecha de pago, cambio de estado, solicitud de adelanto, aprobación y rechazo, con usuario, marca temporal, estado previo y posterior. | Es requisito de una operatoria financiera y condición para resolver disputas; además sostiene varios AC ya escritos (`CON-03b`, `CON-06`, `CON-09.1`, `SIM-03`). | `CON-03b`, `CON-04`, `CON-06`, `CON-09.1`, `CON-11.x`, `SIM-03`, `SIM-05.x` |

---

## 10. Spikes y decisiones pendientes

La columna `DUDAS` del Excel está **vacía en las 23 filas**. Los spikes que siguen surgen del análisis cruzado entre la planilla y la POC: son ambigüedades del requerimiento o divergencias entre lo pedido y lo construido. **Ninguno se resolvió por decisión propia.**

| ID | Pregunta a resolver | Bloquea | Origen |
|----|---------------------|---------|--------|
| `SPK-C01` | ¿Qué significa exactamente *«fecha de Vencimiento (documental) menor a 30 días → Vencida»*? ¿Faltan menos de 30 días para el vencimiento o el vencimiento ya pasó? ¿Y cómo convive ese 30 con el 30 de la fecha de pago? | `CON-09.2` | Excel `CON-09` |
| `SPK-C02` | ¿Se puede **bloquear** una factura que ya está en `Pendiente de aprobación EGP`? Si sí, ¿qué pasa con la solicitud enviada y con el límite freezado? | `CON-11.2`, `SIM-01.5` | Excel `CON-11` vs POC |
| `SPK-C03` | El Excel pide **Editar Fecha de Pago siempre visible y activo**; la POC lo restringe a cuatro estados. ¿Se oculta, se muestra deshabilitado con motivo, o se habilita en todos los estados? | `CON-02`, `CON-04` | Excel `CON-02` vs POC |
| `SPK-C04` | ¿La baja de factura es **lógica o física**? El propio Excel lo pregunta. ¿Y se puede eliminar una factura ya `Financiada` o en curso de desembolso? | `CON-03b`, `CON-06` | Excel `CON-06` |
| `SPK-C05` | ¿Cuál es la **clave única** de una factura? ¿Número solo, número + EGP, número + EGP + Proveedor? ¿Se admite recargar una factura eliminada? | `FAC-01.1`, `FAC-02.2`, `FAC-05a` | Análisis (la POC no valida duplicados) |
| `SPK-C06` | El corte de las **17 hs**: ¿qué zona horaria, qué pasa con días no hábiles y feriados, aplica solo a la generación del adelanto o también a la simulación? | `SIM-03` | Excel `SIM-03` |
| `SPK-C07` | ¿La **aprobación bancaria** es definitivamente automática? En la POC los botones de aprobación y rechazo del banco están desactivados y el flujo pasa directo al core. | `SIM-05.1`, `CON-09.1` | POC vs catálogo de permisos |
| `SPK-C08` | El **motivo del rechazo** del EGP: ¿es texto libre, una lista de motivos, u obligatoriamente el cambio de fecha de pago? Hoy la POC solo pide la nueva fecha. ¿El proveedor debe poder verlo? | `SIM-05.2`, `MSG-C55` | Excel `CON-05` y `SIM-05` vs POC |
| `SPK-C09` | ¿Los selectores de EGP y Proveedor del alta deben alimentarse del ABM y encadenarse (Proveedor filtrado por EGP)? En la POC son listas fijas e independientes. | `FAC-01.1`, `FAC-03` | Análisis |
| `SPK-C10` | ¿Qué estados del ABM cuentan como **«activo»** para permitir cargar una factura: solo `Activo`, o también `Autorizado`? | `FAC-01.2` | Excel `FAC-01` y `FAC-02` |
| `SPK-C11` | ¿Cuál es el **límite de filas** por archivo en la carga masiva y qué comportamiento se espera al superarlo (rechazo, procesamiento asincrónico, troceo)? | `FAC-02.2` | Análisis |
| `SPK-C12` | ¿Qué tecnología de **escaneo** se usa: QR de la factura electrónica, OCR sobre imagen, lectora externa? El propio Excel plantea el escenario con signo de pregunta. | `FAC-02.3` | Excel `FAC-02` |
| `SPK-C13` | ¿La moneda local se rotula **`GS`** (como la POC) o **`PYG`** (como el Excel)? Definir el literal del producto. | `FAC-04` | Excel `FAC-04` vs POC |
| `SPK-C14` | ¿La grilla debe **paginar**? ¿Con qué tamaño de página y qué ordenamiento por defecto? La POC renderiza todo. | `CON-01.1`, `CON-03a` | Análisis |
| `SPK-C15` | ¿El filtro de estado debe **acotarse a los estados de la pestaña activa**? Hoy permite combinaciones que garantizan grilla vacía. | `CON-01.2` | Análisis |
| `SPK-C16` | Al cambiar la **fecha de pago**, ¿debe alinearse también la fecha de vencimiento? La POC lo hace en el rechazo del EGP pero no en la edición desde la grilla. | `CON-04`, `SIM-05.2` | POC (comportamiento inconsistente) |
| `SPK-C17` | ¿El **límite de crédito** del EGP es único en moneda local o hay un límite por moneda? ¿Cómo se consume una factura en USD contra un límite en guaraníes? | `CON-07.1`, `CON-07.3`, `SIM-01.4` | Excel `CON-07` vs POC |
| `SPK-C18` | ¿De dónde salen los **créditos activos** y el **estado de morosidad** del Proveedor? ¿Del core, de un buró, del propio confirming? | `CON-07.2`, `CON-08` | Excel `CON-07` |
| `SPK-C19` | Ciclo de vida del **freeze de límite**: ¿en qué momento exacto se freeza y en cuáles se libera (rechazo del EGP, error del core, expiración, eliminación de la factura, desembolso)? | `SIM-01.5`, `CON-07.3`, `SIM-03` | Excel `SIM-01` |
| `SPK-C20` | Los **días a adelantar**, ¿se cuentan hasta la fecha de **vencimiento** o hasta la fecha de **pago**? La POC usa el vencimiento; la elegibilidad usa la fecha de pago. | `SIM-01.1`, `SIM-01.3`, `SIM-02` | POC vs `RN-C01` |
| `SPK-C21` | ¿Cuál es el **máximo de cuotas** que admite el core para un préstamo de confirming? | `SIM-01.3`, `SIM-03` | Excel `SIM-01` |
| `SPK-C22` | En una solicitud **múltiple**, ¿la aprobación o el rechazo del EGP aplican a toda la operación o factura por factura? La POC hoy resuelve solo la factura desde la que se abrió el modal. | `SIM-05.1`, `SIM-05.2` | POC |
| `SPK-C23` | ¿Una factura ya `Habilitada` debe caer sola a `NO ELEGIBLE` cuando el paso del tiempo la deja dentro del umbral? Es la consecuencia lógica de `RN-C01`, pero no está escrita ni implementada. | `CON-09.3` | Análisis |

---

## 11. Recomendaciones del PO — historias faltantes (no están en el Excel)

**Nada de esta sección está comprometido.** Son huecos detectados al cruzar el Excel con la POC; se proponen para priorizar por separado.

### 11.1 Imprescindibles antes de salir a producción

| # | Propuesta | Motivo |
|---|-----------|--------|
| R-01 | **Aplicar los permisos de Confirming** (ver `TAR-C02`). | Sin esto, el aislamiento entre EGP y Proveedores no está garantizado. Es la brecha más seria detectada. |
| R-02 | **Paginación y ordenamiento** de la grilla. | Con volumen real la pantalla se vuelve inusable y el navegador se degrada. |
| R-03 | **Control de duplicados** al cargar facturas. | Hoy se puede cargar la misma factura dos veces, individualmente o por archivo, y adelantarla dos veces. |
| R-04 | **Motivo de bloqueo y motivo de rechazo** persistidos y visibles. | Hoy una factura queda bloqueada sin que nadie sepa por qué; imposibilita la gestión de excepciones. |
| R-05 | **Confirmación explícita en la aprobación del EGP.** | Es la acción de mayor impacto financiero del circuito y se ejecuta hoy con un solo clic. |
| R-06 | **Manejo de concurrencia** en la grilla (bloqueo optimista, refresco ante conflicto). | Varios usuarios operan la misma cartera; hoy no hay ningún control. |

### 11.2 Recomendadas para completar la experiencia

| # | Propuesta | Motivo |
|---|-----------|--------|
| R-07 | **Descargar la grilla** filtrada a Excel o CSV. | El permiso «Descargar Grilla» ya existe en el catálogo pero no hay funcionalidad; es un pedido recurrente en operaciones. |
| R-08 | **Contador de facturas por pestaña** y por estado. | Da visión de cartera de un vistazo y ayuda a priorizar el trabajo del día. |
| R-09 | **Columna de moneda** en la grilla y **filtro por moneda y por rango de montos**. | Con carteras multimoneda, inferir la moneda del formato del monto es frágil. |
| R-10 | **Filtro por rango de fechas** en lugar de fecha exacta. | Buscar por una fecha puntual obliga a conocer el dato exacto de antemano. |
| R-11 | **Edición del resto de los datos de la factura** (permiso «Editar Factura — datos cargados», que existe en el catálogo pero no tiene pantalla). | Hoy un error en el monto o en el número obliga a eliminar y volver a cargar. |
| R-12 | **Eliminación masiva** de facturas seleccionadas. | Complemento natural de la carga masiva: si se carga un lote equivocado, hay que borrarlo de a una. |
| R-13 | **Flujo de reversión con doble aprobación** (operador y supervisor). | Los permisos «Revertir factura» y «Revertir factura 2da aprobación» y los botones «Operador Aprueba», «Supervisor Aprueba» y «Supervisor Rechaza» existen en la POC pero **no tienen ningún flujo detrás**. |
| R-14 | **Adjuntar y consultar documentos** de la factura. | Los permisos «Ver Documentos» y «Descargar Documentos» existen en el catálogo, sin pantalla asociada. |
| R-15 | **Bloqueo o alerta por morosidad del Proveedor** al solicitar adelanto. | `CON-07.2` muestra la morosidad pero nada impide adelantarle a un proveedor en mora. |
| R-16 | **Informar en el resultado de la carga masiva** cuáles de las facturas cargadas quedaron en `NO ELEGIBLE`. | Hoy entran silenciosamente y el usuario las descubre recién al buscarlas en otra pestaña. |
| R-17 | **Historial de la factura** (línea de tiempo de estados y acciones). | Complementa `TAR-C03` y resuelve la mayoría de las consultas de soporte. |

---

## 12. Observaciones sobre la consistencia del Excel

Se documentan tal como aparecen en la planilla, sin corregirlas en la fuente.

| # | Observación | Fila | Tratamiento en este documento |
|---|-------------|------|-------------------------------|
| O-01 | **`Issue Key` duplicado:** `FAC-05` figura en las filas 7 y 8, para dos entregables distintos (crear factura y notificar la creación). | 7, 8 | Desambiguados como `FAC-05a` y `FAC-05b`. |
| O-02 | **`Issue Key` duplicado:** `CON-03` figura en la fila 10 (`GET/grillafacturas`, BE/BFF) y en la fila 12 (`Grilla accion Eliminar`, FE). | 10, 12 | Desambiguados como `CON-03a` y `CON-03b`. |
| O-03 | **Escenario copiado:** `CON-06` (`PATCH/actualizarfactura`) tiene como escenario `-Escenario FE/BFF/BE consulta las facturas a mostrar en la grilla`, que es literalmente el escenario de `CON-03a` y **no describe una actualización**. | 15 | La HT `CON-06` se redactó a partir del `OBJETIVO` de la fila (baja, fecha de pago, cambio de estado) y de las HU que la consumen. Requiere validación del PO del cliente. |
| O-04 | **Numeración fuera de orden:** las filas se suceden `CON-01`, `CON-03`, `CON-02`, `CON-03`, `CON-04`… | 9 a 12 | Se respetó el orden lógico de lectura, no el de la planilla. |
| O-05 | **Stack sin definir:** `CON-09` tiene `BE/BFF?` con signo de pregunta y `CON-07` tiene la celda de `STACK` **vacía**. | 16, 18 | `CON-09` se trató como enabler de backend; `CON-07` como historias de FE, por su `Summary` («Pantalla Información EGP»). |
| O-06 | **Erratas de tipeo** en los escenarios: `booón Editar`, `masico: cargar desde archivo`, `Hablitar`, `Simulación de Adelante de Factura`, `oprobador del EGP`, `cEGP`, `notificaciónNuevarFactura`. | varias | Se transcriben literales en «Escenarios fuente» y se normalizan en el resto de la redacción. |
| O-07 | **Columna `Issue Type` vacía** en las 23 filas. | todas | El tipo (HU / HT) se derivó de la columna `STACK` y del `Summary`. |
| O-08 | **Columna `DUDAS` vacía** en las 23 filas. | todas | Las ambigüedades detectadas se abrieron como spikes en §10 en lugar de asumirse resueltas. |
| O-09 | **Dos filas apuntan al mismo endpoint:** `FAC-03` y `CON-08` son ambas `GET/obtenerInfoEnte`, con objetivos distintos (estado del ente vs. información financiera). | 5, 17 | Se mantuvieron como dos HT separadas porque responden a necesidades distintas, señalando que comparten servicio y que ya está desarrollado. |
| O-10 | **Sin filas tachadas ni escenarios desestimados.** | — | El alcance del Excel entra completo al backlog. |

---

## 13. Matriz de trazabilidad HU ↔ endpoint ↔ pantalla de la POC

| Historia | Fila Excel | Tipo | Endpoint / componente | Pantalla o elemento de la POC |
|----------|------------|------|-----------------------|-------------------------------|
| `FAC-01.1` | 3 | HU-FE | `POST /cargarFactura` | Botón **Cargar Factura** → modal «Cargar Nueva Factura» → carga individual |
| `FAC-01.2` | 3, 4 | HU-FE | `GET /obtenerInfoEnte` | Modal de carga *(validación no implementada)* |
| `FAC-02.1` | 4 | HU-FE | — (generación en cliente) | Modal de carga → **Descargar Template** |
| `FAC-02.2` | 4 | HU-FE | `POST /cargarFactura` (lote) | Modal de carga → **Cargar desde archivo** → modal «Resultado de carga masiva» |
| `FAC-02.3` | 4 | HU-FE | `POST /cargarFactura` | Modal de carga → acción de escaneo → overlay «Escaneando documento...» |
| `FAC-03` | 5 | HT | `GET /obtenerInfoEnte` | — (reuso `MAGIA-120 / MAGIA-122`) |
| `FAC-04` | 6 | HU-FE | `GET /obtenerInfoEnte` | Modal de carga → campo **Moneda** |
| `FAC-05a` | 7 | HT | `POST /cargarFactura` | — |
| `FAC-05b` | 8 | HT | `POST /notificacionNuevaFactura` | — |
| `CON-01.1` | 9 | HU-FE | `GET /grillaFacturas` | Tabla principal de Confirming |
| `CON-01.2` | 9 | HU-FE | `GET /grillaFacturas` | Barra de filtros: Buscar, Fecha de Vencimiento, Fecha de Pago, Estado |
| `CON-01.3` | 9 | HU-FE | `GET /grillaFacturas`, `GET /estadosDeFacturas` | Pestañas **Facturas Vigentes / No Vigentes / No Operables** |
| `CON-02` | 11 | HU-FE | — | Columna **Acciones** y columna de eliminar de cada fila |
| `CON-03a` | 10 | HT | `GET /grillaFacturas` | — |
| `CON-03b` | 12 | HU-FE | `PATCH /actualizarFactura` | Acción de eliminar → modal «Eliminar factura» |
| `CON-04` | 13 | HU-FE | `PATCH /actualizarFactura` | Acción **Editar fecha de pago** → modal «Editar fecha de pago» |
| `CON-05` | 14 | HU-FE | `GET /simularAdelantoFactura` | Acción **Aprobar EGP** → modal «Aprobación EGP» |
| `CON-06` | 15 | HT | `PATCH /actualizarFactura` | — |
| `CON-07.1` | 16 | HU-FE | `GET /obtenerInfoEnte` | Cabecera de información del ente (EGP) |
| `CON-07.2` | 16 | HU-FE | `GET /obtenerInfoEnte` | Cabecera de información del ente (Proveedor) *(riesgo no implementado)* |
| `CON-07.3` | 16 | HU-FE | `GET /obtenerInfoEnte` | Cabecera de información del ente → Límite Crediticio *(cálculo no implementado)* |
| `CON-08` | 17 | HT | `GET /obtenerInfoEnte` | — (reuso `MAGIA-120 / MAGIA-122`) |
| `CON-09.1` | 18 | HT | Motor de estados | Transversal a toda la pantalla |
| `CON-09.2` | 18 | HT | Proceso programado | Pestaña **Facturas No Vigentes** *(no implementado)* |
| `CON-09.3` | 18 | HT | Motor de estados + proceso programado | Pestaña **Facturas No Operables** |
| `CON-10` | 19 | HT | `GET /estadosDeFacturas` | Filtro **Estado**, pestañas, acciones por fila |
| `CON-11.1` | 20 | HU-FE | `PATCH /actualizarFactura` (lote) | Botón global **Habilitar** |
| `CON-11.2` | 20 | HU-FE | `PATCH /actualizarFactura` (lote) | Botón global **Bloquear** |
| `SIM-01.1` | 21 | HU-FE | `GET /simularAdelantoFactura`, `POST /generarAdelantoFactura` | Acción **Simular** de la fila → modal «Simulación de Adelanto» |
| `SIM-01.2` | 21 | HU-FE | `GET /simularAdelantoFactura`, `POST /generarAdelantoFactura` | Selección múltiple + botón global **Simular** → modal «Simulación de Adelanto (masiva)» |
| `SIM-01.3` | 21 | HU-FE | `GET /simularAdelantoFactura`, `POST /generarAdelantoFactura` | Ídem *(plan de cuotas no implementado)* |
| `SIM-01.4` | 21 | HU-FE | `GET /obtenerInfoEnte`, `GET /simularAdelantoFactura` | Casillas de selección de la grilla *(no implementado)* |
| `SIM-01.5` | 21 | HU-FE + HU-BE | `POST /generarAdelantoFactura` | Confirmación del modal de simulación *(no implementado)* |
| `SIM-02` | 22 | HT | `GET /simularAdelantoFactura` | — |
| `SIM-03` | 23 | HT | `POST /generarAdelantoFactura` | — |
| `SIM-04` | 24 | HT | `POST /notificacionAdelantoFactura` | — |
| `SIM-05.1` | 25 | HU-FE | `PATCH /actualizarFactura`, `POST /notificacionAdelantoFactura` | Modal «Aprobación EGP» → **EGP Aprueba** |
| `SIM-05.2` | 25 | HU-FE | `PATCH /actualizarFactura` | Modal «Aprobación EGP» → **Rechazar c/ motivo** y **Rechazar s/ motivo** |

---

## 14. Definition of Ready / Definition of Done

### 14.1 Definition of Ready (para tomar una historia en un sprint)

1. La historia tiene actor concreto, capacidad observable y beneficio explícito.
2. Los criterios de aceptación están numerados y son verificables en demo con un sí o un no.
3. Los `MSG-Cxx` que la historia referencia están **redactados y aprobados**; ninguna historia entra a sprint con mensajes marcados como *pendiente*.
4. Las `RN-Cxx` que la historia referencia están confirmadas por el PO del cliente.
5. Los spikes que la bloquean (columna «Bloquea» de §10) están **cerrados**.
6. El contrato de los endpoints que consume está acordado con el equipo de backend, incluida la tabla de errores.
7. Los umbrales y parámetros de negocio que usa están definidos y con valor inicial acordado (`TAR-C01`).
8. La historia está estimada por el equipo y su tamaño entra en un sprint.
9. Están identificados los permisos que la gobiernan y el comportamiento esperado cuando el usuario no los tiene (`TAR-C02`).

### 14.2 Definition of Done (para dar una historia por terminada)

1. Todos los criterios de aceptación pasan en el ambiente de pruebas.
2. Los escenarios BDD están automatizados o, como mínimo, ejecutados y registrados por QA.
3. Los textos de la interfaz coinciden exactamente con el catálogo `MSG-Cxx`, sin variantes improvisadas.
4. Las transiciones de estado involucradas pasan por el motor `CON-09.1`; no hay cambios de estado por fuera de la máquina.
5. Las validaciones críticas están implementadas **también en el backend**, no solo en el front.
6. Los permisos correspondientes se aplican en FE y BE (`TAR-C02`).
7. Las acciones quedan registradas en auditoría (`TAR-C03`).
8. Los casos de error del endpoint están cubiertos y el front muestra un mensaje comprensible para cada uno.
9. La pantalla es accesible por teclado y los elementos interactivos tienen rótulo accesible.
10. La documentación del contrato de API está actualizada.
11. No hay divergencias abiertas con la POC sin registrar: si el comportamiento entregado difiere de la POC, la diferencia está documentada y aceptada por el PO.

