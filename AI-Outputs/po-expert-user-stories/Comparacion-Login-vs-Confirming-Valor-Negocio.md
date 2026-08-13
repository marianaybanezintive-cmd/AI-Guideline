# Login vs Confirming — Comparación de valor de negocio para priorizar próxima iteración

**Rol:** Product Owner SR  
**Documentos comparados:**
- `Login-MVP-Happy-Path-EGP-Proveedor.md`
- `Confirming-MVP-Happy-Path-OPUS5-EGP-Proveedor.md`

**Objetivo:** decidir en cuál de los dos avanzar en las próximas iteraciones, mirando exclusivamente el valor que aporta al negocio (no solo el esfuerzo técnico).

---

## Veredicto rápido

**Confirming aporta más valor de negocio directo** (es el producto que genera ingresos: adelantos, comisiones, intereses). **Login es una capacidad habilitante**, no un producto — su happy path no genera feedback de negocio por sí solo, solo destraba el acceso.

Recomendación: avanzar **Confirming** como prioridad de negocio, resolviendo Login con el mínimo indispensable (o usuarios de prueba en Keycloak) para no bloquearlo.

---

## Comparación estructurada

| Dimensión | Login Happy Path | Confirming Happy Path |
|---|---|---|
| **Qué prueba al negocio** | Que un usuario externo puede entrar de forma segura | Que el producto de factoring funciona: carga → habilita → simula → adelanto → aprobación EGP → desembolso |
| **Tipo de valor** | Habilitante / infraestructura | Sustantivo — es la propuesta de valor del producto |
| **Genera ingresos/aprendizaje comercial** | No (por sí solo) | Sí: valida adopción, comportamiento de aprobación EGP, confianza en el cálculo, apetito de crédito |
| **Complejidad técnica del corte mínimo** | Media (OAuth/Keycloak, mail, OTP — patrones estándar) | Alta (máquina de estados, cálculo financiero, freeze de límite, integración CORE, aprobación EGP) |
| **Dependencias externas críticas** | Atlas (mail/JWT) — internas | **CORE BANKING** (desembolso real o stub) — mayor riesgo/latencia de integración con terceros |
| **Spikes bloqueantes de la Iteración 1** | Pocos, casi ninguno bloqueante (Homebanking se pospone sin fricción) | 5 spikes bloqueantes antes de arrancar (`SPK-C13`, `C10`, `C20`, `C19`, `C07`) — más fricción de arranque |
| **Riesgo si se hace mal** | Seguridad / reputacional (accesos, credenciales) | **Financiero directo**: límites de crédito, desembolsos, freeze — error impacta plata real |
| **Demo sin la otra pieza** | Login solo = pantalla de login a un portal vacío. **No demuestra nada al negocio** | Confirming solo = se puede demostrar con usuarios de prueba en Keycloak, sin esperar todo el Login |
| **Feedback que habilita** | UX de onboarding, fricción de 2FA/OTP (genérico, poco diferencial) | Product-market fit real: ¿el EGP aprueba?, ¿el cálculo es creíble?, ¿el Proveedor confía en el neto a cobrar? |
| **Costo de "saltar" la pieza para el demo** | Bajo: se puede crear el usuario directo en Keycloak sin construir Login | Alto: no hay atajo — es el producto mismo |

---

## Pros y contras — Login MVP Happy Path

### Pros

- Alcance acotado y de patrón conocido (OAuth/Keycloak, mail, OTP): menor riesgo de estimación.
- Casi sin spikes bloqueantes; se puede arrancar de inmediato.
- Es prerequisito real para cualquier piloto con **usuarios externos reales** (no de prueba).
- Reduce deuda de seguridad temprano (mejor que parchear accesos tarde).

### Contras

