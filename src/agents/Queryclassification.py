from pydantic import BaseModel, Field
from src.config.State import AgentState
from src.config.environment import Groq_Model 
from typing import List

class Query(BaseModel):
    query: List[str] = Field(description="List of Search queries that is generated from the user query")



def query_node(State : AgentState):
    State["current_step"] = "query_node"

    system_prompt = (
    ''' 
    You are an AI assistant that generates search queries. A user will provide you with a topic, and you will generate a list of 2-3 search queries that are relevant to the topic. You must call the `Query` tool to format your response.
    '''
    )

    messages = [
        {"role": "system" , "content" : system_prompt},
        {"role": "user", "content": State["query"]}
    ]

    response = Groq_Model.with_structured_output(Query).invoke(messages)

    State["search_queries"] = response.query

    return State



    
    