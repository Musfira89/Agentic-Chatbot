from typing_extensions import TypedDict,list
from langgraph.graph.message import add_message
from typing import Annotated


class State(TypedDict):
    messages: Annotated[list,add_message]