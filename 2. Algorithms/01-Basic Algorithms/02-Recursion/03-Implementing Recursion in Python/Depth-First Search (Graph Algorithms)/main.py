# Implementation in Python:


# Depth-First Search (DFS) algorithm implementation
def dfs(graph, node, visited):
    """
    Perform Depth-First Search starting from the given node.

    Args:
        graph: The graph represented as a dictionary (adjacency list)
        node: The current node being visited
        visited: A set of already visited nodes (to avoid revisiting)
    """
    # Check if current node hasn't been visited yet
    if node not in visited:
        # Process the current node (here we just print it)
        print(node, end=" ")

        # Mark the current node as visited by adding it to the set
        visited.add(node)

        # Recursively visit all adjacent nodes (neighbors)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# Define the graph as an adjacency list
# Each key is a node, and its value is a list of connected nodes (neighbors)
graph = {
    "A": ["B", "C"],  # Node A is connected to B and C
    "B": ["D", "E"],  # Node B is connected to D and E
    "C": ["F"],  # Node C is connected to F
    "D": [],  # Node D has no connections
    "E": ["F"],  # Node E is connected to F
    "F": [],  # Node F has no connections
}

# Create a set to keep track of visited nodes
visited = set()

# Test Case:
dfs(graph, "A", visited)  # Output: A B D E F C
