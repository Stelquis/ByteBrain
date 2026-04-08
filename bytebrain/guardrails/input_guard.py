#!/usr/bin/env python3
"""
输入防护

实现 Prompt Injection 检测、PII 过滤和话题边界检查。
"""

from typing import Dict, Any, Tuple, Optional, List


def detect_prompt_injection(input_text: str) -> Tuple[bool, str]:
    """检测 Prompt Injection
    
    Args:
        input_text: 输入文本
        
    Returns:
        (是否存在注入, 检测结果)
    """
    # 这里应该实现实际的 Prompt Injection 检测逻辑
    # 暂时返回模拟数据
    injection_patterns = [
        "ignore previous instructions",
        "system prompt",
        "override",
        "bypass"
    ]
    
    for pattern in injection_patterns:
        if pattern in input_text.lower():
            return True, f"检测到 Prompt Injection: {pattern}"
    
    return False, "未检测到 Prompt Injection"


def filter_pii(input_text: str) -> str:
    """过滤 PII (Personally Identifiable Information)
    
    Args:
        input_text: 输入文本
        
    Returns:
        过滤后的文本
    """
    # 这里应该实现实际的 PII 过滤逻辑
    # 暂时返回原始文本
    # 实际实现应该过滤邮箱、电话、地址等敏感信息
    return input_text


def check_topic_boundary(input_text: str, allowed_topics: Optional[List[Any]] = None) -> Tuple[bool, str]:
    """检查话题边界
    
    Args:
        input_text: 输入文本
        allowed_topics: 允许的话题列表
        
    Returns:
        (是否在边界内, 检查结果)
    """
    # 这里应该实现实际的话题边界检查逻辑
    # 暂时返回模拟数据
    if allowed_topics:
        # 简单的话题匹配
        for topic in allowed_topics:
            if topic in input_text.lower():
                return True, f"话题 '{topic}' 在允许范围内"
        return False, "话题不在允许范围内"
    
    return True, "话题边界检查通过"


def process_input(input_text: str, allowed_topics: Optional[List[Any]] = None) -> Dict[str, Any]:
    """处理输入
    
    Args:
        input_text: 输入文本
        allowed_topics: 允许的话题列表
        
    Returns:
        处理结果
    """
    # 1. 检测 Prompt Injection
    injection_detected, injection_result = detect_prompt_injection(input_text)
    
    # 2. 过滤 PII
    filtered_text = filter_pii(input_text)
    
    # 3. 检查话题边界
    within_boundary, boundary_result = check_topic_boundary(filtered_text, allowed_topics)
    
    return {
        "original_input": input_text,
        "filtered_input": filtered_text,
        "injection_detected": injection_detected,
        "injection_result": injection_result,
        "within_boundary": within_boundary,
        "boundary_result": boundary_result,
        "is_valid": not injection_detected and within_boundary
    }
