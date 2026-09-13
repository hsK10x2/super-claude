---
name: super-claude
description: SuperClaude command dispatcher - Use /super-claude [command] to access all SuperClaude features
---

# SuperClaude Command Dispatcher

Central command dispatcher for the SuperClaude framework.

## Usage

All framework commands are organized under the `/super-claude:` namespace:

```text
/super-claude:command [arguments]
```

## Available Commands

### Research and Analysis
```text
/super-claude:research [query]         - Deep web research with parallel multi-source validation
/super-claude:analyze [path]           - Code quality, security, and performance analysis
/super-claude:spec-panel               - Multi-perspective specification review
/super-claude:business-panel           - Business viability and product impact review
```

### Planning and Architecture
```text
/super-claude:brainstorm [topic]       - Interactive requirements and architecture discovery
/super-claude:design [feature]         - System architecture and API design
/super-claude:estimate [task]          - Engineering effort and complexity estimation
```

### Implementation and Quality
```text
/super-claude:implement [spec]         - Structured step-by-step implementation workflow
/super-claude:test [target]            - Test execution, coverage audit, and failure analysis
/super-claude:troubleshoot [issue]     - Systematic debugging and root cause isolation
/super-claude:cleanup                  - Dead code removal and project structure pruning
/super-claude:improve                  - Targeted code refactoring and modernization
```

### Repository and Tooling
```text
/super-claude:index-repo               - Index repository structure for context and token optimization
/super-claude:task [action]            - Task tracking and milestone execution
/super-claude:workflow [name]          - Multi-phase structured engineering workflows
/super-claude:skill-update             - Synchronize and update installed skills and commands
```

### Specialist Agents
```text
/super-claude:agent [type]             - Launch specialized AI persona
```
Supported agent roles:
- `@system-architect` : High-level system architecture and boundary design
- `@backend-architect` : Data modeling, service design, and API contracts
- `@frontend-architect` : UI hierarchy, state management, and component architecture
- `@deep-research-agent` : Technical literature review and competitor benchmarking
- `@pm-agent` : Requirements prioritization and backlog grooming
- `@security-engineer` : Threat modeling, vulnerability scanning, and hardening
- `@performance-engineer` : Latency profiling, memory optimization, and benchmarks
- `@root-cause-analyst` : Failure investigation and log correlation
- `@quality-engineer` : Test strategy, edge case mapping, and QA sign-off
- `@refactoring-expert` : Technical debt resolution and architectural cleanups

### Status, Guidance and Side-Channels
```text
/super-claude:recommend                - Suggest optimal next commands based on project context
/super-claude:claude-super-guide       - Practical beginner-friendly manual and workflow guide
/super-claude:btw [question]           - Quick side question without polluting context or derailing work
/super-claude                          - Display this command index
```

## Quick Reference

| Command | Purpose | Example |
| :--- | :--- | :--- |
| `/super-claude:research` | Deep web research | `/super-claude:research LLM frameworks` |
| `/super-claude:brainstorm` | Requirements discovery | `/super-claude:brainstorm auth service` |
| `/super-claude:implement` | Structured development | `/super-claude:implement user login` |
| `/super-claude:troubleshoot` | Debugging and triage | `/super-claude:troubleshoot memory leak` |
| `/claude-super-guide` | Practical user manual | `/claude-super-guide` |
| `/btw` | Quick side Q&A | `/btw what was the Redis TTL?` |
| `/super-claude:skill-update` | Sync and update skills | `/super-claude:skill-update` |
| `/super-claude:index-repo` | Index repository | `/super-claude:index-repo` |
| `/super-claude:agent` | Specialist agents | `/super-claude:agent pm-agent` |
| `/super-claude` | Main dashboard | `/super-claude` |
