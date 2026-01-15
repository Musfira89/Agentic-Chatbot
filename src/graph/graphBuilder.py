from ..state.state import State
from langgraph.graph import StateGraph


class graphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graphBuilder=StateGraph(State)