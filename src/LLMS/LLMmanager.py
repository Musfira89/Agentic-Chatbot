
import streamlit as st
from .groqllm import GroqLLM


def initialize_llm(api_key: str, model: str):
    """
    Initialize LLM only if needed.
    Returns: GroqLLM instance or None if failed
    """
    try:
        # Check if we need to reinitialize
        current_model = st.session_state.get("current_model")
        
        if "llm" not in st.session_state or current_model != model:
            llm = GroqLLM(api_key=api_key, model=model)
            
            st.session_state["llm"] = llm
            st.session_state["current_model"] = model
            
            return llm
        
        # Return existing LLM
        return st.session_state["llm"]
    
    except Exception as e:
        st.error(f" Failed to initialize LLM: {str(e)}")
        return None

