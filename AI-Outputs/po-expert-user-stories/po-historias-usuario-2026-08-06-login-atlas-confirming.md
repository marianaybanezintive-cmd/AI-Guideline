# Historias de usuario — Login Portal Confirming (Atlas)

| Campo | Valor |
|-------|--------|
| **Fecha** | 2026-08-06 |
| **Origen** | Excel `login (2) (1).xlsx` (hoja LOGIN + matriz/API); POC https://marianaintive.github.io/atlas-confirming-poc/; diagramas https://drive.google.com/file/d/1x2cOj_Byy9vPTOOcBbOYbb56Ugs-Qf5o/view?usp=sharing |
| **Columnas detectadas** | Issue Type, Issue Key, Summary, OBJETIVO, ESCENARIOS, DUDAS |
| **Alcance** | Épica LOG — Login Atlas Confirming (LO-01…LO-35 no tachados) |
| **Generado con** | skill `po-expert-user-stories` |
| **Historias** | 25 |
| **Filas omitidas por tachado** | 7 grupos (detalle abajo) |
| **Exclusión de producto** | Flujo POC «Ingresar sin credenciales (modo demo)» — no forma parte del producto final |

## Filas / ítems omitidos por tachado o desestimados

- LO-02 (DER LOGIN — fila tachada)
- LO-03 / LO-04 (Mail bienvenida BANCO + EP — tachados; nota Excel: resuelto por Keycloak)
- LO-08 / LO-09 (EP validar pass temporal / actualizar AD — tachados)
- LO-12 (Actualizar contraseña integrada homebanking en primer login — summary tachado)
- LO-14..LO-17 (Primer login Proveedor Cliente + EPs — tachados; cubiertos por LO-10)
- LO-18..LO-20 (Primer login Proveedor No Cliente + EPs — tachados; cubiertos por LO-10)
- LO-21 / LO-23 (2FA primer login BANCO / Proveedor No Cliente como HU separada — tachados)

## Resumen ejecutivo

| Capa | # HU | Riesgo principal |
|------|------|------------------|
| FE | 10 | Alinear wizard a POC; spikes AD 2FA y momento Home Banking |
| BFF | 9 | Contratos first-login / MFA / password + flags de estado |
| BE | 6 | OAuth, ente Open-API, mail/OTP Notificaciones |

| Épica | Historias |
|-------|-----------|
| LOG — Login Atlas Confirming | 25 |

---

# Épica LOG: Login Atlas Confirming


# FE

### HU-LOG.07 — FE — Primer login BANCO con 2FA del Active Directory

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.07`
- **Tipo:** Story
- **Capa:** FE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.01; spike 2FA AD
- **Origen Excel / POC:** LO-07 · POC paso 2FA del AD (https://marianaintive.github.io/atlas-confirming-poc/?paso=2fa-ad&perfil=BANCO)

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO usuario BANCO con dominio/rol habilitado para Confirming
QUIERO ingresar a la plataforma con mis credenciales de AD
PARA loguearme en la plataforma completando el segundo factor del directorio corporativo


NECESIDAD: Usuarios BANCO autentican contra AD; el portal no gestiona el 2FA interno.
CONTEXTO: POC v2.11: pantalla 'Validamos tus credenciales corporativas…' con estado 'Esperando la aprobación del AD…'. Excluir botón 'Ingresar sin credenciales (modo demo)'.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Usuario BANCO completa login y aprueba 2FA del AD |
| 3  | Usuario BANCO cancela o rechaza el 2FA del AD |
| 4  | Credenciales AD inválidas muestran error en login |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Usuario BANCO completa login y aprueba 2FA del AD**

Dado un usuario BANCO en la pantalla de login del Portal de Confirming, cuando ingresa usuario/contraseña AD válidos y aprueba el segundo factor del AD,
- entonces el FE muestra el estado de espera de aprobación del AD
- entonces, al aprobarse el 2FA, el usuario continúa el flujo hacia la plataforma (o al siguiente paso definido por el BFF)
- entonces no se ofrece 'Ingresar sin credenciales'

**ID 3-Escenario Usuario BANCO cancela o rechaza el 2FA del AD**

Dado el FE en espera de aprobación del AD, cuando el 2FA es rechazado o cancelado,
- entonces se informa que no se pudo completar la autenticación
- entonces el usuario permanece fuera de la plataforma
- entonces puede volver a intentar desde el login

**ID 4-Escenario Credenciales AD inválidas muestran error en login**

Dado un usuario BANCO en login, cuando ingresa credenciales inválidas,
- entonces el FE muestra mensaje de error de autenticación
- entonces no se inicia la espera de 2FA del AD

### Criterios de aceptación

Que el FE soporte el flujo de primer/login BANCO con credenciales AD
Que se visualice el estado de espera del segundo factor provisto por el AD
Que no se incluya el acceso demo sin credenciales del producto final

### Fuera de alcance

- Configuración interna del 2FA en AD (spike S-01)
- Wizard de contraseña temporal (no aplica a BANCO vía portal)
- Botón 'Ingresar sin credenciales (modo demo)' de la POC

### Notas / preguntas abiertas

- SPIKE Excel: investigación de 2FA del AD.
- POC: 'El portal no gestiona el segundo factor de los usuarios BANCO: lo provee el AD.'
- Referencia UI: https://marianaintive.github.io/atlas-confirming-poc/

DOD pendiente
DOR pendiente



### HU-LOG.08 — FE — Primer login EGP/Proveedor: validar contraseña temporal y elegir canal

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.08`
- **Tipo:** Story
- **Capa:** FE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.05; HU-LOG.11; HU-LOG.12
- **Origen Excel / POC:** LO-10 · POC pasos Contraseña temporal / Canal de actualización

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO usuario EGP o Proveedor (cliente o no cliente) habilitado para Confirming
QUIERO introducir el usuario y la contraseña temporal recibidos por mail
PARA iniciar el primer login y elegir cómo definir mi contraseña definitiva


NECESIDAD: Tras validar la temporal, el FE obliga a actualizar contraseña (flag temporal del BFF).
CONTEXTO: POC: 'Tu contraseña es temporal' → CTA 'Actualizar mi contraseña' → canal 'Actualizar desde Home Banking' / 'Crear una contraseña nueva acá'. Si no tiene HB: solo creación local. Wizard steps 1 Contraseña · 2 Verificación · 3 Listo.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Credencial temporal válida habilita actualización de contraseña |
| 2  | Usuario con Home Banking elige canal HB o contraseña nueva |
| 3  | Usuario sin Home Banking solo puede crear contraseña en el portal |
| 4  | Contraseña temporal inválida o vencida muestra error |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Credencial temporal válida habilita actualización de contraseña**

Dado un usuario EGP/Proveedor en primer login con contraseña temporal vigente, cuando ingresa usuario y contraseña temporal correctos,
- entonces el BFF/FE detectan flag de contraseña temporal
- entonces se muestra la pantalla de contraseña temporal validada (usuario/rol OK, temporal vigente, próximo paso definir contraseña)
- entonces el CTA 'Actualizar mi contraseña' avanza al paso de canal

**ID 2-Escenario Usuario con Home Banking elige canal HB o contraseña nueva**

Dado el paso 'Canal de actualización' para usuario con HB habilitado, cuando visualiza las opciones,
- entonces puede elegir 'Actualizar desde Home Banking'
- entonces puede elegir 'Crear una contraseña nueva acá'
- SI elige Home Banking,
  - se muestra la derivación informativa hacia HB (alcance spike S-02)
  - puede volver con 'Prefiero crear la contraseña acá'

