# 🚀 SuperClaude for Claude Code

<p align="center">
  <b>Claude Code를 위한 완벽한 엔지니어링 스킬 & 슬래시 명령어 & 전문 AI 에이전트 통합 프레임워크</b>
</p>

---

## 🌟 개요 (Overview)

**SuperClaude**는 [Claude Code](https://docs.claude.com/en/docs/claude-code)의 역량을 극대화하여 전문 소프트웨어 엔지니어링 플랫폼으로 전환해주는 올인원 프레임워크입니다.

- ⚡ **30개의 직관적인 슬래시 명령어** (`/super-claude:*`)
- 🤖 **21명의 도메인 특화 전문 AI 에이전트** (`@pm-agent`, `@system-architect` 등)
- 🧠 **29개의 워크플로우 전문 스킬** (브레인스토밍, 딥 리서치, 디버깅, TDD, 코드 리뷰 등)
- 🛠️ **원클릭 자동 설치 스크립트** (Windows PowerShell / macOS / Linux 지원)

---

## ⚡ 빠른 설치 (Quick Install)

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

설치 후 `claude`를 실행하면 즉시 모든 명령어와 에이전트, 스킬을 사용할 수 있습니다.

---

## 🎮 슬래시 명령어 (`/super-claude:*`)

| 명령어 | 설명 | 예시 |
| :--- | :--- | :--- |
| **`/super-claude`** | **SuperClaude 메인 대시보드 및 가이드 호출** | `/super-claude` |
| **`/super-claude:recommend`** | 현재 프로젝트 맥락에 알맞은 작업 추천 | `/super-claude:recommend` |
| **`/super-claude:research`** | 병렬 웹 검색 기반 심층 연구 및 사실 검증 | `/super-claude:research LLM agent patterns` |
| **`/super-claude:brainstorm`** | 요구사항 발굴 및 아키텍처 기획 브레인스토밍 | `/super-claude:brainstorm CRM 기능 설계` |
| **`/super-claude:design`** | 시스템 아키텍처 및 API 명세 설계 | `/super-claude:design auth-service` |
| **`/super-claude:implement`** | 구조화된 단계별 코드 구현 워크플로우 | `/super-claude:implement user-login` |
| **`/super-claude:test`** | 테스트 실행, 커버리지 검증 및 실패 분석 | `/super-claude:test` |
| **`/super-claude:troubleshoot`** | 체계적 원인 규명 및 버그 디버깅 | `/super-claude:troubleshoot memory leak` |
| **`/super-claude:index-repo`** | 리포지토리 컨텍스트 인덱싱 (토큰 최적화) | `/super-claude:index-repo` |
| **`/super-claude:analyze`** | 코드베이스 종합 분석 (품질, 보안, 성능) | `/super-claude:analyze src/` |
| **`/super-claude:cleanup`** | 미사용 코드 제거 및 구조 정리 | `/super-claude:cleanup` |
| **`/super-claude:git`** | 스마트 커밋 메시지 및 Git 작업 자동화 | `/super-claude:git` |
| **`/super-claude:task`** | 태스크 상태 추적 및 마일스톤 관리 | `/super-claude:task` |
| **`/super-claude:workflow`** | 다단계 엔지니어링 워크플로우 조율 | `/super-claude:workflow` |
| **`/super-claude:agent`** | 전문 AI 에이전트 직접 호출 | `/super-claude:agent pm-agent` |

---

## 🤖 전문 AI 에이전트 (`agents/`)

Claude Code에서 특정 역할로 집중하여 문제를 해결하는 전문 에이전트 목록입니다:

| 에이전트 | 전문 분야 |
| :--- | :--- |
| `@pm-agent` | 프로덕트 매니저: 요구사항 정의, 범위 산정, 백로그 우선순위 |
| `@system-architect` | 시스템 아키텍트: 고수준 시스템 설계, 데이터 파이프라인, 모듈 경계 |
| `@backend-architect` | 백엔드 아키텍트: API 설계, 데이터베이스 스키마, 비즈니스 로직 |
| `@frontend-architect` | 프론트엔드 아키텍트: UI/UX 구조, 컴포넌트 설계, 상태 관리 |
| `@deep-research-agent`| 딥 리서치 에이전트: 다각도 기술 조사, 벤치마크, 레퍼런스 분석 |
| `@security-engineer` | 보안 엔지니어: 취약점 분석, 인증/인가 점검, 보안 하드닝 |
| `@performance-engineer`| 성능 엔지니어: 프로파일링, 병목 식별, 메모리/CPU 최적화 |
| `@root-cause-analyst` | 근본 원인 분석가: 복잡한 버그 추적, 오류 로그 심층 분석 |
| `@quality-engineer` | 품질 보증 엔지니어: E2E 테스트, 엣지 케이스 점검, QA 검증 |
| `@refactoring-expert` | 리팩토링 전문가: 코드 스멜 제거, 기술 부채 해소, 클린 코드 |
| `@devops-architect` | 데브옵스 아키텍트: CI/CD, 컨테이너화, 배포 파이프라인 |
| `@technical-writer` | 테크니컬 라이터: 고품질 API 문서, 아키텍처 다이어그램, 가이드 |

---

## 🧠 탑재된 스킬 라이브러리 (`skills/`)

29개의 엄선된 전문 워크플로우 스킬이 포함되어 있습니다:

- `architecture-design`: 대규모 시스템 및 API 설계
- `brainstorming`: 창의적 기능 기획 및 의도 구체화
- `browser-agent`: 웹 브라우저 자동화 및 UI 테스팅
- `commit-and-pr`: Conventional Commits 메시지 자동 작성 및 PR 생성
- `confidence-check`: 구현 전 사전 맥락 확인 및 리스크 예방
- `deep-research`: 심층 웹 검색 및 사실 검증
- `explain-code`: 학습 및 유지보수를 위한 고밀도 설명서 생성
- `grill-me`: 집요한 질문을 통한 기획/제약조건 명확화
- `how-many-tokens-left`: 세션 컨텍스트 토큰 사용량 측정 및 예산 관리
- `systematic-debugging`: 증명 기반 단계별 디버깅
- `test-driven-development`: 테스트 주도 개발(TDD) 워크플로우
- `using-superclaude`: 세션 시작 시 스킬 자동 탐색 프로토콜
- `verification-before-completion`: 완료 주장 전 증거 검증 강제

---

## 📁 디렉터리 구조

```
super-claude/
├── commands/
│   ├── super-claude.md           # 메인 디스패처 (/super-claude)
│   └── super-claude/             # 29개 하위 명령어 (/super-claude:*)
├── agents/                       # 21개 전문 AI 에이전트
├── skills/                       # 29개 워크플로우 스킬 라이브러리
├── install.ps1                   # Windows 설치 스크립트
├── install.sh                    # macOS / Linux 설치 스크립트
├── .gitignore
└── README.md
```

---

## 📄 라이선스 (License)

MIT License
