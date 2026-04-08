#!/usr/bin/env python3
"""
概念解释技能

解释概念、类比比喻、循序渐进。
"""

from typing import Dict, Any, List


def execute_skill(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """执行概念解释技能
    
    Args:
        input_data: 输入数据，包含 concept 和 level 等字段
        
    Returns:
        执行结果，包含 explanation、analogies、examples 等字段
    """
    # 提取输入参数
    concept = input_data.get("concept", "")
    level = input_data.get("level", "beginner")
    
    # 这里应该实现实际的概念解释逻辑
    # 暂时返回模拟数据
    
    # 生成解释
    explanation = f"{concept} 的概念解释：\n\n"
    explanation += "这是一个复杂的概念，涉及多个方面...\n\n"
    explanation += f"针对 {level} 水平的解释：..."
    
    # 生成类比
    analogies = [
        f"{concept} 就像...",
        f"可以把 {concept} 理解为..."
    ]
    
    # 生成例子
    examples = [
        f"例如，在 {concept} 中...",
        f"另一个例子是..."
    ]
    
    return {
        "explanation": explanation,
        "analogies": analogies,
        "examples": examples,
        "concept": concept,
        "level": level
    }


def get_skill_info() -> Dict[str, Any]:
    """获取技能信息
    
    Returns:
        技能信息
    """
    return {
        "name": "concept-explanation",
        "version": "1.0.0",
        "description": "解释概念、类比比喻、循序渐进",
        "triggers": ["concept_question", "learning_request", "explanation_needed"]
    }
