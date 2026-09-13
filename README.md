# SuperClaude

<p>
  <b>English</b> | <a href="./README.ko.md">한국어</a>
</p>

> A structured engineering toolkit, specialist agents, and workflow skills for Claude Code.

SuperClaude transforms [Claude Code](https://docs.claude.com/en/docs/claude-code) into a systematic software engineering platform. It introduces structured command dispatching, domain-specialist agent personas, and a comprehensive library of engineering workflow skills—covering everything from requirements discovery and deep research to test-driven implementation and code review.

---

## Highlights

- **32 Slash Commands**: Explicit, namespaced commands (`/super-claude:*`) for repeatable engineering tasks.
- **21 Specialist Agents**: Context-tailored personas for architecture, security audits, root-cause triage, and performance profiling.
- **32 Workflow Skills**: Reusable agent skills including TDD, systematic debugging, token budgeting, `claude-super-guide`, and `/btw`.
- **Side-Channel Q&A (`/btw`)**: Ask quick questions without polluting conversation memory or derailing ongoing tasks.
- **User Guide Included**: Run `/claude-super-guide` anytime for real-world scenarios and operational cheatsheets.
- **Automated Skill Synchronization**: Built-in `/super-claude:skill-update` tool to keep installed definitions in sync with Git.
- **Single-Command Setup**: Native PowerShell and Bash installers targeting `~/.claude/`.

---

## Installation

Clone the repository and run the installer for your platform. The installer registers all commands, agents, and skills directly into your global `~/.claude/` directory.

### Windows (PowerShell)

```powershell
git clone https://github.com/hsK10x2/super-claude.git
cd super-claude
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

### macOS / Linux (Bash)

```bash
git clone https://github.com/hsK10x2/super-claude.git
cd super-claude
chmod +x install.sh
./install.sh
```

Once installed, restart your `claude` session to load the updated registry.

---

## Quick Start

Open Claude Code in any project directory:

```bash
claude
```

Type `/super-claude` to view the central dashboard, or trigger the practical guide:

```text
> /claude-super-guide
> /btw what was the database port?
> /super-claude:recommend
> /super-claude:brainstorm "Authentication and Session Architecture"
> /super-claude:research "Zero-trust service-to-service communication patterns"
> /super-claude:implement "Token revocation endpoint with Redis backend"
```

---

## Command Reference

All commands are namespaced under `/super-claude:` to avoid collision with custom project commands.

### Guidance and Tooling

| Command | Description | Example |
| :--- | :--- | :--- |
| `/super-claude` | Main dashboard and command index | `/super-claude` |
| `/claude-super-guide` | Practical manual and real-world scenario cheatsheet | `/claude-super-guide` |
| `/btw` | Quick side Q&A without polluting context or breaking workflow | `/btw what was the Redis TTL?` |
| `/super-claude:recommend` | Context-aware command suggestions based on git state | `/super-claude:recommend` |
| `/super-claude:skill-update` | Audit and synchronize installed skills with repository | `/super-claude:skill-update` |
| `/super-claude:index-repo` | Repository structure indexing for context minimization | `/super-claude:index-repo` |

### Research and Analysis

| Command | Description | Example |
| :--- | :--- | :--- |
| `/super-claude:research` | Multi-source parallel web search and evidence synthesis | `/super-claude:research LLM agent patterns` |
| `/super-claude:analyze` | Code quality, security boundaries, and performance analysis | `/super-claude:analyze src/` |
| `/super-claude:spec-panel` | Multi-perspective specification review | `/super-claude:spec-panel` |
| `/super-claude:business-panel` | Business viability, risk analysis, and product alignment | `/super-claude:business-panel` |

### Planning and Architecture

| Command | Description | Example |
| :--- | :--- | :--- |
| `/super-claude:brainstorm` | Interactive requirements discovery and design alignment | `/super-claude:brainstorm billing service` |
| `/super-claude:design` | System architecture, boundary definition, and API contracts | `/super-claude:design event-bus` |
| `/super-claude:estimate` | Engineering complexity, risks, and effort estimation | `/super-claude:estimate migration-task` |

### Implementation and Quality Assurance

| Command | Description | Example |
| :--- | :--- | :--- |
| `/super-claude:implement` | Structured step-by-step feature implementation | `/super-claude:implement user-login` |
| `/super-claude:test` | Test execution, coverage audits, and failure analysis | `/super-claude:test tests/unit` |
| `/super-claude:troubleshoot` | Root-cause isolation, stack trace triage, and fix plans | `/super-claude:troubleshoot memory-spike` |
| `/super-claude:cleanup` | Dead code elimination and structural pruning | `/super-claude:cleanup` |
| `/super-claude:improve` | Targeted refactoring and maintainability improvements | `/super-claude:improve src/auth.py` |

### Repository and Workflow

| Command | Description | Example |
| :--- | :--- | :--- |
| `/super-claude:git` | Conventional Commits generator and git workflow helpers | `/super-claude:git` |
| `/super-claude:task` | Task breakdown, dependency graphs, and progress tracking | `/super-claude:task` |
| `/super-claude:workflow` | Multi-phase orchestration workflows | `/super-claude:workflow` |
| `/super-claude:agent` | Direct invocation of specialist agent roles | `/super-claude:agent pm-agent` |

---

## Specialist Agents

SuperClaude includes 21 persona definitions located in `agents/`. Agents can be engaged explicitly or delegated to during complex workflows:

| Agent | Focus Area |
| :--- | :--- |
| `@system-architect` | High-level distributed architecture, boundaries, and scalability |
| `@backend-architect` | API schemas, data models, persistence, and microservices |
| `@frontend-architect` | UI component hierarchy, client state, and performance |
| `@security-engineer` | Threat modeling, cryptographic standards, and vulnerability triage |
| `@performance-engineer` | Latency profiling, memory management, and throughput optimization |
| `@pm-agent` | Product requirements, user stories, and acceptance criteria |
| `@root-cause-analyst` | Complex failure investigation, log correlation, and regression prevention |
| `@quality-engineer` | Test suite architecture, integration coverage, and edge-case verification |
| `@refactoring-expert` | Technical debt remediation and clean code compliance |
| `@devops-architect` | CI/CD automation, containerization, and deployment safety |
| `@deep-research-agent` | Exhaustive literature review, technical benchmarking, and synthesis |
| `@technical-writer` | API reference generation, developer guides, and architecture records |

---

## Skills Library

The `skills/` directory provides modular Agent Skills adhering to the open `SKILL.md` specification:

- `btw`: Ephemeral side-channel Q&A protocol avoiding context pollution and task derailment
- `claude-super-guide`: Accessible user manual, cheatsheets, and scenario-based workflow guide
- `architecture-design`: System modeling, architectural trade-offs, and boundary maps
- `brainstorming`: Socratic exploration of intent, edge cases, and technical assumptions
- `browser-agent`: End-to-end browser automation and visual verification
- `commit-and-pr`: Conventional Commits automation and pull request drafting via GitHub CLI
- `confidence-check`: Pre-implementation readiness checks to prevent wasted iterations
- `deep-research`: Multi-source parallel research engine with citation verification
- `explain-code`: Companion markdown explainers tailored for junior developers and onboarding
- `grill-me`: Rigorous design stress-testing through structured questioning
- `how-many-tokens-left`: Session context token measurement and budget monitoring
- `skill-update`: Audit, synchronization, and health checking for installed Claude Code assets
- `systematic-debugging`: Scientific defect reproduction, isolation, and verification
- `test-driven-development`: Red-Green-Refactor test-driven development protocol
- `using-superclaude`: Pre-flight skill discovery and auto-activation rules
- `verification-before-completion`: Evidence-based success criteria verification before claiming completion

---

## Synchronization with `/super-claude:skill-update`

When this repository is modified or pulled from upstream, run:

```bash
# In Claude Code
/super-claude:skill-update

# Or directly via Python
python skills/skill-update/scripts/sync_skills.py --clean
```

---

## License

MIT License. See [LICENSE](./LICENSE) for details.
