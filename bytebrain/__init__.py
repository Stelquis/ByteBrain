#!/usr/bin/env python3
"""
ByteBrain - AI 时代的第二大脑

一个功能强大的个人知识管理和智能助手系统。
"""

from bytebrain.core import (
    OrchestratorAgent,
    KnowledgeAgent,
    CodeAgent,
    ConceptAgent,
    get_agent_by_name,
    RAGSystem,
    VectorDB,
    create_rag_system,
    create_vector_db,
    ByteBrainState,
    build_bytebrain_graph,
    run_workflow
)

from bytebrain.skills import (
    execute_skill,
    get_skill_info,
    get_available_skills
)

from bytebrain.guardrails import (
    detect_prompt_injection,
    filter_pii,
    check_topic_boundary,
    process_input,
    detect_hallucination,
    fact_check,
    verify_sources,
    validate_output,
    audit_operation,
    check_permission,
    check_compliance,
    guard_behavior
)

from bytebrain.prompts import (
    load_system_prompt,
    load_skill_prompt,
    render_prompt
)

__version__ = "1.0.0"
__author__ = "ByteBrain Team"
__description__ = "AI 时代的第二大脑"

__all__ = [
    # Core
    "OrchestratorAgent",
    "KnowledgeAgent",
    "CodeAgent",
    "ConceptAgent",
    "get_agent_by_name",
    "RAGSystem",
    "VectorDB",
    "create_rag_system",
    "create_vector_db",
    "ByteBrainState",
    "build_bytebrain_graph",
    "run_workflow",
    # Skills
    "execute_skill",
    "get_skill_info",
    "get_available_skills",
    # Guardrails
    "detect_prompt_injection",
    "filter_pii",
    "check_topic_boundary",
    "process_input",
    "detect_hallucination",
    "fact_check",
    "verify_sources",
    "validate_output",
    "audit_operation",
    "check_permission",
    "check_compliance",
    "guard_behavior",
    # Prompts
    "load_system_prompt",
    "load_skill_prompt",
    "render_prompt",
    # Metadata
    "__version__",
    "__author__",
    "__description__"
]
