# ByteBrain 设计哲学

> **AI 时代你的第二大脑**
> 
> 大框架支撑格局，小巧思成就细节

---

## 核心理念

### 大框架与小巧思的辩证统一

**大框架决定上限**：Agent、LangGraph、MCP、RAG  
**小巧思决定下限**：Skill、Prompt、Guardrails、Rules

### 五大原则

1. **知识优先** - AI 只是手段，知识才是目的
2. **诚实可信** - 知之为知之，不知为不知
3. **因材施教** - 不同的人，不同的学习方式
4. **实践导向** - 纸上得来终觉浅，绝知此事要躬行
5. **简洁优雅** - 如无必要，勿增实体

---

## 技术架构

```
用户输入
    ↓
Input Guardrails
    ↓
Context Engineering
    ↓
Agent Orchestration (LangGraph)
    ↓
Skill Execution
    ↓
Output Guardrails
    ↓
用户输出
```

---

## 核心技术栈

| 技术 | 用途 |
|------|------|
| LangGraph | Agent 工作流编排 |
| MCP | 数据源连接协议 |
| LlamaIndex | RAG 框架 |
| Qdrant/Chroma | 向量数据库 |
| Skill System | 能力模块化 |
| Prompt Engineering | 精准沟通 |
| Guardrails | 安全防护 |

---

## 更多

- [快速开始](./guide/GETTING_STARTED.md)
- [开发指南](./guide/DEVELOPMENT.md)
