# Recursion vs. Iteration: A Detailed Comparison

## Fundamental Differences

**Recursion** is a programming technique where a function calls itself directly or indirectly to solve a problem by breaking it down into smaller subproblems.

**Iteration** uses looping constructs (like for, while, do-while) to repeatedly execute a block of code until a condition is met.

## Key Differences

### 1. Approach to Problem Solving

- **Recursion**: Follows a "divide and conquer" approach - breaks problem into smaller instances of itself
- **Iteration**: Uses repetition - executes the same code block multiple times with changing state

### 2. Control Flow

- **Recursion**: Implicit control flow through function calls and the call stack
- **Iteration**: Explicit control flow through loop conditions and counters

### 3. Termination Condition

- **Recursion**: Base case(s) stop the recursion
- **Iteration**: Loop condition stops the iteration

### 4. Memory Usage

- **Recursion**: Uses call stack, potentially leading to stack overflow for deep recursion
- **Iteration**: Generally uses constant memory (just variables)

### 5. Performance

- **Recursion**: Function call overhead (stack frame creation/cleanup)
- **Iteration**: Typically more efficient as it avoids function call overhead

## When to Use Each

### Use Recursion When

- The problem naturally fits a recursive definition (e.g., tree traversals, divide-and-conquer algorithms)
- The solution is more elegant and readable in recursive form
- The depth of recursion is manageable and won't cause stack overflow

### Use Iteration When

- Performance is critical and stack overflow is a concern
- The problem can be easily expressed with loops
- You need fine-grained control over the execution flow

---

## 🔁 Iteration vs. 🌀 Recursion: What's the Difference?

| Feature              | Recursion                                    | Iteration                                |
|----------------------|----------------------------------------------|------------------------------------------|
| **Definition**       | A function that calls itself                 | A loop (e.g., `for` or `while`)          |
| **Control Flow**     | Function calls itself repeatedly             | Repeats a block of code using loops      |
| **Termination**      | Base case ends the recursive calls           | Loop ends with a condition               |
| **Memory Usage**     | Uses call stack (extra memory)               | Uses constant memory                     |
| **Speed**            | Slower due to overhead of function calls     | Faster due to no function call overhead  |
| **Best Use Case**    | Naturally recursive problems (trees, graphs) | Linear tasks (searching, counting, etc.) |

---

## 🔢 Example: Factorial of a Number

### 1. **Recursive Version**

```python
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
```

🔍 **Explanation**:

- Calls itself with `n-1` until it reaches `1`
- `factorial_recursive(5)` calls `factorial_recursive(4)` … until `factorial_recursive(1)` returns `1`

🧠 **Time Complexity**: `O(n)`  
📦 **Space Complexity**: `O(n)` (due to call stack)

---

### 2. **Iterative Version**

```python
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

🔍 **Explanation**:

- Uses a `for` loop from `2` to `n`
- Multiplies result step by step

🧠 **Time Complexity**: `O(n)`  
📦 **Space Complexity**: `O(1)` (constant space)

---

## 🧮 Another Example: Fibonacci Numbers

### Recursive Version

```python
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
```

🧠 **Time Complexity**: `O(2ⁿ)` — very inefficient due to repeated calculations  
📦 **Space Complexity**: `O(n)` — max depth of the recursion tree

---

### Iterative Version

```python
def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
```

🧠 **Time Complexity**: `O(n)`  
📦 **Space Complexity**: `O(1)`

---

## 🚨 When to Use Recursion vs Iteration?

### ✅ Use **Recursion** When

- The problem is naturally recursive (e.g., **tree traversal**, **DFS**, **combinations**, etc.)
- It simplifies code logic (though may need optimization)

### ✅ Use **Iteration** When

- You want **better performance** and **less memory**
- The problem doesn’t need stack-based memory
- You need to avoid **stack overflow** for large input sizes

---

## 🚀 Optimizing Recursion: Memoization

Recursive Fibonacci is slow. Add **memoization** to make it efficient:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_memo(n-1) + fibonacci_memo(n-2)
```

🧠 Time Complexity with memo: `O(n)`  
📦 Space Complexity: `O(n)` (for cache and recursion stack)

---

## DFS vs BFS (Recursion vs. Iteration)

Let’s go deeper by comparing **Recursion vs. Iteration** with a classic recursive problem: **Tree Traversal**, and also compare with **Graph Traversal** (DFS vs BFS) to show real-life use cases.

## 🌳 Binary Tree Traversal – Recursion vs Iteration

