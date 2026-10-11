# OpenCode Personal Skills

Personal skill collection for the OpenCode setup. Snapshot date: 2026-10-11.

This catalog covers all **50 skills** currently present in the personal OpenCode skill configuration:

- **18 personal originals** are stored as complete skill folders at `<name>/` in the repository root.
- **32 non-original skills** are not copied; each is listed below with its capability and a link to its original source.

## Personal original skills

| Skill | Capability | Stored file / provenance |
| --- | --- | --- |
| `clarify-before-act` | Resolves costly ambiguity with a focused confirmation before taking a consequential path. | [clarify-before-act/SKILL.md](clarify-before-act/SKILL.md) |
| `execution-economy` | Matches execution, verification, and audit effort to risk; favors the shortest safe path. | [execution-economy/SKILL.md](execution-economy/SKILL.md) |
| `long-term-memory` | Recalls relevant persistent memories and records durable user-approved decisions. | [long-term-memory/SKILL.md](long-term-memory/SKILL.md) |
| `memory-dream` | Consolidates scattered memories and proposes stale-memory cleanup for user confirmation. | [memory-dream/SKILL.md](memory-dream/SKILL.md) |
| `memory-graph-ui` | Opens and explains the local opencode-mem timeline and profile WebUI. | [memory-graph-ui/SKILL.md](memory-graph-ui/SKILL.md) |
| `personal-execution-workflow` | Applies personal execution-economy and tool-call-discipline rules to multi-step work. | [personal-execution-workflow/SKILL.md](personal-execution-workflow/SKILL.md) · extracted from the [root agent contract](https://github.com/Yulimfish/opencode-workflow-kit/blob/main/AGENTS.md) |
| `personal-git-workflow` | Protects commit scope and hidden worktree/index changes during Git operations. | [personal-git-workflow/SKILL.md](personal-git-workflow/SKILL.md) · extracted from the [root agent contract](https://github.com/Yulimfish/opencode-workflow-kit/blob/main/AGENTS.md) |
| `personal-memory-workflow` | Defines when to recall and persist memory, including privacy and deduplication rules. | [personal-memory-workflow/SKILL.md](personal-memory-workflow/SKILL.md) · extracted from the [root agent contract](https://github.com/Yulimfish/opencode-workflow-kit/blob/main/AGENTS.md) |
| `personal-plan-audit-workflow` | Runs a bounded Plan → Build → independent Audit loop for hard and high-risk tasks. | [personal-plan-audit-workflow/SKILL.md](personal-plan-audit-workflow/SKILL.md) · extracted from the [root agent contract](https://github.com/Yulimfish/opencode-workflow-kit/blob/main/AGENTS.md) |
| `personal-release-workflow` | Guides repository releases, distribution registration, privacy, verification, and archival. | [personal-release-workflow/SKILL.md](personal-release-workflow/SKILL.md) · extracted from the [root agent contract](https://github.com/Yulimfish/opencode-workflow-kit/blob/main/AGENTS.md) |
| `personal-session-hygiene` | Keeps context compression deliberate and closes automated browser sessions after use. | [personal-session-hygiene/SKILL.md](personal-session-hygiene/SKILL.md) · extracted from the [root agent contract](https://github.com/Yulimfish/opencode-workflow-kit/blob/main/AGENTS.md) |
| `personal-swarm-workflow` | Coordinates small, independent 2–4-agent work waves and their synthesis. | [personal-swarm-workflow/SKILL.md](personal-swarm-workflow/SKILL.md) · extracted from the [root agent contract](https://github.com/Yulimfish/opencode-workflow-kit/blob/main/AGENTS.md) |
| `post-task-audit` | Requests a fresh-context independent audit after substantial work or a releasable change. | [post-task-audit/SKILL.md](post-task-audit/SKILL.md) |
| `screenshot-to-ui` | Recreates a UI from a reference image through analysis, build, visual diff, and iteration. | [screenshot-to-ui/SKILL.md](screenshot-to-ui/SKILL.md) |
| `swarm-cluster` | Decomposes suitable tasks among parallel subagents and synthesizes their results. | [swarm-cluster/SKILL.md](swarm-cluster/SKILL.md) |
| `tiered-web-search` | Routes web retrieval through quick search, multi-source research, or known-URL fetch. | [tiered-web-search/SKILL.md](tiered-web-search/SKILL.md) · locally authored |
| `tool-call-discipline` | Selects the right tools, parallelizes independent calls, reads broadly, and checks parameters. | [tool-call-discipline/SKILL.md](tool-call-discipline/SKILL.md) |
| `ui-preview-first` | Requires a before/after ASCII wireframe before UI layout or hierarchy changes. | [ui-preview-first/SKILL.md](ui-preview-first/SKILL.md) |

## Non-original skills — source links only

The following skills are present in the local configuration but are authored and maintained elsewhere. Their skill bodies are deliberately not redistributed here; use the linked upstream source and its license terms.

| Skill | Capability | Original source |
| --- | --- | --- |
| `agent-browser` | Automates browser navigation, interaction, screenshots, and page inspection. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/blob/main/skills/agent-browser/SKILL.md) |
| `algorithmic-art` | Creates original generative artwork with seeded randomness and p5.js. | [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/algorithmic-art/SKILL.md) |
| `animate-text` | Selects and implements named text-animation effects from portable motion specs. | [sakuraoxo-clio/sakura-animate-text](https://github.com/sakuraoxo-clio/sakura-animate-text/blob/main/SKILL.md) |
| `animation-vocabulary` | Maps informal descriptions of motion to precise animation terminology. | [emilkowalski/skills](https://github.com/emilkowalski/skills/blob/main/skills/animation-vocabulary/SKILL.md) |
| `apple-design` | Applies gesture, motion, material, typography, and restraint principles to interfaces. | [emilkowalski/skills](https://github.com/emilkowalski/skills/blob/main/skills/apple-design/SKILL.md) |
| `brainstorming` | Clarifies intent and gates design before implementing a feature or architectural change. | [obra/superpowers](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) |
| `brand-guidelines` | Applies Anthropic brand colors, typography, and visual standards. | [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/brand-guidelines/SKILL.md) |
| `design-motion-principles` | Builds purposeful UI motion or audits existing animations against contextual principles. | [kylezantos/design-motion-principles](https://github.com/kylezantos/design-motion-principles/blob/main/skills/design-motion-principles/SKILL.md) |
| `dogfood` | Explores an application systematically and records reproducible UX and functional issues. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/blob/main/skill-data/dogfood/SKILL.md) |
| `electron` | Automates Electron desktop applications through browser automation interfaces. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/blob/main/skill-data/electron/SKILL.md) |
| `executing-plans` | Executes an approved implementation plan with task-level verification and review. | [obra/superpowers](https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md) |
| `figma-implement-design` | Converts Figma designs into production UI while preserving visual fidelity. | [openai/skills](https://github.com/openai/skills/blob/main/skills/.curated/figma-implement-design/SKILL.md) |
| `find-animation-opportunities` | Audits a UI for worthwhile motion opportunities without modifying source code. | [emilkowalski/skills](https://github.com/emilkowalski/skills/blob/main/skills/find-animation-opportunities/SKILL.md) |
| `frontend-design` | Creates distinctive frontend compositions with intentional visual hierarchy. | [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) |
| `frontend-skill` | Designs polished, distinctive frontend pages and application experiences. | [OpenAI's official article containing the original skill](https://developers.openai.com/blog/designing-delightful-frontends-with-gpt-5-4) |
| `impeccable` | Audits and improves frontend UX, hierarchy, typography, layout, accessibility, and polish. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable/blob/main/plugin/skills/impeccable/SKILL.md) |
| `improve-animations` | Produces a prioritized, read-only audit and implementation plans for motion issues. | [emilkowalski/skills](https://github.com/emilkowalski/skills/blob/main/skills/improve-animations/SKILL.md) |
| `internal-comms` | Drafts internal updates, reports, FAQs, incident communications, and leadership notes. | [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/internal-comms/SKILL.md) |
| `review-animations` | Reviews animation code and interaction motion against a high-craft bar. | [emilkowalski/skills](https://github.com/emilkowalski/skills/blob/main/skills/review-animations/SKILL.md) |
| `screenshot` | Captures a desktop, application, window, or screen region. | [openai/skills](https://github.com/openai/skills/blob/main/skills/.curated/screenshot/SKILL.md) |
| `test-driven-development` | Uses the red-green-refactor loop to implement behavior with tests first. | [obra/superpowers](https://github.com/obra/superpowers/blob/main/skills/test-driven-development/SKILL.md) |
| `theme-factory` | Applies or creates visual themes for documents, slides, and web artifacts. | [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/theme-factory/SKILL.md) |
| `web-design-guidelines` | Reviews web UI code for interface quality, accessibility, and best-practice compliance. | [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines/blob/main/command.md) |
| `writing-plans` | Produces concrete, testable implementation plans from approved requirements. | [obra/superpowers](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md) |
| `yuque-personal-daily-capture` | Captures small ideas and organizes them into structured Yuque notes. | [yuque/yuque-plugin](https://github.com/yuque/yuque-plugin/blob/main/plugins/yuque-personal/skills/yuque-personal-daily-capture/SKILL.md) |
| `yuque-personal-knowledge-connect` | Finds relationships between knowledge-base documents and suggests cross-links. | [yuque/yuque-plugin](https://github.com/yuque/yuque-plugin/blob/main/plugins/yuque-personal/skills/yuque-personal-knowledge-connect/SKILL.md) |
| `yuque-personal-note-refine` | Improves rough notes with clearer structure, wording, and formatting. | [yuque/yuque-plugin](https://github.com/yuque/yuque-plugin/blob/main/plugins/yuque-personal/skills/yuque-personal-note-refine/SKILL.md) |
| `yuque-personal-reading-digest` | Extracts key points, quotations, and action items from reading material. | [yuque/yuque-plugin](https://github.com/yuque/yuque-plugin/blob/main/plugins/yuque-personal/skills/yuque-personal-reading-digest/SKILL.md) |
| `yuque-personal-smart-search` | Searches a personal Yuque knowledge base from natural-language questions. | [yuque/yuque-plugin](https://github.com/yuque/yuque-plugin/blob/main/plugins/yuque-personal/skills/yuque-personal-smart-search/SKILL.md) |
| `yuque-personal-smart-summary` | Produces short, bullet, or detailed summaries of a Yuque document or book. | [yuque/yuque-plugin](https://github.com/yuque/yuque-plugin/blob/main/plugins/yuque-personal/skills/yuque-personal-smart-summary/SKILL.md) |
| `yuque-personal-stale-detector` | Finds outdated knowledge-base documents and recommends updates or archiving. | [yuque/yuque-plugin](https://github.com/yuque/yuque-plugin/blob/main/plugins/yuque-personal/skills/yuque-personal-stale-detector/SKILL.md) |
| `yuque-personal-style-extract` | Analyzes writing samples and derives a reusable personal style profile. | [yuque/yuque-plugin](https://github.com/yuque/yuque-plugin/blob/main/plugins/yuque-personal/skills/yuque-personal-style-extract/SKILL.md) |

## Repository links

- **Distribution root:** [Yulimfish/opencode-workflow-kit](https://github.com/Yulimfish/opencode-workflow-kit)
- **Global agent contract:** [`AGENTS.md` in the root kit](https://github.com/Yulimfish/opencode-workflow-kit/blob/main/AGENTS.md)

The root kit installs its ten selected skills from this catalog; external skill bodies remain at their linked upstream sources.

## License

MIT. See `LICENSE`. Only the personal-original skill files are stored here; external skill bodies remain at their linked sources and retain their respective license terms.
