# AI 上下文与记忆

- `Context.md`：当前开发上下文及能力边界。
- `Memory.md`：长期稳定事实（正确拼写为 Memory，不使用 Mermory）。
- `tasks/current.md`：当前任务、状态和验收记录。
- `logs/operations.md`：追加式操作历史。
- `checklists/task-completion.md`：每次操作完成后的核对清单。
- `templates/operation.md`：后续操作记录模板。

事实变更时同时修正上下文和记忆，避免只追加相互矛盾的记录。任务结束必须核对上述文件；没有变化也应在日志中说明。日期使用用户时区；不记录密钥或个人隐私。脚本不调用模型、不写入记忆，仅提供最低限度的结构校验。
