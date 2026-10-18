# 长期记忆

更新时间：2026-10-18

## 已确认需求

- 项目名 Pode；目标是可自部署的 Podcast 软件。
- Go 后端、Vue Web、iOS 和 Android 四端。
- 需要独立设计目录、AI 开发规范、上下文及记忆，每次完成操作后核对并更新。

## 当前工程约定

- 单仓库：`backend/`、`web/`、`ios/`、`android/`。
- 移动端骨架暂选 SwiftUI 和 Kotlin/Compose，这是可调整的初始化选择。
- 根 `AGENTS.md` 是 AI 规则唯一入口，`Agent.md` 仅作兼容索引。
- 尚未确定数据库、认证方案、RSS 刷新策略和音频存储方案，不得当作既定设计。
- `/healthz` 已定义；业务接口尚未实现。

- Git 远程 origin：`git@github.com:batemax/Pode.git`，当前分支 `main`。
