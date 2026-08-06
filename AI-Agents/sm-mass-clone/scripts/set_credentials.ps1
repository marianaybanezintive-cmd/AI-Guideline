# Guarda las credenciales de Jira como variables de entorno del usuario.
#
# Uso en terminal de Cursor (Ctrl+`):
#   powershell -ExecutionPolicy Bypass -File "AI-Agents/sm-mass-clone/scripts/set_credentials.ps1"
#
# Desde archivo (util si el pegado falla):
#   powershell -ExecutionPolicy Bypass -File "...\set_credentials.ps1" -TokenFile "C:\ruta\token.txt"
#
# NOTA: Read-Host -AsSecureString en Cursor solo captura 1 caracter al pegar.
#       Este script usa entrada visible, que es la unica forma fiable de pegar aqui.

param(
    [string]$BaseUrl = "https://bancoatlaspy.atlassian.net",
    [string]$Email = "mariana.ybanez@atlas.com.py",
    [string]$Token,
    [string]$TokenFile
)

if ($TokenFile) {
    if (-not (Test-Path $TokenFile)) {
        Write-Error "No existe el archivo: $TokenFile"
        exit 1
    }
    $Token = (Get-Content $TokenFile -Raw).Trim()
}

if (-not $Email) {
    $Email = Read-Host "Correo de Atlassian"
}

if (-not $Token) {
    Write-Host ""
    Write-Host "Genera un token en: https://id.atlassian.com/manage-profile/security/api-tokens"
    Write-Host ""
    Write-Host "IMPORTANTE (terminal de Cursor):" -ForegroundColor Yellow
    Write-Host "  Pega el token COMPLETO y presiona Enter."
    Write-Host "  Se vera en pantalla un instante - es normal; Cursor no soporta pegado oculto."
    Write-Host "  Debe mostrar ~190 caracteres al guardar."
    Write-Host ""
    $Token = Read-Host "API token"
    $Token = $Token.Trim()
}

if ([string]::IsNullOrWhiteSpace($Token) -or $Token.Length -lt 20) {
    $len = $Token.Length
    Write-Error "Token invalido: $len caracteres. Usa -TokenFile con un archivo .txt"
    exit 1
}

[Environment]::SetEnvironmentVariable("JIRA_BASE_URL", $BaseUrl, "User")
[Environment]::SetEnvironmentVariable("JIRA_EMAIL", $Email, "User")
[Environment]::SetEnvironmentVariable("JIRA_API_TOKEN", $Token, "User")

[Environment]::SetEnvironmentVariable("JIRA_BASE_URL", $BaseUrl, "Process")
[Environment]::SetEnvironmentVariable("JIRA_EMAIL", $Email, "Process")
[Environment]::SetEnvironmentVariable("JIRA_API_TOKEN", $Token, "Process")

Write-Host ""
Write-Host "Credenciales guardadas." -ForegroundColor Green
Write-Host "  JIRA_BASE_URL  = $BaseUrl"
Write-Host "  JIRA_EMAIL     = $Email"
Write-Host "  JIRA_API_TOKEN = $($Token.Length) caracteres"
Write-Host ""
Write-Host "Siguiente paso:" -ForegroundColor Cyan
Write-Host "  powershell -ExecutionPolicy Bypass -File AI-Agents/sm-mass-clone/scripts/run_mass_clone.ps1 -OriginType epic -OriginValue MAGIA-5 -IssueType Historia -Status `"Tareas por hacer`" -TitlePrefix `"QA - `" -DryRun"
