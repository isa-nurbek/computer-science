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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

1. **Visiting Nodes**: Each node is visited exactly once because once a node is marked as visited (added to the `visited` set),
it won't be processed again.
   - Number of nodes: Let `V` be the number of vertices (nodes). Here, `V = 6` (`A`, `B`, `C`, `D`, `E`, `F`).

2. **Traversing Edges**: For each node, we iterate through all its neighbors (edges). In the worst case, we traverse every
edge in the graph.
   - Number of edges: Let `E` be the number of edges. Here, `E = 5` (`A->B`, `A->C`, `B->D`, `B->E`, `E->F`).

3. **Operations Inside `dfs`**:
   - Checking `if node not in visited`: This is an `O(1)` operation on average for a set.
   - Printing the node: `O(1)`.
   - Adding to the `visited` set: `O(1)` on average.
   - Iterating through neighbors: Proportional to the number of edges.

Thus, the total time complexity is `O(V + E)`. This is because we visit each node once and traverse each edge once.

### Space Complexity:

1. **Visited Set**: The `visited` set stores all nodes, so it takes `O(V)` space.
2. **Recursion Stack**: In the worst case, the recursion stack can grow up to `O(V)` (e.g., if the graph is a straight
line like `A -> B -> C -> D -> E -> F`).
   - In a balanced tree-like structure, the recursion stack would be `O(height of the tree)`.

Thus, the total space complexity is `O(V)` (due to the visited set and recursion stack).

### Summary:
- **Time Complexity**: `O(V + E)`
- **Space Complexity**: `O(V)`

"""
