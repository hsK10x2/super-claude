---
name: skill-update
description: Audit and synchronize SuperClaude skills, commands, and agents
---

# Skill Update

Synchronizes the installed Claude Code skills, commands, and agents with the latest version from the repository.

## Usage

```text
/super-claude:skill-update [options]
```

### Options

- `--check` : Preview changes without applying
- `--clean` : Remove deprecated or legacy commands
- `--force` : Overwrite all local modifications

## Actions Performed

1. Scans `~/.claude/commands/super-claude/`, `~/.claude/agents/`, and `~/.claude/skills/`.
2. Compares checksums against the current `super-claude` repository.
3. Updates modified files and registers newly added skills or commands.
4. Removes orphaned or redundant artifacts.

## Example

```text
> /super-claude:skill-update
> /super-claude:skill-update --check
```
