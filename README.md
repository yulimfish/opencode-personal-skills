# OpenCode Personal Workflows

Personal OpenCode agent workflow and first-party skills, consolidated in one repository. Snapshot date: 2026-10-10.

## Included

- **14 first-party skills** in `skills/<name>/SKILL.md`: ten previously published under `Yulimfish/opencode-skill-*` and four personal policy skills extracted from the global contract.
- **Tower workflow** in `agents/`: a primary controller and two model-tier subagents.
- **Global contract** in `AGENTS.md`, with corresponding skill routes.
- **Source records** in `docs/` and a Tower configuration smoke test in `tests/`.

This repository is the consolidated source snapshot. Some skills also retain their existing standalone GitHub repositories for compatibility with the current workflow-kit installer.

## Skill provenance

The ten `opencode-skill-*` entries were matched to repositories owned by `Yulimfish`; local files were compared with each repository's current `main` `SKILL.md` through GitHub's API. Eight match byte-for-byte. `memory-dream` differs because its public copy generalizes account-specific archive references and normalizes trailing whitespace. `post-task-audit` uses a folded YAML description to fix invalid upstream frontmatter. All ten source repositories declare MIT; their original `Yulimfish` copyright notice is retained here.

The four `personal-*` skills are the task-specific policies extracted into the global contract and referenced by its routing rules. Other installed skills were excluded when their provenance points to upstream authors or external skill collections. For example, local `improve-animations` and `review-animations` correspond to Emil Kowalski's upstream `emilkowalski/skills`; the `yuque-personal-*` skills identify `chen201724` as author. Similar names or subject matter alone are not treated as evidence of authorship.

The public copies generalize account-specific email values, the personal persona line, local checkout paths, and a machine-specific incident reference. Local configuration files are unchanged except for adding the required `name` metadata to `swarm-cluster`.

## Use

Copy selected skill directories from `skills/` into `~/.config/opencode/skills/`. Copy `agents/*.md` into `~/.config/opencode/agents/` to use the Tower definitions. Review `AGENTS.md` before adopting it: these files capture one user's preferences and local assumptions, not universal defaults.

Tower model delegation requires model bindings in OpenChamber. The smoke test verifies active agent discovery and configuration markers, not model behavior. After copying `agents/*.md` into the active global config, run:

```bash
python3 tests/2026-10-09-tower-agent-config-smoke-test.py
```

Validate skill metadata with (requires PyYAML):

```bash
python3 tests/validate-skill-frontmatter.py
```

## License

MIT. See `LICENSE`.
