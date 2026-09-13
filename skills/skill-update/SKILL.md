---
name: skill-update
description: Synchronizes, audits, and updates Claude Code skills, slash commands, and specialist agents from local repositories or remote sources. Use when the user asks to update skills ("스킬 업데이트해줘", "skill update", "/skill-update"), audit existing command definitions, or synchronize ~/.claude with the latest repository state.
---

# Skill Update Workflow

Audits and synchronizes Claude Code slash commands, specialist agents, and workflow skills against the source repository or upstream changes.

## When to Use

- Updating installed skills and commands to their latest versions
- Verifying consistency between `~/.claude/` and the local `super-claude` repository
- Cleaning up legacy or orphaned command namespaces (e.g. legacy `sc/` duplicates)
- Checking for outdated frontmatter or syntax errors across installed skills

## Core Steps

### 1. Audit Current State

Check what is currently installed in `~/.claude`:

```bash
# Preview changes without modifying files
python skills/skill-update/scripts/sync_skills.py --dry-run
```

Verify directory structure:
- `~/.claude/commands/super-claude/` (active command namespace)
- `~/.claude/agents/` (specialized agent prompts)
- `~/.claude/skills/` (agent workflow skills)

### 2. Synchronize Changes

Apply updates from the repository to the user configuration:

```bash
# Sync all components and clean legacy paths
python skills/skill-update/scripts/sync_skills.py --clean
```

Alternatively, use the native PowerShell installer on Windows:

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

Or on macOS/Linux:

```bash
./install.sh
```

### 3. Verify Registration

Run a quick status check to confirm Claude Code registers the updated commands:

```bash
claude --print "Check skill update status."
```

Confirm that:
- Commands are visible under `/super-claude:*`
- Deprecated or duplicate namespaces are absent
- Newly added skills are present in `~/.claude/skills/`
