"""Skill MCP Hub Server implementation using FastMCP."""

import os
import sys
import subprocess
from typing import Dict, List, Optional, Any
from mcp.server.fastmcp import FastMCP
from .scanner import SkillScanner
from .grill_helper import GrillSessionManager, LENSES

# Initialize FastMCP Server
mcp = FastMCP(
    "Skill-MCP-Hub",
    instructions=(
        "Universal Skill MCP Hub. Exposes Agent Skills (SKILL.md, runbooks, scripts) "
        "to any MCP-compatible agent (Antigravity IDE, Claude Desktop, Cursor, Zed, etc.). "
        "Use list_skills / search_skills to discover available skills, get_skill to read instructions, "
        "and grill_me_session to conduct deep requirement interviews."
    ),
)

scanner = SkillScanner()
grill_manager = GrillSessionManager()


@mcp.tool()
def list_skills(query: Optional[str] = None, source: Optional[str] = None) -> List[Dict[str, Any]]:
    """List all available skills loaded from Claude, Antigravity, and workspace directories.
    
    Args:
        query: Optional search filter to filter skills by name or keyword.
        source: Optional filter by source: 'claude', 'gemini', 'workspace', 'custom'.
    """
    scanner.scan()
    skills = list(scanner.skills.values())

    if source:
        skills = [s for s in skills if s.source.lower() == source.lower()]

    if query:
        q = query.lower()
        skills = [s for s in skills if q in s.name.lower() or q in s.description.lower()]

    return [s.to_summary_dict() for s in skills]


@mcp.tool()
def get_skill(name: str) -> Dict[str, Any]:
    """Retrieve full details, instructions (SKILL.md), and resource tree for a specific skill.
    
    Args:
        name: The unique name identifier of the skill (e.g., 'grill-me', 'explain-code', 'commit-and-pr').
    """
    skill = scanner.get_skill(name)
    if not skill:
        return {
            "status": "error",
            "message": f"Skill '{name}' not found. Use list_skills to view available skills."
        }
    return {
        "status": "success",
        "skill": skill.to_full_dict()
    }


@mcp.tool()
def search_skills(query: str) -> List[Dict[str, Any]]:
    """Search for relevant skills using keywords or user intent.
    
    Args:
        query: Search query (e.g. 'code explanation', 'git commit', 'interview', 'deep research').
    """
    results = scanner.search_skills(query)
    return [s.to_summary_dict() for s in results]


