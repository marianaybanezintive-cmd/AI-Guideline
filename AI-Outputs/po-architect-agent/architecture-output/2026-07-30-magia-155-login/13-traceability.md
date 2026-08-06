# 13 — Matriz de trazabilidad

| HU (Jira) | Capacidad | Endpoint(s) | Entidad(s) | Diagrama(s) |
|-----------|-----------|-------------|------------|-------------|
| MAGIA-351 / LO-05 | Mail bienvenida | POST /v1/auth/welcome-mail/trigger | NOTIFICACION, USUARIO | 07-sequence-mail-bienvenida, 10-user-flow-notificaciones |
| MAGIA-362 / LO-06 | Envío mail BE | POST /internal/v1/notifications/welcome | NOTIFICACION, TEMPLATE_MAIL | 07-sequence-mail-bienvenida, 05-component-be |
| MAGIA-352 / LO-07 | Primer login BANCO | POST /v1/auth/login | USUARIO, SESION | 07-sequence-primer-login-banco, 09-user-flow-usuarios |
| MAGIA-353 / LO-10 | Primer login EGP/Prov | POST /v1/auth/first-login, PATCH /v1/auth/password | USUARIO, OTP_CHALLENGE | 07-sequence-primer-login-egp |
| MAGIA-363 / LO-11 | Validar temporal | POST /internal/v1/auth/first-login | USUARIO | 07-sequence-primer-login-egp |
| MAGIA-364 / LO-13 | Update password | PATCH /internal/v1/auth/password | USUARIO | 07-sequence-primer-login-egp, 07-sequence-cambio-password |
| MAGIA-354 / LO-22 | Setup 2FA | POST /v1/auth/mfa/setup|verify | OTP_CHALLENGE, DISPOSITIVO_CONFIABLE | 07-sequence-primer-login-egp |
| MAGIA-365 / LO-24 | OTP mail | POST /internal/v1/notifications/otp | OTP_CHALLENGE, NOTIFICACION | 10-user-flow-notificaciones |
| MAGIA-366 / LO-24-a | Mail usuario | GET /v1/auth/user/email | USUARIO | 04-component-bff |
| MAGIA-355 / LO-25 | Login recurrente | POST /v1/auth/login | USUARIO, SESION | 07-sequence-login-recurrente-2fa |
| MAGIA-367 / LO-26 | Validar credenciales | POST /internal/v1/auth/login | USUARIO, INTENTO_LOGIN | 07-sequence-login-recurrente-2fa |
| MAGIA-356 / LO-27 | 2FA posteriores | POST /v1/auth/mfa/verify | OTP_CHALLENGE, SESION | 07-sequence-login-recurrente-2fa |
| MAGIA-368 / LO-28 | Validar 2FA BE | POST /internal/v1/auth/mfa/verify | OTP_CHALLENGE | 07-sequence-login-recurrente-2fa |
| MAGIA-357 / LO-29 | Idle logout | GET /v1/auth/session + cookie | SESION | 03-component-fe, 09-user-flow-usuarios |
| MAGIA-369 / LO-29-a | Cookie sesión | cookie claims | SESION | 04-component-bff |
| MAGIA-358 / LO-30 | Cambio pwd BANCO | — (informativo FE) | USUARIO | 07-sequence-cambio-password |
| MAGIA-359 / LO-31 | Cambio pwd HomeBank | canal externo / R-01 | USUARIO | 07-sequence-cambio-password |
| MAGIA-360 / LO-32 | Cambio pwd manual | POST forgot + PATCH password | USUARIO, OTP_CHALLENGE | 07-sequence-cambio-password |
| MAGIA-370 / LO-33 | Forgot/update BE | PATCH/POST password | USUARIO | 07-sequence-cambio-password |
| MAGIA-361 / LO-34 | Bloqueo FE | POST password/validate | USUARIO, INTENTO_LOGIN | 07-sequence-bloqueo-intentos |
| MAGIA-371 / LO-35 | Flag status BE | POST /internal/v1/auth/password/validate | USUARIO, INTENTO_LOGIN | 07-sequence-bloqueo-intentos |
| MAGIA-372 / T-01 | OAuth Keycloak | infra OIDC | — | 01-c4-context, 02-c4-containers |
| MAGIA-373 / T-02 | Open API Atlas | JWT ente | ENTE | 01-c4-context |
| MAGIA-374 / T-03 | Templates mail | config Core/Trade | TEMPLATE_MAIL | 10-user-flow-notificaciones |
| MAGIA-375 / T-04 | SPEC CORE ente | alta ente Trade | ENTE | 01-c4-context |
| MAGIA-264 | Selección multi-ente | sesión + contexto ente | ENTE, SESION | 08-user-flow-entes |
| MAGIA-274 | CORS BFF | infra | — | 02-c4-containers |
| MAGIA-116 | Alta users script | ops | USUARIO | 09-user-flow-usuarios |

## Inventario Jira fuente

