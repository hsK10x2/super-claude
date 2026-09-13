---
name: btw
description: Use when the user asks a quick side question, starts a message with /btw or "btw", or needs an isolated lookup or answer without derailing the ongoing task or polluting conversation context
---

# /btw: Side-Channel Quick Q&A

Provides quick, isolated answers to side questions or tangents without interrupting the primary task trajectory or cluttering the conversation history with verbose reasoning chains.

## Overview

In CLI environments like Claude Code, `/btw` functions as an ephemeral overlay: you ask a quick question, see the answer, and dismiss it without polluting the conversation memory.

In Antigravity IDE, this skill replicates that exact capability:
- Answers the side question directly with zero conversational filler.
- Minimizes context pollution so the primary task's working memory remains clean.
- Immediately resumes the ongoing task without changing plans or losing focus.

## When to Use

- The user invokes `/btw <question>` or prefixes a query with "btw", "그건 그렇고", "근데 잠깐".
- The user asks for a quick confirmation (variable name, file location, prior decision, config value) while a larger task is in progress.
- The user asks a technical question that should not derail or alter the active implementation plan.

## When NOT to Use

- The user wants to change the scope or requirements of the current task (treat as a regular instruction).
- The user asks for a comprehensive multi-step architecture design or deep refactoring (load `architecture-design` or `brainstorming`).

## Execution Protocols

### 1. Fast Path: In-Memory Recall
If the answer is already present in conversation history or prior decisions:
- Respond **only** with the direct answer string.
- Do not add conversational padding (e.g., "확인해 드렸습니다", "질문하신 내용은 다음과 같습니다").
- Keep response under 3 lines whenever possible.

### 2. Investigation Path: Codebase or Concept Lookup
If the question requires searching files, grepping symbols, or reading a definition:
- Execute the minimal search quietly (`grep_search` or `view_file`).
- Do **not** dump intermediate search logs or verbose explanation of every file viewed.
- Extract and return **only** the substantive answer (e.g., file path, line number, or definition).

### 3. Task Continuity
- After providing the answer, immediately proceed with the active primary task if one was underway.
- Do not pause or ask "다음 작업을 계속할까요?" unless user input is strictly required to continue.

## Examples

### Example 1: In-Memory Recall
**User:** `/btw 아까 정한 세션 스토리지 TTL이 얼마였지?`  
**Agent:**
```text
24시간 (1일)입니다. Redis 클러스터 장애 시 토큰 무효화 테이블을 보존하기 위해 86,400초로 설정했습니다.
```

### Example 2: Codebase Symbol Lookup
**User:** `/btw UserAuthMiddleware가 어느 파일에 마운트되어 있어?`  
*(Agent performs quiet grep on UserAuthMiddleware)*  
**Agent:**
```text
src/middleware/auth.ts 42번 라인에 정의되어 있으며, src/server.ts 88번 라인의 app.use(UserAuthMiddleware)에서 전역 마운트됩니다.
```

### Example 3: Quick Concept Check
**User:** `/btw Go에서 sync.Once와 sync.Mutex의 차이가 뭐였더라?`  
**Agent:**
```text
sync.Once는 프로세스 수명 주기 동안 단 한 번만 실행되는 초기화(싱글톤, 리소스 로딩)에 특화되어 있으며, sync.Mutex는 임계 영역에 대한 반복적인 상호 배제 잠금/해제에 사용됩니다.
```