**ID 3-Escenario Usuario sin Home Banking solo puede crear contraseña en el portal**

Dado un usuario sin Home Banking habilitado, cuando llega al canal de actualización,
- entonces se informa que solo puede crear la contraseña en el portal
- entonces no se ofrece derivación a Home Banking como camino habilitado

**ID 4-Escenario Contraseña temporal inválida o vencida muestra error**

Dado un intento de primer login, cuando la contraseña temporal es inválida o no vigente,
- entonces el FE muestra error de validación
- entonces no avanza al wizard de nueva contraseña

### Criterios de aceptación

Que el FE implemente el wizard de primer login alineado a la POC (steps Contraseña/Verificación/Listo)
Que se obligue el cambio cuando la respuesta indique contraseña temporal
Que se ofrezcan canales según disponibilidad de Home Banking del usuario
Que no se incluya el modo demo sin credenciales

### Fuera de alcance

- Integración real Home Banking en el momento exacto del primer login (spike S-02 / opciones 1-2-3 del Excel)
- Flujo BANCO AD (HU-LOG.07)
- Botón demo sin credenciales

### Notas / preguntas abiertas

- SPIKE Excel: cuándo ofrecer integración HB — (1) primer login, (2) perfil, (3) segundo login/cambio.
- LO-14/LO-18 tachados: se unifican en esta HU según LO-10.
- Referencia UI: https://marianaintive.github.io/atlas-confirming-poc/

DOD pendiente
DOR pendiente



### HU-LOG.09 — FE — Definir nueva contraseña en primer login (reglas y confirmación)

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.09`
- **Tipo:** Story
- **Capa:** FE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.08; HU-LOG.12
- **Origen Excel / POC:** LO-10 / LO-13 · POC paso Nueva contraseña

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO usuario EGP/Proveedor en primer login que eligió crear contraseña en el portal
QUIERO definir y confirmar una nueva contraseña que cumpla las reglas de seguridad
PARA reemplazar la contraseña temporal y continuar hacia la configuración de 2FA


NECESIDAD: El FE debe validar reglas visibles y coincidencia antes de llamar al BFF.
CONTEXTO: POC reglas: mín. 8, mayúscula, minúscula, número, especial, distinta de la anterior; mensaje 'Las contraseñas no coinciden.'; CTAs Guardar / Cancelar y volver al inicio.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Nueva contraseña válida se guarda y avanza a verificación 2FA |
| 3  | Usuario cancela y vuelve al inicio |
| 4  | Validación de reglas o confirmación fallida bloquea el guardado |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Nueva contraseña válida se guarda y avanza a verificación 2FA**

Dado el paso 'Nueva contraseña' del wizard, cuando el usuario ingresa una contraseña que cumple todas las reglas y coincide con la confirmación y confirma Guardar,
- entonces el FE invoca el BFF de actualización de contraseña
- entonces, ante éxito, avanza al paso de verificación (correo/OTP 2FA)
- entonces la contraseña temporal deja de ser usable

**ID 3-Escenario Usuario cancela y vuelve al inicio**

Dado el paso de nueva contraseña, cuando el usuario elige 'Cancelar y volver al inicio',
- entonces regresa a la pantalla de login
- entonces no se persiste una nueva contraseña

**ID 4-Escenario Validación de reglas o confirmación fallida bloquea el guardado**

Dado el formulario de nueva contraseña, cuando falta una regla o las contraseñas no coinciden,
- entonces se muestran las reglas incumplidas y/o 'Las contraseñas no coinciden.'
- entonces no se llama al BFF de guardado

### Criterios de aceptación

Que el FE valide en cliente las reglas de contraseña definidas en la POC
Que se exija confirmación coincidente antes de guardar
Que el éxito deje al usuario en el siguiente paso del wizard (2FA)

### Fuera de alcance

- Política server-side detallada de complejidad (BE/Keycloak)
- Cambio de contraseña post-login recurrente

### Notas / preguntas abiertas

- Referencia UI: https://marianaintive.github.io/atlas-confirming-poc/?paso=nueva-password
- Escenarios de canal HB quedan en HU-LOG.08 / spike.

DOD pendiente
DOR pendiente



### HU-LOG.10 — FE — Configurar 2FA por OTP mail en primer login (EGP/Proveedor)

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.10`
- **Tipo:** Story
- **Capa:** FE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.09; HU-LOG.13; HU-LOG.14
- **Origen Excel / POC:** LO-22 · POC pasos Correo del código / Código OTP / 2FA configurado

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO usuario EGP/Proveedor que ya cambió su contraseña en el primer login
QUIERO configurar la doble autenticación recibiendo e ingresando un OTP por mail
PARA completar el flujo de primer login y quedar apto para operar


NECESIDAD: Al finalizar el cambio de pass se dispara el enrollment 2FA por mail.
CONTEXTO: POC: mensaje 'Te enviamos un correo a {mail}…'; opción 'Usar otro correo'; ingreso de código 6 dígitos; 'Recordar este dispositivo como seguro'; pantalla Listo 'Ya podés operar…' + 'Ingresar al portal'.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | OTP válido completa 2FA y habilita ingreso al portal |
| 2  | Usuario cambia el correo de recepción del OTP |
| 3  | Usuario solicita reenvío de código |
| 4  | OTP inválido o vencido no completa la configuración |

### Escenarios BDD (Gherkin)

**ID 1-Escenario OTP válido completa 2FA y habilita ingreso al portal**

Dado el paso Verificación tras actualizar contraseña, cuando el usuario recibe el OTP en su mail, lo ingresa correctamente y confirma 'Validar código',
- entonces el FE invoca la validación 2FA del BFF
- SI marca 'Recordar este dispositivo como seguro',
  - se envía la preferencia de dispositivo confiable al BFF
- entonces se muestra la pantalla Listo e 'Ingresar al portal' habilita el acceso

**ID 2-Escenario Usuario cambia el correo de recepción del OTP**

Dado el aviso de correo OTP, cuando el usuario elige 'Usar otro correo' e ingresa un mail válido,
- entonces puede 'Enviar código' al nuevo correo
- entonces el FE valida formato de correo antes de enviar

**ID 3-Escenario Usuario solicita reenvío de código**

Dado el paso de ingreso de OTP, cuando el usuario elige 'Reenviar código',
- entonces se solicita un nuevo OTP al BFF/Notificaciones
- entonces se informa que se reenvió el código

**ID 4-Escenario OTP inválido o vencido no completa la configuración**

Dado un código incorrecto o vencido, cuando el usuario intenta validar,
- entonces el FE muestra error de verificación
- entonces no se habilita el ingreso a la plataforma

### Criterios de aceptación

Que el FE cubra correo destino, envío/reenvío e ingreso de OTP de 6 dígitos
Que permita indicar dispositivo seguro
Que al éxito muestre el estado Listo y el acceso al portal

### Fuera de alcance

- 2FA de usuarios BANCO vía AD (HU-LOG.07)
- App authenticator / QR (si el BFF devolviera qrUri en otros flujos)
- Modo demo sin credenciales

### Notas / preguntas abiertas

- LO-21/LO-23 tachados: enrollment BANCO/Proveedor NC separado no aplica; se unifica en LO-22.
- Referencia UI: https://marianaintive.github.io/atlas-confirming-poc/

DOD pendiente
DOR pendiente



