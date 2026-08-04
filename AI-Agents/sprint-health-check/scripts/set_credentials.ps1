# Guarda las credenciales de Jira como variables de entorno del usuario.
# El token se ingresa oculto y no queda en el historial de la consola.
#
# DONDE EJECUTAR: terminal integrada de Cursor (Ctrl+`) en la raiz del repo AI-Guideline:
#   powershell -ExecutionPolicy Bypass -File "AI-Agents/sprint-health-check/scripts/set_credentials.ps1"

param(
    [string]$BaseUrl = "https://bancoatlaspy.atlassian.net",
    [string]$Email
)

if (-not $Email) {
    $Email = Read-Host "Correo de Atlassian"
}

Write-Host ""
Write-Host "Genera un token en: https://id.atlassian.com/manage-profile/security/api-tokens"
$secure = Read-Host "API token (no se muestra)" -AsSecureString
$token = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto(
    [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
)

if ([string]::IsNullOrWhiteSpace($token)) {
    Write-Error "No se ingreso ningun token."
    exit 1
}

# Persistente para sesiones futuras.
[Environment]::SetEnvironmentVariable("JIRA_BASE_URL", $BaseUrl, "User")
[Environment]::SetEnvironmentVariable("JIRA_EMAIL", $Email, "User")
[Environment]::SetEnvironmentVariable("JIRA_API_TOKEN", $token, "User")

# Disponible ya mismo en esta sesion.
$env:JIRA_BASE_URL = $BaseUrl
$env:JIRA_EMAIL = $Email
$env:JIRA_API_TOKEN = $token

Write-Host ""
Write-Host "Credenciales guardadas para el usuario actual." -ForegroundColor Green
Write-Host "  JIRA_BASE_URL = $BaseUrl"
Write-Host "  JIRA_EMAIL    = $Email"
Write-Host "  JIRA_API_TOKEN = (oculto, $($token.Length) caracteres)"
Write-Host ""
Write-Host "Verificacion rapida:" -ForegroundColor Cyan
Write-Host '  python scripts/fetch_sprint_data.py --board-id 1607 -o out/raw.json'
