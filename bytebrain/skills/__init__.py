#!/usr/bin/env python3
"""
ByteBrain 技能系统

包含各种专业技能的实现。
"""

import os
import importlib
from typing import Dict, Any, List


def execute_skill(skill_name: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
    """执行技能
    
    Args:
        skill_name: 技能名称
        input_data: 输入数据
        
    Returns:
        技能执行结果
    """
    # 动态导入技能模块
    try:
        # 将连字符替换为下划线以符合Python包命名规范
        module_name = skill_name.replace('-', '_')
        module = importlib.import_module(f"bytebrain.skills.{module_name}.skill")
        result: Dict[str, Any] = module.execute_skill(input_data)
        return result
    except ImportError:
        return {
            "error": f"技能 {skill_name} 不存在",
            "skill_name": skill_name,
            "input_data": input_data
        }


def get_skill_info(skill_name: str) -> Dict[str, Any]:
    """获取技能信息
    
    Args:
        skill_name: 技能名称
        
    Returns:
        技能信息
    """
    try:
        # 将连字符替换为下划线以符合Python包命名规范
        module_name = skill_name.replace('-', '_')
        module = importlib.import_module(f"bytebrain.skills.{module_name}.skill")
        result: Dict[str, Any] = module.get_skill_info()
        return result
    except ImportError:
        return {
            "error": f"技能 {skill_name} 不存在",
            "skill_name": skill_name
        }


def get_available_skills() -> List[str]:
    """获取可用技能列表
    
    Returns:
        技能名称列表
    """
    skills_dir = os.path.dirname(__file__)
    skills = []
    
    for item in os.listdir(skills_dir):
        item_path = os.path.join(skills_dir, item)
        if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, "skill.py")):
            # 将下划线替换为连字符以保持与用户界面的一致性
            skill_name = item.replace('_', '-')
            skills.append(skill_name)
    
    return skills

__all__ = [
    "execute_skill",
    "get_skill_info",
    "get_available_skills"
]
