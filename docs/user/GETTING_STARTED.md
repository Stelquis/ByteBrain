# 快速开始

欢迎使用 ByteBrain！

---

## 前置要求

- Python 3.9+
- 8GB+ RAM（推荐 16GB）
- Git

---

## 安装步骤

### 1. 克隆仓库
```bash
git clone https://github.com/your-username/ByteBrain.git
cd ByteBrain
```

### 2. 创建虚拟环境（推荐）
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖
```bash
pip install -e .
```

开发模式（包含所有依赖）：
```bash
pip install -e ".[dev,full]"
```

---

## 快速启动

### 运行应用
```bash
make run
```

或者直接使用 Streamlit：
```bash
streamlit run bytebrain/ui/streamlit_app.py
```

---

## 下一步

- 阅读 [设计哲学](../design/DESIGN_PHILOSOPHY.md) 了解项目理念
- 查看 [教程](./TUTORIAL.md) 学习高级用法
- 参考 [常见问题](./FAQ.md) 解决问题

---

## 获取帮助

如有问题，请：
- 查看 [常见问题](./FAQ.md)
- 创建 [Issue](../../.github/ISSUE_TEMPLATE/)
