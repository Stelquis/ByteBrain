# 开发指南

---

## 环境设置

### 步骤 1：创建虚拟环境

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
env\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 步骤 2：安装开发依赖

```bash
# 安装开发依赖
pip install -e "[dev]"

# 验证安装
pip list | grep bytebrain
```

---

## Python 版本要求

| 版本 | 状态 | 说明 |
|------|------|------|
| 3.9 | ❌ 已结束 | 2025-10-31 结束支持 |
| 3.10 | ⚠️ 安全维护 | 2026-10 结束 |
| 3.11 | ✅ 企业稳定 | 2027-10 结束 |
| **3.12** | ✅ **新项目首选** | 2028-10 结束 |
| 3.13 | ✅ 最新稳定版 | 2029-10 结束 |

> **ByteBrain 选择 Python 3.12**：作为 2026 年的新项目，3.12 是最佳选择——新特性多、性能好、生态成熟、支持到 2028 年。

---

## 开发命令

| 命令 | 说明 | 详细信息 |
|------|------|----------|
| `make install` | 安装基础依赖 | 安装运行所需的核心依赖 |
| `make install-dev` | 安装开发依赖 | 安装开发、测试和 lint 工具 |
| `make test` | 运行测试 | 运行完整的测试套件 |
| `make test-unit` | 运行单元测试 | 仅运行单元测试 |
| `make test-integration` | 运行集成测试 | 仅运行集成测试 |
| `make lint` | 运行代码检查 | 使用 flake8 和 mypy 检查代码质量 |
| `make format` | 格式化代码 | 使用 black 和 isort 格式化代码 |
| `make run` | 启动应用 | 启动 Streamlit 应用 |
| `make build` | 构建包 | 构建 Python 包 |
| `make clean` | 清理环境 | 清理构建产物和缓存 |

---

## 项目结构

### 核心目录结构

```
bytebrain/
├── core/               # 核心模块
│   ├── agent.py        # Agent 核心逻辑
│   ├── rag.py          # RAG 核心逻辑
│   ├── workflow.py     # 工作流定义
│   └── __init__.py     # 模块初始化
├── skills/             # Skill 系统
│   ├── knowledge-retrieval/  # 知识检索技能
│   ├── code-coaching/        # 代码教练技能
│   ├── concept-explanation/  # 概念解释技能
│   └── __init__.py           # 模块初始化
├── guardrails/         # 防护系统
│   ├── input_guard.py  # 输入防护
│   ├── output_guard.py # 输出防护
│   ├── behavior_guard.py # 行为防护
│   └── __init__.py     # 模块初始化
├── prompts/            # Prompt 系统
│   ├── system/         # 系统提示
│   ├── skill/          # 技能提示
│   └── __init__.py     # 模块初始化
├── ui/                 # UI 模块
│   ├── streamlit_app.py # Streamlit 应用
│   ├── components/     # UI 组件
│   └── __init__.py     # 模块初始化
├── utils/              # 工具模块
│   ├── config.py       # 配置管理
│   ├── logger.py       # 日志管理
│   ├── embedding.py    # 嵌入工具
│   └── __init__.py     # 模块初始化
├── __init__.py         # 包初始化
├── __main__.py         # 命令行入口
└── cli.py              # 命令行工具
```

### 测试目录结构

```
tests/
├── unit/               # 单元测试
│   ├── test_core.py    # 核心模块测试
│   ├── test_skills.py  # 技能系统测试
│   └── __init__.py     # 模块初始化
├── integration/        # 集成测试
│   ├── test_workflow.py # 工作流测试
│   ├── test_rag.py     # RAG 系统测试
│   └── __init__.py     # 模块初始化
├── __init__.py         # 测试包初始化
└── conftest.py         # 测试配置
```

---

## 代码规范

### Python 代码规范

1. **PEP 8 标准**：遵循 PEP 8 代码风格指南
2. **类型提示**：使用 Python 类型提示增强代码可读性和IDE支持
3. **命名规范**：
   - 类名：使用 `CamelCase`
   - 函数和变量：使用 `snake_case`
   - 常量：使用 `UPPERCASE_WITH_UNDERSCORES`
   - 私有属性和方法：使用 `_single_leading_underscore`

### 文档规范

1. **文档字符串**：使用 Google 风格的文档字符串
2. **模块文档**：每个模块都应有模块级文档
3. **函数文档**：每个函数都应有详细的文档字符串
4. **类型注解**：为所有函数参数和返回值添加类型注解

### 代码示例

```python
"""示例模块文档"""

from typing import List, Dict, Optional


class ExampleClass:
    """示例类
    
    这是一个示例类，展示了代码规范
    
    Attributes:
        name: str - 类的名称
        value: int - 类的值
    """
    
    def __init__(self, name: str, value: int) -> None:
        """初始化示例类
        
        Args:
            name: 类的名称
            value: 类的值
        """
        self.name = name
        self.value = value
    
    def process_data(self, data: List[str]) -> Dict[str, int]:
        """处理数据
        
        Args:
            data: 要处理的数据列表
            
        Returns:
            处理后的字典，键为数据项，值为长度
        """
        result = {}
        for item in data:
            result[item] = len(item)
        return result
```

---

## 开发最佳实践

### 模块化开发

