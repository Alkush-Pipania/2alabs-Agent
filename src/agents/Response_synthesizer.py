from src.config.State import AgentState, SearchResult
from src.config.environment import Groq_Model
from typing import List, Dict, Any

def synthesizer_node(state: AgentState) -> AgentState:
    """
    Synthesizes information from web search, vector search, and conversation memory
    to create a comprehensive response for the user query.
    """
    state["current_step"] = "synthesizer_node"
    
    # Gather all available information
    query = state.get("query", "")
    web_results = state.get("web_results", [])
    vector_results = state.get("vector_results", [])
    memory_results = state.get("memory_results", {})
    conversation_history = state.get("conversation_history", [])
    
    # Prepare context for synthesis
    web_context = ""
    if web_results:
        web_context = "\n".join([
            f"**Source: {result.source}**\n{result.content}\n"
            for result in web_results[:3]  # Limit to top 3 results
        ])
    
    vector_context = ""
    if vector_results:
        vector_context = "\n".join([
            f"**Knowledge Base: {result.source}**\n{result.content}\n"
            for result in vector_results[:3]  # Limit to top 3 results
        ])
    
    memory_context = ""
    if memory_results:
        memory_context = f"**Conversation Context:**\n{memory_results.get('summary', 'No previous context')}\n"
    
    # Create synthesis prompt
    system_prompt = """
    You are an expert information synthesizer. Your task is to create a comprehensive, accurate, and well-structured response by combining information from multiple sources.
    
    Guidelines:
    1. Integrate information from web search, knowledge base, and conversation memory
    2. Prioritize accuracy and relevance to the user's query
    3. Provide a coherent, well-organized response
    4. Include relevant details and examples when available
    5. Maintain objectivity and cite sources when appropriate
    6. If information is conflicting, acknowledge the differences
    7. If information is insufficient, clearly state what's missing
    
    Your response should be informative, comprehensive, and directly address the user's query.
    """
    
    user_prompt = f"""
    User Query: {query}
    
    Web Search Results:
    {web_context or "No web search results available"}
    
    Knowledge Base Results:
    {vector_context or "No knowledge base results available"}
    
    Conversation Memory:
    {memory_context or "No conversation context available"}
    
    Please synthesize this information into a comprehensive response that directly addresses the user's query.
    """
    
    try:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        response = Groq_Model.invoke(messages)
        state["synthesized_response"] = response.content
        
    except Exception as e:
        print(f"Error in synthesizer_node: {e}")
        state["synthesized_response"] = f"I apologize, but I encountered an error while processing your query: {query}. Please try again."
        state["error_state"] = str(e)
    
    return state
