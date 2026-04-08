#!/usr/bin/env python3
"""
ByteBrain 命令行入口

提供命令行工具和主入口点。
"""

import argparse
import sys
from bytebrain import (
    run_workflow,
    execute_skill,
    get_available_skills,
    process_input,
    validate_output
)


def main() -> None:
    """主函数"""
    parser = argparse.ArgumentParser(description="ByteBrain - AI 时代的第二大脑")
    
    # 子命令
    subparsers = parser.add_subparsers(dest="command", help="可用命令")
    
    # ask 命令
    ask_parser = subparsers.add_parser("ask", help="向 ByteBrain 提问")
    ask_parser.add_argument("query", help="问题")
    
    # skill 命令
    skill_parser = subparsers.add_parser("skill", help="执行技能")
    skill_parser.add_argument("skill_name", help="技能名称")
    skill_parser.add_argument("--input", help="输入数据 (JSON 格式)")
    
    # skills 命令
    subparsers.add_parser("skills", help="列出可用技能")
    
    # stats 命令
    subparsers.add_parser("stats", help="查看系统状态")
    
    # version 命令
    subparsers.add_parser("version", help="查看版本")
    
    args = parser.parse_args()
    
    if args.command == "ask":
        # 处理输入
        input_result = process_input(args.query)
        
        if input_result["is_valid"]:
            # 运行工作流
            result = run_workflow(args.query)
            
            # 验证输出
            output_result = validate_output(
                result["response"],
                result["sources"]
            )
            
            print("=== ByteBrain 回答 ===")
            print(output_result["output_text"])
            if result.get("sources"):
                print(f"\n来源: {', '.join(result['sources'])}")
            print(f"置信度: {output_result['overall_confidence']:.2f}")
        else:
            print("输入验证失败:")
            if input_result["injection_detected"]:
                print(input_result["injection_result"])
            else:
                print(input_result["boundary_result"])
    
    elif args.command == "skill":
        # 执行技能
        import json
        input_data = {}
        if args.input:
            try:
                input_data = json.loads(args.input)
            except json.JSONDecodeError:
                print("输入数据格式错误，请使用 JSON 格式")
                sys.exit(1)
        
        result = execute_skill(args.skill_name, input_data)
        
        print(f"=== {args.skill_name} 技能执行结果 ===")
        if "error" in result:
            print(f"错误: {result['error']}")
        else:
            # 根据技能类型输出不同格式
            if args.skill_name == "knowledge-retrieval":
                print(result.get("answer", ""))
                if result.get("sources"):
                    print(f"\n来源: {', '.join(result['sources'])}")
                print(f"置信度: {result.get('confidence', 0):.2f}")
            elif args.skill_name == "code-coaching":
                print("反馈:")
                print(result.get("feedback", ""))
                print("\n建议:")
                print(result.get("suggestion", ""))
                print("\n解释:")
                print(result.get("explanation", ""))
            elif args.skill_name == "concept-explanation":
                print("解释:")
                print(result.get("explanation", ""))
                print("\n类比:")
                for analogy in result.get("analogies", []):
                    print(f"- {analogy}")
                print("\n例子:")
                for example in result.get("examples", []):
                    print(f"- {example}")
            elif args.skill_name == "exercise-generation":
                print("练习题:")
                for exercise in result.get("exercises", []):
                    print(f"{exercise['id']}. {exercise['question']}")
                print("\n学习材料:")
                for material in result.get("materials", []):
                    print(f"- {material}")
            else:
                print(result)
    
    elif args.command == "skills":
        # 列出可用技能
        skills = get_available_skills()
        print("=== 可用技能 ===")
        for skill in skills:
            print(f"- {skill}")
    
    elif args.command == "stats":
        # 查看系统状态
        print("=== 系统状态 ===")
        print("版本: 1.0.0")
        print("状态: 运行中")
        print("可用技能: " + str(len(get_available_skills())))
        print("知识库: 就绪")
    
    elif args.command == "version":
        # 查看版本
        from bytebrain import __version__
        print(f"ByteBrain 版本: {__version__}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
