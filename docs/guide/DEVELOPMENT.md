# 开发指南

---

## 环境设置

```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

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
