# Code Explanation: Singly Linked List Implementation in Python

This code defines two Python classes, `Node` and `LinkedList`, to implement a singly linked list. Let's go through it step by step:

---

## **Node Class**

---

```python
class Node:
    # Initialize a new node with a value and optional next node reference
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    # Return the value stored in this node
    def get_value(self):
        return self.value

    # Return the reference to the next node
    def get_next_node(self):
        return self.next_node

    # Set the reference to the next node
    def set_next_node(self, next_node):
        self.next_node = next_node

    # String representation of the node
    def __str__(self):
        return f"Node({self.value})"

```

---

### Purpose:

The `Node` class represents a single element in the linked list, containing:

1. **A value (`value`)**: The data the node holds.
2. **A reference to the next node (`next_node`)**: A pointer to the next `Node` in the list.

### Key Methods:

1. **`__init__(value, next_node=None)`**: Constructor to initialize a node with a given value and an optional reference to the next node.
2. **`get_value()`**: Returns the value stored in the node.
3. **`get_next_node()`**: Returns the reference to the next node.
4. **`set_next_node(next_node)`**: Updates the reference to point to another node.
5. **`__str__()`**: Returns a string representation of the node (`Node(value)`).

---

## **Linked List Class**

---

```python
class LinkedList:
    # Initialize a new linked list with an optional starting value
    def __init__(self, value=None):
        self.head_node = Node(value)

    # Return the first node in the list
    def get_head_node(self):
        return self.head_node

    # Add a new node at the beginning of the list
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)  # Link new node to current head
        self.head_node = new_node  # Update head to new node

    # Add a new node at the end of the list
    def insert_end(self, value):
        new_node = Node(value)
        # Handle empty list case
        if self.head_node is None:
            self.head_node = new_node
            return

        # Find the last node in the list
        current_node = self.head_node
        while current_node.get_next_node() is not None:
            current_node = current_node.get_next_node()

        # Link the last node to our new node
        current_node.set_next_node(new_node)

    # Remove the first occurrence of a node with the specified value
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()

        # Special case: removing head node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            # Traverse list looking for the value to remove
            while current_node:
                next_node = current_node.get_next_node()
                if next_node and next_node.get_value() == value_to_remove:
                    current_node.set_next_node(
                        next_node.get_next_node()
                    )  # Skip over the removed node
                    current_node = None  # Exit the loop
                else:
                    current_node = next_node

    # Convert the linked list to a string representation
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        # Traverse the list and build string representation
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()

        return string_list


# Test the LinkedList implementation
ll = LinkedList("D")  # Create new list with 'D' as head
ll.insert_beginning("C")  # Add 'C' to the beginning
ll.insert_beginning("B")  # Add 'B' to the beginning
ll.insert_beginning("A")  # Add 'A' to the beginning
print(ll.stringify_list())  # Print the list: A->B->C->D

ll.remove_node("B")  # Remove node with value 'B'
print(ll.stringify_list())  # Print the modified list: A->C->D


```

---

### Purpose:

The `LinkedList` class manages a collection of `Node` instances and provides utility methods to perform common operations on the list.

### Key Methods:

1. **`__init__(value=None)`**:

    - Initializes the list with an optional value for the head node.
    - If no value is provided, the head node is `None`.

2. **`get_head_node()`**:

    - Returns the head (first) node of the list.

3. **`insert_beginning(new_value)`**:

    - Adds a new node with the specified value at the start of the list.
    - Steps:
        - Create a new node with the given value.
        - Set its `next_node` to the current head node.
        - Update the list's `head_node` to this new node.

4. **`insert_end(value)`**:

    - Adds a new node with the specified value at the end of the list.
    - Steps:
        - If the list is empty (`head_node` is `None`), set the new node as the head.
        - Otherwise, traverse the list to find the last node (a node whose `next_node` is `None`).
        - Update the last node's `next_node` to reference the new node.

5. **`remove_node(value_to_remove)`**:

    - Removes the first node with the specified value.
    - Steps:
        - Check if the head node contains the value to remove. If so, update `head_node` to skip the current head.
        - Otherwise, traverse the list while keeping track of the current node and the next node.
        - If the next node contains the value to remove, skip it by updating the `next_node` of the current node.

6. **`stringify_list()`**:
    - Returns a string representation of the list by concatenating the values of all nodes.
    - Steps:
        - Start from the head node and traverse the list.
        - Append each node's value to a string, followed by a newline.

---

### Example Execution

#### 1. **Initialization and Adding Nodes**

```python
ll = LinkedList("D")  # Creates a linked list with 'D' as the head node.
ll.insert_beginning("C")  # Adds 'C' before 'D': C -> D
ll.insert_beginning("B")  # Adds 'B' before 'C': B -> C -> D
ll.insert_beginning("A")  # Adds 'A' before 'B': A -> B -> C -> D
```

-   The list structure becomes:  
    **A → B → C → D**

#### 2. **Printing the List**

```python
print(ll.stringify_list())
```

This traverses the list starting from the head node (`A`), appending each value to the string. Output:

```
A
B
C
D
```

#### 3. **Removing a Node**

```python
ll.remove_node("B")
```

-   **Step 1**: Check if the head node (`A`) contains the value `"B"`. It doesn't.
-   **Step 2**: Traverse the list. The `next_node` of `A` is `B`, which matches the value to remove.
-   **Step 3**: Update the `next_node` of `A` to skip `B` and point to `C`.

The list structure becomes:  
**A → C → D**

#### 4. **Printing the Modified List**

```python
print(ll.stringify_list())
```

This traverses the updated list, starting from `A`. Output:

```
A
C
D
```

---

### Summary of Key Features:

1. **Dynamic Insertion**:
    - Nodes can be added at the beginning or end of the list.
2. **Removal**:
    - The `remove_node` method handles edge cases like removing the head node.
3. **Traversal**:
    - The `stringify_list` method ensures easy visualization of the list contents.

This implementation is a simple yet powerful way to work with linked lists in Python!

---

## **Big O:**

The **Big O complexity** of operations in `LinkedList` implementation is as follows:

### **1. `insert_beginning(new_value)`**

-   **Complexity:** \(O(1)\)
-   **Explanation:** This operation involves creating a new node and updating the `head_node` reference, which takes constant time.

---

### **2. `insert_end(value)`**

-   **Complexity:** \(O(n)\)
-   **Explanation:** In the worst case, you traverse the entire list to find the last node before inserting the new node at the end. This traversal takes linear time, where \(n\) is the number of nodes in the list.

---

### **3. `remove_node(value_to_remove)`**

-   **Complexity:** \(O(n)\)
-   **Explanation:**
    -   In the worst case, you need to traverse the entire list to find the node with the value to remove.
    -   The traversal is linear in the number of nodes \(n\).

---

### **4. `stringify_list()`**

-   **Complexity:** \(O(n)\)
-   **Explanation:** This operation traverses all \(n\) nodes in the list to build the string representation. Each traversal step takes \(O(1)\), leading to a total complexity of \(O(n)\).
