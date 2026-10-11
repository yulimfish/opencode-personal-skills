# OpenCode Personal Workflows

Personal OpenCode agent workflow and first-party skills, consolidated in one repository. Snapshot date: 2026-10-11.

## Included

- **18 first-party skills** in `skills/<name>/SKILL.md`: ten previously published under `Yulimfish/opencode-skill-*`, seven personal policy skills extracted from the global contract, and the locally authored `tiered-web-search` skill.
- **Global contract** in `AGENTS.md`, with corresponding skill routes.
- **Source records** in `docs/`, including the latest tiered-search Spec/Plan.

This repository is the consolidated source snapshot. Some skills also retain their existing standalone GitHub repositories for compatibility with the current workflow-kit installer.

## Skill provenance

The ten `opencode-skill-*` entries were matched to repositories owned by `Yulimfish`; local files were compared with each repository's current `main` `SKILL.md` through GitHub's API. Eight match byte-for-byte. `memory-dream` differs because its public copy generalizes account-specific archive references, normalizes trailing whitespace, and folds the long YAML description; `post-task-audit` also uses a folded YAML description to fix invalid upstream frontmatter. All ten source repositories declare MIT; their original `Yulimfish` copyright notice is retained here.

The seven `personal-*` skills are the task-specific policies extracted into the global contract and referenced by its routing rules. `tiered-web-search` is an additional locally authored skill whose approved design, implementation plan, and tool-only behavior are documented in `docs/superpowers/`; it uses only the existing `websearch` and `webfetch` tools. Other installed skills were excluded when their provenance points to upstream authors or external skill collections. For example, local `improve-animations` and `review-animations` correspond to Emil Kowalski's upstream `emilkowalski/skills`; the `yuque-personal-*` skills identify `chen201724` as author. Similar names or subject matter alone are not treated as evidence of authorship.

The public copies generalize account-specific email and Yuque values, the personal persona line, local checkout paths, and machine-specific incident references. Local configuration files are unchanged except for adding the required `name` metadata to `swarm-cluster`.

## Use

Copy selected skill directories from `skills/` into `~/.config/opencode/skills/`. Review `AGENTS.md` before adopting it: these files capture one user's preferences and local assumptions, not universal defaults.

Validate skill metadata with (requires PyYAML):

```bash
python3 tests/validate-skill-frontmatter.py
```

## License

MIT. See `LICENSE`.
