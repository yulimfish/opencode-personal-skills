# Global Agent Dynamic Disclosure Design

## Goal

Reduce always-loaded content in `~/.config/opencode/AGENTS.md` by moving task-specific, low-frequency procedures into first-party skills, while keeping the user's broadly applicable core rules complete and immediately available.

## Constraints

- Do not modify existing skills whose first-party authorship is unconfirmed.
- `execution-economy` is confirmed as a user-authored skill and may be reused; no change to it is needed for this scope.
- Keep the global contract's core communication, authorization, risk, memory, tool-use, verification, audit, and baseline Git-safety rules.
- Keep an explicit global trigger for every extracted policy so the relevant skill is loaded when needed.
- Do not change existing email/release policies, browser tooling, swarm thresholds, or compaction values. Package-author representation follows the user's explicit clarification below; public contact details stay in the designated README/docs/issues fields.
- Package author metadata follows the user's clarification: use the GitHub profile display name; if the email field is public, use the current GitHub public email, and if none is configured omit it. For non-public email fields, use the local commit email. Refresh profile details if the settings change.

## Proposed extraction

Create four first-party skills and update the global contract's references:

1. `personal-git-workflow` — move Git-specific commit-scope checks and hidden-index-change safeguards from §3.1. Keep baseline protections in `AGENTS.md` (inspect and preserve user changes, use narrow scope, avoid destructive cleanup, do not commit without authorization).
2. `personal-release-workflow` — move identity/email rules (§3.5) and the full publishing workflow (§3.6). Route repository initialization, commit identity setup, and release/distribution tasks to this skill.
3. `personal-swarm-workflow` — move the detailed coordination and concurrency rules from §3.4. Do not modify the existing `swarm-cluster` skill.
4. `personal-session-hygiene` — move context-compression configuration (§3.7) and browser-session cleanup (§3.8). Route compression/configuration and browser-automation tasks to this skill.

The global file will retain the short task triggers and point to these skill names. Existing third-party or provenance-unknown skills will not be edited.

## Non-goals

- No broad rewrite or style cleanup of `AGENTS.md`.
- No changes to the contents of existing skills.
- No changes to `.config/opencode` beyond `AGENTS.md` and the four new skills.
- No changes to the risk thresholds, audit criteria, swarm thresholds, email values, release steps, or compression values.

## Verification

- Review the final diff to ensure extracted rules are preserved without semantic changes and the global contract retains its core safeguards.
- Check that all four skill names and trigger references match exactly and that none of the target paths already exist.
- Run a focused structural check (frontmatter/name consistency and references); no application test suite applies to Markdown policy files.
