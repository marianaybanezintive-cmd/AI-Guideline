# Arquitectura — Épica Login (MAGIA-155)

| Campo | Valor |
|-------|--------|
| **Fecha** | 2026-07-30 |
| **Épica** | [MAGIA-155](https://bancoatlaspy.atlassian.net/browse/MAGIA-155) — Login |
| **Producto** | Portal de Confirming (Atlas Trade) · Banco Atlas |
| **Historias Jira** | MAGIA-351, MAGIA-352, MAGIA-353, MAGIA-354, MAGIA-355, MAGIA-356, MAGIA-357, MAGIA-358, MAGIA-359, MAGIA-360, MAGIA-361 |
| **Historias técnicas** | MAGIA-362, MAGIA-363, MAGIA-364, MAGIA-365, MAGIA-366, MAGIA-367, MAGIA-368, MAGIA-369, MAGIA-370, MAGIA-371 |
| **Tareas** | MAGIA-372, MAGIA-373, MAGIA-374, MAGIA-375, MAGIA-116, MAGIA-264, MAGIA-274 |
| **Total issues procesadas** | 28 |
| **Generado con** | skill `jira-stories-to-architecture` · agente `po-architect-agent` (Alex) |

## Artefactos

| Archivo | Descripción |
|---------|-------------|
| [00-summary.md](./00-summary.md) | Síntesis PO + decisiones de arquitectura |
| [01-c4-context.mmd](./01-c4-context.mmd) / [.png](./01-c4-context.png) | Contexto C4 |
| [02-c4-containers.mmd](./02-c4-containers.mmd) / [.png](./02-c4-containers.png) | Contenedores FE/BFF/BE |
| [03-component-fe.mmd](./03-component-fe.mmd) / [.png](./03-component-fe.png) | Componentes Frontend |
| [04-component-bff.mmd](./04-component-bff.mmd) / [.png](./04-component-bff.png) | Componentes BFF Identity |
| [05-component-be.mmd](./05-component-be.mmd) / [.png](./05-component-be.png) | Componentes BE Identity |
| [06-er-database.mmd](./06-er-database.mmd) / [.png](./06-er-database.png) | Modelo ER Login/Sesión/Notificaciones |
| [07-sequence-mail-bienvenida.mmd](./07-sequence-mail-bienvenida.mmd) | Secuencia mail bienvenida |
| [07-sequence-primer-login-banco.mmd](./07-sequence-primer-login-banco.mmd) | Primer login BANCO (AD) |
| [07-sequence-primer-login-egp.mmd](./07-sequence-primer-login-egp.mmd) | Primer login EGP/Proveedor |
| [07-sequence-login-recurrente-2fa.mmd](./07-sequence-login-recurrente-2fa.mmd) | Login recurrente + 2FA |
| [07-sequence-cambio-password.mmd](./07-sequence-cambio-password.mmd) | Cambio / desbloqueo contraseña |
| [07-sequence-bloqueo-intentos.mmd](./07-sequence-bloqueo-intentos.mmd) | Bloqueo por n intentos |
| [08-user-flow-entes.mmd](./08-user-flow-entes.mmd) | User flow selección de ente |
| [09-user-flow-usuarios.mmd](./09-user-flow-usuarios.mmd) | User flow login por dominio |
| [10-user-flow-notificaciones.mmd](./10-user-flow-notificaciones.mmd) | User flow notificaciones |
| [11-api-rest-bff.md](./11-api-rest-bff.md) | Contratos BFF orientados a UI |
| [12-api-rest-be.md](./12-api-rest-be.md) | Contratos BE de dominio |
| [13-traceability.md](./13-traceability.md) | Matriz HU ↔ endpoint ↔ entidad ↔ diagrama |

## Cómo regenerar PNG

```bash
python "$HOME/.agents/skills/jira-stories-to-architecture/scripts/render_mermaid.py" .
```
