# Referencia — Product Owner y calidad de historias

## INVEST (recordatorio breve)

- **I**ndependiente: minimizar acoplamiento entre historias.
- **N**egociable: detalle conversacional; esta skill ya aporta el detalle inicial.
- **V**aliosa: cada historia entrega valor al usuario o al negocio.
- **E**stimable: suficiente claridad para sizing; si no, spike en §9.
- **S**mall: cabe en un sprint típico del equipo destino.
- **T**estable: criterios y Gherkin verificables.

Documentar el chequeo INVEST en cada tarjeta HU (§6) con ✅ / ⚠️ / ❌ por dimensión.

## Partir épicas sin perder valor

- Por defecto: separar por **resultado de usuario** (no por capa técnica).
- **Excepción Excel** (columnas canónicas): sí separar / etiquetar **BE / FE / BFF** según [excel-input.md](excel-input.md).
- Extraer **spikes** a §9 cuando falte exploración (POC, integración desconocida).
- Agrupar **reglas transversales** en §4 (RN) si afectan a múltiples flujos.

## Criterios de aceptación sólidos

- Formulación **observable** («se muestra», «se registra», «no se permite»).
- Incluir **límites**: volúmenes, timeouts visibles al usuario, formatos, permisos.
- **Numerados** con tags de camino: `[Feliz]`, `[Alternativo]`, `[Error]`, `[Validación]`.
- Referenciar **RN-XX** y **MSG-XX** (con texto inline del catálogo §5 cuando el criterio menciona un mensaje).
- Alinear criterios con **escenarios Gherkin** sin repetirlos palabra por palabra.

## Catálogo de mensajes (§5)

- Una sola definición por mensaje (`MSG-XX`).
- En BDD y AC: citar código **y** texto literal inline.
- Placeholders (`{n}`, `{mailEnmascarado}`) se mantienen en el texto.

## Supuestos y spikes (HITL)

- §3.3: supuestos técnicos/negocio — **pausa obligatoria** para confirmación del usuario.
- §9: dudas abiertas — **pausa obligatoria** para aclaración o skip.
- Las respuestas del usuario se persisten en las columnas Confirmación / Respuesta.

## Story map → historias

- Cada **tarjeta de actividad** puede generar una o varias historias según variaciones de actor o canal.
- Los **releases** del mapa sugieren orden; las dependencias técnicas pueden invertir el orden: documentar en metadatos «Depende de».

## Diagramas

- **Estados**: un escenario Gherkin por transición crítica.
- **Secuencia**: «Cuando» alinea al mensaje o acción que dispara el siguiente paso.
- **Dominio**: nombres de entidades del diagrama en Connextra o pasos Gherkin.

## Entregables (recordatorio)

- **`.md`**: 13 secciones (0–13) + tarjetas completas — ver [md-template.md](md-template.md).
- **CSV**: 4 columnas; delimitador **`;`**; un registro por HU/HT elaborada.
- Description CSV: cuerpo de tarjeta (Connextra → AC → BDD → …). Sin metadatos de tabla.
- Detalle CSV: [csv-schema.md](csv-schema.md).
