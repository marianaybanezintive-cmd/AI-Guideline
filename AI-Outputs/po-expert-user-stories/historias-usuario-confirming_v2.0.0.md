# Historias de Usuario — Épica CONFIRMING v2.0.0 (Portal de Confirming · Banco Atlas)

> **Versión:** v2.0.0 · **Fecha:** 2026-08-11  
> **Fuente única de requerimientos:** `Confirming.xlsx` — hoja **CONFIRMING** (filas 3 a 25).  
> **Autor:** PO (skill `po-expert-user-stories`) · **Producto:** Portal de Confirming (Atlas Trade)  
> **POC de referencia FE:** https://marianaintive.github.io/atlas-confirming-poc/ — pantalla Confirming  
> **Relación con v1.0.0:** Se conserva `historias-usuario-confirming_v1.0.0.md` (derivada solo de POC). **Esta v2 no la pisa** y toma el Excel como fuente de verdad; la POC aporta validaciones, mensajes y flujos ya prototipados.

### Criterio de esta versión (pedido explícito)

- **Todas las filas** del Excel tienen historia(s) elaborada(s).
- **Cada escenario** de cada fila tiene **su propia tarjeta** (`{IssueKey}-E{n}`).
- Keys duplicadas en el Excel (`FAC-05` filas 7 y 8; `CON-03` filas 10 y 12) se desambiguan como `FAC-05-a` y `CON-03-a` *(propuesto)*.
- Nada tachado en el archivo recibido → **0 desestimadas**.

---

## Tabla de contenidos

