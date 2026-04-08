# ByteBrain

> **AI 时代你的第二大脑**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.3+-green.svg)](https://github.com/langchain-ai/langgraph)
[![MCP](https://img.shields.io/badge/MCP-2024--11--05-orange.svg)](https://modelcontextprotocol.io/)
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-0.10+-purple.svg)](https://github.com/run-llama/llama_index)

---

## 简介

ByteBrain 是 AI 时代你的第二大脑，一个功能强大的个人知识管理和智能助手系统。它利用先进的 AI 技术，帮助你管理、检索和利用个人知识，成为你的"数字分身"。

**设计理念**：大框架支撑格局，小巧思成就细节。

---

## 核心功能

### 🧠 知识管理
- **智能检索**：基于 RAG 技术的语义搜索，快速找到相关知识
- **知识组织**：自动分类和标签化，构建个人知识图谱
- **多源集成**：支持本地文件、云笔记、代码仓库等多种数据源

### 🤖 AI 助手
- **多 Agent 协作**：协调者、知识专员、代码教练、概念导师协同工作
- **技能系统**：基于 Anthropic Skills 标准的可扩展技能体系
- **智能对话**：理解上下文，提供连贯的对话体验

### 🔒 安全防护
- **输入防护**：Prompt Injection 检测、PII 过滤
- **输出防护**：幻觉检测、事实核查、来源验证
- **行为防护**：操作审计、权限控制、合规检查

### 📊 数据分析
- **知识洞察**：分析知识结构和使用模式
- **学习推荐**：基于使用习惯推荐相关知识
- **性能监控**：系统运行状态和性能指标

---

## 使用场景

### 👨‍💻 开发者
- **代码知识库**：管理代码片段、API 文档、技术博客
- **学习助手**：解释复杂概念，提供编程建议
- **项目管理**：跟踪项目进展，管理技术债务

### 🎓 学生/研究者
- **学习笔记**：整理课程材料，生成复习大纲
- **文献管理**：组织论文和研究资料，提取关键信息
- **创意助手**：激发灵感，辅助写作和研究

### 💼 专业人士
- **知识管理**：构建行业知识库，跟踪市场动态
- **决策支持**：提供数据驱动的决策建议
- **个人品牌**：管理专业内容，提升个人影响力

---

## 技术栈

| 技术 | 用途 | 版本 |
|------|------|------|
| **LangGraph** | Agent 工作流编排 | 0.3+ |
| **LlamaIndex** | RAG 框架 | 0.10+ |
| **MCP** | 数据源连接协议 | 2024-11-05 |
| **Qdrant/Chroma** | 向量数据库 | 1.5+ |
| **Streamlit** | Web UI | 1.30+ |
| **Python** | 开发语言 | 3.12+ |

---

## 快速开始

### 前置要求
- Python 3.12+（2026 年新项目首选）
- 8GB+ RAM（推荐 16GB）
- 足够的磁盘空间用于向量数据库存储

### 安装

```bash
git clone https://github.com/your-username/ByteBrain.git
cd ByteBrain
# 安装基础依赖
pip install -e .
# 安装开发依赖（可选）
pip install -e "[dev]"
```

### 配置

1. **环境变量配置**：
   - 复制 `.env.example` 文件为 `.env`
   - 填写必要的配置信息（如 API 密钥等）

2. **数据源配置**：
   - 在 `config.yaml` 中配置 MCP 服务器
   - 添加你想要集成的数据源

### 运行

```bash
# 启动应用
make run

# 或者直接运行
streamlit run bytebrain/ui/streamlit_app.py
```

打开浏览器访问 `http://localhost:8501`

---

## 开发指南

### 开发命令

| 命令 | 说明 |
|------|------|
| `make install` | 安装基础依赖 |
| `make install-dev` | 安装开发依赖 |
| `make test` | 运行测试套件 |
| `make lint` | 运行代码检查 |
| `make format` | 格式化代码 |
| `make run` | 启动应用 |

### 项目结构

```
bytebrain/
├── core/               # 核心模块
│   ├── agent.py        # Agent 核心逻辑
│   ├── rag.py          # RAG 核心逻辑
│   └── workflow.py     # 工作流定义
├── skills/             # Skill 系统
│   ├── knowledge-retrieval/  # 知识检索技能
│   ├── code-coaching/        # 代码教练技能
│   └── concept-explanation/  # 概念解释技能
├── guardrails/         # 防护系统
│   ├── input_guard.py  # 输入防护
│   ├── output_guard.py # 输出防护
│   └── behavior_guard.py # 行为防护
├── prompts/            # Prompt 系统
│   ├── system/         # 系统提示
│   └── skill/          # 技能提示
├── ui/                 # UI 模块
│   └── streamlit_app.py # Streamlit 应用
└── utils/              # 工具模块
    ├── config.py       # 配置管理
    └── logger.py       # 日志管理
```

---

## API 概览

### 核心 API

```python
# 初始化 ByteBrain
from bytebrain.core import ByteBrain

brain = ByteBrain()

# 提问
response = brain.ask("什么是 LangGraph？")
print(response)

# 检索知识
results = brain.retrieve("Python 设计模式")
print(results)

# 添加知识
brain.add_knowledge("path/to/document.pdf")

# 执行技能
result = brain.execute_skill("code-coaching", {"code": "def hello(): print('Hello')"})
print(result)
```

### Web API

ByteBrain 提供 RESTful API 接口，支持远程调用：

- `POST /api/ask` - 发送问题并获取回答
- `POST /api/retrieve` - 检索知识
- `POST /api/add` - 添加知识
- `POST /api/skill` - 执行技能

---

## 文档

- [设计哲学](docs/PHILOSOPHY.md) - 详细的设计理念和技术架构
- [快速开始](docs/guide/GETTING_STARTED.md) - 详细的安装和配置指南
- [开发指南](docs/guide/DEVELOPMENT.md) - 开发者详细指南
- [API 文档](docs/API.md) - 完整的 API 参考
- [使用示例](docs/examples/) - 各种使用场景的示例

---

## 贡献

我们欢迎社区贡献！请参考 [CONTRIBUTING.md](.github/CONTRIBUTING.md) 了解如何参与开发。

### 贡献流程
1. Fork 仓库
2. 创建特性分支
3. 提交更改
4. 运行测试
5. 提交 Pull Request

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 路线图

### 近期计划
- [ ] 支持更多数据源集成
- [ ] 增强多语言支持
- [ ] 优化性能和可靠性
- [ ] 完善文档和示例

### 长期愿景
- [ ] 支持个性化学习路径
- [ ] 集成更多专业领域知识
- [ ] 提供企业级部署方案
- [ ] 构建开源社区生态

---

**ByteBrain - 让 AI 成为你的第二大脑**
