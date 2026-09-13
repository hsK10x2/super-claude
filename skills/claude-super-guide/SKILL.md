---
name: claude-super-guide
description: Use when looking for guidance on how to choose, combine, or use SuperClaude skills, slash commands, and specialist agents, or when explaining the toolkit to new users and team members
---

# SuperClaude Guide: Practical Manual

SuperClaude의 모든 슬래시 명령어, 전문 AI 에이전트, 워크플로우 스킬을 쉽게 이해하고 실무에서 즉시 활용할 수 있도록 정리한 실전 가이드입니다.

---

## 1. 프레임워크 한눈에 보기

SuperClaude는 크게 3가지 계층으로 동작합니다:

1. **슬래시 명령어 (`/super-claude:*`)**: 사용자가 터미널에서 직접 실행하는 명시적 작업 단위
2. **전문 AI 에이전트 (`@agent-name`)**: 아키텍트, 보안 담당자, PM 등 특정 시각과 전문성을 가진 페르소나
3. **워크플로우 스킬 (`skills/`)**: 개발 라이프사이클의 품질과 안전성을 강제하는 세부 실행 프로토콜

---

## 2. 상황별 추천 워크플로우

어떤 명령어를 먼저 써야 할지 고민될 때 아래 4가지 시나리오를 참고하세요.

### 시나리오 A: 새로운 기능을 기획하고 구현할 때
기능을 무작정 코딩하기보다 체계적으로 설계하고 검증하는 흐름입니다.

1. **요구사항 구체화**: `/super-claude:brainstorm "결제 및 환불 API 설계"`
   - 사용자 의도, 엣지 케이스, 숨은 제약조건을 질문을 통해 먼저 도출합니다.
2. **아키텍처 및 스키마 설계**: `/super-claude:design "환불 트랜잭션 모델링"`
   - `@backend-architect`나 `@system-architect`를 활용해 데이터베이스 구조와 인터페이스를 정의합니다.
3. **테스트 주도 구현**: `/super-claude:implement "PG사 결제 취소 연동"`
   - `test-driven-development` 스킬에 따라 실패하는 테스트 코드를 먼저 작성한 뒤 최소한의 구현을 진행합니다.
4. **완료 전 검증**: `/super-claude:test`
   - 실제 단위/통합 테스트를 구동하여 성공 여부를 확인합니다.
5. **커밋 및 PR 생성**: `/super-claude:git` (또는 `/commit-and-pr`)
   - Conventional Commits 형식의 커밋 메시지를 자동 생성하고 GitHub PR을 오픈합니다.

### 시나리오 B: 원인을 알 수 없는 복잡한 버그를 해결할 때
추측에 의존해 코드를 이것저것 고치는 실수를 방지합니다.

1. **오류 격리 및 진단**: `/super-claude:troubleshoot "결제 시 간헐적 504 게이트웨이 타임아웃"`
   - `@root-cause-analyst`가 로그, 스택 트레이스, 네트워크 지연 요인을 분석합니다.
2. **원인 입증 (`systematic-debugging`)**:
   - 버그를 재현하는 최소 테스트 코드를 먼저 작성하여 실제 원인을 과학적으로 확인합니다.
3. **수정 및 사이드이펙트 점검**:
   - 최소한의 코드 수정 후 기존 회귀 테스트를 실행합니다.

### 시나리오 C: 기술 스택을 검토하거나 라이브러리를 비교할 때
최신 자료와 신뢰할 수 있는 출처를 바탕으로 기술 의사결정을 내립니다.

1. **심층 기술 조사**: `/super-claude:research "FastAPI vs Go Gin 처리량 벤치마크 및 프로덕션 사례"`
   - 병렬 검색을 통해 공식 문서, 벤치마크 리포트, 기술 블로그를 교차 검증합니다.
2. **비즈니스 영향도 분석**: `/super-claude:business-panel`
   - 도입 비용, 팀의 학습 곡선, 유지보수 리스크를 종합 평가합니다.

### 시나리오 D: 기존 코드를 공부하거나 유지보수 문서를 만들 때
복잡한 레거시 코드를 빠르게 파악하고 신규 팀원을 온보딩시킵니다.

1. **저장소 구조 파악**: `/super-claude:index-repo`
   - 전체 리포지토리의 진입점과 모듈 의존성을 한 번에 인덱싱합니다.