1. [Criterio de elaboración](#1-criterio-de-elaboración)
2. [Matriz fila Excel → historias por escenario](#2-matriz-fila-excel--historias-por-escenario)
3. [Contexto, actores y supuestos](#3-contexto-actores-y-supuestos)
4. [Reglas de negocio (RN)](#4-reglas-de-negocio-rn)
5. [Catálogo de mensajes (MSG) — POC + Excel](#5-catálogo-de-mensajes-msg--poc--excel)
6. [Historias por escenario (tarjetas)](#6-historias-por-escenario-tarjetas)
7. [Spikes / dudas](#7-spikes--dudas)
8. [Recomendaciones (no están como escenario en el Excel)](#8-recomendaciones-no-están-como-escenario-en-el-excel)
9. [Observaciones de consistencia del Excel](#9-observaciones-de-consistencia-del-excel)
10. [Trazabilidad HU ↔ POC](#10-trazabilidad-hu--poc)
11. [DoR / DoD](#11-dor--dod)

---

## 1. Criterio de elaboración

| Criterio | Decisión |
|----------|----------|
| Filas tachadas | Ninguna en el Excel recibido |
| Unidad de elaboración | **1 escenario Excel = 1 tarjeta** de backlog |
| Escenarios fuente | Transcripción literal del Excel en cada tarjeta |
| FE | Apoyo en POC Confirming (validaciones, msgs, flujos) sin inventar alcance fuera del Excel |
| Gaps / solo POC | §8 Recomendaciones |
| Identificadores | `Issue Key` Excel + sufijo `-E{n}`; desambiguación `-a` si el key se repite |

**Tipos:** `HU-FE` pantalla · `HT` enabler API/BFF/BE · `HU-BE` proceso/sistema cuando aplique.

---

## 2. Matriz fila Excel → historias por escenario

| Fila | Key Excel | Key doc | STACK | Summary (corto) | # Esc | Historias |
|-----:|-----------|---------|-------|-----------------|------:|-----------|
| 3 | FAC-01 | FAC-01 | FE | Pantalla CONFIRMING - Botonera Cargar Factura / Recurso | 2 | FAC-01-E1, FAC-01-E2 |
| 4 | FAC-02 | FAC-02 | FE | Pantalla CONFIRMING - Botonera Cargar Factura / Recurso | 4 | FAC-02-E1, FAC-02-E2, FAC-02-E3, FAC-02-E4 |
| 5 | FAC-03 | FAC-03 | BE/BFF | API CONFIRMING - GET/obtenerInfoEnte | 1 | FAC-03-E1 |
| 6 | FAC-04 | FAC-04 | FE | Pantalla CONFIRMING - Cargar Factura Multimoneda USD o  | 1 | FAC-04-E1 |
| 7 | FAC-05 | FAC-05 | BE/BFF | API CONFIRMING - POST/cargarFactura | 2 | FAC-05-E1, FAC-05-E2 |
| 8 | FAC-05 | FAC-05-a \* | BFF | API CONFIRMING - POST/notificaciónNuevarFactura | 2 | FAC-05-a-E1, FAC-05-a-E2 |
| 9 | CON-01 | CON-01 | FE | Pantalla CONFIRMING -  Filtros / Grilla / pestañas FV / | 3 | CON-01-E1, CON-01-E2, CON-01-E3 |
| 10 | CON-03 | CON-03 | BE/BFF | API CONFIRMING - GET/grillafacturas | 1 | CON-03-E1 |
| 11 | CON-02 | CON-02 | FE | Pantalla CONFIRMING - Grilla acciones / Recurso: todos  | 4 | CON-02-E1, CON-02-E2, CON-02-E3, CON-02-E4 |
| 12 | CON-03 | CON-03-a \* | FE | Pantalla CONFIRMING - Grilla accion Eliminar / Recurso: | 1 | CON-03-a-E1 |
| 13 | CON-04 | CON-04 | FE | Pantalla CONFIRMING - Grilla accion Editar / Recurso: t | 1 | CON-04-E1 |
| 14 | CON-05 | CON-05 | FE | Pantalla CONFIRMING - Grilla accion Aprobar EGP / Recur | 1 | CON-05-E1 |
| 15 | CON-06 | CON-06 | BE/BFF | API CONFIRMING - PATCH/actualizarfactura | 1 | CON-06-E1 |
| 16 | CON-07 | CON-07 | — | Pantalla Información EGP / Recurso: EGP / Dominio: EGP | 3 | CON-07-E1, CON-07-E2, CON-07-E3 |
| 17 | CON-08 | CON-08 | BE/BFF | API CONFIRMING - GET/obtenerInfoEnte | 1 | CON-08-E1 |
| 18 | CON-09 | CON-09 | BE/BFF? | Implementar maquina de estados de Facturas | 6 | CON-09-E1, CON-09-E2, CON-09-E3, CON-09-E4, CON-09-E5, CON-09-E6 |
| 19 | CON-10 | CON-10 | BE/BFF | API CONFIRMING - GET/estados de facturas | 1 | CON-10-E1 |
| 20 | CON-11 | CON-11 | FE | Pantalla CONFIRMING - Botonera Hablitar / Bloquear / Re | 2 | CON-11-E1, CON-11-E2 |
| 21 | SIM-01 | SIM-01 | FE | Pantalla CONFIRMING - Simular Múltiples / Simular Indiv | 6 | SIM-01-E1, SIM-01-E2, SIM-01-E3, SIM-01-E4, SIM-01-E5, SIM-01-E6 |
| 22 | SIM-02 | SIM-02 | BE/BFF | API CONFIRMING - GET/simularAdelantoFactura | 3 | SIM-02-E1, SIM-02-E2, SIM-02-E3 |
| 23 | SIM-03 | SIM-03 | BE/BFF | API CONFIRMING - POST/generarAdelantoFactura | 6 | SIM-03-E1, SIM-03-E2, SIM-03-E3, SIM-03-E4, SIM-03-E5, SIM-03-E6 |
| 24 | SIM-04 | SIM-04 | BFF | API CONFIRMING - POST/notificaciónAdelantoFactura / Rec | 4 | SIM-04-E1, SIM-04-E2, SIM-04-E3, SIM-04-E4 |
| 25 | SIM-05 | SIM-05 | FE | Pantalla CONFIRMING - Aprobación / Rechazo de Simulació | 2 | SIM-05-E1, SIM-05-E2 |

\* Key propuesto por duplicado en Excel.

**Totales:** 23 filas · **58 historias** (una por escenario).

---

## 3. Contexto, actores y supuestos

| Actor | Rol en Confirming |
|-------|-------------------|
| Operador Banco | Supervisa y opera grilla completa |
| Operador / Aprobador EGP | Habilita/bloquea, aprueba/rechaza adelantos, ve límites |
| Operador Proveedor | Carga (según permiso), simula/solicita adelanto |
| BFF/BE Confirming | APIs de grilla, alta, estados, simulación, adelanto |
| CORE BANKING | Recibe préstamo-factura; desembolso |
| Notificaciones | Avisos a EGP/Proveedor en alta y adelanto |

| # | Supuesto |
|---|----------|
| SUP-01 | `GET/obtenerInfoEnte` se reutiliza de MAGIA-120/122 (FAC-03, CON-08). |
| SUP-02 | Moneda PYG del Excel equivale a GS en la POC. |
| SUP-03 | “Creación de factura” en escenarios SIM-03 se interpreta como creación de **solicitud de adelanto** cuando el contexto es generarAdelanto. |
| SUP-04 | Ante conflicto Excel vs POC en reglas (p. ej. bloquear desde Pendiente aprobación EGP, nacer siempre Pendiente, N cuotas), **prevalece el Excel**. |

---

## 4. Reglas de negocio (RN)

| ID | Regla | Origen |
|----|-------|--------|
| RN-C01 | FV = Pendiente, Habilitada, Bloqueada, Pendiente aprobación EGP, Pendiente desembolso; FNV = Financiada, Vencida; FNO = No elegible | CON-01 Excel |
| RN-C02 | Facturas nacen en Pendiente (automático) | CON-09 |
| RN-C03 | Habilitar (manual): desde Pendiente/Bloqueada → Habilitada | CON-09 / CON-11 |
| RN-C04 | Bloquear (manual): desde Pendiente/Habilitada/Pendiente aprobación EGP → Bloqueada | CON-11 Excel |
| RN-C05 | Vencimiento documental &lt; 30 días → Vencida automática, no operable | CON-09 |
| RN-C06 | Fecha de pago &lt; 30 días → No elegible; al corregir fecha (≥30) → Habilitada | CON-09 / CON-04 |
| RN-C07 | Simulación múltiple exige mismo EGP-Proveedor-Moneda; misma fecha → 1 cuota; fechas distintas → N cuotas | SIM-01 |
| RN-C08 | Confirmación de simulación freeza límite; disponible = límite API − freeze | SIM-01 / CON-07 |
| RN-C09 | Solicitante de adelanto ≠ usuario que cargó la factura | SIM-03 |
| RN-C10 | Adelanto solo antes de las 17:00 | SIM-03 |
| RN-C11 | Valores del modal de simulación son estimativos (leyenda obligatoria) | SIM-01 |
| RN-C12 | EGP y Proveedor de la factura deben existir y estar activos | FAC-01 / FAC-02 |

---

## 5. Catálogo de mensajes (MSG) — POC + Excel

| Código | Uso | Texto / plantilla |
|--------|-----|-------------------|
| MSG-C01 | Empty grilla | "No se encontraron facturas con los filtros aplicados." |
| MSG-C02 | Alta incompleta | "Por favor complete todos los campos obligatorios." |
| MSG-C03 | Alta OK | "La factura ha sido registrada exitosamente." |
| MSG-C04 | Alta NO ELEGIBLE | "La factura fue registrada en estado NO ELEGIBLE: la fecha de pago debe estar a 30 días o más desde hoy." |
| MSG-C05 | Scan OK | "Factura leída correctamente desde código QR." |
| MSG-C06–C11 | Tooltips habilitar/bloquear/simular | Ver POC `HABILITAR_*` / `BLOQUEAR_*` / `SIMULAR_*` |
| MSG-C12–C15 | Confirm/éxito habilitar-bloquear | Ver POC |
| MSG-C16–C22 | Simulación / EGP | Ver POC |
| MSG-C23–C24 | CORE desembolso | Ver POC |
| MSG-C25–C27 | Fecha de pago | Ver POC |
| MSG-C28–C29 | Eliminar | Ver POC |
| MSG-C30 | Template | "No se pudo generar el template…" |
| MSG-C40 | Desembolso en curso (Excel CON-02) | "Desembolso en curso..." |
| MSG-C41 | Estimativos (Excel SIM-01) | "Los valores simulados son estimativos…" |
| MSG-C42 | Fuera de horario 17hs | "Las solicitudes de adelanto solo se pueden realizar antes de las 17:00." *(propuesto)* |
| MSG-C43 | Mismo usuario carga/adelanto | "No podés solicitar el adelanto de una factura que cargaste vos." *(propuesto)* |
| MSG-C44 | Límite insuficiente | "La factura excede el límite de crédito disponible del EGP." *(propuesto)* |
| MSG-C45 | Ventana N días expirada | "Venció el plazo para solicitar el adelanto de esta factura." *(propuesto)* |

---

## 6. Historias por escenario (tarjetas)

### Fila 3 — `FAC-01` · Pantalla CONFIRMING - Botonera Cargar Factura | Recurso: todos | dominio: todos

| | |
|---|---|
| **Issue Key Excel** | FAC-01 |
| **STACK** | FE |
| **OBJETIVO (Excel)** | Botonera global de la pantalla: botón cargar factura / Flujo de Crear factura individual |
| **Escenarios en esta fila** | 2 |

#### FAC-01-E1 — Cargar facturas individual

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 3 (FAC-01) · escenario 1/2 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#new-invoice-modal` · `submitNewInvoice` |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero cargar facturas individual
para Botonera global de la pantalla: botón cargar factura

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 3 para el objetivo: Botonera global de la pantalla: botón cargar factura
Flujo de Crear factura individual.

##### Escenarios fuente
> Transcripción literal del Excel (fila 3, escenario 1):
>
> Escenario Cargar facturas individual

##### Criterios de aceptación
1. **[Feliz]** Desde Confirming, el botón **Cargar Factura** abre el modal de alta individual con los campos de factura.
2. **[Feliz]** Completo nro, EGP, proveedor, emisión, vencimiento, fecha de pago, moneda, monto y guardo → la factura se registra (estado inicial según máquina de estados / CON-09).
3. **[Error]** Si faltan campos obligatorios → mensaje de validación y no se guarda (POC: MSG-C02).
4. **[Feliz]** Tras guardar OK → feedback de éxito y la factura aparece en la grilla (POC: MSG-C03 / MSG-C04 si NO ELEGIBLE).

##### Escenarios BDD
```gherkin
Característica: Cargar facturas individual

  Escenario: Cargar factura individual exitosa
    Dado estoy en la pantalla Confirming con permiso de carga
    Cuando abro "Cargar Factura" y completo los datos obligatorios válidos
    Y confirmo guardar
    Entonces la factura queda registrada
    Y veo el mensaje de éxito correspondiente
    Y la factura es visible en la grilla según su estado
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- POC: `openNewInvoiceModal` / `submitNewInvoice`. Fecha de pago default = vencimiento.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### FAC-01-E2 — VALIDACION que el EGP y PROVEEDOR asociados a la factura a guardar…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 3 (FAC-01) · escenario 2/2 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#new-invoice-modal` · `submitNewInvoice` |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero vALIDACION que el EGP y PROVEEDOR asociados a la factura a guardar…
para Botonera global de la pantalla: botón cargar factura

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 3 para el objetivo: Botonera global de la pantalla: botón cargar factura
Flujo de Crear factura individual.

##### Escenarios fuente
> Transcripción literal del Excel (fila 3, escenario 2):
>
> Escenario de VALIDACION que el EGP y PROVEEDOR asociados a la factura a guardar exista y esté activo

##### Criterios de aceptación
1. **[Validación]** Al guardar, el sistema valida que el **EGP** asociado exista y esté **activo**.
2. **[Validación]** Al guardar, el sistema valida que el **Proveedor** asociado exista y esté **activo**.
3. **[Error]** Si EGP o Proveedor no existe o no está activo → no se guarda y se informa el error de validación.
4. **[Feliz]** Si ambos están activos → continúa el alta (FAC-01-E1 / FAC-05).

##### Escenarios BDD
```gherkin
Característica: VALIDACION que el EGP y PROVEEDOR asociados a la factura a guardar…

  Escenario: Rechazo por ente inactivo o inexistente
    Dado un EGP o Proveedor inexistente o no activo
    Cuando intento guardar una factura asociada a ese ente
    Entonces el sistema rechaza el alta
    Y muestra un mensaje de validación de existencia/estado del ente
    Y no se crea la factura

  Escenario: EGP y Proveedor activos
    Dado EGP y Proveedor existentes y activos
    Cuando guardo la factura
    Entonces la validación de entes es exitosa
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- Depende de FAC-03 / MAGIA-120-122 (`GET/obtenerInfoEnte`).

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 4 — `FAC-02` · Pantalla CONFIRMING - Botonera Cargar Factura | Recurso: todos | dominio: todos

| | |
|---|---|
| **Issue Key Excel** | FAC-02 |
| **STACK** | FE |
| **OBJETIVO (Excel)** | Flujo de Crear factura |
| **Escenarios en esta fila** | 4 |

#### FAC-02-E1 — Cargar facturas masivo: descargar template

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 4 (FAC-02) · escenario 1/4 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#new-invoice-modal` · template/bulk/`simulateScan` |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero cargar facturas masivo: descargar template
para Flujo de Crear factura

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 4 para el objetivo: Flujo de Crear factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 4, escenario 1):
>
> Escenario Cargar facturas masivo: descargar template

##### Criterios de aceptación
1. **[Feliz]** Desde el flujo de carga puedo **descargar el template** oficial de facturas.
2. **[Feliz]** El archivo incluye las columnas requeridas para la carga masiva (POC: `BULK_INVOICE_HEADERS`).
3. **[Error]** Si no se puede generar el archivo → mensaje de fallo de descarga (POC: MSG-C30).

##### Escenarios BDD
```gherkin
Característica: Cargar facturas masivo: descargar template

  Escenario: Descargar template de carga masiva
    Dado estoy en el flujo de Cargar Factura
    Cuando elijo descargar el template
    Entonces obtengo un archivo Excel con el formato oficial de carga
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### FAC-02-E2 — Cargar facturas masico: cargar desde archivo

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 4 (FAC-02) · escenario 2/4 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#new-invoice-modal` · template/bulk/`simulateScan` |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero cargar facturas masico: cargar desde archivo
para Flujo de Crear factura

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 4 para el objetivo: Flujo de Crear factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 4, escenario 2):
>
> Escenario Cargar facturas masico: cargar desde archivo

##### Criterios de aceptación
1. **[Feliz]** Puedo seleccionar un archivo `.xls` / `.xlsx` / `.csv` y procesar la carga masiva.
2. **[Feliz]** Se muestra el resultado: filas cargadas vs rechazadas con motivo.
3. **[Validación]** Cada fila aplica la validación de EGP/Proveedor activos (FAC-02-E4).
4. **[Error]** Archivo vacío o ilegible → mensaje de error y ninguna factura creada.

##### Escenarios BDD
```gherkin
Característica: Cargar facturas masico: cargar desde archivo

  Escenario: Carga masiva desde archivo
    Dado un archivo con filas de facturas
    Cuando proceso "Cargar desde archivo"
    Entonces veo el resumen de filas cargadas y no cargadas
    Y las filas válidas aparecen en la grilla
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- POC: `handleBulkInvoiceFile` / `#bulk-upload-result-modal`.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### FAC-02-E3 — Scanear facturas?

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 4 (FAC-02) · escenario 3/4 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#new-invoice-modal` · template/bulk/`simulateScan` |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero scanear facturas?
para Flujo de Crear factura

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 4 para el objetivo: Flujo de Crear factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 4, escenario 3):
>
> Escenario scanear facturas?

##### Criterios de aceptación
1. **[Feliz]** Si el alcance incluye escaneo, puedo disparar el escaneo desde el modal de carga y precargar datos.
2. **[Alternativo]** Si el Excel marca el escaneo con duda (`?`), la historia queda condicionada a decisión de alcance (spike S-CF-01).
3. **[Feliz]** Tras un escaneo demo exitoso veo confirmación (POC: MSG-C05).

##### Escenarios BDD
```gherkin
Característica: Scanear facturas?

  Escenario: Escanear factura (condicionado a decisión de alcance)
    Dado el modal de Cargar Factura
    Cuando ejecuto la acción de escanear
    Entonces los campos se precargan con los datos leídos
    Y puedo revisar/editar antes de guardar
```

##### Fuera de alcance
- OCR/QR productivo real — pendiente de decisión (Excel trae “?”).

##### Notas / preguntas abiertas
- Excel: “Escenario scanear facturas?”. POC tiene `simulateScan` demo.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### FAC-02-E4 — VALIDACION que el EGP y PROVEEDOR asociados a la factura a guardar…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 4 (FAC-02) · escenario 4/4 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#new-invoice-modal` · template/bulk/`simulateScan` |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero vALIDACION que el EGP y PROVEEDOR asociados a la factura a guardar…
para Flujo de Crear factura

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 4 para el objetivo: Flujo de Crear factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 4, escenario 4):
>
> Escenario de VALIDACION que el EGP y PROVEEDOR asociados a la factura a guardar exista y esté activo

##### Criterios de aceptación
1. **[Validación]** En carga masiva, cada fila valida existencia y estado activo de EGP y Proveedor.
2. **[Error]** Filas con ente inválido/inactivo no se cargan y figuran en el reporte de rechazos.
3. **[Feliz]** Solo se persisten filas con entes válidos y activos.

##### Escenarios BDD
```gherkin
Característica: VALIDACION que el EGP y PROVEEDOR asociados a la factura a guardar…

  Escenario: Rechazo de fila por ente inválido en bulk
    Dado un archivo con una fila cuyo EGP no está activo
    Cuando proceso la carga masiva
    Entonces esa fila no se crea
    Y queda informada como rechazada por validación de ente
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 5 — `FAC-03` · API CONFIRMING - GET/obtenerInfoEnte

| | |
|---|---|
| **Issue Key Excel** | FAC-03 |
| **STACK** | BE/BFF |
| **OBJETIVO (Excel)** | Obtener la información de existencia y estado del ente |
| **Escenarios en esta fila** | 1 |

#### FAC-03-E1 — MAGIA-120 / MAGIA-122 Ya desarrollado

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 5 (FAC-03) · escenario 1/1 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API (sin pantalla) — panel ente / validación alta |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero mAGIA-120 / MAGIA-122 Ya desarrollado
para habilitar el flujo FE descrito en FAC-03

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 5 para el objetivo: Obtener la información de existencia y estado del ente.

##### Escenarios fuente
> Transcripción literal del Excel (fila 5, escenario 1):
>
> MAGIA-120 / MAGIA-122 Ya desarrollado

##### Criterios de aceptación
1. **[Feliz]** El contrato `GET/obtenerInfoEnte` responde existencia y estado del ente (EGP/Proveedor).
2. **[Alternativo]** La capacidad ya está cubierta por **MAGIA-120 / MAGIA-122** — reutilizar, no reimplementar.
3. **[Error]** Ente inexistente → respuesta de no encontrado / no activo consumible por el FE de alta.

##### Escenarios BDD
```gherkin
Característica: MAGIA-120 / MAGIA-122 Ya desarrollado

  Escenario: Reutilizar MAGIA-120 / MAGIA-122
    Dado existen los endpoints MAGIA-120 / MAGIA-122
    Cuando el FE de Confirming valida un ente al cargar factura
    Entonces consume esos contratos ya desarrollados
    Y obtiene existencia y estado del ente
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- Excel: “MAGIA-120 / MAGIA-122 Ya desarrollado”. HT de integración/consumo.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 6 — `FAC-04` · Pantalla CONFIRMING - Cargar Factura Multimoneda USD o PYG | Recurso: todos | do

| | |
|---|---|
| **Issue Key Excel** | FAC-04 |
| **STACK** | FE |
| **OBJETIVO (Excel)** | Flujo de Crear factura en diferentes monedas |
| **Escenarios en esta fila** | 1 |

#### FAC-04-E1 — Selector de moneda USD / PYG

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 6 (FAC-04) · escenario 1/1 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#ni-moneda` en modal nueva factura |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero selector de moneda USD / PYG
para Flujo de Crear factura en diferentes monedas

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 6 para el objetivo: Flujo de Crear factura en diferentes monedas.

##### Escenarios fuente
> Transcripción literal del Excel (fila 6, escenario 1):
>
> Escenario selector de moneda USD / PYG

##### Criterios de aceptación
1. **[Feliz]** En el alta de factura puedo seleccionar moneda **USD** o **PYG** (GS en POC).
2. **[Validación]** La moneda seleccionada debe estar habilitada para el EGP (alineado a validación de carga).
3. **[Feliz]** La factura queda registrada en la moneda elegida y se refleja en grilla/simulación.

##### Escenarios BDD
```gherkin
Característica: Selector de moneda USD / PYG

  Escenario: Selector de moneda USD / PYG
    Dado el modal de Cargar Factura
    Cuando selecciono la moneda USD o PYG
    Y guardo la factura válida
    Entonces la factura queda en esa moneda
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- POC usa etiqueta GS equivalente a PYG; confirmar nomenclatura con negocio.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 7 — `FAC-05` · API CONFIRMING - POST/cargarFactura

| | |
|---|---|
| **Issue Key Excel** | FAC-05 |
| **STACK** | BE/BFF |
| **OBJETIVO (Excel)** | Crear factura |
| **Escenarios en esta fila** | 2 |

#### FAC-05-E1 — Creación de factura OK

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 7 (FAC-05) · escenario 1/2 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API `POST` carga factura |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero creación de factura OK
para habilitar el flujo FE descrito en FAC-05

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 7 para el objetivo: Crear factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 7, escenario 1):
>
> Escenario creación de factura OK

##### Criterios de aceptación
1. **[Feliz]** `POST/cargarFactura` con payload válido crea la factura y responde OK con identificador y estado.
2. **[Feliz]** Aplica reglas de estado inicial (CON-09: nace Pendiente / NO ELEGIBLE según fecha de pago).
3. **[Feliz]** Dispara la notificación de alta solo si OK (FAC-05-a-E1).

##### Escenarios BDD
```gherkin
Característica: Creación de factura OK

  Escenario: Creación de factura OK
    Cuando el BFF/BE recibe POST/cargarFactura válido
    Entonces persiste la factura
    Y responde éxito con los datos creados
    Y queda disponible para la grilla
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### FAC-05-E2 — Creación de factura con ERROR

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 7 (FAC-05) · escenario 2/2 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API `POST` carga factura |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero creación de factura con ERROR
para habilitar el flujo FE descrito en FAC-05

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 7 para el objetivo: Crear factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 7, escenario 2):
>
> Escenario creación de factura con ERROR

##### Criterios de aceptación
1. **[Error]** Si la creación falla (validación, ente, persistencia, etc.) el API responde error y **no** crea la factura.
2. **[Error]** No se envía notificación de alta (FAC-05-a-E2).
3. **[Error]** El FE muestra mensaje de error accionable.

##### Escenarios BDD
```gherkin
Característica: Creación de factura con ERROR

  Escenario: Creación de factura con ERROR
    Cuando POST/cargarFactura falla por validación o error de servicio
    Entonces no se persiste la factura
    Y la respuesta indica el error
    Y no se dispara notificación de nueva factura
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 8 — `FAC-05-a` · API CONFIRMING - POST/notificaciónNuevarFactura

 *(propuesto: Excel repite `FAC-05` en fila 8; se desambigua como `FAC-05-a`)*

| | |
|---|---|
| **Issue Key Excel** | FAC-05 |
| **STACK** | BFF |
| **OBJETIVO (Excel)** | Notificación de creación de factura |
| **Escenarios en esta fila** | 2 |

#### FAC-05-a-E1 — Creación de factura OK, se envia NOTIFICACION al EGP del pedido de…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 8 (FAC-05) · escenario 1/2 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Notificación post-alta (BFF) |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero creación de factura OK, se envia NOTIFICACION al EGP del pedido de…
para habilitar el flujo FE descrito en FAC-05-a

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 8 para el objetivo: Notificación de creación de factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 8, escenario 1):
>
> Escenario creación de factura OK, se envia NOTIFICACION al EGP del pedido de carga de factura

##### Criterios de aceptación
1. **[Feliz]** Tras alta OK se envía **notificación al EGP** del pedido/carga de factura.
2. **[Feliz]** La notificación usa el canal configurado (ABM Notificaciones / mail).
3. **[Validación]** Solo se envía si la creación fue exitosa.

##### Escenarios BDD
```gherkin
Característica: Creación de factura OK, se envia NOTIFICACION al EGP del pedido de…

  Escenario: Notificación al EGP tras alta OK
    Dado que POST/cargarFactura respondió OK
    Cuando se procesa la notificación de nueva factura
    Entonces el EGP recibe la notificación del pedido de carga
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### FAC-05-a-E2 — Creación de factura con ERROR, NO se envia NOTIFICACION del pedido…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 8 (FAC-05) · escenario 2/2 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Notificación post-alta (BFF) |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero creación de factura con ERROR, NO se envia NOTIFICACION del pedido…
para habilitar el flujo FE descrito en FAC-05-a

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 8 para el objetivo: Notificación de creación de factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 8, escenario 2):
>
> Escenario creación de factura con ERROR, NO se envia NOTIFICACION del pedido de carga de factura

##### Criterios de aceptación
1. **[Error]** Si la creación de factura falla, **no** se envía notificación al EGP.
2. **[Validación]** No quedan notificaciones huérfanas asociadas a facturas no creadas.

##### Escenarios BDD
```gherkin
Característica: Creación de factura con ERROR, NO se envia NOTIFICACION del pedido…

  Escenario: Sin notificación si el alta falla
    Dado que POST/cargarFactura respondió ERROR
    Cuando se evalúa el envío de notificación
    Entonces no se envía notificación de nueva factura al EGP
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 9 — `CON-01` · Pantalla CONFIRMING -  Filtros / Grilla / pestañas FV / FNV / FNO | Recurso: tod

| | |
|---|---|
| **Issue Key Excel** | CON-01 |
| **STACK** | FE |
| **OBJETIVO (Excel)** | Crear la pantalla Confirming, su grilla y filtros, con las pestañas correspondientes a los estados de las facturas Facturas Vigentes (estados pendiente, habilitada, bloqueada, pendiente de aprobación EGP, pendiente de desembolso), Facturas No Vigentes (financiada, vencida) y Facturas No Operables (N |
| **Escenarios en esta fila** | 3 |

#### CON-01-E1 — Filtros de Busqueda

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 9 (CON-01) · escenario 1/3 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#confirming-view` · filtros · tabs FV/FNV/FNO |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero filtros de Busqueda
para Crear la pantalla Confirming, su grilla y filtros, con las pestañas correspondientes a los estados de las facturas Factu

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 9 para el objetivo: Crear la pantalla Confirming, su grilla y filtros, con las pestañas correspondientes a los estados de las facturas Facturas Vigentes (estados pendiente, habilit.

##### Escenarios fuente
> Transcripción literal del Excel (fila 9, escenario 1):
>
> Escenario de Filtros de Busqueda

##### Criterios de aceptación
1. **[Feliz]** Puedo filtrar por texto (nro, EGP, Proveedor), fecha de vencimiento, fecha de pago y estado.
2. **[Feliz]** Los filtros se combinan con la pestaña activa y el ente operativo del topbar.
3. **[Alternativo]** Sin coincidencias → empty state (POC: MSG-C01).

##### Escenarios BDD
```gherkin
Característica: Filtros de Busqueda

  Escenario: Filtros de búsqueda
    Dado existen facturas en Confirming
    Cuando aplico filtros de búsqueda / fechas / estado
    Entonces la grilla muestra solo las facturas que cumplen los criterios
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### CON-01-E2 — Campos a Mostrar en la Grilla

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 9 (CON-01) · escenario 2/3 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#confirming-view` · filtros · tabs FV/FNV/FNO |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero campos a Mostrar en la Grilla
para Crear la pantalla Confirming, su grilla y filtros, con las pestañas correspondientes a los estados de las facturas Factu

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 9 para el objetivo: Crear la pantalla Confirming, su grilla y filtros, con las pestañas correspondientes a los estados de las facturas Facturas Vigentes (estados pendiente, habilit.

##### Escenarios fuente
> Transcripción literal del Excel (fila 9, escenario 2):
>
> Escenario de campos a Mostrar en la Grilla

##### Criterios de aceptación
1. **[Feliz]** La grilla muestra al menos: Nro. Factura, EGP, Proveedor, Emisión, Vencimiento, Fecha de Pago, Monto, Estado, Eliminar, Acciones.
2. **[Feliz]** Montos se formatean con moneda; estados con badge visual.
3. **[Feliz]** Hay selección múltiple (checkbox) alineada a acciones de botonera.

##### Escenarios BDD
```gherkin
Característica: Campos a Mostrar en la Grilla

  Escenario: Campos visibles en la grilla
    Dado estoy en Confirming con facturas cargadas
    Entonces veo las columnas de negocio definidas para la grilla
    Y cada fila refleja los datos de la factura
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### CON-01-E3 — Pestañas FV/FNV/FNO de la grilla según estado de la facturas

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 9 (CON-01) · escenario 3/3 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#confirming-view` · filtros · tabs FV/FNV/FNO |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero pestañas FV/FNV/FNO de la grilla según estado de la facturas
para Crear la pantalla Confirming, su grilla y filtros, con las pestañas correspondientes a los estados de las facturas Factu

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 9 para el objetivo: Crear la pantalla Confirming, su grilla y filtros, con las pestañas correspondientes a los estados de las facturas Facturas Vigentes (estados pendiente, habilit.

##### Escenarios fuente
> Transcripción literal del Excel (fila 9, escenario 3):
>
> Escenario de pestañas FV/FNV/FNO de la grilla según estado de la facturas

##### Criterios de aceptación
1. **[Feliz]** Pestaña **Facturas Vigentes (FV)**: Pendiente, Habilitada, Bloqueada, Pendiente aprobación EGP, Pendiente de desembolso.
2. **[Feliz]** Pestaña **Facturas No Vigentes (FNV)**: Financiada, Vencida.
3. **[Feliz]** Pestaña **Facturas No Operables (FNO)**: No elegible / NO ELEGIBLE.
4. **[Validación]** Una factura solo aparece en la pestaña que corresponde a su estado.

##### Escenarios BDD
```gherkin
Característica: Pestañas FV/FNV/FNO de la grilla según estado de la facturas

  Escenario: Pestañas FV / FNV / FNO
    Dado facturas en distintos estados
    Cuando selecciono cada pestaña
    Entonces solo veo los estados definidos para FV, FNV o FNO
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 10 — `CON-03` · API CONFIRMING - GET/grillafacturas

| | |
|---|---|
| **Issue Key Excel** | CON-03 |
| **STACK** | BE/BFF |
| **OBJETIVO (Excel)** | Obtener todas las facturas del EGP / Proveedor |
| **Escenarios en esta fila** | 1 |

#### CON-03-E1 — FE/BFF/BE consulta las facturas a mostrar en la grilla

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 10 (CON-03) · escenario 1/1 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API `GET` grilla facturas |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero fE/BFF/BE consulta las facturas a mostrar en la grilla
para habilitar el flujo FE descrito en CON-03

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 10 para el objetivo: Obtener todas las facturas del EGP / Proveedor.

##### Escenarios fuente
> Transcripción literal del Excel (fila 10, escenario 1):
>
> Escenario FE/BFF/BE consulta las facturas a mostrar en la grilla

##### Criterios de aceptación
1. **[Feliz]** `GET/grillafacturas` devuelve las facturas del EGP/Proveedor (o todas según dominio Banco) para armar la grilla.
2. **[Feliz]** Soporta parámetros de filtro/pestaña alineados a CON-01.
3. **[Error]** 401/403 si sesión o permisos inválidos.

##### Escenarios BDD
```gherkin
Característica: FE/BFF/BE consulta las facturas a mostrar en la grilla

  Escenario: Consulta de facturas para la grilla
    Cuando el FE solicita GET/grillafacturas con filtros
    Entonces el BFF/BE responde el listado correspondiente al ente/dominio
    Y el FE renderiza la grilla
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 11 — `CON-02` · Pantalla CONFIRMING - Grilla acciones | Recurso: todos | dominio: todos

| | |
|---|---|
| **Issue Key Excel** | CON-02 |
| **STACK** | FE |
| **OBJETIVO (Excel)** | Tiene como objetivo SOLO agregar la Botonera de la grilla por factura, cada flujo luego se desarrollara en otras historias |
| **Escenarios en esta fila** | 4 |

#### CON-02-E1 — Boton Eliminar Factura, siempre visible y activo

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 11 (CON-02) · escenario 1/4 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Columna Acciones de la grilla |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero boton Eliminar Factura, siempre visible y activo
para Tiene como objetivo SOLO agregar la Botonera de la grilla por factura, cada flujo luego se desarrollara en otras histori

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 11 para el objetivo: Tiene como objetivo SOLO agregar la Botonera de la grilla por factura, cada flujo luego se desarrollara en otras historias.

##### Escenarios fuente
> Transcripción literal del Excel (fila 11, escenario 1):
>
> Escenario de boton Eliminar Factura, siempre visible y activo

##### Criterios de aceptación
1. **[Feliz]** El botón/ícono **Eliminar Factura** está siempre visible y activo en la columna de acciones/eliminar.
2. **[Nota]** El flujo completo del modal se elabora en CON-03-a; esta historia solo garantiza la presencia del control.

##### Escenarios BDD
```gherkin
Característica: Boton Eliminar Factura, siempre visible y activo

  Escenario: Botón Eliminar siempre visible
    Dado cualquier factura listada en la grilla
    Entonces veo la acción Eliminar visible y activa
```

##### Fuera de alcance
- Lógica de confirmación y borrado (CON-03-a).

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### CON-02-E2 — Booón Editar Fecha de Pago, siempre visible y activo

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 11 (CON-02) · escenario 2/4 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Columna Acciones de la grilla |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero booón Editar Fecha de Pago, siempre visible y activo
para Tiene como objetivo SOLO agregar la Botonera de la grilla por factura, cada flujo luego se desarrollara en otras histori

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 11 para el objetivo: Tiene como objetivo SOLO agregar la Botonera de la grilla por factura, cada flujo luego se desarrollara en otras historias.

##### Escenarios fuente
> Transcripción literal del Excel (fila 11, escenario 2):
>
> Escenario de booón Editar Fecha de Pago, siempre visible y activo

##### Criterios de aceptación
1. **[Feliz]** El botón **Editar Fecha de Pago** está siempre visible y activo en la grilla.
2. **[Nota]** El modal y warning de NO Elegible se elaboran en CON-04.

##### Escenarios BDD
```gherkin
Característica: Booón Editar Fecha de Pago, siempre visible y activo

  Escenario: Botón Editar Fecha de Pago siempre visible
    Dado cualquier factura listada en la grilla
    Entonces veo la acción Editar Fecha de Pago visible y activa
```

##### Fuera de alcance
- Flujo modal de edición (CON-04).

##### Notas / preguntas abiertas
- POC restringe edición a ciertos estados (`FECHA_PAGO_EDITABLE_STATES`); Excel pide siempre visible — prevalece Excel; anotar gap POC.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### CON-02-E3 — Botón Aprobar EGP, solo se muestra para facturas en estado Pendiente…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 11 (CON-02) · escenario 3/4 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Columna Acciones de la grilla |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero botón Aprobar EGP, solo se muestra para facturas en estado Pendiente…
para Tiene como objetivo SOLO agregar la Botonera de la grilla por factura, cada flujo luego se desarrollara en otras histori

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 11 para el objetivo: Tiene como objetivo SOLO agregar la Botonera de la grilla por factura, cada flujo luego se desarrollara en otras historias.

##### Escenarios fuente
> Transcripción literal del Excel (fila 11, escenario 3):
>
> Escenario de botón Aprobar EGP, solo se muestra para facturas en estado Pendiente de Aprobación EGP

##### Criterios de aceptación
1. **[Feliz]** El botón **Aprobar EGP** solo se muestra para facturas en estado **Pendiente de Aprobación EGP**.
2. **[Validación]** En cualquier otro estado el botón no se muestra.
3. **[Nota]** El modal de aprobación/rechazo se elabora en CON-05 / SIM-05.

##### Escenarios BDD
```gherkin
Característica: Botón Aprobar EGP, solo se muestra para facturas en estado Pendiente…

  Escenario: Visibilidad condicional de Aprobar EGP
    Dado una factura en "Pendiente aprobación EGP"
    Entonces veo el botón Aprobar EGP
    Dado una factura en "Habilitada"
    Entonces no veo el botón Aprobar EGP
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### CON-02-E4 — Mensaje de Espera en desembolso: cuando e desembolso está en curso…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 11 (CON-02) · escenario 4/4 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Columna Acciones de la grilla |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero mensaje de Espera en desembolso: cuando e desembolso está en curso…
para Tiene como objetivo SOLO agregar la Botonera de la grilla por factura, cada flujo luego se desarrollara en otras histori

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 11 para el objetivo: Tiene como objetivo SOLO agregar la Botonera de la grilla por factura, cada flujo luego se desarrollara en otras historias.

##### Escenarios fuente
> Transcripción literal del Excel (fila 11, escenario 4):
>
> Escenario de Mensaje de Espera en desembolso: cuando e desembolso está en curso se muestra un msj dentro de la columna de acciones "Desembolso en curso..." con ruedita animada, solo se muestra para facturas en estado "Pendiente de Desembolso"

##### Criterios de aceptación
1. **[Feliz]** Para facturas en **Pendiente de Desembolso**, en la columna Acciones se muestra el mensaje **"Desembolso en curso..."** con indicador animado (ruedita).
2. **[Validación]** Ese mensaje no se muestra en otros estados.
3. **[Feliz]** No se ofrecen acciones conflictivas mientras el desembolso está en curso.

##### Escenarios BDD
```gherkin
Característica: Mensaje de Espera en desembolso: cuando e desembolso está en curso…

  Escenario: Mensaje de espera en desembolso
    Dado una factura en "Pendiente de desembolso"
    Entonces en Acciones veo "Desembolso en curso..." con indicador animado
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- POC: hint “CORE BANKING desembolsando…”. Alinear copy a “Desembolso en curso...”.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 12 — `CON-03-a` · Pantalla CONFIRMING - Grilla accion Eliminar | Recurso: todos | dominio: todos

 *(propuesto: Excel repite `CON-03` en fila 12; se desambigua como `CON-03-a`)*

| | |
|---|---|
| **Issue Key Excel** | CON-03 |
| **STACK** | FE |
| **OBJETIVO (Excel)** | Flujo de Eliminar factura |
| **Escenarios en esta fila** | 1 |

#### CON-03-a-E1 — Modal de confirmación del boton Eliminar Factura, con los datos de…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 12 (CON-03) · escenario 1/1 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `deleteInvoice` · confirm modal |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero modal de confirmación del boton Eliminar Factura, con los datos de…
para Flujo de Eliminar factura

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 12 para el objetivo: Flujo de Eliminar factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 12, escenario 1):
>
> Escenario modal de confirmación del boton Eliminar Factura, con los datos de la factura y boton de confirmar

##### Criterios de aceptación
1. **[Feliz]** Al elegir Eliminar se abre un **modal de confirmación** con los datos de la factura y botón confirmar.
2. **[Feliz]** Si confirmo → la factura se elimina (baja según CON-06) y desaparece de la grilla (POC: MSG-C28/C29).
3. **[Alternativo]** Si cancelo → no hay cambios.

##### Escenarios BDD
```gherkin
Característica: Modal de confirmación del boton Eliminar Factura, con los datos de…

  Escenario: Modal de confirmación de eliminación
    Dado una factura en la grilla
    Cuando elijo Eliminar
    Entonces veo un modal con los datos de la factura y opción de confirmar
    Cuando confirmo
    Entonces la factura ya no figura en la grilla
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 13 — `CON-04` · Pantalla CONFIRMING - Grilla accion Editar | Recurso: todos | dominio: todos

| | |
|---|---|
| **Issue Key Excel** | CON-04 |
| **STACK** | FE |
| **OBJETIVO (Excel)** | Flujo de Editar Factura |
| **Escenarios en esta fila** | 1 |

#### CON-04-E1 — Modal de confirmación del boton Editar Fecha de Pago de Factura, con…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 13 (CON-04) · escenario 1/1 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#edit-fecha-pago-modal` |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero modal de confirmación del boton Editar Fecha de Pago de Factura, con…
para Flujo de Editar Factura

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 13 para el objetivo: Flujo de Editar Factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 13, escenario 1):
>
> Escenario modal de confirmación del boton Editar Fecha de Pago de Factura, con los datos de la factura y boton de confirmar (con warning de cantidad de dias para que pase a NO Elegible)

##### Criterios de aceptación
1. **[Feliz]** Al editar fecha de pago se abre modal con datos de la factura y confirmación.
2. **[Validación]** Si la nueva fecha implica pasar a **NO Elegible** (&lt; 30 días), se muestra **warning** de cantidad de días antes de confirmar (POC: MSG-C26).
3. **[Feliz]** Al confirmar se actualiza la fecha y el estado según máquina (CON-09-E6).
4. **[Error]** Fecha inválida → mensaje y no actualiza (POC: MSG-C25).

##### Escenarios BDD
```gherkin
Característica: Modal de confirmación del boton Editar Fecha de Pago de Factura, con…

  Escenario: Editar fecha de pago con warning de NO Elegible
    Dado una factura operable
    Cuando cambio la fecha de pago a menos de 30 días desde hoy
    Entonces veo un warning de NO Elegible con la cantidad de días
    Y si confirmo la factura queda No elegible
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 14 — `CON-05` · Pantalla CONFIRMING - Grilla accion Aprobar EGP | Recurso: todos | dominio: todo

| | |
|---|---|
| **Issue Key Excel** | CON-05 |
| **STACK** | FE |
| **OBJETIVO (Excel)** | Flujo de Aprobacion del EGP por el desembolso de una factura |
| **Escenarios en esta fila** | 1 |

#### CON-05-E1 — Modal de confirmación del boton Aprobar EGP, con los datos de la…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 14 (CON-05) · escenario 1/1 |
| **Actor** | Aprobador EGP |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#simulate-modal` modo `approve-egp` |

##### Historia
Como Aprobador EGP
quiero modal de confirmación del boton Aprobar EGP, con los datos de la…
para Flujo de Aprobacion del EGP por el desembolso de una factura

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 14 para el objetivo: Flujo de Aprobacion del EGP por el desembolso de una factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 14, escenario 1):
>
> Escenario modal de confirmación del boton Aprobar EGP, con los datos de la factura y boton de confirmar (misma información que el modal de Simulación, con datos bloqueados) y opciones Aprobar, Rechazar (con o sin motivo)

##### Criterios de aceptación
1. **[Feliz]** Al elegir Aprobar EGP se abre modal con la **misma información que Simulación**, datos **bloqueados**.
2. **[Feliz]** Ofrece opciones **Aprobar**, **Rechazar con motivo** y **Rechazar sin motivo**.
3. **[Nota]** La lógica de negocio de aprobación/rechazo se detalla en SIM-05; esta historia cubre el modal de la grilla.

##### Escenarios BDD
```gherkin
Característica: Modal de confirmación del boton Aprobar EGP, con los datos de la…

  Escenario: Modal Aprobar EGP desde grilla
    Dado una factura en Pendiente aprobación EGP
    Cuando abro Aprobar EGP
    Entonces veo el ticket de simulación en solo lectura
    Y veo acciones Aprobar y Rechazar (con o sin motivo)
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 15 — `CON-06` · API CONFIRMING - PATCH/actualizarfactura

| | |
|---|---|
| **Issue Key Excel** | CON-06 |
| **STACK** | BE/BFF |
| **OBJETIVO (Excel)** | Actualizar factura: baja logica o fisica?, actualizar fecha de pago, cambio de estado de factura, etc... |
| **Escenarios en esta fila** | 1 |

#### CON-06-E1 — FE/BFF/BE consulta las facturas a mostrar en la grilla

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 15 (CON-06) · escenario 1/1 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API `PATCH` actualizar factura |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero fE/BFF/BE consulta las facturas a mostrar en la grilla
para habilitar el flujo FE descrito en CON-06

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 15 para el objetivo: Actualizar factura: baja logica o fisica?, actualizar fecha de pago, cambio de estado de factura, etc....

##### Escenarios fuente
> Transcripción literal del Excel (fila 15, escenario 1):
>
> Escenario FE/BFF/BE consulta las facturas a mostrar en la grilla

##### Criterios de aceptación
1. **[Feliz]** `PATCH/actualizarfactura` permite actualizar fecha de pago, cambio de estado y baja (lógica o física — ver notas).
2. **[Feliz]** Cada actualización respeta la máquina de estados (CON-09 / CON-10).
3. **[Error]** Transición inválida → 409/422 sin mutar.
4. **[Nota]** El escenario Excel dice “consulta grilla” (probable copy-paste); se elabora según OBJETIVO.

##### Escenarios BDD
```gherkin
Característica: FE/BFF/BE consulta las facturas a mostrar en la grilla

  Escenario: Actualizar factura (fecha / estado / baja)
    Cuando el FE invoca PATCH/actualizarfactura con un cambio válido
    Entonces el BE aplica el cambio
    Y responde la factura actualizada

  Escenario: Transición de estado inválida
    Cuando se solicita un cambio de estado no permitido por la máquina
    Entonces el API responde error de conflicto/validación
    Y no modifica la factura
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- Duda Excel en OBJETIVO: “baja logica o fisica?”. Spike S-CF-02.
- Escenario Excel mal pegado (“consulta grilla”); AC tomados del OBJETIVO.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 16 — `CON-07` · Pantalla Información EGP | Recurso: EGP | Dominio: EGP

| | |
|---|---|
| **Issue Key Excel** | CON-07 |
| **STACK** | — |
| **OBJETIVO (Excel)** | Mostrar la información crediticia para facilitar al oprobador del EGP, aprobar o rechazar adelantos / Calculo de Limite de credito a mostrar = limite de credito obtenido desde la API - Limite freezado |
| **Escenarios en esta fila** | 3 |

#### CON-07-E1 — Cabecera de información financiera del EGP: RUC, Razón Social,…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 16 (CON-07) · escenario 1/3 |
| **Actor** | Aprobador EGP / Operador Proveedor |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#operating-entity-panel` |

##### Historia
Como Aprobador EGP / Operador Proveedor
quiero cabecera de información financiera del EGP: RUC, Razón Social,…
para Mostrar la información crediticia para facilitar al oprobador del EGP, aprobar o rechazar adelantos

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 16 para el objetivo: Mostrar la información crediticia para facilitar al oprobador del EGP, aprobar o rechazar adelantos
Calculo de Limite de credito a mostrar = limite de credito o.

##### Escenarios fuente
> Transcripción literal del Excel (fila 16, escenario 1):
>
> Escenario cabecera de información financiera del EGP: RUC, Razón Social, Limites, Tasas

##### Criterios de aceptación
1. **[Feliz]** Cabecera EGP muestra: RUC, Razón Social, Límites, Tasas.
2. **[Feliz]** Visible al operar/aprobar en contexto EGP (panel Confirming).

##### Escenarios BDD
```gherkin
Característica: Cabecera de información financiera del EGP: RUC, Razón Social,…

  Escenario: Cabecera financiera EGP
    Dado selecciono un ente EGP
    Entonces veo RUC, Razón Social, límites y tasas en la cabecera/panel
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### CON-07-E2 — Cabecera de información financiera del Proveedor: RUC, Razón Social,…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 16 (CON-07) · escenario 2/3 |
| **Actor** | Aprobador EGP / Operador Proveedor |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#operating-entity-panel` |

##### Historia
Como Aprobador EGP / Operador Proveedor
quiero cabecera de información financiera del Proveedor: RUC, Razón Social,…
para Mostrar la información crediticia para facilitar al oprobador del EGP, aprobar o rechazar adelantos

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 16 para el objetivo: Mostrar la información crediticia para facilitar al oprobador del EGP, aprobar o rechazar adelantos
Calculo de Limite de credito a mostrar = limite de credito o.

##### Escenarios fuente
> Transcripción literal del Excel (fila 16, escenario 2):
>
> Escenario cabecera de información financiera del Proveedor: RUC, Razón Social, creditos activos, estado de morosidad

##### Criterios de aceptación
1. **[Feliz]** Cabecera Proveedor muestra: RUC, Razón Social, créditos activos, estado de morosidad.
2. **[Feliz]** Visible al operar en contexto Proveedor.

##### Escenarios BDD
```gherkin
Característica: Cabecera de información financiera del Proveedor: RUC, Razón Social,…

  Escenario: Cabecera financiera Proveedor
    Dado selecciono un ente Proveedor
    Entonces veo RUC, Razón Social, créditos activos y estado de morosidad
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- POC actual muestra panel genérico de ente; completar campos de morosidad/créditos activos en producto.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### CON-07-E3 — Calculo de Limite de credito a mostrar = limite de credito obtenido…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 16 (CON-07) · escenario 3/3 |
| **Actor** | Aprobador EGP / Operador Proveedor |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#operating-entity-panel` |

##### Historia
Como Aprobador EGP / Operador Proveedor
quiero calculo de Limite de credito a mostrar = limite de credito obtenido…
para Mostrar la información crediticia para facilitar al oprobador del EGP, aprobar o rechazar adelantos

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 16 para el objetivo: Mostrar la información crediticia para facilitar al oprobador del EGP, aprobar o rechazar adelantos
Calculo de Limite de credito a mostrar = limite de credito o.

##### Escenarios fuente
> Transcripción literal del Excel (fila 16, escenario 3):
>
> Escenario Calculo de Limite de credito a mostrar = limite de credito obtenido desde la API - Limite freezado

##### Criterios de aceptación
1. **[Feliz]** Límite a mostrar = **límite de crédito API − límite freezado**.
2. **[Feliz]** El valor se actualiza tras freeze por simulación (SIM-01-E5 / SIM-03-E6).
3. **[Validación]** Nunca muestra negativo sin indicación; si disponible = 0 se refleja claramente.

##### Escenarios BDD
```gherkin
Característica: Calculo de Limite de credito a mostrar = limite de credito obtenido…

  Escenario: Cálculo de límite disponible
    Dado un EGP con límite de crédito L y freeze F
    Cuando consulto la información crediticia
    Entonces el límite mostrado es L - F
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 17 — `CON-08` · API CONFIRMING - GET/obtenerInfoEnte

| | |
|---|---|
| **Issue Key Excel** | CON-08 |
| **STACK** | BE/BFF |
| **OBJETIVO (Excel)** | Obtener la información financiera para el modal de info crediticia |
| **Escenarios en esta fila** | 1 |

#### CON-08-E1 — MAGIA-120 / MAGIA-122 Ya desarrollado

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 17 (CON-08) · escenario 1/1 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API info ente (MAGIA-120/122) |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero mAGIA-120 / MAGIA-122 Ya desarrollado
para habilitar el flujo FE descrito en CON-08

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 17 para el objetivo: Obtener la información financiera para el modal de info crediticia.

##### Escenarios fuente
> Transcripción literal del Excel (fila 17, escenario 1):
>
> MAGIA-120 / MAGIA-122 Ya desarrollado

##### Criterios de aceptación
1. **[Feliz]** `GET/obtenerInfoEnte` entrega la información financiera para el modal/panel crediticio.
2. **[Alternativo]** Reutilizar **MAGIA-120 / MAGIA-122** ya desarrollados.
3. **[Feliz]** Incluye datos necesarios para CON-07 (límites, tasas, freeze si aplica).

##### Escenarios BDD
```gherkin
Característica: MAGIA-120 / MAGIA-122 Ya desarrollado

  Escenario: Obtener info financiera del ente
    Cuando el FE solicita información crediticia del ente
    Entonces consume MAGIA-120 / MAGIA-122
    Y obtiene los datos para la cabecera Confirming
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 18 — `CON-09` · Implementar maquina de estados de Facturas

| | |
|---|---|
| **Issue Key Excel** | CON-09 |
| **STACK** | BE/BFF? |
| **OBJETIVO (Excel)** | Implementar el funcionamiento de la maquina de estados de facturas |
| **Escenarios en esta fila** | 6 |

#### CON-09-E1 — Cada uno de los estados de la maquina de estados, si es de ejecución…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 18 (CON-09) · escenario 1/6 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Máquina de estados (BE) — reflejada en tabs POC |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero cada uno de los estados de la maquina de estados, si es de ejecución…
para habilitar el flujo FE descrito en CON-09

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 18 para el objetivo: Implementar el funcionamiento de la maquina de estados de facturas.

##### Escenarios fuente
> Transcripción literal del Excel (fila 18, escenario 1):
>
> Escenarios de cada uno de los estados de la maquina de estados, si es de ejecución manual o automatico, estado previo y estado posterior

##### Criterios de aceptación
1. **[Feliz]** Existe catálogo de estados de la máquina con: nombre, tipo de transición (manual/automática), estado previo y posterior permitidos.
2. **[Feliz]** El BE rechaza transiciones no catalogadas.
3. **[Feliz]** FE refleja estados en badges y pestañas FV/FNV/FNO.

##### Escenarios BDD
```gherkin
Característica: Cada uno de los estados de la maquina de estados, si es de ejecución…

  Escenario: Catálogo de transiciones de la máquina de estados
    Dado el motor de estados de facturas
    Cuando consulto las transiciones definidas
    Entonces cada estado informa si su cambio es manual o automático
    Y cuáles son los estados previos y posteriores válidos
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### CON-09-E2 — 1-Todas las facturas nacen en Pendiente, automatico

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 18 (CON-09) · escenario 2/6 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Máquina de estados (BE) — reflejada en tabs POC |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero 1-Todas las facturas nacen en Pendiente, automatico
para habilitar el flujo FE descrito en CON-09

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 18 para el objetivo: Implementar el funcionamiento de la maquina de estados de facturas.

##### Escenarios fuente
> Transcripción literal del Excel (fila 18, escenario 2):
>
> 1-Todas las facturas nacen en Pendiente, automatico

##### Criterios de aceptación
1. **[Feliz]** Toda factura nueva **nace en Pendiente** de forma **automática** (salvo regla de NO Elegible por fecha de pago — E6).
2. **[Validación]** No se permite crear directamente en Habilitada/Financiada salvo regla explícita de negocio futura.

##### Escenarios BDD
```gherkin
Característica: 1-Todas las facturas nacen en Pendiente, automatico

  Escenario: Alta automática en Pendiente
    Cuando se crea una factura con fecha de pago elegible
    Entonces su estado inicial es Pendiente
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- POC permite elegir estado inicial en el modal; Excel manda nacer en Pendiente — alinear producto al Excel.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### CON-09-E3 — 2-Cuando un usuario finaliza flujo de Habilitar, actualiza a ese…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 18 (CON-09) · escenario 3/6 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Máquina de estados (BE) — reflejada en tabs POC |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero 2-Cuando un usuario finaliza flujo de Habilitar, actualiza a ese…
para habilitar el flujo FE descrito en CON-09

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 18 para el objetivo: Implementar el funcionamiento de la maquina de estados de facturas.

##### Escenarios fuente
> Transcripción literal del Excel (fila 18, escenario 3):
>
> 2-Cuando un usuario finaliza flujo de Habilitar, actualiza a ese estado de forma manual

##### Criterios de aceptación
1. **[Feliz]** Al finalizar el flujo **Habilitar**, el estado pasa a **Habilitada** de forma **manual** (usuario).
2. **[Validación]** Solo desde estados previos válidos (Pendiente/Bloqueada — CON-11-E1).

##### Escenarios BDD
```gherkin
Característica: 2-Cuando un usuario finaliza flujo de Habilitar, actualiza a ese…

  Escenario: Transición manual a Habilitada
    Dado una factura en estado válido para habilitar
    Cuando el usuario finaliza el flujo Habilitar
    Entonces la factura queda Habilitada
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### CON-09-E4 — 3-Cuando un usuario finaliza flujo de Bloquear, actualiza a ese…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 18 (CON-09) · escenario 4/6 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Máquina de estados (BE) — reflejada en tabs POC |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero 3-Cuando un usuario finaliza flujo de Bloquear, actualiza a ese…
para habilitar el flujo FE descrito en CON-09

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 18 para el objetivo: Implementar el funcionamiento de la maquina de estados de facturas.

##### Escenarios fuente
> Transcripción literal del Excel (fila 18, escenario 4):
>
> 3-Cuando un usuario finaliza flujo de Bloquear, actualiza a ese estado de forma manual

##### Criterios de aceptación
1. **[Feliz]** Al finalizar el flujo **Bloquear**, el estado pasa a **Bloqueada** de forma **manual**.
2. **[Validación]** Estados previos según CON-11-E2 (Excel: pendiente / habilitado / pendiente de aprobación EGP).

##### Escenarios BDD
```gherkin
Característica: 3-Cuando un usuario finaliza flujo de Bloquear, actualiza a ese…

  Escenario: Transición manual a Bloqueada
    Dado una factura en estado válido para bloquear
    Cuando el usuario finaliza el flujo Bloquear
    Entonces la factura queda Bloqueada
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### CON-09-E5 — Si la fecha de Vencimiento (documental) es menor a 30 dias pasa…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 18 (CON-09) · escenario 5/6 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Máquina de estados (BE) — reflejada en tabs POC |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero si la fecha de Vencimiento (documental) es menor a 30 dias pasa…
para habilitar el flujo FE descrito en CON-09

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 18 para el objetivo: Implementar el funcionamiento de la maquina de estados de facturas.

##### Escenarios fuente
> Transcripción literal del Excel (fila 18, escenario 5):
>
> Si la fecha de Vencimiento (documental) es menor a 30 dias pasa automaticamente a estado Vencida y ya no es operable

##### Criterios de aceptación
1. **[Feliz]** Si la **fecha de Vencimiento (documental)** es menor a 30 días, la factura pasa **automáticamente** a **Vencida** y deja de ser operable.
2. **[Feliz]** Aparece en pestaña FNV y no admite simulación/habilitación.

##### Escenarios BDD
```gherkin
Característica: Si la fecha de Vencimiento (documental) es menor a 30 dias pasa…

  Escenario: Paso automático a Vencida por vencimiento documental
    Dado una factura cuya fecha de vencimiento documental está a menos de 30 días
    Cuando corre la evaluación automática de la máquina de estados
    Entonces la factura pasa a Vencida
    Y ya no es operable
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- POC no implementa aún el job automático a Vencida; obligatorio por Excel.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### CON-09-E6 — Si la fecha de Pago es menor a 30 dias, la factura pasa a un estado…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 18 (CON-09) · escenario 6/6 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Máquina de estados (BE) — reflejada en tabs POC |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero si la fecha de Pago es menor a 30 dias, la factura pasa a un estado…
para habilitar el flujo FE descrito en CON-09

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 18 para el objetivo: Implementar el funcionamiento de la maquina de estados de facturas.

##### Escenarios fuente
> Transcripción literal del Excel (fila 18, escenario 6):
>
> Si la fecha de Pago es menor a 30 dias, la factura pasa a un estado "No elegible" (mediante modal, la EGP puede modificar fecha de Pago y se actualiza automaticamente el estado a Habilitada)

##### Criterios de aceptación
1. **[Feliz]** Si la **fecha de Pago** es menor a 30 días → estado **No elegible**.
2. **[Feliz]** Mediante modal, la EGP puede modificar la fecha de Pago y el estado se actualiza automáticamente a **Habilitada** si vuelve a ser elegible.
3. **[Feliz]** Visible en pestaña FNO.

##### Escenarios BDD
```gherkin
Característica: Si la fecha de Pago es menor a 30 dias, la factura pasa a un estado…

  Escenario: No elegible por fecha de pago y recuperación
    Dado una factura con fecha de pago a menos de 30 días
    Entonces está en No elegible
    Cuando la EGP actualiza la fecha de pago a 30 días o más
    Entonces la factura pasa automáticamente a Habilitada
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 19 — `CON-10` · API CONFIRMING - GET/estados de facturas

| | |
|---|---|
| **Issue Key Excel** | CON-10 |
| **STACK** | BE/BFF |
| **OBJETIVO (Excel)** | obtener estados de facturas |
| **Escenarios en esta fila** | 1 |

#### CON-10-E1 — Condiciones de cambio de estados de una factura a traves de la…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 19 (CON-10) · escenario 1/1 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API estados / transiciones |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero condiciones de cambio de estados de una factura a traves de la…
para habilitar el flujo FE descrito en CON-10

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 19 para el objetivo: obtener estados de facturas.

##### Escenarios fuente
> Transcripción literal del Excel (fila 19, escenario 1):
>
> Escenario de condiciones de cambio de estados de una factura a traves de la maquina de estados

##### Criterios de aceptación
1. **[Feliz]** `GET/estados de facturas` (o equivalente) expone estados y **condiciones de cambio** de la máquina.
2. **[Feliz]** El FE/BFF puede validar en cliente/servidor antes de PATCH.
3. **[Error]** Condición no cumplida → transición denegada.

##### Escenarios BDD
```gherkin
Característica: Condiciones de cambio de estados de una factura a traves de la…

  Escenario: Consultar condiciones de cambio de estado
    Cuando consulto el API de estados de facturas
    Entonces obtengo las condiciones de transición vigentes
    Y puedo determinar si un cambio solicitado es válido
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 20 — `CON-11` · Pantalla CONFIRMING - Botonera Hablitar / Bloquear | Recurso: todos | dominio: t

| | |
|---|---|
| **Issue Key Excel** | CON-11 |
| **STACK** | FE |
| **OBJETIVO (Excel)** | Botonera global de la pantalla: botón habilitar / bloquear |
| **Escenarios en esta fila** | 2 |

#### CON-11-E1 — Habiliar Factura: cambio de estado de multiples facturas en estados…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 20 (CON-11) · escenario 1/2 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#btn-habilitar-facturas` / `#btn-bloquear-facturas` |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero habiliar Factura: cambio de estado de multiples facturas en estados…
para Botonera global de la pantalla: botón habilitar / bloquear

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 20 para el objetivo: Botonera global de la pantalla: botón habilitar / bloquear.

##### Escenarios fuente
> Transcripción literal del Excel (fila 20, escenario 1):
>
> Escenario Habiliar Factura: cambio de estado de multiples facturas en estados válidos para la transicion (pendiente/bloqueado)

##### Criterios de aceptación
1. **[Feliz]** Botón **Habilitar** cambia a Habilitada **múltiples** facturas en estados válidos: **Pendiente / Bloqueada**.
2. **[Validación]** Si la selección incluye estados inválidos → acción deshabilitada o error (POC tooltips MSG-C06/C07).
3. **[Feliz]** Pide confirmación y muestra éxito (POC MSG-C12/C13).

##### Escenarios BDD
```gherkin
Característica: Habiliar Factura: cambio de estado de multiples facturas en estados…

  Escenario: Habilitar múltiples facturas
    Dado selecciono facturas en Pendiente y/o Bloqueada
    Cuando confirmo Habilitar
    Entonces todas pasan a Habilitada
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### CON-11-E2 — Bloquear Factura: cambio de estado de multiples facturas en estados…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 20 (CON-11) · escenario 2/2 |
| **Actor** | Operador del Portal Confirming (dominio según recurso) |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#btn-habilitar-facturas` / `#btn-bloquear-facturas` |

##### Historia
Como Operador del Portal Confirming (dominio según recurso)
quiero bloquear Factura: cambio de estado de multiples facturas en estados…
para Botonera global de la pantalla: botón habilitar / bloquear

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 20 para el objetivo: Botonera global de la pantalla: botón habilitar / bloquear.

##### Escenarios fuente
> Transcripción literal del Excel (fila 20, escenario 2):
>
> Escenario Bloquear Factura: cambio de estado de multiples facturas en estados válidos para la transicion (pendiente/habilitado/pendiente de aprobacion de EGP)

##### Criterios de aceptación
1. **[Feliz]** Botón **Bloquear** cambia a Bloqueada múltiples facturas en estados válidos Excel: **Pendiente / Habilitada / Pendiente de aprobación EGP**.
2. **[Validación]** Selección inválida → no ejecuta (tooltip/error).
3. **[Feliz]** Confirmación + mensaje de éxito.

##### Escenarios BDD
```gherkin
Característica: Bloquear Factura: cambio de estado de multiples facturas en estados…

  Escenario: Bloquear múltiples facturas
    Dado selecciono facturas en Pendiente, Habilitada o Pendiente aprobación EGP
    Cuando confirmo Bloquear
    Entonces todas pasan a Bloqueada
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- POC solo permite Pendiente/Habilitada para bloquear; Excel agrega Pendiente aprobación EGP — prevalece Excel.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 21 — `SIM-01` · Pantalla CONFIRMING - Simular Múltiples / Simular Individual | Recurso: todos | 

| | |
|---|---|
| **Issue Key Excel** | SIM-01 |
| **STACK** | FE |
| **OBJETIVO (Excel)** | Botonera global de la pantalla: botón simular |
| **Escenarios en esta fila** | 6 |

#### SIM-01-E1 — Simular Adelanto de múltiples factura-misma fecha de pago: abrir…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 21 (SIM-01) · escenario 1/6 |
| **Actor** | Operador Proveedor / EGP / Banco con permiso de simular |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#simulate-modal` · `#btn-simular-facturas` |

##### Historia
Como Operador Proveedor / EGP / Banco con permiso de simular
quiero simular Adelanto de múltiples factura-misma fecha de pago: abrir…
para Botonera global de la pantalla: botón simular

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 21 para el objetivo: Botonera global de la pantalla: botón simular.

##### Escenarios fuente
> Transcripción literal del Excel (fila 21, escenario 1):
>
> Escenario Simular Adelanto de múltiples factura-misma fecha de pago: abrir modal de Simulación de Adelanto para multiples facturas en estados válidos (Habilitada), con los calculos unificados, VALIDACION: si múltiples facturas correspondan a mismo EGP-Proveedor Y misma moneda, entonces permite simular multiple y genera la solicitud de un mismo prestamo en 1 cuota, sino error

##### Criterios de aceptación
1. **[Feliz]** Simular múltiples con **misma fecha de pago**, mismo EGP-Proveedor-Moneda, estado Habilitada → modal con cálculos unificados.
2. **[Feliz]** Genera solicitud de **un mismo préstamo en 1 cuota**.
3. **[Error]** Si no comparten EGP-Proveedor-Moneda → error y no abre simulación válida.

##### Escenarios BDD
```gherkin
Característica: Simular Adelanto de múltiples factura-misma fecha de pago: abrir…

  Escenario: Simulación masiva misma fecha de pago (1 cuota)
    Dado ≥2 facturas Habilitada mismo EGP, Proveedor, Moneda y misma fecha de pago
    Cuando simulo el lote
    Entonces veo el modal con cálculos unificados
    Y la solicitud generada es un préstamo en 1 cuota
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-01-E2 — Simular Adelanto de múltiples factura-fecha de pago distinta: abrir…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 21 (SIM-01) · escenario 2/6 |
| **Actor** | Operador Proveedor / EGP / Banco con permiso de simular |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#simulate-modal` · `#btn-simular-facturas` |

##### Historia
Como Operador Proveedor / EGP / Banco con permiso de simular
quiero simular Adelanto de múltiples factura-fecha de pago distinta: abrir…
para Botonera global de la pantalla: botón simular

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 21 para el objetivo: Botonera global de la pantalla: botón simular.

##### Escenarios fuente
> Transcripción literal del Excel (fila 21, escenario 2):
>
> Escenario Simular Adelanto de múltiples factura-fecha de pago distinta: abrir modal de Simulación de Adelanto para multiples facturas en estados válidos (Habilitada), con los calculos unificados, VALIDACION: si múltiples facturas correspondan a mismo EGP-Proveedor Y misma moneda, entonces permite simular multiple y genera la solicitud de un mismo prestamo en n cuotas segun fecha de pago, sino error

##### Criterios de aceptación
1. **[Feliz]** Simular múltiples con **fechas de pago distintas**, mismo EGP-Proveedor-Moneda → modal unificado.
2. **[Feliz]** Genera solicitud de **un mismo préstamo en N cuotas** según fechas de pago.
3. **[Error]** Combinatoria inválida → error.

##### Escenarios BDD
```gherkin
Característica: Simular Adelanto de múltiples factura-fecha de pago distinta: abrir…

  Escenario: Simulación masiva fechas de pago distintas (N cuotas)
    Dado ≥2 facturas Habilitada mismo EGP-Proveedor-Moneda con fechas de pago distintas
    Cuando simulo el lote
    Entonces el préstamo se estructura en N cuotas según las fechas de pago
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- POC no implementa N cuotas; obligatorio por Excel.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-01-E3 — Simular Adelanto de factura individual: abrir modal de Simulación de…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 21 (SIM-01) · escenario 3/6 |
| **Actor** | Operador Proveedor / EGP / Banco con permiso de simular |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#simulate-modal` · `#btn-simular-facturas` |

##### Historia
Como Operador Proveedor / EGP / Banco con permiso de simular
quiero simular Adelanto de factura individual: abrir modal de Simulación de…
para Botonera global de la pantalla: botón simular

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 21 para el objetivo: Botonera global de la pantalla: botón simular.

##### Escenarios fuente
> Transcripción literal del Excel (fila 21, escenario 3):
>
> Escenario Simular Adelanto de factura individual: abrir modal de Simulación de Adelanto para la factura seleccionada en un estado valido (Habilitada), con los calculo individual, genera la solicitud de un prestamo en 1 cuota

##### Criterios de aceptación
1. **[Feliz]** Simular individual sobre factura Habilitada abre modal con cálculo individual.
2. **[Feliz]** Genera solicitud de préstamo en **1 cuota**.
3. **[Validación]** Solo estado Habilitada.

##### Escenarios BDD
```gherkin
Característica: Simular Adelanto de factura individual: abrir modal de Simulación de…

  Escenario: Simulación individual
    Dado una factura Habilitada
    Cuando abro Simular
    Entonces veo el cálculo individual
    Y al confirmar se solicita un préstamo en 1 cuota
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-01-E4 — VALIDACION que el EGP tenga limite suficiente para realizar el…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 21 (SIM-01) · escenario 4/6 |
| **Actor** | Operador Proveedor / EGP / Banco con permiso de simular |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#simulate-modal` · `#btn-simular-facturas` |

##### Historia
Como Operador Proveedor / EGP / Banco con permiso de simular
quiero vALIDACION que el EGP tenga limite suficiente para realizar el…
para Botonera global de la pantalla: botón simular

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 21 para el objetivo: Botonera global de la pantalla: botón simular.

##### Escenarios fuente
> Transcripción literal del Excel (fila 21, escenario 4):
>
> Escenario VALIDACION que el EGP tenga limite suficiente para realizar el adelanto (se grisan/bloquean las facturas que excedan del limite de credito del cEGP)

##### Criterios de aceptación
1. **[Validación]** Si el adelanto excede el límite de crédito disponible del EGP, esas facturas se **grisan/bloquean** y no se pueden simular.
2. **[Feliz]** Solo se habilitan para simulación las que entran en el límite.

##### Escenarios BDD
```gherkin
Característica: VALIDACION que el EGP tenga limite suficiente para realizar el…

  Escenario: Tope de límite de crédito en simulación
    Dado un EGP con límite disponible insuficiente para una factura
    Cuando intento incluirla en la simulación
    Entonces la factura aparece grisada/bloqueada por límite
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-01-E5 — CONFIRMACIÓN, al crearse una simulación se freeza el limite de…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 21 (SIM-01) · escenario 5/6 |
| **Actor** | Operador Proveedor / EGP / Banco con permiso de simular |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#simulate-modal` · `#btn-simular-facturas` |

##### Historia
Como Operador Proveedor / EGP / Banco con permiso de simular
quiero cONFIRMACIÓN, al crearse una simulación se freeza el limite de…
para Botonera global de la pantalla: botón simular

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 21 para el objetivo: Botonera global de la pantalla: botón simular.

##### Escenarios fuente
> Transcripción literal del Excel (fila 21, escenario 5):
>
> Escenario de CONFIRMACIÓN, al crearse una simulación se freeza el limite de credito correspondiente y se descuenta del limite crediticio total del EGP

##### Criterios de aceptación
1. **[Feliz]** Al **confirmar** la simulación se **freeza** el límite de crédito correspondiente.
2. **[Feliz]** El freeze se descuenta del límite total mostrado (CON-07-E3).
3. **[Validación]** Si la operación falla después, se revierte el freeze (SIM-03-E5/E6).

##### Escenarios BDD
```gherkin
Característica: CONFIRMACIÓN, al crearse una simulación se freeza el limite de…

  Escenario: Freeze de límite al confirmar simulación
    Dado una simulación válida
    Cuando confirmo la simulación
    Entonces se freeza el monto correspondiente en el límite del EGP
    Y el límite disponible se reduce en ese monto
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-01-E6 — Para todos los calculos en el modal de simulacion siempre debera…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 21 (SIM-01) · escenario 6/6 |
| **Actor** | Operador Proveedor / EGP / Banco con permiso de simular |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#simulate-modal` · `#btn-simular-facturas` |

##### Historia
Como Operador Proveedor / EGP / Banco con permiso de simular
quiero para todos los calculos en el modal de simulacion siempre debera…
para Botonera global de la pantalla: botón simular

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 21 para el objetivo: Botonera global de la pantalla: botón simular.

##### Escenarios fuente
> Transcripción literal del Excel (fila 21, escenario 6):
>
> Para todos los calculos en el modal de simulacion siempre debera figurar "los valores simulados son estimativos... " o algo por el estilo

##### Criterios de aceptación
1. **[Feliz]** En el modal de simulación, para todos los cálculos, se muestra la leyenda de que **los valores simulados son estimativos**.
2. **[Validación]** La leyenda es visible antes de confirmar.

##### Escenarios BDD
```gherkin
Característica: Para todos los calculos en el modal de simulacion siempre debera…

  Escenario: Leyenda de valores estimativos
    Dado el modal de Simulación de Adelanto
    Entonces veo el aviso de que los valores simulados son estimativos
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- Copy sugerido POC/UX: “Los valores simulados son estimativos…”.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 22 — `SIM-02` · API CONFIRMING - GET/simularAdelantoFactura

| | |
|---|---|
| **Issue Key Excel** | SIM-02 |
| **STACK** | BE/BFF |
| **OBJETIVO (Excel)** | Obtener información de los calculos financieros a mostrar en el modal de simulación de adelanto y limites crediticios actualizados |
| **Escenarios en esta fila** | 3 |

#### SIM-02-E1 — Donde se muestran todos los datos OK del calculo

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 22 (SIM-02) · escenario 1/3 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API `GET` simular adelanto |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero donde se muestran todos los datos OK del calculo
para habilitar el flujo FE descrito en SIM-02

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 22 para el objetivo: Obtener información de los calculos financieros a mostrar en el modal de simulación de adelanto y limites crediticios actualizados.

##### Escenarios fuente
> Transcripción literal del Excel (fila 22, escenario 1):
>
> Escenario donde se muestran todos los datos OK del calculo

##### Criterios de aceptación
1. **[Feliz]** `GET/simularAdelantoFactura` devuelve todos los datos del cálculo y límites crediticios actualizados.
2. **[Feliz]** El FE pinta el ticket completo (interés, comisión, IVA, neto, días, límite).

##### Escenarios BDD
```gherkin
Característica: Donde se muestran todos los datos OK del calculo

  Escenario: Cálculo OK
    Cuando consulto GET/simularAdelantoFactura con parámetros válidos
    Entonces recibo el desglose financiero completo y límites actualizados
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-02-E2 — Con error al mostrar datos del calculo

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 22 (SIM-02) · escenario 2/3 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API `GET` simular adelanto |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero con error al mostrar datos del calculo
para habilitar el flujo FE descrito en SIM-02

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 22 para el objetivo: Obtener información de los calculos financieros a mostrar en el modal de simulación de adelanto y limites crediticios actualizados.

##### Escenarios fuente
> Transcripción literal del Excel (fila 22, escenario 2):
>
> Escenario con error al mostrar datos del calculo

##### Criterios de aceptación
1. **[Error]** Si el cálculo no puede obtenerse, el API responde error y el FE informa el fallo (sin datos parciales engañosos).

##### Escenarios BDD
```gherkin
Característica: Con error al mostrar datos del calculo

  Escenario: Error al obtener cálculo
    Cuando GET/simularAdelantoFactura falla
    Entonces el FE muestra error
    Y no permite confirmar un adelanto sin ticket válido
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-02-E3 — VALIDACION de limite de tiempo desde que el EGP aprobo la factura y…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 22 (SIM-02) · escenario 3/3 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API `GET` simular adelanto |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero vALIDACION de limite de tiempo desde que el EGP aprobo la factura y…
para habilitar el flujo FE descrito en SIM-02

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 22 para el objetivo: Obtener información de los calculos financieros a mostrar en el modal de simulación de adelanto y limites crediticios actualizados.

##### Escenarios fuente
> Transcripción literal del Excel (fila 22, escenario 3):
>
> Escenario de VALIDACION de limite de tiempo desde que el EGP aprobo la factura y se solicito el adelanto (variable de configuracion n dias para bloquear adelantos ante expiracion)

##### Criterios de aceptación
1. **[Validación]** Se valida el **límite de tiempo** (variable de configuración N días) desde que el EGP aprobó la factura hasta la solicitud de adelanto.
2. **[Error]** Si expiró → se bloquea el adelanto con mensaje claro.

##### Escenarios BDD
```gherkin
Característica: VALIDACION de limite de tiempo desde que el EGP aprobo la factura y…

  Escenario: Expiración de ventana de adelanto
    Dado que pasaron más de N días desde la aprobación EGP de la factura
    Cuando intento simular/solicitar adelanto
    Entonces el sistema bloquea la operación por expiración
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- Parametrizar N días (config). Spike S-CF-03 si no está definido.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 23 — `SIM-03` · API CONFIRMING - POST/generarAdelantoFactura

| | |
|---|---|
| **Issue Key Excel** | SIM-03 |
| **STACK** | BE/BFF |
| **OBJETIVO (Excel)** | Crear solicitud de adelanto factura |
| **Escenarios en esta fila** | 6 |

#### SIM-03-E1 — Creación de factura OK y se envia solicitud al CORE (relacion cuenta…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 23 (SIM-03) · escenario 1/6 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API `POST` generar adelanto |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero creación de factura OK y se envia solicitud al CORE (relacion cuenta…
para habilitar el flujo FE descrito en SIM-03

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 23 para el objetivo: Crear solicitud de adelanto factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 23, escenario 1):
>
> Escenario creación de factura OK y se envia solicitud al CORE (relacion cuenta prestamo - factura que componen el prestamo / en core se guarda el num de factura)

##### Criterios de aceptación
1. **[Feliz]** `POST/generarAdelantoFactura` OK crea la solicitud y **envía al CORE** la relación cuenta préstamo–factura(s) (CORE guarda nro de factura).
2. **[Feliz]** Responde OK al FE y habilita notificaciones (SIM-04-E1/E3).

##### Escenarios BDD
```gherkin
Característica: Creación de factura OK y se envia solicitud al CORE (relacion cuenta…

  Escenario: Generación OK con envío a CORE
    Cuando POST/generarAdelantoFactura es exitoso
    Entonces se crea la solicitud de adelanto
    Y se envía al CORE la relación préstamo-factura
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- Excel dice “creación de factura OK” en escenario de adelanto — se interpreta como creación de solicitud de adelanto.

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-03-E2 — Creación de factura con ERROR y NO se envia solicitud al CORE

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 23 (SIM-03) · escenario 2/6 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API `POST` generar adelanto |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero creación de factura con ERROR y NO se envia solicitud al CORE
para habilitar el flujo FE descrito en SIM-03

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 23 para el objetivo: Crear solicitud de adelanto factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 23, escenario 2):
>
> Escenario creación de factura con ERROR y NO se envia solicitud al CORE

##### Criterios de aceptación
1. **[Error]** Si falla la generación, **no** se envía solicitud al CORE.
2. **[Error]** No se notifica éxito (SIM-04-E2/E4).

##### Escenarios BDD
```gherkin
Característica: Creación de factura con ERROR y NO se envia solicitud al CORE

  Escenario: Error sin envío a CORE
    Cuando POST/generarAdelantoFactura falla
    Entonces no se envía solicitud al CORE
    Y la operación se informa como error al FE
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-03-E3 — VALIDACION usuario que solicita adelanto no es el mismo que cargo la…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 23 (SIM-03) · escenario 3/6 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API `POST` generar adelanto |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero vALIDACION usuario que solicita adelanto no es el mismo que cargo la…
para habilitar el flujo FE descrito en SIM-03

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 23 para el objetivo: Crear solicitud de adelanto factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 23, escenario 3):
>
> Escenario de VALIDACION usuario que solicita adelanto no es el mismo que cargo la factura

##### Criterios de aceptación
1. **[Validación]** El usuario que solicita el adelanto **no** puede ser el mismo que cargó la factura (segregación de funciones).
2. **[Error]** Si es el mismo usuario → rechazo con mensaje de validación.

##### Escenarios BDD
```gherkin
Característica: VALIDACION usuario que solicita adelanto no es el mismo que cargo la…

  Escenario: Segregación: solicitante ≠ cargador
    Dado que el usuario actual es quien cargó la factura
    Cuando intenta generar el adelanto
    Entonces el sistema rechaza la operación por validación de usuario
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-03-E4 — VALIDACION usuario que solicita adelanto lo está haciendo antes de…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 23 (SIM-03) · escenario 4/6 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API `POST` generar adelanto |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero vALIDACION usuario que solicita adelanto lo está haciendo antes de…
para habilitar el flujo FE descrito en SIM-03

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 23 para el objetivo: Crear solicitud de adelanto factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 23, escenario 4):
>
> Escenario de VALIDACION usuario que solicita adelanto lo está haciendo antes de las 17hs

##### Criterios de aceptación
1. **[Validación]** La solicitud de adelanto solo se permite **antes de las 17:00** (hora Paraguay / configuración).
2. **[Error]** Fuera de horario → rechazo con mensaje.

##### Escenarios BDD
```gherkin
Característica: VALIDACION usuario que solicita adelanto lo está haciendo antes de…

  Escenario: Ventana horaria antes de las 17hs
    Dado que la hora actual es 17:00 o posterior
    Cuando intento generar adelanto
    Entonces el sistema rechaza por fuera de horario operativo
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-03-E5 — Reversion automatica ante respuesta de error del servicio

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 23 (SIM-03) · escenario 5/6 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API `POST` generar adelanto |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero reversion automatica ante respuesta de error del servicio
para habilitar el flujo FE descrito en SIM-03

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 23 para el objetivo: Crear solicitud de adelanto factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 23, escenario 5):
>
> Escenario reversion automatica ante respuesta de error del servicio

##### Criterios de aceptación
1. **[Error]** Ante respuesta de error del servicio/CORE se ejecuta **reversión automática** de la operación (estado/freeze).
2. **[Feliz]** El FE informa el error tras la reversión.

##### Escenarios BDD
```gherkin
Característica: Reversion automatica ante respuesta de error del servicio

  Escenario: Reversión automática por error
    Dado que el CORE/servicio responde error
    Cuando se procesa la respuesta
    Entonces se revierte automáticamente el efecto parcial de la solicitud
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-03-E6 — Re-calculo de limite crediticio - freeze de la simulación de adelanto

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 23 (SIM-03) · escenario 6/6 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | API `POST` generar adelanto |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero re-calculo de limite crediticio - freeze de la simulación de adelanto
para habilitar el flujo FE descrito en SIM-03

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 23 para el objetivo: Crear solicitud de adelanto factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 23, escenario 6):
>
> Re-calculo de limite crediticio - freeze de la simulación de adelanto

##### Criterios de aceptación
1. **[Feliz]** Se **recalcula** el límite crediticio aplicando el **freeze** de la simulación/adelanto confirmado.
2. **[Feliz]** CON-07 refleja el nuevo disponible.
3. **[Error]** Si hay reversión, se libera el freeze.

##### Escenarios BDD
```gherkin
Característica: Re-calculo de limite crediticio - freeze de la simulación de adelanto

  Escenario: Recálculo y freeze de límite
    Cuando se confirma la generación de adelanto
    Entonces el límite freezado se actualiza
    Y el disponible mostrado es límite API − freeze
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 24 — `SIM-04` · API CONFIRMING - POST/notificaciónAdelantoFactura | Recurso: EGP/PROVEEDOR | Dom

| | |
|---|---|
| **Issue Key Excel** | SIM-04 |
| **STACK** | BFF |
| **OBJETIVO (Excel)** | Notificación de creación de factura |
| **Escenarios en esta fila** | 4 |

#### SIM-04-E1 — Adelanto de factura OK, se envia NOTIFICACION al EGP del pedido de…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 24 (SIM-04) · escenario 1/4 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Notificación adelanto (BFF) |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero adelanto de factura OK, se envia NOTIFICACION al EGP del pedido de…
para habilitar el flujo FE descrito en SIM-04

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 24 para el objetivo: Notificación de creación de factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 24, escenario 1):
>
> Escenario adelanto de factura OK, se envia NOTIFICACION al EGP del pedido de adelanto

##### Criterios de aceptación
1. **[Feliz]** Adelanto OK → se envía notificación al **EGP** del pedido de adelanto.

##### Escenarios BDD
```gherkin
Característica: Adelanto de factura OK, se envia NOTIFICACION al EGP del pedido de…

  Escenario: Notificación EGP en adelanto OK
    Dado adelanto generado OK
    Entonces el EGP recibe notificación del pedido de adelanto
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-04-E2 — Adelanto de factura con ERROR, NO se envia NOTIFICACION al EGP del…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 24 (SIM-04) · escenario 2/4 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Notificación adelanto (BFF) |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero adelanto de factura con ERROR, NO se envia NOTIFICACION al EGP del…
para habilitar el flujo FE descrito en SIM-04

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 24 para el objetivo: Notificación de creación de factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 24, escenario 2):
>
> Escenario adelanto  de factura con ERROR, NO se envia NOTIFICACION al EGP del pedido de adelanto

##### Criterios de aceptación
1. **[Error]** Adelanto con ERROR → **no** se envía notificación al EGP.

##### Escenarios BDD
```gherkin
Característica: Adelanto de factura con ERROR, NO se envia NOTIFICACION al EGP del…

  Escenario: Sin notificación EGP si error
    Dado adelanto con ERROR
    Entonces no se envía notificación al EGP
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-04-E3 — Adelanto de factura OK, se envia NOTIFICACION al PROVEEDOR del…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 24 (SIM-04) · escenario 3/4 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Notificación adelanto (BFF) |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero adelanto de factura OK, se envia NOTIFICACION al PROVEEDOR del…
para habilitar el flujo FE descrito en SIM-04

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 24 para el objetivo: Notificación de creación de factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 24, escenario 3):
>
> Escenario adelanto de factura OK, se envia NOTIFICACION al PROVEEDOR del CREDITO GENERADO

