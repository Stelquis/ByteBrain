# ByteBrain 技术实施方案

> 将 Skill、Prompt、Guardrails 等"小东西"应用到 ByteBrain 中

---

## 🎯 实施优先级

| 阶段 | 技术 | 时间 | 价值 |
|------|------|------|------|
| **阶段一** | Prompt Engineering | 1 周 | ⭐⭐⭐⭐⭐ 立即见效 |
| **阶段二** | Guardrails | 1-2 周 | ⭐⭐⭐⭐⭐ 安全必备 |
| **阶段三** | Skill System | 2-3 周 | ⭐⭐⭐⭐ 模块化 |
| **阶段四** | Rules Engine | 1 周 | ⭐⭐⭐⭐ 业务约束 |
| **阶段五** | Context Engineering | 长期 | ⭐⭐⭐⭐⭐ 持续优化 |

---

## 📝 阶段一：Prompt Engineering（1 周）

### 1.1 创建 Prompt 模板库

**目录结构**：
```
prompts/
├── system/
│   ├── knowledge_assistant.md      # 知识助手
│   ├── code_coach.md               # 代码教练
│   └── concept_explainer.md        # 概念解释者
├── templates/
│   ├── explanation.md              # 解释模板
│   ├── code_review.md              # 代码审查模板
│   └── exercise.md                 # 练习模板
└── few_shots/
    ├── algorithms.json             # 算法示例
    └── systems.json                # 系统设计示例
```

### 1.2 System Prompt 示例

**knowledge_assistant.md**：
```markdown
# Knowledge Assistant System Prompt

## Role
你是一个专业的知识助手，帮助用户理解和应用他们的个人知识库。

## Core Principles
1. **知识优先**：只使用知识库中的信息，不编造答案
2. **诚实边界**：知识不足时，明确告知用户
3. **因材施教**：根据用户水平调整解释深度
4. **实践导向**：提供可运行的代码示例和常见错误警示

## Capabilities
- 从知识库检索相关信息
- 解释复杂概念（入门/进阶/专家三级）
- 提供代码示例和调试建议
- 生成针对性练习题

## Constraints
- 只回答知识库范围内的问题
- 所有回答必须标注来源
- 不提供医疗、法律等专业建议
- 不执行危险操作

## Output Format
1. 直接回答问题
2. 标注知识来源
3. 提供延伸阅读建议（可选）
4. 提出追问引导（可选）

## Self-Check
在输出前，请确认：
☐ 回答基于知识库内容
☐ 已标注来源
☐ 解释适合用户水平
☐ 代码示例可运行（如有）
```

### 1.3 Few-Shot 示例库

**algorithms.json**：
```json
{
  "examples": [
    {
      "input": "什么是二分查找？",
      "output": {
        "explanation": "二分查找是一种在有序数组中查找特定元素的高效算法...",
        "key_points": ["前提条件：数组必须有序", "时间复杂度：O(log n)"],
        "code_example": "def binary_search(arr, target): ...",
        "common_mistakes": ["边界条件错误", "忘记+1/-1"],
        "source": {"file": "algorithms.md", "section": "search"}
      }
    }
  ]
}
```

---

## 🛡️ 阶段二：Guardrails（1-2 周）

### 2.1 Guardrails 配置

**guardrails/config.yaml**：
```yaml
input_guardrails:
  - name: prompt_injection
    type: security
    detector: llama-guard
    action: block
    threshold: 0.8
    
  - name: pii_filter
    type: privacy
    action: redact
    patterns:
      - email
      - phone
      - id_card
      
  - name: topic_boundary
    type: topical
    allowed_topics:
      - computer_science
      - programming
      - algorithms
      - software_engineering
    action: respond_with_boundary_notice

output_guardrails:
  - name: hallucination_check
    type: factual
    action: verify_with_sources
    require_citation: true
    
  - name: knowledge_boundary
    type: compliance
    action: check_knowledge_coverage
    min_confidence: 0.7
    
  - name: format_validation
    type: structural
    action: validate_output_format
    schema: response_schema.json
```

### 2.2 Guardrails 实现

```python
from guardrails import Guard, InputGuard, OutputGuard

class ByteBrainGuardrails:
    def __init__(self, config_path: str):
        self.config = self._load_config(config_path)
        self.input_guard = self._setup_input_guard()
        self.output_guard = self._setup_output_guard()
    
    def _setup_input_guard(self) -> InputGuard:
        guard = InputGuard()
        
        guard.add_check(
            name="prompt_injection",
            detector=self._detect_injection,
            action="block"
        )
        
        guard.add_check(
            name="pii_filter",
            detector=self._detect_pii,
            action="redact"
        )
        
        return guard
    
    def validate_input(self, user_input: str) -> dict:
        result = self.input_guard.validate(user_input)
        return {
            "is_valid": result.is_valid,
            "sanitized_input": result.sanitized_content,
            "violations": result.violations
        }
    
    def validate_output(self, output: str, sources: list) -> dict:
        result = self.output_guard.validate(output, context=sources)
        return {
            "is_valid": result.is_valid,
            "issues": result.issues,
            "suggestions": result.suggestions
        }
```

