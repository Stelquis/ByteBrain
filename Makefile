# ByteBrain Makefile
# 常用任务自动化

.PHONY: help install install-dev clean test lint format docs run

# 默认显示帮助
help:
	@echo "ByteBrain 开发工具"
	@echo ""
	@echo "可用命令："
	@echo "  make install      - 安装生产依赖"
	@echo "  make install-dev  - 安装开发依赖"
	@echo "  make clean        - 清理临时文件"
	@echo "  make test         - 运行测试"
	@echo "  make lint         - 运行代码检查"
	@echo "  make format       - 格式化代码"
	@echo "  make docs         - 构建文档"
	@echo "  make run          - 启动应用"

# 安装依赖
install:
	pip install -e .

install-dev:
	pip install -e ".[dev,full]"
	pre-commit install

# 清理
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name ".DS_Store" -delete
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

# 测试
test:
	pytest

test-cov:
	pytest --cov=bytebrain --cov-report=html

# 代码质量
lint:
	black --check .
	flake8 .
	mypy bytebrain

format:
	black .

# 文档
docs:
	cd docs && make html

# 运行
run:
	streamlit run bytebrain/ui/streamlit_app.py
