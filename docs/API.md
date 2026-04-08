# API 文档

---

## 核心 API

### ByteBrain 主类

`ByteBrain` 是整个系统的核心类，提供了所有主要功能的访问接口。

#### 初始化

```python
from bytebrain.core import ByteBrain

# 基本初始化
brain = ByteBrain()

# 自定义配置初始化
brain = ByteBrain(
    config_path="path/to/config.yaml",
    vector_db_type="chroma",  # 或 "qdrant"
    model="gpt-4o"
)
```

#### 方法

| 方法 | 描述 | 参数 | 返回值 |
|------|------|------|--------|
| `ask()` | 向 ByteBrain 提问 | `query: str` - 问题<br>`context: dict = None` - 上下文信息 | `str` - 回答 |
| `retrieve()` | 检索知识 | `query: str` - 查询关键词<br>`top_k: int = 5` - 返回结果数量 | `List[Dict]` - 检索结果 |
| `add_knowledge()` | 添加知识 | `data: Union[str, Path]` - 文件路径或文本<br>`metadata: dict = None` - 元数据 | `bool` - 是否成功 |
| `execute_skill()` | 执行技能 | `skill_name: str` - 技能名称<br>`input_data: dict` - 输入数据 | `dict` - 技能执行结果 |
| `get_skills()` | 获取可用技能 | 无 | `List[str]` - 技能列表 |
| `update_config()` | 更新配置 | `config: dict` - 配置信息 | `bool` - 是否成功 |
| `get_stats()` | 获取系统状态 | 无 | `dict` - 系统状态信息 |

#### 示例

```python
# 提问
response = brain.ask("什么是 LangGraph？")
print(response)

# 检索知识
results = brain.retrieve("Python 设计模式", top_k=3)
for result in results:
    print(f"{result['score']}: {result['content'][:100]}...")

# 添加知识
success = brain.add_knowledge("path/to/document.pdf")
print(f"添加知识: {'成功' if success else '失败'}")

# 执行技能
result = brain.execute_skill("code-coaching", {
    "code": "def hello(): print('Hello')",
    "question": "如何改进这段代码？"
})
print(result['feedback'])

# 获取技能列表
skills = brain.get_skills()
print("可用技能:", skills)

# 获取系统状态
stats = brain.get_stats()
print("系统状态:", stats)
```

---

## Web API

ByteBrain 提供 RESTful API 接口，支持远程调用。默认端口为 8000。

### 认证

所有 API 调用需要在请求头中包含 `Authorization` 令牌：

```
Authorization: Bearer YOUR_API_KEY
```

### 端点

#### 1. 提问

- **URL**: `/api/ask`
- **方法**: `POST`
- **请求体**:
  ```json
  {
    "query": "什么是 LangGraph？",
    "context": {}
  }
  ```
- **响应**:
  ```json
  {
    "answer": "LangGraph 是一个用于构建 Agent 工作流的框架...",
    "sources": ["document.pdf"],
    "confidence": 0.95
  }
  ```

#### 2. 检索知识

- **URL**: `/api/retrieve`
- **方法**: `POST`
- **请求体**:
  ```json
  {
    "query": "Python 设计模式",
    "top_k": 5
  }
  ```
- **响应**:
  ```json
  {
    "results": [
      {
        "score": 0.92,
        "content": "单例模式确保一个类只有一个实例...",
        "source": "design_patterns.pdf",
        "metadata": {}
      }
    ]
  }
  ```

#### 3. 添加知识

- **URL**: `/api/add`
- **方法**: `POST`
- **请求体** (表单数据):
  - `file`: 文件上传
  - `metadata`: JSON 格式的元数据
- **响应**:
  ```json
  {
    "success": true,
    "message": "知识添加成功",
    "document_id": "doc_123"
  }
  ```

#### 4. 执行技能

- **URL**: `/api/skill`
- **方法**: `POST`
- **请求体**:
  ```json
  {
    "skill_name": "code-coaching",
    "input_data": {
      "code": "def hello(): print('Hello')",
      "question": "如何改进这段代码？"
    }
  }
  ```
- **响应**:
  ```json
  {
    "result": {
      "feedback": "代码可以添加类型注解...",
      "suggestion": "def hello() -> None: print('Hello')"
    },
    "skill_name": "code-coaching",
    "execution_time": 1.2
  }
  ```

#### 5. 获取技能列表

- **URL**: `/api/skills`
- **方法**: `GET`
- **响应**:
  ```json
  {
    "skills": [
      "knowledge-retrieval",
      "code-coaching",
      "concept-explanation"
    ]
  }
  ```