- **No genera valor de negocio medible por sí solo.** Nadie decide seguir invirtiendo en el producto por ver un login funcionando.
- El feedback que produce (fricción de 2FA, UX de primer acceso) es genérico a cualquier portal, no específico del negocio de Confirming.
- Si se prioriza primero y se agota presupuesto/tiempo del sprint, se retrasa la validación de la hipótesis de negocio real (factoring).
- Se puede bypassear técnicamente con usuarios de prueba en Keycloak sin construir nada de esto — lo que reduce su urgencia real para el próximo sprint.

---

## Pros y contras — Confirming MVP Happy Path (OPUS5)

### Pros

- Es **el producto**: prueba la hipótesis de negocio (adelantos de factura, comisión bancaria, adopción EGP/Proveedor).
- El feedback obtenido es accionable para negocio: ¿confían en el cálculo?, ¿el EGP aprueba con la información dada?, ¿el límite/freeze es entendible?
- Ya viene acotado a lo mínimo creíble (individual, sin masivo, sin N cuotas) — no es un scope inflado.
- Habilita conversaciones reales con el banco/CORE sobre integración, que es la dependencia más riesgosa del programa completo — mejor destrabarla temprano.

### Contras

- Mayor complejidad técnica de entrada: máquina de estados, motor de cálculo, freeze de límite, integración CORE — más superficie de error.
- **5 spikes bloqueantes** antes de poder arrancar la Iteración 1 (moneda GS/PYG, qué es "activo" en el ABM, días a adelantar, ciclo de vida del freeze, si la aprobación banco es automática). Login casi no tiene esta fricción.
- Depende de CORE BANKING: si no hay stub acordado, el riesgo de bloqueo por un tercero es alto.
- Riesgo financiero real si el happy path tiene errores (freeze de límite mal liberado, doble adelanto, etc.) — exige más cuidado incluso en el corte mínimo.
- Sin Login real, el demo solo puede hacerse con usuarios de prueba — válido para demo interno, pero no sirve todavía para un piloto con clientes reales.

---

## Recomendación

No es una decisión "esto o lo otro" sino de **secuencia y de dónde poner el músculo del equipo**:

1. **Avanzar Confirming como prioridad de negocio** en la próxima iteración: es donde está el valor que hay que validar (¿el mercado quiere este producto?, ¿el EGP se comporta como se espera?). El aprendizaje de Confirming es el que puede cambiar el rumbo del roadmap; el de Login, no.
2. **Resolver Login en paralelo con el mínimo indispensable** (o directamente con usuarios de prueba en Keycloak para el demo de Confirming), sin invertir todavía en 2FA/OTP completo si el objetivo inmediato es demo interno o piloto controlado.
3. Antes de comprometer sprint en Confirming, cerrar los 5 spikes bloqueantes de su Iteración 1 (son baratos de resolver — decisiones, no desarrollo) y acordar con el equipo de CORE si el primer demo usa integración real o stub.
4. Login pasa a ser bloqueante recién cuando el objetivo cambie de "demo interno" a **"piloto con usuarios externos reales"** — ahí sí hay que construirlo completo (al menos su happy path) porque ya no se puede bypassear con usuarios de prueba.

En síntesis: **Confirming es el "qué" del negocio; Login es el "cómo se entra".** Para maximizar aprendizaje de negocio por unidad de esfuerzo en la próxima iteración, conviene priorizar Confirming y tratar Login como enabler de soporte, no como el entregable principal.

---

## Próximos pasos sugeridos

1. Cerrar los 5 spikes bloqueantes de Confirming It. 1 (`SPK-C13`, `SPK-C10`, `SPK-C20`, `SPK-C19`, `SPK-C07`) antes de sprint planning.
2. Acordar con el equipo de CORE BANKING si el primer demo usa integración real o stub controlado.
3. Crear usuarios de prueba EGP/Proveedor en Keycloak para destrabar el demo de Confirming sin esperar Login completo.
4. Revisar con negocio en qué momento el objetivo pasa de "demo interno" a "piloto con usuarios externos reales" — ese es el disparador para priorizar Login completo.
