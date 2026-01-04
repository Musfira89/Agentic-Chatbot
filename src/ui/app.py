
import streamlit as st
from .config import PAGE_TITLE
from .components import render_sidebar , display_result

def main():
    st.set_page_config(page_title=PAGE_TITLE, page_icon="🤖")
    st.title(PAGE_TITLE)
    
    # Render sidebar and get selections
    llm, usecase, model = render_sidebar()
    
    # Main chat interface
    st.header(f"💬 {usecase}")
    
    user_input = st.text_input("Your message:", key="user_input")
    
    if st.button("Send", type="primary"):
        if user_input:
            # TODO: Call your agent here
            response = f"You selected {model} for {usecase}"
            display_result(response)
        else:
            st.warning("Please enter a message first!")

if __name__ == "__main__":
    main()