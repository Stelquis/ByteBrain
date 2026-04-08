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

## 设计哲学

### 核心理念

**大框架与小巧思的辩证统一**

- **大框架决定上限**：Agent、LangGraph、MCP、RAG
- **小巧思决定下限**：Skill、Prompt、Guardrails、Rules

> 伟大的系统，必有宏大的架构支撑格局，也必有精微的细节成就体验。

### 五大原则

1. **知识优先** - AI 只是手段，知识才是目的
2. **诚实可信** - 知之为知之，不知为不知
3. **因材施教** - 不同的人，不同的学习方式
4. **实践导向** - 纸上得来终觉浅，绝知此事要躬行
5. **简洁优雅** - 如无必要，勿增实体

---

## 技术架构

### 整体架构

```
┌─────────────────────────────────────────────────────────────┐
│                      用户界面层                              │
│                    (Streamlit UI)                           │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   Agent 编排层                               │
│                    (LangGraph)                              │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │协调者   │ │知识专员 │ │代码教练 │ │概念导师 │           │
│  │Agent    │ │Agent    │ │Agent    │ │Agent    │           │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘           │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   Skill 能力层                               │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│  │知识检索      │ │概念解释      │ │代码教练      │        │
│  │Skill         │ │Skill         │ │Skill         │        │
│  └──────────────┘ └──────────────┘ └──────────────┘        │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   RAG 检索层                                 │
│              (LlamaIndex + Qdrant)                          │
│  混合检索 → 重排序 → 知识溯源                               │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   MCP 协议层                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │文件系统  │ │云笔记    │ │代码仓库  │ │网络资源  │       │
│  │MCP       │ │MCP       │ │MCP       │ │MCP       │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   Guardrails 防护层                          │
│  输入防护 → 输出防护 → 行为防护                             │
└─────────────────────────────────────────────────────────────┘
```

### 数据流程

```
用户输入
    ↓
┌─────────────────────────────┐
│    Input Guardrails         │
│  • Prompt Injection 检测    │
│  • PII 过滤                 │
│  • 话题边界检查             │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│    Context Engineering      │
│  • 加载系统提示             │
│  • RAG 检索知识上下文       │
│  • 加载用户历史             │
│  • 选择 Few-Shot 示例       │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│    Agent Orchestration      │
│  (LangGraph 工作流)         │
│  理解意图 → 规划步骤 → 执行 │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│    Skill Execution          │
│  调用专业 Skill 执行任务    │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│    Output Guardrails        │
│  • 幻觉检测                 │
│  • 事实核查                 │
│  • 来源验证                 │
│  • 格式校验                 │
└──────────────┬──────────────┘
               ↓
用户输出
```

---

## 技术选型

### Agent 框架选型

根据 2026 年最新的企业实践和框架对比分析：

| 框架 | 设计哲学 | 适用场景 | 企业采用率 |
|------|---------|---------|-----------|
| **LangGraph** | 图结构状态机 | 复杂工作流、精确控制 | ⭐⭐⭐⭐⭐ |
| **CrewAI** | 角色驱动团队 | 快速原型、业务流程 | ⭐⭐⭐⭐ |
| **AutoGen** | 对话驱动协作 | 研究场景、多Agent对话 | ⭐⭐⭐⭐ |

**ByteBrain 选择 LangGraph**：
- ✅ 生产级可靠性（99.5% 成功率）
- ✅ 精确的状态管理和控制流
- ✅ 内置检查点和故障恢复
- ✅ LangSmith 可视化调试
- ✅ 最大的生态系统（100K+ GitHub Stars）

### RAG 技术栈

根据 Stanford AI Index 研究，RAG 系统可减少 **68% 幻觉率**：

| 组件 | 推荐方案 | 说明 |
|------|---------|------|
| **向量数据库** | Qdrant / Chroma | 高性能、开源、易部署 |
| **检索策略** | 混合检索 | 语义检索 + BM25 关键词 |
| **RAG 框架** | LlamaIndex | RAG 专用，性能优化好 |
| **重排序** | BGE-Reranker | 提升检索精度 |

