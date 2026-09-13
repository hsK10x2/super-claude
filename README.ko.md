# SuperClaude

<p>
  <a href="./README.md">English</a> | <b>한국어</b>
</p>

> Claude Code를 위한 체계적인 엔지니어링 툴킷, 전문 AI 에이전트 및 워크플로우 스킬 모음.

SuperClaude는 [Claude Code](https://docs.claude.com/en/docs/claude-code)를 전문 소프트웨어 엔지니어링 플랫폼으로 확장해주는 프레임워크입니다. 구조화된 슬래시 명령어 디스패처, 도메인별 특화 에이전트, 그리고 요구사항 분석부터 딥 리서치, 테스트 주도 개발(TDD), 코드 리뷰까지 포괄하는 고밀도 워크플로우 스킬 라이브러리를 제공합니다.

---

## 핵심 기능

- **31개 슬래시 명령어**: 반복적인 개발 작업을 표준화한 `/super-claude:*` 네임스페이스 명령어 제공
- **21명 도메인 특화 에이전트**: 아키텍처 설계, 보안 감사, 근본 원인 분석, 성능 프로파일링 등 맥락에 최적화된 페르소나
- **31종 워크플로우 스킬**: TDD, 체계적 디버깅, 토큰 예산 관리 및 누구나 쉽게 배우는 `claude-super-guide` 탑재
- **초심자/팀원 친화적 실전 가이드**: `/claude-super-guide`로 4가지 실전 시나리오와 명령어 총람 상시 조회 가능
- **자동 스킬 동기화 도구**: 로컬 설치본과 Git 저장소 간의 상태를 감사하고 갱신하는 `/super-claude:skill-update` 탑재
- **원클릭 설치 지원**: `~/.claude/` 경로에 자동 배치되는 Windows PowerShell 및 Bash 스크립트 제공

---

## 설치 방법

저장소를 클론한 후 사용 중인 운영체제에 맞는 설치 스크립트를 실행합니다. 스크립트가 모든 명령어, 에이전트, 스킬을 사용자의 전역 `~/.claude/` 디렉터리에 자동으로 등록합니다.

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

설치가 완료되면 터미널에서 `claude` 세션을 시작하여 바로 사용할 수 있습니다.

---

## 빠른 시작

프로젝트 디렉터리에서 Claude Code를 실행합니다:

```bash
claude
```

대화창에 `/claude-super-guide`를 입력하여 실전 가이드를 읽거나, 필요한 작업을 직접 호출합니다:

```text
> /claude-super-guide
> /super-claude:recommend
> /super-claude:brainstorm "인증 및 세션 아키텍처 설계"
> /super-claude:research "마이크로서비스 간 무상태 통신 패턴 및 벤치마크"
> /super-claude:implement "Redis 기반 토큰 무효화 엔드포인트 구현"
```

---

## 명령어 레퍼런스

기존 프로젝트의 자체 커스텀 명령어와의 충돌을 방지하기 위해 모든 명령어가 `/super-claude:` 네임스페이스로 격리되어 있습니다.

### 안내 및 도구 관리 (Guidance and Tooling)

| 명령어 | 설명 | 사용 예시 |
| :--- | :--- | :--- |
| `/super-claude` | 프레임워크 메인 대시보드 및 명령어 색인 호출 | `/super-claude` |
| `/claude-super-guide` | 초심자 및 팀원을 위한 상황별 실전 활용 매뉴얼 | `/claude-super-guide` |
| `/super-claude:recommend` | Git 상태 및 프로젝트 맥락에 따른 다음 권장 작업 제안 | `/super-claude:recommend` |
| `/super-claude:skill-update` | 로컬에 설치된 스킬/명령어를 저장소와 동기화 및 감사 | `/super-claude:skill-update` |
| `/super-claude:index-repo` | 컨텍스트 토큰 최적화를 위한 저장소 구조 인덱싱 | `/super-claude:index-repo` |

### 리서치 및 분석 (Research and Analysis)

| 명령어 | 설명 | 사용 예시 |
| :--- | :--- | :--- |
| `/super-claude:research` | 다중 소스 병렬 웹 검색 및 사실 검증 기반 심층 리서치 | `/super-claude:research LLM agent patterns` |
| `/super-claude:analyze` | 코드 품질, 보안 경계 및 성능 병목 종합 분석 | `/super-claude:analyze src/` |
| `/super-claude:spec-panel` | 다각도 관점에서의 기술 명세 및 요구사항 검토 | `/super-claude:spec-panel` |
| `/super-claude:business-panel` | 비즈니스 실현 가능성, 위험 요인 및 제품 가치 분석 | `/super-claude:business-panel` |

### 기획 및 설계 (Planning and Architecture)

| 명령어 | 설명 | 사용 예시 |
| :--- | :--- | :--- |
| `/super-claude:brainstorm` | 대화형 요구사항 발굴 및 아키텍처 설계 브레인스토밍 | `/super-claude:brainstorm billing service` |
| `/super-claude:design` | 시스템 아키텍처, 컴포넌트 경계 및 API 명세 설계 | `/super-claude:design event-bus` |
| `/super-claude:estimate` | 작업 복잡도 산정, 리스크 식별 및 개발 일정 추정 | `/super-claude:estimate migration-task` |

### 개발 및 품질 보증 (Implementation and Quality Assurance)

| 명령어 | 설명 | 사용 예시 |
| :--- | :--- | :--- |
| `/super-claude:implement` | 단계별 구조화된 기능 구현 워크플로우 실행 | `/super-claude:implement user-login` |
| `/super-claude:test` | 단위/통합 테스트 실행, 커버리지 점검 및 실패 분석 | `/super-claude:test tests/unit` |
| `/super-claude:troubleshoot` | 로그 기반 원인 격리, 스택 트레이스 분석 및 수정안 도출 | `/super-claude:troubleshoot memory-spike` |
| `/super-claude:cleanup` | 미사용 사장 코드(Dead Code) 제거 및 디렉터리 구조 정돈 | `/super-claude:cleanup` |
| `/super-claude:improve` | 대상 코드의 가독성 및 유지보수성 리팩토링 | `/super-claude:improve src/auth.py` |

### 저장소 및 워크플로우 (Repository and Workflow)

| 명령어 | 설명 | 사용 예시 |
| :--- | :--- | :--- |
| `/super-claude:git` | Conventional Commits 규격 커밋 메시지 작성 및 Git 작업 지원 | `/super-claude:git` |
| `/super-claude:task` | 태스크 세분화, 의존성 매핑 및 마일스톤 추적 | `/super-claude:task` |
| `/super-claude:workflow` | 다단계 복합 엔지니어링 파이프라인 조율 | `/super-claude:workflow` |
| `/super-claude:agent` | 특정 분야 전문 AI 에이전트 직접 호출 | `/super-claude:agent pm-agent` |

---

## 전문 AI 에이전트 목록

복잡한 개발 과정에서 역할을 세분화하여 위임할 수 있는 21명의 전문 에이전트 페르소나가 `agents/`에 정의되어 있습니다:

| 에이전트 | 주요 담당 영역 |
| :--- | :--- |
| `@system-architect` | 분산 시스템 아키텍처, 서비스 경계 정의, 확장성 및 가용성 설계 |
| `@backend-architect` | API 계약 설계, 데이터 모델링, 영속성 계층 및 서비스 로직 |
| `@frontend-architect` | UI 컴포넌트 계층 구조, 클라이언트 상태 관리 및 프론트엔드 성능 |
| `@security-engineer` | 위협 모델링, 취약점 진단, 인증/인가 체계 및 암호화 표준 준수 |
| `@performance-engineer` | 응답 지연 시간 프로파일링, 메모리 누수 분석 및 리소스 최적화 |
| `@pm-agent` | 제품 요구사항 정의서(PRD), 사용자 스토리 도출 및 백로그 우선순위 |
| `@root-cause-analyst` | 복합 장애 심층 분석, 로그 상관관계 추적 및 재발 방지책 수립 |
| `@quality-engineer` | 통합 테스트 전략 수립, 엣지 케이스 시나리오 도출 및 QA 검증 |
| `@refactoring-expert` | 기술 부채 해소, 코드 스멜 제거 및 클린 아키텍처 유지 |
| `@devops-architect` | CI/CD 파이프라인 구성, 컨테이너화 및 안전한 배포 전략 수립 |
| `@deep-research-agent` | 기술 문헌 심층 조사, 오픈소스 벤치마크 및 비교 분석 보고서 작성 |
| `@technical-writer` | 개발자 친화적 API 레퍼런스, 아키텍처 결정 기록(ADR) 문서화 |

---

## 워크플로우 스킬 라이브러리

`skills/` 디렉터리는 오픈 Agent Skill 규격(`SKILL.md`)을 준수하는 모듈형 스킬을 포함합니다:

- `claude-super-guide`: 초심자 친화적 실전 가이드, 4대 워크플로우 시나리오 및 치트시트
- `architecture-design`: 시스템 모델링, 아키텍처 트레이드오프 평가 및 경계 설계
- `brainstorming`: 소크라테스식 문답을 통한 기획 의도 구체화 및 전제 검증
- `browser-agent`: 웹 브라우저 기반 E2E 동작 테스트 및 UI 시각적 검증
- `commit-and-pr`: Conventional Commits 규격 준수 커밋 및 GitHub PR 초안 자동 작성
- `confidence-check`: 구현 착수 전 맥락 이해도 검증을 통한 무의미한 반복 작업 방지
- `deep-research`: 인용 출처 검증 기능을 갖춘 병렬 심층 리서치 엔진
- `explain-code`: 주니어 개발자 학습 및 신규 팀원 온보딩을 위한 고밀도 코드 해설서 작성
- `grill-me`: 집요한 질문 인터뷰를 통한 설계/요구사항 스트레스 테스트
- `how-many-tokens-left`: 세션 컨텍스트 토큰 소비량 측정 및 예산 관리
- `skill-update`: 설치된 Claude Code 자산의 무결성 검증, 동기화 및 레거시 파일 정리
- `systematic-debugging`: 결함 재현, 원인 격리, 증거 기반 단계별 디버깅 프로토콜
- `test-driven-development`: Red-Green-Refactor 사이클을 준수하는 TDD 프로토콜
- `using-superclaude`: 대화 시작 시 적합한 스킬 자동 탐색 및 로드 규칙
- `verification-before-completion`: 완료 선언 전 실제 실행 증거 확보를 강제하는 검증 절차

---

## 스킬 동기화 (`/super-claude:skill-update`)

저장소의 스킬이나 명령어가 수정되었거나 원격 저장소에서 pull을 받은 경우 다음 명령으로 로컬 환경을 즉시 동기화할 수 있습니다:

```bash
# Claude Code 대화창에서 실행 시
/super-claude:skill-update

# 터미널에서 Python 스크립트로 직접 실행 시
python skills/skill-update/scripts/sync_skills.py --clean
```

---

## 라이선스 (License)

MIT License. 자세한 내용은 [LICENSE](./LICENSE) 파일을 참고하세요.
