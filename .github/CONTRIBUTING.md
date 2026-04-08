# 贡献指南

> **AI 时代你的第二大脑**

感谢你对 ByteBrain 项目感兴趣！

---

## 开发环境设置

### 1. 克隆仓库
```bash
git clone https://github.com/your-username/ByteBrain.git
cd ByteBrain
```

### 2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖
```bash
# 安装开发依赖
make install-dev

# 验证安装
python -m pytest tests/unit/ -v
```

---

## 开发工作流

### 1. 创建分支
```bash
git checkout -b feature/your-feature-name
```

### 2. 编写代码
- 遵循项目的 [代码规范](#代码规范)
- 添加必要的类型注解
- 编写单元测试
- 确保代码符合 ByteBrain 的设计哲学

### 3. 运行测试
```bash
# 运行单元测试
make test-unit

# 运行集成测试
make test-integration

# 运行所有测试
make test
```

### 4. 代码质量检查
```bash
# 格式化代码
make format

# 运行代码检查
make lint
```

### 5. 提交代码
```bash
git add .
git commit -m "feat: 描述你的变更"
git push origin feature/your-feature-name
```

### 6. 创建 Pull Request
在 GitHub 上创建 PR，填写 PR 模板

---

## 代码规范

### Python 代码
- **PEP 8 标准**：遵循 PEP 8 代码风格指南
- **类型提示**：使用 Python 类型提示增强代码可读性和IDE支持
- **命名规范**：
  - 类名：使用 `CamelCase`
  - 函数和变量：使用 `snake_case`
  - 常量：使用 `UPPERCASE_WITH_UNDERSCORES`
  - 私有属性和方法：使用 `_single_leading_underscore`
- **文档字符串**：使用 Google 风格的文档字符串
- **格式化工具**：使用 Black 格式化代码
- **代码检查**：遵循 Flake8 检查

### 文档
- 使用 Markdown 格式
- 代码示例要可运行
- 英文术语首字母大写
- 保持与 README.md 风格一致

---

## 提交信息规范

使用 Conventional Commits 格式：

```
<type>(<scope>): <subject>

<body>

<footer>
```

Type 类型：
- **feat**: 新功能
- **fix**: 修复 bug
- **docs**: 文档变更
- **style**: 代码格式（不影响功能）
- **refactor**: 重构
- **test**: 测试相关
- **chore**: 构建/工具相关

---

## 项目架构

ByteBrain 采用分层架构设计：

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

## 问题报告

使用 Issue 模板报告 Bug 或请求新功能：
- **Bug 报告**：使用 [bug_report.md](ISSUE_TEMPLATE/bug_report.md) 模板
- **功能请求**：使用 [feature_request.md](ISSUE_TEMPLATE/feature_request.md) 模板
- **文档问题**：使用 [documentation.md](ISSUE_TEMPLATE/documentation.md) 模板

---

## 行为准则

我们希望这个社区是包容和友好的。请尊重其他贡献者，遵循以下原则：
- 保持友善和尊重的沟通
- 接受建设性的批评
- 关注问题本身，而不是人
- 共同努力创造积极的社区环境

---

## 获取帮助

如有问题，请：
1. 查看 [README.md](../../README.md) 文档
2. 搜索现有 Issue
3. 创建新 Issue

---

## 贡献者指南

### 核心贡献领域
- **Agent 开发**：扩展和改进 Agent 系统
- **Skill 开发**：创建新的技能和功能
- **RAG 优化**：改进检索和生成系统
- **Guardrails**：增强安全防护机制
- **UI 改进**：提升用户界面体验
- **文档完善**：改进和扩展文档

### 首次贡献
如果你是首次贡献，建议从以下方面入手：
- 修复文档中的拼写错误或格式问题
- 为现有功能添加测试
- 实现小型的功能改进

---

**再次感谢你的贡献！ByteBrain 因你而更强大！**