### HU-LOG.15 — FE — Pantalla de login recurrente (credenciales definitivas)

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.15`
- **Tipo:** Story
- **Capa:** FE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.01; HU-LOG.16
- **Origen Excel / POC:** LO-25 · POC Login

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO usuario de la plataforma que finalizó su primer login
QUIERO ingresar a la plataforma con las nuevas credenciales
PARA acceder y utilizar la plataforma


NECESIDAD: Login unificado: AD / Homebanking / manual según dominio; Keycloak resuelve el store.
CONTEXTO: POC LO-25: Usuario, Contraseña, toggle ver pass, 'Ingresar al Portal', '¿Olvidaste tu contraseña?'. EXCLUIR 'Ingresar sin credenciales (modo demo)'.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Credenciales válidas inician autenticación y avanzan a 2FA o plataforma |
| 2  | Usuario navega a olvido de contraseña |
| 4  | Credenciales inválidas muestran error y contabilizan intento |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Credenciales válidas inician autenticación y avanzan a 2FA o plataforma**

Dado un usuario que ya completó primer login, cuando ingresa usuario y contraseña válidos y confirma 'Ingresar al Portal',
- entonces el FE invoca el BFF de login
- SI el BFF indica MFA requerido,
  - entonces navega al paso de verificación OTP
- SI no requiere MFA adicional en ese momento,
  - entonces ingresa a la plataforma
- entonces no existe CTA de ingreso sin credenciales

**ID 2-Escenario Usuario navega a olvido de contraseña**

Dado la pantalla de login, cuando el usuario elige '¿Olvidaste tu contraseña?',
- entonces inicia el flujo de recuperación según dominio (BANCO / HB / manual)

**ID 4-Escenario Credenciales inválidas muestran error y contabilizan intento**

Dado un intento fallido, cuando el BFF rechaza las credenciales,
- entonces el FE muestra mensaje de error
- entonces se contabiliza el intento hacia la política de bloqueo (n=3)

### Criterios de aceptación

Que la pantalla de login permita usuario/contraseña y acceso al portal
Que exista enlace de olvido de contraseña
Que no se publique el modo demo sin credenciales en el producto final

### Fuera de alcance

- Panel lateral de escenarios de la POC
- Ingresar sin credenciales (modo demo)
- Dashboard interno de la plataforma (fuera de épica login)

### Notas / preguntas abiertas

- Escenarios Excel: auth AD / homebanking / manual — Keycloak diferencia dónde buscar la pass.
- Referencia UI: https://marianaintive.github.io/atlas-confirming-poc/

DOD pendiente
DOR pendiente



### HU-LOG.17 — FE — Doble autenticación en accesos posteriores

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.17`
- **Tipo:** Story
- **Capa:** FE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.15; HU-LOG.18
- **Origen Excel / POC:** LO-27 · POC Código OTP (login recurrente)

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO usuario de la plataforma que finalizó su primer login
QUIERO validar doble autenticación y registrar dispositivo como seguro
PARA acceder y utilizar la plataforma


NECESIDAD: Tras password OK, el sistema pide OTP; política: pedirlo siempre al cerrar sesión (EGP/Proveedor).
CONTEXTO: Reutilizar UI de OTP de la POC; opción recordar dispositivo seguro.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | OTP correcto completa el acceso y opcionalmente marca dispositivo seguro |
| 4  | OTP incorrecto impide el acceso |

### Escenarios BDD (Gherkin)

**ID 1-Escenario OTP correcto completa el acceso y opcionalmente marca dispositivo seguro**

Dado un login recurrente con MFA requerido, cuando el usuario ingresa el OTP válido y confirma validar,
- entonces el FE llama a la verificación 2FA del BFF
- SI marca recordar dispositivo seguro,
  - se envía trustDevice=true
- entonces el usuario ingresa a la plataforma

**ID 4-Escenario OTP incorrecto impide el acceso**

Dado MFA requerido, cuando el OTP es inválido,
- entonces se muestra error
- entonces no se abre la plataforma

### Criterios de aceptación

Que el FE solicite OTP cuando el BFF indique MFA requerido
Que permita marcar dispositivo seguro
Que al éxito complete el acceso

### Fuera de alcance

- Decisión de cadencia MFA para BANCO (spike AD)
- Modo demo

### Notas / preguntas abiertas

- Dudas Excel: spike BANCO AD+AUTH; para EGP/Proveedor ¿cada tanto? = siempre al cerrar sesión.
- Referencia UI: https://marianaintive.github.io/atlas-confirming-poc/

DOD pendiente
DOR pendiente



### HU-LOG.19 — FE — Cierre de sesión automático por inactividad

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.19`
- **Tipo:** Story
- **Capa:** FE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta — seguridad
- **Dependencias:** HU-LOG.15; cookie/sesión BFF
- **Origen Excel / POC:** LO-29 · POC idle warning

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO usuario logueado en la plataforma
QUIERO que se cierre la sesión automáticamente luego de n minutos de inactividad
PARA proteger la información sensible que gestiono en la plataforma


NECESIDAD: Política Excel/POC: 5 minutos de inactividad; 1 minuto antes warning; basado en cookies FE; cookie inválida → login.
CONTEXTO: POC modal: 'Tu sesión está por cerrarse… ¿Querés continuar conectado?' con countdown; extender o cerrar.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Warning previo permite extender la sesión |
| 2  | Sin confirmación se cierra la sesión y vuelve al login |
| 4  | Cookie/sesión inválida redirige al login |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Warning previo permite extender la sesión**

Dado un usuario logueado e inactivo ~4 minutos (con timeout 5), cuando aparece el warning,
- entonces se muestra el aviso con countdown (~60s)
- cuando el usuario confirma continuar conectado,
  - entonces la sesión se extiende y el modal se cierra

**ID 2-Escenario Sin confirmación se cierra la sesión y vuelve al login**

Dado el warning visible, cuando el usuario no confirma y vence el countdown o la inactividad total,
- entonces la sesión se cierra
- entonces se informa el cierre por protección de información sensible
- entonces se redirige al login

**ID 4-Escenario Cookie/sesión inválida redirige al login**

Dado una cookie/sesión inválida, cuando el FE detecta el estado,
- entonces redirige al login
- entonces no mantiene acceso a pantallas protegidas

### Criterios de aceptación

Que exista timer de inactividad de 5 minutos con aviso 1 minuto antes
Que el usuario pueda extender la sesión desde el warning
Que el cierre redirija al login

### Fuera de alcance

- Configuración server-side de refresh token TTL (salvo cookie helper)
- Modo demo

### Notas / preguntas abiertas

- Valores Excel: 5 min inactividad; warning 1 min antes; cookies FE.
- Referencia UI: https://marianaintive.github.io/atlas-confirming-poc/ (control Inactividad LO-29).

DOD pendiente
DOR pendiente



### HU-LOG.21 — FE — Olvido/desbloqueo de contraseña para usuarios BANCO (aviso AD)

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.21`
- **Tipo:** Story
- **Capa:** FE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Media
- **Dependencias:** HU-LOG.15
- **Origen Excel / POC:** LO-30 · POC Olvidé mi contraseña / Aviso AD

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO usuario BANCO que olvidó o tiene expirada/bloqueada su contraseña
QUIERO conocer cómo recuperar el acceso
PARA poder volver a loguearme a la plataforma


NECESIDAD: BANCO no cambia pass en el portal: se deriva a AD / Mesa de Ayuda.
CONTEXTO: POC: captura usuario → mensaje seguridad (misma respuesta exista o no) → aviso AD + contactos Mesa de Ayuda (interno 1500 / mail).

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Usuario BANCO recibe aviso de actualizar desde AD / Mesa de Ayuda |
| 4  | Respuesta no revela si el usuario existe |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Usuario BANCO recibe aviso de actualizar desde AD / Mesa de Ayuda**

