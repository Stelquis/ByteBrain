#!/usr/bin/env python3
"""
ByteBrain 防护系统

包含输入防护、输出防护和行为防护。
"""

from .input_guard import (
    detect_prompt_injection,
    filter_pii,
    check_topic_boundary,
    process_input
)

from .output_guard import (
    detect_hallucination,
    fact_check,
    verify_sources,
    validate_output
)

from .behavior_guard import (
    audit_operation,
    check_permission,
    check_compliance,
    guard_behavior
)

__all__ = [
    # 输入防护
    "detect_prompt_injection",
    "filter_pii",
    "check_topic_boundary",
    "process_input",
    # 输出防护
    "detect_hallucination",
    "fact_check",
    "verify_sources",
    "validate_output",
    # 行为防护
    "audit_operation",
    "check_permission",
    "check_compliance",
    "guard_behavior"
]