##### Criterios de aceptación
1. **[Feliz]** Adelanto OK → se envía notificación al **Proveedor** del **crédito generado**.

##### Escenarios BDD
```gherkin
Característica: Adelanto de factura OK, se envia NOTIFICACION al PROVEEDOR del…

  Escenario: Notificación Proveedor crédito generado
    Dado adelanto generado OK
    Entonces el Proveedor recibe notificación del crédito generado
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-04-E4 — Adelanto de factura con ERROR, NO se envia NOTIFICACION al PROVEEDOR…

| | |
|---|---|
| **Tipo** | HT |
| **Épica** | CONFIRMING |
| **Fila Excel** | 24 (SIM-04) · escenario 4/4 |
| **Actor** | Sistema / BFF-BE Confirming |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | Notificación adelanto (BFF) |

##### Historia
Como consumidor del BFF/BE de Confirming
quiero adelanto de factura con ERROR, NO se envia NOTIFICACION al PROVEEDOR…
para habilitar el flujo FE descrito en SIM-04

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 24 para el objetivo: Notificación de creación de factura.

##### Escenarios fuente
> Transcripción literal del Excel (fila 24, escenario 4):
>
> Escenario adelanto  de factura con ERROR, NO se envia NOTIFICACION al PROVEEDOR de LA FACTURA GENERADA

##### Criterios de aceptación
1. **[Error]** Adelanto con ERROR → **no** se envía notificación al Proveedor.
2. **[Nota]** Excel menciona “LA FACTURA GENERADA” en el error de proveedor; se interpreta como no notificar crédito/factura de adelanto inexistente.

##### Escenarios BDD
```gherkin
Característica: Adelanto de factura con ERROR, NO se envia NOTIFICACION al PROVEEDOR…

  Escenario: Sin notificación Proveedor si error
    Dado adelanto con ERROR
    Entonces no se envía notificación al Proveedor
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### Fila 25 — `SIM-05` · Pantalla CONFIRMING - Aprobación / Rechazo de Simulación de Adelante de Factura 

