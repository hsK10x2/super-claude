#!/usr/bin/env bash
set -e

echo "🚀 Installing SuperClaude to ~/.claude..."

CLAUDE_DIR="$HOME/.claude"
COMMANDS_TARGET="$CLAUDE_DIR/commands"
AGENTS_TARGET="$CLAUDE_DIR/agents"
SKILLS_TARGET="$CLAUDE_DIR/skills"

mkdir -p "$COMMANDS_TARGET/super-claude"
mkdir -p "$AGENTS_TARGET"
mkdir -p "$SKILLS_TARGET"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 1. Commands
echo "📦 Copying slash commands to $COMMANDS_TARGET..."
cp -f "$SCRIPT_DIR/commands/super-claude.md" "$COMMANDS_TARGET/"
cp -rf "$SCRIPT_DIR/commands/super-claude/"* "$COMMANDS_TARGET/super-claude/"

# 2. Agents
echo "🤖 Copying specialized agents to $AGENTS_TARGET..."
cp -rf "$SCRIPT_DIR/agents/"*.md "$AGENTS_TARGET/"

# 3. Skills
echo "🧠 Copying skills to $SKILLS_TARGET..."
cp -rf "$SCRIPT_DIR/skills/"* "$SKILLS_TARGET/"

echo ""
echo "✅ SuperClaude installed successfully!"
echo "💡 Usage in Claude Code:"
echo "   > /super-claude                (Open main dashboard)"
echo "   > /super-claude:recommend      (Get recommended actions)"
echo "   > /super-claude:research       (Deep web research)"
echo "   > /super-claude:brainstorm     (Requirements & design brainstorming)"
echo "   > /super-claude:implement      (Structured implementation workflow)"
