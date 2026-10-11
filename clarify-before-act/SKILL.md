---
name: clarify-before-act
description: Use before committing to any task that has multiple viable paths with non-trivial trade-offs, ambiguous acceptance criteria, or is destructive. Produces a single-message confirmation with a recommended path, so the user makes one decision instead of watching guesswork unfold. Do NOT use for straightforward tasks — those go straight to execution.
---

# Clarify Before Act

Only invoke this skill when a wrong guess wastes real work. Otherwise, execute.

## Trigger checklist

Invoke if **any** applies:

- **Multiple architectures viable** and choice is hard to reverse (framework, storage, protocol).
- **Ambiguous scope**: user says "clean it up" / "make it better" without a target.
- **Destructive step** on files outside the git worktree, or on the git history itself.
- **New file/module location** where placing it wrong causes rework in 3+ callsites.
- **Cost / rate-limit** implications the user might not have priced in (bulk API calls, big downloads).

Skip if:

- The task has one obvious path.
- You can try-then-adjust cheaply.
- The user already answered the question upstream — check `memory_search` first.

## Output format (single message)

```
【要做的事一句话】

推荐方案：<one line>
理由：<≤ 2 lines>

需要你拍板的：
1. <question>  —— 推荐: <A>（原因半句话）
2. <question>  —— 推荐: <B>
（≤ 3 items. If more, you're over-clarifying.）

如无异议，我就按推荐来。
```

Then **stop**. Do not run tools until user replies. Even a `y` / `👍` / `按推荐来` counts as go.

## Anti-patterns

- Listing every possible option A/B/C/D — pick one, offer it, mention the runner-up in the reason.
- Asking about details the user obviously doesn't care about (name of internal variable, order of arguments).
- Asking permission for reversible actions inside git.
- Bundling 6 questions — pick the 1-3 that actually change the plan.

## Example

Good:
```
要做的事：把 memory 存储从 JSON 换成 SQLite+向量索引。

推荐：SQLite + sqlite-vec，本地文件在 ~/.config/opencode/memory/store.db。
理由：跨会话，零依赖，>1k 条也快。

需要你拍板的：
1. 是否顺便加个 WebUI 关系图？—— 推荐: 是（Bun 自带 http server，30 行代码）

如无异议，我就按推荐来。
```

Bad:
```
你想用什么？
- (a) JSON
- (b) SQLite
- (c) SQLite + vec
- (d) Redis
- (e) 语雀
- (f) 自定义...
```
