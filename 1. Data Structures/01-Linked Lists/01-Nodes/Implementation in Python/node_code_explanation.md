# Code Explanation: Node Implementation in Python

This code defines a simple **Node** class to create and manipulate a linked list, where each node contains a value and a reference (or link) to the next node in the list. Here's a step-by-step breakdown of the code and how it works:

---

```python
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
```

---

## Big O Analysis

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

### Summary

- **Time Complexity**: All methods in the `Node` class have a time complexity of O(1) because they involve a constant number of operations.
- **Space Complexity**: All methods in the `Node` class have a space complexity of O(1) because they do not require any additional space beyond what is already allocated for the node.

This makes the `Node` class very efficient for basic operations, which is typical for a simple linked list node implementation.

---

### **Code Breakdown**

#### 1. **Node Class**

- The `Node` class represents an individual unit (or "node") in the linked list.
- Each `Node` has two attributes:
  - `value`: Stores the data for that node.
  - `link_node`: A reference to another node, representing the "link" to the next node in the list. By default, this is set to `None` (i.e., no link).

##### **Methods**

1. `__init__(self, value, link_node=None)`:

    - The constructor initializes a node with a given `value` and an optional `link_node`.
    - If no link is provided, it defaults to `None`.

2. `get_value(self)`:

    - A getter method to retrieve the value stored in the node.

3. `get_link_node(self)`:

    - A getter method to retrieve the reference to the next node (if it exists).

4. `set_link_node(self, link_node)`:
    - A setter method to update the reference to the next node.

---

#### 2. **Creating Nodes**

- Three nodes are created:

```python
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
```

- `node1` stores the value `"A"`, `node2` stores `"B"`, and `node3` stores `"C"`.
- Initially, their `link_node` attributes are `None`.

---

#### 3. **Linking the Nodes**

- The `set_link_node` method is used to connect the nodes:

```python
node1.set_link_node(node2)
node2.set_link_node(node3)
```

- `node1`'s `link_node` now points to `node2`.
- `node2`'s `link_node` now points to `node3`.

---

#### 4. **Accessing Node Data**

- **Print Statements**

```python
print(node1.get_value())  # A
```

- Calls the `get_value()` method of `node1`, which returns `"A"`.

```python
print(node1.get_link_node().get_value())  # B
```

- First, `node1.get_link_node()` retrieves the reference to `node2`.
- Then, `node2.get_value()` retrieves the value stored in `node2`, which is `"B"`.

```python
print(node2.get_link_node().get_value())  # C
```

- Similarly:
  - `node2.get_link_node()` retrieves the reference to `node3`.
  - `node3.get_value()` retrieves the value stored in `node3`, which is `"C"`.

---

### **Execution Flow**

- The program essentially builds and traverses a **singly linked list**, where:
  - `node1` links to `node2`.
  - `node2` links to `node3`.
  - `node3` is the last node and does not link to any other node (`link_node` is `None`).
- The print statements navigate through this chain using the `link_node` references to access each node and display its value.

---

### **Visualization**

The linked list can be visualized as:

```plaintext
[A] -> [B] -> [C] -> None
```

- **`node1`**: `[A] -> [B]`
- **`node2`**: `[B] -> [C]`
- **`node3`**: `[C] -> None`

The code effectively demonstrates the basic structure and traversal of a singly linked list, which is foundational in data structures.
