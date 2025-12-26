from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, SystemMessage
from logs.logger import logger

from toolkit.tools import *
from utils.model_loader import ModelLoader

class StateGraph(TypedDict):
    messages=Annotated[list, add_messages]

class graph_builder:
    def __init__(self):
        pass

    def _chatbot_node(self, state: StateGraph):
        pass
    
    def build(self):
        pass

    def get_graph(Self):
        pass
    
    

