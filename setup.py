#!/usr/bin/env python
"""
ByteBrain 安装配置
"""
from setuptools import setup, find_packages

setup(
    name="bytebrain",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "bytebrain=bytebrain.__main__:main",
        ],
    },
)
