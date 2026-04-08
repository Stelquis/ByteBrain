#!/usr/bin/env python3
"""
ByteBrain 概念解释示例

展示如何使用概念解释技能解释复杂概念。
"""

from bytebrain import ByteBrain

def main():
    """主函数"""
    print("=== ByteBrain 概念解释示例 ===")
    print()
    
    # 初始化 ByteBrain
    print("1. 初始化 ByteBrain...")
    brain = ByteBrain()
    print("✓ ByteBrain 初始化成功")
    print()
    
    # 解释深度学习概念
    print("2. 解释深度学习概念")
    print("概念: 深度学习")
    print("难度级别: beginner")
    
    print("\n执行概念解释技能...")
    result = brain.execute_skill("concept-explanation", {
        "concept": "深度学习",
        "level": "beginner"
    })
    
    print("\n解释:")
    print(result['explanation'])
    print("\n类比:")
    for analogy in result.get('analogies', []):
        print(f"- {analogy}")
    print("\n例子:")
    for example in result.get('examples', []):
        print(f"- {example}")
    print()
    
    # 解释LangGraph概念
    print("3. 解释 LangGraph 概念")
    print("概念: LangGraph")
    print("难度级别: intermediate")
    
    print("\n执行概念解释技能...")
    result2 = brain.execute_skill("concept-explanation", {
        "concept": "LangGraph",
        "level": "intermediate"
    })
    
    print("\n解释:")
    print(result2['explanation'])
    print("\n类比:")
    for analogy in result2.get('analogies', []):
        print(f"- {analogy}")
    print("\n例子:")
    for example in result2.get('examples', []):
        print(f"- {example}")
    print()
    
    # 解释RAG概念
    print("4. 解释 RAG 概念")
    print("概念: RAG (Retrieval-Augmented Generation)")
    print("难度级别: advanced")
    
    print("\n执行概念解释技能...")
    result3 = brain.execute_skill("concept-explanation", {
        "concept": "RAG (Retrieval-Augmented Generation)",
        "level": "advanced"
    })
    
    print("\n解释:")
    print(result3['explanation'])
    print("\n类比:")
    for analogy in result3.get('analogies', []):
        print(f"- {analogy}")
    print("\n例子:")
    for example in result3.get('examples', []):
        print(f"- {example}")
    print()
    
    print("=== 示例完成 ===")

if __name__ == "__main__":
    main()