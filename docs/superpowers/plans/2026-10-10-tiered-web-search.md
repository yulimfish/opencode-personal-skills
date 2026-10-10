# Tiered Web Search Implementation Plan

> **For agentic workers:** Use the installed `swarm-cluster` skill for approved parallel work, or follow the current environment's in-session plan execution workflow. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a global `tiered-web-search` OpenCode skill that provides quick search, research search, and fetch-by-URL workflows using only the agent's existing tools.

**Architecture:** One Markdown skill file with YAML frontmatter. It routes user intent to `websearch` and/or `webfetch`, gives bounded query and source-selection rules, and explicitly describes unsupported backend features rather than simulating unavailable metadata.

**Tech Stack:** OpenCode skill Markdown/frontmatter; existing `websearch({ query })` and `webfetch({ url, format?, timeout? })` tools only.

**Spec:** `docs/superpowers/specs/2026-10-10-tiered-web-search-design.md`

## Global Constraints

- Skill name: `tiered-web-search` (must not contain `kimi`).
- Use only the existing `websearch` and `webfetch` tool interfaces for web retrieval.
- Do not directly call any external API, REST endpoint, SDK, or `curl`; do not request, read, or use API keys.
- Do not claim that native-tool results expose metadata or filters that the tools do not actually return or support.
- Install globally at `~/.config/opencode/skills/tiered-web-search/SKILL.md`.
- Add no dependencies, helper scripts, or unrelated features.

## Review Focus

1. Empty or weak search results: the skill makes at most one materially revised query, then reports insufficient evidence. Verify with the no-results handling review in Task 2.
2. Missing or uncertain dates/authority/rank metadata: the skill does not fabricate fields or numeric scores. Verify by inspecting source-selection and citation rules in Task 2.
3. `site:` and date phrases: they are described as query hints, not guaranteed filters. Verify by checking the limitation language in Task 2.
4. Conflicting sources: the final answer identifies the disagreement and cites both sources. Verify with the research-mode smoke test in Task 2.
5. Fetch failures or incomplete page extraction: the skill does not invent page contents and discloses the limitation. Verify by inspecting the fetch error path in Task 2.

---

### Task 1: Create the Global Skill

**Files:**
- Create: `~/.config/opencode/skills/tiered-web-search/SKILL.md`

**Interfaces:**
- Consumes: `websearch({ query })`; `webfetch({ url, format?, timeout? })`.
- Produces: a skill named `tiered-web-search` with three user-facing modes: Quick Search, Research Search, and Fetch by URL.

- [x] **Step 1: Create the skill directory and `SKILL.md`**

  Add OpenCode-compatible YAML frontmatter with the exact skill name and a concise description. Document mode selection, the three workflows, query/source rules, bounded retries, citation behavior, limitations, and honest failure handling from the approved spec.

- [x] **Step 2: Enforce the tool boundary in the skill instructions**

  State that `websearch` and `webfetch` are the only web-retrieval interfaces. Do not include direct endpoint URLs, HTTP-client instructions, SDK usage, `curl`, credential access, or API-key environment variables.

### Task 2: Verify the Skill Behavior

**Files:**
- Read: `~/.config/opencode/skills/tiered-web-search/SKILL.md`

**Interfaces:**
- Consumes: Task 1's skill and the existing `websearch` / `webfetch` tools.
- Produces: structural and tool-only evidence for all three modes and the five Review Focus cases.

- [x] **Step 1: Check the skill structure and constraints**

  Read the full file. Confirm the frontmatter name is exactly `tiered-web-search`, all three modes and error paths are present, and all web retrieval instructions route only through the two allowed tools. Inspect for unsupported claims about ranking, authority, or structured filters.

- [x] **Step 2: Smoke-test Quick Search using `websearch` only**

  Use a simple factual query. Confirm the workflow uses one focused query, returns a concise answer, and cites only links actually returned by the tool.

- [x] **Step 3: Smoke-test Research Search using `websearch` and `webfetch`**

  Use a comparison question. Confirm searches cover distinct angles rather than near-duplicate wording, selected pages are fetched only when useful, and any source disagreement is surfaced with citations.

- [x] **Step 4: Smoke-test Fetch by URL using `webfetch` only**

  Fetch `https://www.iana.org/domains/reserved` directly. Confirm no broad search is made first and the response is grounded in the retrieved page.

- [x] **Step 5: Review failure and metadata edge cases**

  Inspect the written no-results, missing-metadata, failed-fetch, and incomplete-extraction behavior. Confirm the skill neither fabricates content nor treats `site:`/date query text as a guaranteed filter.

### Task 3: Independent Audit and Fixes

**Files:**
- Read-only audit: `~/.config/opencode/skills/tiered-web-search/SKILL.md`
- Possible fix: the same skill file only.

**Interfaces:**
- Consumes: the implemented skill and Task 2 verification evidence.
- Produces: a fresh-context `goal-verify` audit verdict; fix any blocker/major findings and re-audit if needed.

- [x] **Step 1: Run an independent read-only audit**

  Provide the original user request, the approved spec, the skill path, and the no-direct-API constraint. Audit completeness, logical correctness, edge cases, tool compatibility, verification coverage, and actual tool-only runtime evidence.

- [x] **Step 2: Resolve findings and confirm final state**

  Fix any BLOCKER findings and inexpensive MAJOR findings; run the affected targeted checks and obtain a final PASS. Do not stage or commit because no Git repository is present and no commit was requested.

## Verification Results

- Skill discovery/load: `tiered-web-search` loaded successfully from its installed path.
- Structure and boundary: frontmatter contains `name: tiered-web-search`; full-file review confirmed all three modes. A targeted scan for URLs, credentials, `curl`, SDKs, and authorization found only the negative prohibition at the tool-boundary paragraph; no endpoint or credential instructions are present.
- Quick Search used `websearch` with `Python 3.13 release date official Python.org`. Results mixed the series' first stable release and later maintenance releases, so a materially more specific query, `Python 3.13.0 stable release date official python.org`, was used. The official Python.org result identified the stable `Python 3.13.0` release date as Oct. 7, 2024.
- Research Search used two distinct queries: `IETF RFC 9112 HTTP/1.1 message syntax persistent connections` and `IETF RFC 9113 HTTP/2 multiplexed streams binary framing`. The official RFC sources were fetched from `https://www.rfc-editor.org/rfc/rfc9112.html` and `https://www.rfc-editor.org/rfc/rfc9113.html`; results supported the comparison of HTTP/1.1 message syntax/persistent connections with HTTP/2 binary framing/multiplexed streams. No source conflict surfaced in this smoke test.
- Fetch by URL called `webfetch` directly on `https://www.iana.org/domains/reserved`; it returned the IANA-managed Reserved Domains page without a preceding search.
- Error and metadata edge cases (empty results, missing fields, failed/incomplete fetch, and `site:`/date hints) were checked against the written instructions. Fault injection was not performed; these runtime failure branches remain statically reviewed only.
- The initial independent audit returned PASS with one MINOR finding requesting this verification evidence be recorded here. This section addressed it. A fresh final audit then returned PASS with BLOCKER 0, MAJOR 0, MINOR 0.
