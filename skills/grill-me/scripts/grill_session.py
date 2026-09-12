# -*- coding: utf-8 -*-
"""grill-me helper script for managing interrogation sessions and auto-logging."""

import os
import sys
import argparse
import json
import re
import datetime

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

LENSES = {
    "first_principles": {
        "name": "First-Principles (근본 원리)",
        "probe": "기존 도구나 관행 없이 완전히 제로(0)에서 시작한다면, 여전히 이 방식으로 설계/접근하시겠습니까?",
        "strawman": "기존에 익숙한 패턴에 갇혀 있을 수 있습니다. 가장 본질적인 최소 구성요소만 남기면 구조가 달라집니다."
    },
    "constraints": {
        "name": "Constraint Surfacing (핵심 제약조건 발굴)",
        "probe": "타협할 수 없는 절대적 제약조건(시간, 기술 스택, 리소스, 호환성)은 구체적으로 무엇인가요?",
        "strawman": "마감 일정과 기존 레거시 시스템 호환성이 가장 큰 병목일 가능성이 큽니다."
    },
    "hidden_assumptions": {
        "name": "Hidden Assumptions (숨은 전제 검증)",
        "probe": "이 계획이 성공하기 위해 '반드시 사실이어야만 하는' 암묵적 가정은 무엇인가요?",
        "strawman": "연동 시스템이나 사용자가 항상 이상적인 상태로 작동할 것이라 가정하고 있을 수 있습니다."
    },
    "pre_mortem": {
        "name": "Pre-Mortem (사전 부검)",
        "probe": "12개월 뒤 이 계획이 완전히 실패했다고 가정할 때, 가장 결정적인 실패 원인은 무엇일까요?",
        "strawman": "설계 복잡성 과다로 인한 유지보수 불능 또는 예외 상황 누락이 실패 원인일 확률이 높습니다."
    },
    "steelman_opposite": {
        "name": "Steelman the Opposite (반대 논리 강화)",
        "probe": "이 계획에 대한 가장 강력하고 타당한 반론이나 대안 논리는 무엇인가요?",
        "strawman": "지금 단계에서는 오버엔지니어링이며, 더 단순한 대안으로도 충분하다는 주장이 가장 강력합니다."
    },
    "boundary_testing": {
        "name": "Boundary Testing (스코프 경계 설정)",
        "probe": "이번 작업에서 '절대 하지 않기로' 명확히 선을 그은 제외 범위(Out of Scope)는 무엇인가요?",
        "strawman": "경계를 닫지 않으면 기능이 비대해져 마감이 지연됩니다. 1차 버전에서는 부가 최적화를 제외해야 합니다."
    }
}

def cmd_start(args):
    topic = args.topic
    domain = args.domain or "coding"
    lens_key = args.lens if args.lens in LENSES else ("constraints" if domain == "coding" else "first_principles")
    lens = LENSES[lens_key]

    data = {
        "session_id": f"grill_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "topic": topic,
        "domain": domain,
        "lens": lens["name"],
        "question": f"[{lens['name']}] '{topic}'을(를) 구체화하기 위해 묻습니다:\n{lens['probe']}",
        "recommended_strawman": lens["strawman"]
    }
    print(json.dumps(data, ensure_ascii=False, indent=2))

def cmd_log(args):
    topic = args.topic
    intent = args.intent
    slug = re.sub(r"[^a-zA-Z0-9가-힣_-]+", "-", topic.strip().lower()).strip("-") or "session"
    out_dir = os.path.abspath(args.cwd or os.getcwd())
    grill_dir = os.path.join(out_dir, ".grill")
    os.makedirs(grill_dir, exist_ok=True)
    log_file = os.path.join(grill_dir, f"{slug}.md")

    lines = [
        f"# Grill: {topic}",
        f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        "## Intent",
        f"{intent.strip()}\n"
    ]

    if args.constraints:
        lines.append("## Constraints")
        for c in args.constraints:
            lines.append(f"- {c}")
        lines.append("")

    if args.decision:
        lines.append("## Key decisions")
        for d in args.decision:
            lines.append(f"- {d}")
        lines.append("")

    if args.assumptions:
        lines.append("## Surfaced assumptions")
        for a in args.assumptions:
            lines.append(f"- {a}")
        lines.append("")

    if args.open_questions:
        lines.append("## Open questions")
        for q in args.open_questions:
            lines.append(f"- {q}")
        lines.append("")

    if args.out_of_scope:
        lines.append("## Out of scope")
        for o in args.out_of_scope:
            lines.append(f"- {o}")
        lines.append("")

    content = "\n".join(lines)
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(json.dumps({"status": "success", "saved_path": log_file}, ensure_ascii=False, indent=2))

def main():
    parser = argparse.ArgumentParser(description="grill-me session manager")
    sub = parser.add_subparsers(dest="command")

    p_start = sub.add_parser("start")
    p_start.add_argument("--topic", required=True, help="Topic or decision to pressure-test")
    p_start.add_argument("--domain", default="coding", help="Domain (coding, business, etc.)")
    p_start.add_argument("--lens", default=None, help="Question lens")

    p_log = sub.add_parser("log")
    p_log.add_argument("--topic", required=True)
    p_log.add_argument("--intent", required=True)
    p_log.add_argument("--constraints", action="append")
    p_log.add_argument("--decision", action="append")
    p_log.add_argument("--assumptions", action="append")
    p_log.add_argument("--open-questions", action="append", dest="open_questions")
    p_log.add_argument("--out-of-scope", action="append", dest="out_of_scope")
    p_log.add_argument("--cwd", default=None)

    args = parser.parse_args()
    if args.command == "start":
        cmd_start(args)
    elif args.command == "log":
        cmd_log(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
