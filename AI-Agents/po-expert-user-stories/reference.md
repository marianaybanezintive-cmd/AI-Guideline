# Referencia — Product Owner y calidad de historias

## INVEST (recordatorio breve)

- **I**ndependiente: minimizar acoplamiento entre historias.
- **N**egociable: detalle conversacional; esta skill ya aporta el detalle inicial.
- **V**aliosa: cada historia entrega valor al usuario o al negocio.
- **E**stimable: suficiente claridad para sizing; si no, spike aparte.
- **S**mall: cabe en un sprint típico del equipo destino.
- **T**estable: criterios y Gherkin verificables.

## Partir épicas sin perder valor

- Por defecto: separar por **resultado de usuario** (no por capa técnica).
- **Excepción Excel** (columnas canónicas): sí separar / etiquetar **BE / FE / BFF** según [excel-input.md](excel-input.md).
- Extraer **spikes** cuando falte exploración (POC, integración desconocida).
- Agrupar **reglas transversales** (RGPD, auditoría) en historias dedicadas si afectan a múltiples flujos.

## Criterios de aceptación sólidos

- Formulación **observable** ("se muestra", "se registra", "no se permite") en lugar de "está implementado".
- Incluir **límites**: volúmenes, timeouts visibles al usuario, formatos, idiomas, permisos.
- Alinear criterios con **escenarios Gherkin** sin repetirlos palabra por palabra.
- **No** etiquetar criterios como `[Feliz]`, `[Alternativo]`, `[Error]`, `[Validación]` ni `Criterio N: […]`. Esa clasificación va solo en Escenarios BDD.

## Story map → historias

- Cada **tarjeta de actividad** puede generar una o varias historias según variaciones de actor o canal.
- Los **releases** del mapa sugieren orden; las dependencias técnicas pueden invertir el orden: documentar por qué.

## Diagramas

- **Estados**: un escenario Gherkin por transición crítica o por regla de entrada/salida.
- **Secuencia**: "Cuando" suele alinearse al mensaje o acción que dispara el siguiente paso.
- **Dominio**: nombres de entidades del diagrama deben aparecer en COMO/QUIERO/PARA o en los pasos para trazabilidad.

## Entregables (recordatorio)

- El **`.md`** es el entregable canónico: todas las historias completas, no un resumen.
- **CSV**: 4 columnas; delimitador **`;`**; **un registro lógico por HU** (`Issue Key`).
- Description: LF reales dentro de `"…"` (Alt+Enter). Sin `\n` literal. Sin bloque Metadatos.
- Orden: Escenarios BDD (Gherkin) completo → Criterios (“Que …”) → Fuera de alcance → Notas / preguntas abiertas.
- Detalle CSV: [csv-schema.md](csv-schema.md).