| | |
|---|---|
| **Issue Key Excel** | SIM-05 |
| **STACK** | FE |
| **OBJETIVO (Excel)** | Flujos de Aprobación y Rechazos de simulación de adelanto por parte del usuario aprobador EGP |
| **Escenarios en esta fila** | 2 |

#### SIM-05-E1 — Aprobación del adelanto por parte del EGP para avanzar con el…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 25 (SIM-05) · escenario 1/2 |
| **Actor** | Aprobador EGP |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#simulate-modal` approve/reject EGP |

##### Historia
Como Aprobador EGP
quiero aprobación del adelanto por parte del EGP para avanzar con el…
para Flujos de Aprobación y Rechazos de simulación de adelanto por parte del usuario aprobador EGP

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 25 para el objetivo: Flujos de Aprobación y Rechazos de simulación de adelanto por parte del usuario aprobador EGP.

##### Escenarios fuente
> Transcripción literal del Excel (fila 25, escenario 1):
>
> Escenario de Aprobación del adelanto por parte del EGP para avanzar con el desembolso solicitado por el usuario Proveedor

##### Criterios de aceptación
1. **[Feliz]** El aprobador EGP **aprueba** el adelanto solicitado por el Proveedor y el flujo avanza al **desembolso**.
2. **[Feliz]** La factura pasa a Pendiente de desembolso (o equivalente de máquina) y se muestra “Desembolso en curso...” (CON-02-E4).
3. **[Feliz]** Feedback de éxito al aprobador.

