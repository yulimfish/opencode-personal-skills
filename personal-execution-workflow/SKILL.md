---
name: personal-execution-workflow
description: "Mandatory for non-trivial multi-tool work (3+ calls, file exploration, refactors, or batch edits), and whenever choosing execution, verification, retry, or audit effort. Combines the personal execution-economy contract with tool-call discipline; load before the first tool call in matching work."
---

# Personal Execution and Tool Workflow

This personal workflow combines execution economy with tool-call discipline. Load it for every matching task, then use `tool-call-discipline` and `execution-economy` for their detailed mechanics.

## Hard tool rules

- Prefer the dedicated file/search/edit tool over shell workarounds; use shell only when no dedicated tool applies.
- Run independent tool calls in parallel; sequence only when the next call depends on the previous result.
- Read at least 100 lines when exploring an unknown file; use wide reads rather than repeated small slices.
- Read before editing. Check absolute paths, exact field names, and real values before calls; never fabricate parameters.
- On failure, inspect the actual error, fix that cause, and retry at most once. Do not switch tools speculatively.

## Risk and effort

- Optimize for the user's final requested state, not intermediate checks or preparation. Choose the shortest safe path and add complexity only for a real risk or observed failure.
- Level 1 (low-risk/reversible): execute directly; verify by reading back the target and ensuring only intended changes.
- Level 2 (moderate): perform one relevant scope check and one targeted verification; audit only when a `personal-plan-audit-workflow` trigger applies.
- Level 3 (high-risk/irreversible: deletion, force overwrite/history rewrite, migration, production change, publication, broad automated edits): make a backup, obtain confirmation before the irreversible step, verify strictly, and follow the mandatory Plan → Build → Audit gate.
- Risk and complexity are separate axes. A large but reversible task is not automatically high-risk; a small destructive task is.
- Keep validation minimal but sufficient: each check must catch a likely defect, prevent data loss, satisfy an explicit contract, or be necessary for acceptance. Do not repeat a settled check unless state could have changed or the prior result was ambiguous.
- Prefer narrow paths, processes, parameters, and permissions over broad operations plus post-hoc auditing.
- After one failed automation attempt, compare fixing automation with a simpler/manual path; use the simpler route when it reaches the goal sooner. Work around unrelated environment problems rather than rebuilding the environment.

## Continuous execution and reporting

- Treat authorization for a complete task as authorization for its normal necessary intermediate steps; do not pause for routine “continue?” confirmations.
- For tasks with 4+ tool calls or 2+ phases, send one short progress update between meaningful stages; do not narrate routine tool use.
- Trust credible user-provided results unless they conflict with evidence or a high-risk action needs independent verification.
- Before completion, run a relevant test/lint/typecheck, reproduce the original scenario, or explicitly report “未验证 — 原因 …”. Never claim an unrun check passed.
