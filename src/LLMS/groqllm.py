# claude version

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage , SystemMessage

#This is the object that actually talks to Groq servers

# Defines a class 
# Purpose: hide Groq + LangChain complexity / encapsulate
# then create a constructor that only run once when obj is created
class GROQLLM:
    
    def __init__(self,api_key=str,model=str):
      self.llm=ChatGroq(groq_api_key=api_key, model=model, temperature=0.7)
      
      
    