##### Escenarios BDD
```gherkin
Característica: Aprobación del adelanto por parte del EGP para avanzar con el…

  Escenario: Aprobación EGP del adelanto
    Dado un adelanto pendiente de aprobación EGP
    Cuando el aprobador EGP aprueba
    Entonces se avanza el desembolso solicitado por el Proveedor
    Y el estado de la factura refleja el desembolso en curso
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

#### SIM-05-E2 — Rechazo del adelanto por parte del EGP para avanzar con el…

| | |
|---|---|
| **Tipo** | HU-FE |
| **Épica** | CONFIRMING |
| **Fila Excel** | 25 (SIM-05) · escenario 2/2 |
| **Actor** | Aprobador EGP |
| **Dominios** | Según Summary Excel (recurso/dominio) |
| **Prioridad sugerida** | Must |
| **Pantalla / contrato POC** | `#simulate-modal` approve/reject EGP |

##### Historia
Como Aprobador EGP
quiero rechazo del adelanto por parte del EGP para avanzar con el…
para Flujos de Aprobación y Rechazos de simulación de adelanto por parte del usuario aprobador EGP

##### Valor de negocio
Cubre el escenario comprometido en `Confirming.xlsx` fila 25 para el objetivo: Flujos de Aprobación y Rechazos de simulación de adelanto por parte del usuario aprobador EGP.

