# Code Explanation: Depth-First Search (Graph Algorithms) Implementing in Python

## **Climbing Stairs function**

```python
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
```

### **Explanation of the Depth-First Search (DFS) Code**

The given Python code implements **Depth-First Search (DFS)** using recursion to traverse a directed graph represented as an **adjacency list**.

---

### **1. Understanding the Graph Representation**

The `graph` is a dictionary where:

- Keys represent nodes (vertices).
- Values are lists of neighboring nodes (edges).

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
```

#### **Graph Visualization**

```
     A
    / \
   B   C
  / \   \
 D   E   F
      \
       F
```

- 'A' connects to ['B', 'C']
- 'B' connects to ['D', 'E']
- 'C' connects to ['F']
- 'D' has no connections (empty list)
- 'E' connects to ['F']
- 'F' has no connections

---

### **2. Depth-First Search (DFS) Function**

#### **Function Definition**

```python
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
```

- `graph`: The adjacency list representation of the graph.
- `node`: The current node being visited.
- `visited`: A **set** to track visited nodes and avoid cycles.

---

### **3. Execution Flow**

#### **Step 1: Initialize and Call DFS**

```python
visited = set()
dfs(graph, 'A', visited)
```

- A **set** `visited` is initialized to track visited nodes.
- DFS starts from node `'A'`.

---

### **4. Recursive DFS Traversal**

#### **Step 2: Visit Node 'A'**

- `'A'` is **not** in `visited`, so:
  - Print `'A'` → **Output:** `A`
  - Add `'A'` to `visited`: `{'A'}`
  - Recursively call `dfs` for `'A'`'s neighbors: `['B', 'C']`

#### **Step 3: Visit Node 'B'**

- `'B'` is **not** in `visited`, so:
  - Print `'B'` → **Output:** `A B`
  - Add `'B'` to `visited`: `{'A', 'B'}`
  - Recursively call `dfs` for `'B'`'s neighbors: `['D', 'E']`

#### **Step 4: Visit Node 'D'**

- `'D'` is **not** in `visited`, so:
  - Print `'D'` → **Output:** `A B D`
  - Add `'D'` to `visited`: `{'A', 'B', 'D'}`
  - `'D'` has **no neighbors**, return to previous recursive call (node `'B'`).

#### **Step 5: Visit Node 'E'**

- `'E'` is **not** in `visited`, so:
  - Print `'E'` → **Output:** `A B D E`
  - Add `'E'` to `visited`: `{'A', 'B', 'D', 'E'}`
  - Recursively call `dfs` for `'E'`'s neighbor: `['F']`

#### **Step 6: Visit Node 'F'**

- `'F'` is **not** in `visited`, so:
  - Print `'F'` → **Output:** `A B D E F`
  - Add `'F'` to `visited`: `{'A', 'B', 'D', 'E', 'F'}`
  - `'F'` has **no neighbors**, return to previous recursive call (node `'E'` → `'B'`).

#### **Step 7: Back to Node 'A', Visit 'C'**

- `'C'` is **not** in `visited`, so:
  - Print `'C'` → **Output:** `A B D E F C`
  - Add `'C'` to `visited`: `{'A', 'B', 'D', 'E', 'F', 'C'}`
  - Recursively call `dfs` for `'C'`'s neighbor: `['F']`

#### **Step 8: Node 'F' Already Visited**

- `'F'` is **already** in `visited`, so we **skip it** and return.

---

### **5. Final Output**

```
A B D E F C
```

- **Traversal Order:** `'A' → 'B' → 'D' → 'E' → 'F' → 'C'`
- `'C'` is visited last because DFS explores each path **deeply** before backtracking.

---

### **6. Key Points**

- DFS **recursively explores** each branch fully before moving to the next.
- The `visited` **set** prevents revisiting nodes.
- DFS **follows a depth-first traversal order**.
- `'F'` was already visited when processing `'C'`, so it was skipped.

