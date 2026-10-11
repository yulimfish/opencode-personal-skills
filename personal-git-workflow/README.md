# Personal Git Workflow

Git 提交与上游操作前的个人防护规范，补充全局 `AGENTS.md` 的 Git 安全基线。

## 内容结构
1. **提交范围**：提交前核对工作区，暂存后查看 `git diff --cached --name-status`，确认仅含授权文件。
2. **提交文本**：默认使用英文 commit message 和 PR 标题/正文，除非用户指定中文。
3. **计划检查点**：仅适用于使用长期 ledger 的任务；未获授权不提交、不推送。
4. **隐藏本地改动保护**：merge/rebase 前识别 `skip-worktree` 与 `assume-unchanged` 标记，精确备份并恢复内容及索引标记。

## 核心原则
`git status` 看不到被隐藏的工作区改动；禁止用重置或强制覆盖处理它们。

参见 [`SKILL.md`](SKILL.md)。
