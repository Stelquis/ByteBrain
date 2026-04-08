# ByteBrain 使用示例

---

## 目录

- [基础使用](#基础使用)
- [知识管理](#知识管理)
- [代码教练](#代码教练)
- [概念解释](#概念解释)
- [多Agent协作](#多agent协作)
- [Web API使用](#web-api使用)
- [命令行工具](#命令行工具)
- [高级配置](#高级配置)

---

## 基础使用

### 快速开始示例

**功能**：展示 ByteBrain 的基本使用方法，包括初始化、提问和检索知识。

**文件**：[basic_usage.py](basic_usage.py)

**示例代码**：
```python
from bytebrain import ByteBrain

# 初始化 ByteBrain
brain = ByteBrain()

# 提问
print("=== 提问示例 ===")
response = brain.ask("什么是人工智能？")
print("回答:", response)

# 检索知识
print("\n=== 检索知识示例 ===")
results = brain.retrieve("机器学习", top_k=3)
for i, result in enumerate(results, 1):
    print(f"{i}. 分数: {result['score']:.2f}")
    print(f"   内容: {result['content'][:100]}...")
    print(f"   来源: {result['source']}")
```

---

## 知识管理

### 添加知识示例

**功能**：展示如何添加不同类型的知识到 ByteBrain。

**文件**：[knowledge_management.py](knowledge_management.py)

**示例代码**：
```python
from bytebrain import ByteBrain

# 初始化 ByteBrain
brain = ByteBrain()

# 添加单个文件
print("=== 添加单个文件 ===")
success = brain.add_knowledge("path/to/document.pdf")
print(f"添加文件: {'成功' if success else '失败'}")

# 添加目录
print("\n=== 添加目录 ===")
success = brain.add_knowledge("path/to/documents/")
print(f"添加目录: {'成功' if success else '失败'}")

# 添加文本
print("\n=== 添加文本 ===")
text = "这是一段测试文本，用于演示如何添加文本知识。"
success = brain.add_knowledge(text, metadata={"title": "测试文本", "type": "notes"})
print(f"添加文本: {'成功' if success else '失败'}")
```

### 知识库管理示例

**功能**：展示如何管理和查询知识库。

**文件**：[knowledge_base_management.py](knowledge_base_management.py)

---

## 代码教练

### 代码优化示例

**功能**：展示如何使用代码教练技能优化代码。

**文件**：[code_coaching.py](code_coaching.py)

**示例代码**：
```python
from bytebrain import ByteBrain

# 初始化 ByteBrain
brain = ByteBrain()

# 代码优化
print("=== 代码优化示例 ===")
code = """
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
"""

result = brain.execute_skill("code-coaching", {
    "code": code,
    "question": "如何优化这段斐波那契数列代码？"
})

print("原代码:")
print(code)
print("\n反馈:")
print(result['feedback'])
print("\n优化建议:")
print(result['suggestion'])
print("\n解释:")
print(result['explanation'])
```

### 代码解释示例

**功能**：展示如何使用代码教练技能解释代码。

**文件**：[code_explanation.py](code_explanation.py)

---

## 概念解释

### 概念解释示例

**功能**：展示如何使用概念解释技能解释复杂概念。

**文件**：[concept_explanation.py](concept_explanation.py)

**示例代码**：
```python
from bytebrain import ByteBrain

# 初始化 ByteBrain
brain = ByteBrain()

# 解释概念
print("=== 概念解释示例 ===")
result = brain.execute_skill("concept-explanation", {
    "concept": "深度学习",
    "level": "beginner"
})

print("概念:", "深度学习")
print("解释:")
print(result['explanation'])
print("\n类比:")
for analogy in result['analogies']:
    print(f"- {analogy}")
print("\n例子:")
for example in result['examples']:
    print(f"- {example}")
```

---

## 多Agent协作

### 多Agent工作流示例

**功能**：展示如何使用多Agent协作完成复杂任务。

**文件**：[multi_agent_workflow.py](multi_agent_workflow.py)

**示例代码**：
```python
from bytebrain import ByteBrain

# 初始化 ByteBrain
brain = ByteBrain()

# 多Agent协作完成任务
print("=== 多Agent协作示例 ===")
task = "分析 Python 中的装饰器概念，并提供一个实用的装饰器示例"

# 使用协调者Agent处理复杂任务
response = brain.ask(task)

print("任务:", task)
print("\n多Agent协作结果:")
print(response)
```

---

## Web API使用

### Python客户端示例

**功能**：展示如何使用 Python 客户端调用 ByteBrain Web API。

**文件**：[web_api_client.py](web_api_client.py)

**示例代码**：
```python
import requests
import json

# API配置
API_URL = "http://localhost:8000/api"
API_KEY = "YOUR_API_KEY"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 提问
def ask_question(query):
    url = f"{API_URL}/ask"
    data = {"query": query}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# 检索知识
def retrieve_knowledge(query, top_k=5):
    url = f"{API_URL}/retrieve"
    data = {"query": query, "top_k": top_k}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# 执行技能
def execute_skill(skill_name, input_data):
    url = f"{API_URL}/skill"
    data = {"skill_name": skill_name, "input_data": input_data}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# 示例使用
print("=== Web API 示例 ===")

# 提问
print("\n1. 提问:")
result = ask_question("什么是 LangGraph？")
print("回答:", result['answer'])

# 检索知识
print("\n2. 检索知识:")
result = retrieve_knowledge("Python 装饰器", top_k=3)
for i, item in enumerate(result['results'], 1):
    print(f"{i}. {item['content'][:100]}...")

# 执行技能
print("\n3. 执行代码教练技能:")
result = execute_skill("code-coaching", {
    "code": "def hello(): print('Hello')",
    "question": "如何改进这段代码？"
})
print("反馈:", result['result']['feedback'])
```

### JavaScript客户端示例

**功能**：展示如何使用 JavaScript 客户端调用 ByteBrain Web API。

**文件**：[web_api_client.js](web_api_client.js)

---

## 命令行工具

### 命令行使用示例

**功能**：展示如何使用 ByteBrain 命令行工具。

**文件**：[cli_usage.md](cli_usage.md)

**示例命令**：

```bash
# 初始化系统
bytebrain init

# 添加知识
bytebrain add-knowledge path/to/documents/

# 提问
bytebrain ask "如何使用 Python 装饰器？"

# 检索知识
bytebrain retrieve "机器学习算法"

# 执行技能
bytebrain skill code-coaching '{"code": "def factorial(n): return 1 if n <= 1 else n * factorial(n-1)", "question": "如何优化？"}'

# 查看系统状态
bytebrain stats

# 查看日志
bytebrain logs --verbose

# 查看版本
bytebrain version
```

---

## 高级配置

### 自定义配置示例

**功能**：展示如何自定义 ByteBrain 配置。

**文件**：[advanced_configuration.py](advanced_configuration.py)

**示例代码**：
```python
from bytebrain import ByteBrain
from bytebrain.utils.config import load_config, update_config

# 加载默认配置
print("=== 加载默认配置 ===")
config = load_config()
print("当前配置:", config)

# 更新配置
print("\n=== 更新配置 ===")
new_config = {
    "agent": {
        "temperature": 0.5,
        "max_tokens": 4096,
        "model": "gpt-4o"
    },
    "rag": {
        "chunk_size": 1500,
        "chunk_overlap": 300,
        "top_k": 10
    },
    "vector_db": {
        "type": "qdrant",
        "host": "localhost",
        "port": 6333
    }
}

update_config(new_config)
print("配置更新成功")

# 使用自定义配置初始化
print("\n=== 使用自定义配置初始化 ===")
brain = ByteBrain(
    config_path="path/to/custom_config.yaml",
    vector_db_type="qdrant",
    model="gpt-4o"
)

print("ByteBrain 初始化成功")
```

### 性能优化示例

**功能**：展示如何优化 ByteBrain 性能。

**文件**：[performance_optimization.py](performance_optimization.py)

---

## 实际应用场景

### 开发者知识库

**功能**：展示如何使用 ByteBrain 作为开发者的知识库。

**文件**：[developer_knowledge_base.py](developer_knowledge_base.py)

### 学生学习助手

**功能**：展示如何使用 ByteBrain 作为学生的学习助手。

**文件**：[student_learning_assistant.py](student_learning_assistant.py)

### 专业人士知识管理

**功能**：展示如何使用 ByteBrain 作为专业人士的知识管理工具。

**文件**：[professional_knowledge_management.py](professional_knowledge_management.py)

---

## 常见问题解决

### 问题排查示例

**功能**：展示如何排查和解决 ByteBrain 使用中遇到的常见问题。

**文件**：[troubleshooting.py](troubleshooting.py)

---

## 最佳实践

### 使用建议

1. **定期更新知识库**：定期添加新的知识源，保持知识库的新鲜度
2. **合理配置参数**：根据硬件资源和使用场景调整配置参数
3. **使用技能系统**：充分利用技能系统处理特定类型的任务
4. **监控系统状态**：定期查看系统状态，确保系统正常运行
5. **优化查询方式**：使用具体、明确的查询语句获得更准确的结果

---

## 更多资源

- [API 文档](../API.md) - 详细的 API 参考
- [设计哲学](../PHILOSOPHY.md) - ByteBrain 的设计理念
- [快速开始](../guide/GETTING_STARTED.md) - 快速开始指南
- [开发指南](../guide/DEVELOPMENT.md) - 开发者指南