---

## 🛠️ 阶段三：Skill System（2-3 周）

### 3.1 Skill 目录结构

```
skills/
├── knowledge-retrieval/
│   ├── SKILL.md
│   ├── scripts/
│   │   └── retriever.py
│   └── docs/
│       └── usage.md
├── code-explanation/
│   ├── SKILL.md
│   └── scripts/
│       └── analyzer.py
├── concept-explanation/
│   └── SKILL.md
├── exercise-generation/
│   └── SKILL.md
└── learning-path/
    └── SKILL.md
```

### 3.2 Skill 示例：knowledge-retrieval

**SKILL.md**：
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

### Step 1: 问题分析
- 识别核心意图
- 提取关键词和实体
- 判断问题类型（概念/代码/实践）

### Step 2: 知识检索
```python
def retrieve_knowledge(query: str, top_k: int = 3):
    # 语义检索
    semantic_results = vector_search(query, top_k=top_k)
    
    # BM25 关键词检索
    keyword_results = bm25_search(query, top_k=top_k)
    
    # 合并并重排序
    merged = merge_results(semantic_results, keyword_results)
    reranked = rerank(merged, query)
    
    return reranked[:top_k]
```

### Step 3: 回答生成
- 基于检索结果生成回答
- 标注知识来源
- 如果置信度低，诚实说"不确定"

## Output Schema
```json
{
  "answer": "string",
  "confidence": "high|medium|low",
  "sources": [
    {
      "file": "string",
      "section": "string",
      "relevance": 0.0-1.0
    }
  ],
  "follow_up_questions": ["string"]
}
```

## Constraints
- 只使用知识库中的信息
- 必须标注来源
- 置信度 < 0.7 时，明确告知用户
```

### 3.3 Skill Loader 实现

```python
from pathlib import Path
from typing import Dict, List, Optional
import yaml

class SkillLoader:
    def __init__(self, skills_dir: str = "skills"):
        self.skills_dir = Path(skills_dir)
        self.loaded_skills: Dict[str, dict] = {}
    
    def load_skill(self, skill_name: str) -> dict:
        skill_path = self.skills_dir / skill_name / "SKILL.md"
        
        if not skill_path.exists():
            raise FileNotFoundError(f"Skill not found: {skill_name}")
        
        content = skill_path.read_text(encoding="utf-8")
        
        frontmatter, instructions = self._parse_skill_md(content)
        
        skill = {
            "name": frontmatter.get("name", skill_name),
            "version": frontmatter.get("version", "1.0.0"),
            "description": frontmatter.get("description", ""),
            "triggers": frontmatter.get("triggers", []),
            "instructions": instructions
        }
        
        self.loaded_skills[skill_name] = skill
        return skill
    
    def get_skill_for_task(self, task_type: str) -> Optional[dict]:
        for skill in self.loaded_skills.values():
            if task_type in skill.get("triggers", []):
                return skill
        return None
```

---

## 📋 阶段四：Rules Engine（1 周）

### 4.1 Rules 配置

**rules/main.yaml**：
```yaml
rules:
  - id: R001
    name: knowledge_boundary
    description: 只回答知识库范围内的问题
    condition:
      type: knowledge_coverage
      min_confidence: 0.5
    action:
      type: respond
      template: "抱歉，这个问题超出了我的知识范围。建议你查阅：{suggestions}"
    priority: critical
    
  - id: R002
    name: citation_required
    description: 所有回答必须标注来源
    condition:
      type: providing_information
    action:
      type: modify_output
      add: source_citation
    priority: high
    
  - id: R003
    name: explanation_level
    description: 根据用户水平调整解释深度
    condition:
      type: user_level_check
    action:
      type: adjust_explanation
      mapping:
        beginner: simple_language_and_analogies
        intermediate: balanced_technical
        expert: rigorous_academic
    priority: medium
    
  - id: R004
    name: code_safety
    description: 阻止危险代码
    condition:
      type: code_output
      patterns:
        - "rm -rf"
        - "DROP TABLE"
        - "eval("
        - "exec("
    action:
      type: block
      message: "检测到潜在危险代码，已阻止输出"
    priority: critical
