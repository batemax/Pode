# Pode

面向自部署的 Podcast 软件，使用 Go 后端、Vue Web 前端、SwiftUI iOS 客户端和 Kotlin/Compose Android 客户端。

当前阶段：仓库骨架。提供健康检查 API 和 Web 欢迎页；订阅、播放、同步、认证和数据存储尚未实现。移动端为源码起点，尚未包含可直接构建的 Xcode/Gradle 工程。

## 目录

| 目录 | 用途 |
| --- | --- |
| `backend/` | Go API、业务逻辑、存储、数据库迁移 |
| `web/` | Vue 3 + TypeScript + Vite |
| `ios/` | SwiftUI 源码和原生工程说明 |
| `android/` | Kotlin/Compose 源码和原生工程说明 |
| `design/` | 产品、交互、视觉、原型及资源 |
| `docs/` | 架构、接口、开发规范和决策记录 |
| `.ai/` | AI 上下文、记忆、任务记录和检查清单 |
| `deploy/` | 自部署配置 |
| `scripts/` | 开发与 AI 记忆检查脚本 |

## 本地启动

1. 安装 Go 1.22+、Node.js 22+ 和 npm。
2. `cp .env.example .env`（Compose 自动读取；直接启动 Go 时应自行导出环境变量）。
3. `cd backend && go run ./cmd/server`，默认监听 `:8080`。
4. 在另一个终端执行 `cd web && npm install && npm run dev`，访问终端输出的地址。
5. `curl http://localhost:8080/healthz` 检查后端。

Vite 将 `/api` 和 `/healthz` 代理至后端；正式部署的反向代理配置后续补充。

## 容器启动后端

`docker compose -f deploy/compose.yaml --env-file .env up --build`

当前仅启动后端，无持久化数据；完整生产部署仍待实现。

## 开发与 AI 协作

先阅读 [AGENTS.md](AGENTS.md)、[开发规范](docs/development/standards.md) 和 [.ai/Context.md](.ai/Context.md)。每次完成操作后核对并更新记忆，再运行 `python3 scripts/check_ai_memory.py`。详见 [.ai/README.md](.ai/README.md)。
