"""Grill-me specialized interactive assistant and log generator."""

import os
import re
import datetime
from typing import Dict, List, Optional, Any

LENSES = {
    "first_principles": {
        "name": "First-Principles (근본 원리)",
        "probe": "기존 도구나 선입견 없이 완전히 제로(0)에서 시작한다면, 여전히 이 방식으로 설계/결정하시겠습니까?",
        "default_strawman": "기존 익숙한 관성 때문에 이 방식을 택했을 가능성이 높습니다. 가장 본질적인 최소 구성요소만 남긴다면 달라질 수 있습니다."
    },
    "intent_outcome": {
        "name": "Intent and Outcome (진정한 의도와 최종 목표)",
        "probe": "프로젝트의 표면적 스펙 외에, 본인이 생각하는 진정한 '성공'의 모습은 무엇인가요?",
        "default_strawman": "단순히 기능 구현 완료가 아니라, 운영 비용 최소화 또는 확장성 확보가 핵심일 수 있습니다."
    },
    "constraints": {
        "name": "Constraint Surfacing (핵심 제약조건 발굴)",
        "probe": "타협할 수 없는 절대적 제약조건(시간, 예산, 기술 스택 호환성, 리소스)은 구체적으로 무엇인가요?",
        "default_strawman": "마감 일정과 기존 레거시 시스템 호환성이 가장 큰 병목일 가능성이 큽니다."
    },
    "hidden_assumptions": {
        "name": "Hidden Assumptions (숨은 전제 검증)",
        "probe": "이 계획이 정상 작동하기 위해 '반드시 사실이어야만 하는' 암묵적 가정은 무엇인가요?",
        "default_strawman": "사용자나 연동 시스템이 항상 기대한 데이터 포맷과 속도로 응답할 것이라고 가정하고 있을 수 있습니다."
    },
    "second_best": {
        "name": "Second-Best Alternative (차선책 검증)",
        "probe": "지금 선택하지 않은 차선책(2순위 대안)은 무엇이며, 왜 그것을 탈락시켰나요?",
        "default_strawman": "대안이 명확히 떠오르지 않는다면, 아직 실제 선택을 한 것이 아니라 첫 번째로 떠오른 아이디어를 그대로 밀고 나가는 것일 수 있습니다."
    },
    "pre_mortem": {
        "name": "Pre-Mortem (사전 부검)",
        "probe": "지금으로부터 12개월 뒤, 이 계획이 완전히 실패했다고 가정해 봅시다. 가장 결정적인 실패 원인은 무엇이었을까요?",
        "default_strawman": "설계 복잡성 과다로 인한 유지보수 불가 또는 비정상 엣지 케이스 누락이 실패 원인일 확률이 높습니다."
    },
    "steelman_opposite": {
        "name": "Steelman the Opposite (반대 논리 강화)",
        "probe": "이 계획의 반대편 입장에서 제시할 수 있는 가장 강력한 반박 논리는 무엇인가요?",
        "default_strawman": "지금 단계에서는 너무 오버엔지니어링(Over-engineering)이며, 훨씬 단순한 방식으로도 충분하다는 반론이 가장 강력합니다."
    },
    "boundary_testing": {
        "name": "Boundary Testing (스코프 경계 설정)",
        "probe": "이번 작업에서 '절대 하지 않기로' 명확히 선을 그은 범위(Out of Scope)는 무엇인가요?",
        "default_strawman": "경계를 닫지 않으면 기능이 계속 불어나 마감이 무기한 지연될 수 있습니다. 부가 기능이나 고급 최적화는 1차 범위에서 제외해야 합니다."
    },
    "reversibility": {
        "name": "Reversibility (되돌릴 수 있는 문인가?)",
        "probe": "이 결정은 되돌리기 쉬운 '양방향 문(Two-way door)'인가요, 아니면 되돌리기 극도로 힘든 '일방향 문(One-way door)'인가요?",
        "default_strawman": "데이터 스키마나 공용 인터페이스 변경이라면 일방향 문에 가까우므로 지금 더 엄격하게 검증해야 합니다."
    }
}

