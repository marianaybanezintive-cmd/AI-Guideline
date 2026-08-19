# Pipeline: clone_issues.py -> render_report.py
# Uso (desde la raiz del repo AI-Guideline):
#   powershell -ExecutionPolicy Bypass -File AI-Agents/sm-mass-clone/scripts/run_mass_clone.ps1 `
#     -OriginType epic -OriginValue MAGIA-5 `
#     -IssueType Historia -Status "Tareas por hacer" `
#     -TitlePrefix "QA - " -Assignee "Alexis Alvarez"
#
# Dry-run:
#   ... -DryRun

param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("epica", "epic", "sprint", "backlog")]
    [string]$OriginType,

    [string]$OriginValue = "",

    [Parameter(Mandatory = $true)]
    [string]$IssueType,

    [Parameter(Mandatory = $true)]
    [string]$Status,

    [string]$TitlePrefix = "",

    [string]$Assignee = "",

    [ValidateSet("same_sprint", "backlog")]
    [string]$TargetPlacement = "same_sprint",

    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$SkillRoot = Split-Path -Parent $PSScriptRoot
$RepoRoot = Split-Path -Parent (Split-Path -Parent $SkillRoot)

$configPath = Join-Path $SkillRoot "config.json"
$config = Get-Content $configPath -Raw | ConvertFrom-Json
$outputDir = Join-Path $RepoRoot $config.output_dir
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

$lastRunPath = Join-Path $outputDir "last-run.json"
$stamp = Get-Date -Format "yyyyMMdd-HHmm"
$reportName = if ($DryRun) { "$stamp-clone-dry-run.md" } else { "$stamp-clone-report.md" }
$reportPath = Join-Path $outputDir $reportName

foreach ($name in @("JIRA_BASE_URL", "JIRA_EMAIL", "JIRA_API_TOKEN")) {
    $current = [Environment]::GetEnvironmentVariable($name, "Process")
    if (-not $current) {
        $stored = [Environment]::GetEnvironmentVariable($name, "User")
        if ($stored) { [Environment]::SetEnvironmentVariable($name, $stored, "Process") }
    }
}

$token = [Environment]::GetEnvironmentVariable("JIRA_API_TOKEN", "Process")
if (-not $token -or $token.Length -lt 10) {
    Write-Host ""
    Write-Host "Credenciales de Jira invalidas o incompletas (token: $($token.Length) caracteres)." -ForegroundColor Red
    Write-Host "Ejecuta una sola vez:"
    Write-Host '  powershell -ExecutionPolicy Bypass -File "AI-Agents/sm-mass-clone/scripts/set_credentials.ps1"'
    Write-Host ""
    exit 1
}

Write-Host "=== SM Mass Clone ===" -ForegroundColor Cyan
Write-Host "Repo:   $RepoRoot"
Write-Host "Output: $outputDir"
Write-Host "Mode:   $(if ($DryRun) { 'DRY-RUN' } else { 'CLONE' })"
Write-Host ""

$cloneArgs = @(
    (Join-Path $PSScriptRoot "clone_issues.py"),
    "--config", $configPath,
    "--origin-type", $OriginType,
    "--origin-value", $OriginValue,
    "--issue-type", $IssueType,
    "--status", $Status,
    "--title-prefix", $TitlePrefix,
    "--assignee", $Assignee,
    "--target-placement", $TargetPlacement,
    "-o", $lastRunPath
)
if ($DryRun) { $cloneArgs += "--dry-run" }

python @cloneArgs
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python (Join-Path $PSScriptRoot "render_report.py") $lastRunPath -o $reportPath
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host ""
Write-Host "Informe generado:" -ForegroundColor Green
Write-Host "  $reportPath"
Write-Host "  $lastRunPath"
Write-Host ""
