# Historias de Usuario — Épica CONFIRMING (Portal de Confirming · Banco Atlas)

> **Versión:** v1.0.0 · **Fecha:** 2026-08-11  
> **Fuente de requerimientos (solicitada):** `Confirming.xlsx` — **no adjunto en este run de Cloud Agent** (no apareció en `~/.cursor/projects/workspace/uploads/`).  
> **Fuente operativa usada para elaborar:** POC publicada https://marianaintive.github.io/atlas-confirming-poc/ — pantalla **Confirming** (`#confirming-view`), código `app.js` / `index.html`, más `assets/funcional_v1.0.0.md` §7.3 y `assets/tecnico_v1.0.0`.  
> **Autor:** PO (elaboración con skill `po-expert-user-stories`) · **Producto:** Portal de Confirming (Atlas Trade)  
> **Nota crítica:** Al no disponer del Excel, **no se inventó** la matriz fila-a-fila del archivo. El alcance **comprometido** de este documento es el comportamiento **ya implementado y demostrable** en la POC Confirming (flujos, validaciones, mensajes). Cuando se adjunte `Confirming.xlsx`, se debe reconciliar §2 (inclusión/desestimación), keys Jira y tachados, sin mezclar recomendaciones.

---

## Tabla de contenidos

1. [Criterio de elaboración y alcance](#1-criterio-de-elaboración-y-alcance)
2. [Matriz de inclusión (pendiente de Excel) y mapa POC](#2-matriz-de-inclusión-pendiente-de-excel-y-mapa-poc)
3. [Contexto de solución, actores y supuestos](#3-contexto-de-solución-actores-y-supuestos)
4. [Reglas de negocio transversales (RN)](#4-reglas-de-negocio-transversales-rn)
5. [Catálogo de mensajes de UI](#5-catálogo-de-mensajes-de-ui)
6. [Historias de usuario funcionales (tarjetas de backlog)](#6-historias-de-usuario-funcionales-tarjetas-de-backlog)
7. [Historias técnicas — Endpoints BFF / BE (enablers)](#7-historias-técnicas--endpoints-bff--be-enablers)
8. [Tareas técnicas / habilitadores](#8-tareas-técnicas--habilitadores)
9. [Spikes y decisiones pendientes](#9-spikes-y-decisiones-pendientes)
10. [Recomendaciones del PO — gaps vs catálogo de permisos / Excel](#10-recomendaciones-del-po--gaps-vs-catálogo-de-permisos--excel)
11. [Observaciones de consistencia (POC vs funcional vs Excel)](#11-observaciones-de-consistencia-poc-vs-funcional-vs-excel)
12. [Matriz de trazabilidad HU ↔ endpoint ↔ pantalla POC](#12-matriz-de-trazabilidad-hu--endpoint--pantalla-poc)
13. [Definition of Ready / Definition of Done](#13-definition-of-ready--definition-of-done)

---

## 1. Criterio de elaboración y alcance

| Criterio | Decisión aplicada |
|----------|-------------------|
| **Excel `Confirming.xlsx`** | **No disponible.** §2 queda como plantilla de reconciliación. No se inventan filas, tachados ni Issue Keys del Excel. |
| **POC Confirming** | **Fuente de verdad FE** para flujos, validaciones, tooltips y mensajes literales demostrables en la pantalla Confirming. |
| **Documento funcional v1.0.0** | Referencia histórica; **donde diverge de la POC vigente, prevalece la POC** (p. ej. estados Pagada/Mora, aprobación banco manual, Ejecutar → Financiada directa). Ver §11. |
| **Historias faltantes / stubs de UI** | Se listan en §10 como **recomendación**, no como alcance comprometido. |
| **Identificadores** | Keys propuestas `CO-xx` (Confirming). Al reconciliar con Excel/Jira, mapear a los Issue Keys reales. |
| **Idioma y formato** | Español; tarjeta PO + AC numerados + Gherkin con keywords en español (`Característica`, `Antecedentes`, `Escenario`, `Dado`, `Cuando`, `Entonces`, `Y`). |

**Convención de tipos**

| Tipo | Significado |
|------|-------------|
| `HU-FE` | Historia con impacto principal en Front End (pantalla Confirming). |
| `HU-BE` | Valor vía proceso/sistema (p. ej. CORE BANKING) sin pantalla propia. |
| `HT` | Historia técnica (endpoint BFF/BE). |
| `TAREA` | Habilitador de infraestructura / configuración. |

---

## 2. Matriz de inclusión (pendiente de Excel) y mapa POC

### 2.1 Plantilla de reconciliación con `Confirming.xlsx`

> Completar cuando el archivo esté adjunto (misma mecánica que LOGIN: tachadas → desestimar; puntuadas → elaborar).

| Fila Excel | Key Excel | Summary | Tipo | Estado | Motivo |
|-----------:|-----------|---------|------|--------|--------|
| — | — | *(pendiente de adjuntar Confirming.xlsx)* | — | ⏳ Pendiente | Archivo no recibido en el run |

### 2.2 Mapa de capacidades Confirming en la POC (alcance elaborado)

| Key propuesto | Capacidad (POC) | Tipo | Estado | Pantalla / modal POC |
|---------------|-----------------|------|--------|----------------------|
| **CO-01** | Ver Confirming: pestañas, filtros, grilla, empty state | HU-FE | ✅ Elaborada | `#confirming-view` |
| **CO-02** | Panel informativo del ente operativo | HU-FE | ✅ Elaborada | `#operating-entity-panel` + topbar |
| **CO-03** | Cargar factura manual + regla 30 días | HU-FE | ✅ Elaborada | `#new-invoice-modal` |
| **CO-04** | Escanear factura (QR demo) | HU-FE | ✅ Elaborada | scan en modal nueva factura |
| **CO-05** | Carga masiva (.xls/.xlsx/.csv) + resultado | HU-FE | ✅ Elaborada | bulk + `#bulk-upload-result-modal` |
| **CO-06** | Editar fecha de pago / elegibilidad | HU-FE | ✅ Elaborada | `#edit-fecha-pago-modal` |
| **CO-07** | Habilitar facturas (selección) | HU-FE | ✅ Elaborada | `#btn-habilitar-facturas` |
| **CO-08** | Bloquear facturas (selección) | HU-FE | ✅ Elaborada | `#btn-bloquear-facturas` |
| **CO-09** | Simular adelanto individual | HU-FE | ✅ Elaborada | `#simulate-modal` modo `simulate` |
| **CO-10** | Simular adelanto masivo (≥2, misma combinatoria) | HU-FE | ✅ Elaborada | modo `bulk-simulate` |
| **CO-11** | Aprobar adelanto EGP → desembolso automático | HU-FE | ✅ Elaborada | modo `approve-egp` |
| **CO-12** | Rechazar EGP con motivo (nueva fecha) | HU-FE | ✅ Elaborada | `btn-rechazar-egp-motivo` |
| **CO-13** | Rechazar EGP sin motivo → Bloqueada | HU-FE | ✅ Elaborada | `btn-rechazar-egp-sin-motivo` |
| **CO-14** | Desembolso CORE BANKING (éxito / error) | HU-BE | ✅ Elaborada | transición automática |
| **CO-15** | Eliminar factura | HU-FE | ✅ Elaborada | columna Eliminar |
| **CO-16** | Descargar template de carga masiva | HU-FE | ✅ Elaborada | `downloadInvoiceTemplate` |
| **CO-20…CO-30** | Endpoints BFF/BE propuestos | HT | ✅ Elaboradas | §7 |
| **CO-T01…** | Tareas habilitadoras | TAREA | ✅ Incluidas | §8 |

**Resumen POC:** **15 HU** · **11 HT** · **3 TAREA** · spikes §9 · recomendaciones §10.

---

## 3. Contexto de solución, actores y supuestos

### 3.1 Actores

| Actor | Dominio | Job en Confirming (POC) |
|-------|---------|-------------------------|
| Operador / Admin Banco | BANCO | Supervisar grilla, operar todas las facturas (en POC sin chequeo runtime de permisos) |
| Operador EGP | EGP | Habilitar/bloquear, aprobar/rechazar adelantos de sus facturas |
| Operador Proveedor | Proveedor | Consultar / simular según permisos (catálogo ABM; runtime pendiente — R-01) |
| Sistema / CORE BANKING | — | Desembolso automático tras aprobación EGP |

### 3.2 Componentes

- **FE:** SPA Portal Confirming — vista `#confirming-view`.
- **BFF Confirming (propuesto):** contratos orientados a UI (filtros, acciones masivas, ticket de simulación).
- **BE Confirming / Facturas (propuesto):** máquina de estados, elegibilidad, persistencia.
- **CORE BANKING (simulado en POC):** desembolso con delay y tasa de error.

### 3.3 Supuestos

| # | Supuesto |
|---|----------|
| SUP-01 | La **fecha de pago** es la fuente de verdad de elegibilidad operativa (≥ 30 días calendario desde hoy). |
| SUP-02 | Tras **EGP aprueba**, la aprobación bancaria es **automática** (no hay estado “Pendiente aprobación banco” en la POC vigente). |
| SUP-03 | Simulación masiva exige **misma combinatoria** EGP + Proveedor + Moneda y ≥ 2 facturas **Habilitada**. |
| SUP-04 | Los permisos del catálogo ABM Confirming (21 ítems) **aún no se aplican en runtime** en la POC; el producto productivo debe hacerlo (R-01). |
| SUP-05 | Los keys `CO-xx` son **propuestos** hasta mapear contra `Confirming.xlsx` / Jira. |

---

## 4. Reglas de negocio transversales (RN)

| ID | Regla | Fuente POC |
|----|-------|------------|
| **RN-C01** | Estados vigentes: Pendiente, Habilitada, Bloqueada, Pendiente aprobación EGP, Pendiente de desembolso, Financiada, Vencida, NO ELEGIBLE. | `INVOICE_STATES` |
| **RN-C02** | Pestañas: **Vigentes** = Pendiente, Habilitada, Bloqueada, Pendiente aprobación EGP, Pendiente de desembolso; **No vigentes** = Financiada, Vencida; **No operables** = NO ELEGIBLE. | `INVOICE_STATES_BY_VIEW_TAB` |
| **RN-C03** | Elegibilidad: `fechaPago` a **≥ 30 días** calendario desde hoy (`PAYMENT_DATE_MIN_DAYS`). Si no, estado **NO ELEGIBLE**. | `isPaymentDateEligible` |
| **RN-C04** | Alta (manual/masiva): `resolveInitialInvoiceState` fuerza NO ELEGIBLE si la fecha no es elegible, aunque el estado solicitado sea otro. | `resolveInitialInvoiceState` |
| **RN-C05** | Habilitar (masivo): solo desde Pendiente o Bloqueada → Habilitada. | `HABILITAR_VALID_STATES` |
| **RN-C06** | Bloquear (masivo): solo desde Pendiente o Habilitada → Bloqueada. | `BLOQUEAR_VALID_STATES` |
| **RN-C07** | Simular: factura(s) en Habilitada → Pendiente aprobación EGP. Masivo: ≥2, mismo EGP+Proveedor+Moneda, selección 100% Habilitada. | `simularSelectedInvoices`, `btn-execute-adelanto` |
| **RN-C08** | EGP aprueba → Pendiente de desembolso + disparo CORE BANKING. EGP rechaza **con motivo** → Habilitada o NO ELEGIBLE según nueva fecha. EGP rechaza **sin motivo** → Bloqueada. | listeners EGP |
| **RN-C09** | CORE BANKING: éxito → Financiada; error → vuelve a Pendiente aprobación EGP (reintento). POC: delay 2,5 s; error ~15%. | `scheduleCoreBankingDisbursement` |
| **RN-C10** | Cálculo adelanto: interés = monto × TNA × días/365; comisión = monto × %; IVA = (interés+comisión)×%; neto = monto − interés − comisión − IVA. Defaults si falta config EGP: 12% / 1,5% / 10%. | `recalculateSimulation` |
| **RN-C11** | Selección múltiple: ancla EGP+Proveedor+Moneda de la primera factura; el resto debe coincidir. | `getSelectionAnchorCombo` |
| **RN-C12** | Fecha de pago editable en: Pendiente, Habilitada, Bloqueada, NO ELEGIBLE. | `FECHA_PAGO_EDITABLE_STATES` |
| **RN-C13** | Filtro ente topbar: muestra facturas donde EGP **o** Proveedor coincide con el ente seleccionado. | `invoiceMatchesOperatingEntity` |

---

## 5. Catálogo de mensajes de UI

Mensajes **literales** (o plantilla) tomados de la POC. Referenciar `MSG-Cxx` en AC/BDD.

| Código | Contexto | Mensaje / título |
|--------|----------|------------------|
| MSG-C01 | Empty state grilla | "No se encontraron facturas con los filtros aplicados." |
| MSG-C02 | Campos obligatorios alta | "Por favor complete todos los campos obligatorios." |
| MSG-C03 | Alta OK | "La factura ha sido registrada exitosamente." / título `Factura Registrada` |
| MSG-C04 | Alta NO ELEGIBLE | "La factura fue registrada en estado NO ELEGIBLE: la fecha de pago debe estar a 30 días o más desde hoy." |
| MSG-C05 | QR OK | "Factura leída correctamente desde código QR." |
| MSG-C06 | Tooltip habilitar inválido | "Solo pueden habilitarse facturas en estado Bloqueada o Pendiente" |
| MSG-C07 | Tooltip habilitar vacío | "Seleccione facturas en estado Bloqueada o Pendiente para habilitar" |
| MSG-C08 | Tooltip bloquear inválido | "Solo pueden bloquearse facturas en estado Habilitada o Pendiente" |
| MSG-C09 | Tooltip bloquear vacío | "Seleccione facturas en estado Habilitada o Pendiente para bloquear" |
| MSG-C10 | Tooltip simular inválido | "Seleccione 2 o más facturas Habilitada con mismo EGP, Proveedor y Moneda" |
| MSG-C11 | Tooltip simular vacío | "Seleccione al menos 2 facturas Habilitada (misma combinatoria) para simular" |
| MSG-C12 | Confirm habilitar 1 | "¿Confirma habilitar la factura {id}? Pasará al estado \"Habilitada\"." |
| MSG-C13 | Habilitar OK | "La factura fue habilitada correctamente." / "N facturas fueron habilitadas correctamente." |
| MSG-C14 | Confirm bloquear 1 | "¿Confirma bloquear la factura {id}? Pasará al estado \"Bloqueada\"." |
| MSG-C15 | Bloquear OK | "La factura fue bloqueada correctamente." / "N facturas fueron bloqueadas correctamente." |
| MSG-C16 | Confirm adelanto 1 | "¿Confirma solicitar el adelanto de la factura {id}?\n\nMonto neto estimado: …\nPasará a \"Pendiente aprobación EGP\"." |
| MSG-C17 | Adelanto enviado | "La solicitud de adelanto para la factura {id} fue enviada al EGP. Estado: \"Pendiente aprobación EGP\"." |
| MSG-C18 | Simulación masiva OK | "N facturas enviadas a aprobación EGP." |
| MSG-C19 | Hint approve-egp | "Al aprobar, el banco aprueba la TX automáticamente y la factura pasa a Pendiente de desembolso." |
| MSG-C20 | EGP aprobó | "EGP aprobó el adelanto. La aprobación bancaria es automática: la factura {id} pasa a \"Pendiente de desembolso\"." |
| MSG-C21 | EGP rechazó con motivo | "El EGP rechazó con motivo. La factura {id} vuelve a Habilitada\|queda en NO ELEGIBLE (fecha de pago menor a 30 días) (fecha de pago: …)." |
| MSG-C22 | EGP rechazó sin motivo | "El EGP rechazó sin motivo. La factura {id} pasa a estado Bloqueada." |
| MSG-C23 | CORE error | "La API CORE BANKING reportó un ERROR al desembolsar la factura {id}. La factura vuelve a \"Pendiente aprobación EGP\" para reintentar." |
| MSG-C24 | CORE OK | "Desembolso completado por CORE BANKING. La factura {id} pasa a estado \"Financiada\"." |
| MSG-C25 | Fecha inválida | "Indique una fecha de pago válida (dd-mm-yyyy)." |
| MSG-C26 | Warning sale de Vigentes | "La fecha de pago indicada (…) está a menos de 30 días desde hoy.\n\nLa factura {id} quedará No Operable (NO ELEGIBLE) y dejará de estar en Vigentes.\n\n¿Desea guardar de todos modos?" |
| MSG-C27 | Fecha actualizada | Variantes: sigue NO ELEGIBLE / pasó a No Operables / volvió a Habilitada / quedó en fecha. Título `Fecha de pago actualizada`. |
| MSG-C28 | Eliminar confirm | "¿Confirma eliminar la factura {id} ({egp} – {prov})? Esta acción no se puede deshacer." |
| MSG-C29 | Eliminar OK | "La factura fue eliminada correctamente." |
| MSG-C30 | Template fallido | "No se pudo generar el template (librería de Excel no disponible)." |
| MSG-C31 | Formato fecha rechazo | "Formato de fecha inválido. Use dd-mm-yyyy." |
| MSG-C32 | Modal simulación roto | "No se pudo abrir el modal de simulación." |
| MSG-C33 | Hint simulate | "Revise el cálculo del adelanto. Al ejecutar, la solicitud pasa a Pendiente aprobación EGP." |
| MSG-C34 | Hint bulk-simulate | "Revise el cálculo. Al ejecutar, todas las facturas seleccionadas pasan a Pendiente aprobación EGP." |

---

## 6. Historias de usuario funcionales (tarjetas de backlog)

> Formato skill `po-expert-user-stories`. Escenarios fuente: comportamiento observado en la POC (y, cuando exista, transcripción del Excel).

---

### CO-01 — Consultar facturas Confirming (pestañas, filtros y grilla)

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador Banco / EGP / Proveedor con acceso a Confirming |
| **Dominios** | BANCO, EGP, Proveedor |
| **Prioridad sugerida** | Must |
| **Depende de** | Login / sesión |
| **Habilita** | CO-02…CO-16 |
| **Pantalla POC** | `#confirming-view` · tabs Vigentes / No vigentes / No operables |

#### Historia
Como operador del Portal de Confirming  
quiero ver las facturas organizadas por vigencia y filtrarlas  
para localizar rápidamente las que debo operar o consultar

#### Valor de negocio
Sin una grilla filtrable por pestaña y criterios, el ciclo de confirming no es operable a escala.

#### Escenarios fuente
> POC: pestañas `INVOICE_VIEW_TABS`; filtros buscar / vencimiento / fecha de pago / estado; empty state MSG-C01; filtro ente topbar (RN-C13).

#### Criterios de aceptación
1. **[Feliz]** Al entrar a Confirming veo la pestaña **Facturas Vigentes** activa con facturas de estados RN-C02.
2. **[Feliz]** Puedo cambiar a **No vigentes** y **No operables** y solo veo los estados correspondientes (RN-C02).
3. **[Feliz]** Filtros de búsqueda (nro/EGP/Proveedor), fecha vencimiento, fecha de pago y estado se combinan con la pestaña y el ente operativo.
4. **[Alternativo]** Sin resultados: MSG-C01.
5. **[Validación]** El filtro de estado ofrece los estados de RN-C01 (+ “Todos”).

#### Escenarios BDD
```gherkin
Característica: Consulta de facturas en Confirming
  Antecedentes:
    Dado estoy autenticado en el Portal de Confirming
    Y navego a la sección "Confirming"

  Escenario: Pestaña Vigentes por defecto
    Entonces veo la pestaña "Facturas Vigentes" seleccionada
    Y la grilla solo incluye estados de Vigentes según RN-C02

  Escenario: Cambiar a No operables
    Cuando selecciono la pestaña "Facturas No Operables"
    Entonces solo veo facturas en estado "NO ELEGIBLE"

  Escenario: Sin resultados con filtros
    Cuando aplico filtros que no coinciden con ninguna factura
    Entonces veo el mensaje MSG-C01
```

#### Fuera de alcance
- Paginación server-side, exportación de grilla (R-05), permisos runtime por rol (R-01).

#### Notas / preguntas abiertas
- Reconciliar columnas y filtros con `Confirming.xlsx` cuando esté disponible.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CO-02 — Panel del ente operativo

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador que selecciona un ente en el topbar |
| **Dominios** | BANCO, EGP, Proveedor |
| **Prioridad sugerida** | Must |
| **Depende de** | CO-01, ABM entes |
| **Habilita** | Decisiones de simulación (TNA/comisión/IVA) |
| **Pantalla POC** | `#operating-entity-panel` · `#operating-entity-select` |

#### Historia
Como operador  
quiero ver los datos crediticios del ente con el que estoy operando  
para validar límites y tasas antes de adelantar

#### Valor de negocio
Reduce errores de operación al exponer TNA, comisión, IVA, línea y monedas junto a la grilla filtrada.

#### Escenarios fuente
> POC: panel oculto con “Todos los entes”; visible con ente seleccionado; campos Razón Social, RUC, Límite, TNA, Comisión, IVA, monedas; `refreshConfirmingView`.

#### Criterios de aceptación
1. **[Feliz]** Con ente seleccionado, el panel muestra razón, RUC, límite, TNA, comisión, IVA y monedas.
2. **[Alternativo]** Con “Todos los entes”, el panel está oculto y la grilla no filtra por ente.
3. **[Feliz]** Al cambiar el ente, se refrescan panel y grilla (RN-C13).

#### Escenarios BDD
```gherkin
Característica: Panel informativo del ente operativo
  Escenario: Mostrar panel al seleccionar EGP
    Dado estoy en Confirming
    Cuando selecciono el ente "Retail S.A. (EGP)"
    Entonces veo el panel del ente con TNA y monedas habilitadas
    Y la grilla solo muestra facturas de ese EGP o asociadas

  Escenario: Ocultar panel con todos los entes
    Cuando selecciono "Todos los entes"
    Entonces el panel del ente no se muestra
```

#### Fuera de alcance
- Edición de parámetros del ente desde Confirming (se hace en ABM).

#### Notas / preguntas abiertas
- ¿El límite crediticio debe bloquear la simulación si se excede? (spike S-C02)

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CO-03 — Cargar factura manual

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador con permiso de carga manual |
| **Dominios** | BANCO, EGP |
| **Prioridad sugerida** | Must |
| **Depende de** | CO-01; catálogo EGP/Proveedor |
| **Habilita** | CO-07…CO-10 |
| **Pantalla POC** | `#new-invoice-modal` · `submitNewInvoice` |

#### Historia
Como operador EGP/Banco  
quiero registrar una factura con su fecha de pago  
para incorporarla a la máquina de estados de Confirming

#### Valor de negocio
Es el ingreso al ciclo operativo; sin alta no hay habilitación ni adelanto.

#### Escenarios fuente
> POC: campos nro, EGP, proveedor, emisión, vto, fecha pago, moneda, monto, estado inicial; validación obligatorios; RN-C03/C04; MSG-C02/C03/C04; fecha pago default = vto.

#### Criterios de aceptación
1. **[Feliz]** Completo campos obligatorios con fecha de pago ≥ 30 días → se registra en el estado solicitado y MSG-C03.
2. **[Error]** Faltan obligatorios → MSG-C02 y no se guarda.
3. **[Validación]** Fecha de pago &lt; 30 días → se registra como **NO ELEGIBLE** con MSG-C04 (RN-C04), aunque el estado inicial pedido sea otro.
4. **[Alternativo]** Si no toqué fecha de pago, hereda el vencimiento.

#### Escenarios BDD
```gherkin
Característica: Alta manual de factura
  Antecedentes:
    Dado estoy en Confirming
    Y abro "Cargar Factura"

  Escenario: Alta exitosa operable
    Cuando completo nro, emisión, vencimiento, fecha de pago a 45 días, monto y guardo
    Entonces la factura aparece en Vigentes en el estado inicial elegido
    Y veo MSG-C03

  Escenario: Campos incompletos
    Cuando intento guardar sin monto
    Entonces veo MSG-C02
    Y la factura no se crea

  Escenario: Fecha de pago no elegible
    Cuando indico fecha de pago a 10 días desde hoy y guardo
    Entonces la factura queda en estado "NO ELEGIBLE"
    Y veo MSG-C04
```

#### Fuera de alcance
- Edición posterior de datos de factura cargados (R-04); integración ERP real.

#### Notas / preguntas abiertas
- Validar unicidad de nro. de factura por EGP en BE (no en POC).

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CO-04 — Escanear factura (QR demo)

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador en alta manual |
| **Dominios** | BANCO, EGP |
| **Prioridad sugerida** | Could |
| **Depende de** | CO-03 |
| **Habilita** | Precarga de formulario |
| **Pantalla POC** | `simulateScan` · overlay “Escaneando documento...” |

#### Historia
Como operador  
quiero precargar datos de factura desde un escaneo  
para agilizar la carga manual

#### Valor de negocio
Reduce tiempo de captura; en POC es simulación demostrativa.

#### Escenarios fuente
> POC: overlay 2 s; autocompleta nro/EGP/proveedor/fechas/monto; MSG-C05.

#### Criterios de aceptación
1. **[Feliz]** Al escanear, veo overlay y luego campos precargados + MSG-C05.
2. **[Alternativo]** Puedo editar los campos antes de guardar (sigue CO-03).

#### Escenarios BDD
```gherkin
Característica: Precarga por escaneo QR (demo)
  Escenario: Escaneo exitoso
    Dado el modal de nueva factura está abierto
    Cuando elijo escanear factura
    Entonces veo "Escaneando documento..."
    Y al finalizar los campos quedan precargados
    Y veo MSG-C05
```

#### Fuera de alcance
- OCR/QR real de facturas paraguayas (spike S-C03).

#### Notas / preguntas abiertas
- Confirmar si el Excel exige escaneo real o solo demo.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ |

---

### CO-05 — Carga masiva de facturas

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador con permiso de carga masiva |
| **Dominios** | BANCO, EGP |
| **Prioridad sugerida** | Must |
| **Depende de** | CO-16, CO-03 (mismas reglas de estado) |
| **Habilita** | Operación por lote |
| **Pantalla POC** | `handleBulkInvoiceFile` · `#bulk-upload-result-modal` |

#### Historia
Como operador  
quiero cargar muchas facturas desde Excel/CSV  
para incorporar carteras sin carga una a una

#### Valor de negocio
Habilita onboarding de volumen típico de confirming.

#### Escenarios fuente
> POC: `.xls/.xlsx/.csv`; columnas `BULK_INVOICE_HEADERS`; moneda debe estar habilitada en el EGP; estados de entrada Pendiente/Habilitada/Bloqueada; RN-C04; modal de resultado con cargadas / incompletas / moneda inválida.

#### Criterios de aceptación
1. **[Feliz]** Archivo válido → se cargan filas completas y veo resumen de procesadas/cargadas.
2. **[Error]** Filas incompletas o monto ≤ 0 → no se cargan; se listan como incompletas.
3. **[Error]** Moneda no habilitada para el EGP → no se cargan; sección “moneda no habilitada”.
4. **[Validación]** Fecha de pago &lt; 30 días → factura cargada como NO ELEGIBLE (RN-C04).
5. **[Alternativo]** Archivo vacío → mensaje de sin filas.

#### Escenarios BDD
```gherkin
Característica: Carga masiva de facturas
  Escenario: Carga con observaciones
    Dado un Excel con filas válidas, incompletas y moneda inválida
    Cuando proceso el archivo en Confirming
    Entonces veo el modal de resultado con las tres secciones
    Y solo las filas válidas aparecen en la grilla

  Escenario: Fecha de pago corta en bulk
    Dado una fila válida con fecha de pago a 5 días
    Cuando proceso el archivo
    Entonces esa factura queda "NO ELEGIBLE"
```

#### Fuera de alcance
- Validación tributaria / CDC real; tamaño máximo a definir con BE.

#### Notas / preguntas abiertas
- Definir límite de filas y reporte descargable de rechazos (recomendación R-06).

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ |

---

### CO-06 — Editar fecha de pago y elegibilidad

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador con permiso de editar fecha de pago |
| **Dominios** | BANCO, EGP |
| **Prioridad sugerida** | Must |
| **Depende de** | CO-01 |
| **Habilita** | Recuperar facturas NO ELEGIBLE |
| **Pantalla POC** | `#edit-fecha-pago-modal` · `submitEditFechaPago` |

#### Historia
Como operador  
quiero corregir la fecha de pago de una factura  
para volverla operable o marcarla no operable según la regla de 30 días

#### Valor de negocio
Evita pérdidas operativas por fechas mal cargadas sin rehacer el alta.

#### Escenarios fuente
> POC: editable en RN-C12; warning MSG-C26 al salir de Vigentes; retorno NO ELEGIBLE→Habilitada; MSG-C25/C27.

#### Criterios de aceptación
1. **[Feliz]** Desde NO ELEGIBLE, fecha ≥ 30 días → pasa a **Habilitada** y pestaña Vigentes + MSG-C27.
2. **[Alternativo]** Desde Vigentes, fecha &lt; 30 días → confirmación MSG-C26; al aceptar → NO ELEGIBLE / No operables.
3. **[Error]** Fecha inválida → MSG-C25.
4. **[Validación]** Solo estados RN-C12 muestran la acción.

#### Escenarios BDD
```gherkin
Característica: Edición de fecha de pago
  Escenario: Recuperar factura no operable
    Dado una factura en "NO ELEGIBLE"
    Cuando actualizo la fecha de pago a 40 días desde hoy
    Entonces la factura queda "Habilitada"
    Y veo la pestaña Vigentes

  Escenario: Advertencia al volver no operable
    Dado una factura "Habilitada"
    Cuando indico fecha de pago a 7 días
    Entonces veo la confirmación MSG-C26
    Y si confirmo la factura queda "NO ELEGIBLE"
```

#### Fuera de alcance
- Editar otros campos de la factura (R-04).

#### Notas / preguntas abiertas
- ¿Debe actualizar también el vencimiento siempre? POC alinea `vto` en rechazo EGP; en edit solo si no había vto.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CO-07 — Habilitar facturas

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador EGP/Banco |
| **Dominios** | BANCO, EGP |
| **Prioridad sugerida** | Must |
| **Depende de** | CO-01 |
| **Habilita** | CO-09, CO-10 |
| **Pantalla POC** | `#btn-habilitar-facturas` · `habilitarSelectedInvoices` |

#### Historia
Como operador EGP  
quiero habilitar facturas pendientes o bloqueadas  
para dejarlas listas para simular adelanto

#### Valor de negocio
Control del EGP sobre qué facturas entran al funnel de financiamiento.

#### Escenarios fuente
> POC: RN-C05; tooltips MSG-C06/C07; confirm MSG-C12; éxito MSG-C13.

#### Criterios de aceptación
1. **[Feliz]** Selección solo Pendiente/Bloqueada → confirmación → estado Habilitada + MSG-C13.
2. **[Validación]** Sin selección elegible → botón deshabilitado + MSG-C07.
3. **[Validación]** Selección mixta inválida → botón deshabilitado + MSG-C06.
4. **[Feliz]** Funciona para 1 o N facturas.

#### Escenarios BDD
```gherkin
Característica: Habilitar facturas
  Escenario: Habilitar una factura bloqueada
    Dado una factura en "Bloqueada" seleccionada
    Cuando confirmo habilitar
    Entonces la factura queda "Habilitada"
    Y veo MSG-C13

  Escenario: Botón deshabilitado con selección inválida
    Dado selecciono una factura "Financiada"
    Entonces el botón Habilitar está deshabilitado
    Y el tooltip indica MSG-C06
```

#### Fuera de alcance
- Habilitar desde acción de fila individual (POC solo masivo/cabecera).

#### Notas / preguntas abiertas
- Excel puede pedir habilitar individual: mapear al reconciliar.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CO-08 — Bloquear facturas

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador EGP/Banco |
| **Dominios** | BANCO, EGP |
| **Prioridad sugerida** | Must |
| **Depende de** | CO-01 |
| **Habilita** | Contención operativa |
| **Pantalla POC** | `#btn-bloquear-facturas` |

#### Historia
Como operador EGP  
quiero bloquear facturas pendientes o habilitadas  
para impedir que se solicite adelanto indebido

#### Valor de negocio
Freno operativo ante disputa, fraude o datos incorrectos.

#### Escenarios fuente
> POC: RN-C06; MSG-C08/C09/C14/C15.

#### Criterios de aceptación
1. **[Feliz]** Selección Pendiente/Habilitada → confirmación → Bloqueada + MSG-C15.
2. **[Validación]** Tooltips MSG-C08/C09 cuando no aplica.
3. **[Feliz]** 1 o N facturas.

#### Escenarios BDD
```gherkin
Característica: Bloquear facturas
  Escenario: Bloquear factura habilitada
    Dado una factura "Habilitada" seleccionada
    Cuando confirmo bloquear
    Entonces queda "Bloqueada"
    Y veo MSG-C15
```

#### Fuera de alcance
- Bloqueo automático por mora (no implementado).

#### Notas / preguntas abiertas
- —

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CO-09 — Simular y solicitar adelanto (individual)

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador con permiso de simular |
| **Dominios** | BANCO, EGP, Proveedor (según permiso) |
| **Prioridad sugerida** | Must |
| **Depende de** | CO-02 (tasas), CO-07 |
| **Habilita** | CO-11…CO-14 |
| **Pantalla POC** | `#simulate-modal` modo `simulate` · `recalculateSimulation` |

#### Historia
Como operador  
quiero simular el neto a acreditar de una factura habilitada y solicitar el adelanto  
para que el EGP lo apruebe con costos transparentes

#### Valor de negocio
Transparencia de pricing (TNA/comisión/IVA) antes de comprometer el desembolso.

#### Escenarios fuente
> POC: solo Habilitada; ticket RN-C10; hint MSG-C33; confirm MSG-C16; éxito MSG-C17; monto no supera factura; moneda editable solo si EGP multimoneda.

#### Criterios de aceptación
1. **[Feliz]** Desde Habilitada abro simulación, veo ticket (días, interés, comisión, IVA, neto) y MSG-C33.
2. **[Feliz]** Confirmo ejecutar → Pendiente aprobación EGP + MSG-C17.
3. **[Validación]** Monto a adelantar no puede superar el monto de la factura.
4. **[Alternativo]** Si hay ≥2 Habilitada seleccionadas, el Simular de fila se deshabilita (usar masivo CO-10).
5. **[Error]** Si el modal no inicializa → MSG-C32.

#### Escenarios BDD
```gherkin
Característica: Simulación individual de adelanto
  Antecedentes:
    Dado una factura en estado "Habilitada"
    Y el EGP tiene TNA, comisión e IVA configurados

  Escenario: Solicitar adelanto
    Cuando abro Simular y confirmo el adelanto
    Entonces la factura pasa a "Pendiente aprobación EGP"
    Y veo MSG-C17
    Y el ticket mostró el monto neto según RN-C10

  Escenario: Tope de monto
    Cuando intento adelantar más que el monto de la factura
    Entonces el sistema ajusta el monto al máximo de la factura
```

#### Fuera de alcance
- Desembolso inmediato sin aprobación EGP.

#### Notas / preguntas abiertas
- ¿Adelanto parcial siempre permitido? POC sí (monto editable).

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CO-10 — Simular adelanto masivo

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador con permiso de simular |
| **Dominios** | BANCO, EGP |
| **Prioridad sugerida** | Must |
| **Depende de** | CO-09, RN-C07, RN-C11 |
| **Habilita** | CO-11 |
| **Pantalla POC** | `#btn-simular-facturas` · modo `bulk-simulate` |

#### Historia
Como operador  
quiero simular un adelanto para varias facturas de la misma combinatoria  
para operar carteras homogéneas en un solo paso

#### Valor de negocio
Eficiencia operativa en lotes del mismo EGP/Proveedor/Moneda.

#### Escenarios fuente
> POC: ≥2 Habilitada, misma combinatoria; tooltips MSG-C10/C11; monto=suma; moneda/monto readonly; MSG-C18/C34.

#### Criterios de aceptación
1. **[Feliz]** ≥2 Habilitada misma combinatoria → modal masivo, ticket agregado, al ejecutar todas a Pendiente aprobación EGP + MSG-C18.
2. **[Validación]** Botón deshabilitado si no cumple → MSG-C10/C11.
3. **[Validación]** No puedo mezclar combinatorias en la selección (RN-C11).

#### Escenarios BDD
```gherkin
Característica: Simulación masiva de adelanto
  Escenario: Lote homogéneo
    Dado 3 facturas "Habilitada" del mismo EGP, proveedor y moneda
    Cuando selecciono las 3 y confirmo Simular
    Entonces las 3 pasan a "Pendiente aprobación EGP"
    Y veo MSG-C18

  Escenario: Combinatoria inválida
    Dado selecciono facturas de distintos proveedores
    Entonces no puedo completar la selección heterogénea
    Y Simular permanece deshabilitado con MSG-C10
```

#### Fuera de alcance
- Simular monedas mixtas en un solo ticket.

#### Notas / preguntas abiertas
- Días a adelantar en bulk usan vto de la factura ancla (comportamiento POC): validar con negocio.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CO-11 — Aprobar adelanto (EGP)

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Aprobador EGP |
| **Dominios** | EGP, BANCO (supervisión) |
| **Prioridad sugerida** | Must |
| **Depende de** | CO-09/CO-10 |
| **Habilita** | CO-14 |
| **Pantalla POC** | modo `approve-egp` · `btn-aprobar-egp` |

#### Historia
Como aprobador EGP  
quiero aprobar la solicitud de adelanto  
para disparar el desembolso automático hacia el proveedor

#### Valor de negocio
Gate de control del pagador antes de comprometer fondos/línea.

#### Escenarios fuente
> POC: MSG-C19/C20; estado → Pendiente de desembolso; dispara CORE (CO-14). Aprobación banco automática (SUP-02).

#### Criterios de aceptación
1. **[Feliz]** Desde Pendiente aprobación EGP, apruebo → Pendiente de desembolso + MSG-C20 + hint MSG-C19.
2. **[Feliz]** Se inicia el proceso de desembolso CORE (CO-14).
3. **[Validación]** Moneda/monto en este modo son de solo lectura.

#### Escenarios BDD
```gherkin
Característica: Aprobación EGP del adelanto
  Escenario: Aprobación con desembolso automático
    Dado una factura en "Pendiente aprobación EGP"
    Cuando el EGP aprueba
    Entonces la factura pasa a "Pendiente de desembolso"
    Y veo MSG-C20
    Y se dispara el desembolso CORE BANKING
```

#### Fuera de alcance
- Aprobación bancaria manual (R-02; código residual en POC).

#### Notas / preguntas abiertas
- ¿Doble firma EGP? Catálogo menciona “Revertir 2da aprobación” (R-03).

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CO-12 — Rechazar adelanto EGP con motivo

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Aprobador EGP |
| **Dominios** | EGP |
| **Prioridad sugerida** | Must |
| **Depende de** | CO-11 (mismo modal) |
| **Habilita** | Reintento de simulación / corrección de fecha |
| **Pantalla POC** | `btn-rechazar-egp-motivo` |

#### Historia
Como aprobador EGP  
quiero rechazar con una nueva fecha de pago  
para devolver la factura al circuito operable o no operable según elegibilidad

#### Valor de negocio
Permite renegociar plazo sin bloquear definitivamente.

#### Escenarios fuente
> POC: prompt fecha dd-mm-yyyy; RN-C08; MSG-C21/C31.

#### Criterios de aceptación
1. **[Feliz]** Nueva fecha ≥ 30 días → Habilitada + MSG-C21.
2. **[Alternativo]** Nueva fecha &lt; 30 días → NO ELEGIBLE + MSG-C21.
3. **[Error]** Formato inválido → MSG-C31 y no cambia estado.
4. **[Alternativo]** Cancelar el prompt → sin cambios.

#### Escenarios BDD
```gherkin
Característica: Rechazo EGP con motivo
  Escenario: Nueva fecha operable
    Dado una factura en "Pendiente aprobación EGP"
    Cuando rechazo con motivo e indico fecha a 45 días
    Entonces la factura vuelve a "Habilitada"

  Escenario: Fecha inválida
    Cuando ingreso "32-13-2026"
    Entonces veo MSG-C31
    Y el estado no cambia
```

#### Fuera de alcance
- Captura estructurada del “motivo” textual (POC solo pide fecha). Recomendación R-07.

#### Notas / preguntas abiertas
- Reemplazar `window.prompt` por modal accesible en producto.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CO-13 — Rechazar adelanto EGP sin motivo

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Aprobador EGP |
| **Dominios** | EGP |
| **Prioridad sugerida** | Must |
| **Depende de** | CO-11 |
| **Habilita** | Contención |
| **Pantalla POC** | `btn-rechazar-egp-sin-motivo` |

#### Historia
Como aprobador EGP  
quiero rechazar sin motivo  
para bloquear la factura y evitar reintentos inmediatos

#### Valor de negocio
Cierra el caso ante rechazo duro (fraude, disputa, política).

#### Escenarios fuente
> POC: estado → Bloqueada; MSG-C22.

#### Criterios de aceptación
1. **[Feliz]** Rechazo sin motivo → Bloqueada + MSG-C22.
2. **[Feliz]** La factura deja de ser simulable hasta re-habilitar (CO-07).

#### Escenarios BDD
```gherkin
Característica: Rechazo EGP sin motivo
  Escenario: Bloqueo por rechazo
    Dado una factura en "Pendiente aprobación EGP"
    Cuando rechazo sin motivo
    Entonces la factura queda "Bloqueada"
    Y veo MSG-C22
```

#### Fuera de alcance
- Notificación automática al proveedor (ABM Notificaciones — otra épica).

#### Notas / preguntas abiertas
- —

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CO-14 — Desembolso CORE BANKING (éxito / error)

| | |
|---|---|
| **Tipo** | HU-BE |
| **Épica** | CONFIRMING |
| **Actor** | Sistema (CORE BANKING) · visibilidad para operador |
| **Dominios** | BANCO, EGP, Proveedor |
| **Prioridad sugerida** | Must |
| **Depende de** | CO-11 |
| **Habilita** | Factura Financiada / reintento EGP |
| **Pantalla POC** | `scheduleCoreBankingDisbursement` (feedback por alerta) |

#### Historia
Como sistema de Confirming  
quiero concretar o fallar el desembolso contra CORE BANKING  
para acreditar al proveedor o devolver la factura a reintento EGP

#### Valor de negocio
Cierra el ciclo financiero con trazabilidad de éxito/error.

#### Escenarios fuente
> POC: RN-C09; MSG-C23/C24; hint “CORE BANKING desembolsando…”.

#### Criterios de aceptación
1. **[Feliz]** Desembolso OK → Financiada + MSG-C24 (No vigentes).
2. **[Error]** Error CORE → vuelve a Pendiente aprobación EGP + MSG-C23.
3. **[Validación]** Solo procesa si sigue en Pendiente de desembolso al momento del callback.

#### Escenarios BDD
```gherkin
Característica: Desembolso CORE BANKING
  Escenario: Acreditación exitosa
    Dado una factura en "Pendiente de desembolso"
    Cuando CORE BANKING responde OK
    Entonces la factura pasa a "Financiada"
    Y veo MSG-C24

  Escenario: Error de desembolso
    Dado una factura en "Pendiente de desembolso"
    Cuando CORE BANKING responde ERROR
    Entonces la factura vuelve a "Pendiente aprobación EGP"
    Y veo MSG-C23
```

#### Fuera de alcance
- Contabilidad / asientos; conciliación bancaria real.

#### Notas / preguntas abiertas
- Parametrizar timeout y política de reintentos (S-C01). La tasa 15% es solo demo POC.

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CO-15 — Eliminar factura

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador con permiso de baja |
| **Dominios** | BANCO, EGP |
| **Prioridad sugerida** | Should |
| **Depende de** | CO-01 |
| **Habilita** | Limpieza de errores de carga |
| **Pantalla POC** | `deleteInvoice` |

#### Historia
Como operador  
quiero eliminar una factura con confirmación  
para corregir cargas erróneas antes de financiar

#### Valor de negocio
Evita basura operativa en la grilla.

#### Escenarios fuente
> POC: MSG-C28/C29; acción irreversible en POC (memoria).

#### Criterios de aceptación
1. **[Feliz]** Confirmo eliminación → desaparece de la grilla + MSG-C29.
2. **[Alternativo]** Cancelar confirmación → sin cambios.
3. **[Validación]** Productivo: restringir eliminación a estados no financiados (propuesta PO; POC permite cualquier estado — ver notas).

#### Escenarios BDD
```gherkin
Característica: Eliminación de factura
  Escenario: Eliminar con confirmación
    Dado una factura visible en la grilla
    Cuando confirmo eliminarla
    Entonces deja de listarse
    Y veo MSG-C29
```

#### Fuera de alcance
- Soft-delete / auditoría completa (R-08).

#### Notas / preguntas abiertas
- POC permite borrar Financiada: **cerrar regla de negocio con Excel** (propuesta: solo Pendiente/Habilitada/Bloqueada/NO ELEGIBLE).

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### CO-16 — Descargar template de carga masiva

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Actor** | Operador de carga masiva |
| **Dominios** | BANCO, EGP |
| **Prioridad sugerida** | Should |
| **Depende de** | — |
| **Habilita** | CO-05 |
| **Pantalla POC** | `downloadInvoiceTemplate` → `template-facturas.xlsx` |

#### Historia
Como operador  
quiero descargar la plantilla oficial de facturas  
para completar el archivo sin errores de columnas

#### Valor de negocio
Estandariza el input y reduce rechazos de bulk.

#### Escenarios fuente
> POC: headers `BULK_INVOICE_HEADERS` + fila ejemplo; MSG-C30 si falta SheetJS.

#### Criterios de aceptación
1. **[Feliz]** Descargo `template-facturas.xlsx` con columnas oficiales y fila ejemplo.
2. **[Error]** Si no hay librería Excel → MSG-C30.

#### Escenarios BDD
```gherkin
Característica: Template de carga masiva
  Escenario: Descarga exitosa
    Dado el modal de nueva factura
    Cuando descargo el template
    Entonces obtengo un Excel con las columnas de carga masiva
```

#### Fuera de alcance
- Template versionado en CMS.

#### Notas / preguntas abiertas
- —

#### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## 7. Historias técnicas — Endpoints BFF / BE (enablers)

> Contratos **propuestos** (POC no tiene backend). Alinear con hoja API del Excel cuando exista. Prefijo orientativo `/v1/confirming` o `/api/v1/invoices` según `tecnico_v1.0.0`.

---

### CO-20 — GET · Listado de facturas (filtros / pestaña)

| | |
|---|---|
| **Tipo** | HT (enabler) |
| **Habilita** | CO-01, CO-02 |
| **Contrato** | `GET /api/v1/invoices?tab=&status=&q=&vto=&fechaPago=&enteId=` |

#### Objetivo técnico
Devolver facturas paginadas según pestaña RN-C02, filtros y ente operativo.

#### Criterios de aceptación
1. Filtra por tab/estado/texto/fechas/ente.
2. Respuesta incluye campos de grilla + `fechaPago` + `estado`.
3. 401 si sesión inválida.

#### Escenarios BDD
```gherkin
Característica: Listado de facturas
  Escenario: Filtro por tab no operables
    Cuando consulto GET /api/v1/invoices?tab=no-operables
    Entonces solo recibo facturas "NO ELEGIBLE"
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 401 | UNAUTHORIZED | Sesión inválida |
| 403 | FORBIDDEN | Sin permiso Ver Confirming |

---

### CO-21 — POST · Alta de factura

| | |
|---|---|
| **Tipo** | HT |
| **Habilita** | CO-03 |
| **Contrato** | `POST /api/v1/invoices` |

#### Objetivo técnico
Persistir factura aplicando RN-C03/C04.

#### Criterios de aceptación
1. 201 con estado resultante (puede ser NO ELEGIBLE).
2. 422 si faltan campos o monto inválido.
3. 409 si nro duplicado (propuesta).

#### Escenarios BDD
```gherkin
Característica: Alta de factura API
  Escenario: Alta no elegible
    Cuando POST con fechaPago a 5 días
    Entonces responde 201 con estado "NO ELEGIBLE"
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 422 | VALIDATION_ERROR | Campos inválidos |
| 409 | DUPLICATE_INVOICE | Nro duplicado |

---

### CO-22 — POST · Carga masiva

| | |
|---|---|
| **Tipo** | HT |
| **Habilita** | CO-05 |
| **Contrato** | `POST /api/v1/invoices/bulk` |

#### Objetivo técnico
Procesar filas y devolver resumen (cargadas / incompletas / moneda inválida).

#### Criterios de aceptación
1. Respuesta con conteos y detalle por fila.
2. Aplica RN-C04 y validación de moneda del EGP.
3. Transacción parcial aceptada (como POC) o all-or-nothing — **definir en spike S-C04**.

#### Escenarios BDD
```gherkin
Característica: Bulk de facturas
  Escenario: Resumen con rechazos
    Cuando envío un archivo con filas mixtas
    Entonces la respuesta lista cargadas e inválidas por motivo
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 400 | EMPTY_FILE | Sin filas |
| 422 | INVALID_FORMAT | Archivo ilegible |

---

### CO-23 — PATCH · Fecha de pago

| | |
|---|---|
| **Tipo** | HT |
| **Habilita** | CO-06 |
| **Contrato** | `PATCH /api/v1/invoices/{id}/payment-date` |

#### Objetivo técnico
Actualizar `fechaPago` y recalcular estado (RN-C03/C12).

#### Criterios de aceptación
1. 200 con nuevo estado.
2. 422 fecha inválida.
3. 409 si estado no editable.

#### Escenarios BDD
```gherkin
Característica: Actualizar fecha de pago
  Escenario: Recuperar elegibilidad
    Dado id en NO ELEGIBLE
    Cuando PATCH con fecha a 40 días
    Entonces estado pasa a Habilitada
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 409 | STATE_NOT_EDITABLE | Estado fuera de RN-C12 |
| 422 | INVALID_DATE | Formato/fecha inválida |

---

### CO-24 — POST · Habilitar / Bloquear (batch)

| | |
|---|---|
| **Tipo** | HT |
| **Habilita** | CO-07, CO-08 |
| **Contrato** | `POST /api/v1/invoices/bulk/enable` · `POST /api/v1/invoices/bulk/block` |

#### Objetivo técnico
Transicionar lotes respetando RN-C05/C06.

#### Criterios de aceptación
1. 200 con ids actualizados.
2. 422 si algún id no es elegible (o política “skip inválidos” — definir).

#### Escenarios BDD
```gherkin
Característica: Habilitar/Bloquear batch
  Escenario: Habilitar válidas
    Cuando POST enable con ids Pendiente/Bloqueada
    Entonces todas quedan Habilitada
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 422 | INVALID_STATE | Estado no permitido |

---

### CO-25 — POST · Simular adelanto (individual)

| | |
|---|---|
| **Tipo** | HT |
| **Habilita** | CO-09 |
| **Contrato** | `POST /api/v1/invoices/{id}/simulate` |

#### Objetivo técnico
Calcular ticket RN-C10 y, si `confirm=true`, pasar a Pendiente aprobación EGP.

#### Criterios de aceptación
1. Preview sin mutar estado.
2. Confirm muta a Pendiente aprobación EGP solo desde Habilitada.
3. 422 si monto &gt; factura.

#### Escenarios BDD
```gherkin
Característica: Simulación individual API
  Escenario: Confirmación
    Dado factura Habilitada
    Cuando POST simulate con confirm=true
    Entonces estado = Pendiente aprobación EGP
    Y la respuesta incluye neto calculado
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 409 | INVALID_STATE | No Habilitada |
| 422 | AMOUNT_EXCEEDED | Monto &gt; factura |

---

### CO-26 — POST · Simular adelanto masivo

| | |
|---|---|
| **Tipo** | HT |
| **Habilita** | CO-10 |
| **Contrato** | `POST /api/v1/invoices/bulk/simulate` |

#### Objetivo técnico
Validar combinatoria RN-C07 y calcular ticket agregado.

#### Criterios de aceptación
1. Exige ≥2 ids Habilitada misma combinatoria.
2. Confirm pasa todas a Pendiente aprobación EGP.

#### Escenarios BDD
```gherkin
Característica: Simulación masiva API
  Escenario: Combinatoria inválida
    Cuando POST bulk/simulate con proveedores distintos
    Entonces 422 COMBINATORIA_INVALIDA
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 422 | COMBINATORIA_INVALIDA | EGP/Prov/Moneda mixtos |
| 422 | MIN_SELECTION | &lt; 2 facturas |

---

### CO-27 — POST · Decisión EGP (aprobar / rechazar)

| | |
|---|---|
| **Tipo** | HT |
| **Habilita** | CO-11, CO-12, CO-13 |
| **Contrato** | `POST /api/v1/invoices/{id}/egp-decision` body `{ action: approve\|reject_with_reason\|reject_without_reason, paymentDate? }` |

#### Objetivo técnico
Aplicar RN-C08 y disparar desembolso en approve.

#### Criterios de aceptación
1. approve → Pendiente de desembolso + evento CORE.
2. reject_with_reason exige paymentDate válida.
3. reject_without_reason → Bloqueada.

#### Escenarios BDD
```gherkin
Característica: Decisión EGP API
  Escenario: Aprobar
    Cuando action=approve
    Entonces estado = Pendiente de desembolso
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 409 | INVALID_STATE | No está pendiente EGP |
| 422 | PAYMENT_DATE_REQUIRED | Rechazo con motivo sin fecha |

---

### CO-28 — Webhook / callback CORE BANKING

| | |
|---|---|
| **Tipo** | HT |
| **Habilita** | CO-14 |
| **Contrato** | `POST /api/v1/invoices/disbursement-callback` (o cola interna) |

#### Objetivo técnico
Recibir resultado de desembolso y aplicar RN-C09.

#### Criterios de aceptación
1. success → Financiada.
2. error → Pendiente aprobación EGP.
3. Idempotencia por `operationId`.

#### Escenarios BDD
```gherkin
Característica: Callback de desembolso
  Escenario: Idempotencia
    Dado un callback ya procesado
    Cuando llega el mismo operationId
    Entonces no duplica efectos y responde 200
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 404 | INVOICE_NOT_FOUND | Id desconocido |
| 409 | INVALID_STATE | No estaba en desembolso |

---

### CO-29 — DELETE · Factura

| | |
|---|---|
| **Tipo** | HT |
| **Habilita** | CO-15 |
| **Contrato** | `DELETE /api/v1/invoices/{id}` |

#### Objetivo técnico
Eliminar (o soft-delete) según política de estados.

#### Criterios de aceptación
1. 204 en estados permitidos.
2. 409 si financiada/desembolso (propuesta PO).

#### Escenarios BDD
```gherkin
Característica: Baja de factura
  Escenario: No borrar financiada
    Dado estado Financiada
    Cuando DELETE
    Entonces 409 STATE_NOT_DELETABLE
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 409 | STATE_NOT_DELETABLE | Estado restringido |

---

### CO-30 — GET · Template de carga

| | |
|---|---|
| **Tipo** | HT |
| **Habilita** | CO-16 |
| **Contrato** | `GET /api/v1/invoices/bulk/template` |

#### Objetivo técnico
Servir el Excel oficial versionado.

#### Criterios de aceptación
1. 200 file xlsx con columnas vigentes.
2. Header `Content-Disposition` con nombre de archivo.

#### Escenarios BDD
```gherkin
Característica: Descarga de template
  Escenario: OK
    Cuando GET template
    Entonces recibo un xlsx descargable
```

#### Errores esperados
| Código HTTP | Código negocio | Cuándo |
|-------------|----------------|--------|
| 500 | TEMPLATE_UNAVAILABLE | Asset ausente |

---

## 8. Tareas técnicas / habilitadores

| ID | Tarea | Objetivo | Definition of Done |
|----|-------|----------|--------------------|
| **CO-T01** | Modelo de datos Factura + máquina de estados | Persistir RN-C01…C09 | Migraciones + tests de transición |
| **CO-T02** | Integración CORE BANKING (desembolso) | Reemplazar simulación POC | Sandbox OK/ERROR + callback idempotente |
| **CO-T03** | Enforcement de permisos Confirming en BFF | Aplicar catálogo de 21 permisos | 403 en acciones no autorizadas; matriz QA |

---

## 9. Spikes y decisiones pendientes

| ID | Pregunta | Impacto | Propuesta PO |
|----|----------|---------|--------------|
| **S-C01** | Timeouts, reintentos y compensación del desembolso CORE | CO-14/CO-28 | Reintento manual vía re-aprobación EGP (como POC); max N reintentos automáticos |
| **S-C02** | ¿La línea de crédito bloquea la simulación/aprobación? | CO-02, CO-09 | Validar en approve EGP; mostrar disponible en panel |
| **S-C03** | Alcance real del “Escanear factura” | CO-04 | MVP sin OCR; precarga manual/ERP |
| **S-C04** | Bulk all-or-nothing vs parcial | CO-05/CO-22 | Parcial con reporte (comportamiento POC) |
| **S-C05** | Reconciliar `Confirming.xlsx` (keys, tachados, endpoints) | Todo el backlog | Adjuntar Excel y regenerar §2 |

---

## 10. Recomendaciones del PO — gaps vs catálogo de permisos / Excel

> **No están elaboradas como HU comprometidas.** Provienen del catálogo `ROLE_PERMISSION_CATALOG` (Confirming) y de stubs/código residual de la POC.

| ID | Historia propuesta | Por qué falta / riesgo | Prioridad |
|----|--------------------|------------------------|-----------|
| **R-01** | **Enforcement runtime de permisos Confirming** | El catálogo existe en ABM pero Confirming no chequea permisos al operar | 🔴 Alta |
| **R-02** | **Aprobación / rechazo bancario manual** | Código/listeners residuales; POC vigente usa aprobación automática | 🟠 Media (solo si el Excel lo exige) |
| **R-03** | **Revertir factura (1ª y 2ª aprobación)** | Permisos en catálogo; botones sin wiring en POC | 🟠 Media-alta |
| **R-04** | **Editar datos cargados de factura** | Permiso en catálogo; POC solo edita fecha de pago | 🟠 Media |
| **R-05** | **Ver/Descargar documentos y descargar grilla** | Permisos en catálogo sin UI | 🟠 Media |
| **R-06** | **Reporte descargable de rechazos de bulk** | Operación a escala necesita evidencia | 🟡 Media |
| **R-07** | **Motivo textual estructurado en rechazo EGP** | POC solo pide nueva fecha vía prompt | 🟡 Media |
| **R-08** | **Auditoría de transiciones de estado** | Requisito bancario típico | 🔴 Alta |
| **R-09** | **Job de paso a Vencida** | Estado existe en mocks; no hay transición automática | 🟡 Media |
| **R-10** | **Notificaciones por estado Confirming** | ABM Notificaciones tiene agrupador; falta cablear eventos Confirming | 🟠 Media |

---

## 11. Observaciones de consistencia (POC vs funcional vs Excel)

1. **`Confirming.xlsx` no adjunto:** no se pudo validar tachados ni Issue Keys. Este doc usa `CO-xx` propuestos.
2. **`funcional_v1.0.0.md` desactualizado vs POC:** menciona Pagada/Mora, “Pendiente aprobación banco”, Ejecutar Adelanto → Financiada directa, Revertir operativo. **La POC vigente** usa la máquina de estados de §4 y aprobación EGP + CORE.
3. **Aprobación banco:** HTML comentado / listeners huérfanos; decisión vigente SUP-02 (automática).
4. **Revertir:** UI stub sin listeners → §10 R-03.
5. **Permisos:** 21 ítems en catálogo vs subset implementado en UI → R-01/R-03/R-04/R-05.
6. **Eliminar Financiada:** permitido en POC; restringir en producto (nota CO-15).

---

## 12. Matriz de trazabilidad HU ↔ endpoint ↔ pantalla POC

| HU | HT | Contrato propuesto | Pantalla / control POC |
|----|----|--------------------|------------------------|
| CO-01 | CO-20 | `GET /api/v1/invoices` | `#confirming-view` + tabs/filtros |
| CO-02 | CO-20 | (mismo listado + datos ente ABM) | `#operating-entity-panel` |
| CO-03 | CO-21 | `POST /api/v1/invoices` | `#new-invoice-modal` |
| CO-04 | — | — (FE demo) | `simulateScan` |
| CO-05 | CO-22 | `POST /api/v1/invoices/bulk` | bulk upload + result modal |
| CO-06 | CO-23 | `PATCH .../payment-date` | `#edit-fecha-pago-modal` |
| CO-07 | CO-24 | `POST .../bulk/enable` | `#btn-habilitar-facturas` |
| CO-08 | CO-24 | `POST .../bulk/block` | `#btn-bloquear-facturas` |
| CO-09 | CO-25 | `POST .../simulate` | `#simulate-modal` simulate |
| CO-10 | CO-26 | `POST .../bulk/simulate` | `#btn-simular-facturas` |
| CO-11/12/13 | CO-27 | `POST .../egp-decision` | modo approve-egp |
| CO-14 | CO-28 | callback desembolso | alertas CORE |
| CO-15 | CO-29 | `DELETE .../{id}` | eliminar fila |
| CO-16 | CO-30 | `GET .../bulk/template` | descargar template |

POC de referencia: https://marianaintive.github.io/atlas-confirming-poc/ (ingresar en modo demo → nav **Confirming**).

---

## 13. Definition of Ready / Definition of Done

**Definition of Ready**

- [ ] Como / quiero / para en tarjeta.
- [ ] AC numerados binarios con tags y referencias MSG/RN.
- [ ] BDD en español alineado a AC.
- [ ] Mensajes §5 validados con UX.
- [ ] Contrato HT §7 acordado (o spike acotado).
- [ ] Pantalla POC de referencia identificada.
- [ ] Tras adjuntar Excel: fila mapeada en §2 (incluir/desestimar).
- [ ] INVEST OK o spike marcado.
- [ ] Estimada por el equipo.

**Definition of Done**

- [ ] AC verificados en demo (sí/no).
- [ ] BDD verificados (manual/auto).
- [ ] Validaciones y mensajes según §5.
- [ ] Transiciones de estado auditadas (R-08 cuando exista).
- [ ] Permisos enforced según rol (CO-T03 / R-01).
- [ ] Probado en dominios aplicables.
- [ ] Documentación y matriz §12 actualizadas.
- [ ] Reconciliación con `Confirming.xlsx` registrada si el Excel ya está disponible.

---

*Fin del documento v1.0.0 — Épica CONFIRMING. Pendiente: adjuntar `Confirming.xlsx` para regenerar §2 y mapear keys Jira.*
