---
name: btw
description: Ask a quick side question without interrupting ongoing work or polluting conversation context
---

# /btw: Side-Channel Quick Q&A

Ask a quick side question without interrupting the primary task trajectory or cluttering the conversation history.

## Usage

```text
/btw <question>
/super-claude:btw <question>
```

## Behavior

1. **In-Memory Recall**: Answers immediately in 1-2 lines with zero conversational fluff.
2. **Quiet Lookup**: Searches codebase or references without dumping intermediate tool logs into context.
3. **No Derailment**: Automatically preserves the active implementation plan and resumes the main task.

## Examples

```text
> /btw what was the name of the interface we defined earlier?
> /btw where is SessionMiddleware mounted in src/server?
> /btw remind me what the Redis TTL was set to
```