Dado un usuario BANCO en '¿Olvidaste tu contraseña?', cuando ingresa su usuario y continúa,
- entonces el FE muestra el warning de actualizar desde AD
- entonces se exponen datos de Mesa de Ayuda Banco Atlas
- entonces puede volver al inicio/login

**ID 4-Escenario Respuesta no revela si el usuario existe**

Dado cualquier usuario ingresado en olvido BANCO, cuando el sistema responde,
- entonces el mensaje es equivalente exista o no el usuario
- entonces no se filtra información de cuenta

### Criterios de aceptación

Que el flujo de olvido para BANCO derive a AD/Mesa de Ayuda
Que no se ofrezca cambio de contraseña local para BANCO
Que se preserve privacidad de existencia de usuario

### Fuera de alcance

- Cambio de contraseña en portal para EGP/Proveedor
- Desbloqueo técnico Keycloak (ops)

### Notas / preguntas abiertas

- Referencia UI: https://marianaintive.github.io/atlas-confirming-poc/
- POST /v1/auth/password/forgot action REDIRECT_AD.

DOD pendiente
DOR pendiente



### HU-LOG.22 — FE — Olvido/desbloqueo EGP/Proveedor con opción Home Banking o manual

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.22`
- **Tipo:** Story
- **Capa:** FE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.15; HU-LOG.24
- **Origen Excel / POC:** LO-31 / LO-32 · POC Derivación HB / Nueva contraseña / Contraseña actualizada

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO usuario EGP/Proveedor que olvidó, expiró o tiene bloqueada su contraseña
QUIERO cambiar la contraseña de mi cuenta (vía Home Banking o manualmente)
PARA poder loguearme nuevamente a la plataforma


NECESIDAD: EGP/Proveedor pueden recuperar acceso vía Home Banking o cambio manual en el portal.
CONTEXTO: Excel LO-31: warning HB o continuar manual. LO-32: flujo cambio manual. POC: derivación HB + 'Prefiero crear la contraseña acá'; pantalla éxito desbloquea si estaba bloqueado.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Usuario con HB elige Home Banking o cambio manual |
| 2  | Usuario completa cambio manual y ve confirmación de contraseña actualizada |
| 3  | Usuario bloqueado puede desbloquearse al cambiar contraseña |
| 4  | Validación de nueva contraseña falla y no actualiza |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Usuario con HB elige Home Banking o cambio manual**

Dado un usuario EGP/Proveedor cliente en olvido de contraseña, cuando el sistema ofrece canales,
- entonces puede ir a Home Banking
- entonces puede elegir crear/cambiar la contraseña en el portal

**ID 2-Escenario Usuario completa cambio manual y ve confirmación de contraseña actualizada**

Dado el flujo manual (LO-32), cuando el usuario define una nueva contraseña válida y confirma,
- entonces el FE llama al BFF PATCH de contraseña
- entonces muestra la pantalla de contraseña actualizada (y desbloqueo si correspondía)
- entonces puede 'Ir al login'

**ID 3-Escenario Usuario bloqueado puede desbloquearse al cambiar contraseña**

Dado un usuario bloqueado por intentos, cuando completa el cambio de contraseña exitoso,
- entonces el sistema desbloquea el usuario
- entonces se informa que puede ingresar con las nuevas credenciales

**ID 4-Escenario Validación de nueva contraseña falla y no actualiza**

Dado el formulario de nueva contraseña, cuando las reglas no se cumplen,
- entonces se muestran errores de validación
- entonces no se actualiza ni desbloquea la cuenta

### Criterios de aceptación

Que el FE ofrezca canal HB o manual según perfil
Que el cambio manual reutilice reglas de contraseña de la POC
Que el éxito desbloquea si estaba bloqueado y vuelva al login

### Fuera de alcance

- Usuarios BANCO (HU-LOG.21)
- Modo demo

### Notas / preguntas abiertas

- LO-31 y LO-32 se entregan juntos en FE por compartir wizard; BFF en HU-LOG.24.
- Referencia UI: https://marianaintive.github.io/atlas-confirming-poc/

DOD pendiente
DOR pendiente



### HU-LOG.23 — FE — Bloqueo de usuario tras N intentos fallidos de login

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.23`
- **Tipo:** Story
- **Capa:** FE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta — seguridad
- **Dependencias:** HU-LOG.15; HU-LOG.16; HU-LOG.25
- **Origen Excel / POC:** LO-34 · POC Usuario bloqueado

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO usuario que falla reiteradamente el login
QUIERO ser informado cuando mi usuario queda bloqueado por intentos fallidos
PARA conocer cómo recuperar el acceso (cambio de contraseña o Mesa de Ayuda)


NECESIDAD: Política: 3 intentos → bloqueo Keycloak/BFF; FE muestra mensaje.
CONTEXTO: POC: mensaje de bloqueo + 'El desbloqueo se realiza cambiando tu contraseña o desde la Mesa de Ayuda' + CTAs Cambiar mi contraseña / Volver al inicio.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Al 3er intento fallido el FE muestra estado de usuario bloqueado |
| 2  | Usuario bloqueado inicia cambio de contraseña desde el mensaje |
| 4  | Intentos previos al bloqueo muestran error de credenciales sin bloquear aún |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Al 3er intento fallido el FE muestra estado de usuario bloqueado**

Dado un usuario con 2 intentos fallidos previos, cuando falla el 3er POST login,
- entonces el BFF/Keycloak bloquea la cuenta y actualiza flag de pass bloqueada
- entonces el FE muestra la pantalla/mensaje de usuario bloqueado

**ID 2-Escenario Usuario bloqueado inicia cambio de contraseña desde el mensaje**

Dado el mensaje de bloqueo, cuando el usuario elige 'Cambiar mi contraseña',
- entonces ingresa al flujo de recuperación según dominio

**ID 4-Escenario Intentos previos al bloqueo muestran error de credenciales sin bloquear aún**

Dado el 1er o 2do intento fallido, cuando el login falla,
- entonces se muestra error de credenciales
- entonces aún no se muestra el estado de bloqueo definitivo

### Criterios de aceptación

Que el FE reaccione al flag/estado de bloqueo del BFF
Que se ofrezcan caminos de desbloqueo (cambio pass / Mesa de Ayuda)
Que la política de 3 intentos sea visible operativamente

### Fuera de alcance

- Lógica server-side de contador (HU-LOG.25)
- Modo demo

### Notas / preguntas abiertas

- Referencia UI: https://marianaintive.github.io/atlas-confirming-poc/
- Excel LO-34.

DOD pendiente
DOR pendiente



# BFF

