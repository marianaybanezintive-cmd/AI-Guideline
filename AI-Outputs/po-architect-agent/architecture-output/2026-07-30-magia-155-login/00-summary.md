# 00 — Síntesis PO y decisiones de arquitectura

## Objetivo de negocio

Habilitar el **login y autenticación** de usuarios de dominios **BANCO**, **EGP** y **PROVEEDOR** (cliente / no cliente) en el Portal de Confirming (Atlas Trade), incluyendo onboarding por mail, primer login, 2FA, sesión, cambio/desbloqueo de contraseña y bloqueo por intentos.

**Épica:** [MAGIA-155](https://bancoatlaspy.atlassian.net/browse/MAGIA-155)

## Actores

| Actor | Dominio | Credencial | 2FA | Cambio password |
|-------|---------|------------|-----|-----------------|
| Usuario interno Banco | BANCO | Active Directory (federado Keycloak) | Provisto por AD | Fuera del portal (Mesa de ayuda / AD) |
| Usuario EGP | EGP | Temporal → propia en Keycloak | OTP mail | Home Banking o manual |
| Proveedor cliente | PROVEEDOR | Ídem EGP | OTP mail | Home Banking o manual |
| Proveedor no cliente | PROVEEDOR | Ídem EGP | OTP mail | Solo manual + OTP |
| Admin ABM | BANCO/EGP | — | — | Dispara / reenvía mail bienvenida |
| Sistemas | Keycloak, Atlas Core Notificaciones, Home Banking, Open API Atlas | — | — | — |

## Capacidades (por historia)

| Capacidad | HU / HT | Notas |
|-----------|---------|-------|
| Mail bienvenida | MAGIA-351 / MAGIA-362 | Dispara onboarding EGP/Proveedor |
| Primer login BANCO | MAGIA-352 / MAGIA-367 / MAGIA-372 | AD + OAuth |
| Primer login EGP/Proveedor | MAGIA-353 / MAGIA-363 / MAGIA-364 | Temporal → definitiva |
| Setup 2FA primer login | MAGIA-354 / MAGIA-365 / MAGIA-366 | OTP mail |
| Login recurrente | MAGIA-355 / MAGIA-367 / MAGIA-369 | Cookie sesión |
| 2FA accesos posteriores | MAGIA-356 / MAGIA-368 | Siempre post logout |
| Timeout inactividad | MAGIA-357 / MAGIA-369 | Cookie BFF |
| Cambio password BANCO | MAGIA-358 | Informativo |
| Cambio password Home Banking | MAGIA-359 | Canal externo |
| Cambio password manual | MAGIA-360 / MAGIA-370 | Forgot + update |
| Bloqueo n intentos | MAGIA-361 / MAGIA-371 | Flag desde Keycloak |
| Multi-ente | MAGIA-264 | Selección entidad |
| Infra OAuth / OpenAPI / Mail / Ente | MAGIA-372..375 | Habilitadores |

## Entidades de dominio

- **Usuario** (dominio, rol, mail, estado, flags temporal/bloqueado)
- **Ente / Organización** (multi-ente por usuario)
- **Sesion** (cookie BFF, idle timeout)
- **DispositivoConfiable** (opcional post-2FA)
- **Notificacion** (histórico Atlas Trade: template, estado, reintentos)
- **OtpChallenge** (código, vigencia, propósito: 2FA / reset)
- **CredencialPolicy** (reglas RN-02 en Keycloak)

## Flujos principales

1. Alta ABM → mail bienvenida → primer login temporal → set password → setup 2FA → home
2. Login BANCO → OIDC/AD → (2FA AD) → home / selección ente
3. Login recurrente EGP/Proveedor → password → 2FA OTP → cookie sesión
4. Forgot / cambio password (manual o Home Banking)
5. Bloqueo por intentos → mensaje FE → Mesa de ayuda
6. Inactividad → cierre sesión automático

## NFR implícitos

- Seguridad financiera: no exponer datos sensibles en mail; temporal one-time; rate limiting recomendado (R-10 fuera de alcance Excel)
- Sesión por cookie HttpOnly emitida por BFF
- Reintentos mail con backoff (hasta 3)
- Trazabilidad de notificaciones e intentos de login

## Decisiones de arquitectura

| Decisión | Elección | Rationale | Trazabilidad |
|----------|----------|-----------|--------------|
| Separación capas | FE → BFF Identity → BE Identity + Keycloak | FE nunca decide origen de credencial | SUP-01, LO-26 |
| IdP | Keycloak (AD federado + users locales) | Un solo broker | T-01, LO-07 |
| Mail | Atlas Core Notificaciones (existente) | Reuso; histórico en Atlas Trade | LO-05, LO-06, T-03 |
| Sesión FE | Cookie BFF (+ token backend) | Nota Excel LO-29 | LO-29, LO-29-a |
| 2FA EGP/Proveedor | OTP por mail (no TOTP en MVP Excel) | Escenarios Excel; TOTP = R-02 pendiente | LO-22, LO-24, LO-27 |
| Password BANCO | Fuera de portal | AD es fuente de verdad | LO-30 |
| BFF contratos | `/v1/auth/*` orientados a UI | Hoja API BFF | HT LO-11..35 |
| BE contratos | `/internal/v1/**` | Dominio Identity | HT LO-06..35 |

## Supuestos

1. Keycloak resuelve el store de credenciales según dominio (AD vs local).
2. El alta ABM dispara `welcome-mail/trigger`.
3. Idle timeout sugerido: 5 minutos (S-06), parametrizable.
4. Vigencia contraseña temporal: 72 h (S-05).
5. Home Banking channel (R-01) no tiene endpoint vivo en Excel; LO-31 queda parcialmente bloqueado hasta decisión.

## Preguntas abiertas (spikes)

| ID | Pregunta | Impacto |
|----|----------|---------|
| S-01 | Experiencia 2FA AD (redirect vs embebido) | LO-07 / LO-27 BANCO |
| S-02 | Momento integración Home Banking | LO-10 / LO-31 |
| S-03 | Vigencia dispositivo confiable | LO-27 |
| S-04 | Política formal passwords SI | LO-10/31/32 |
| R-01..R-06 | Historias faltantes pre-prod | Ver documento HU v2 |
