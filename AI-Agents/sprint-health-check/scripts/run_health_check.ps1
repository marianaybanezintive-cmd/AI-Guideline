# Ejecuta el pipeline completo: fetch -> analyze -> render.
# Uso (desde la raiz del repo AI-Guideline):
#   powershell -ExecutionPolicy Bypass -File AI-Agents/sprint-health-check/scripts/run_health_check.ps1
#
# Requiere JIRA_API_TOKEN configurado (ver README.md del repo).

param(
    [int]$BoardId = 0,
    [int]$SprintId = 0
)

$ErrorActionPreference = "Stop"

# Raiz del repo: tres niveles arriba de scripts/ (AI-Agents/sprint-health-check/scripts)
$SkillRoot = Split-Path -Parent $PSScriptRoot
$RepoRoot = Split-Path -Parent (Split-Path -Parent $SkillRoot)

$configPath = Join-Path $SkillRoot "config.json"
$config = Get-Content $configPath -Raw | ConvertFrom-Json

if ($BoardId -eq 0) { $BoardId = $config.board_id }
$outputDir = Join-Path $RepoRoot $config.output_dir
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

$rawPath = Join-Path $outputDir "raw.json"
$metricsPath = Join-Path $outputDir "metrics.json"

# Verificar credenciales antes de llamar a Jira
$token = [Environment]::GetEnvironmentVariable("JIRA_API_TOKEN", "User")
if (-not $token) { $token = $env:JIRA_API_TOKEN }
if (-not $token) {
    Write-Host ""
    Write-Host "Faltan credenciales de Jira." -ForegroundColor Red
    Write-Host "Ejecuta primero (una sola vez, en la terminal de Cursor con Ctrl+`):"
    Write-Host '  powershell -ExecutionPolicy Bypass -File "AI-Agents/sprint-health-check/scripts/set_credentials.ps1"'
    Write-Host ""
    exit 1
}

Write-Host "=== Sprint Health Check ===" -ForegroundColor Cyan
Write-Host "Repo:   $RepoRoot"
Write-Host "Output: $outputDir"
Write-Host ""

# Paso 1 — descargar
$fetchArgs = @(
    (Join-Path $PSScriptRoot "fetch_sprint_data.py"),
    "--board-id", $BoardId,
    "--config", $configPath,
    "-o", $rawPath
)
if ($SprintId -gt 0) { $fetchArgs += @("--sprint-id", $SprintId) }

python @fetchArgs
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

# Nombre del sprint para el archivo final
$sprintMeta = (Get-Content $rawPath -Raw | ConvertFrom-Json).sprint
$sprintName = $sprintMeta.name -replace '[\\/:*?"<>|]', '-'
$reportPath = Join-Path $outputDir "$sprintName - Health Check.md"

# Paso 2 — analizar
python (Join-Path $PSScriptRoot "analyze_sprint.py") $rawPath --config $configPath -o $metricsPath
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

# Paso 3 — renderizar
python (Join-Path $PSScriptRoot "render_report.py") $metricsPath --config $configPath -o $reportPath
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host ""
Write-Host "Informe generado:" -ForegroundColor Green
Write-Host "  $reportPath"
Write-Host ""
Write-Host "Para publicar en GitHub:"
Write-Host "  git add `"AI-Outputs/sprint-health-check/$sprintName - Health Check.md`""
Write-Host "  git commit -m `"docs: sprint health check $sprintName`""
Write-Host "  git push"
