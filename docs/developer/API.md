# API 文档

---

## 概述

本文档描述 ByteBrain 的公共 API。

---

## 核心模块

### bytebrain.core.llm

#### LLM 类
大语言模型封装类。

```python
class LLM:
    def __init__(self, config: Config):
        """
        初始化 LLM
        
        Args:
            config: 配置对象
        """
    
    def generate(self, prompt: str, **kwargs) -> str:
        """
        生成文本
        
        Args:
            prompt: 输入提示
            **kwargs: 其他参数
        
        Returns:
            生成的文本
        """
```

### bytebrain.core.rag

#### RAGSystem 类
RAG 系统类。

```python
class RAGSystem:
    def __init__(self, knowledge_base, llm):
        """
        初始化 RAG 系统
        
        Args:
            knowledge_base: 知识库
            llm: LLM 实例
        """
    
    def query(self, question: str, top_k: int = 3) -> dict:
        """
        检索并回答问题
        
        Args:
            question: 用户问题
            top_k: 返回 top_k 个结果
        
        Returns:
            包含回答和来源的字典
        """
```

---

## Skill 模块

### bytebrain.skills.base

#### Skill 基类
所有 Skill 的基类。

```python
class Skill:
    name: str
    description: str
    
    def execute(self, **kwargs) -> dict:
        """
        执行 Skill
        
        Args:
            **kwargs: 输入参数
        
        Returns:
            执行结果
        """
        raise NotImplementedError
```

---

## 更多信息

- [开发指南](./DEVELOPMENT_GUIDE.md)
- [架构设计](./ARCHITECTURE.md)
- [测试指南](./TESTING.md)

---

**注意**：本文档会持续更新，请关注最新版本。
