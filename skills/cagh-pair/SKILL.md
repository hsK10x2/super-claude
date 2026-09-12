---
name: cagh-pair
description: >-
  Claude(CEO & Hub)가 작업 특성과 양대 에이전트의 강점(Claude: 설계/추론, Antigravity: 구현/테스트)을 스스로 분석하여
  최적의 역할을 자율 분담하고, 불필요한 보일러플레이트를 배제하는 토큰 절약(Token-Efficient) 페어 프로그래밍을 실행합니다.
  "페어 프로그래밍 해줘", "Claude랑 협업해줘", "Antigravity랑 협업해줘", "CEO Claude한테 시켜줘", "둘이 알아서 역할 나눠서 짜줘",
  "토큰 아껴서 짜줘", "pair with claude", "pair with antigravity", 또는 /cagh-pair, /pair 호출 시 사용합니다.
---

# CAGH Autonomous Strength-Based & Token-Efficient Pairing

Claude가 대장(CEO & Central Hub)으로서 작업의 성격을 스스로 진단하고, **각자 가장 잘하는 영역으로 역할을 자율 분담**하여 토큰 소모를 최소화하면서 고밀도 결과물을 도출하는 하이어라키 오케스트레이션 스킬입니다.

---

## 🎯 강점 기반 자율 역할 분담 원칙 (Strength-Based Allocation)

| 에이전트 | 핵심 강점 (Specialty) | 주 담당 업무 (Assigned Scope) | 토큰 절약 행동 강령 |
| :--- | :--- | :--- | :--- |
| **👑 Claude (CEO & Hub)** | 심층 추론, 거시 아키텍처, 시스템 경계 설정, 보안/엣지케이스 설계 | • 아키텍처 청사진 수립<br/>• 인터페이스 규격 및 타입 계약 정의<br/>• 서브에이전트 최종 감사(Audit) & 승인 | 수백 줄의 반복 코드 직접 출력 금지. **타입 시그니처와 핵심 인터페이스 규격만 간결히 정의**하여 하달. |
| **🛠️ Antigravity (Subagent)** | 빠른 코드 생성, 파일 I/O 조작, 로컬 터미널/쉘 실행, 단위 테스트 자동화 | • 실제 소스 파일 작성/수정<br/>• 로컬 빌드 및 pytest 구동<br/>• 실행 결과 팩트 위주 요약 보고 | 장황한 이론 설명이나 사족 배제. **동작하는 코드와 테스트 결과 리포트만 고밀도로 작성**. |

---

## ⚡ 토큰 최적화 3단계 파이프라인 (3-Stage Token-Saving Pipeline)

```text
[사용자 작업 요청: /cagh-pair]
         │
         ▼
[Stage 1: 👑 CEO Claude 자율 역할 판단 & 인터페이스 계약]
  • 작업 분석 후 상단에 [역할 분담 선언] 명시:
    "Claude는 설계/규격을 맡고, Antigravity는 파일 구현/테스트를 맡는다."
  • 보일러플레이트 없이 필수 인터페이스 및 제약 조건만 컴팩트하게 하달
         │ (업무 지시 하달)
         ▼
[Stage 2: 🛠️ Subagent Antigravity 고밀도 구현 & 검증]
  • CEO Claude의 인터페이스 계약에 맞춰 실제 파일 작성
  • 로컬 터미널에서 단위 테스트 실행 및 검증
  • 불필요한 사족 없이 실제 수정 내역과 테스트 결과만 CEO에게 보고
         │ (실행 결과 보고)
         ▼
[Stage 3: 👑 CEO Claude 컴팩트 감사 & 최종 승인 (Sign-off)]
  • 설계 계약 충족 여부 확인 및 최종 사인오프 (2~3문장 고밀도 요약)
  • 지식 그래프(shared-memory MCP)에 세션 결과 자동 영구 기록
```

---

## 실행 방법

### 채팅창에서 바로 호출
```text
/cagh-pair <작업 내용>
```
*(예: `/cagh-pair 토큰 버킷 기반 레이트 리미터 모듈 설계 및 구현`)*

### 터미널에서 직접 실행
```bash
cagh pair "<작업 내용>"
```

### 지식 그래프 저장 확인
```bash
cagh memory list
```
CEO Claude가 내린 자율 역할 분담과 Antigravity의 실행 리포트가 `Claude_CEO_Hub`와 `Antigravity_Subagent` 관계 엣지로 공통 메모리에 영구 동기화됩니다.
