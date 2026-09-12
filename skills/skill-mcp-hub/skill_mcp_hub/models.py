"""Data models for skills representation in Skill MCP Hub."""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class SkillMetadata:
    name: str
    description: str
    path: str
    source: str  # e.g., 'claude', 'gemini', 'workspace', 'custom'
    triggers: List[str] = field(default_factory=list)
    parameters: Dict[str, Any] = field(default_factory=dict)
    scripts: List[str] = field(default_factory=list)
    templates: List[str] = field(default_factory=list)
    references: List[str] = field(default_factory=list)
    body: str = ""
    raw_content: str = ""

    def to_summary_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "source": self.source,
            "triggers": self.triggers,
            "has_scripts": len(self.scripts) > 0,
            "scripts": self.scripts,
            "templates": self.templates,
            "references": self.references,
            "path": self.path,
        }

    def to_full_dict(self) -> Dict[str, Any]:
        d = self.to_summary_dict()
        d["body"] = self.body
        d["parameters"] = self.parameters
        return d
