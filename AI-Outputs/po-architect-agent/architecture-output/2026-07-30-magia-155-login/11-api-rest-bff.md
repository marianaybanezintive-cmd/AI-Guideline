# 11 — API REST BFF (orientada a UI)

Base: `/v1/auth` · Consumidor: Frontend · Orquesta Keycloak + BE Identity.

| Método | Path | HU/HT | Descripción | Request (resumen) | Response (resumen) |
|--------|------|-------|-------------|-------------------|--------------------|
| POST | `/v1/auth/welcome-mail/trigger` | MAGIA-351, MAGIA-362 | Dispara mail bienvenida | `{ userId, templateId? }` | `202` |
| POST | `/v1/auth/first-login` | MAGIA-353, MAGIA-363 | Valida temporal | `{ email, password }` | `{ passwordTemporal, nextStep, channels[] }` |
| PATCH | `/v1/auth/password` | MAGIA-353, MAGIA-364, MAGIA-370 | Set/update password | `{ email, currentPassword?, newPassword, otp? }` | `{ nextStep }` |
| POST | `/v1/auth/login` | MAGIA-352, MAGIA-355, MAGIA-367 | Login recurrente / BANCO | `{ email\|username, password, domain }` | `{ requiresMfa, session?, nextStep }` |
| GET | `/v1/auth/user/email` | MAGIA-366 | Mail del usuario | — | `{ email, maskedEmail }` |
| POST | `/v1/auth/mfa/setup` | MAGIA-354, MAGIA-365 | Inicia setup 2FA OTP mail | `{ channel: "EMAIL" }` | `{ challengeId }` |
| POST | `/v1/auth/mfa/verify` | MAGIA-354, MAGIA-356, MAGIA-368 | Valida OTP | `{ challengeId, code }` | `{ trustedDevice?, session }` |
| POST | `/v1/auth/password/forgot` | MAGIA-360, MAGIA-370 | Inicio forgot | `{ email }` | `202` |
| POST | `/v1/auth/password/validate` | MAGIA-361, MAGIA-371 | Valida pass + flag status | `{ email, password }` | `{ ok, locked, remainingAttempts }` |
| POST | `/v1/auth/logout` | RN-06 / R-03 | Cierre sesión (recomendado) | — | `204` + clear cookie |
| GET | `/v1/auth/session` | MAGIA-357, MAGIA-369 | Estado sesión / idle | — | `{ active, expiresAt }` |

### Errores comunes UI

| HTTP | Código | Uso FE |
|------|--------|--------|
| 400 | `VALIDATION_ERROR` | Campos inválidos |
| 401 | `INVALID_CREDENTIALS` | Credencial incorrecta |
| 403 | `USER_LOCKED` | Bloqueo n intentos |
| 409 | `PASSWORD_TEMPORARY_REQUIRED` | Debe completar primer login |
| 429 | `RATE_LIMITED` | Abuso (recomendado) |

### Cookie de sesión

- Nombre sugerido: `ATLAS_SESSION`
- Flags: `HttpOnly`, `Secure`, `SameSite=Lax`
- Idle: configurable (default 5 min) — MAGIA-357 / MAGIA-369
