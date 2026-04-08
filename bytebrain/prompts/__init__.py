#!/usr/bin/env python3
"""
ByteBrain Prompt 系统

包含系统提示和技能提示。
"""

import os
from typing import Dict, Any


def load_system_prompt(prompt_name: str = "system_prompt") -> str:
    """加载系统提示
    
    Args:
        prompt_name: 提示名称
        
    Returns:
        提示内容
    """
    prompt_path = os.path.join(os.path.dirname(__file__), "system", f"{prompt_name}.md")
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return """## INSTRUCTIONS
你是 ByteBrain，AI 时代的第二大脑。

## INPUTS
用户的问题

## CONSTRAINTS
- 诚实可信
- 知识优先
- 因材施教
- 实践导向
- 简洁优雅

## OUTPUT FORMAT
- 结构清晰
- 逻辑连贯
- 标注来源
"""


def load_skill_prompt(skill_name: str) -> str:
    """加载技能提示
    
    Args:
        skill_name: 技能名称
        
    Returns:
        提示内容
    """
    prompt_path = os.path.join(os.path.dirname(__file__), "skill", f"{skill_name}.md")
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"""## INSTRUCTIONS
你是 {skill_name} 技能的执行者。

## INPUTS
用户的输入

## CONSTRAINTS
- 专业
- 准确
- 友好

## OUTPUT FORMAT
- 清晰
- 详细
- 有用
"""


def render_prompt(prompt_template: str, variables: Dict[str, Any]) -> str:
    """渲染提示模板
    
    Args:
        prompt_template: 提示模板
        variables: 变量字典
        
    Returns:
        渲染后的提示
    """
    rendered = prompt_template
    for key, value in variables.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", str(value))
    return rendered

__all__ = [
    "load_system_prompt",
    "load_skill_prompt",
    "render_prompt"
]