##### Escenarios fuente
> Transcripción literal del Excel (fila 25, escenario 2):
>
> Escenario de Rechazo del adelanto por parte del EGP para avanzar con el desembolso solicitado por el usuario Proveedor, con o sin motivo.

##### Criterios de aceptación
1. **[Feliz]** El EGP puede **rechazar con motivo** o **sin motivo** el adelanto solicitado por el Proveedor.
2. **[Feliz]** Rechazo con motivo: captura motivo/nueva fecha según reglas (alineado CON-05 / CON-09-E6).
3. **[Feliz]** Rechazo sin motivo: bloquea/cierra según máquina de estados.
4. **[Feliz]** Se libera freeze de límite si correspondía.

##### Escenarios BDD
```gherkin
Característica: Rechazo del adelanto por parte del EGP para avanzar con el…

  Escenario: Rechazo EGP con o sin motivo
    Dado un adelanto pendiente de aprobación EGP
    Cuando el EGP rechaza con motivo
    Entonces la factura vuelve a un estado operable según la regla de fecha/motivo
    Cuando el EGP rechaza sin motivo
    Entonces la factura queda bloqueada o en el estado definido por la máquina
```

##### Fuera de alcance
- Alcance no descrito en este escenario del Excel.

##### Notas / preguntas abiertas
- —

