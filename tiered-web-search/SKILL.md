---
name: tiered-web-search
description: Search the web in quick, research, or fetch-by-URL mode using only the agent's existing websearch and webfetch tools.
compatibility: Requires the agent runtime to expose the existing websearch and webfetch tools.
---

# Tiered Web Search

Provide three distinct web-retrieval modes with the tools already available in the agent runtime: a fast lookup, a multi-source research workflow, and direct retrieval of a known URL.

## Strict Tool Boundary

- Use only the existing `websearch` and `webfetch` tool calls for web retrieval.
- Never directly invoke an external API or endpoint, send HTTP requests, use an SDK or `curl`, or access API credentials or keys.
- Do not switch to another provider or direct network method if either tool is unavailable. Explain the limitation instead.
- Call tools with their actual supported inputs: `websearch({ query })` and `webfetch({ url })`. Do not invent parameters.

## Choose a Mode

- Use **Quick Search** for a simple fact, a quick lookup, or when the user asks for a brief search.
- Use **Research Search** for comparisons, reports, synthesis, contested claims, or questions that need evidence from multiple sources.
- Use **Fetch by URL** when the user provides a specific URL or asks to read a known page.
- If the user explicitly names a mode, follow it when possible. Otherwise infer the mode from the task; do not ask the user to choose when their intent is clear.

## Mode 1: Quick Search

1. Reduce the request to one focused information need.
2. Form a query with the relevant entity and, where useful, a date, year, version, angle, or source-type qualifier.
3. Call `websearch({ query })` once.
4. Give a concise answer grounded in the returned results and include the relevant source links.
5. If there are no useful results, make at most one materially revised query. If that also fails, say that the available search did not find adequate evidence.

Fetch a result page only when its snippet is insufficient to answer accurately or the user asks for more detail.

## Mode 2: Research Search

Use a bounded, evidence-oriented workflow:

1. Identify the main information need and form a precise first query.
2. Search distinct useful angles or source types with up to two additional non-duplicate queries. Do not issue near-identical synonym searches.
3. If a query yields no useful results, one materially revised query may replace it. Keep the overall search to at most four calls, including any such retry; stop earlier when evidence is sufficient.
4. Select a small set of relevant results. Prefer primary sources, then independent corroboration. Use only metadata actually returned by `websearch`; do not invent authority, ranking, score, date, or other fields.
5. Call `webfetch({ url })` for selected results when their full-page context is needed. Fetch no more than five pages by default, and fewer when the evidence is sufficient.
6. Synthesize the evidence, cite claims with the source URLs, and disclose disagreement, missing information, stale or unavailable dates, and failed or incomplete page retrieval.

### Research Query Guidance

- Keep each query focused on one information need. Combine closely related subquestions instead of issuing redundant searches.
- For time-sensitive topics, include the relevant date, year, or version in the query.
- Add a source-type or angle qualifier when it improves precision.
- A `site:` operator or date phrase is only query text. Do not claim it enforces a structured allowlist or guaranteed date-range filter.
- Evaluate sources using visible relevance, source identity, primary-source status, available recency, and corroboration. The available tools do not provide a guaranteed numeric authority or ranking score; do not manufacture or compare one.

## Mode 3: Fetch by URL

1. Call `webfetch({ url })` directly for the supplied or otherwise known URL.
2. Summarize or extract the requested information from the returned page and link to it.
3. Do not run a broad search first unless the URL is invalid or inaccessible, or the user also asks for related sources.
4. If retrieval fails or omits relevant content, say so. Do not infer or fabricate the missing page content.

## Response and Citation Rules

- Answer in the user's language.
- Lead with the answer; add evidence and source links in proportion to the requested depth.
- Cite only URLs and source details actually returned or fetched.
- Include publication dates only when present in the returned source data or page; never infer them.
- In research answers, distinguish well-supported facts from inference and call out material source conflicts.
- Do not claim exact ranking, authority scores, structured filtering, or content that the tools did not return.

## Failure Handling

| Situation | Response |
| --- | --- |
| Search results are empty or irrelevant | Make at most one materially revised query within the mode's call limit, then report insufficient evidence. |
| A fetched URL fails | Do not fabricate its contents. Use a search-result snippet only if one is already available, and label the limitation; otherwise report the fetch failure. |
| Extracted page content is incomplete | State what could not be retrieved rather than filling gaps with guesses. |
| A source has no visible date or other metadata | Omit the missing field; do not infer it. |
| Required tool is unavailable | Explain that the runtime lacks the needed tool; do not fall back to a direct API or network client. |
