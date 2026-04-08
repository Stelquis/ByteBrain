# 2026 年 AI "小东西" 全景：Skill、Prompt、Guardrails 等

> **这些"小东西"往往是决定 AI 应用成败的关键**

---

## 📚 概览：2026 年 AI 技术栈的"小东西"

| 技术 | 是什么 | 为什么重要 | 企业需求 |
|------|--------|-----------|---------|
| **Skill（技能）** | AI 的专项能力包 | 让 Agent 具备专业能力 | ⭐⭐⭐⭐⭐ |
| **Prompt Engineering** | 与 AI 沟通的技术 | 决定输出质量 | ⭐⭐⭐⭐⭐ |
| **Guardrails（护栏）** | AI 安全边界 | 防止 AI 乱说话、乱做事 | ⭐⭐⭐⭐⭐ |
| **Rules（规则）** | 行为约束 | 确保符合业务逻辑 | ⭐⭐⭐⭐ |
| **Context Engineering** | 上下文设计 | 2026 年的新范式 | ⭐⭐⭐⭐⭐ |

---

## 🛠️ 一、Skill（技能系统）

### 1.1 什么是 Skill？

**Skill ≠ Tool**

| 概念 | 定义 | 特点 |
|------|------|------|
| **Tool（工具）** | 单一函数，执行并返回结果 | 简单、原子化 |
| **Skill（技能）** | 结构化的能力包，包含指令、脚本、参考文档 | 复杂、多文件、有工作流 |

**Skill 的组成**（Anthropic 2025 年 10 月提出）：
```
my-skill/
├── SKILL.md          # 核心指令文件（必需）
├── scripts/          # 可执行脚本（可选）
│   ├── main.py
│   └── utils.py
├── docs/             # 参考文档（可选）
│   └── guide.md
└── assets/           # 其他资源（可选）
    └── template.json
```

### 1.2 SKILL.md 规范

```markdown
---
name: knowledge-retrieval
description: 从知识库检索相关信息并生成回答
version: 1.0.0
author: ByteBrain Team
tags: [rag, retrieval, knowledge]
---

# Knowledge Retrieval Skill

## Purpose
从用户的知识库中检索相关信息，生成准确、可溯源的回答。

## When to Use
- 用户询问与知识库相关的问题
- 需要引用具体来源的回答
- 需要验证信息准确性

## Instructions

### Step 1: 分析问题
- 识别问题的核心意图
- 提取关键词和实体

### Step 2: 检索知识
- 使用语义检索获取 Top-K 相关文档
- 使用 BM25 进行关键词匹配
- 合并结果并重排序

### Step 3: 生成回答
- 基于检索结果生成回答
- 标注知识来源
- 如果知识不足，诚实说"不知道"

## Output Format
```json
{
  "answer": "回答内容",
  "sources": [
    {"file": "文件名", "section": "章节", "confidence": 0.95}
  ],
  "confidence": "high/medium/low"
}
```

## Examples
[示例输入输出...]

## Constraints
- 只使用知识库中的信息
- 不编造答案
- 必须标注来源
```

### 1.3 2026 年 Skill 生态

| 项目/框架 | 特点 | Stars/采用率 |
|----------|------|-------------|
| **Anthropic Skills** | 官方标准，62K+ GitHub Stars | ⭐⭐⭐⭐⭐ |
| **SkillNet** | 浙大开源，200,000+ 技能库 | ⭐⭐⭐⭐ |
| **langchain-ai-skills-framework** | LangChain 集成 | ⭐⭐⭐⭐ |
| **EvoSkills** | 自进化技能框架 | ⭐⭐⭐ |

**关键数据**：
- Anthropic Skills 仓库 **4 个月内获得 62,000+ Stars**
- Atlassian、Figma、Canva、Stripe、Notion 等已构建官方 Skills
- **26.1%** 的社区贡献 Skills 存在安全漏洞（需要治理！）

### 1.4 ByteBrain 如何使用 Skill？

```
bytebrain-skills/
├── knowledge-retrieval/     # 知识检索技能
│   └── SKILL.md
├── code-explanation/        # 代码解释技能
│   └── SKILL.md
├── concept-explanation/     # 概念解释技能
│   └── SKILL.md
├── exercise-generation/     # 练习生成技能
│   └── SKILL.md
└── learning-path/           # 学习路径规划技能
    └── SKILL.md
```

---

## 📝 二、Prompt Engineering（提示词工程）

### 2.1 2026 年的 Prompt Engineering

**核心观点**：Prompt Engineering 不再是"写更长的提示词"，而是"写更清晰的规范"。

### 2.2 2026 年最佳实践清单

```
✅ 2026 Checklist（每次必用）

1. Success Criteria（成功标准）
   - "完成"是什么样子？
   - 如何评判？

2. Output Contract（输出契约）
   - 格式、长度、语气、必需章节
   - 使其可测试

3. Constraints（约束）
   - 范围、假设、排除项
   - 不确定时该怎么办

4. Inputs（输入）
   - 最小上下文 + 必需数据

5. Examples（示例）
   - 格式或风格重要时，提供 1-3 个示例

6. Verification（验证）
   - 简短的检查清单，捕获常见错误

7. Iteration（迭代）
   - 置信度低时，请求澄清或替代方案
```

