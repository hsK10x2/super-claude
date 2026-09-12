#!/usr/bin/env bash
set -e

echo "Installing SuperClaude to ~/.claude..."

CLAUDE_DIR="$HOME/.claude"
COMMANDS_TARGET="$CLAUDE_DIR/commands"
AGENTS_TARGET="$CLAUDE_DIR/agents"
SKILLS_TARGET="$CLAUDE_DIR/skills"

mkdir -p "$COMMANDS_TARGET/super-claude"
mkdir -p "$AGENTS_TARGET"
mkdir -p "$SKILLS_TARGET"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 1. Commands
echo "Syncing slash commands to $COMMANDS_TARGET..."
cp -f "$SCRIPT_DIR/commands/super-claude.md" "$COMMANDS_TARGET/"
cp -rf "$SCRIPT_DIR/commands/super-claude/"* "$COMMANDS_TARGET/super-claude/"

# 2. Agents
echo "Syncing specialized agents to $AGENTS_TARGET..."
cp -rf "$SCRIPT_DIR/agents/"*.md "$AGENTS_TARGET/"

# 3. Skills
echo "Syncing workflow skills to $SKILLS_TARGET..."
cp -rf "$SCRIPT_DIR/skills/"* "$SKILLS_TARGET/"

# Clean legacy directory if present
if [ -d "$COMMANDS_TARGET/sc" ]; then
  rm -rf "$COMMANDS_TARGET/sc"
  echo "Removed legacy commands/sc namespace."
fi

echo ""
echo "SuperClaude successfully installed."
echo "Available commands in Claude Code:"
echo "  /super-claude               Open command dashboard"
echo "  /super-claude:recommend     View contextual suggestions"
echo "  /super-claude:research      Run multi-source web research"
echo "  /super-claude:brainstorm    Start requirements discovery"
echo "  /super-claude:implement     Execute structured implementation"
echo "  /super-claude:skill-update  Check and synchronize skills"
