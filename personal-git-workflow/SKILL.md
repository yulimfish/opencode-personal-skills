---
name: personal-git-workflow
description: "Load before Git commits, staging, merges/rebases, upstream synchronization, or other operations that can interact with hidden local changes. Contains user-specific commit-scope and hidden-index safeguards beyond the global baseline rules."
---

# Personal Git Workflow

The global `AGENTS.md` contains the always-applicable Git safety baseline. Load this skill for the detailed commit and upstream-operation safeguards below.

## Commit scope

- Before editing, translate the user's authorization into an explicit allowlist of repository-relative paths; keep exclusions explicit. Related documentation or tests remain out of scope unless authorized.
- Before committing, run `git status --short` and identify pre-existing changes so they are preserved.
- Stage explicit paths. Inspect `git diff --cached --name-status` and compare the entire staged path list against the allowlist—not just whether each path seems related. If an unexpected path appears, stop and determine its origin; do not discard it or expand scope without authorization.
- Before committing, verify the candidate commit's changed paths against its intended parent, for example with `git diff --cached <intended-parent> --name-status`. For a normal commit, the parent is current `HEAD`; for `--amend`, compare against the parent of the commit being amended. The resulting path list must exactly match the allowlist; checking only the staged diff against current `HEAD` can miss paths already present in an amended commit.
- If correcting out-of-scope content would require restoring files or rewriting history, explain the exact paths and impact and obtain explicit user authorization first. Once authorized, back up the original branch tip and all index, worktree, and untracked changes before rewriting; then verify the final candidate against its intended parent.
- Use English commit messages and PR titles/bodies unless the user explicitly asks for Chinese.

## Multi-repository scope

- Identify every independent Git root involved (including content subrepositories) and map each changed path to its owning repository before staging. A clean status in one root does not prove another root is clean or synchronized.
- Compare each source/destination mapping, including additions and deletions; stage explicit repository-relative paths and inspect `git diff --cached --name-status` separately in every repository.
- Treat commit and push authorization as repository-specific. Do not push any repository without explicit authorization for that repository in the current task.
- Exclude incidental operating-system/editor artifacts such as `.DS_Store` and `Thumbs.db` unless one is itself an explicit deliverable.

## Superpowers phase checkpoints

- This applies only to a task using the long-running Superpowers ledger (`.superpowers/sdd/.../progress.md`), not every task or every small implementation step.
- After each independently completable plan task passes its targeted verification, treat it as one local commit checkpoint. Do not commit incomplete work or split trivial operations into commits.
- Commit only within the scope explicitly authorized by the user in the current session, following global `AGENTS.md` §3.1. Without authorization, update the ledger/todo and mark the checkpoint as pending; do not stage or commit.
- After a checkpoint is committed, record its commit hash in the plan ledger so progress and repository state stay connected. Do not push unless separately authorized.

## Hidden local changes before merge/rebase

- Before merging or rebasing with upstream, run `git ls-files -v` to identify paths marked `skip-worktree` (`S`), `assume-unchanged` (`h`), or both (`s`). With `-v`, lowercase tags indicate `assume-unchanged`; therefore lowercase `s` is a skip-worktree path with assume-unchanged also set.
- Back up the exact bytes and the full combination of index flags for those paths; after the merge/rebase, restore each byte-for-byte and restore every original index flag, then verify.
- `git status` cannot show these hidden changes. Never run `reset`, `checkout`, or force an overwrite against them.
