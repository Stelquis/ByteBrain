#!/usr/bin/env python3
"""
ByteBrain Web UI

使用 Streamlit 构建的 ByteBrain Web 界面。
"""

import streamlit as st
from bytebrain.core import run_workflow
from bytebrain.skills import execute_skill, get_available_skills
from bytebrain.guardrails import process_input, validate_output

# 设置页面配置
st.set_page_config(
    page_title="ByteBrain - AI 时代的第二大脑",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 页面标题
st.title("🧠 ByteBrain")
st.subheader("AI 时代的第二大脑")

# 侧边栏
with st.sidebar:
    st.header("功能菜单")
    selected_tab = st.radio(
        "选择功能",
        ["对话", "技能", "知识库", "设置"]
    )
    
    st.divider()
    st.header("关于")
    st.markdown("ByteBrain 是 AI 时代的第二大脑，帮助你管理和检索个人知识，成为你的数字分身。")

# 对话功能
if selected_tab == "对话":
    st.header("💬 智能对话")
    
    # 对话历史
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # 显示对话历史
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # 用户输入
    if prompt := st.chat_input("请输入你的问题..."):
        # 添加用户消息
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # 处理输入
        input_result = process_input(prompt)
        
        if input_result["is_valid"]:
            # 运行工作流
            with st.spinner("思考中..."):
                result = run_workflow(prompt)
            
            # 验证输出
            output_result = validate_output(
                result["response"],
                result["sources"]
            )
            
            # 添加助手消息
            st.session_state.messages.append({"role": "assistant", "content": output_result["output_text"]})
            with st.chat_message("assistant"):
                st.markdown(output_result["output_text"])
                if result.get("sources"):
                    st.caption(f"来源: {', '.join(result['sources'])}")
                st.caption(f"置信度: {output_result['overall_confidence']:.2f}")
        else:
            # 输入验证失败
            error_message = "输入验证失败: "
            if input_result["injection_detected"]:
                error_message += input_result["injection_result"]
            else:
                error_message += input_result["boundary_result"]
            
            st.session_state.messages.append({"role": "assistant", "content": error_message})
            with st.chat_message("assistant"):
                st.error(error_message)

# 技能功能
elif selected_tab == "技能":
    st.header("⚡ 技能中心")
    
    # 获取可用技能
    skills = get_available_skills()
    
    # 技能选择
    selected_skill = st.selectbox("选择技能", skills)
    
    # 技能参数输入
    if selected_skill == "knowledge-retrieval":
        query = st.text_input("查询内容")
        top_k = st.slider("返回结果数量", 1, 10, 5)
        
        if st.button("执行技能"):
            with st.spinner("执行中..."):
                result = execute_skill(selected_skill, {
                    "query": query,
                    "top_k": top_k
                })
            
            st.success("执行完成!")
            st.markdown("### 结果")
            st.markdown(result["answer"])
            if result.get("sources"):
                st.caption(f"来源: {', '.join(result['sources'])}")
            st.caption(f"置信度: {result['confidence']:.2f}")
    
    elif selected_skill == "code-coaching":
        code = st.text_area("代码", height=200)
        question = st.text_input("问题")
        
        if st.button("执行技能"):
            with st.spinner("执行中..."):
                result = execute_skill(selected_skill, {
                    "code": code,
                    "question": question
                })
            
            st.success("执行完成!")
            st.markdown("### 反馈")
            st.markdown(result["feedback"])
            st.markdown("### 建议")
            st.code(result["suggestion"])
            st.markdown("### 解释")
            st.markdown(result["explanation"])
    
    elif selected_skill == "concept-explanation":
        concept = st.text_input("概念")
        level = st.selectbox("理解水平", ["beginner", "intermediate", "advanced"])
        
        if st.button("执行技能"):
            with st.spinner("执行中..."):
                result = execute_skill(selected_skill, {
                    "concept": concept,
                    "level": level
                })
            
            st.success("执行完成!")
            st.markdown("### 解释")
            st.markdown(result["explanation"])
            st.markdown("### 类比")
            for analogy in result["analogies"]:
                st.markdown(f"- {analogy}")
            st.markdown("### 例子")
            for example in result["examples"]:
                st.markdown(f"- {example}")
    
    elif selected_skill == "exercise-generation":
        topic = st.text_input("主题")
        level = st.selectbox("难度级别", ["beginner", "intermediate", "advanced"])
        count = st.slider("题目数量", 1, 10, 5)
        
        if st.button("执行技能"):
            with st.spinner("执行中..."):
                result = execute_skill(selected_skill, {
                    "topic": topic,
                    "level": level,
                    "count": count
                })
            
            st.success("执行完成!")
            st.markdown("### 练习题")
            for exercise in result["exercises"]:
                st.markdown(f"**{exercise['id']}. {exercise['question']}")
            st.markdown("### 学习材料")
            for material in result["materials"]:
                st.markdown(f"- {material}")
            st.markdown("### 答案")
            for answer in result["answers"]:
                st.markdown(f"**{answer['id']}. 答案:** {answer['answer']}")
                st.markdown(f"**解释:** {answer['explanation']}")

# 知识库功能
elif selected_tab == "知识库":
    st.header("📚 知识库管理")
    
    st.markdown("### 知识库状态")
    st.info("知识库功能开发中...")
    
    # 上传文件
    st.markdown("### 上传文件")
    uploaded_files = st.file_uploader(
        "选择文件",
        accept_multiple_files=True,
        type=["pdf", "txt", "md", "docx"]
    )
    
    if uploaded_files:
        st.success(f"已选择 {len(uploaded_files)} 个文件")
        for file in uploaded_files:
            st.write(f"- {file.name} ({file.size} bytes)")
        
        if st.button("添加到知识库"):
            st.success("文件已添加到知识库!")

# 设置功能
elif selected_tab == "设置":
    st.header("⚙️ 设置")
    
    st.markdown("### 系统设置")
    
    # 模型设置
    st.subheader("模型设置")
    model = st.selectbox("选择模型", ["gpt-4o", "gpt-3.5-turbo", "claude-3-opus"])
    temperature = st.slider("温度", 0.0, 1.0, 0.7)
    
    # RAG 设置
    st.subheader("RAG 设置")
    chunk_size = st.slider("Chunk 大小", 500, 2000, 1000)
    top_k = st.slider("Top K", 1, 20, 5)
    
    # 防护设置
    st.subheader("防护设置")
    enable_input_guard = st.checkbox("启用输入防护", value=True)
    enable_output_guard = st.checkbox("启用输出防护", value=True)
    enable_behavior_guard = st.checkbox("启用行为防护", value=True)
    
    if st.button("保存设置"):
        st.success("设置已保存!")

# 页脚
st.divider()
st.caption("ByteBrain - AI 时代的第二大脑 | © 2026")
