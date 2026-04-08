# ByteBrain

> **AI 时代你的第二大脑**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.3+-green.svg)](https://github.com/langchain-ai/langgraph)
[![MCP](https://img.shields.io/badge/MCP-2024--11--05-orange.svg)](https://modelcontextprotocol.io/)

---

## 简介

ByteBrain 是 AI 时代你的第二大脑。帮助你管理和检索个人知识，成为你的"数字分身"。

**设计理念**：大框架支撑格局，小巧思成就细节。

---

## 技术栈

| 技术 | 用途 |
|------|------|
| LangGraph | Agent 工作流编排 |
| MCP | 数据源连接协议 |
| LlamaIndex | RAG 框架 |
| Qdrant/Chroma | 向量数据库 |
| Streamlit | Web UI |

---

## 快速开始

### 安装

```bash
git clone https://github.com/your-username/ByteBrain.git
cd ByteBrain
pip install -e .
```

### 运行

```bash
make run
```

打开浏览器访问 `http://localhost:8501`

---

## 开发

```bash
make install-dev
make test
make lint
make format
```

---

## 文档

- [设计哲学](docs/PHILOSOPHY.md)
- [快速开始](docs/guide/GETTING_STARTED.md)
- [开发指南](docs/guide/DEVELOPMENT.md)

---

## 许可证

MIT License

---

**ByteBrain - 让 AI 成为你的第二大脑**
