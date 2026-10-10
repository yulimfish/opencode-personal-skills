---
name: personal-session-hygiene
description: "Load when changing context-compaction settings, deciding when to compress context, or using agent-browser (or another automated browser) so sessions are cleaned up correctly."
---

# Personal Session Hygiene

## Context compression

- Do not compress too early or too often; preserve context quality.
- In `dcp.jsonc`, `maxContextLimit="85%"` and `minContextLimit="50%"`; limits adapt to `model.limit.context` percentages. `modelMaxLimits` uses per-model overrides keyed by `providerId/modelId`.
- **Do not change back to fixed absolute limits**; small-context models would never trigger compression. Consider compression at about 85% context usage.

## Automated browser sessions

When using `agent-browser` or an equivalent automated browser, always close the session when the task ends; do not leave it idle overnight.

- Close one session with `agent-browser --session <name> close`; close all with `agent-browser close --all`.
- If `agent-browser doctor` recommends `close`, execute that recommendation.
- A stale session can leave Chrome in a Mojo IPC busy loop (full receiver queue → zero-timeout retries without backoff), consuming a full CPU core. Close stale automation sessions promptly; investigate any sustained browser CPU usage using the current project's incident records.
