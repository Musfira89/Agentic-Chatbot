import streamlit as st
from .config import LLM_OPTIONS, USECASE_OPTIONS, GROQ_MODELS

#This function’s job: draw sidebar UI and return user selections

def render_sidebar():
    with st.sidebar:
        st.header("⚙️ Configuration")

        groq_api_key = st.text_input(
            "Groq API Key", placeholder="Paste your Groq API key here", help="You can get your API key from Groq Console"
        )

        st.markdown("[Get Groq API Key ↗](https://console.groq.com/keys)",unsafe_allow_html=True)
        st.divider()

        usecase = st.selectbox("Use Case", USECASE_OPTIONS,help="Select what the agent should do"
)
        llm = st.selectbox("LLM Provider", LLM_OPTIONS)
        model = st.selectbox("Model", GROQ_MODELS)
      
        st.divider()
        st.caption("Your API key is never stored.")

        return groq_api_key, llm, usecase, model

   
def init_chat_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []


def render_chat_history():
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


def add_message(role: str, content: str):
    st.session_state.messages.append(
        {"role": role, "content": content}
    )
