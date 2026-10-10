---
name: memory-graph-ui
description: Use when the user wants to view, open, or check status of the opencode-mem memory WebUI (timeline + user-profile browser at http://127.0.0.1:4747). Trigger phrases include "打开记忆图", "启动记忆 UI", "看一下记忆", "memory ui", "开图谱", "关掉记忆 UI", "记忆服务还开着吗", "看看关系图". opencode-mem starts its WebUI automatically when opencode is running (per opencode-mem.jsonc), so start/stop is really about telling the user the URL, and stop = tell them to quit opencode.
---

# Memory WebUI

The `opencode-mem` plugin embeds its own WebUI. Because it's an in-process HTTP server tied to opencode's lifecycle, it starts automatically when opencode is running (as long as `webServerEnabled: true` in `~/.config/opencode/opencode-mem.jsonc`, which is the default) and stops when opencode exits.

**URL**: `http://127.0.0.1:4747`

## Trigger → response

| User says | Action |
|---|---|
| "打开记忆" / "看图谱" / "启动 memory ui" | Reply: `已在 http://127.0.0.1:4747 (opencode-mem 常驻)。浏览器打开即可。` |
| "关掉" / "停掉那个 web" | Reply: `WebUI 生命周期绑在 opencode 上，退出 opencode 就关掉了。要现在关就 exit opencode。` |
| "还开着吗" / "状态" | `curl -sS http://127.0.0.1:4747/ >/dev/null && echo up \|\| echo down` → if `up`, `在跑 → :4747`; else `没开（opencode 未运行或 opencode-mem 未加载）`。 |

## Anti-patterns

- Do NOT try to `bun run` a separate server — opencode-mem owns the port.
- Do NOT curl the URL to "prove" it works unless the user asks for status.
- Do NOT paste the whole URL in a preamble; keep the response one line.

## Under the hood (reference only)

- Port set in `~/.config/opencode/opencode-mem.jsonc` via `webServerPort`.
- To change port, edit that file and restart opencode.
- Features: memory timeline, user profile viewer, add/delete/tag inline. No graph 3D view — that was our custom prototype; opencode-mem's built-in UI is more feature-complete.