#### 6. 获取系统状态

- **URL**: `/api/stats`
- **方法**: `GET`
- **响应**:
  ```json
  {
    "status": "healthy",
    "version": "1.0.0",
    "knowledge_base_size": 100,
    "vector_db_status": "connected"
  }
  ```

---

## 技能 API

### 技能执行接口

每个技能都可以通过 `execute_skill()` 方法执行，也可以通过 Web API 调用。

#### 知识检索技能

- **技能名称**: `knowledge-retrieval`
- **输入**:
  ```json
  {
    "query": "什么是 RAG？",
    "top_k": 3
  }
  ```
- **输出**:
  ```json
  {
    "answer": "RAG (Retrieval-Augmented Generation) 是一种结合检索和生成的 AI 技术...",
    "sources": ["rag_paper.pdf"],
    "confidence": 0.98
  }
  ```

#### 代码教练技能

- **技能名称**: `code-coaching`
- **输入**:
  ```json
  {
    "code": "def factorial(n): return 1 if n <= 1 else n * factorial(n-1)",
    "question": "如何优化这段代码？"
  }
  ```
- **输出**:
  ```json
  {
    "feedback": "代码实现正确，但可以添加类型注解和缓存...",
    "suggestion": "from functools import lru_cache\n\n@lru_cache\ndef factorial(n: int) -> int: return 1 if n <= 1 else n * factorial(n-1)",
    "explanation": "使用 lru_cache 可以缓存中间结果，提高性能"
  }
  ```

#### 概念解释技能

- **技能名称**: `concept-explanation`
- **输入**:
  ```json
  {
    "concept": "神经网络",
    "level": "beginner"
  }
  ```
- **输出**:
  ```json
  {
    "explanation": "神经网络是一种模仿人脑结构的 AI 模型...",
    "analogies": ["像大脑中的神经元网络"],
    "examples": ["图像识别", "语音识别"]
  }
  ```

---

## 配置 API

### 配置管理

#### 加载配置

```python
from bytebrain.utils.config import load_config

# 加载默认配置
config = load_config()

# 加载自定义配置
config = load_config("path/to/config.yaml")
```

#### 更新配置

```python
from bytebrain.utils.config import update_config

# 更新配置
update_config({
    "agent": {
        "temperature": 0.7,
        "max_tokens": 2048
    },
    "rag": {
        "chunk_size": 1000,
        "top_k": 5
    }
})
```

#### 配置结构

```yaml
# 基本配置
app:
  name: ByteBrain
  version: 1.0.0
  env: development

# Agent 配置
agent:
  temperature: 0.7
  max_tokens: 2048
  model: gpt-4o

# RAG 配置
rag:
  chunk_size: 1000
  chunk_overlap: 200
  top_k: 5
  embedding_model: text-embedding-3-small

# 向量数据库配置
vector_db:
  type: chroma  # 或 qdrant
  host: localhost
  port: 8000
  path: ./vector_db

# MCP 服务器配置
mcpServers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/knowledge"]
  chroma:
    command: "npx"
    args: ["-y", "mcp-server-chroma"]

# 防护系统配置
guardrails:
  input:
    enabled: true
    prompt_injection: true
    pii_filter: true
  output:
    enabled: true
    hallucination_detection: true
    fact_checking: true
  behavior:
    enabled: true
    audit: true
    permissions: true

# 日志配置
logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  file: ./logs/bytebrain.log

# API 配置
api:
  host: 0.0.0.0
  port: 8000
  debug: false
  cors: true
```

---

## 命令行 API

ByteBrain 提供命令行工具，可以通过 `python -m bytebrain` 或 `bytebrain` 命令访问。

### 命令

| 命令 | 描述 | 参数 | 示例 |
|------|------|------|------|
| `init` | 初始化系统 | `--force` - 强制初始化 | `bytebrain init` |
| `add-knowledge` | 添加知识 | `path` - 文件或目录路径 | `bytebrain add-knowledge docs/` |
| `ask` | 提问 | `query` - 问题 | `bytebrain ask "什么是 LangGraph？"` |
| `retrieve` | 检索知识 | `query` - 查询关键词 | `bytebrain retrieve "Python 设计模式"` |
| `skill` | 执行技能 | `skill_name` - 技能名称<br>`input` - 输入数据 | `bytebrain skill code-coaching '{"code": "def hello(): print(\"Hello\")"}'` |
| `stats` | 查看系统状态 | 无 | `bytebrain stats` |
| `logs` | 查看日志 | `--verbose` - 详细模式 | `bytebrain logs` |
| `version` | 查看版本 | 无 | `bytebrain version` |

