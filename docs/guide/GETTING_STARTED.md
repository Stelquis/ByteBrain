# 快速开始

---

## 前置要求

- **Python 3.12+**（2026 年新项目首选）
- 8GB+ RAM（推荐 16GB）
- 足够的磁盘空间用于向量数据库存储（至少 1GB）
- 网络连接（用于下载依赖和模型）

> **为什么选择 Python 3.12？**
> - Python 3.9 已于 2025-10-31 结束生命周期
> - Python 3.12 是 2026 年新项目的首选版本
> - 性能优异，新特性多，生态基本成熟
> - 支持到 2028-10，长期稳定

---

## 安装

### 步骤 1：克隆仓库

```bash
git clone https://github.com/your-username/ByteBrain.git
cd ByteBrain
```

### 步骤 2：安装依赖

```bash
# 安装基础依赖
pip install -e .

# 安装开发依赖（可选，用于开发和测试）
pip install -e "[dev]"
```

### 步骤 3：验证安装

```bash
# 检查版本
python -m bytebrain --version

# 运行基本测试
python -m pytest tests/unit/ -v
```

---

## 配置

### 环境变量配置

1. **创建环境变量文件**：
   ```bash
   cp .env.example .env
   ```

2. **编辑 .env 文件**：
   ```env
   # API 密钥
   OPENAI_API_KEY=your-openai-api-key
   ANTHROPIC_API_KEY=your-anthropic-api-key
   
   # 向量数据库配置
   VECTOR_DB_TYPE=chroma  # 或 qdrant
   VECTOR_DB_HOST=localhost
   VECTOR_DB_PORT=8000
   
   # 应用配置
   APP_ENV=development  # 或 production
   DEBUG=True
   
   # 日志配置
   LOG_LEVEL=INFO
   ```

### 数据源配置

1. **编辑 config.yaml 文件**：
   ```yaml
   # MCP 服务器配置
   mcpServers:
     filesystem:
       command: "npx"
       args: ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/knowledge"]
     
     chroma:
       command: "npx"
       args: ["-y", "mcp-server-chroma"]
       env:
         CHROMA_HOST: "localhost"
         CHROMA_PORT: "8000"
     
     notion:
       command: "npx"
       args: ["-y", "mcp-server-notion"]
       env:
         NOTION_API_KEY: "${NOTION_API_KEY}"
   
   # RAG 配置
   rag:
     chunk_size: 1000
     chunk_overlap: 200
     top_k: 5
     
   # Agent 配置
   agent:
     temperature: 0.7
     max_tokens: 2048
   ```

### 首次运行配置

1. **初始化向量数据库**：
   ```bash
   python -m bytebrain init
   ```

2. **添加初始知识**：
   ```bash
   python -m bytebrain add-knowledge "path/to/your/documents"
   ```

---

## 运行

### 方法 1：使用 Make 命令

```bash
make run
```

### 方法 2：直接运行 Streamlit 应用

```bash
streamlit run bytebrain/ui/streamlit_app.py
```

### 方法 3：使用 Python 模块

```bash
python -m bytebrain run
```

打开浏览器访问 `http://localhost:8501`

---

## 使用指南

### 基本操作

1. **提问**：在输入框中输入你的问题，点击"发送"按钮
2. **上传文件**：点击"上传文件"按钮，选择要添加到知识库的文件
3. **管理知识库**：在"知识库"标签页中查看和管理已添加的知识
4. **技能执行**：在"技能"标签页中选择并执行各种技能

### 高级功能

1. **自定义提示**：在设置中配置系统提示和技能提示
2. **数据源管理**：添加和管理多个数据源
3. **性能监控**：查看系统运行状态和性能指标
4. **导出数据**：导出知识库和对话历史

---

## 常见问题解答

### 安装问题

**Q: 安装依赖时出现权限错误？**
A: 使用 `pip install --user` 或创建虚拟环境后安装。

**Q: 找不到 Python 3.12？**
A: 请从 [Python 官网](https://www.python.org/downloads/) 下载并安装最新版本。

### 运行问题

**Q: 启动时出现端口被占用错误？**
A: 尝试修改 Streamlit 端口：`streamlit run bytebrain/ui/streamlit_app.py --server.port 8502`

**Q: 向量数据库连接失败？**
A: 确保向量数据库服务正在运行，检查配置文件中的连接信息。

### 使用问题

**Q: 回答不够准确？**
A: 尝试添加更多相关知识，或调整 RAG 配置中的 `top_k` 参数。

**Q: 技能执行失败？**
A: 检查技能配置和依赖是否正确安装。

### 性能问题

**Q: 响应速度慢？**
A: 增加 RAM 容量，或使用更快的向量数据库。

**Q: 内存使用过高？**
A: 调整 `chunk_size` 参数，减少单次处理的文本量。

---

## 故障排除

### 日志查看

```bash
# 查看应用日志
python -m bytebrain logs

# 查看详细日志
python -m bytebrain logs --verbose
```

### 常见错误及解决方案

| 错误信息 | 可能原因 | 解决方案 |
|---------|---------|---------|
| `API key not found` | 环境变量未设置 | 检查 .env 文件中的 API 密钥配置 |
| `VectorDB connection error` | 向量数据库未运行 | 启动向量数据库服务 |
| `Skill execution failed` | 技能依赖缺失 | 安装技能所需的依赖 |
| `MemoryError` | 内存不足 | 增加 RAM 或调整配置参数 |

---

## 下一步

- **阅读 [设计哲学](../PHILOSOPHY.md)** - 了解 ByteBrain 的设计理念和技术架构
- **查看 [开发指南](./DEVELOPMENT.md)** - 了解如何开发和扩展 ByteBrain
- **探索 [API 文档](../API.md)** - 了解 ByteBrain 的 API 接口
- **查看 [使用示例](../examples/)** - 学习如何使用 ByteBrain 的各种功能

---

## 联系支持

如果遇到问题，可以通过以下方式获取支持：

- **GitHub Issues**：在 [GitHub 仓库](https://github.com/your-username/ByteBrain/issues) 提交问题
- **Discord 社区**：加入 ByteBrain 社区 Discord 服务器
- **文档**：查看完整的 [文档](https://bytebrain-docs.example.com)
