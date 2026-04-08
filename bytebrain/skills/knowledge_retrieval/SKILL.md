---
name: knowledge-retrieval
version: 1.0.0
description: 从知识库检索信息并生成回答
triggers:
  - user_question
  - search_request
---

# Knowledge Retrieval Skill

## Purpose
从用户的知识库中检索相关信息，生成准确、可溯源的回答。

## Workflow
1. 分析问题 → 提取关键词和实体
2. 检索知识 → 混合检索 + 重排序
3. 生成回答 → 标注来源

## Constraints
- 只使用知识库中的信息
- 必须标注来源
- 置信度 < 0.7 时告知用户
