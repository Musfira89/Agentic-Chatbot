# claude version

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage , SystemMessage

#This is the object that actually talks to Groq servers
# Defines a class 
# Purpose: hide Groq + LangChain complexity / encapsulate
# then create a constructor that only run once when obj is created
class GroqLLM:
    
    def __init__(self,api_key=str,model=str):
      self.llm=ChatGroq(groq_api_key=api_key, model=model, temperature=0.7)
      
    def chat(self, user_message:str, system_prompt:str = None):
        """Send messages and get response"""
        messages=[]
        
        #Check if system prompt exists
        if system_prompt:
            messages.append(SystemMessage(content=system_prompt))
            messages.append(HumanMessage(content=user_message))
            
            response=self.llm.invoke(messages)
            return response.content
        
    def chat_stream(self, user_message:str , system_prompt: str =None):
        """Stream response word by word"""
        messages=[]
        messages.append(SystemMessage(content=system_prompt))
        messages.append(HumanMessage(content=user_message))
        
        for chunk in self.llm.stream(messages):    
            
            # Sometimes chunks are empty .This avoids printing blanks
            # yield sends data gradually. Perfect for live typing effect in UI
            if chunk.content:
                yield chunk.content
            
    