Say we have this binary tree:

```plaintext
      1
     / \
    2   3
   / \
  4   5
```

### Tree Node Definition in Python

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

---

### 1. **Inorder Traversal (Left ➝ Root ➝ Right)**

#### ✅ Recursive Version

```python
def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.val, end=' ')
        inorder_recursive(root.right)
```

#### ✅ Iterative Version

```python
def inorder_iterative(root):
    stack = []
    current = root
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print(current.val, end=' ')
            current = current.right
```

### 🔍 Complexity (Both Versions)

- **Time Complexity**: `O(n)` (visit every node once)
- **Space Complexity**:  
  - Recursive: `O(h)` (h = height of tree, for call stack)
  - Iterative: `O(h)` (explicit stack)

---

## 🌐 Graph Traversal – DFS vs BFS

We’ll show both **recursive** and **iterative** DFS, and also **BFS** using a queue.

Say we have this graph:

```plaintext
Graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
```

---

### 🔍 Depth-First Search (DFS)

#### ✅ Recursive DFS

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)
```

#### ✅ Iterative DFS (using Stack)

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Push neighbors in reverse to maintain order
            stack.extend(reversed(graph[node]))
```

---

### 🔁 Breadth-First Search (BFS)

✅ **Always iterative** using a **queue**

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])
```

---

### 🔬 Complexity Analysis

| Algorithm      | Time Complexity  | Space Complexity | Notes                         |
|----------------|------------------|------------------|-------------------------------|
| DFS (rec/iter) | `O(V + E)`       | `O(V)`           | Stack depth or explicit stack |
| BFS            | `O(V + E)`       | `O(V)`           | Uses a queue                  |

Where:

- `V` = number of vertices
- `E` = number of edges

---

## 🧠 Recap: When to Use What?

| Task Type                          | Use Recursion                   | Use Iteration               |
|------------------------------------|---------------------------------|-----------------------------|
| Tree Traversal                     | ✅ Clean and simple             | ✅ Avoid recursion limit   |
| Graph DFS                          | ✅ or Iteration (both fine)     | ✅ Same performance        |
| Fibonacci / Factorial              | ✅ With memoization             | ✅ Faster without memo     |
| BFS                                | ❌ Not natural in recursion     | ✅ Queue-based             |
| Deep recursion (e.g. depth > 1000) | ❌ May hit stack overflow       | ✅ Safer                   |

---

## Sorting Algorithms (Recursion vs Iteration)

Let’s go through some **popular sorting algorithms** that use **recursion**, along with how they work, Python code, and their time/space complexities.

## 🔀 Sorting Algorithms Using Recursion

### 1. **Merge Sort** – Divide and Conquer

Merge Sort splits the array in half recursively, sorts each half, and merges them.

#### ✅ Python Code

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Merge two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

🧠 **Time Complexity**: `O(n log n)`  
📦 **Space Complexity**: `O(n)` (extra space for merging)

---

### 2. **Quick Sort** – Divide and Conquer (but in-place)

Quick Sort picks a pivot, partitions the array, and recursively sorts the sub-arrays.

#### ✅ Python Code

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)
```

🧠 **Time Complexity**:

- Best/Average: `O(n log n)`
- Worst: `O(n²)` (if pivot is badly chosen)

📦 **Space Complexity**: `O(n)` (because it returns new arrays)

---

### 🔄 In-Place Quick Sort Version (No Extra Space)

```python
def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
```

📦 **Space Complexity**: `O(log n)` (for recursive calls only – no extra lists)

---

### 3. **Heap Sort** (Not recursive by nature, but can use recursive heapify)

```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # Recursive call

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
```

🧠 **Time Complexity**: `O(n log n)`  
📦 **Space Complexity**: `O(1)` (in-place sorting)

---

## 🔁 Comparison Table of Recursive Sorting Algorithms

| Algorithm    | Time (Best/Average/Worst)                  | Space                | Stable? | In-Place?                  |
|--------------|--------------------------------------------|----------------------|---------|----------------------------|
| Merge Sort   | `O(n log n)` / `O(n log n)` / `O(n log n)` | `O(n)`               | ✅ Yes  | ❌ No                     |
| Quick Sort   | `O(n log n)` / `O(n log n)` / `O(n²)`      | `O(log n)` or `O(n)` | ❌ No   | ✅ Yes (in-place version) |
| Heap Sort    | `O(n log n)` / `O(n log n)` / `O(n log n)` | `O(1)`               | ❌ No   | ✅ Yes                    |

---
