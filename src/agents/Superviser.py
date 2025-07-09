from pydantic import BaseModel , Field
from typing import Literal
from src.config.State import AgentState
from langgraph.types import Command 
from langchain_core.messages import HumanMessage
from src.config.environment import Gemini_Model

class Supervisor(BaseModel):
  next: Literal["technical" , "creative" , "analytical" , "work" , "Excited"] = Field(
    description="Determines which specialist to activate next in the workflow sequence."
    "'technical' for technical task . when it require to do with mathematical calculation , coding , for asking that require to be done by a technical specialist"
    "creative for creative task . when it require to do with creative thinking , design , art , for asking that require to be done by a creative specialist"
    "analytical for analytical task . when it require to do with data analysis , statistics , for asking that require to be done by an analytical specialist"
    "work for work task . when it require to do with work task , for asking that require to be done by a work specialist" \
    "Excited for excited task . when the user query includes ideas , suggestions or brainstorming or something that require so much information over the web ."
  )
  reason : str = Field(
    description="A brief explanation of why this specialist was chosen based on the user's query."
  )

def supervisor_node(State: AgentState) -> Command[Literal["technical","creative",
"analytical", "work" , "Excited"]]:
  
  system_prompt = (
    '''
   You are a supervisor agent responsible for routing a user's request to the correct specialist in a    workflow. Analyze the user's query and determine which of the following specialists should be activated  next based on their described capabilities.
   
   - technical: Choose this for technical tasks. This includes requests involving mathematical calculations, coding problems, or anything that requires a technical specialist.
   
   - creative: Choose this for creative tasks. This is for requests that involve creative thinking, design, art, or content generation by a creative specialist.
   
   - analytical: Choose this for analytical tasks. This applies to requests needing data analysis, statistics,or logical reasoning by an analytical specialist.
   
   - work: Choose this for work-related tasks. This is for general professional or work-specific requests.
   
   - Excited: Choose this when the user's query includes brainstorming, sharing ideas, making suggestions, or asks for a broad range of information that requires searching the web extensively.
   
   Based on the user's query, which specialist should handle the task? Respond with only the single, most  appropriate option.
  ''')
  messages =  [
    {"role":"system" , "content" : system_prompt},
  ] + State["messages"]
  
  response = Gemini_Model.with_structured_output(Supervisor).invoke(messages=messages)

  goto = response.next
  reason = response.reason

  print(f"--- Workflow Transition : Supervisor -> {goto} ---")

  return Command(
    update={
      "messages": [
        HumanMessage(content=reason , name="Supervisor")
      ]
    },
    goto=goto
  )