@mcp.tool()
def read_skill_resource(name: str, relative_path: str) -> Dict[str, Any]:
    """Read a specific auxiliary file inside a skill (e.g. references/, templates/, scripts/).
    
    Args:
        name: The skill name (e.g. 'deep-research', 'grill-me').
        relative_path: The relative path inside the skill directory (e.g. 'templates/report_template.md').
    """
    skill = scanner.get_skill(name)
    if not skill:
        return {"status": "error", "message": f"Skill '{name}' not found."}

    # Security check: prevent directory traversal outside the skill path
    target_path = os.path.abspath(os.path.join(skill.path, relative_path))
    skill_root = os.path.abspath(skill.path)
    if not target_path.startswith(skill_root):
        return {"status": "error", "message": "Access denied: Path traversal detected."}

    if not os.path.isfile(target_path):
        return {"status": "error", "message": f"File '{relative_path}' does not exist in skill '{name}'."}

    try:
        with open(target_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        return {
            "status": "success",
            "skill": name,
            "path": relative_path,
            "content": content
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@mcp.tool()
def execute_skill_script(
    name: str,
    script_name: str,
    args: Optional[List[str]] = None,
    cwd: Optional[str] = None
) -> Dict[str, Any]:
    """Execute a script located in a skill's scripts/ directory.
    
    Args:
        name: The skill name (e.g., 'grill-me', 'token-budget-guard').
        script_name: The script file name in scripts/ (e.g., 'grill_session.py').
        args: List of command-line arguments to pass to the script.
        cwd: Working directory to run the script in. Defaults to current directory.
    """
    skill = scanner.get_skill(name)
    if not skill:
        return {"status": "error", "message": f"Skill '{name}' not found."}

    script_path = os.path.abspath(os.path.join(skill.path, "scripts", script_name))
    scripts_dir = os.path.abspath(os.path.join(skill.path, "scripts"))
    if not script_path.startswith(scripts_dir) or not os.path.isfile(script_path):
        return {"status": "error", "message": f"Script '{script_name}' not found in {scripts_dir}."}

    ext = os.path.splitext(script_name)[1].lower()
    if ext == ".py":
        cmd = [sys.executable, script_path] + (args or [])
    elif ext in [".js", ".mjs"]:
        cmd = ["node", script_path] + (args or [])
    elif ext in [".sh", ".bash"]:
        cmd = ["bash", script_path] + (args or [])
    elif ext in [".bat", ".cmd"]:
        cmd = [script_path] + (args or [])
    else:
        return {"status": "error", "message": f"Unsupported script extension: {ext}"}

    try:
        run_cwd = cwd or os.getcwd()
        result = subprocess.run(
            cmd,
            cwd=run_cwd,
            capture_output=True,
            text=True,
            timeout=60,
            encoding="utf-8",
            errors="replace"
        )
        return {
            "status": "success" if result.returncode == 0 else "failure",
            "exit_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except subprocess.TimeoutExpired:
        return {"status": "error", "message": f"Execution timed out (limit: 60s)."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@mcp.tool()
def grill_me_session(
    action: str,
    topic: Optional[str] = None,
    domain: Optional[str] = "coding",
    lens: Optional[str] = None,
    previous_answer: Optional[str] = None,
    session_id: Optional[str] = None,
    intent: Optional[str] = None,
    constraints: Optional[List[str]] = None,
    key_decisions: Optional[List[Dict[str, str]]] = None,
    surfaced_assumptions: Optional[List[str]] = None,
    open_questions: Optional[List[str]] = None,
    out_of_scope: Optional[List[str]] = None,
    target_dir: Optional[str] = None
) -> Dict[str, Any]:
    """Dedicated interactive session helper for the grill-me interview skill.
    
    Conducts relentless questioning across First-principles, Constraints, Pre-mortem,
    Steelman, and Boundary lenses, and generates distilled session logs in .grill/<slug>.md.
    
    Args:
        action: One of 'start', 'next', 'save_log', 'list_lenses'.
        topic: The topic, architecture, decision, or plan to pressure-test (required for 'start').
        domain: Domain of topic: 'coding', 'business_product', 'marketing_branding', 'sop_process', 'general_decision'.
        lens: Questioning lens key (e.g. 'first_principles', 'constraints', 'pre_mortem', 'steelman_opposite', 'boundary_testing').
        previous_answer: The user's answer to the previous grilling question (used for 'next').
        session_id: The ID of an active grilling session.
        intent: The refined intent summary (required for 'save_log').
        constraints: List of discovered non-negotiable constraints.
        key_decisions: List of dicts with keys 'decision', 'reason', 'alternative'.
        surfaced_assumptions: List of surfaced hidden assumptions.
        open_questions: List of unresolved questions deferred for later.
        out_of_scope: List of items explicitly ruled out of scope.
        target_dir: Directory where .grill/<slug>.md should be saved. Defaults to current working directory.
    """
    act = action.lower()

    if act == "list_lenses":
        return {
            "status": "success",
            "lenses": {k: v["name"] for k, v in LENSES.items()}
        }

    if act == "start":
        if not topic:
            return {"status": "error", "message": "Field 'topic' is required when starting a grill session."}
        return grill_manager.start_session(topic=topic, domain=domain or "coding", lens=lens)

    if act == "next":
        if not previous_answer:
            return {"status": "error", "message": "Field 'previous_answer' is required to drill into the next question."}
        return grill_manager.next_question(
            session_id=session_id or "default_session",
            previous_answer=previous_answer,
            next_lens=lens
        )

    if act == "save_log":
        if not topic or not intent:
            return {"status": "error", "message": "Fields 'topic' and 'intent' are required to save a session log."}
        return grill_manager.save_log(
            topic=topic,
            intent=intent,
            constraints=constraints,
            key_decisions=key_decisions,
            surfaced_assumptions=surfaced_assumptions,
            open_questions=open_questions,
            out_of_scope=out_of_scope,
            target_dir=target_dir
        )

    return {
        "status": "error",
        "message": f"Unknown action '{action}'. Supported actions: 'start', 'next', 'save_log', 'list_lenses'."
    }


# Prompts
@mcp.prompt()
def grill_me_prompt(topic: str) -> str:
    """Prompt template for conducting a relentless grill-me interview on any idea, architecture, or plan."""
    skill = scanner.get_skill("grill-me")
    instructions = skill.body if skill else "Interview the user relentlessly to surface intent, constraints, hidden assumptions, and unstated alternatives."
    return f"""당신은 사용자의 계획과 의도를 집요하게 검증하는 'grill-me' 인터뷰어입니다.
주제: {topic}

다음 핵심 지침을 엄격히 따라 질문을 1개씩 던지고 strawman 추천 답변을 함께 제시하세요:
{instructions}
"""


@mcp.prompt()
def explain_code_prompt(target_file_or_code: str) -> str:
    """Prompt template for generating junior-developer friendly explanation markdown documents."""
    skill = scanner.get_skill("explain-code")
    instructions = skill.body if skill else "Analyze the given code and write a structured explanation markdown document."
    return f"""다음 대상에 대해 초보 개발자 학습 및 유지보수용 설명서(MD)를 작성하세요:
대상: {target_file_or_code}

지침:
{instructions}
"""


@mcp.prompt()
def commit_and_pr_prompt(message_hint: Optional[str] = None) -> str:
    """Prompt template for Conventional Commits and automated GitHub Pull Request creation."""
    skill = scanner.get_skill("commit-and-pr")
    instructions = skill.body if skill else "Inspect git diff, create Conventional Commits, and create PR using gh CLI."
    hint = f"메시지 힌트: {message_hint}" if message_hint else ""
    return f"""작업 트리의 변경 사항을 분석하여 Conventional Commits 커밋을 작성하고 GitHub PR을 생성하세요.
{hint}

지침:
{instructions}
"""


# Dynamic Resources
@mcp.resource("skill://{name}")
def get_skill_resource(name: str) -> str:
    """Exposes any skill's complete markdown runbook as an MCP resource."""
    skill = scanner.get_skill(name)
    if not skill:
        return f"# Error: Skill '{name}' not found."
    return skill.raw_content


def run_stdio():
    """Run FastMCP over standard input/output (Stdio)."""
    mcp.run(transport="stdio")


def run_sse(host: str = "127.0.0.1", port: int = 8765):
    """Run FastMCP over Server-Sent Events (SSE)."""
    mcp.run(transport="sse", host=host, port=port)


if __name__ == "__main__":
    run_stdio()
