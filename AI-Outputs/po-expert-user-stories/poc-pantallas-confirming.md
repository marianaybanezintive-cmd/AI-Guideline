# POC — Pantalla CONFIRMING (guía de recorrido)

> **Historias:** `assets/historias-usuario-confirming_v1.0.0.md`  
> **URL publicada:** https://marianaintive.github.io/atlas-confirming-poc/  
> **Entrada:** *Ingresar sin credenciales (modo demo)* → nav **Confirming**

La máquina de estados, validaciones y mensajes están simulados en `app.js` (sin backend).

---

## 1. Regiones de la pantalla

| Región | Qué probar | HU |
|--------|------------|-----|
| Topbar **Estás operando para el ente** | Filtra grilla + muestra panel TNA/comisión/IVA | CO-02 |
| Filtros (buscar, vto, fecha pago, estado) | Combinan con pestaña | CO-01 |
| Tabs Vigentes / No vigentes / No operables | Partición RN-C02 | CO-01 |
| Botones Habilitar / Bloquear / Simular | Tooltips y reglas de selección | CO-07…CO-10 |
| Cargar Factura | Alta manual, QR demo, template, bulk | CO-03…CO-05, CO-16 |
| Acciones por fila | Simular, Aprobar EGP, Editar fecha pago, Eliminar | CO-06, CO-09, CO-11…CO-15 |

---

## 2. Recorridos sugeridos

### 2.1 Feliz: Pendiente → Habilitada → Adelanto → Financiada

1. Tab **Vigentes**, seleccionar factura **Pendiente** → **Habilitar** (CO-07).
2. Con **Habilitada**, **Simular** → revisar ticket → **Ejecutar Adelanto** (CO-09).
3. Estado **Pendiente aprobación EGP** → **Aprobar EGP** (CO-11).
4. Espera ~2,5 s: CORE OK → **Financiada** (CO-14) o error → vuelve a Pendiente EGP.

### 2.2 Rechazos EGP

1. Factura en Pendiente aprobación EGP → **Rechazar con motivo** (nueva fecha) (CO-12).
2. O **Rechazar sin motivo** → **Bloqueada** (CO-13).

### 2.3 Elegibilidad 30 días

1. Alta con fecha de pago &lt; 30 días → **NO ELEGIBLE** (CO-03).
2. Tab **No operables** → **Editar fecha de pago** ≥ 30 días → **Habilitada** (CO-06).

### 2.4 Masivo

1. Seleccionar ≥2 **Habilitada** mismo EGP+Proveedor+Moneda → **Simular** cabecera (CO-10).
2. Cargar Excel/CSV desde modal (CO-05); descargar template primero (CO-16).

---

## 3. Mocks útiles

Hay ≥2 facturas por cada estado en `invoices` (`app.js`). Estados: Pendiente, Habilitada, Bloqueada, Pendiente aprobación EGP, Pendiente de desembolso, Financiada, Vencida, NO ELEGIBLE.

---

## 4. Limitaciones POC (no confundir con producto)

- Sin chequeo runtime de permisos Confirming (R-01).
- Aprobación banco manual y Revertir: stubs / residuales (R-02, R-03).
- CORE BANKING con error aleatorio ~15% (solo demo).
- Rechazo con motivo usa `window.prompt` (mejorar a modal en producto).