##### Chequeo INVEST
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## 7. Spikes / dudas

| ID | Origen | Pregunta | Propuesta |
|----|--------|----------|-----------|
| S-CF-01 | FAC-02-E3 | ¿Escaneo de facturas entra en el MVP? (Excel trae “?”) | Timebox; POC solo demo |
| S-CF-02 | CON-06 | ¿Baja lógica o física al eliminar? | Preferir baja lógica + auditoría |
| S-CF-03 | SIM-02-E3 | Valor de N días de ventana post-aprobación EGP | Definir con negocio/riesgo |
| S-CF-04 | SIM-01-E2 | Modelo de N cuotas en CORE por fechas de pago distintas | Diseño con CORE |
| S-CF-05 | SIM-03-E4 | Zona horaria y feriados para corte 17:00 | America/Asuncion |

## 8. Recomendaciones (no están como escenario en el Excel)

| ID | Recomendación | Por qué | Prioridad |
|----|---------------|---------|-----------|
| R-CF-01 | Enforcement runtime de permisos Confirming (catálogo ABM 21 ítems) | Excel asume recurso/dominio pero no detalla matriz | Alta |
| R-CF-02 | Auditoría de transiciones y de freeze de límite | Requisito bancario | Alta |
| R-CF-03 | Revertir adelanto / 2da aprobación | Presente en permisos POC, no en Excel | Media |
| R-CF-04 | Aprobación banco manual | Residual en POC; Excel apunta a desembolso post-EGP | Baja salvo negocio lo pida |
| R-CF-05 | Unificar keys duplicados FAC-05 / CON-03 en el Excel | Evita colisiones Jira | Alta (higiene) |

