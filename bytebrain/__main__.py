"""
ByteBrain 入口模块
"""

import sys
from .utils.logger import setup_logger

logger = setup_logger(__name__)

def main():
    """主函数"""
    logger.info("Starting ByteBrain...")
    try:
        from .ui.streamlit_app import main as ui_main
        ui_main()
    except KeyboardInterrupt:
        logger.info("ByteBrain stopped by user")
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
