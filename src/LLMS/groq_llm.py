# This file’s job is only one thing:
# Create and return a Groq LLM object

import os
import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model
    
    def get_llm_model(self):
        """Returns initialized ChatGroq LLM"""
        try:
            # Check if API key exists
            if not self.api_key and not os.environ.get("GROQ_API_KEY"):
                st.error("Please Enter the Groq API KEY")
                return None
            
            # Use provided key or fall back to environment variable
            final_api_key = self.api_key or os.environ.get("GROQ_API_KEY")
            
            llm = ChatGroq(api_key=final_api_key, model=self.model)
            
            return llm
        
        except Exception as e:
            raise ValueError(f"Error Occurred With Exception: {e}")