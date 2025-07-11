from src.config.State import AgentState


def conversation_node(state : AgentState):
    """this get data from conversation memory and create a good data for vibe agent to work on"""
    # Extract relevant conversation context
    conversation_history = state.get("conversation_history", [])
    
    # Create memory results with context summary
    memory_results = {
        "summary": "No previous conversation context available",
        "relevant_topics": [],
        "user_preferences": {}
    }
    
    if conversation_history:
        # Extract key information from conversation history
        recent_messages = conversation_history[-5:]  # Last 5 messages
        topics = []
        
        for msg in recent_messages:
            if isinstance(msg, dict) and "content" in msg:
                topics.append(msg["content"][:100])  # First 100 chars
        
        memory_results["summary"] = f"Recent conversation topics: {'; '.join(topics)}"
        memory_results["relevant_topics"] = topics
    
    return {"memory_results": memory_results}