2. **학습용 코드 설명서 작성**: `explain-code` 스킬 실행
   - `이 코드 설명해줘` 또는 `/explain-code`를 입력하면 주니어 개발자가 스스로 유지보수할 수 있는 상세한 `.explain.md` 문서를 생성합니다.

---

## 3. 핵심 슬래시 명령어 총람

| 분류 | 명령어 | 언제 쓰는가? | 실제 입력 예시 |
| :--- | :--- | :--- | :--- |
| **안내** | `/super-claude` | 전체 기능 메뉴와 현재 상태를 확인하고 싶을 때 | `/super-claude` |
| **추천** | `/super-claude:recommend` | 지금 상황에서 무엇을 해야 할지 조언이 필요할 때 | `/super-claude:recommend` |
| **기획** | `/super-claude:brainstorm` | 새로운 기능의 요구사항과 예외 처리를 명확히 할 때 | `/super-claude:brainstorm 알림 센터 기능` |
| **설계** | `/super-claude:design` | 데이터 모델, API 엔드포인트, 서비스 구조를 짤 때 | `/super-claude:design Redis 캐시 계층` |
| **조사** | `/super-claude:research` | 최신 기술 트렌드나 공식 문서를 깊이 있게 찾아볼 때 | `/super-claude:research OAuth2 PKCE 흐름` |
| **구현** | `/super-claude:implement` | 스펙에 맞춰 단계별로 안전하게 코드를 짤 때 | `/super-claude:implement 소셜 로그인 연동` |
| **테스트** | `/super-claude:test` | 테스트를 실행하고 실패한 이유를 분석할 때 | `/super-claude:test tests/unit` |
| **디버깅** | `/super-claude:troubleshoot` | 오류 로그나 장애 원인을 규명하고 고칠 때 | `/super-claude:troubleshoot 메모리 누수` |
| **정리** | `/super-claude:cleanup` | 쓰이지 않는 코드나 임시 파일을 정리할 때 | `/super-claude:cleanup` |
| **인덱싱** | `/super-claude:index-repo` | 큰 프로젝트의 토큰 사용량을 아끼며 파악할 때 | `/super-claude:index-repo` |
| **동기화** | `/super-claude:skill-update` | 설치된 스킬과 명령어를 최신 상태로 갱신할 때 | `/super-claude:skill-update` |
| **Git** | `/super-claude:git` | 의미 있는 커밋 메시지를 자동 생성할 때 | `/super-claude:git` |

---

## 4. 전문 에이전트 활용법 (`/super-claude:agent [이름]`)

특정 분야의 전문적인 검토가 필요할 때 해당 에이전트를 불러와 상담하거나 작업을 맡길 수 있습니다.

```text
> /super-claude:agent system-architect
> /super-claude:agent security-engineer
> /super-claude:agent pm-agent
```

### 추천 에이전트 역할:
- `@pm-agent`: 사용자 관점에서 기능 명세서(PRD)를 다듬고 우선순위를 정할 때
- `@system-architect`: 트래픽 증가나 서비스 분리 등 구조적 큰 그림을 그릴 때
- `@security-engineer`: 토큰 저장, 사용자 입력 검증, 권한 체크 등 보안 점검 시
- `@performance-engineer`: 응답 속도 개선, 쿼리 최적화, CPU/메모리 부하 해결 시
- `@root-cause-analyst`: 복잡한 재현 불가 버그나 예외를 집요하게 파고들 때
- `@refactoring-expert`: 지저분한 코드를 클린 코드 원칙에 맞게 리팩토링할 때

---

## 5. 자주 묻는 질문 및 팁

### Q1. 일반적인 질문을 할 때도 명령어를 꼭 써야 하나요?
아닙니다. 평소처럼 자연어로 대화하셔도 되며, 보다 체계적이고 깊이 있는 결과를 원할 때 해당 명령어나 에이전트를 부르시면 됩니다.

### Q2. 스킬이 최신 상태인지 어떻게 확인하나요?
터미널에서 `/super-claude:skill-update`를 실행하시면 로컬 `~/.claude/` 경로의 파일들을 검사하여 최신 상태로 맞춰줍니다.

### Q3. 명령어가 너무 많아 외우기 힘들어요.
처음에는 딱 세 가지만 기억하세요:
1. 시작할 때: `/super-claude` (대시보드)
2. 무엇을 할지 모를 때: `/super-claude:recommend` (작업 추천)
3. 구현할 때: `/super-claude:brainstorm` ➡️ `/super-claude:implement`