### HU-LOG.06 — BFF — disparar envío de mail de bienvenida con reintentos e histórico

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.06`
- **Tipo:** Story
- **Capa:** BFF
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.05; MAGIA-62 / MAGIA-133
- **Origen Excel / POC:** LO-06

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO sistema BFF de Confirming
QUIERO orquestar el POST de envío de mail de bienvenida hacia Notificaciones
PARA garantizar reintentos e histórico de notificaciones en Atlas Trade


NECESIDAD: El BFF concentra el disparo desde ABM/alta y registra histórico.
CONTEXTO: Excel LO-06. Endpoint BFF: POST /v1/auth/welcome-mail/trigger. Usa servicio Notificaciones existente.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | BFF dispara welcome-mail y registra histórico exitoso |
| 3  | BFF reintenta ante fallo transitorio del servicio de notificaciones |
| 4  | BFF responde error controlado si Notificaciones no está disponible |

### Escenarios BDD (Gherkin)

**ID 1-Escenario BFF dispara welcome-mail y registra histórico exitoso**

Dado un alta que requiere mail de bienvenida, cuando el BFF invoca POST /v1/auth/welcome-mail/trigger,
- entonces llama al servicio de Notificaciones/Mail existente
- entonces guarda histórico de notificación en Atlas Trade
- entonces responde éxito al consumidor (ABM/proceso de alta)

**ID 3-Escenario BFF reintenta ante fallo transitorio del servicio de notificaciones**

Dado un fallo transitorio de Notificaciones, cuando el BFF procesa el envío,
- entonces aplica política de reintentos
- entonces actualiza el histórico con el estado del intento

**ID 4-Escenario BFF responde error controlado si Notificaciones no está disponible**

Dado Notificaciones no disponible tras reintentos, cuando el BFF finaliza el flujo,
- entonces responde error controlado al origen
- entonces el histórico refleja el fallo

### Criterios de aceptación

Que el BFF invoque el servicio de notificaciones existente
Que existan reintentos ante fallos transitorios
Que se persista histórico de notificaciones en Atlas Trade

### Fuera de alcance

- Diseño del template HTML del mail
- UI de reenvío manual (si aplica ABM aparte)

### Notas / preguntas abiertas

- Duda Excel: Guarda histórico de notificaciones en Atlas Trade; BFF llama al servicio ya existente.

DOD pendiente
DOR pendiente



### HU-LOG.11 — BFF — Validar usuario/contraseña temporal (flag pass temporal)

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.11`
- **Tipo:** Story
- **Capa:** BFF
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.01; Keycloak
- **Origen Excel / POC:** LO-11

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO BFF de autenticación
QUIERO validar mail/usuario y contraseña temporal contra Keycloak devolviendo flag de pass temporal
PARA indicar al FE que debe forzar el cambio de contraseña en el primer login


NECESIDAD: El FE depende del flag para enrutar al wizard.
CONTEXTO: Excel LO-11. Relacionado a POST /v1/auth/first-login y login-policy de canales.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Credencial temporal válida responde con flag temporal y nextStep |
| 4  | Credencial inválida responde error sin filtrar datos sensibles |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Credencial temporal válida responde con flag temporal y nextStep**

Dado un usuario en primer login con pass temporal vigente, cuando el BFF valida contra Keycloak,
- entonces autentica la temporal
- entonces responde con flag de contraseña temporal y nextStep de actualización (y canales permitidos si aplica)
- entonces no entrega acceso completo a la plataforma aún

**ID 4-Escenario Credencial inválida responde error sin filtrar datos sensibles**

Dado usuario/contraseña inválidos, cuando el BFF valida,
- entonces responde error de autenticación (401/422 según contrato)
- entonces no expone detalles internos de Keycloak

### Criterios de aceptación

Que la validación consulte Keycloak
Que la respuesta incluya flag de pass temporal para forzar cambio
Que el contrato sea consumible por el FE del wizard

### Fuera de alcance

- Pantallas FE
- Actualización de contraseña (HU-LOG.12)

### Notas / preguntas abiertas

- Escenarios derivados (columna Escenarios vacía en Excel).

DOD pendiente
DOR pendiente



### HU-LOG.12 — BFF — Actualizar contraseña ingresada por el usuario (primer login)

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.12`
- **Tipo:** Story
- **Capa:** BFF
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.11; Keycloak
- **Origen Excel / POC:** LO-13

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO BFF de autenticación
QUIERO actualizar la contraseña ingresada por el usuario tras la temporal
PARA dejar la cuenta lista para enrollment 2FA


NECESIDAD: Sustituye la temporal por la definitiva vía Keycloak/política de dominio.
CONTEXTO: Excel LO-13. LO-12 (HB en primer login) tachado — fuera de alcance de esta HU.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | PATCH/POST de nueva contraseña válida actualiza Keycloak y avanza nextStep 2FA |
| 4  | Contraseña que no cumple política es rechazada |

### Escenarios BDD (Gherkin)

**ID 1-Escenario PATCH/POST de nueva contraseña válida actualiza Keycloak y avanza nextStep 2FA**

Dado un usuario con sesión de primer login válida, cuando el BFF recibe la nueva contraseña válida,
- entonces actualiza la credencial en Keycloak
- entonces invalida la contraseña temporal
- entonces responde nextStep de configuración 2FA

**ID 4-Escenario Contraseña que no cumple política es rechazada**

Dado un payload con contraseña inválida según política, cuando el BFF procesa la actualización,
- entonces responde error de validación
- entonces no cambia la contraseña vigente

### Criterios de aceptación

Que el BFF actualice la contraseña en Identity/Keycloak
Que se invalide la temporal
Que se indique el siguiente paso (2FA)

### Fuera de alcance

- Actualización integrada a Home Banking en el primer login (LO-12 tachado)
- Cambio de contraseña olvidada post-alta (HU-LOG.20+)

### Notas / preguntas abiertas

- Escenarios derivados (Escenarios vacío).
- Spike HB sigue abierto a nivel producto.

DOD pendiente
DOR pendiente



### HU-LOG.14 — BFF — Obtener mail del usuario para envío OTP

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.14`
- **Tipo:** Story
- **Capa:** BFF
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Media
- **Dependencias:** HU-LOG.13; padrón de usuarios
- **Origen Excel / POC:** xx EP GET Mail del usuario

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO BFF de autenticación
QUIERO obtener el mail del usuario para prellenar / enviar el OTP
PARA mostrar en FE el destino del código y permitir cambio controlado


NECESIDAD: El FE muestra 'Te enviamos un correo a {mail}'.
CONTEXTO: Excel: EP GET BFF/BE - Mail del usuario (sin issue_key LO).

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | BFF devuelve mail enmascarado o completo según política de UI |
| 4  | Usuario sin mail registrado no puede completar OTP hasta cargar uno |

### Escenarios BDD (Gherkin)

**ID 1-Escenario BFF devuelve mail enmascarado o completo según política de UI**

Dado un usuario autenticado en el wizard 2FA, cuando el FE solicita el mail,
- entonces el BFF responde el correo registrado del usuario
- entonces el FE puede mostrar el destino del OTP

**ID 4-Escenario Usuario sin mail registrado no puede completar OTP hasta cargar uno**

Dado un usuario sin mail, cuando se intenta enviar OTP,
- entonces el BFF indica que se requiere mail
- entonces el FE habilita captura de correo válido

### Criterios de aceptación

Que exista endpoint GET de mail de usuario usable por el wizard
Que el FE pueda mostrar y opcionalmente cambiar el destino del OTP

### Fuera de alcance

- ABM de alta de usuarios

### Notas / preguntas abiertas

- issue_key xx — ID generado HU-LOG.14.
- Escenarios derivados.

DOD pendiente
DOR pendiente



