import streamlit as st
from .config import PAGE_TITLE, SYSTEM_PROMPTS
from .components import (
    render_sidebar,
    init_chat_state,
    render_chat_history,
    add_message,
)

from .LLMS.LLMmanager import initialize_llm


def main():
    st.set_page_config(
        page_title=PAGE_TITLE,
        layout="wide"
    )

    st.title(PAGE_TITLE)

    # Sidebar output
    groq_api_key, llm, usecase, model = render_sidebar()

    #  Stop app if API key missing
    if not groq_api_key:
        st.info("Please paste your Groq API key in the sidebar to continue.")
        st.stop()

    # Save key in session memory
    st.session_state["GROQ_API_KEY"] = groq_api_key

    # Initialize LLM
    llm = initialize_llm(
        api_key=groq_api_key,
        model=model
    )

    system_prompt = SYSTEM_PROMPTS.get(
        usecase, SYSTEM_PROMPTS["Basic Chatbot"])


# Chat setup
init_chat_state()
render_chat_history()

user_input = st.chat_input("Type your message...")


if user_input:
      add_message("user", user_input)
      

      with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = llm.chat(
                    user_message=user_input,
                    system_prompt=system_prompt
                )
                st.markdown(response)

      add_message("assistant", response)


if __name__ == "__main__":
    main()
