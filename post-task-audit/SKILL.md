---
name: post-task-audit
description: >-
  Use AFTER a non-trivial task is claimed complete. Spawns one or more
  context-free subagents to independently audit the work — functional
  correctness, code compliance, security, alignment with user intent, doc
  consistency. Trigger phrases include "审一下", "复核", "核查", "audit it",
  "verify the work", "检查一下我刚才做的". Main agent MAY also auto-activate
  when the task involved: destructive ops, security/credential surface,
  multi-file refactor, releasable artifact, >30 lines of code change, or
  ambiguous acceptance criteria. Do NOT audit for: single-file tweaks, read-only
  Q&A, tasks the user explicitly said "不用审".
---

# Post-Task Audit (Independent Verifier)

Spawn a **fresh, context-uncontaminated subagent** to audit the just-finished work. The auditor has NOT seen the main agent's reasoning trail — this is the point: fresh eyes catch things the executor rationalized past.

## 0. When to activate — main agent decides

**Activate when ANY of these fire**:

- User explicitly says: "审一下", "复核", "核查", "checkone", "audit it", "verify the work".
- The task produced a **releasable artifact** (published package, merged PR, sent email, external API call already made or about to be made).
- The task touched a **security surface**: credentials, permissions, `.env`, auth, encryption.
- The task performed a **destructive op**: `rm -rf`, force-push, DB drop, key revocation.
- The task was a **multi-file refactor** (≥3 files touched) or ≥30 lines changed.
- **Acceptance criteria were ambiguous** and the main agent guessed — an auditor should confirm the guess was defensible.

**Do NOT activate for**:

- Single-file surgical edits (< 30 lines).
- Read-only lookups / Q&A / research summaries with no artifacts.
- Tasks where the user said "别审 / 不用检查 / no audit".
- Interactive design iteration where the user is already reviewing each step.

If unsure, **skip**. Over-auditing wastes tokens and slows the loop. Under-auditing is fine when the change is small — the user still has the diff.

## 1. Single-auditor (default) vs multi-auditor (upgrade)

### Single-auditor — use `goal-verify`

