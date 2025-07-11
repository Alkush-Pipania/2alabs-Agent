from typing import Optional, TypedDict
from enum import Enum
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

class VibeType(Enum):
    EXCITED = "excited_node"
    WORK = "work_node"
    CASUAL = "casual_node"
    ACADEMIC = "academic_node"
    CREATIVE = "creative_node"

class QueryType(Enum):
    WEB_SEARCH = "web_search"
    KNOWLEDGE_BASE = "knowledge_base"
    COMPLEX_REASONING = "complex_reasoning"
    MULTI_STEP_TASK = "multi_step_task"

@dataclass
class SearchResult:
    content: str
    source: str
    confidence: float
    metadata: Dict[str, Any]

  

# LangGraph State Schema (TypedDict approach)
class AgentState(TypedDict):
    query: str
    vibe: 'VibeType'
    conversation_history: List[Dict]
    current_step: str
    intermediate_results: Dict[str, Any]
    final_response: Optional[str]
    markdown_response: Optional[str]
    error_state: Optional[str]
    search_queries: Optional[List[str]]
    web_results: Optional[List['SearchResult']]
    vector_results: Optional[List['SearchResult']]
    reasoning_results: Optional[Dict[str, Any]]
    synthesized_response: Optional[str]
    memory_results: Optional[Dict[str, Any]]
