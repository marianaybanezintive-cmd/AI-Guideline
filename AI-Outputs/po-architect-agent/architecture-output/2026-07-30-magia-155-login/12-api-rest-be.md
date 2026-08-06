# 12 — API REST BE Identity (dominio)

Base: `/internal/v1` · Consumidor: BFF (no expuesto a Internet).

| Método | Path | HT | Descripción |
|--------|------|----|-------------|
| POST | `/internal/v1/notifications/welcome` | MAGIA-362 | Orquesta bienvenida + histórico + reintentos |
| POST | `/internal/v1/notifications/otp` | MAGIA-365 | Envía OTP (template distinto) |
| POST | `/internal/v1/auth/first-login` | MAGIA-363 | Valida temporal / nextStep dominio |
| PATCH | `/internal/v1/auth/password` | MAGIA-364, MAGIA-370 | Update password en IdP + flags |
| POST | `/internal/v1/auth/login` | MAGIA-367 | Validación credencial AD/Home/Manual vía Keycloak |
| POST | `/internal/v1/auth/mfa/verify` | MAGIA-368 | Verifica OTP challenge |
| GET | `/internal/v1/users/{id}/email` | MAGIA-366 | Mail canónico usuario |
| POST | `/internal/v1/auth/password/validate` | MAGIA-371 | Valida pass y actualiza flag status |
| POST | `/internal/v1/session/cookie-claims` | MAGIA-369 | Material para cookie BFF |

### Estados de notificación

`PENDIENTE` → `PENDIENTE_REINTENTO` → `ENVIADO` | `ERROR`

### Principios

- BE no conoce detalles de UI (sin `nextStep` de pantallas salvo campos de dominio).
- Keycloak es SoT de secretos; BE persiste flags e histórico de negocio.
- Llamadas a Atlas Core con idempotencia / correlation id.
