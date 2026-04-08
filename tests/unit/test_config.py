#!/usr/bin/env python3
"""
测试配置模块
"""

import pytest
from bytebrain.utils.config import Config


def test_config_creation():
    """测试配置创建"""
    config = Config()
    assert config.model_name == "IEITYuan/Yuan2-2B-July-hf"
    assert config.max_seq_length == 2048
    assert config.top_k == 3


def test_config_post_init():
    """测试配置后初始化"""
    config = Config()
    assert config.model_path is not None
    assert config.embed_model_path is not None


def test_config_with_custom_values():
    """测试自定义配置值"""
    config = Config(
        model_name="test-model",
        max_seq_length=1024,
        top_k=5
    )
    assert config.model_name == "test-model"
    assert config.max_seq_length == 1024
    assert config.top_k == 5