### MCP (Model Context Protocol)

MCP 是 2026 年最火的 AI 协议：

- **97 million** SDK downloads
- **13,000+** MCP servers on GitHub
- **28%** Fortune 500 公司已实施
- Gartner 预测：2026 年底 **75%** API 网关将支持 MCP

**MCP 三大原语**：
1. **Tools** - AI 可调用的函数
2. **Resources** - AI 可读取的数据
3. **Prompts** - 可复用的提示模板

### Guardrails 安全防护

企业级 AI 应用必备的安全层：

| 防护类型 | 功能 | 工具 |
|---------|------|------|
| **输入防护** | Prompt Injection 检测、PII 过滤 | Llama Guard |
| **输出防护** | 幻觉检测、事实核查 | 自定义验证 |
| **行为防护** | 操作审计、权限控制 | Rules Engine |

---

## Agent 团队设计

### 多 Agent 协作架构

根据 Forrester Research (2025)，多 Agent 系统比单一 Agent 快 **3.2 倍** 完成工作流，每笔交易成本降低 **40%**。

```
┌─────────────────────────────────────────────────────────────┐
│                    ByteBrain Agent 团队                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🎯 协调者 Agent (Orchestrator)                             │
│     职责：理解意图、分配任务、整合结果                       │
│     思考："用户真正想要什么？需要哪些专家协作？"             │
│                                                             │
│  📚 知识专员 Agent (Knowledge Specialist)                   │
│     职责：检索知识、验证来源、标注可信度                     │
│     思考："知识库里有答案吗？来源可靠吗？"                   │
│                                                             │
│  💻 代码教练 Agent (Code Coach)                             │
│     职责：解释代码、审查问题、提供示例                       │
│     思考："这段代码有什么问题？如何改进？"                   │
│                                                             │
│  🧠 概念导师 Agent (Concept Mentor)                         │
│     职责：解释概念、类比比喻、循序渐进                       │
│     思考："用户能理解吗？需要什么类比？"                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### LangGraph 工作流示例

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

class ByteBrainState(TypedDict):
    query: str
    intent: str
    knowledge: list
    response: str
    sources: list

def build_bytebrain_graph():
    graph = StateGraph(ByteBrainState)
    
    # 添加节点
    graph.add_node("understand_intent", understand_intent)
    graph.add_node("retrieve_knowledge", retrieve_knowledge)
    graph.add_node("check_boundary", check_boundary)
    graph.add_node("generate_response", generate_response)
    graph.add_node("validate_output", validate_output)
    
    # 定义边
    graph.set_entry_point("understand_intent")
    graph.add_edge("understand_intent", "retrieve_knowledge")
    graph.add_edge("retrieve_knowledge", "check_boundary")
    
    # 条件分支
    graph.add_conditional_edges(
        "check_boundary",
        decide_next_step,
        {
            "generate": "generate_response",
            "unknown": END
        }
    )
    
    graph.add_edge("generate_response", "validate_output")
    graph.add_edge("validate_output", END)
    
    return graph.compile()
```

---

## Skill 系统设计

### Skill 结构规范

基于 Anthropic Skills 标准：

```
skills/
├── knowledge-retrieval/
│   ├── SKILL.md          # 核心指令文件
│   ├── scripts/          # 可执行脚本
│   └── docs/             # 参考文档
├── code-coaching/
│   └── SKILL.md
├── concept-explanation/
│   └── SKILL.md
└── exercise-generation/
    └── SKILL.md
```

### SKILL.md 规范

```markdown
---
name: knowledge-retrieval
version: 1.0.0
description: 从知识库检索信息并生成回答
triggers:
  - user_question
  - search_request
---

# Knowledge Retrieval Skill

## Purpose
从用户的知识库中检索相关信息，生成准确、可溯源的回答。

## Workflow
1. 分析问题 → 提取关键词和实体
2. 检索知识 → 混合检索 + 重排序
3. 生成回答 → 标注来源

## Constraints
- 只使用知识库中的信息
- 必须标注来源
- 置信度 < 0.7 时告知用户
```

