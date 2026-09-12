# SuperClaude Installer for Windows PowerShell
$ErrorActionPreference = "Stop"

Write-Host "🚀 Installing SuperClaude to ~/.claude..." -ForegroundColor Cyan

$claudeDir = Join-Path $HOME ".claude"
$commandsTarget = Join-Path $claudeDir "commands"
$agentsTarget = Join-Path $claudeDir "agents"
$skillsTarget = Join-Path $claudeDir "skills"

# Create directories if they do not exist
New-Item -ItemType Directory -Path $commandsTarget -Force | Out-Null
New-Item -ItemType Directory -Path $agentsTarget -Force | Out-Null
New-Item -ItemType Directory -Path $skillsTarget -Force | Out-Null

$scriptRoot = $PSScriptRoot

# 1. Install Commands
Write-Host "📦 Copying slash commands to $commandsTarget..." -ForegroundColor Yellow
Copy-Item "$scriptRoot\commands\super-claude.md" "$commandsTarget\" -Force
New-Item -ItemType Directory -Path "$commandsTarget\super-claude" -Force | Out-Null
Copy-Item "$scriptRoot\commands\super-claude\*.md" "$commandsTarget\super-claude\" -Force

# 2. Install Agents
Write-Host "🤖 Copying specialized agents to $agentsTarget..." -ForegroundColor Yellow
Copy-Item "$scriptRoot\agents\*.md" "$agentsTarget\" -Force

# 3. Install Skills
Write-Host "🧠 Copying skills to $skillsTarget..." -ForegroundColor Yellow
Get-ChildItem -Path "$scriptRoot\skills" -Directory | ForEach-Object {
    Copy-Item -Path $_.FullName -Destination "$skillsTarget\$($_.Name)" -Recurse -Force
}

Write-Host "`n✅ SuperClaude installed successfully!" -ForegroundColor Green
Write-Host "💡 Usage in Claude Code:" -ForegroundColor Cyan
Write-Host "   > /super-claude                (Open main dashboard)"
Write-Host "   > /super-claude:recommend      (Get recommended actions)"
Write-Host "   > /super-claude:research       (Deep web research)"
Write-Host "   > /super-claude:brainstorm     (Requirements & design brainstorming)"
Write-Host "   > /super-claude:implement      (Structured implementation workflow)"
