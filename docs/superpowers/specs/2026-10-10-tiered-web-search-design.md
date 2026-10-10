# Tiered Web Search Skill Design

## Goal

Create a reusable global OpenCode skill that reproduces the practical capability of a three-mode web-search workflow: quick search, research-oriented search, and fetch by known URL. The skill must use only the existing `websearch` and `webfetch` tool calls available to the agent.

## User Intent and Constraints

- The skill name must not contain `kimi`; use `tiered-web-search`.
- Reproduce comparable user-facing capability through the agent's existing tool interface, without directly invoking any provider API.
- Do not directly call any external API, REST endpoint, SDK, or `curl`; do not request, read, or use API keys.
- Do not claim that native-tool results expose metadata or filters that the tools do not actually return or support.
- Keep the skill global so it is available across projects.
- Add no dependencies, helper scripts, or unrelated features.

## Target

Create:

`~/.config/opencode/skills/tiered-web-search/SKILL.md`

The skill directory does not currently exist. The workspace is not a Git repository. This design document is stored in the workspace using its required date-prefixed filename convention.

## Tool Boundary

The skill may retrieve web content only through the existing agent tools:

- `websearch({ query })` for web search.
- `webfetch({ url, format?, timeout? })` for retrieving a known page.

No direct network client or endpoint calls are permitted. In particular, the design must not invoke provider-specific search APIs, send HTTP requests, use SDKs or `curl`, or access credentials/environment variables for API keys. The article that inspired the workflow is a design reference only; its APIs are not part of this implementation. `websearch` and `webfetch` are the only permitted interfaces for web retrieval.

## Three Modes

### 1. Quick Search

Use one focused `websearch` call for a simple factual question, quick lookup, or when the user explicitly asks for a brief search. Return a concise answer and cite the most relevant returned source links. Fetch a page only when its snippet is insufficient or the user asks for detail.

### 2. Research Search

Use a bounded research workflow when the user asks for comparison, synthesis, a report, or a question requiring evidence from multiple sources:

1. Form one precise query around the main information need.
2. When materially useful, issue up to two additional, non-duplicate queries that cover distinct angles or source types. Do not repeat the same search with near-synonym wording.
3. Select a small set of relevant sources, preferring primary sources and then independent corroborating sources. Use the metadata actually returned by `websearch`; do not invent authority scores, ranking scores, dates, or source fields.
4. Use `webfetch` on selected URLs when full-page context is necessary. By default, fetch no more than five pages; fetch fewer when enough evidence is already available.
5. Synthesize the evidence, cite claims with the retrieved URLs, and disclose disagreement, missing evidence, or failed fetches.

This is a research-oriented orchestration over native tools. It does not reproduce a proprietary relevance-chunking or authority-ranking backend.

### 3. Fetch by URL

When the user provides a specific URL or asks to read a known page, call `webfetch` directly. Summarize or extract the requested information from the retrieved content and cite the page. Do not run a broad search first unless the URL is invalid, inaccessible, or the user separately asks for related sources.

## Mode Selection

- Prefer Fetch by URL for a supplied target URL.
- Prefer Quick Search for a simple lookup or an explicit request for a brief answer.
- Prefer Research Search for comparisons, research, reports, contested claims, or multi-source evidence.
- If the user names a mode, follow it unless the requested operation is impossible with the available tools.
- Do not ask the user to select a mode when their intent already makes the appropriate mode clear.

## Query and Source Strategy

- Include specific entities and, for time-sensitive questions, a date, year, or version where relevant.
- Add an angle or source-type qualifier when it improves precision.
- Keep each query focused on one information need; combine closely related subquestions rather than issuing redundant searches.
- If results are poor, refine with a missing entity, time qualifier, or genuinely different angle. Do not send a near-identical query.
- A `site:` operator or date phrase in the query is only a search hint. The current tool interface does not expose structured site allowlists or guaranteed date-window filters, so do not claim that such filtering is enforced.
- Rank evidence using visible relevance, source identity, primary-source status, available recency, and corroboration. Do not compare nonexistent numeric scores.
- Cite only URLs and source details actually returned or fetched. If a publication date is absent, omit it rather than infer it.

## Error Handling and Honesty

- If `websearch` returns no useful results, make at most one materially revised query. If it still fails, report that the search did not find adequate evidence.
- If `webfetch` fails, do not fabricate page contents. Use a search result snippet only when available and clearly label the limitation.
- If a page omits relevant content or media, state that the available extraction was incomplete.
- If either required tool is unavailable in the runtime, explain the limitation instead of switching to direct API calls or pretending the work succeeded.
- Answer in the user's language and separate supported facts from inference.

## Non-goals

- Calling the source article's search or fetch APIs, or any other external API.
- Reproducing exact backend ranking, relevance chunks, authority metadata, or guaranteed structured site/date filters.
- Installing dependencies, asking for API credentials, or creating helper scripts.

## Verification Plan

- Confirm the skill has the exact name `tiered-web-search` and documents only the available `websearch` and `webfetch` tools.
- Inspect the final skill for accidental API/credential/`curl` instructions and unsupported claims about ranking or filters.
- Exercise Quick Search, Research Search, and Fetch by URL using only the existing tool calls; verify citations come from returned sources and failures are disclosed.
- Run the required independent read-only audit before delivery because this is a reusable skill artifact.