| Key | Tipo | Summary |
|-----|------|---------|
| [MAGIA-116](https://bancoatlaspy.atlassian.net/browse/MAGIA-116) | Tarea | Alta de users por rol y ADMIN BD por script |
| [MAGIA-264](https://bancoatlaspy.atlassian.net/browse/MAGIA-264) | Tarea | Login: selección de entidad cuando el usuario tiene múltiples entes |
| [MAGIA-274](https://bancoatlaspy.atlassian.net/browse/MAGIA-274) | Tarea | CORS: Ajuste de cors BFF |
| [MAGIA-351](https://bancoatlaspy.atlassian.net/browse/MAGIA-351) | Historia | LO-05 — Mail de bienvenida para EGP / PROVEEDOR |
| [MAGIA-352](https://bancoatlaspy.atlassian.net/browse/MAGIA-352) | Historia | LO-07 — Primer login BANCO con credenciales de AD |
| [MAGIA-353](https://bancoatlaspy.atlassian.net/browse/MAGIA-353) | Historia | LO-10 — Primer login EGP / PROVEEDOR con contraseña temporal |
| [MAGIA-354](https://bancoatlaspy.atlassian.net/browse/MAGIA-354) | Historia | LO-22 — Configuración de 2FA en el primer login (EGP / PROVEEDOR) |
| [MAGIA-355](https://bancoatlaspy.atlassian.net/browse/MAGIA-355) | Historia | LO-25 — Acceso recurrente con credenciales definitivas |
| [MAGIA-356](https://bancoatlaspy.atlassian.net/browse/MAGIA-356) | Historia | LO-27 — Validación de 2FA en accesos posteriores |
| [MAGIA-357](https://bancoatlaspy.atlassian.net/browse/MAGIA-357) | Historia | LO-29 — Cierre de sesión automático por inactividad |
| [MAGIA-358](https://bancoatlaspy.atlassian.net/browse/MAGIA-358) | Historia | LO-30 — Cambio / desbloqueo de contraseña · BANCO |
| [MAGIA-359](https://bancoatlaspy.atlassian.net/browse/MAGIA-359) | Historia | LO-31 — Cambio / desbloqueo de contraseña · EGP/PROVEEDOR con Home Banking |
| [MAGIA-360](https://bancoatlaspy.atlassian.net/browse/MAGIA-360) | Historia | LO-32 — Cambio / desbloqueo de contraseña · gestión manual |
| [MAGIA-361](https://bancoatlaspy.atlassian.net/browse/MAGIA-361) | Historia | LO-34 — Bloqueo de contraseña por n intentos (FE) |
| [MAGIA-362](https://bancoatlaspy.atlassian.net/browse/MAGIA-362) | Historia | LO-06 — POST · Envío de mail (Notificaciones existente) |
| [MAGIA-363](https://bancoatlaspy.atlassian.net/browse/MAGIA-363) | Historia | LO-11 — POST · Validar mail/contraseña temporal (flag temporal) |
| [MAGIA-364](https://bancoatlaspy.atlassian.net/browse/MAGIA-364) | Historia | LO-13 — PATCH · Actualizar contraseña ingresada por el usuario |
| [MAGIA-365](https://bancoatlaspy.atlassian.net/browse/MAGIA-365) | Historia | LO-24 — POST · Envío OTP + validación de código |
| [MAGIA-366](https://bancoatlaspy.atlassian.net/browse/MAGIA-366) | Historia | LO-24-a — GET · Mail del usuario *(propuesto)* |
| [MAGIA-367](https://bancoatlaspy.atlassian.net/browse/MAGIA-367) | Historia | LO-26 — POST · Validación de credenciales AD / Home / Manual |
| [MAGIA-368](https://bancoatlaspy.atlassian.net/browse/MAGIA-368) | Historia | LO-28 — POST · Validación de 2FA |
| [MAGIA-369](https://bancoatlaspy.atlassian.net/browse/MAGIA-369) | Historia | LO-29-a — Cookie de sesión en el inicio de sesión *(propuesto)* |
| [MAGIA-370](https://bancoatlaspy.atlassian.net/browse/MAGIA-370) | Historia | LO-33 — PATCH/POST · Cambio de contraseña (forgot + update) |
| [MAGIA-371](https://bancoatlaspy.atlassian.net/browse/MAGIA-371) | Historia | LO-35 — POST · Validación de pass + flag de estado |
| [MAGIA-372](https://bancoatlaspy.atlassian.net/browse/MAGIA-372) | Tarea | T-01 (LO-01) — Implementar servicio OAuth |
| [MAGIA-373](https://bancoatlaspy.atlassian.net/browse/MAGIA-373) | Tarea | T-02 (XX) — Configuración de ente Open-API Atlas |
| [MAGIA-374](https://bancoatlaspy.atlassian.net/browse/MAGIA-374) | Tarea | T-03 — Atlas Core / Atlas Trade — configuración de servicios de mail |
| [MAGIA-375](https://bancoatlaspy.atlassian.net/browse/MAGIA-375) | Tarea | T-04 — SPEC CORE |
