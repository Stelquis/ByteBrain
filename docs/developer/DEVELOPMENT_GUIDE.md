# 开发指南

---

## 开发环境设置

### 1. 克隆仓库
```bash
git clone https://github.com/your-username/ByteBrain.git
cd ByteBrain
```

### 2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate
```

### 3. 安装开发依赖
```bash
make install-dev
```

这将安装：
- 生产依赖
- 开发工具（pytest、black、flake8、mypy）
- 预提交钩子

---

## 开发工作流

### 1. 创建分支
```bash
git checkout -b feature/your-feature-name
```

### 2. 编写代码
- 遵循项目代码风格
- 添加类型注解
- 编写文档字符串

### 3. 运行代码检查
```bash
make lint
```

### 4. 格式化代码
```bash
make format
```

### 5. 运行测试
```bash
make test
```

### 6. 提交代码
```bash
git add .
git commit -m "feat: 描述你的变更"
git push origin feature/your-feature-name
```

---

## 代码规范

### Python 代码
- 使用 Black 格式化（行宽 100）
- 遵循 Flake8 检查
- 使用类型注解
- Google 风格文档字符串

### 示例
```python
from typing import List, Optional

def binary_search(arr: List[int], target: int) -> int:
    """
    二分查找实现
    
    Args:
        arr: 有序数组
        target: 要查找的目标值
    
    Returns:
        目标值的索引，不存在返回 -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

---

## 目录结构

```
bytebrain/
├── core/               # 核心模块
├── skills/             # Skill 系统
├── guardrails/         # 防护系统
├── prompts/            # Prompt 系统
├── ui/                 # UI 模块
└── utils/              # 工具模块
```

---

## 更多文档

- [架构设计](./ARCHITECTURE.md)
- [API 文档](./API.md)
- [测试指南](./TESTING.md)
- [贡献指南](../../.github/CONTRIBUTING.md)
