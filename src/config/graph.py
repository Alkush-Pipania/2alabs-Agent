from langgraph.graph import END, START, StateGraph
from src.agents.Markdown import markdown_node
from src.config.State import AgentState
from src.agents.vibeAgents_fixed import * 

graph = StateGraph(AgentState)

# Add all nodes
graph.add_node("vibe_node", vibe_node)
graph.add_node("excited_node", excited_node)
graph.add_node("work_node", work_node)
graph.add_node("casual_node", casual_node)
graph.add_node("academic_node", academic_node)
graph.add_node("creative_node", creative_node)
graph.add_node("markdown_node",markdown_node)

# Add edges
graph.add_edge(START, "vibe_node")

# Add conditional edges from vibe_node to specific vibe nodes
graph.add_conditional_edges(
    "vibe_node",
    route_by_vibe,  
    {
        "excited_node": "excited_node",
        "work_node": "work_node", 
        "casual_node": "casual_node",
        "academic_node": "academic_node",
        "creative_node": "creative_node"
    }
)

# Add edges from each vibe node to END
graph.add_edge("excited_node", "markdown_node")
graph.add_edge("work_node", "markdown_node")
graph.add_edge("casual_node", "markdown_node")
graph.add_edge("academic_node", "markdown_node")
graph.add_edge("creative_node", "markdown_node")
graph.add_edge("markdown_node", END)



# # Compile the graph
app = graph.compile()

# # Save the graph visualization to a file
# try:
#     graph_image = app.get_graph(xray=True).draw_mermaid_png()
#     with open('graph_visualization.png', 'wb') as f:
#         f.write(graph_image)
#     print("Graph visualization saved to 'graph_visualization.png'")
# except Exception as e:
#     print(f"Error saving graph visualization: {e}")
    
# # Print the graph structure
# print("\nGraph structure:")
# print(app.get_graph().draw_ascii()) 













# result = app.invoke({
#     "vibe": VibeType.EXCITED,
#     "query": [{"role": "user", "content": "Tell me about artificial intelligence!"}],
# })


# print(result)