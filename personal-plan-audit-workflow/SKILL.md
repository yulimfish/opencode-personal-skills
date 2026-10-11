---
name: personal-plan-audit-workflow
description: "Mandatory for any non-trivial implementation plan, hard/high-risk work, tasks with 3+ executable steps, cross-phase/cross-context/cross-session plans, Level 3 production changes or broad automation, any independent-audit trigger, or user-requested review. Governs planning, ledger, audit, and pass-before-delivery; load before planning or implementation."
---

# Personal Plan and Audit Workflow

This personal workflow owns the global planning and independent-audit contract. Load it whenever any trigger in the description or global `AGENTS.md` applies. It supplements, and does not replace, the task-specific mechanics in `writing-plans`, `executing-plans`, and `subagent-driven-development`. Its audit procedure below is self-contained; mandatory audit decisions must not be delegated to generic skill opt-out rules.

## Planning and routing

- Simple or single-step work: execute directly; do not create a plan just to satisfy process.
- Any non-trivial implementation plan: load `writing-plans` before drafting it. Use that Skill's planning structure and quality checks, but follow the global authorization/interrupt rules: do not present an execution-method menu or pause for routine plan approval when the user has already authorized implementation. Give the recommendation and continue; pause only for a material decision/high-risk boundary under `AGENTS.md` §1.1 or an explicit design/spec approval gate such as `brainstorming`.
- Three or more executable steps: create/update todos, keep exactly one `in_progress`, and transition the completed step and next active step together.
- Hard work (multi-file refactor, architecture/data-model decisions, complex state machine, releasable artifact, ambiguous acceptance, or user says “认真做/好好搞/严格一点”): use Plan → Build → Audit. The concise in-chat Plan summary is at most 10 lines and names scope, target files, key decisions, and verification. If `writing-plans` requires a detailed plan artifact, its required structure may exceed 10 lines; the cap does not apply to that artifact.
- Long-running ledger applies only when all are true: the work is Hard/large, has at least 3 substantive steps, and spans multiple phases or may resume across context/session. Do not create a ledger for small or short-lived work.
- For ledger work, use the appropriate plan-execution skill and its `sdd-workspace` workflow; resume at the first incomplete task, preserve the plan's ledger, and update ledger/todos at task completion, after a fix-loop/ruling, and before handoff. If the workspace is not Git or ledger tooling is unavailable, use plan/handoff checkpoints and say so; never claim a ledger was recorded unless the file was actually updated.
- Prefer inline execution for sequential work. Use `subagent-driven-development` for primarily independent plan tasks; use `swarm-cluster` only for genuinely independent work that benefits from parallelism.

## Independent audit triggers

Run a fresh-context, read-only independent audit when ANY applies:

- Releasable artifact, security/credential surface, or destructive operation.
- Any Level 3 operation, including production changes or broad automated edits.
- Multi-file refactor touching at least 3 files or at least 30 changed lines.
- Acceptance criteria were ambiguous and the agent made a consequential interpretation.
- User explicitly requests review/audit/verification.
- Hard task as defined above.

Skip audit for pure Q&A/read-only research and a single-file change under 30 lines, unless the user explicitly requests an audit or another trigger applies. These mandatory global/Hard-task triggers override any generic skip example in `post-task-audit`. A user request to “快点” does not waive an audit; explicit “不用审/不用核查” may waive an ordinary audit only, never a Hard-task or Level 3 requirement.

Use a fresh `goal-verify` subagent by default. Supply the original user request, changed paths, claimed result, bounded read-only scope, and the applicable audit dimensions. The auditor must not edit files or self-expand the task. A multi-auditor wave is reserved for genuinely distinct high-stakes dimensions and follows `personal-swarm-workflow`; otherwise use one independent auditor.

## Hard-task audit gate

1. Plan → Build → Audit. Keep the audit independent and read-only; the executor must not self-audit.
2. The audit covers requirement completeness, logical correctness, edge cases, code quality, test coverage (including tautological tests), and actual runtime evidence.
3. Fix BLOCKER findings before delivery. Fix inexpensive MAJOR findings; otherwise disclose them. Mention MINOR findings without silently dropping them. This severity guidance does not waive the required final PASS for Hard or Level 3 work: if a deferred finding leaves the audit at CONDITIONAL PASS/FAIL, do not claim completion; fix it or escalate the blocker to the user.
4. Default to at most 3 fix-and-independent-re-audit rounds for the same deliverable in one review window. Obtain explicit user authorization before a fourth round. Without that authorization, stop and report each remaining finding and its impact; Hard/Level 3 work still cannot be delivered as complete without PASS.
5. Deliver with the auditor, verdict, finding counts, and evidence. Both Hard and Level 3 work require a final PASS before delivery; an audit never substitutes for user authorization or confirmation before irreversible actions.

## Phase checkpoints and commits

- For plans using a long-running ledger, after each independently completable task passes targeted verification, mark one local commit checkpoint; do not split trivial actions or commit incomplete work.
- A checkpoint is staged/committed only if the user authorized that operation in this session. Otherwise record it as pending in the ledger/todo. Load `personal-git-workflow` before staging, committing, merging/rebasing, or upstream synchronization.
- Never commit or push merely because a plan example or this workflow mentions a checkpoint.
