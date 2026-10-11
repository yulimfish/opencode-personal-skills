---
name: personal-swarm-workflow
description: "Load when coordinating 2–4 parallel subagents for independent work, multi-perspective synthesis, or when the user asks for a swarm/parallel agents. Do not use for one-file edits, one-off queries, or strictly sequential tasks."
---

# Personal Swarm Workflow

## When to use

Use 2–4 parallel subagents for complex or high-quality critical work when it can be split into at least two independent tasks, when multiple perspectives need to converge, or when the user says “开启集群/并行/分头/swarm/cluster it”. Do not use for a one-file edit, a one-off query, or a strictly sequential task.

## Coordination

- Dispatch up to 4 `task` calls in one message. On HTTP 429, halve to 2 and then proceed serially. Maximum 4 workers per wave; no nested swarms.
- Default worker: `swarm-worker` (inherits the main model). Use `explore`, `general`, or `goal-verify` as appropriate.
- Use `swarm-synth` only when at least 3 workers disagree or their output is too long to synthesize directly.
- If the user asks for a specific model to perform a task, map it to `agents/swarm-worker-<name>.md`.
- Synthesize results in this order: consensus > majority > highest confidence.
- On failure, record the missing information as `BLOCKED:`; do not retry more than once with a halved worker count.
- Detailed swarm mechanics are also covered by `swarm-cluster`.