## 9. Observaciones de consistencia del Excel

1. **Keys duplicados:** `FAC-05` (filas 7 y 8) y `CON-03` (filas 10 y 12). En este doc: `FAC-05-a`, `CON-03-a`.
2. **CON-06 escenarios** repite texto de consulta de grilla; el OBJETIVO habla de PATCH/actualizar — se elaboró por OBJETIVO.
3. **SIM-03** dice “creación de factura” en escenarios de `generarAdelantoFactura` — interpretado como solicitud de adelanto (SUP-03).
4. **SIM-04-E4** texto “NOTIFICACION al PROVEEDOR de LA FACTURA GENERADA” en rama de error — interpretado como no notificar crédito.
5. **FAC-02** “scanear facturas?” con interrogación — spike S-CF-01.
6. **CON-11 bloquear** incluye Pendiente aprobación EGP; la POC no — prevalece Excel.
7. **CON-09** manda nacer en Pendiente; la POC permite elegir estado inicial — prevalece Excel.

## 10. Trazabilidad HU ↔ POC

| Historias | POC |
|-----------|-----|
| FAC-01-* / FAC-02-* / FAC-04-* | Modal Cargar Factura, bulk, scan demo, moneda |
| CON-01-* | Tabs FV/FNV/FNO + filtros + grilla |
| CON-02-* / CON-03-a / CON-04 / CON-05 | Acciones de fila + modales |
| CON-07-* | Panel ente topbar |
| CON-09-* / CON-11-* | Estados + habilitar/bloquear |
| SIM-01-* / SIM-05-* | Modal simulación / aprobación EGP |
| FAC-03/05*, CON-03/06/08/10, SIM-02/03/04 | Sin backend real en POC — contratos a implementar |

Guía de recorrido: `assets/poc-pantallas-confirming.md`.

## 11. DoR / DoD

**DoR:** escenario Excel trazado · AC binarios · Gherkin ES · MSG/RN referenciados · dependencia API clara · POC de referencia si FE · estimado.

**DoD:** AC demo OK · BDD verificado · mensajes según §5 · máquina de estados/freeze consistentes · notificaciones solo en ramas OK · permisos de dominio aplicados.

---

*Fin v2.0.0 — 58 tarjetas (1 por escenario) · fuente `Confirming.xlsx`.*
