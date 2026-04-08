# ByteBrain 仓库规范化方案

## 目标
建立一个符合开源社区标准、企业级的 Github 仓库结构

---

## 📁 最终仓库结构

```
ByteBrain/
├── .github/                    # GitHub 特定文件
│   ├── ISSUE_TEMPLATE/        # Issue 模板
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── documentation.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── workflows/             # GitHub Actions
│   │   └── ci.yml
│   └── CONTRIBUTING.md
├── .gitignore                 # Git 忽略文件
├── .pre-commit-config.yaml     # Pre-commit 钩子配置
├── LICENSE                    # MIT 许可证
├── README.md                  # 项目主页
├── pyproject.toml            # Python 项目配置
├── requirements.txt            # 依赖列表
├── setup.py                  # 包安装配置
├── Makefile                  # 自动化任务
├── docs/                     # 文档目录
│   ├── README.md            # 文档索引
│   ├── design/              # 设计文档
│   │   └── DESIGN_PHILOSOPHY.md
│   ├── user/                # 用户文档
│   │   ├── GETTING_STARTED.md
│   │   ├── TUTORIAL.md
│   │   └── FAQ.md
│   ├── developer/           # 开发者文档
│   │   ├── ARCHITECTURE.md
│   │   ├── DEVELOPMENT_GUIDE.md
│   │   ├── API.md
│   │   └── TESTING.md
│   └── archive/             # 归档文档
├── assets/                   # 资源文件
│   ├── images/
│   │   ├── logo.png
│   │   ├── architecture.png
│   │   └── demo.gif
│   └── slides/
│       └── ByteBrain.pptx
├── legacy/                   # 旧代码（保留参考）
├── scripts/                  # 脚本目录
│   ├── download_model.sh
│   ├── finetune.sh
│   └── evaluate.py
├── bytebrain/                # 包目录（替代 src）
│   ├── __init__.py
│   ├── __main__.py
│   ├── core/               # 核心模块
│   │   ├── __init__.py
│   │   ├── llm.py
│   │   ├── embedding.py
│   │   ├── vector_store.py
│   │   ├── rag.py
│   │   └── agent.py
│   ├── skills/             # Skill 系统
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── knowledge_retrieval.py
│   │   ├── code_coaching.py
│   │   └── concept_explanation.py
│   ├── guardrails/         # 防护系统
│   │   ├── __init__.py
│   │   ├── input.py
│   │   ├── output.py
│   │   └── rules.py
│   ├── prompts/            # Prompt 系统
│   │   ├── __init__.py
│   │   ├── system.py
│   │   ├── templates.py
│   │   └── few_shot.py
│   ├── ui/                 # UI 模块
│   │   ├── __init__.py
│   │   └── streamlit_app.py
│   └── utils/              # 工具模块
│       ├── __init__.py
│       ├── config.py
│       └── logger.py
├── tests/                    # 测试目录
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   │   ├── test_core/
│   │   ├── test_skills/
│   │   ├── test_guardrails/
│   │   └── test_utils/
│   └── integration/
│       └── test_end_to_end.py
└── examples/                 # 示例目录
    ├── quickstart.py
    ├── custom_skill.py
    └── rag_example.py
```

---

## 🔄 迁移计划

### 阶段一：创建新结构
1. 创建 `bytebrain/` 目录（替代 `src/`）
2. 创建 `.github/` 目录
3. 创建 `scripts/` 目录
4. 创建 `examples/` 目录
5. 完善 `docs/` 结构

### 阶段二：移动现有文件
1. 移动 `src/utils/` → `bytebrain/utils/`
2. 移动资源文件到 `assets/`
3. 移动旧脚本到 `scripts/`

### 阶段三：创建配置文件
1. `pyproject.toml`
2. `setup.py`
3. `Makefile`
4. `.pre-commit-config.yaml`
5. GitHub 相关文件

### 阶段四：更新文档
1. 重组 `docs/` 目录
2. 创建各分类文档
3. 更新 `README.md`

---

## 📋 文件命名规范

### 目录命名
- 全小写
- 使用下划线分隔单词
- 复数形式表示集合

### 文件命名
- 模块文件：全小写，下划线分隔
- 文档文件：全大写，下划线分隔（如 README.md、GETTING_STARTED.md）
- 配置文件：. 前缀，全小写
- 脚本文件：全小写，下划线分隔

### 类命名
- 大驼峰命名法（如 `KnowledgeRetrievalSkill`）
- 名词形式

### 函数命名
- 全小写，下划线分隔
- 动词开头

---

## ✅ 检查清单

整理完成后请确认：
- [ ] 所有文件符合命名规范
- [ ] 目录结构清晰合理
- [ ] 配置文件完整
- [ ] 文档分类清晰
- [ ] 旧内容已归档
- [ ] README.md 已更新
