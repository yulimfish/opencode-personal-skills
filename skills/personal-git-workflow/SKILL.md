---
name: personal-git-workflow
description: "Load before Git commits, staging, merges/rebases, upstream synchronization, or other operations that can interact with hidden local changes. Contains user-specific commit-scope and hidden-index safeguards beyond the global baseline rules."
---

# Personal Git Workflow

The global `AGENTS.md` contains the always-applicable Git safety baseline. Load this skill for the detailed commit and upstream-operation safeguards below.

## Commit scope

- Before committing, run `git status --short` and identify the exact intended scope.
- After staging, inspect `git diff --cached --name-status`. Confirm every staged path is intended and that no user-explicitly-excluded content is included (for example, test package names / `applicationId`, test files, or existing Gradle worktree changes).
- Use English commit messages and PR titles/bodies unless the user explicitly asks for Chinese.

## Hidden local changes before merge/rebase

- Before merging or rebasing with upstream, run `git ls-files -v` to identify paths marked `skip-worktree` (`S`), `assume-unchanged` (`h`), or both (`s`). With `-v`, lowercase tags indicate `assume-unchanged`; therefore lowercase `s` is a skip-worktree path with assume-unchanged also set.
- Back up the exact bytes and the full combination of index flags for those paths; after the merge/rebase, restore each byte-for-byte and restore every original index flag, then verify.
- `git status` cannot show these hidden changes. Never run `reset`, `checkout`, or force an overwrite against them.
