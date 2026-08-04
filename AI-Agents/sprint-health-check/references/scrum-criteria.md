# Criterios de interpretación (Scrum Master Senior)

Guía para leer los números del informe y redactar la sección 16. Los umbrales viven en
`config.json`; acá va el criterio de lectura.

## Semáforo de salud

| Veredicto | Condición |
|-----------|-----------|
| `SALUDABLE` | Ninguna señal alta y menos de 3 señales medias |
| `ATENCION` | 3 o más señales medias |
| `EN RIESGO` | Al menos 1 señal alta |
| `CRITICO` | 3 o más señales altas |

Señales altas: avance >25 pp por detrás del tiempo, proyección que no cierra, ítems
estancados, inconsistencias de QA. Señales medias: faltantes de estimación o asignación,
reaperturas, scope creep >10%, WIP sobre el límite.

## Ritmo vs tiempo transcurrido

Comparar `timeElapsedPct` contra `completionPctByPoints`:

- Diferencia menor a 10 pp: ritmo normal.
- Entre 10 y 25 pp: el sprint se sostiene sólo si el trabajo en QA cierra.
- Más de 25 pp: replanificar alcance ahora, no en la review.

Ojo con el efecto "todo cierra el último día": si la mayor parte de los puntos está en
`Pruebas QA` o `En revisión`, el avance real es menor al que muestra el conteo de ítems.

## Ítems estancados

Se miden desde la **última transición de estado**, no desde la última edición. Un ticket
editado ayer pero sin moverse hace 8 días está estancado.

Preguntas a responder en la narrativa:
- ¿Está bloqueado por una dependencia externa (CORE, ambiente, tercero)?
- ¿Está en curso de forma nominal pero la persona está en otra cosa?
- ¿Debería salir del sprint en vez de arrastrarse?

Los ítems con `neverMoved: true` en `Tareas por hacer` a mitad de sprint son candidatos
directos a salir del alcance.

## Estimación y asignación

Un ítem sin estimar no entra al burndown: distorsiona hacia abajo el total y hace ver
mejor el avance. Si hay muchos sin estimar, aclararlo al leer el porcentaje de avance.

Un ítem sin asignar en curso o en QA no tiene dueño real. Los que están en `Tareas por
hacer` sin asignar a mitad de sprint difícilmente se completen.

## Puntos por persona

No usar para comparar rendimiento individual — usar para detectar desbalance de carga y
concentración de riesgo. Señales:

- Una persona con más del doble de puntos que la mediana del equipo.
- Una persona que concentra todo el QA del sprint (cuello de botella estructural).
- Alguien con muchos ítems y `unestimatedIssues` alto: su carga real es desconocida.

## Evolución diaria

Lo relevante es la **forma** de la curva, no el total:

- Cierres concentrados en los últimos 2 días: el equipo trabaja en modo batch, el riesgo
  se descubre tarde.
- Días sin ningún cierre en mitad del sprint: probable bloqueo o WIP excesivo.
- Una persona con cierres diarios parejos: flujo sano.

## Cambios de alcance (Description)

Distinguir tres casos al escribir el `_Impacto:_`:

1. **Aclaración** — se precisa lo mismo con otras palabras. Sin impacto.
2. **Reducción** — se quitan requisitos para que entre en el sprint. Verificar que la
   estimación se haya ajustado y que el PO esté al tanto.
3. **Ampliación** — se agregan requisitos con el sprint ya empezado. Es scope creep
   encubierto: no aparece como ticket nuevo pero consume capacidad.

Un cambio de descripción sobre un ticket que ya está en `Pruebas QA` o `Finalizado` es
señal de alerta: lo probado puede no cubrir lo que ahora dice la historia.

## Consistencia de QA

El patrón esperado es que cada historia con desarrollo tenga 1 QA Automation + 1
Ejecución de Tests. Los desvíos importan porque:

- Falta QA Automation: se acumula deuda de regresión.
- Falta Ejecución de Tests: nadie validó funcionalmente.
- Historia en `Pruebas QA` con subtareas de QA abiertas: el estado de la historia miente,
  el tablero no refleja la realidad.

La antigüedad de QA es el indicador más predictivo de caída de sprint: si el QA lleva más
días esperando que los días hábiles que restan, ese ítem no cierra.

## Goals

Sólo los goals `CRITICO` justifican reasignar gente en caliente. Para `ALTA`, si el
desarrollo está cerrado y sólo falta QA, es aceptable arrastrar el QA al sprint siguiente
siempre que quede explícito en la review. Los `MEDIA`/`BAJA` que estén sin iniciar a
mitad de sprint conviene bajarlos del alcance para liberar foco.

## Burndown y proyección

La proyección extrapola linealmente la velocidad observada sobre los días hábiles
restantes. Es optimista por naturaleza: no descuenta el tiempo de QA de lo que hoy está
en desarrollo. Si `projectedGap` es mayor a cero, el sprint no cierra completo — la
conversación es qué se baja, no cómo se acelera.

## WIP

Más de 3 ítems simultáneos por persona indica multitarea y aumenta el tiempo de ciclo de
todo lo demás. El `agingByStatus` señala el cuello de botella: el estado con mayor
promedio de días es donde se acumula el trabajo.

## Scope creep

Comparar `addedPoints` contra `baselinePoints`. Por encima del 10% el compromiso original
del sprint dejó de ser medible: al informar el cumplimiento hay que aclarar contra qué
línea de base se mide.

## Calidad

- **Reaperturas**: trabajo que se dio por terminado y no lo estaba. Revisar la Definition
  of Done.
- **Rechazos de QA**: tasa sana por debajo del 15%. Por encima, el problema está aguas
  arriba (criterios de aceptación ambiguos o falta de pruebas de desarrollo).

## Redacción de la sección 16

Entre 3 y 6 acciones. Cada una: verbo en infinitivo + ticket o persona + resultado
esperado. Sin generalidades tipo "mejorar la comunicación".

Buen ejemplo: *"Bajar MAGIA-61 y MAGIA-131 del sprint (goal MEDIA, sin iniciar a 3 días
del cierre) para liberar a Alejandro y cerrar el QA de MAGIA-119 y MAGIA-121."*

Mal ejemplo: *"Mejorar la estimación de las historias."*
