# Implementation in Python:


class Node:
    # Initialize a new node with a value and optional link to next node
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    # Get the value stored in the node
    def get_value(self):
        return self.value

    # Get the next node that this node links to
    def get_link_node(self):
        return self.link_node

    # Set the next node that this node links to
    def set_link_node(self, link_node):
        self.link_node = link_node


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")

node1.set_link_node(node2)
node2.set_link_node(node3)

print(node1.get_value())  # A
print(node1.get_link_node().get_value())  # B
print(node2.get_link_node().get_value())  # C

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `Node` class and its methods.

### Time Complexity

1. **`__init__` Method**:
   - This method initializes a new node with a value and an optional link to the next node.
   - **Time Complexity**: O(1) - It involves a constant number of operations (assigning values to `self.value` and `self.link_node`).

2. **`get_value` Method**:
   - This method simply returns the value stored in the node.
   - **Time Complexity**: O(1) - It involves a single operation (returning `self.value`).

3. **`get_link_node` Method**:
   - This method returns the next node that this node links to.
   - **Time Complexity**: O(1) - It involves a single operation (returning `self.link_node`).

4. **`set_link_node` Method**:
   - This method sets the next node that this node links to.
   - **Time Complexity**: O(1) - It involves a single operation (assigning `link_node` to `self.link_node`).

---

### Space Complexity

1. **`__init__` Method**:
   - This method initializes a new node with a value and an optional link to the next node.
   - **Space Complexity**: O(1) - It only requires space for the `value` and `link_node` attributes, which are constant.

2. **`get_value` Method**:
   - This method does not use any additional space beyond what is already allocated for the node.
   - **Space Complexity**: O(1) - No additional space is required.

3. **`get_link_node` Method**:
   - This method does not use any additional space beyond what is already allocated for the node.
   - **Space Complexity**: O(1) - No additional space is required.

4. **`set_link_node` Method**:
   - This method does not use any additional space beyond what is already allocated for the node.
   - **Space Complexity**: O(1) - No additional space is required.

---

### Summary

- **Time Complexity**: All methods in the `Node` class have a time complexity of O(1) because they involve
a constant number of operations.

- **Space Complexity**: All methods in the `Node` class have a space complexity of O(1) because they do not
require any additional space beyond what is already allocated for the node.

This makes the `Node` class very efficient for basic operations, which is typical for a simple linked list node implementation.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The provided code implements a basic **singly linked list** using a `Node` class. Here’s a detailed breakdown:

---

### Code Explanation in detailed:

1. **The `Node` Class**  
   The `Node` class defines a single node in a linked list.  
   Each node stores two pieces of information:
   - **`value`**: The data stored in the node.
   - **`link_node`**: A reference (or pointer) to the next node in the list (or `None` if it's the last node).

   #### Key Methods:
   - **`__init__(self, value, link_node=None)`**  
     - Constructor to initialize the node.
     - `value` is the data stored in the node.  
     - `link_node` is optional and is set to `None` by default, meaning the node doesn't link to another node unless explicitly specified.

   - **`get_value(self)`**  
     - Returns the value stored in the node.

   - **`get_link_node(self)`**  
     - Returns the `link_node`, i.e., the reference to the next node.

   - **`set_link_node(self, link_node)`**  
     - Sets the `link_node` to reference a different node, effectively linking this node to the next node in the list.

---

2. **Creating and Linking Nodes**
   - **`node1 = Node('A')`**  
     Creates a new node with the value `'A'`. Since no `link_node` is provided, `node1.link_node` is set to `None`.
   - **`node2 = Node('B')`**  
     Creates another node with the value `'B'`. Again, `node2.link_node` is set to `None`.
   - **`node3 = Node('C')`**  
     Creates a third node with the value `'C'`. Its `link_node` is also `None`.

   - **`node1.set_link_node(node2)`**  
     Links `node1` to `node2`. Now, `node1.link_node` points to `node2`.

   - **`node2.set_link_node(node3)`**  
     Links `node2` to `node3`. Now, `node2.link_node` points to `node3`.

   At this point, the nodes are linked to form a sequence:
   ```
   node1 ('A') → node2 ('B') → node3 ('C') → None
   ```

---

3. **Accessing and Printing Node Values**
   - **`print(node1.get_value())`**  
     - Calls the `get_value()` method of `node1` and prints `'A'`, the value stored in `node1`.

   - **`print(node1.get_link_node().get_value())`**  
     - `node1.get_link_node()` retrieves the `link_node` of `node1`, which is `node2`.
     - `node2.get_value()` retrieves the value stored in `node2`, which is `'B'`.
     - Prints `'B'`.

   - **`print(node2.get_link_node().get_value())`**  
     - `node2.get_link_node()` retrieves the `link_node` of `node2`, which is `node3`.
     - `node3.get_value()` retrieves the value stored in `node3`, which is `'C'`.
     - Prints `'C'`.

---

### How It Works

This program demonstrates the concept of a **singly linked list**, where each node links to the next one in a linear sequence.  

1. **Dynamic Linking**: Nodes are linked dynamically using `set_link_node()`. You can reorder or extend the chain by
reassigning the links.  
2. **Traversal**: You can traverse the linked list by following the `link_node` references from one node to the next.
3. **Modularity**: Each node is self-contained with its own data (`value`) and a reference to the next node (`link_node`).

---

### Example Visualization

Here’s how the nodes are linked after running the code:

```
Node 1 ('A')  --->  Node 2 ('B')  --->  Node 3 ('C')  --->  None
```

- `node1` points to `node2`.
- `node2` points to `node3`.
- `node3` points to `None` (end of the list).

By calling methods like `get_link_node()` and `get_value()`, you can access and manipulate data in this sequence.

"""