### HU-LOG.16 — BFF — Validación de credenciales AD / Homebanking / Manual

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.16`
- **Tipo:** Story
- **Capa:** BFF
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.01
- **Origen Excel / POC:** LO-26

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO BFF de autenticación
QUIERO validar credenciales de login recurrente vía Keycloak (AD/HB/Manual)
PARA iniciar la sesión o indicar que se requiere 2FA


NECESIDAD: Keycloak diferencia el origen de la contraseña; el BFF orquesta OAuth/token-exchange.
CONTEXTO: Endpoints: POST /v1/auth/login y POST /v1/auth/token-exchange (matriz).

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Login válido devuelve tokens y mfaRequired según política |
| 4  | Login inválido incrementa intentos / puede dejar usuario bloqueado |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Login válido devuelve tokens y mfaRequired según política**

Dado un usuario recurrente con credenciales válidas, cuando el BFF ejecuta login/token-exchange,
- entonces obtiene autorización OAuth vía Keycloak
- entonces responde access/refresh token y flag mfaRequired si aplica
- entonces registra intento/sesión de auditoría según diseño

**ID 4-Escenario Login inválido incrementa intentos / puede dejar usuario bloqueado**

Dado credenciales inválidas, cuando el BFF valida,
- entonces responde error al FE
- SI se alcanzan N intentos (3),
  - entonces Keycloak/BFF dejan la cuenta bloqueada y actualizan flag de pass bloqueada

### Criterios de aceptación

Que el BFF unifique la validación sin que el FE elija el store de passwords
Que se exponga si corresponde MFA
Que se integre con la política de bloqueo

### Fuera de alcance

- UI
- Enrollment 2FA primer login

### Notas / preguntas abiertas

- Nota Excel LO-26: Keycloak se encarga de diferenciar dónde buscar la pass.

DOD pendiente
DOR pendiente



### HU-LOG.18 — BFF — Validación de 2FA (OTP) en login recurrente

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.18`
- **Tipo:** Story
- **Capa:** BFF
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.13; HU-LOG.16
- **Origen Excel / POC:** LO-28

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO BFF de autenticación
QUIERO validar el OTP de 2FA y registrar dispositivo confiable si corresponde
PARA cerrar el login recurrente de forma segura


NECESIDAD: Contrato: POST /v1/auth/mfa/verify { otp, trustDevice } → verified + deviceId.
CONTEXTO: Excel LO-28.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | OTP válido verifica MFA y opcionalmente registra DISPOSITIVO_CONFIABLE |
| 4  | OTP inválido responde error |

### Escenarios BDD (Gherkin)

**ID 1-Escenario OTP válido verifica MFA y opcionalmente registra DISPOSITIVO_CONFIABLE**

Dado un login con mfaRequired, cuando el BFF recibe OTP correcto,
- entonces responde verified=true
- SI trustDevice=true,
  - registra DISPOSITIVO_CONFIABLE y devuelve deviceId
- entonces habilita la sesión de plataforma

**ID 4-Escenario OTP inválido responde error**

Dado un OTP incorrecto, cuando el BFF valida,
- entonces responde error de verificación
- entonces no emite sesión completa

### Criterios de aceptación

Que el endpoint de verify MFA esté disponible para el FE
Que se pueda registrar dispositivo confiable

### Fuera de alcance

- UI
- Política de caducidad de dispositivo confiable (si aplica más adelante)

### Notas / preguntas abiertas

- Escenarios derivados (Escenarios vacío).

DOD pendiente
DOR pendiente



### HU-LOG.20 — BFF — Emitir/validar cookie de sesión junto al inicio de sesión

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.20`
- **Tipo:** Story
- **Capa:** BFF
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Media
- **Dependencias:** HU-LOG.16
- **Origen Excel / POC:** xx EP validador cookie

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO BFF de autenticación
QUIERO emitir y validar la cookie de sesión junto al login
PARA permitir al FE detectar sesión inválida y volver al login


NECESIDAD: Complementa el idle timer FE.
CONTEXTO: Excel: EP validador del inicio de sesión envía también el cookie.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Login exitoso setea cookie de sesión usable por el FE |
| 4  | Cookie inválida o ausente no autoriza recursos protegidos |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Login exitoso setea cookie de sesión usable por el FE**

Dado un login/token-exchange exitoso (y MFA OK si aplica), cuando el BFF cierra el flujo,
- entonces emite cookie/sesión según política
- entonces el FE puede usarla para detectar validez

**ID 4-Escenario Cookie inválida o ausente no autoriza recursos protegidos**

Dado cookie inválida, cuando el FE/BFF validan la sesión,
- entonces se niega el acceso
- entonces se deriva al login

### Criterios de aceptación

Que el inicio de sesión entregue cookie/sesión al FE
Que la invalidación fuerce re-login

### Fuera de alcance

- Diseño visual del modal de inactividad

### Notas / preguntas abiertas

- issue_key xx — ID generado HU-LOG.20.
- Escenarios derivados.

DOD pendiente
DOR pendiente



### HU-LOG.24 — BFF — PATCH cambio de contraseña (olvido/desbloqueo)

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.24`
- **Tipo:** Story
- **Capa:** BFF
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.01; Notificaciones OTP si aplica
- **Origen Excel / POC:** LO-33

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO BFF de autenticación
QUIERO exponer el cambio de contraseña (forgot/patch) según dominio
PARA actualizar credenciales y desbloquear si correspondía


NECESIDAD: Contratos: PATCH /v1/auth/password; POST /v1/auth/password/forgot con actions REDIRECT_AD | CHOOSE_CHANNEL | OTP_SENT.
CONTEXTO: Excel LO-33.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Cambio manual válido actualiza pass y desbloquea si estaba bloqueado |
| 2  | Forgot BANCO responde REDIRECT_AD |
| 3  | Forgot EGP/Proveedor responde CHOOSE_CHANNEL u OTP_SENT |
| 4  | Payload inválido no modifica la contraseña |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Cambio manual válido actualiza pass y desbloquea si estaba bloqueado**

Dado un usuario EGP/Proveedor en recuperación, cuando el BFF recibe PATCH válido (current/new/otp según contrato),
- entonces actualiza la contraseña en Identity
- SI estaba bloqueado,
  - entonces desbloquea la cuenta
- entonces responde updated=true

**ID 2-Escenario Forgot BANCO responde REDIRECT_AD**

Dado dominio BANCO, cuando se invoca password/forgot,
- entonces action=REDIRECT_AD con mensaje orientativo

**ID 3-Escenario Forgot EGP/Proveedor responde CHOOSE_CHANNEL u OTP_SENT**

Dado dominio EGP/Proveedor, cuando se invoca password/forgot,
- entonces el BFF responde CHOOSE_CHANNEL o inicia OTP_SENT según política/canal

**ID 4-Escenario Payload inválido no modifica la contraseña**

Dado un PATCH inválido, cuando el BFF valida,
- entonces responde error
- entonces no cambia la credencial

### Criterios de aceptación

Que existan forgot y patch de password en el BFF
Que se desbloquee al actualizar pass si correspondía
Que las actions orienten al FE por dominio

### Fuera de alcance

- Pantallas FE
- Sync real Home Banking (spike)

### Notas / preguntas abiertas

- Escenarios derivados + contratos de hoja API BFF.

DOD pendiente
DOR pendiente



