#!/usr/bin/env python3
"""
ByteBrain 基础使用示例

展示 ByteBrain 的基本使用方法，包括初始化、提问和检索知识。
"""

from bytebrain import ByteBrain

def main():
    """主函数"""
    print("=== ByteBrain 基础使用示例 ===")
    print()
    
    # 初始化 ByteBrain
    print("1. 初始化 ByteBrain...")
    brain = ByteBrain()
    print("✓ ByteBrain 初始化成功")
    print()
    
    # 提问示例
    print("2. 提问示例")
    print("问题: 什么是人工智能？")
    response = brain.ask("什么是人工智能？")
    print("回答:", response)
    print()
    
    # 检索知识示例
    print("3. 检索知识示例")
    print("查询: 机器学习")
    results = brain.retrieve("机器学习", top_k=3)
    for i, result in enumerate(results, 1):
        print(f"{i}. 分数: {result['score']:.2f}")
        print(f"   内容: {result['content'][:100]}...")
        print(f"   来源: {result['source']}")
    print()
    
    # 获取技能列表
    print("4. 获取可用技能")
    skills = brain.get_skills()
    print("可用技能:", skills)
    print()
    
    # 获取系统状态
    print("5. 获取系统状态")
    stats = brain.get_stats()
    print(f"版本: {stats['version']}")
    print(f"知识库大小: {stats['knowledge_base_size']} 文档")
    print(f"向量数据库: {stats['vector_db_status']}")
    print(f"系统状态: {stats['status']}")
    print()
    
    print("=== 示例完成 ===")

if __name__ == "__main__":
    main()