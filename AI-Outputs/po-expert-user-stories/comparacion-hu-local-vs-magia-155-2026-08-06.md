# Comparación HU local (PO Expert) vs Épica MAGIA-155 (Jira)

| Campo | Valor |
|-------|--------|
| **Fecha** | 2026-08-06 |
| **Fuente A (local)** | `po-historias-usuario-2026-08-06-login-atlas-confirming.md` (skill `po-expert-user-stories`, 25 HU) |
| **Fuente B (Jira)** | Épica [MAGIA-155](https://bancoatlaspy.atlassian.net/browse/MAGIA-155) — Login (historias `MAGIA-351`…`MAGIA-375`, origen `historias-usuario-login_v2.0.0.md`) |
| **Foco** | Escenarios (tabla + BDD) y criterios de aceptación |
| **Veredicto global** | **Jira es más completo** en escenarios y AC. Lo más apropiado para la HU final es **un mix con base Jira**, enriquecido con anclas POC / exclusión demo del local y, donde el local aporta claridad de capa FE/BFF. |

---

## 1. Resumen ejecutivo

| Dimensión | Local (PO Expert 2026-08-06) | Jira MAGIA-155 (v2.0) | Mejor para HU final |
|-----------|------------------------------|----------------------|---------------------|
| **Cobertura funcional** | Misma épica LOG / mismos LO Excel | Misma épica; IDs LO 1:1 en summary | Empate (ambos cubren el alcance) |
| **Granularidad** | Parte LO-10 en 2 HU FE; une LO-31+LO-32 en 1 HU | Respeta Excel: LO-10 única; LO-31 y LO-32 separadas | **Jira** (trazabilidad LO); split local solo si se necesita sizing de sprint |
| **Tabla ESCENARIOS** | 2–4 por HU, alineados a POC | Lista Excel + ampliación PO (hasta 11) | **Jira** en amplitud; **local** en foco POC |
| **BDD Gherkin** | Corto, pasos UI/POC | Completo: Antecedentes, Esquemas, ejemplos, MSG/RN | **Jira** |
| **Criterios de aceptación** | 3–4 “Que el FE/BFF…” (alto nivel) | 5–8 tipados `[Feliz]/[Error]/[Alternativo]/[Validación]` + RN/MSG | **Jira** |
| **Mensajería / reglas** | Menciona copy POC; sin catálogo MSG | Referencias MSG-xx + RN-01… de la épica | **Jira** |
| **POC / demo** | Links de paso POC; excluye modo demo | Pantalla POC en metadatos (a veces removidos del body); demo menos explícito | **Local** (llevar al mix) |
| **Contratos BFF** | Endpoints mencionados | Códigos HTTP, errores, body flags | **Jira** |
| **Listo para desarrollo/QA** | Buena base de alcance | Ya usable como DoR casi completo | **Mix: base Jira + aportes local** |

**Conclusión:** para la historia de usuario final en Jira, **tomar MAGIA-xxx como base** y **incorporar del local** (1) exclusión explícita del modo demo, (2) referencias POC por paso, (3) dónde el local aclara interacción FE (wizard steps). No reemplazar Jira por el local: se perderían edge cases, MSG, RN y AC tipados.

---

## 2. Matriz de mapeo (clave LO)

| LO Excel | Local HU | Jira | Relación |
|----------|----------|------|----------|
| LO-05 | HU-LOG.05 | [MAGIA-351](https://bancoatlaspy.atlassian.net/browse/MAGIA-351) | 1:1 |
| LO-06 | HU-LOG.06 | [MAGIA-362](https://bancoatlaspy.atlassian.net/browse/MAGIA-362) | 1:1 |
| LO-07 | HU-LOG.07 | [MAGIA-352](https://bancoatlaspy.atlassian.net/browse/MAGIA-352) | 1:1 |
| LO-10 | HU-LOG.08 + HU-LOG.09 | [MAGIA-353](https://bancoatlaspy.atlassian.net/browse/MAGIA-353) | Local **parte** en 2; Jira **una** |
| LO-11 | HU-LOG.11 | [MAGIA-363](https://bancoatlaspy.atlassian.net/browse/MAGIA-363) | 1:1 |
| LO-13 | HU-LOG.12 (+ parte FE en .09) | [MAGIA-364](https://bancoatlaspy.atlassian.net/browse/MAGIA-364) | 1:1 BFF; FE en LO-10 |
| LO-22 | HU-LOG.10 | [MAGIA-354](https://bancoatlaspy.atlassian.net/browse/MAGIA-354) | 1:1 |
| LO-24 | HU-LOG.13 | [MAGIA-365](https://bancoatlaspy.atlassian.net/browse/MAGIA-365) | 1:1 |
| LO-24-a / GET mail | HU-LOG.14 | [MAGIA-366](https://bancoatlaspy.atlassian.net/browse/MAGIA-366) | 1:1 |
| LO-25 | HU-LOG.15 | [MAGIA-355](https://bancoatlaspy.atlassian.net/browse/MAGIA-355) | 1:1 |
| LO-26 | HU-LOG.16 | [MAGIA-367](https://bancoatlaspy.atlassian.net/browse/MAGIA-367) | 1:1 |
| LO-27 | HU-LOG.17 | [MAGIA-356](https://bancoatlaspy.atlassian.net/browse/MAGIA-356) | 1:1 |
| LO-28 | HU-LOG.18 | [MAGIA-368](https://bancoatlaspy.atlassian.net/browse/MAGIA-368) | 1:1 |
| LO-29 | HU-LOG.19 | [MAGIA-357](https://bancoatlaspy.atlassian.net/browse/MAGIA-357) | 1:1 |
| LO-29-a cookie | HU-LOG.20 | [MAGIA-369](https://bancoatlaspy.atlassian.net/browse/MAGIA-369) | 1:1 |
| LO-30 | HU-LOG.21 | [MAGIA-358](https://bancoatlaspy.atlassian.net/browse/MAGIA-358) | 1:1 |
| LO-31 | HU-LOG.22 (parcial) | [MAGIA-359](https://bancoatlaspy.atlassian.net/browse/MAGIA-359) | Local **fusiona** 31+32 |
| LO-32 | HU-LOG.22 (parcial) | [MAGIA-360](https://bancoatlaspy.atlassian.net/browse/MAGIA-360) | Local **fusiona** 31+32 |
| LO-33 | HU-LOG.24 | [MAGIA-370](https://bancoatlaspy.atlassian.net/browse/MAGIA-370) | 1:1 |
| LO-34 | HU-LOG.23 | [MAGIA-361](https://bancoatlaspy.atlassian.net/browse/MAGIA-361) | 1:1 |
| LO-35 | HU-LOG.25 | [MAGIA-371](https://bancoatlaspy.atlassian.net/browse/MAGIA-371) | 1:1 |
| LO-01 / T-01 | HU-LOG.01 | [MAGIA-372](https://bancoatlaspy.atlassian.net/browse/MAGIA-372) | 1:1 |
| XX ente Open-API | HU-LOG.02 | [MAGIA-373](https://bancoatlaspy.atlassian.net/browse/MAGIA-373) | 1:1 |
| Mail services | HU-LOG.03 | [MAGIA-374](https://bancoatlaspy.atlassian.net/browse/MAGIA-374) | 1:1 |
| SPEC CORE | HU-LOG.04 | [MAGIA-375](https://bancoatlaspy.atlassian.net/browse/MAGIA-375) | 1:1 |

---

## 3. Comparación por historia (escenarios + AC)

Leyenda de veredicto: **J** = preferir Jira · **L** = preferir local · **M** = mix (base Jira + aportes local).

### 3.1 FE — Login y onboarding

#### LO-07 · Primer login BANCO (HU-LOG.07 ↔ MAGIA-352)

| | Local | Jira |
|-|-------|------|
| **Escenarios tabla** | 3: 2FA OK; 2FA rechazado; credenciales inválidas | 1 en tabla Excel (“doble factor desde AD”) |
| **BDD** | 3 escenarios; UI espera AD; excluye demo | **7** escenarios: feliz+auditoría, 2FA rechazado (MSG-14), credenciales (MSG-01/RN-04), sin rol+Mesa Ayuda, pass AD expirada (MSG-12), campos vacíos, BFF caído |
| **Cómo los describe** | Enfoque POC (“Esperando aprobación del AD…”) | Enfoque producto + catálogo MSG/RN + auditoría |
| **AC** | 3 alto nivel | **8** tipados |
| **Más completo** | Jira (BDD/AC) | |
| **Más apropiado final** | **M** — base MAGIA-352; del local: estado UI de espera AD + “no modo demo” |

#### LO-10 · Primer login EGP/Proveedor (HU-LOG.08+09 ↔ MAGIA-353)

| | Local | Jira |
|-|-------|------|
| **Estructura** | 2 HU: canal (08) + nueva pass (09) | 1 HU de journey completo |
| **Escenarios** | 08: 4 · 09: 3 (temporal, HB/manual, sin HB, error; pass OK/cancel/reglas) | Tabla 3; BDD **~15** (dominios, temporal incorrecta/vencida, sin rol, inexistente, HB, sin HB, derivación, manual OK, política con ejemplos, confirmación, igual a temporal, checklist, error servicio, abandono) |
| **AC** | 08: 4 · 09: 3 | **8** tipados con RN-01/02/04/07/09 |
| **Más completo** | **Jira** (unifica y profundiza) | |
| **Más apropiado final** | **M** — mantener **una** HU Jira (mejor journey); del local: wizard steps Contraseña/Verificación/Listo, CTAs POC, exclusión demo. Si el sprint exige sizing: usar local como **subtareas** FE, no como dos HU de negocio distintas. |

#### LO-22 · 2FA primer login (HU-LOG.10 ↔ MAGIA-354)

| | Local | Jira |
|-|-------|------|
| **Escenarios** | 4: OTP OK (+dispositivo), otro correo, reenvío, OTP inválido | Tabla 7; BDD **~14** (enmascarado, cambio mail+formato, envío, validación, intentos, vencido, cooldown, máx reenvíos, formato código, notificaciones caídas, no saltear 2FA) |
| **AC** | 3 | **8** + RN-03/08/10 |
| **Más completo / final** | **Jira** · Mix: del local pantalla Listo + “Ingresar al portal” y checkbox dispositivo seguro explícito en UI |

#### LO-25 · Login recurrente (HU-LOG.15 ↔ MAGIA-355)

| | Local | Jira |
|-|-------|------|
| **Escenarios** | 3: válidas→2FA/plataforma; olvido; inválidas+intentos | Tabla **9**; BDD: orígenes AD/HB/manual, sin elegir origen, incorrectas, bloqueado, baja ABM, expirada, sesión vigente, BFF caído, obligatorios |
| **AC** | 3 | **6** |
| **Más completo / final** | **Jira** · Mix: del local toggle ver pass, CTA “Ingresar al Portal”, exclusión demo |

#### LO-27 · 2FA accesos posteriores (HU-LOG.17 ↔ MAGIA-356)

| | Local | Jira |
|-|-------|------|
| **Escenarios** | 2: OTP OK+trust; OTP incorrecto | Tabla **11**; BDD: post-logout, trust, dispositivo confiable sin logout, dispositivo nuevo, OTP tras logout aun confiable, inválido/vencido, intentos, reenvío RN-03, abandono, BANCO vía AD |
| **AC** | 3 | **8** |
| **Más completo / final** | **Jira** (política RN-06 mucho más clara). Local insuficiente solo. |

#### LO-29 · Idle logout (HU-LOG.19 ↔ MAGIA-357)

| | Local | Jira |
|-|-------|------|
| **Escenarios** | 3: warning+extender; cierre; cookie inválida | Tabla **8**; BDD: MSG-10/11, Continuar/Cerrar, reinicio por interacción (navegar/clic/escribir/scroll), cookie, datos no guardados, cierre manual |
| **AC** | 3 (5 min / aviso 1 min) | **7** |
| **Más completo / final** | **Jira** · Mix: del local valores Excel “5 min / warning 1 min” ya alineados; mantener copy POC del modal |

#### LO-30 · Olvido BANCO (HU-LOG.21 ↔ MAGIA-358)

| | Local | Jira |
|-|-------|------|
| **Escenarios** | 2: aviso AD/Mesa; no revelar existencia | **5**: olvido, pass expirada en login, BANCO bloqueado, no revelar, volver login |
| **AC** | 3 | **5** |
| **Más completo / final** | **Jira** |

#### LO-31 + LO-32 · Olvido EGP/Proveedor (HU-LOG.22 ↔ MAGIA-359 + MAGIA-360)

| | Local | Jira |
|-|-------|------|
| **Estructura** | 1 HU FE unificada | 2 HU (con HB / solo manual) |
| **Escenarios** | 4 genéricos | 359: **9** · 360: **7** (OTP en recupero, últimas 3 pass, sin mail, código reutilizado, expirada por política, etc.) |
| **AC** | 3 | 6 + 5 |
| **Más completo** | **Jira** | |
| **Más apropiado final** | **M** — **mantener 2 issues Jira** (mejor por dominio/canal). Del local: reutilizar reglas/UI del wizard de nueva contraseña y CTA “Prefiero crear la contraseña acá”. |

#### LO-34 · Bloqueo FE (HU-LOG.23 ↔ MAGIA-361)

| | Local | Jira |
|-|-------|------|
| **Escenarios** | 3: 3er intento; CTA cambiar pass; intentos 1–2 | Tabla 3 Excel + BDD **8**: restantes, bloqueo, login con pass correcta bloqueado, reset contador, desbloqueo LO-31/32, BANCO, no revelar, auditoría |
| **AC** | 3 | **7** |
| **Más completo / final** | **Jira** |

---

### 3.2 BE negocio — Mail bienvenida

#### LO-05 (HU-LOG.05 ↔ MAGIA-351)

| | Local | Jira |
|-|-------|------|
| **Escenarios** | 2: envío OK; fallo con trazabilidad | Tabla 1 + BDD 4 (esquema dominios, BANCO no recibe, fallo reintento, reenvío ABM) |
| **AC** | 3 | **7** (incluye reenvío ABM, no mail BANCO, RN-01/02) |
| **Más completo / final** | **Jira** |

---

### 3.3 BFF / HT (habilitadores)

| Par | Escenarios local | Escenarios Jira (tabla≈BDD) | AC L / J | Veredicto |
|-----|------------------|-----------------------------|----------|-----------|
| HU-LOG.06 ↔ MAGIA-362 LO-06 | 3 | 4 | 3 / 4 | **J** — HTTP 202/400, estados histórico, backoff |
| HU-LOG.11 ↔ MAGIA-363 LO-11 | 2 | 7 | 3 / 5 | **J** — códigos 401/403/422/423/503 |
| HU-LOG.12 ↔ MAGIA-364 LO-13 | 2 | 5 | 3 / 5 | **J** — reuse, sessionToken wizard |
| HU-LOG.13 ↔ MAGIA-365 LO-24 | 3 | 4 | 2 / 4 | **J** — template flag, OTP_ATTEMPTS, cooldown |
| HU-LOG.14 ↔ MAGIA-366 LO-24-a | 2 | 3 | 2 / 3 | **J** — enmascarado + update contacto |
| HU-LOG.16 ↔ MAGIA-367 LO-26 | 2 | 5 | 3 / 5 | **J** — OAuth PKCE, login-policy, mfaRequired |
| HU-LOG.18 ↔ MAGIA-368 LO-28 | 2 | 5 | 2 / 5 | **J** — trustDevice + RN-06 en flag |
| HU-LOG.20 ↔ MAGIA-369 LO-29-a | 2 | 4 | 2 / 4 | **J** — HttpOnly/Secure/SameSite, renew, logout |
| HU-LOG.24 ↔ MAGIA-370 LO-33 | 4 | 5 | 3 / 5 | **J** — actions por dominio + rate limit |
| HU-LOG.25 ↔ MAGIA-371 LO-35 | 3 | 5 | 2 / 5 | **J** — remainingAttempts, estados ACTIVA/TEMPORAL/… |

**Aporte local en BFF:** nombres de capa “BFF — …” y dependencia FE explícita; útil como subtítulo/labels, no como reemplazo de contratos Jira.

---

### 3.4 Tareas habilitadoras BE

| Par | Local | Jira | Veredicto |
|-----|-------|------|-----------|
| HU-LOG.01 ↔ MAGIA-372 | BDD tokens + rechazo; AC realm/clients/bloqueo n=3 | DoD OAuth+PKCE+AD | **M** — DoD Jira + política n=3 y no filtrar existencia del local |
| HU-LOG.02 ↔ MAGIA-373 | JWT OK/inválido | DoD JWT + conectividad | Empate técnico; **J** como issue |
| HU-LOG.03 ↔ MAGIA-374 | Template registrado / fallo | DoD templates + envío prueba | **J** |
| HU-LOG.04 ↔ MAGIA-375 | Ente+permisos / rechazo | DoD ente+llamada real | **J** |

---

## 4. Cómo se describen (patrón de redacción)

| Elemento | Local | Jira |
|----------|-------|------|
| **COMO/QUIERO/PARA** | Actor de negocio o sistema BFF | Igual; FE más “usuario de dominio” |
| **NECESIDAD / CONTEXTO** | Corto; POC y Excel | NECESIDAD de valor; metadatos a veces fuera del body (post-reorder backlog) |
| **ESCENARIOS** | Tabla corta feliz/error | Tabla Excel + ampliación en BDD |
| **BDD** | `Dado/cuando/entonces` con viñetas; IDs 1/3/4 | Feature + Antecedentes + Esquemas con tablas de ejemplos + MSG |
| **AC** | Checklist “Que…” | Criterios numerados tipados, testeables |
| **Fuera de alcance / Notas** | Spikes S-01/S-02, demo | Spikes + inconsistencias API (R-xx) |

---

## 5. Recomendación de estructura final

1. **Mantener issues Jira** MAGIA-351…375 como historias/tareas oficiales (ya tipadas LO).
2. **No reemplazar** descripciones Jira por el md local: se pierde cobertura.
3. **Aplicar mix** en Description de cada HU FE:
   - Conservar BDD + AC tipados de Jira.
   - Agregar bloque `Referencia POC` (URL paso) del local.
   - Agregar bullet de exclusión: *No incluir “Ingresar sin credenciales (modo demo)”*.
   - Alinear copy de CTAs a la POC cuando no contradiga MSG.
4. **Granularidad:** no fusionar LO-31/LO-32; no partir LO-10 en dos HU de negocio (usar subtareas FE si hace falta).
5. **RN/MSG** viven en la épica MAGIA-155; las HU deben seguir referenciándolos (fortaleza Jira).

---

## 6. Historias finales mixeadas (ejemplos listos para pegar)

> Formato sugerido Description Jira. Se muestra el **mix** (no un dump completo de todo el BDD Jira cuando no cambia). Donde el BDD Jira ya es el correcto, se indica “conservar BDD MAGIA-xxx” y solo se listan **deltas** del local.

### 6.1 MAGIA-352 / LO-07 — Primer login BANCO *(mix)*

**COMO** Usuario interno del Banco (dominio BANCO)  
**QUIERO** ingresar a la plataforma con mis credenciales de AD  
**PARA** loguearme en la plataforma completando el segundo factor del directorio corporativo  

**NECESIDAD:** Habilita el acceso de operadores internos sin gestionar contraseñas en el portal, reutilizando el AD corporativo. El portal **no gestiona** el 2FA BANCO: lo provee el AD.

**Referencia POC:** [login → 2fa-ad](https://marianaintive.github.io/atlas-confirming-poc/?paso=2fa-ad&perfil=BANCO) — pantalla “Validamos tus credenciales corporativas…” / “Esperando la aprobación del AD…”.  
**Exclusión producto:** no publicar “Ingresar sin credenciales (modo demo)”.

**ESCENARIOS**

| ID | ESCENARIO |
|----|-----------|
| 1 | Primer ingreso exitoso con AD + 2FA del AD (UI en espera hasta aprobación) |
| 2 | 2FA del AD rechazado o no completado |
| 3 | Credenciales AD incorrectas (MSG-01, RN-04) |
| 4 | Usuario AD válido sin rol Confirming |
| 5 | Contraseña AD expirada (MSG-12 → LO-30) |
| 6 | Campos obligatorios vacíos |
| 7 | BFF de login no disponible (MSG-14) |

**Escenarios BDD:** conservar el bloque Gherkin de MAGIA-352; agregar en el feliz:

- Entonces el FE muestra el estado de espera de aprobación del AD mientras el IdP/AD resuelve el 2FA  
- Y no se ofrece ingreso sin credenciales  

**CRITERIOS DE ACEPTACIÓN**

1. [Feliz] Usuario BANCO habilitado ingresa con AD, completa 2FA del AD, accede con dominio/rol; **FE muestra espera de 2FA AD**; sin crear pass en portal.  
2. [Feliz] Intento exitoso auditado (RN-08).  
3. [Error] 2FA rechazado/no completado → no accede, login + MSG-14; audita fallo.  
4. [Error] Credenciales incorrectas → MSG-01 + intentos (RN-04); **no inicia espera 2FA**.  
5. [Error] Sin rol Confirming → sin acceso + Mesa de Ayuda.  
6. [Error] Pass AD expirada → MSG-12.  
7. [Validación] Campos vacíos no envían solicitud.  
8. [Error] BFF caído → MSG-14 + reintento.  
9. [Validación] **No existe CTA de modo demo** en producto final.

**Fuera de alcance:** configurar 2FA/pass BANCO en portal; cambio AD en portal (LO-30 solo informa).  
**Notas:** S-01 — redirección IdP vs embebido.

---

### 6.2 MAGIA-353 / LO-10 — Primer login EGP/Proveedor *(mix; una sola HU)*

**COMO** Usuario EGP o Proveedor (cliente o no cliente)  
**QUIERO** introducir usuario y contraseña temporal del mail y definir mi contraseña definitiva  
**PARA** completar el primer login y continuar a la configuración de 2FA  

**NECESIDAD:** Convierte la temporal del mail en definitiva y habilita onboarding seguro (RN-01).

**Referencia POC:** wizard `primer-login-temporal` → `canal-password` → `nueva-password` (steps Contraseña · Verificación · Listo).  
CTAs: “Actualizar mi contraseña” · “Actualizar desde Home Banking” · “Crear una contraseña nueva acá” · “Prefiero crear la contraseña acá”.  
**Exclusión:** modo demo.

**ESCENARIOS** — conservar los de MAGIA-353 (tabla + BDD completo) y **añadir énfasis UI del local:**

| Extra ID | ESCENARIO (delta local) |
|----------|-------------------------|
| L1 | Tras temporal válida se muestra pantalla “Tu contraseña es temporal” antes del canal |
| L2 | Cancelar en nueva contraseña vuelve al login sin persistir |
| L3 | Checklist de reglas en vivo (POC) antes de llamar BFF |

**CRITERIOS DE ACEPTACIÓN** — base MAGIA-353 (C1–C8) **más**:

9. [Validación] Wizard alineado a POC (pasos y CTAs arriba).  
10. [Validación] Validación de reglas en cliente **antes** del PATCH (sin llamar BFF si no cumple / no coinciden).  
11. [Validación] Sin modo demo.  
12. [Feliz] Éxito de actualización deja al usuario en LO-22 (2FA).

**Granularidad:** no partir en dos HU; subtareas FE opcionales: (a) canal HB/manual, (b) formulario nueva pass.

---

### 6.3 MAGIA-354 / LO-22 — 2FA primer login *(mix)*

Base: descripción + BDD + AC de MAGIA-354.

**Deltas local a incorporar:**

- Pantalla final **Listo** (“Ya podés operar…”) + CTA **“Ingresar al portal”**.  
- Checkbox **“Recordar este dispositivo como seguro”** en el paso OTP (si aplica enrollment; alinear con contrato BFF).  
- Exclusión modo demo.  
- Referencia POC: `2fa-mail` → `2fa-otp` → `2fa-listo`.

**AC adicional:**  
9. [Feliz] Tras OTP válido se muestra estado Listo y el acceso al portal.  
10. [Validación] Preferencia de dispositivo seguro se envía al BFF cuando el usuario la marca.

---

### 6.4 MAGIA-355 / LO-25 — Login recurrente *(mix)*

Base MAGIA-355 + deltas:

- UI: Usuario, Contraseña, toggle ver pass, “Ingresar al Portal”, “¿Olvidaste tu contraseña?”.  
- Sin modo demo.  
- Conservar escenarios de origen transparente (AD/HB/manual), bloqueo, baja, expirada, sesión vigente, BFF caído.

**AC adicional:**  
7. [Validación] Enlace de olvido visible; sin CTA demo.

---

### 6.5 MAGIA-356 / LO-27 — 2FA posteriores *(recomendación: Jira puro + 1 delta)*

Usar MAGIA-356 casi sin cambios (es claramente más completa que HU-LOG.17).

**Único delta local:** reutilizar la misma UI OTP de la POC que en LO-22 (consistencia visual).

---

### 6.6 MAGIA-357 / LO-29 — Inactividad *(mix corto)*

Base MAGIA-357. Del local reafirmar: timeout **5 min**, aviso **1 min antes**, cookie FE; copy modal POC “Tu sesión está por cerrarse… ¿Querés continuar conectado?”.

---

### 6.7 MAGIA-359 + MAGIA-360 (vs HU-LOG.22 unificada)

**No mixear en una sola issue.** Mantener:

- [MAGIA-359](https://bancoatlaspy.atlassian.net/browse/MAGIA-359) — canal HB  
- [MAGIA-360](https://bancoatlaspy.atlassian.net/browse/MAGIA-360) — solo manual  

**Delta local compartido en ambas:** mismas reglas/checklist de contraseña que primer login; pantalla éxito “Contraseña actualizada” + desbloqueo; CTA “Ir al login”.

---

### 6.8 Plantilla de mix para HT BFF (MAGIA-362…371)

Para cada HT:

1. Conservar **contratos, códigos de error y BDD** de Jira.  
2. En NECESIDAD, una línea del local: *“Consumido por HU FE LO-xx / pantalla POC …”*.  
3. No degradar AC tipados a “Que el BFF…”.

Ejemplo delta LO-11 (MAGIA-363):  
*Habilita wizard FE LO-10 (pantallas temporal → canal → nueva password).*

---

## 7. Scorecard de completitud (orientativo)

| LO | Escenarios BDD L≈ | BDD J≈ | AC L | AC J | Ganador escenarios | Ganador AC | HU final |
|----|-------------------|--------|------|------|--------------------|------------|----------|
| 05 | 2 | 4 | 3 | 7 | J | J | J |
| 07 | 3 | 7 | 3 | 8 | J | J | **M** |
| 10 | 7 (08+09) | 15 | 7 | 8 | J | J | **M** (1 HU) |
| 22 | 4 | 14 | 3 | 8 | J | J | **M** |
| 25 | 3 | 9 | 3 | 6 | J | J | **M** |
| 27 | 2 | 11 | 3 | 8 | J | J | J (+UI) |
| 29 | 3 | 8 | 3 | 7 | J | J | **M** |
| 30 | 2 | 5 | 3 | 5 | J | J | J |
| 31/32 | 4 | 9+7 | 3 | 6+5 | J | J | J (2 issues) |
| 34 | 3 | 8 | 3 | 7 | J | J | J |
| BFF LO-06…35 | 2–4 | 3–7 | 2–4 | 3–5 | J | J | J |
| T-01…04 | 2 | DoD | 2–3 | 1–3 | M | M | **M**/J |

---

## 8. Gaps del local que Jira ya cubre (no reabrir como “faltantes”)

El md local lista “recomendaciones de escenarios faltantes” (timeout AD, límite reenvíos OTP, etc.). **Varios ya están en MAGIA-354/356/352/361**. Antes de crear issues nuevas, contrastar contra BDD Jira + RN de la épica.

Gaps que **sí** conviene vigilar (ambos lados débiles o en spikes):

- Timeout / abandono en espera 2FA AD (S-01).  
- Integración real Home Banking (S-02 / R-01).  
- Vigencia dispositivo confiable (S-03).  
- Política pass vs Seguridad (S-04).  
- Multi-pestaña / race en bloqueo (ni local ni Jira lo detallan).  

---

## 9. Próximos pasos sugeridos

1. Usar este documento como guía de **actualización de Description** en MAGIA-351…361 (FE) con los deltas de la §6.  
2. Dejar HT MAGIA-362…375 con contratos Jira; solo agregar “habilita LO-xx / POC”.  
3. Opcional: crear subtareas bajo MAGIA-353 para canal vs formulario pass (sizing), sin romper la HU de negocio.  
4. No importar el CSV/md local a Jira como reemplazo masivo.

---

## 10. Fuentes

- Local: `AI-Guideline/AI-Outputs/po-expert-user-stories/po-historias-usuario-2026-08-06-login-atlas-confirming.md`  
- Jira épica: https://bancoatlaspy.atlassian.net/browse/MAGIA-155  
- Cache historias: `AI-Guideline/AI-Outputs/po-architect-agent/architecture-output/_cache-magia-155.json`  
- Verificación puntual Description vigente: MAGIA-352 (2026-07-31) alineada al cache v2.0  