### HU-LOG.25 — BFF/BE — Validación de password con actualización de flag de estado

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.25`
- **Tipo:** Story
- **Capa:** BFF
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta — seguridad
- **Dependencias:** HU-LOG.16; Keycloak
- **Origen Excel / POC:** LO-35

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO BFF/BE de autenticación
QUIERO validar la password respondiendo al FE y actualizando el flag de status de pass
PARA reflejar estados vigente / temporal / bloqueada / expirada hacia la UI


NECESIDAD: Complementa bloqueo por N intentos y ruteo del wizard.
CONTEXTO: Excel LO-35: EP POST Validación de pass (responde al FE y actualiza flag).

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Validación exitosa responde status de pass y permite continuar el flujo |
| 3  | Pass temporal responde flag que obliga cambio |
| 4  | Pass bloqueada/expirada responde flag y mensaje para FE |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Validación exitosa responde status de pass y permite continuar el flujo**

Dado un POST de validación de pass con credencial válida no bloqueada, cuando el BFF valida,
- entonces responde OK al FE con flag de status
- entonces actualiza el flag de status de pass en el modelo de sesión/usuario

**ID 3-Escenario Pass temporal responde flag que obliga cambio**

Dado una pass temporal, cuando se valida,
- entonces el flag indica temporal
- entonces el FE debe enrutar a cambio obligatorio

**ID 4-Escenario Pass bloqueada/expirada responde flag y mensaje para FE**

Dado pass bloqueada o expirada, cuando se valida,
- entonces el BFF responde el estado correspondiente
- entonces el FE muestra el flujo de bloqueo u olvido

### Criterios de aceptación

Que el EP de validación actualice y exponga el flag de status de pass
Que el FE pueda ramificar primer login / bloqueo / recurrente

### Fuera de alcance

- Copy final de mensajes de error
- UI

### Notas / preguntas abiertas

- Escenarios derivados (Escenarios vacío).

DOD pendiente
DOR pendiente



# BE

### HU-LOG.01 — Implementar servicio OAuth / Keycloak para login

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.01`
- **Tipo:** Task
- **Capa:** BE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta — bloqueante de todos los flujos de autenticación
- **Dependencias:** Configuración de ente Open-API Atlas; realm/client Keycloak
- **Origen Excel / POC:** LO-01

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO equipo de plataforma Confirming
QUIERO contar con OAuth (Keycloak) operativo para autenticar usuarios del Portal
PARA habilitar login seguro, tokens y políticas de credenciales por dominio


NECESIDAD: Sin Identity Provider no es posible primer login, login recurrente ni 2FA.
CONTEXTO: Excel LO-01. Matriz: capacidad OAuth Keycloak. Diagramas C4 context/containers.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Keycloak autentica usuario válido y emite tokens |
| 4  | Credenciales inválidas son rechazadas sin filtrar existencia de usuario |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Keycloak autentica usuario válido y emite tokens**

Dado un realm/client configurado para Atlas Confirming, cuando un usuario válido autentica,
- entonces Keycloak emite access/refresh token según política del realm
- entonces el BFF puede completar el intercambio de sesión hacia el Portal

**ID 4-Escenario Credenciales inválidas son rechazadas sin filtrar existencia de usuario**

Dado un intento de autenticación con credenciales inválidas, cuando Keycloak evalúa el login,
- entonces responde error de autenticación
- entonces no se expone si el usuario existe o no

### Criterios de aceptación

Que el servicio OAuth/Keycloak quede disponible para el BFF de login
Que existan clientes/scopes necesarios para BANCO, EGP y Proveedor
Que las políticas de bloqueo por intentos fallidos puedan aplicarse (n=3)

### Fuera de alcance

- Pantallas FE del wizard de login
- Mail de bienvenida (HU de notificaciones)

### Notas / preguntas abiertas

- Escenarios derivados de Summary/Objetivo (columna Escenarios vacía).
- Dependencia de spike 2FA AD para usuarios BANCO.

DOD pendiente
DOR pendiente



### HU-LOG.02 — Configurar ente Open-API Atlas y JWT hacia BFF OAuth

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.02`
- **Tipo:** Task
- **Capa:** BE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta — prerequisito de integraciones Core/Trade
- **Dependencias:** LO-01 / HU-LOG.01
- **Origen Excel / POC:** XX (issue_key no LO)

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO equipo de integración Atlas
QUIERO configurar el ente Open-API Atlas (JWT y conexión al BFF OAuth)
PARA permitir que Trade/Confirming consuma servicios Atlas de forma autenticada


NECESIDAD: Se requiere ente y token para conectar Trade como cliente Atlas.
CONTEXTO: Fila Excel sin issue_key LO (marcado XX). Objetivo: generar JWT y conexión a BFF OAuth.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Ente Open-API genera JWT válido para el BFF |
| 4  | JWT inválido o vencido es rechazado |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Ente Open-API genera JWT válido para el BFF**

Dado el ente Open-API Atlas configurado, cuando se solicita un JWT de servicio,
- entonces se obtiene un token firmado vigente
- entonces el BFF OAuth acepta la conexión con ese token

**ID 4-Escenario JWT inválido o vencido es rechazado**

Dado un JWT inválido o expirado, cuando se invoca un endpoint protegido,
- entonces la API responde no autorizado
- entonces no se ejecuta la operación de dominio

### Criterios de aceptación

Que exista configuración de ente Open-API para Trade/Confirming
Que el BFF OAuth acepte el JWT de servicio

### Fuera de alcance

- Flujos de UI de login

### Notas / preguntas abiertas

- issue_key vacío/XX en Excel — ID generado HU-LOG.02.
- Escenarios derivados de Summary/Objetivo.

DOD pendiente
DOR pendiente



### HU-LOG.03 — Configurar servicio de mail Atlas Core / Atlas Trade

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.03`
- **Tipo:** Task
- **Capa:** BE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta — habilita bienvenida y OTP
- **Dependencias:** HU-LOG.02; servicio Notificaciones Core
- **Origen Excel / POC:** xx mail services

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO equipo de plataforma
QUIERO configurar el servicio de mail entre Atlas Core y Atlas Trade
PARA enviar mails de bienvenida y OTP con templates correctos


NECESIDAD: Login depende de notificaciones (bienvenida y OTP 2FA).
CONTEXTO: Excel: Atlas Core - Atlas Trade configuración de servicios de mail.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Template de mail queda registrado y es usable por Notificaciones |
| 4  | Fallo de configuración impide envío y queda registrado |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Template de mail queda registrado y es usable por Notificaciones**

Dado el servicio de mail configurado, cuando se registra un template (bienvenida/OTP),
- entonces Atlas Core persiste el template
- entonces Atlas Trade guarda la referencia/ID de template usable por el BFF

**ID 4-Escenario Fallo de configuración impide envío y queda registrado**

Dado un error de configuración del canal de mail, cuando se intenta un envío,
- entonces el sistema no confirma entrega exitosa
- entonces queda traza para soporte/operaciones

### Criterios de aceptación

Que existan templates para bienvenida y validación OTP
Que Trade pueda referenciar el ID de template al disparar notificaciones

### Fuera de alcance

- Contenido visual del mail (copy final de negocio)

### Notas / preguntas abiertas

- issue_key xx en Excel — ID generado HU-LOG.03.
- Escenarios derivados de Summary/Objetivo.

DOD pendiente
DOR pendiente



