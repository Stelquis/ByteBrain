"""
ByteBrain UI Application
"""

import streamlit as st

def main():
    """Streamlit 应用主函数"""
    st.set_page_config(
        page_title="ByteBrain - AI 时代你的第二大脑",
        page_icon="🧠",
        layout="wide"
    )
    
    st.title("🧠 ByteBrain")
    st.subheader("AI 时代你的第二大脑")
    
    st.markdown("""
    欢迎使用 ByteBrain！
    
    - 📚 管理你的个人知识
    - 🤖 智能问答与解释
    - 🔗 连接你的数字世界
    
    更多信息请查看 [文档](../docs/README.md)
    """)
    
    with st.sidebar:
        st.header("设置")
        st.slider("温度", 0.0, 1.0, 0.7)

if __name__ == "__main__":
    main()
