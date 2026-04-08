#!/usr/bin/env python3
"""
代码教练技能

解释代码、审查问题、提供示例。
"""

from typing import Dict, Any


def execute_skill(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """执行代码教练技能
    
    Args:
        input_data: 输入数据，包含 code 和 question 等字段
        
    Returns:
        执行结果，包含 feedback、suggestion、explanation 等字段
    """
    # 提取输入参数
    code = input_data.get("code", "")
    question = input_data.get("question", "")
    
    # 这里应该实现实际的代码分析逻辑
    # 暂时返回模拟数据
    
    # 生成反馈
    feedback = f"代码分析结果：\n{code}\n\n问题分析：{question}"
    
    # 生成建议
    suggestion = "优化建议：\n" + """def optimized_function():
    # 添加类型注解
    # 使用更清晰的变量名
    # 优化算法复杂度
    pass"""
    
    # 生成解释
    explanation = "代码解释：\n这段代码实现了...\n\n改进建议：..."
    
    return {
        "feedback": feedback,
        "suggestion": suggestion,
        "explanation": explanation,
        "code": code,
        "question": question
    }


def get_skill_info() -> Dict[str, Any]:
    """获取技能信息
    
    Returns:
        技能信息
    """
    return {
        "name": "code-coaching",
        "version": "1.0.0",
        "description": "解释代码、审查问题、提供示例",
        "triggers": ["code_question", "code_review", "code_optimization"]
    }
