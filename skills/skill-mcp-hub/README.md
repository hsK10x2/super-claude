# 🌐 Skill MCP Hub

**Universal Model Context Protocol (MCP) Hub for AI Agent Skills.**

Skill MCP Hub bridges the gap between file-based Agent Skills (`SKILL.md`) and any MCP-compatible AI agent or editor — including **Google Antigravity IDE**, **Claude Desktop**, **Claude Code**, **Cursor**, **Windsurf**, **Zed**, and custom agent frameworks (LangGraph, CrewAI, AutoGen).

---

## ✨ Features

- **Multi-Source Discovery**: Automatically scans and aggregates skills from:
  - `~/.claude/skills`
  - `~/.gemini/config/skills`
  - Workspace directories (`.agents/skills`, `.claude/skills`)
  - Any custom paths specified via `--skills-dir`
- **MCP Tools**:
  - `list_skills(query, source)`: Discover available skills, triggers, and resources.
  - `get_skill(name)`: Fetch full markdown instructions (`SKILL.md`) for progressive disclosure.
  - `search_skills(query)`: Intent and keyword matching across skills.
  - `read_skill_resource(name, relative_path)`: Read files from `references/`, `templates/`, etc.
  - `execute_skill_script(name, script_name, args, cwd)`: Run executable helpers in `scripts/`.
  - `grill_me_session(action, topic, ...)`: Specialized interactive assistant for deep requirement grilling.
- **MCP Prompts**: Dynamically exposes skills as interactive prompts (`/grill-me`, `/explain-code`, `/commit-and-pr`).
- **MCP Resources**: Access skills via URI `skill://<skill_name>`.
- **Dual Transports**: Supports both `stdio` (IDE integrations) and `sse` (remote/network agents).

---

## 🚀 Quick Start

### 1. View Discovered Skills
```bash
python -m skill_mcp_hub.cli --list
```

### 2. Run as Stdio MCP Server (Default)
```bash
python -m skill_mcp_hub.cli --transport stdio
```

### 3. Run as SSE Server (Remote / Web Agents)
```bash
python -m skill_mcp_hub.cli --transport sse --port 8765
```

---

## ⚙️ Configuration in MCP Clients

### 1. Antigravity IDE (`~/.gemini/config/mcp_config.json`)
```json
{
  "mcpServers": {
    "skill-hub": {
      "command": "python",
      "args": ["-m", "skill_mcp_hub.cli", "--transport", "stdio"],
      "env": {
        "PYTHONPATH": "C:\\Users\\cl041\\.gemini\\antigravity-ide\\scratch\\skill-mcp-hub"
      }
    }
  }
}
```

### 2. Claude Desktop (`%APPDATA%\Claude\claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "skill-hub": {
      "command": "python",
      "args": ["-m", "skill_mcp_hub.cli", "--transport", "stdio"],
      "env": {
        "PYTHONPATH": "C:\\Users\\cl041\\.gemini\\antigravity-ide\\scratch\\skill-mcp-hub"
      }
    }
  }
}
```

### 3. Cursor (`.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "skill-hub": {
      "command": "python",
      "args": ["-m", "skill_mcp_hub.cli", "--transport", "stdio"],
      "env": {
        "PYTHONPATH": "C:\\Users\\cl041\\.gemini\\antigravity-ide\\scratch\\skill-mcp-hub"
      }
    }
  }
}
```