### 示例

```bash
# 初始化系统
bytebrain init

# 添加知识
bytebrain add-knowledge path/to/documents/

# 提问
bytebrain ask "如何使用 LangGraph？"

# 检索知识
bytebrain retrieve "RAG 技术"

# 执行技能
bytebrain skill code-coaching '{"code": "def fib(n): return n if n <= 1 else fib(n-1) + fib(n-2)", "question": "如何优化？"}'

# 查看系统状态
bytebrain stats

# 查看日志
bytebrain logs --verbose

# 查看版本
bytebrain version
```

---

## SDK 集成

### Python SDK

```python
from bytebrain import ByteBrain

# 初始化
brain = ByteBrain(api_key="YOUR_API_KEY", base_url="http://localhost:8000")

# 使用 API
response = brain.ask("什么是 MCP？")
print(response)
```

### JavaScript SDK

```javascript
const { ByteBrain } = require('bytebrain-sdk');

// 初始化
const brain = new ByteBrain({
  apiKey: 'YOUR_API_KEY',
  baseUrl: 'http://localhost:8000'
});

// 使用 API
brain.ask('什么是 LangGraph？').then(response => {
  console.log(response);
});
```

---

## 错误处理

### 常见错误

| 错误代码 | 描述 | 解决方案 |
|---------|------|----------|
| 400 | 无效请求 | 检查请求参数是否正确 |
| 401 | 未授权 | 检查 API 密钥是否有效 |
| 404 | 资源不存在 | 检查技能名称或路径是否正确 |
| 408 | 请求超时 | 增加超时时间或简化请求 |
| 500 | 服务器错误 | 检查日志并联系支持 |
| 503 | 服务不可用 | 检查服务是否运行 |

### 错误响应格式

```json
{
  "error": {
    "code": 400,
    "message": "无效的请求参数",
    "details": "缺少必要的 query 参数"
  }
}
```

---

## 最佳实践

### API 使用建议

1. **批量操作**：对于大量知识添加，使用批量 API 以提高性能
2. **缓存策略**：缓存频繁查询的结果，减少 API 调用
3. **错误处理**：实现适当的错误处理和重试机制
4. **超时设置**：为 API 调用设置合理的超时时间
5. **并发控制**：避免同时发送过多请求，合理控制并发

### 性能优化

1. **使用异步 API**：对于 I/O 密集型操作，使用异步 API
2. **分页查询**：对于大量结果，使用分页机制
3. **压缩传输**：启用 HTTP 压缩以减少传输时间
4. **批量请求**：将多个小请求合并为一个批量请求

---

## 示例代码

### 完整示例

```python
from bytebrain import ByteBrain

# 初始化 ByteBrain
brain = ByteBrain()

# 1. 添加知识
print("添加知识...")
success = brain.add_knowledge("path/to/technical_document.pdf")
print(f"知识添加: {'成功' if success else '失败'}")

# 2. 检索知识
print("\n检索知识...")
results = brain.retrieve("Python 设计模式", top_k=3)
for i, result in enumerate(results, 1):
    print(f"{i}. 分数: {result['score']:.2f}")
    print(f"   内容: {result['content'][:150]}...")
    print(f"   来源: {result['source']}")

# 3. 提问
print("\n提问...")
response = brain.ask("解释一下单例设计模式，并给出 Python 示例")
print("回答:", response)

# 4. 执行技能
print("\n执行代码教练技能...")
code = """
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
"""
result = brain.execute_skill("code-coaching", {
    "code": code,
    "question": "如何优化这段代码？"
})
print("反馈:", result['feedback'])
print("建议:", result['suggestion'])

# 5. 获取系统状态
print("\n系统状态...")
stats = brain.get_stats()
print(f"版本: {stats['version']}")
print(f"知识库大小: {stats['knowledge_base_size']} 文档")
print(f"向量数据库: {stats['vector_db_status']}")
print(f"系统状态: {stats['status']}")
```

---

## 更多

- [设计哲学](PHILOSOPHY.md) - 了解 ByteBrain 的设计理念
- [快速开始](guide/GETTING_STARTED.md) - 了解如何快速开始使用 ByteBrain
- [开发指南](guide/DEVELOPMENT.md) - 了解如何开发和扩展 ByteBrain
- [贡献指南](../.github/CONTRIBUTING.md) - 了解如何为 ByteBrain 贡献代码