1. **单一职责**：每个模块和函数应只有一个职责
2. **依赖注入**：使用依赖注入提高代码可测试性
3. **接口抽象**：定义清晰的接口，便于扩展和测试
4. **配置外部化**：将配置信息从代码中分离出来

### 测试最佳实践

1. **测试覆盖**：目标是 80%+ 的代码覆盖率
2. **测试隔离**：每个测试应独立运行，不依赖外部状态
3. **测试命名**：使用清晰的测试命名，如 `test_function_name_should_behavior`
4. **测试数据**：使用有意义的测试数据，覆盖边界情况

### 版本控制

1. **Git 工作流**：使用 Git Flow 工作流
2. **提交信息**：使用清晰的提交信息，如 `feat: 添加新功能`
3. **分支管理**：
   - `main`：稳定版本
   - `develop`：开发分支
   - `feature/*`：功能分支
   - `bugfix/*`：bug 修复分支

### 性能优化

1. **代码性能**：避免不必要的计算和内存使用
2. **缓存策略**：合理使用缓存减少重复计算
3. **异步处理**：对于 I/O 密集型操作使用异步
4. **数据库优化**：优化查询和索引

---

## 扩展开发

### 开发新技能

1. **创建技能目录**：
   ```bash
   mkdir -p bytebrain/skills/new-skill
   ```

2. **创建 SKILL.md 文件**：
   ```markdown
   ---   
   name: new-skill
   version: 1.0.0
   description: 新技能描述
   triggers:
     - user_question
   ---
   
   # New Skill
   
   ## Purpose
   技能的目的和用途
   
   ## Workflow
   1. 步骤 1
   2. 步骤 2
   3. 步骤 3
   
   ## Constraints
   - 约束条件 1
   - 约束条件 2
   ```

3. **实现技能逻辑**：
   ```python
   # bytebrain/skills/new-skill/skill.py
   def execute_skill(input_data: dict) -> dict:
       """执行新技能
       
       Args:
           input_data: 输入数据
           
       Returns:
           执行结果
       """
       # 技能逻辑
       return {"result": "技能执行结果"}
   ```

### 开发新 Agent

1. **在 core/agent.py 中添加新 Agent**：
   ```python
   class NewAgent:
       """新 Agent
       
       新 Agent 的描述
       """
       
       def __init__(self):
           self.name = "New Agent"
       
       def process(self, task: str) -> str:
           """处理任务
           
           Args:
               task: 任务描述
               
           Returns:
               处理结果
           """
           # Agent 逻辑
           return f"处理结果: {task}"
   ```

2. **在工作流中集成新 Agent**：
   ```python
   # core/workflow.py
   def build_workflow():
       # 现有代码
       new_agent = NewAgent()
       # 集成到工作流
   ```

---

## 部署指南

### 本地部署

```bash
# 安装依赖
pip install -e .

# 启动应用
make run
```

### 容器部署

1. **构建 Docker 镜像**：
   ```bash
   docker build -t bytebrain .
   ```

2. **运行容器**：
   ```bash
   docker run -p 8501:8501 bytebrain
   ```

### 云部署

1. **Heroku 部署**：
   - 连接 GitHub 仓库
   - 配置环境变量
   - 部署应用

2. **AWS 部署**：
   - 创建 EC2 实例
   - 安装依赖
   - 配置安全组
   - 启动应用

---

## 调试技巧

### 日志调试

```python
# 使用内置日志
from bytebrain.utils.logger import logger

logger.info("信息日志")
logger.debug("调试日志")
logger.warning("警告日志")
logger.error("错误日志")
```

### 断点调试

1. **使用 VS Code**：
   - 设置断点
   - 启动调试模式
   - 单步执行代码

2. **使用 pdb**：
   ```python
   import pdb
   pdb.set_trace()  # 断点
   ```

### 性能分析

```bash
# 使用 cProfile 分析性能
python -m cProfile -o profile.out bytebrain/ui/streamlit_app.py

# 查看分析结果
python -m pstats profile.out
```

---

## 代码审查

### 审查流程

1. **创建 Pull Request**：
   - 从 feature 分支创建 PR 到 develop 分支
   - 填写详细的 PR 描述
   - 关联相关的 issue

2. **代码审查**：
   - 检查代码风格和规范
   - 验证功能实现
   - 检查测试覆盖
   - 提供改进建议

3. **合并流程**：
   - 解决所有审查意见
   - 确保所有测试通过
   - 合并到 develop 分支

### 审查要点

1. **代码质量**：
   - 代码风格是否符合规范
   - 命名是否清晰
   - 注释是否充分

2. **功能实现**：
   - 是否满足需求
   - 边界情况是否处理
   - 错误处理是否完善

3. **性能考量**：
   - 是否存在性能瓶颈
   - 资源使用是否合理

4. **安全性**：
   - 是否存在安全漏洞
   - 敏感信息是否妥善处理

---

## 更多

- [设计哲学](../PHILOSOPHY.md) - 了解 ByteBrain 的设计理念
- [快速开始](./GETTING_STARTED.md) - 了解如何快速开始使用 ByteBrain
- [API 文档](../API.md) - 了解 ByteBrain 的 API 接口
- [贡献指南](../../.github/CONTRIBUTING.md) - 了解如何为 ByteBrain 贡献代码
