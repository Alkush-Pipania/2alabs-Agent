from src.config.graph import app
from src.config.State import VibeType

def test_graph():
    # Test with different vibe types
    test_cases = [
        {
            "query": "different between development and dsa . gave me difference table",
            "vibe": VibeType.EXCITED,
            "conversation_history": [],
            "current_step": "start",
            "intermediate_results": {},
            "final_response": None,
            "markdown_response": None,
            "error_state": None,
            "search_queries": None,
            "web_results": None,
            "vector_results": None,
            "reasoning_results": None,
            "synthesized_response": None,
            "memory_results": None
        },
    ]
    
    for i, test_case in enumerate(test_cases):
        print(f"\n--- Test Case {i+1}: {test_case['vibe'].value.upper()} ---")
        print(f"Query: {test_case['query']}")
        
        try:
            # Run the graph
            result = app.invoke(test_case)
            print(f"Markdown Response: {result.get('markdown_response', 'No response')}")
            print(f"Current Step: {result.get('current_step', 'Unknown')}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_graph()