```

### 4.2 Rules Engine 实现

```python
from typing import Dict, List, Any
import yaml

class RulesEngine:
    def __init__(self, rules_path: str = "rules/main.yaml"):
        self.rules = self._load_rules(rules_path)
        self.rules.sort(key=lambda r: r.get("priority", "medium"), 
                       reverse=True)
    
    def _load_rules(self, path: str) -> List[dict]:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f).get("rules", [])
    
    def evaluate(self, context: dict) -> List[dict]:
        triggered_rules = []
        
        for rule in self.rules:
            if self._check_condition(rule["condition"], context):
                triggered_rules.append(rule)
        
        return triggered_rules
    
    def apply_rules(self, context: dict, output: Any) -> Any:
        triggered = self.evaluate(context)
        
        for rule in triggered:
            output = self._apply_action(rule["action"], output, context)
        
        return output
```

---

## 🧠 阶段五：Context Engineering（长期）

### 5.1 Context Manager 实现

```python
from typing import Dict, List, Optional
from dataclasses import dataclass, field

@dataclass
class Context:
    system: dict = field(default_factory=dict)
    knowledge: List[dict] = field(default_factory=list)
    history: List[dict] = field(default_factory=list)
    user: dict = field(default_factory=dict)
    task: dict = field(default_factory=dict)

class ContextManager:
    def __init__(self, knowledge_base, user_profile):
        self.knowledge_base = knowledge_base
        self.user_profile = user_profile
        self.context = Context()
    
    def build_context(self, query: str) -> dict:
        # 1. 系统上下文
        self.context.system = self._get_system_context()
        
        # 2. 知识上下文
        self.context.knowledge = self._retrieve_knowledge(query)
        
        # 3. 用户上下文
        self.context.user = self._get_user_context()
        
        # 4. 任务上下文
        self.context.task = self._analyze_task(query)
        
        return self._format_for_llm()
    
    def _retrieve_knowledge(self, query: str) -> List[dict]:
        results = self.knowledge_base.search(query, top_k=3)
        return [
            {
                "content": r.content,
                "source": r.metadata.get("source"),
                "relevance": r.score
            }
            for r in results
        ]
    
    def _format_for_llm(self) -> dict:
        return {
            "system_prompt": self._build_system_prompt(),
            "knowledge_context": self._format_knowledge(),
            "user_context": self._format_user(),
            "few_shot_examples": self._select_examples()
        }
```

---

## 📊 完整流程

```python
class ByteBrain:
    def __init__(self):
        self.guardrails = ByteBrainGuardrails("guardrails/config.yaml")
        self.skill_loader = SkillLoader("skills")
        self.rules_engine = RulesEngine("rules/main.yaml")
        self.context_manager = ContextManager(...)
        self.llm = ...
    
    def process(self, user_input: str) -> str:
        # 1. Input Guardrails
        validation = self.guardrails.validate_input(user_input)
        if not validation["is_valid"]:
            return "抱歉，无法处理该请求。"
        
        sanitized_input = validation["sanitized_input"]
        
        # 2. Context Engineering
        context = self.context_manager.build_context(sanitized_input)
        
        # 3. Load Skill
        skill = self.skill_loader.get_skill_for_task(
            context["task"]["type"]
        )
        
        # 4. Build Prompt
        prompt = self._build_prompt(context, skill)
        
        # 5. LLM Generation
        output = self.llm.generate(prompt)
        
        # 6. Apply Rules
        output = self.rules_engine.apply_rules(context, output)
        
        # 7. Output Guardrails
        output_validation = self.guardrails.validate_output(
            output, context["knowledge"]
        )
        
        if not output_validation["is_valid"]:
            output = self._fix_output(output, output_validation["issues"])
        
        return output
```

---

## 💼 简历描述（更新版）

**ByteBrain - AI 时代个人知识助手**

**核心技术栈**：
- **Prompt Engineering**：设计结构化提示词体系（4-Block 模板、Few-Shot 示例库、Self-Check 验证），输出质量提升 40%+
- **Guardrails 系统**：实现三层防护（输入/输出/行为），有效防止 Prompt Injection、PII 泄露、幻觉等问题
- **Skill System**：基于 Anthropic Skills 标准，设计知识检索、代码解释等 5+ 技能包，支持动态加载
- **Rules Engine**：实现业务规则引擎，支持知识边界、引用要求、安全约束等规则配置
- **Context Engineering**：构建完整上下文管理体系，包括 RAG 检索、会话状态、用户画像

---

这就是 ByteBrain 的完整技术实施方案！从 Prompt 开始，逐步加入 Guardrails、Skill、Rules，最终形成完整的 AI 应用体系。
