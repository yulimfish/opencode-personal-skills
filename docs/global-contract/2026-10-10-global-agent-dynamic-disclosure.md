# Global Agent Dynamic Disclosure Implementation Plan

> **For agentic workers:** Use the installed `swarm-cluster` skill for approved parallel work, or follow the current environment's in-session plan execution workflow. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reduce always-loaded global-agent prompt content by extracting task-specific policies into first-party skills without weakening broadly applicable rules.

**Architecture:** Keep core behavior and safety rules in `~/.config/opencode/AGENTS.md`; add four focused skills for detailed Git safeguards, release identity/process, swarm coordination, and session hygiene. The global file retains concise task triggers that point to those skills. No existing skill will be modified.

**Tech Stack:** Markdown, OpenCode `SKILL.md` frontmatter.

**Spec:** `2026-10-10-global-agent-dynamic-disclosure-design.md` (sibling file)

## Global Constraints

- Preserve the global contract's core communication, authorization, risk, memory, tool-use, verification, audit, and baseline Git-safety rules.
- Do not modify existing skills whose first-party authorship is unconfirmed.
- Do not reinterpret or change existing email values, release steps, swarm thresholds, or context-compression values.
- Keep global triggers for each extracted policy.
- Do not commit or publish.

## Review Focus

- A normal code edit still encounters the baseline Git protections in `AGENTS.md`; verify those clauses remain.
- A Git commit/upstream operation can discover the detailed Git safeguards; verify the route and skill name match, including lowercase `s` for a path carrying both hidden index flags.
- Repository initialization or release loads the identity/publishing policy; verify package author follows GitHub's current public-email policy, non-public email fields use the local commit identity, original identity values remain private, npm 2FA is user-run, and author/committer are both validated after identity repair.
- A swarm-triggering task loads the original concurrency limits and worker/retry rules; verify no thresholds changed.
- Context compression and browser automation each load the retained configuration/cleanup details; verify the exact percentages, flags, and cleanup commands survive.

---

### Task 1: Add first-party policy skills

**Files:**
- Create: `skills/personal-git-workflow/SKILL.md`
- Create: `skills/personal-release-workflow/SKILL.md`
- Create: `skills/personal-swarm-workflow/SKILL.md`
- Create: `skills/personal-session-hygiene/SKILL.md`

**Interfaces:**
- Consumes: Policy text currently in `~/.config/opencode/AGENTS.md` §§3.1, 3.4–3.8.
- Produces: Skills named exactly `personal-git-workflow`, `personal-release-workflow`, `personal-swarm-workflow`, and `personal-session-hygiene`, with descriptions that identify their task triggers.

- [x] Copy the corresponding detailed policy into each skill, retaining exact operational values and commands.
- [x] Verify each frontmatter `name` matches its directory and global routing slug; verify the relevant source rules are present.

### Task 2: Refactor global routing

**Files:**
- Modify: `AGENTS.md`

**Interfaces:**
- Consumes: The four skill names from Task 1.
- Produces: A shorter global file with explicit routes and complete core safeguards.

- [x] Keep the core rule sections and baseline Git protections; replace only extracted detailed blocks with concise trigger references.
- [x] Ensure release/identity, swarm, Git-special-case, context-compression, and browser-cleanup triggers point to the exact new skill names.

### Task 3: Verify the resulting policy surface

**Files:**
- Verify: `AGENTS.md`
- Verify: the four `SKILL.md` files listed in Task 1.

**Interfaces:**
- Consumes: Tasks 1–2.
- Produces: Evidence that no core rule was dropped, all moved rules remain available, and no unrelated existing skill was changed.

- [x] Compare the final text against the approved spec and review the changed paths.
- [x] Check frontmatter names, all global references, exact route commands/values, and absence of changes to existing skills.
- [x] Report validation limitations: no application suite applies to Markdown policy; OpenCode surfaced all four skill IDs and explicit loading of each succeeded, but automatic trigger selection was not separately simulated. The config directory is not a Git repository, so no Git diff is available; within that directory the patch operations changed only `AGENTS.md` and the four new skills. The global contract went from 179 lines before the change to 158 after (-21 lines).

### Task 4: Independent audit and remediation

**Files:**
- Verify: the global contract, four new skills, and this implementation plan.

- [x] Run a fresh-context, read-only audit against the approved user request and spec.
- [x] Fix identified BLOCKER/MAJOR findings (explicit authorization for history rewrites; recognize combined `skip-worktree` + `assume-unchanged` marker `s`; validate both author and committer before publishing an amended commit).
- [x] Obtain a fresh independent re-audit before completion.

Audit result: **CONDITIONAL PASS** — no remaining policy-content defect was confirmed. Independent verification could not establish a pre-change baseline because `~/.config/opencode` is not a Git repository, and automatic trigger-based skill selection was not simulated; the four skills were explicitly loaded successfully in the primary session.
