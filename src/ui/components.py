import streamlit as st
from .config import LLM_OPTIONS, USECASE_OPTIONS, GROQ_MODELS

def render_sidebar():
    """Render the configuration sidebar"""
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        usecase = st.selectbox("Select Use Case", USECASE_OPTIONS)
        llm = st.selectbox("Select LLM Provider", LLM_OPTIONS)
        model = st.selectbox("Select Model", GROQ_MODELS)
        
        return llm, usecase, model

def display_result(response: str):
    """Display the agent's response"""
    st.markdown("### 🤖 Response")
    st.write(response)