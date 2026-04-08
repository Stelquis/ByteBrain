# ByteBrain 项目结构说明

> 整理日期：2026-04-08

---

## 📁 项目结构总览

```
ByteBrain/
├── 📁 assets/              # 资源文件（图片、PPT）
├── 📁 docs/                # 文档目录
│   ├── 📁 archive/         # 旧版本/重复文档（归档）
│   └── ... (核心文档)
├── 📁 legacy/              # 旧代码（保留用于参考）
├── 📁 src/                 # 新代码目录（待开发）
│   ├── core/               # 核心模块
│   ├── data/               # 数据模块
│   ├── ui/                 # UI 模块
│   └── utils/              # 工具模块
├── 📁 tests/               # 测试目录
├── .gitignore              # Git 忽略文件
├── LICENSE                 # MIT 许可证
├── README.md               # 项目主页（最新版）
└── requirements.txt        # 依赖列表
```

---

## 📁 各目录详细说明

### 1. assets/ - 资源文件
存放图片、PPT 等资源：
- `ByteBrain.png` - 项目封面图
- `ByteBrain.pptx` - 项目介绍 PPT
- `logo.png` - Logo
- `background.png` - 背景图

---

### 2. docs/ - 文档目录（核心）

#### 核心文档（保留）
| 文档 | 说明 | 优先级 |
|------|------|-------|
| [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md) | 设计哲学宣言（最新版） | ⭐⭐⭐⭐⭐ |
| [NEEDS_ANALYSIS_2026.md](NEEDS_ANALYSIS_2026.md) | 2026年需求分析 | ⭐⭐⭐⭐⭐ |
| [TECH_PLAYGROUND_2026.md](TECH_PLAYGROUND_2026.md) | 2026年技术全景 | ⭐⭐⭐⭐⭐ |
| [SKILL_PROMPT_GUARDRAILS_2026.md](SKILL_PROMPT_GUARDRAILS_2026.md) | Skill/Prompt/Guardrails 详解 | ⭐⭐⭐⭐⭐ |
| [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) | 技术实施方案 | ⭐⭐⭐⭐ |
| [PROJECT_POSITIONING.md](PROJECT_POSITIONING.md) | 项目定位与价值体系 | ⭐⭐⭐⭐ |
| [KNOWLEDGE_BASE_GUIDELINE.md](KNOWLEDGE_BASE_GUIDELINE.md) | 知识库内容标准 | ⭐⭐⭐⭐ |

#### archive/ - 归档文档（旧版本）
已归档的旧文档，保留用于参考：
- `DESIGN_PHILOSOPHY.md` - 旧版设计哲学
- `AI_AGENT_STRATEGY.md` - 内容已整合到新版
- `PROJECT_PLAN.md` - 内容已整合
- `PRODUCT_FEATURES.md` - 内容已整合

---

### 3. legacy/ - 旧代码（保留）
旧版本的代码，保留用于参考和迁移：
- `app.py` - 基础对话应用
- `appFineTuning.py` - 微调版本
- `appRAG.py` - RAG 版本
- `download_model.py` - 模型下载脚本
- `finetune_model.py` - 微调脚本
- `start.sh` - 启动脚本
- `knowledge.txt` - 旧知识库
- `finetune_data.json` - 旧微调数据

---

### 4. src/ - 新代码目录（待开发）
这是未来的代码目录，采用模块化设计：

```
src/
├── core/                  # 核心模块
│   ├── llm.py            # 大语言模型封装
│   ├── embedding.py      # 向量模型封装
│   ├── vector_store.py   # 向量存储
│   ├── rag.py            # RAG 系统
│   ├── agent.py          # Agent 框架
│   └── skills/           # Skill 系统
│       ├── __init__.py
│       └── ...
├── ui/                    # UI 模块
│   └── streamlit_app.py
├── data/                  # 数据模块
│   └── data_loader.py
└── utils/                 # 工具模块
    ├── config.py
    ├── logger.py
    └── guardrails.py
```

当前已有基础文件：
- `utils/config.py` - 配置管理
- `utils/logger.py` - 日志系统

---

### 5. tests/ - 测试目录
待开发的测试模块：
```
tests/
├── __init__.py
├── test_core/
│   ├── test_llm.py
│   ├── test_embedding.py
│   ├── test_rag.py
│   └── test_agent.py
└── test_utils/
    ├── test_config.py
    └── test_logger.py
```

---

## 📖 阅读建议

### 第一遍：理解项目定位
1. [README.md](../README.md) - 项目主页，快速了解
2. [PROJECT_POSITIONING.md](PROJECT_POSITIONING.md) - 三重价值体系
3. [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md) - 完整设计哲学

### 第二遍：理解技术栈
1. [TECH_PLAYGROUND_2026.md](TECH_PLAYGROUND_2026.md) - 2026 年技术全景
2. [SKILL_PROMPT_GUARDRAILS_2026.md](SKILL_PROMPT_GUARDRAILS_2026.md) - 核心"小东西"详解
3. [NEEDS_ANALYSIS_2026.md](NEEDS_ANALYSIS_2026.md) - 真实需求分析

### 第三遍：开始实施
1. [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) - 具体实施方案
2. [KNOWLEDGE_BASE_GUIDELINE.md](KNOWLEDGE_BASE_GUIDELINE.md) - 知识库建设

---

## 🚀 下一步行动

### 选项一：从 Prompt 开始（最简单，1周）
1. 创建 `prompts/` 目录
2. 编写 System Prompt
3. 创建 Few-Shot 示例库
4. 实现 Self-Check 验证

### 选项二：从 Guardrails 开始（安全优先，1-2周）
1. 实现输入/输出防护
2. 集成 Llama Guard
3. 实现知识边界规则
4. 建立验证体系

### 选项三：从 Skill 开始（模块化，2-3周）
1. 创建 `skills/` 目录
2. 实现 Knowledge Retrieval Skill
3. 实现 Concept Explanation Skill
4. 实现 Code Coaching Skill

### 选项四：从 RAG 开始（核心能力，2-3周）
1. 集成 LlamaIndex
2. 使用 Qdrant/Chroma
3. 实现混合检索
4. 实现知识溯源

---

## 📊 文档统计

| 类别 | 数量 |
|------|------|
| 核心文档 | 7 个 |
| 归档文档 | 4 个 |
| 代码文件（已有） | 6 个 |
| 资源文件 | 4 个 |
| 旧代码（参考） | 8 个 |

---

## 💡 重要提示

### 不要删除的内容
- `legacy/` 目录下的旧代码 - 保留用于参考和迁移
- `docs/archive/` 目录下的文档 - 保留历史版本

### 可以新增的目录
- `prompts/` - Prompt 模板库
- `skills/` - Skill 系统
- `guardrails/` - 防护规则
- `config/` - 配置文件

---

## 📝 版本历史

| 版本 | 日期 | 说明 |
|------|------|------|
| 2.0 | 2026-04-08 | 仓库大整理，重新定位项目 |
| 1.0 | 2024 | 初始版本，Datawhale 夏令营项目 |

---

**仓库整理完成！现在结构清晰，开始你的 AI 技术试验场之旅吧！**