**`goal-verify`** is the default auditor — shipped by the [`opencode-swarm-agents`](https://github.com/Yulimfish/opencode-swarm-agents) bundle (not a built-in). It is context-free by construction (fresh session, no tool history) and read-only. Use for 80% of audits.

```
task(goal-verify, "<audit prompt — see template §3>")
```

### Multi-auditor — swarm 2-3 dimensions in parallel

Upgrade to a swarm ONLY when the task spans multiple dimensions that need distinct expertise. Reuse existing `swarm-worker*` variants (provider-specific variants exist only if `agents/swarm-worker-<name>.md` is installed; otherwise use the generic `swarm-worker` in a fresh session) and inject an **audit persona**. Example (release-day audit of an npm publish):

```
task(swarm-worker-deepseek, "You are the SECURITY auditor …")
task(swarm-worker-kimi,     "You are the CODE-COMPLIANCE auditor …")
task(swarm-worker,          "You are the USER-INTENT auditor …")
```

Concurrency & failure rules from the `swarm-cluster` skill apply verbatim (max 4 per wave, no nested swarms, halve on 429).

**Prefer** a different provider for re-audit when provider-specific variants are installed (kimi ↔ deepseek ↔ glm); the essential independence is a **fresh context** (a new session), which `goal-verify` provides even when the underlying model is inherited.

### Read-only audit wave (2–4 auditors; extends the multi-auditor upgrade)

The multi-auditor upgrade above splits by **dimension** (2–3 auditors). For a high-stakes or multi-**module** deliverable, widen it to a wave of 2–4 fresh-context read-only auditors, split by dimension **or** by module (semantics / UI / storage / algorithm).

1. **Fan out 2–4 auditors in one message**; each auditor still takes **1–2 dimensions** (§2) — never all six, per §2's hard rule.
2. **Bind the boundaries in every auditor prompt**: 只读、不改文件、不 commit/push、不派生代理（no nested agents）、不运行 Gradle/build（若用户要求“先代码审计”）、显式声明设备侧未验证（no device → `source-only`）、不得把源码扫描当作运行验证。
3. **Hard return format**: first line `PASS | CONDITIONAL PASS | FAIL`, then a one-line verdict summary, the per-auditor dimension verdicts, findings by severity, then “Not audited / device unverified” + Confidence (same shape as §3).
4. **Fix loop**: main agent fixes by severity (BLOCKER first), then spawns a **new** auditor (a fresh session — never the same session; prefer a different provider when available) to re-verify only the fixed slice. Max 3 rounds; if still not PASS, escalate to the user with the blocker.
5. **Evidence per pass**: name the exact command and test count (e.g. a unit-test suite going 175→177 tests, 0 failures/errors/skipped).

A wave raises independence, not authority: it never substitutes for user approval on destructive operations.

## 2. Audit dimension menu (pick what fits)

In **multi-auditor / wave** mode, give each auditor 1–2 dimensions from this list — never all six. In **single-auditor** mode the default `goal-verify` covers all six (see `agents/goal-verify.md:26-33`).

| Dimension | What to check | Best auditor |
|---|---|---|
| **Functional correctness** | Does the code/change actually do what the user asked? Are the claimed test-pass / lint-pass real? Re-run if possible. | `goal-verify` |
| **Code compliance** | Style (matches existing codebase), lint / typecheck clean, no dead code, no unrequested refactor | `swarm-worker-kimi` |
| **Security & secrets** | No hardcoded keys, no logs leaking creds, permission changes are intentional, no injection surface | `swarm-worker-deepseek` |
| **Performance / resource** | No obvious O(n²) hot paths, no unbounded loops, no memory leaks, no accidental network fanout | `swarm-worker-deepseek` |
| **Doc / naming consistency** | Docs, comments, filenames match the code; no stale references to renamed symbols | `swarm-worker` |
| **User intent alignment** | The delivered thing matches what the user actually asked, not what was easy to build; no gold-plating, no scope creep | `swarm-worker-glm` |

## 3. Auditor prompt template

Every audit prompt MUST contain, in this order:

```
## Your role
You are an INDEPENDENT context-free auditor. You have NOT seen how the work was done. Your job is to check the RESULT with fresh eyes.

## Task the executor was given (verbatim from user)
<paste the original user request>

## What the executor claims to have delivered
<one-paragraph summary: files changed, key decisions, verification the executor claims>

## Your audit dimensions (do NOT expand)
- <dim 1 from §2>
- <dim 2 from §2 — max 2 dims per auditor>

## Scope
- Read anything under <bounded paths>.
- You MAY run: <specific verification commands, e.g. "cat / grep / rg / lint / test">
- You MAY NOT: edit files, commit, push, delete.

## Return format (hard)
<one-line verdict on first line: PASS | CONDITIONAL PASS | FAIL>

## Verdict summary
<one paragraph>

## Findings
- [BLOCKER] <finding> — <evidence: file:line or command output>
- [MAJOR]   <finding> — <evidence>
- [MINOR]   <finding> — <evidence>

## Not audited (out of scope)
- <what you deliberately did not check>

## Confidence
<low | medium | high> — <one-line reason>
```

Severity legend (main agent must respect):

- **BLOCKER** — must be fixed before yielding to user. Anything security/correctness/destructive falls here.
- **MAJOR** — should be fixed this turn unless user is time-pressed; flag prominently in summary.
- **MINOR** — record in output; fix if convenient, defer otherwise.

## 4. How the main agent handles the audit result

1. **Read every auditor's final message.** Do not skim.
2. **Handle by severity**:
   - Any `BLOCKER` → fix it in the current turn, then re-audit ONLY the fixed slice with a fresh context (`goal-verify` is the default; prefer a different provider for security-sensitive fixes — see §1).
   - `MAJOR` → fix if cheap (< 5 min), else surface in the final summary as "known limitation".
   - `MINOR` → mention in summary, do not fix unless asked.
3. **If the auditor is wrong** (false positive, misunderstood scope):
   - State explicitly why in the summary: "auditor flagged X but scope excluded it, standing by decision".
   - Do NOT silently ignore auditor findings.
4. **If auditors disagree** (multi-auditor mode): apply swarm-cluster reconciliation — consensus > majority > highest-confidence — and state which rule you used.

## 5. Output shape for the user

After audit, main agent's final answer to the user should include:

```
<one-line result>

<the actual deliverable>

## 独立核查
- 审计员：<goal-verify | swarm-worker-kimi | ...>
- 结论：PASS | CONDITIONAL PASS | FAIL
- BLOCKER 数：<N>（已修 / 未修）
- MAJOR 数：<N>
- MINOR 数：<N>（列出，不修）
```

If audit was NOT run, say why in one line: "未开审计 —— 单文件小改动，diff 已可读" or "用户显式说无需核查".

## 6. Anti-patterns

- **Do not** pass the main agent's reasoning trail to the auditor. The point is a fresh session.
- **Do not** ask the same auditor to check its own previous audit — spawn a new one if re-check is needed.
- **Do not** treat "audit passed" as license to skip user confirmation on destructive ops (audit ≠ approval).
- **Do not** run audit on every trivial answer. This is the fastest way to burn tokens with no benefit.
- **Do not** self-audit (main agent auditing its own work) — that IS the context pollution this skill exists to avoid.
