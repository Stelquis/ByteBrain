# 贡献指南

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
make install-dev
```

---

## 开发工作流

### 1. 创建分支
```bash
git checkout -b feature/your-feature-name
```

### 2. 编写代码
- 遵循项目的代码风格
- 添加必要的类型注解
- 编写单元测试

### 3. 运行测试
```bash
make test
```

### 4. 代码格式化
```bash
make format
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
- 使用 Black 格式化代码
- 遵循 Flake8 检查
- 使用类型注解（Type Hints）
- 遵循 Google 风格的文档字符串

### 文档
- 使用 Markdown 格式
- 代码示例要可运行
- 英文术语首字母大写

---

## 提交信息规范

使用 Conventional Commits 格式：

```
<type>(<scope>): <subject>

<body>

<footer>
```

Type 类型：
- feat: 新功能
- fix: 修复 bug
- docs: 文档变更
- style: 代码格式（不影响功能）
- refactor: 重构
- test: 测试相关
- chore: 构建/工具相关

---

## 问题报告

使用 Issue 模板报告 Bug 或请求新功能。

---

## 行为准则

我们希望这个社区是包容和友好的。请尊重其他贡献者。

---

## 获取帮助

如有问题，请：
1. 查看文档
2. 搜索现有 Issue
3. 创建新 Issue

---

**再次感谢你的贡献！**
