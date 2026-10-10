---
name: personal-release-workflow
description: "Load when initializing a repository, setting or correcting commit identity/metadata, creating or publishing a package, open-sourcing a project, distributing an agent/CLI, or registering a release in opencode-workflow-kit."
---

# Personal Release Workflow

## Identity and email

| Use | Email | Where it appears |
|---|---|---|
| Commit identity | `<local commit email>` | Local Git author/committer configuration; keep private unless explicitly public |
| Login | `[private login email omitted from public copy]` | GitHub/npm/Yuque backend credentials; **must not** appear in public files, commits, package metadata, or README |
| Public contact | `<public contact email>` | README contact, docs footer, issue |

When initializing a repository or publishing a new package, configure a local commit email without placing a private address in public files. Set the npm `package.json` author name to the current GitHub profile display name. If an email field is public, use the account's current GitHub public email; if none is configured, omit that email rather than substituting a private address. If the email field will not be public, use the local commit email. Refresh profile details when settings change. Never use the login email as public package metadata.

If a commit accidentally uses the login email, set `git config user.email` to the configured local commit email, then run `GIT_AUTHOR_EMAIL=<local commit email> GIT_COMMITTER_EMAIL=<local commit email> git commit --amend --reset-author`. Before publishing, verify both fields with `git show -s --format='%ae' HEAD` and `git show -s --format='%ce' HEAD`; each must match the configured local commit identity. Treat the amend and force-push as Level 3 history rewrites: back up first, explain the impact, and obtain explicit user authorization before either operation; never force-push without authorization. Follow the global Git preflight and `personal-git-workflow` safeguards.

## Release workflow

Trigger phrases include “整理代码并发布 / 开源发布 / publish it / 发个新包 / 发到 kit 里 / 让别人一键装”.

1. **Open source** — Create a public `github.com/<account>/<name>` repository with MIT `LICENSE` and `README.md`; configure the local Git commit identity; commit, push `main`, and tag `v0.1.0` (increment semver if that tag already exists).
2. **Distribution** — Plugin/library with code → `npm publish` (the user must run the 2FA passkey on their own machine; the agent must not run it); pure-Markdown skill → `git clone`; agent Markdown bundle → clone into `~/.config/opencode/agents/`; CLI → npm bin or GitHub Release.
3. **Register in [`opencode-workflow-kit`](https://github.com/Yulimfish/opencode-workflow-kit)** — Add to the `SKILLS` / `PLUGINS` / `AGENT_BUNDLES` arrays in `install.sh`, make the symmetric removal in `uninstall.sh`, and update `README.md` (feature list, contents table, manual-install block); commit and push `main`.
4. **Verify** — `git ls-remote https://github.com/Yulimfish/<repo>.git HEAD` returns a hash; `bash -n install.sh` and `bash -n uninstall.sh` pass.
5. **Archive** — Write `YYYY-MM-DD-<slug>.md` to the workspace and sync it to the configured Yuque repository (follow the project contract's archive rules).
6. **Memory** — Tag with `release`, artifact name, and date.

Working clone: `<local workflow-kit checkout path>`.
