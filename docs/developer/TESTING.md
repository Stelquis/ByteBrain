# 测试指南

---

## 测试框架

ByteBrain 使用 pytest 作为测试框架。

---

## 运行测试

### 运行所有测试
```bash
make test
```

### 运行特定测试
```bash
pytest tests/unit/test_core/
```

### 运行测试并生成覆盖率报告
```bash
make test-cov
```

---

## 测试目录结构

```
tests/
├── conftest.py          # pytest 配置
├── unit/                # 单元测试
│   ├── test_core/
│   ├── test_skills/
│   ├── test_guardrails/
│   └── test_utils/
└── integration/          # 集成测试
    └── test_end_to_end.py
```

---

## 编写测试

### 单元测试示例
```python
import pytest
from bytebrain.core.llm import LLM

def test_llm_initialization():
    """测试 LLM 初始化"""
    config = Config()
    llm = LLM(config)
    assert llm is not None

def test_llm_generate():
    """测试 LLM 生成"""
    config = Config()
    llm = LLM(config)
    result = llm.generate("Hello")
    assert isinstance(result, str)
```

---

## 测试最佳实践

1. **每个模块都要有测试**
2. **使用 Fixtures 复用测试数据**
3. **测试异常情况**
4. **保持测试独立**
5. **使用描述性的测试名称**

---

## 更多文档

- [开发指南](./DEVELOPMENT_GUIDE.md)
- [架构设计](./ARCHITECTURE.md)
- [API 文档](./API.md)