---

## Prompt 工程最佳实践

### 2026 年 Prompt 设计原则

根据实测数据，良好的 Prompt 工程可以：
- Chain-of-Thought 提升 **23%** 推理准确率
- Few-Shot 示例提升 **31%** 任务遵循度
- Self-Consistency 提升 **12%** 准确率

### 4-Block 模板

```markdown
## INSTRUCTIONS
{{做什么}}

## INPUTS
{{数据、文档或上下文}}

## CONSTRAINTS
{{范围、排除项、不确定性规则}}

## OUTPUT FORMAT
{{输出契约/模式}}
```

### Self-Check 模块

```markdown
Before finalizing, verify:
☐ Output matches the requested format
☐ All claims are supported by sources
☐ Uncertain content is marked as [UNCERTAIN]
☐ Next steps are specific and actionable

Score the draft (0-5 each):
- Correctness
- Completeness
- Clarity

If any score < 4, revise once.
```

---

## Guardrails 安全体系

### 三层防护

```
┌─────────────────────────────────────────────────────────────┐
│                    Input Guardrails                          │
│  • Prompt Injection 检测                                    │
│  • PII 过滤                                                 │
│  • 话题边界                                                 │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                    Output Guardrails                         │
│  • 幻觉检测                                                 │
│  • 事实核查                                                 │
│  • 来源验证                                                 │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                    Behavior Guardrails                       │
│  • 操作审计                                                 │
│  • 权限控制                                                 │
│  • 合规检查                                                 │
└─────────────────────────────────────────────────────────────┘
```

### 幻觉检测策略

根据研究，RAG 系统仍有 **15-30%** 幻觉率，需要：
1. 来源验证：每个事实陈述必须有来源
2. 置信度评估：低于阈值时标注"不确定"
3. 交叉验证：多个来源交叉确认

---

## MCP 集成设计

### MCP Server 配置

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/knowledge"]
    },
    "chroma": {
      "command": "npx",
      "args": ["-y", "mcp-server-chroma"],
      "env": {
        "CHROMA_HOST": "localhost",
        "CHROMA_PORT": "8000"
      }
    },
    "notion": {
      "command": "npx",
      "args": ["-y", "mcp-server-notion"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}"
      }
    }
  }
}
```

### RAG + MCP 架构

```
用户查询
    ↓
AI Client (Claude/GPT)
    ↓
┌──────────┬──────────┬──────────┐
│ Vector   │ Document │ Database │
│ DB MCP   │ MCP      │ MCP      │
│ (Chroma) │ (Files)  │ (SQLite) │
└──────────┴──────────┴──────────┘
    ↓
检索结果 → 生成回答
```

---

## 性能指标

### 企业级性能要求

| 指标 | 目标值 | 说明 |
|------|--------|------|
| **成功率** | > 99% | LangGraph 生产级可靠性 |
| **响应延迟** | < 3s | P95 延迟 |
| **幻觉率** | < 5% | RAG + Guardrails |
| **可用性** | > 99.5% | 系统可用性 |

### 成本优化

| 策略 | 效果 |
|------|------|
| 语义缓存 | 减少 **68.8%** LLM 成本 |
| 混合检索 | 准确率提升 **25%** |
| Prompt 优化 | 小模型匹配大模型性能 |

---

## 技术选型总结

| 层次 | 技术 | 原因 |
|------|------|------|
| **Agent 框架** | LangGraph | 企业首选、精确控制、最大生态 |
| **RAG 框架** | LlamaIndex | RAG 专用、性能优化 |
| **向量数据库** | Qdrant/Chroma | 开源、高性能、易部署 |
| **协议** | MCP | 2026 最火、行业标准 |
| **防护** | Llama Guard + 自定义 | 安全必备 |
| **UI** | Streamlit | 快速开发 |

---

## 项目结构

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

## 快速开始

### 前置要求
- Python 3.12+（2026 年新项目首选）
- 8GB+ RAM（推荐 16GB）

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

## 许可证

MIT License

---

**ByteBrain - 让 AI 成为你的第二大脑**