### 2.3 黄金模板：4-Block 结构

```
## INSTRUCTIONS
{{做什么}}

## INPUTS
{{数据、文档或上下文}}

## CONSTRAINTS
{{范围、排除项、不确定性规则}}

## OUTPUT FORMAT
{{契约/模式}}
```

### 2.4 Few-Shot Prompting（少样本提示）

**最佳实践**：
- 提供 **3-5 个示例**（研究表明 4-5 个后收益递减）
- 示例要**相关**：紧密反映实际用例
- 示例要**多样**：覆盖边界情况
- 使用**结构化分隔符**：`<example>` 标签

**示例**：
```xml
<example>
<input>什么是二分查找？</input>
<output>
二分查找是一种在有序数组中查找特定元素的高效算法。

**核心要点**：
1. 前提条件：数组必须有序
2. 时间复杂度：O(log n)
3. 每次比较将搜索范围缩小一半

**代码示例**：
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**常见错误**：
- 边界条件：`left < right` 应为 `left <= right`
- 更新边界：忘记 `+1` 或 `-1` 会导致死循环
</output>
</example>
```

### 2.5 Self-Check Block（自检模块）

```
Before finalizing, verify:
☐ Output matches the requested format exactly
☐ All success criteria are satisfied
☐ Claims not supported by inputs are marked as [UNCERTAIN]
☐ Next steps are specific and actionable

Score the draft (0-5 each):
- Correctness
- Completeness
- Clarity
- Actionability

If any score < 4, revise once and rescore.
```

### 2.6 ByteBrain 的 Prompt 模板库

```
prompts/
├── system_prompts/
│   ├── knowledge_assistant.yaml    # 知识助手系统提示
│   ├── code_coach.yaml             # 代码教练系统提示
│   └── concept_explainer.yaml      # 概念解释者系统提示
├── templates/
│   ├── explanation_template.md     # 解释模板
│   ├── code_review_template.md     # 代码审查模板
│   └── exercise_template.md        # 练习题模板
└── few_shots/
    ├── algorithm_examples.json     # 算法示例
    └── system_examples.json        # 系统设计示例
```

---

## 🛡️ 三、Guardrails（护栏系统）

### 3.1 什么是 Guardrails？

**Guardrails = AI 的安全边界**

就像高速公路的护栏，防止 AI"跑偏"：
- 说出有害内容
- 泄露敏感信息
- 执行危险操作
- 偏离业务规则

### 3.2 Guardrails 的三层防护

```
┌─────────────────────────────────────────────────────────────┐
│                    Input Guardrails（输入护栏）              │
│  • 检测 Prompt Injection 攻击                               │
│  • 过滤 PII（个人身份信息）                                  │
│  • 阻止非法/有害请求                                         │
│  • 识别越狱尝试                                             │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                      LLM / Agent                             │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   Output Guardrails（输出护栏）              │
│  • 检测幻觉（Hallucination）                                 │
│  • 过滤敏感数据泄露                                          │
│  • 验证事实准确性                                            │
│  • 检查品牌一致性                                            │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Guardrails 类型

| 类型 | 功能 | 示例 |
|------|------|------|
| **Topical Guardrails** | 限制话题 | 银行 AI 不讨论政治 |
| **Security Guardrails** | 防止攻击 | 检测 Prompt Injection |
| **Safety Guardrails** | 内容安全 | 阻止有害内容 |
| **Compliance Guardrails** | 合规要求 | HIPAA、GDPR |
| **Factual Guardrails** | 事实核查 | 对比知识库验证 |
| **Action Guardrails** | 行为约束 | 限制 Agent 可执行的操作 |

### 3.4 2026 年主流 Guardrails 框架

| 框架 | 特点 | 适用场景 |
|------|------|---------|
| **Llama Guard** | Meta 开源，内容安全 | 通用安全 |
| **NVIDIA NeMo Guardrails** | 企业级，可编程 | 复杂业务规则 |
| **Guardrails AI** | Python 库，易集成 | 快速开发 |
| **Lyzr Guardrails** | Agent 专用 | Multi-Agent 系统 |

### 3.5 ByteBrain 的 Guardrails 设计

```python
# guardrails/config.yaml

input_guardrails:
  - name: prompt_injection_detector
    type: security
    action: block
    threshold: 0.8
    
  - name: pii_filter
    type: privacy
    action: redact
    patterns:
      - email
      - phone
      - id_number
      
  - name: topic_filter
    type: topical
    allowed_topics:
      - computer_science
      - programming
      - algorithms
      - software_engineering
    action: redirect

