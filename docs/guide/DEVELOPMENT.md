# 开发指南

---

## 环境设置

```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

---

## Python 版本要求

| 版本 | 状态 | 说明 |
|------|------|------|
| 3.9 | ❌ 已结束 | 2025-10-31 结束支持 |
| 3.10 | ⚠️ 安全维护 | 2026-10 结束 |
| 3.11 | ✅ 企业稳定 | 2027-10 结束 |
| **3.12** | ✅ **新项目首选** | 2028-10 结束 |
| 3.13 | ✅ 最新稳定版 | 2029-10 结束 |

> **ByteBrain 选择 Python 3.12**：作为 2026 年的新项目，3.12 是最佳选择——新特性多、性能好、生态成熟、支持到 2028 年。

---

## 开发命令

| 命令 | 说明 |
|------|------|
| `make install` | 安装依赖 |
| `make install-dev` | 安装开发依赖 |
| `make test` | 运行测试 |
| `make lint` | 运行代码检查 |
| `make format` | 格式化代码 |
| `make run` | 启动应用 |

---

## 项目结构

```
bytebrain/
├── core/               # 核心模块
├── skills/             # Skill 系统
├── guardrails/         # 防护系统
├── prompts/            # Prompt 系统
├── ui/                 # UI 模块
└── utils/              # 工具模块
```

---

## 更多

- [设计哲学](../PHILOSOPHY.md)
- [快速开始](./GETTING_STARTED.md)
