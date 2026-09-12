"""Unit and integration tests for Skill MCP Hub."""

import unittest
import os
import sys
import shutil

# Ensure skill_mcp_hub is in sys.path
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from skill_mcp_hub.scanner import SkillScanner
from skill_mcp_hub.server import (
    list_skills,
    get_skill,
    search_skills,
    read_skill_resource,
    execute_skill_script,
    grill_me_session,
    grill_me_prompt,
    explain_code_prompt,
)

class TestSkillMCPHub(unittest.TestCase):

    def setUp(self):
        self.scanner = SkillScanner()
        self.skills = self.scanner.scan()

    def test_scanner_discovery(self):
        self.assertGreater(len(self.skills), 5, "Should discover at least 5 skills")
        self.assertIn("grill-me", self.skills)
        self.assertIn("explain-code", self.skills)
        self.assertIn("commit-and-pr", self.skills)

    def test_list_skills(self):
        all_skills = list_skills()
        self.assertIsInstance(all_skills, list)
        self.assertGreaterEqual(len(all_skills), 5)

        # Filter by query
        filtered = list_skills(query="grill")
        self.assertTrue(any(s["name"] == "grill-me" for s in filtered))

    def test_get_skill(self):
        res = get_skill("grill-me")
        self.assertEqual(res["status"], "success")
        skill_data = res["skill"]
        self.assertEqual(skill_data["name"], "grill-me")
        self.assertTrue(len(skill_data["body"]) > 50)
        self.assertIn("grill_session.py", skill_data["scripts"])
        self.assertIn("grill_log_template.md", skill_data["templates"])

    def test_search_skills(self):
        results = search_skills("interview")
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]["name"], "grill-me")

    def test_read_skill_resource(self):
        res = read_skill_resource("grill-me", "templates/grill_log_template.md")
        self.assertEqual(res["status"], "success")
        self.assertIn("## Intent", res["content"])
        self.assertIn("## Constraints", res["content"])

        # Security check: path traversal
        traversal = read_skill_resource("grill-me", "../../secret.txt")
        self.assertEqual(traversal["status"], "error")

    def test_execute_skill_script(self):
        res = execute_skill_script(
            name="grill-me",
            script_name="grill_session.py",
            args=["start", "--topic", "Unit Test Topic", "--domain", "coding"]
        )
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["exit_code"], 0)
        self.assertIn("session_id", res["stdout"])
        self.assertIn("Unit Test Topic", res["stdout"])

    def test_grill_me_session_flow(self):
        # 1. Start session
        start_res = grill_me_session(
            action="start",
            topic="High Performance Cache Layer",
            domain="coding"
        )
        self.assertIn("session_id", start_res)
        self.assertIn("question", start_res)
        self.assertIn("recommended_answer", start_res)
        session_id = start_res["session_id"]

        # 2. Next question
        next_res = grill_me_session(
            action="next",
            session_id=session_id,
            previous_answer="Redis를 사용하고 TTL은 60초로 둘 예정입니다."
        )
        self.assertIn("question", next_res)
        self.assertIn("recommended_answer", next_res)

        # 3. Save log
        test_dir = os.path.join(repo_root, "scratch_test_grill")
        os.makedirs(test_dir, exist_ok=True)
        try:
            log_res = grill_me_session(
                action="save_log",
                topic="High Performance Cache Layer",
                intent="캐시 히트율을 95% 이상으로 유지하고 응답 속도를 5ms 이내로 단축",
                constraints=["메모리 사용량 최대 4GB", "데이터 유실 허용 안됨"],
                key_decisions=[
                    {
                        "decision": "Redis Cluster 도입",
                        "reason": "고가용성 및 샤딩 지원",
                        "alternative": "단일 인스턴스 + 복제"
                    }
                ],
                target_dir=test_dir
            )
            self.assertEqual(log_res["status"], "success")
            self.assertTrue(os.path.isfile(log_res["log_path"]))
            with open(log_res["log_path"], "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("High Performance Cache Layer", content)
            self.assertIn("Redis Cluster", content)
        finally:
            if os.path.exists(test_dir):
                shutil.rmtree(test_dir, ignore_errors=True)

    def test_prompts(self):
        p_grill = grill_me_prompt("MSA 전환")
        self.assertIn("MSA 전환", p_grill)
        self.assertIn("grill-me", p_grill)

        p_explain = explain_code_prompt("server.py")
        self.assertIn("server.py", p_explain)

if __name__ == "__main__":
    unittest.main()
