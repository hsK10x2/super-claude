# SuperClaude Installer for Windows PowerShell
$ErrorActionPreference = "Stop"

Write-Host "Installing SuperClaude to ~/.claude..." -ForegroundColor Cyan

$claudeDir = Join-Path $HOME ".claude"
$commandsTarget = Join-Path $claudeDir "commands"
$agentsTarget = Join-Path $claudeDir "agents"
$skillsTarget = Join-Path $claudeDir "skills"

# Create target directories
New-Item -ItemType Directory -Path $commandsTarget -Force | Out-Null
New-Item -ItemType Directory -Path $agentsTarget -Force | Out-Null
New-Item -ItemType Directory -Path $skillsTarget -Force | Out-Null

$scriptRoot = $PSScriptRoot

# 1. Install Commands
Write-Host "Syncing slash commands to $commandsTarget..." -ForegroundColor Gray
Copy-Item "$scriptRoot\commands\super-claude.md" "$commandsTarget\" -Force
Copy-Item "$scriptRoot\commands\super-claude.md" "$commandsTarget\skill-update.md" -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path "$commandsTarget\super-claude" -Force | Out-Null
Copy-Item "$scriptRoot\commands\super-claude\*.md" "$commandsTarget\super-claude\" -Force

# 2. Install Agents
Write-Host "Syncing specialized agents to $agentsTarget..." -ForegroundColor Gray
Copy-Item "$scriptRoot\agents\*.md" "$agentsTarget\" -Force

# 3. Install Skills
Write-Host "Syncing workflow skills to $skillsTarget..." -ForegroundColor Gray
Get-ChildItem -Path "$scriptRoot\skills" -Directory | ForEach-Object {
    Copy-Item -Path $_.FullName -Destination "$skillsTarget\$($_.Name)" -Recurse -Force
}

# Clean legacy sc directory if present
$legacySc = Join-Path $commandsTarget "sc"
if (Test-Path $legacySc) {
    Remove-Item $legacySc -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "Removed legacy commands/sc namespace." -ForegroundColor DarkGray
}

Write-Host "`nSuperClaude successfully installed." -ForegroundColor Green
Write-Host "Available commands in Claude Code:" -ForegroundColor Cyan
Write-Host "  /super-claude               Open command dashboard"
Write-Host "  /super-claude:recommend     View contextual suggestions"
Write-Host "  /super-claude:research      Run multi-source web research"
Write-Host "  /super-claude:brainstorm    Start requirements discovery"
Write-Host "  /super-claude:implement     Execute structured implementation"
Write-Host "  /super-claude:skill-update  Check and synchronize skills"
