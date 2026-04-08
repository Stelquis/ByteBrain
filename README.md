# ByteBrain

> **AI 时代你的智能助手 / 数字分身**
> 
> 一个基于 RAG 和 Multi-Agent 的个人知识管理系统，同时也是 AI 技术的实战试验场

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.3+-green.svg)](https://github.com/langchain-ai/langgraph)
[![MCP](https://img.shields.io/badge/MCP-2024--11--05-orange.svg)](https://modelcontextprotocol.io/)

---

## 🎯 项目定位

ByteBrain 不仅仅是一个项目，它有三重价值：

### 1. 实用价值：你的"第二大脑"
- 上传你的 Markdown 笔记，构建个人知识库
- 语义检索，找到真正相关的内容
- 知识图谱，看到知识之间的联系
- 主动推荐，发现你可能感兴趣的内容

### 2. 学习价值：AI 技术试验场
在解决真实问题中掌握 2026 年最火的 AI 技术：
- **Agent 框架**：LangGraph、CrewAI
- **RAG 技术**：LlamaIndex、向量数据库
- **AI 协议**：MCP (Model Context Protocol)
- **工程化**：Docker、CI/CD、监控

### 3. 简历价值：企业级技术栈
掌握企业最需要的 AI 技能：
- RAG 系统（企业知识库、智能客服）
- Agent 开发（自动化工作流）
- MCP 协议（AI 工具集成）
- 向量数据库（语义搜索）

---

## ✨ 核心功能

### 📚 知识管理
- 支持 Markdown 文件上传
- 自动向量化存储
- 语义检索与关键词检索混合
- 知识溯源与引用

### 🤖 智能问答
- 基于你的笔记回答问题
- 多级解释（入门/进阶/专家）
- 追问引导，深入理解
- 代码示例与常见错误

### 🔗 数据连接（MCP）
- 连接本地文件系统
- 连接云笔记工具（Notion、Obsidian）
- 连接代码仓库（GitHub）
- 标准化数据接入

### 🧠 Multi-Agent 协作
- 知识整理 Agent：自动分类、打标签
- 知识问答 Agent：检索 + 解释 + 引用
- 知识扩展 Agent：推荐相关内容
- 学习规划 Agent：个性化学习路径

---

## 🏗️ 技术架构

```
┌─────────────────────────────────────────────────────────────┐
│                    用户界面层 (Streamlit)                    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   Agent 协调层 (LangGraph)                   │
│  • 知识整理 Agent  • 问答 Agent  • 推荐 Agent  • 规划 Agent  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                    RAG 检索层 (LlamaIndex)                   │
│  • 混合检索  • 重排序  • 知识溯源  • 语义缓存                 │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                  数据存储层 (Qdrant/Chroma)                  │
│  • 向量存储  • 元数据管理  • 知识图谱                        │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                    MCP 协议层                                │
│  • 文件系统连接  • 云笔记连接  • 代码仓库连接                 │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 快速开始

### 环境要求
- Python 3.9+
- 8GB+ RAM（推荐 16GB）
- 可选：NVIDIA GPU（用于本地模型推理）

### 安装步骤

```bash
# 克隆项目
git clone https://github.com/your-username/ByteBrain.git
cd ByteBrain

# 安装依赖
pip install -r requirements.txt

# 启动应用
streamlit run app.py --server.address 127.0.0.1 --server.port 8501
```

### 上传你的笔记

1. 打开浏览器访问 `http://127.0.0.1:8501`
2. 点击"上传笔记"按钮
3. 选择你的 Markdown 文件或文件夹
4. 等待向量化完成
5. 开始提问！

---

## 📖 技术文档

| 文档 | 说明 |
|------|------|
| [设计哲学](./docs/DESIGN_PHILOSOPHY.md) | 项目的核心理念与设计原则 |
| [需求分析](./docs/NEEDS_ANALYSIS_2026.md) | 2026 年 AI 学习领域的痛点分析 |
| [功能规划](./docs/PRODUCT_FEATURES.md) | 详细的功能设计与实现方案 |
| [技术试验场](./docs/TECH_PLAYGROUND_2026.md) | 2026 年热门 AI 技术全景 |
| [项目定位](./docs/PROJECT_POSITIONING.md) | 项目的三重价值体系 |
| [Agent 策略](./docs/AI_AGENT_STRATEGY.md) | MCP、Skill、Agent 的应用方案 |
| [知识库标准](./docs/KNOWLEDGE_BASE_GUIDELINE.md) | 知识库内容的标准与示例 |

---

## 🛠️ 技术栈

### 核心技术
| 领域 | 技术 | 版本 |
|------|------|------|
| Agent 框架 | LangGraph | 0.3+ |
| RAG 框架 | LlamaIndex | 0.12+ |
| 向量数据库 | Qdrant / Chroma | latest |
| AI 协议 | MCP | 2024-11-05 |
| 大模型框架 | LangChain | 0.3+ |
| Web 框架 | Streamlit | 1.24+ |

### 可选组件
| 组件 | 用途 |
|------|------|
| Ollama | 本地模型推理 |
| LangSmith | 监控与调试 |
| Docker | 容器化部署 |

---

## 📊 项目进展

### 已完成 ✅
- [x] 基础 RAG 检索
- [x] Streamlit 界面
- [x] 设计哲学文档
- [x] 需求分析文档
- [x] 技术试验场规划

### 进行中 🚧
- [ ] MCP 协议集成
- [ ] LangGraph Agent 系统
- [ ] 向量数据库优化

### 计划中 📋
- [ ] 多 Agent 协作
- [ ] 知识图谱可视化
- [ ] 云笔记工具集成
- [ ] 开源发布

---

## 🤝 贡献指南

欢迎贡献！请查看 [贡献指南](./CONTRIBUTING.md) 了解详情。

### 贡献方式
- 提交 Issue 报告 Bug 或提出新功能
- 提交 Pull Request 修复 Bug 或添加功能
- 完善文档
- 分享你的使用经验

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

- [LangChain](https://github.com/langchain-ai/langchain) - LLM 应用框架
- [LlamaIndex](https://github.com/run-llama/llama_index) - RAG 框架
- [Qdrant](https://github.com/qdrant/qdrant) - 向量数据库
- [MCP](https://modelcontextprotocol.io/) - AI 协议标准
- [Streamlit](https://streamlit.io/) - Web 框架

---

## 📞 联系方式

- 项目主页：[GitHub](https://github.com/your-username/ByteBrain)
- 问题反馈：[Issues](https://github.com/your-username/ByteBrain/issues)

---

**ByteBrain - 让 AI 成为你知识的延伸**