output_guardrails:
  - name: hallucination_detector
    type: factual
    action: verify_with_knowledge_base
    
  - name: source_attribution
    type: compliance
    action: require_citation
    
  - name: code_safety
    type: safety
    action: block_dangerous_code
    patterns:
      - rm -rf
      - DROP TABLE
      - eval(
```

---

## 📋 四、Rules（规则系统）

### 4.1 什么是 Rules？

Rules 是**业务逻辑层面的约束**，定义 AI 应该和不应该做什么。

### 4.2 Rules 示例

```yaml
# rules/knowledge_assistant_rules.yaml

rules:
  - id: R001
    name: knowledge_boundary
    description: 只回答知识库范围内的问题
    condition: "question_outside_knowledge_base"
    action: "respond_with_unknown"
    priority: high
    
  - id: R002
    name: citation_required
    description: 所有回答必须标注来源
    condition: "providing_information"
    action: "add_source_citation"
    priority: high
    
  - id: R003
    name: explanation_level
    description: 根据用户水平调整解释深度
    condition: "user_level == 'beginner'"
    action: "use_simple_language_and_analogies"
    priority: medium
    
  - id: R004
    name: code_example_required
    description: 代码相关问题必须提供可运行示例
    condition: "question_about_code"
    action: "provide_runnable_code_example"
    priority: medium
    
  - id: R005
    name: common_mistakes_warning
    description: 指出常见错误
    condition: "explaining_concept"
    action: "add_common_mistakes_section"
    priority: low
```

---

## 🧠 五、Context Engineering（上下文工程）

### 5.1 2026 年的新范式

**Context Engineering > Prompt Engineering**

核心观点：不仅要写好提示词，更要设计好整个上下文环境。

### 5.2 Context Engineering 的组成

```
Context Engineering
├── System Context（系统上下文）
│   ├── 角色定义
│   ├── 能力边界
│   └── 行为规范
├── Knowledge Context（知识上下文）
│   ├── RAG 检索结果
│   ├── 用户历史
│   └── 会话状态
├── Task Context（任务上下文）
│   ├── 当前任务
│   ├── 子任务
│   └── 进度追踪
└── Environment Context（环境上下文）
    ├── 可用工具
    ├── 权限设置
    └── 资源限制
```

---

## 🏗️ 六、ByteBrain 完整架构（整合所有"小东西"）

```
┌─────────────────────────────────────────────────────────────┐
│                      用户输入                                │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   Input Guardrails                          │
│  • Prompt Injection 检测                                    │
│  • PII 过滤                                                 │
│  • 话题限制                                                  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   Context Engineering                       │
│  • 加载 System Prompt                                       │
│  • 检索 Knowledge Context (RAG)                             │
│  • 加载用户历史                                              │
│  • 准备 Few-Shot Examples                                   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                     Skill Loader                            │
│  • 识别需要的 Skills                                        │
│  • 加载 SKILL.md                                            │
│  • 注入指令和约束                                            │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   Rules Engine                              │
│  • 应用业务规则                                              │
│  • 检查约束条件                                              │
│  • 设置行为边界                                              │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                      LLM / Agent                            │
│  • 执行推理                                                  │
│  • 调用工具                                                  │
│  • 生成输出                                                  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   Output Guardrails                         │
│  • 幻觉检测                                                  │
│  • 事实核查                                                  │
│  • 来源验证                                                  │
│  • 格式校验                                                  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                      用户输出                                │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 七、企业需求 vs. 你的技能

| 企业需求 | 对应技术 | ByteBrain 实践 |
|---------|---------|---------------|
| AI 安全合规 | Guardrails | 输入/输出护栏系统 |
| 输出质量稳定 | Prompt Engineering | 模板库 + Few-Shot |
| 能力模块化 | Skill System | 技能包设计 |
| 业务规则执行 | Rules Engine | 规则配置系统 |
| 上下文管理 | Context Engineering | RAG + 会话管理 |

---

## 💼 八、简历描述

### 基础版
- 掌握 **Prompt Engineering** 最佳实践，包括 Few-Shot、Chain-of-Thought、Self-Check 等技术
- 实现了 **Guardrails 系统**，确保 AI 输出的安全性和合规性
- 设计了 **Skill 模块化架构**，将 AI 能力拆分为可复用的技能包

### 进阶版
- **Prompt Engineering**：设计并实施了结构化提示词体系，包括 4-Block 模板、Few-Shot 示例库、Self-Check 验证模块，输出质量提升 40%+
- **Guardrails 系统**：实现了三层防护（输入/输出/行为），集成 Llama Guard 和自定义规则，有效防止 Prompt Injection、PII 泄露、幻觉等问题
- **Skill System**：基于 Anthropic Skills 标准，设计了知识检索、代码解释、概念讲解等 5+ 技能包，支持动态加载和组合
- **Context Engineering**：构建了完整的上下文管理体系，包括 RAG 检索、会话状态、用户历史等，实现个性化回答

---

## 🎯 总结

这些"小东西"不是锦上添花，而是**决定 AI 应用成败的关键**：

| 技术 | 核心价值 |
|------|---------|
| **Skill** | 让 AI 具备专业能力 |
| **Prompt** | 让 AI 理解你的意图 |
| **Guardrails** | 让 AI 不乱说话、乱做事 |
| **Rules** | 让 AI 遵守业务规则 |
| **Context** | 让 AI 有足够的背景信息 |

**掌握这些"小东西"，你就掌握了 AI 应用的核心竞争力！**
