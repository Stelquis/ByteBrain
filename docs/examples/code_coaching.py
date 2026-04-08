#!/usr/bin/env python3
"""
ByteBrain 代码教练示例

展示如何使用代码教练技能优化代码。
"""

from bytebrain import ByteBrain

def main():
    """主函数"""
    print("=== ByteBrain 代码教练示例 ===")
    print()
    
    # 初始化 ByteBrain
    print("1. 初始化 ByteBrain...")
    brain = ByteBrain()
    print("✓ ByteBrain 初始化成功")
    print()
    
    # 代码优化示例
    print("2. 代码优化示例")
    print("原代码:")
    code = """
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
"""
    print(code)
    
    print("\n执行代码教练技能...")
    result = brain.execute_skill("code-coaching", {
        "code": code,
        "question": "如何优化这段斐波那契数列代码？"
    })
    
    print("\n反馈:")
    print(result['feedback'])
    print("\n优化建议:")
    print(result['suggestion'])
    print("\n解释:")
    print(result['explanation'])
    print()
    
    # 代码解释示例
    print("3. 代码解释示例")
    print("代码:")
    code2 = """
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def hello():
    print("Hello, world!")
"""
    print(code2)
    
    print("\n执行代码教练技能...")
    result2 = brain.execute_skill("code-coaching", {
        "code": code2,
        "question": "请解释这段代码的工作原理"
    })
    
    print("\n解释:")
    print(result2['explanation'])
    print("\n关键点:")
    for point in result2.get('key_points', []):
        print(f"- {point}")
    print()
    
    print("=== 示例完成 ===")

if __name__ == "__main__":
    main()