class GrillSessionManager:
    """Manages grill-me interrogation sessions and session logs."""

    def __init__(self):
        self._sessions: Dict[str, Dict[str, Any]] = {}

    def start_session(self, topic: str, domain: str = "coding", lens: Optional[str] = None) -> Dict[str, Any]:
        session_id = f"grill_{re.sub(r'[^a-zA-Z0-9]', '_', topic.lower())[:20]}_{datetime.datetime.now().strftime('%H%M%S')}"
        chosen_lens_key = lens if lens in LENSES else "constraints" if "설계" in topic or "개발" in topic else "first_principles"
        lens_data = LENSES[chosen_lens_key]

        session = {
            "session_id": session_id,
            "topic": topic,
            "domain": domain,
            "question_count": 1,
            "current_lens": chosen_lens_key,
            "qa_history": [],
            "status": "in_progress"
        }
        self._sessions[session_id] = session

        question = f"[{lens_data['name']}] '{topic}'을(를) 구체화하기 위해 먼저 묻습니다:\n{lens_data['probe']}"
        recommended_answer = f"추천/기준 답변 (Strawman): {lens_data['default_strawman']}"

        return {
            "session_id": session_id,
            "topic": topic,
            "domain": domain,
            "question_number": 1,
            "lens": lens_data["name"],
            "question": question,
            "recommended_answer": recommended_answer,
            "guidance": "사용자의 답변을 받은 후 한 걸음 더 깊게 파고들거나(drill-down), 다른 렌즈(pre-mortem, boundary_testing 등)로 검증을 이어가세요."
        }

    def next_question(self, session_id: str, previous_answer: str, next_lens: Optional[str] = None) -> Dict[str, Any]:
        session = self._sessions.get(session_id)
        if not session:
            # Create ad-hoc session if not present
            session_id = f"grill_adhoc_{datetime.datetime.now().strftime('%H%M%S')}"
            session = {
                "session_id": session_id,
                "topic": "System Discussion",
                "domain": "coding",
                "question_count": 1,
                "current_lens": "hidden_assumptions",
                "qa_history": [],
                "status": "in_progress"
            }
            self._sessions[session_id] = session

        session["qa_history"].append({
            "question_number": session["question_count"],
            "lens": session["current_lens"],
            "answer": previous_answer
        })
        session["question_count"] += 1

        # Select next lens
        available_lenses = [k for k in LENSES.keys() if k != session["current_lens"]]
        chosen_lens_key = next_lens if next_lens in LENSES else available_lenses[(session["question_count"] - 2) % len(available_lenses)]
        lens_data = LENSES[chosen_lens_key]
        session["current_lens"] = chosen_lens_key

        # Detect vague answers
        is_vague = any(w in previous_answer for w in ["아마", "나중에", "대충", "글쎄", "몰라", "maybe", "probably", "later"])
        prefix = "⚠️ 이전 답변에서 불확실하거나 모호한 부분이 감지되었습니다. 더 구체적인 기준이 필요합니다.\n" if is_vague else ""

        question = f"{prefix}[{lens_data['name']}] 질문 {session['question_count']}:\n{lens_data['probe']}"
        recommended_answer = f"추천/기준 답변 (Strawman): {lens_data['default_strawman']}"

        return {
            "session_id": session_id,
            "question_number": session["question_count"],
            "lens": lens_data["name"],
            "question": question,
            "recommended_answer": recommended_answer,
            "ready_to_finalize": session["question_count"] >= 4,
            "guidance": "최소 3~4개의 렌즈 질문이 완료되고 명확한 실행 계획이 수립되면 log_session을 호출하여 .grill/<slug>.md 요약 로그를 저장하세요."
        }

    def save_log(
        self,
        topic: str,
        intent: str,
        constraints: Optional[List[str]] = None,
        key_decisions: Optional[List[Dict[str, str]]] = None,
        surfaced_assumptions: Optional[List[str]] = None,
        open_questions: Optional[List[str]] = None,
        out_of_scope: Optional[List[str]] = None,
        target_dir: Optional[str] = None
    ) -> Dict[str, Any]:
        """Save distilled session markdown log to <target_dir>/.grill/<slug>.md."""
        slug = re.sub(r"[^a-zA-Z0-9가-힣_\-]+", "-", topic.strip().lower()).strip("-") or "session"
        base_dir = os.path.abspath(target_dir or os.getcwd())
        grill_dir = os.path.join(base_dir, ".grill")
        os.makedirs(grill_dir, exist_ok=True)
        log_file = os.path.join(grill_dir, f"{slug}.md")

        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        lines = [
            f"# Grill: {topic}",
            f"Date: {now_str}\n",
            "## Intent",
            f"{intent.strip()}\n"
        ]

        if constraints:
            lines.append("## Constraints")
            for c in constraints:
                lines.append(f"- {c}")
            lines.append("")

        if key_decisions:
            lines.append("## Key decisions")
            for d in key_decisions:
                decision = d.get("decision", "")
                reason = d.get("reason", "")
                alt = d.get("alternative", "")
                lines.append(f"- **결정**: {decision} | **이유**: {reason}" + (f" | **검토 대안**: {alt}" if alt else ""))
            lines.append("")

        if surfaced_assumptions:
            lines.append("## Surfaced assumptions")
            for a in surfaced_assumptions:
                lines.append(f"- {a}")
            lines.append("")

        if open_questions:
            lines.append("## Open questions")
            for q in open_questions:
                lines.append(f"- {q}")
            lines.append("")

        if out_of_scope:
            lines.append("## Out of scope")
            for o in out_of_scope:
                lines.append(f"- {o}")
            lines.append("")

        content = "\n".join(lines)
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(content)

        return {
            "status": "success",
            "log_path": log_file,
            "topic": topic,
            "content_preview": content[:300] + "..." if len(content) > 300 else content
        }