### HU-LOG.04 — SPEC CORE — ente Trade, alta/baja Open API y permisos de notificaciones

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.04`
- **Tipo:** Task
- **Capa:** BE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta — prerequisito de notificaciones Trade
- **Dependencias:** HU-LOG.02
- **Origen Excel / POC:** xx SPEC CORE

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO equipo Core / Trade
QUIERO crear el ente Trade como cliente Atlas con permisos de notificaciones
PARA habilitar alta/baja Open API y envío de mails desde el dominio de Confirming


NECESIDAD: Sin ente y permisos, Trade no puede usar Notificaciones Core.
CONTEXTO: Excel SPEC CORE: Michi Fenix/Ignis Open API alta-baja; permisos ente notificaciones.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Ente Trade queda creado con permisos de notificaciones |
| 4  | Operación sin permisos es rechazada |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Ente Trade queda creado con permisos de notificaciones**

Dado el alta del ente Trade en Open API, cuando se asignan permisos de notificaciones,
- entonces Trade puede invocar el servicio de notificaciones como cliente Atlas
- entonces alta/baja de ente respeta el contrato Open API

**ID 4-Escenario Operación sin permisos es rechazada**

Dado un ente sin permiso de notificaciones, cuando intenta enviar un mail,
- entonces la API responde error de autorización
- entonces no se despacha la notificación

### Criterios de aceptación

Que exista ente Trade conectable como cliente Atlas
Que los permisos de notificaciones queden otorgados al ente

### Fuera de alcance

- Diseño de pantallas FE

### Notas / preguntas abiertas

- issue_key xx — ID generado HU-LOG.04.
- Escenarios derivados de Summary/Objetivo.

DOD pendiente
DOR pendiente



### HU-LOG.05 — Mail de bienvenida al alta — usuarios EGP / Proveedor

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.05`
- **Tipo:** Story
- **Capa:** BE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta — habilita primer acceso
- **Dependencias:** HU-LOG.03; HU-LOG.04; servicio Notificaciones existente (MAGIA-62 / MAGIA-133)
- **Origen Excel / POC:** LO-05

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO usuario con dominio/rol dado de alta en la plataforma
QUIERO recibir un mail de bienvenida
PARA obtener la información para loguearme en la plataforma


NECESIDAD: Tras el alta, el usuario EGP/Proveedor necesita link, usuario y contraseña temporal.
CONTEXTO: Excel LO-05. Mail BANCO (LO-03) tachado — fuera de alcance (Keycloak). Templates en Trade/Core.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Alta de usuario dispara mail con link, usuario y contraseña temporal |
| 4  | Fallo de envío no deja al usuario sin trazabilidad operativa |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Alta de usuario dispara mail con link, usuario y contraseña temporal**

Dado un usuario EGP o Proveedor dado de alta con mail válido, cuando el sistema procesa el alta,
- entonces se envía correo de bienvenida con link de acceso, usuario y contraseña temporal
- entonces Atlas Trade guarda el ID de template usado
- entonces el Servicio de Notificaciones de Core ejecuta el envío
- entonces Atlas Core mantiene el template de referencia

**ID 4-Escenario Fallo de envío no deja al usuario sin trazabilidad operativa**

Dado un error del servicio de notificaciones, cuando falla el envío del mail de bienvenida,
- entonces queda registrado el intento/histórico para reintento u operación manual
- entonces no se confirma al origen un envío exitoso

### Criterios de aceptación

Que el mail de bienvenida se dispare al alta de usuario EGP/Proveedor
Que el correo incluya link de acceso y credencial temporal
Que quede persistida la referencia de template en Trade/Core

### Fuera de alcance

- Mail de bienvenida usuarios BANCO (LO-03 tachado / Keycloak)
- Pantallas FE del primer login (HU FE asociadas a LO-10)

### Notas / preguntas abiertas

- Trazabilidad matriz: capacidad Mail bienvenida EGP/Proveedor.

DOD pendiente
DOR pendiente



### HU-LOG.13 — BE/BFF — Envío de mail OTP (template validación) y validación de código

#### Metadatos y alcance de la historia
- **ID Historia:** `HU-LOG.13`
- **Tipo:** Story
- **Capa:** BE
- **Épica:** LOG — Login Atlas Confirming
- **Prioridad sugerida:** Alta
- **Dependencias:** HU-LOG.03; HU-LOG.06; MAGIA-62 / MAGIA-133
- **Origen Excel / POC:** LO-24

> Este bloque **Metadatos y alcance de la historia** es **solo para el `.md`**.  
> **No** va en la columna Description del CSV (el CSV usa el cuerpo desde COMO).

---

COMO sistema de autenticación
QUIERO enviar mail OTP con template de validación y validar el código recibido
PARA completar el enrollment/verificación 2FA del login


NECESIDAD: Mismo servicio de notificaciones con flag/template distinto a bienvenida.
CONTEXTO: Excel LO-24: envío con template flag=validacion OTP / notificación primer mail; validación del código desde response.

ESCENARIOS

| ID | ESCENARIO |
|----|-----------|
| 1  | Se envía OTP con template de validación y se valida código correcto |
| 3  | Se reenvía OTP invalidando o supersidiendo el código anterior según política |
| 4  | Código incorrecto es rechazado |

### Escenarios BDD (Gherkin)

**ID 1-Escenario Se envía OTP con template de validación y se valida código correcto**

Dado un usuario en enrollment/verify 2FA, cuando se solicita el envío OTP,
- entonces se usa el template de validación OTP (distinto al de bienvenida)
- entonces el usuario recibe un código de 6 dígitos
- cuando ingresa el código correcto,
  - entonces la validación desde response confirma OK y se registra el factor

**ID 3-Escenario Se reenvía OTP invalidando o supersidiendo el código anterior según política**

Dado un OTP previo vigente, cuando el usuario solicita reenvío,
- entonces se emite un nuevo código según política
- entonces el histórico de notificaciones registra el nuevo envío

**ID 4-Escenario Código incorrecto es rechazado**

Dado un código OTP incorrecto, cuando se valida,
- entonces la respuesta indica fallo de verificación
- entonces no se completa el 2FA

### Criterios de aceptación

Que exista template diferenciado para OTP vs bienvenida
Que la validación del código se resuelva en BE/BFF con respuesta clara al FE

### Fuera de alcance

- UI del wizard (HU-LOG.10)
- 2FA AD BANCO

### Notas / preguntas abiertas

- Escenarios derivados parcialmente de Summary (Escenarios vacío).

DOD pendiente
DOR pendiente



## Glosario

| Término | Definición |
|---------|------------|
| AD | Active Directory corporativo (usuarios BANCO) |
| HB / Home Banking | Canal de credenciales Banco Atlas para clientes |
| OTP | One-Time Password enviado por mail (6 dígitos en POC) |
| Pass temporal | Credencial de un solo uso enviada en mail de bienvenida |
| BFF | Backend for Frontend de autenticación orientado a UI |
| Dispositivo confiable | Dispositivo marcado para política MFA posterior |

## Recomendaciones de escenarios faltantes

### HU-LOG.07 — Primer login BANCO
- Timeout / abandono mientras espera aprobación del AD.
- Usuario BANCO con cuenta bloqueada en AD (mensaje vs Mesa de Ayuda).

### HU-LOG.08 / HU-LOG.09 — Primer login EGP/Proveedor
- Doble submit / reintento al guardar contraseña (idempotencia).
- Sesión de primer login expirada a mitad del wizard.
- Pegado de contraseña con espacios leading/trailing.

### HU-LOG.10 / HU-LOG.17 — OTP
- Límite de reenvíos OTP por ventana de tiempo.
- OTP correcto pero sesión wizard expirada.
- Dispositivo ya confiable: ¿omitir OTP o pedirlo igual tras logout? (Excel sugiere siempre tras cerrar sesión).

### HU-LOG.15 / HU-LOG.23 — Login recurrente / bloqueo
- Mensajería exacta en intento 1 y 2 (¿mostrar intentos restantes?).
- Race: dos pestañas intentando login hasta bloqueo.
- Accesibilidad: toggle mostrar contraseña con teclado/lector de pantalla.

### HU-LOG.19 — Inactividad
- Actividad en otra pestaña del mismo origen ¿resetea timer?
- Warning visible mientras hay request largo en curso.

### HU-LOG.22 — Recuperación
- Proveedor no cliente sin HB: asegurar que no se muestre CTA HB habilitado.
- Olvido con usuario tipográficamente inválido (formato).

### Transversal
- Internacionalización / tono voseo vs usted en copy final de producción.
- Auditoría/logging de intentos sin PII excesiva.
