---
name: personal-memory-workflow
description: "Mandatory at the start of any non-trivial task; before recalling prior decisions/preferences, editing an untouched project or subsystem, making architecture/stack/dependency/naming/format choices, asking a clarifying question that may be answered by prior context, or resuming after compaction; also at task close when durable decisions or pitfalls should be saved. Use with long-term-memory."
---

# Personal Memory Workflow

This workflow owns the personal memory requirements formerly embedded in global `AGENTS.md`. Load it whenever any trigger in the description or global contract applies, then use the `long-term-memory` skill and the `memory` tool for the actual operation.

## Recall before acting

- At the start of every non-trivial task, search memory proactively, even if none of the narrower examples below seems to apply.
- Search before referring to prior work/preferences, starting work on an untouched project/subsystem, making architecture/stack/dependency/naming/format decisions, composing a clarification question, or continuing after context compaction.
- Search `scope:"project"` first; if it has no useful hit, widen to `scope:"all-projects"`; ask the user only if both miss. Do not skip directly to the broader scope.
- A precise topic may use one focused search. For vague or broad topics, narrow in up to 3 layers (topic → subtopic → exact fact), using each result to refine the next query; stop when the needed authoritative result is found.
- If a memory is used, cite it in the first line as `（依据 memory <id> · <日期>）`.

## Persist durable outcomes

At task close, add a concise, self-contained, dated memory for durable decisions, non-obvious pitfalls, or confirmed workflows that would benefit future sessions. First search to avoid duplication. Explicit requests such as “记住/以后都用/别再问我/remember/从今天开始” always trigger this workflow.

- Do not save session-only WIP, transient errors, secrets, credentials, tokens, PII, or verbose logs.
- Record the reusable conclusion and reason, not the full trace.
- Apply outcome tags when relevant: `outcome:corrected` after a user correction (include the correct rule and a short “曾误：…” note); optionally `outcome:success` for a reusable one-pass workflow or `outcome:rework` for a resolved rework.
- `profile` is read only when the user asks what has been learned about them. Never paste raw profile data.

## Failure handling

Follow `long-term-memory` for tool/API details. If the memory system reports it is initializing, wait 2 seconds and retry once; if it still fails, proceed without memory and disclose that limitation. If project-scope search returns no useful result, widen scope before asking the user.
