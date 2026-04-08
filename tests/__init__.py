"""
ByteBrain Tests Configuration
"""

import pytest
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

@pytest.fixture
def sample_config():
    """示例配置 fixture"""
    from bytebrain.utils import Config
    return Config()
