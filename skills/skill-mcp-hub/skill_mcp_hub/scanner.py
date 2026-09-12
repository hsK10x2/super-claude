"""Multi-directory skill scanner and parser for Skill MCP Hub."""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from .models import SkillMetadata

def parse_simple_frontmatter(content: str) -> Tuple[Dict[str, Any], str]:
    """Parse YAML-like frontmatter from markdown content without external dependencies.
    
    Supports:
    - key: value
    - key: >- / > / | (multi-line folded/literal text)
    - key: [list, of, values]
    - - list items under a key
    """
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content

    frontmatter_raw = parts[1]
    body = parts[2].strip()

    metadata: Dict[str, Any] = {}
    lines = frontmatter_raw.splitlines()
    current_key: Optional[str] = None
    multiline_buf: List[str] = []
    is_multiline = False

    def flush_multiline():
        nonlocal current_key, multiline_buf, is_multiline
        if current_key and is_multiline:
            metadata[current_key] = " ".join([l.strip() for l in multiline_buf if l.strip()])
            multiline_buf = []
            is_multiline = False

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # Check for top-level key: value
        match = re.match(r"^([a-zA-Z0-9_\-]+):\s*(.*)$", line)
        if match and not line.startswith(" ") and not line.startswith("\t"):
            flush_multiline()
            key = match.group(1).strip()
            val = match.group(2).strip()

            if val in (">-", ">", "|", "|-"):
                current_key = key
                is_multiline = True
                multiline_buf = []
            elif val.startswith("[") and val.endswith("]"):
                # inline list: [a, b, c]
                items = [item.strip().strip("'\"") for item in val[1:-1].split(",") if item.strip()]
                metadata[key] = items
                current_key = key
            elif val:
                metadata[key] = val.strip("'\"")
                current_key = key
            else:
                current_key = key
        elif is_multiline:
            if line.startswith(" ") or line.startswith("\t"):
                multiline_buf.append(line.strip())
            else:
                flush_multiline()
        elif current_key and (stripped.startswith("- ") or stripped.startswith("* ")):
            item_val = stripped[2:].strip().strip("'\"")
            if current_key not in metadata or not isinstance(metadata[current_key], list):
                metadata[current_key] = []
            metadata[current_key].append(item_val)

    flush_multiline()
    return metadata, body


class SkillScanner:
    """Discovers and parses skills across multiple directories."""

    DEFAULT_PATHS = [
        os.path.expanduser(r"~\.claude\skills"),
        os.path.expanduser(r"~\.gemini\config\skills"),
        os.path.expanduser(r"~\.gemini\antigravity-ide\builtin\skills"),
        os.path.abspath(r".\.agents\skills"),
        os.path.abspath(r".\.claude\skills"),
    ]

    def __init__(self, extra_paths: Optional[List[str]] = None):
        self.search_paths: List[str] = []
        for p in (extra_paths or []) + self.DEFAULT_PATHS:
            p_abs = os.path.abspath(p)
            if p_abs not in self.search_paths:
                self.search_paths.append(p_abs)
        self.skills: Dict[str, SkillMetadata] = {}

    def scan(self) -> Dict[str, SkillMetadata]:
        """Scan all configured paths and return discovered skills."""
        discovered: Dict[str, SkillMetadata] = {}

        for search_path in self.search_paths:
            if not os.path.isdir(search_path):
                continue

            try:
                for entry in os.listdir(search_path):
                    skill_dir = os.path.join(search_path, entry)
                    if not os.path.isdir(skill_dir):
                        continue

                    # Look for SKILL.md
                    skill_file = None
                    for candidate in ["SKILL.md", "skill.md", "Skill.md"]:
                        cand_path = os.path.join(skill_dir, candidate)
                        if os.path.isfile(cand_path):
                            skill_file = cand_path
                            break

                    if not skill_file:
                        continue

                    skill_obj = self._parse_skill_directory(skill_dir, skill_file, search_path)
                    if skill_obj and skill_obj.name not in discovered:
                        discovered[skill_obj.name] = skill_obj
            except Exception as e:
                print(f"[SkillScanner] Error scanning {search_path}: {e}")

        self.skills = discovered
        return self.skills

    def _parse_skill_directory(self, skill_dir: str, skill_file: str, root_path: str) -> Optional[SkillMetadata]:
        try:
            with open(skill_file, "r", encoding="utf-8") as f:
                content = f.read()

            frontmatter, body = parse_simple_frontmatter(content)
            name = frontmatter.get("name", os.path.basename(skill_dir)).strip()
            description = frontmatter.get("description", "").strip()

            # Determine source label
            if ".claude" in root_path:
                source = "claude"
            elif ".gemini" in root_path:
                source = "gemini"
            elif ".agents" in root_path:
                source = "workspace"
            else:
                source = "custom"

            # Check for subdirectories
            scripts = []
            scripts_dir = os.path.join(skill_dir, "scripts")
            if os.path.isdir(scripts_dir):
                scripts = [f for f in os.listdir(scripts_dir) if os.path.isfile(os.path.join(scripts_dir, f))]

            templates = []
            templates_dir = os.path.join(skill_dir, "templates")
            if os.path.isdir(templates_dir):
                templates = [f for f in os.listdir(templates_dir) if os.path.isfile(os.path.join(templates_dir, f))]

            references = []
            refs_dir = os.path.join(skill_dir, "references")
            if os.path.isdir(refs_dir):
                refs_dir_path = refs_dir
                references = [f for f in os.listdir(refs_dir_path) if os.path.isfile(os.path.join(refs_dir_path, f))]

            # Extract triggers from frontmatter or description
            triggers = frontmatter.get("triggers", [])
            if not triggers:
                # Look for triggers in description like `/name`, "keyword"
                found_cmds = re.findall(r"(/[a-zA-Z0-9_\-]+)", description)
                found_quotes = re.findall(r"[\"']([^\"']+)[\"']", description)
                triggers = list(dict.fromkeys(found_cmds + found_quotes))

            return SkillMetadata(
                name=name,
                description=description,
                path=skill_dir,
                source=source,
                triggers=triggers,
                parameters=frontmatter.get("parameters", {}),
                scripts=scripts,
                templates=templates,
                references=references,
                body=body,
                raw_content=content,
            )
        except Exception as e:
            print(f"[SkillScanner] Failed parsing {skill_file}: {e}")
            return None

    def get_skill(self, name: str) -> Optional[SkillMetadata]:
        if not self.skills:
            self.scan()
        return self.skills.get(name)

    def search_skills(self, query: str) -> List[SkillMetadata]:
        if not self.skills:
            self.scan()

        q = query.lower()
        results = []
        for skill in self.skills.values():
            score = 0
            if q in skill.name.lower():
                score += 10
            if q in skill.description.lower():
                score += 5
            for tr in skill.triggers:
                if q in tr.lower():
                    score += 8
            if score > 0:
                results.append((score, skill))

        results.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in results]
