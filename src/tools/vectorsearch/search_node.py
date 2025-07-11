from src.config.State import AgentState, SearchResult
from src.config.environment import Tavily_tool
import json



def search_node(state: AgentState):
    queries = state.get("search_queries", [])
    
    if not queries:
        return {"web_results": []}
    
    all_results = []
    
    # Process each query individually
    for query in queries:
        try:
            # Invoke Tavily with a single query string
            result = Tavily_tool.invoke({"query": query})
            
            # Parse the JSON result
            if isinstance(result, str):
                result_data = json.loads(result)
            else:
                result_data = result
            
            # Convert to SearchResult objects
            for item in result_data.get("results", []):
                search_result = SearchResult(
                    content=item.get("content", ""),
                    source=item.get("url", ""),
                    confidence=1.0,  # Tavily doesn't provide confidence scores
                    metadata={
                        "title": item.get("title", ""),
                        "query": query,
                        "raw_score": item.get("score", 0)
                    }
                )
                all_results.append(search_result)
                
        except Exception as e:
            print(f"Error searching for query '{query}': {e}")
            continue
    
    return {"web_results": all_results}
