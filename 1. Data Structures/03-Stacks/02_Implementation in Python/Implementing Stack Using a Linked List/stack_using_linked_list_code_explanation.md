# Code Explanation: Stack with Linked List Implementation in Python

Let's break down the code and understand how the `Stack` class works in detail.

## 1. **Node Class**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

The `Node` class is a basic building block for the stack. It has two attributes:

- `data`: This holds the value of the node.
- `next`: This is a pointer to the next node in the stack.

### 2. **Stack Class**

```python
class Stack:
    def __init__(self):
        self.top = None  # Top of the stack (initially None)

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Push a new element onto the stack
    def push(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.top  # Link the new node to the current top
        self.top = new_node  # Update the top to the new node

    # Remove and return the top element from the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")  # Raise error if stack is empty
        popped_data = self.top.data  # Get data from the top node
        self.top = self.top.next  # Move the top to the next node
        return popped_data  # Return the popped data

    # Return the top element without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")  # Raise error if stack is empty
        return self.top.data  # Return the data of the top node

    # String representation of the stack for easy visualization
    def __str__(self):
        if self.is_empty():
            return "Stack is empty"  # Return message if stack is empty
        current = self.top  # Start from the top
        stack_str = ""  # Initialize an empty string
        while current:
            stack_str += str(current.data) + " -> "  # Append current node data
            current = current.next  # Move to the next node
        return stack_str[:-4]  # Remove the last " -> " for cleaner output
```

The `Stack` class implements the stack data structure using a linked list. It has the following methods:

#### **Attributes**

```python
class Stack:
    def __init__(self):
        self.top = None
```

- `top`: This is a pointer to the top node of the stack. Initially, it is set to `None` because the stack is empty.

#### **Methods**

```python
def is_empty(self):
    return self.top is None
```

1. **`is_empty()`**
   - This method checks if the stack is empty by checking if `self.top` is `None`.
   - Returns `True` if the stack is empty, otherwise `False`.

--

```python
def push(self, data):
    new_node = Node(data)
    new_node.next = self.top
    self.top = new_node
```

2. **`push(data)`**
   - This method adds a new node with the given `data` to the top of the stack.
   - A new `Node` object is created with the provided `data`.
   - The `next` attribute of the new node is set to the current `top` node.
   - The `top` pointer is updated to point to the new node.

--

```python
def pop(self):
    if self.is_empty():
        raise IndexError("pop from empty stack")
    popped_data = self.top.data
    self.top = self.top.next
    return popped_data
```

3. **`pop()`**
   - This method removes and returns the top element of the stack.
   - If the stack is empty, it raises an `IndexError`.
   - The `data` of the top node is stored in `popped_data`.
   - The `top` pointer is updated to point to the next node in the stack.
   - The `popped_data` is returned.

--

```python
def peek(self):
    if self.is_empty():
        raise IndexError("peek from empty stack")
    return self.top.data
```

4. **`peek()`**
   - This method returns the `data` of the top node without removing it.
   - If the stack is empty, it raises an `IndexError`.

--

```python
def __str__(self):
    if self.is_empty():
        return "Stack is empty"
    current = self.top
    stack_str = ""
    while current:
        stack_str += str(current.data) + " -> "
        current = current.next
    return stack_str[:-4]  # Remove the last " -> "
```

5. **`__str__()`**
   - This method provides a string representation of the stack.
   - If the stack is empty, it returns "Stack is empty".
   - Otherwise, it traverses the stack from the top to the bottom, appending each node's data to a string separated by " -> ".
   - The last " -> " is removed before returning the string.

### 3. **Example Usage**

Let's go through the example usage step by step:

```python
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack)  # Output: 30 -> 20 -> 10

print("Popped:", stack.pop())  # Output: Popped: 30
print(stack)  # Output: 20 -> 10

print("Top element:", stack.peek())  # Output: Top element: 20

stack.push(40)
print(stack)  # Output: 40 -> 20 -> 10
```

#### **Step-by-Step Execution**

1. **Initialization**
   - `stack = Stack()` creates an empty stack with `top` pointing to `None`.

2. **Push 10**
   - `stack.push(10)` adds a node with `data = 10` to the stack.
   - The stack now looks like: `10 -> None`

3. **Push 20**
   - `stack.push(20)` adds a node with `data = 20` to the stack.
   - The stack now looks like: `20 -> 10 -> None`

4. **Push 30**
   - `stack.push(30)` adds a node with `data = 30` to the stack.
   - The stack now looks like: `30 -> 20 -> 10 -> None`

5. **Print Stack**
   - `print(stack)` outputs: `30 -> 20 -> 10`

6. **Pop**
   - `stack.pop()` removes the top node (`30`) and returns it.
   - The stack now looks like: `20 -> 10 -> None`
   - `print(stack)` outputs: `20 -> 10`

7. **Peek**
   - `stack.peek()` returns the top element (`20`) without removing it.
   - `print("Top element:", stack.peek())` outputs: `Top element: 20`

8. **Push 40**
   - `stack.push(40)` adds a node with `data = 40` to the stack.
   - The stack now looks like: `40 -> 20 -> 10 -> None`
   - `print(stack)` outputs: `40 -> 20 -> 10`

### 4. **Summary**

- The `Stack` class uses a linked list to implement the stack data structure.
- The `push` operation adds an element to the top of the stack.
- The `pop` operation removes and returns the top element.
- The `peek` operation returns the top element without removing it.
- The `__str__` method provides a readable string representation of the stack.

This implementation is efficient for stack operations, with `push`, `pop`, and `peek` all running in **O(1)** time complexity.

---

### Time and Space Complexity Analysis

Let's analyze the **time complexity** and **space complexity** of the `Stack` implementation provided.

---

### **Time Complexity**

1. **`push(data)`**:
   - **Time Complexity**: \(O(1)\)
   - Explanation: Inserting a new node at the top of the stack involves creating a new node and updating the `top` pointer. This is a constant-time operation.

2. **`pop()`**:
   - **Time Complexity**: \(O(1)\)
   - Explanation: Removing the top node involves updating the `top` pointer to the next node. This is also a constant-time operation.

3. **`peek()`**:
   - **Time Complexity**: \(O(1)\)
   - Explanation: Accessing the data of the top node is a constant-time operation.

4. **`is_empty()`**:
   - **Time Complexity**: \(O(1)\)
   - Explanation: Checking if the `top` pointer is `None` is a constant-time operation.

5. **`__str__()`**:
   - **Time Complexity**: \(O(n)\), where \(n\) is the number of elements in the stack.
   - Explanation: The `__str__` method traverses the entire stack to construct the string representation. This requires visiting each node once, so the time complexity is linear in the number of elements.

---

### **Space Complexity**

1. **Overall Space Complexity**:
   - **Space Complexity**: \(O(n)\), where \(n\) is the number of elements in the stack.
   - Explanation: The space required to store the stack is proportional to the number of elements in it. Each node stores data and a pointer to the next node, so the total space used is \(O(n)\).

2. **Auxiliary Space**:
   - **`push(data)`**: \(O(1)\)
     - Explanation: No additional space is required beyond the new node being added.
   - **`pop()`**: \(O(1)\)
     - Explanation: No additional space is required beyond the temporary variable to store the popped data.
   - **`peek()`**: \(O(1)\)
     - Explanation: No additional space is required.
   - **`is_empty()`**: \(O(1)\)
     - Explanation: No additional space is required.
   - **`__str__()`**: \(O(n)\)
     - Explanation: The `stack_str` variable grows linearly with the number of elements in the stack.

---

### **Summary**

| Operation       | Time Complexity | Space Complexity |
|------------------|-----------------|------------------|
| `push(data)`     | \(O(1)\)        | \(O(1)\)         |
| `pop()`          | \(O(1)\)        | \(O(1)\)         |
| `peek()`         | \(O(1)\)        | \(O(1)\)         |
| `is_empty()`     | \(O(1)\)        | \(O(1)\)         |
| `__str__()`      | \(O(n)\)        | \(O(n)\)         |
| **Overall**      | -               | \(O(n)\)         |

---

### **Example Walkthrough**

For the example usage provided:

```python
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack)  # Output: 30 -> 20 -> 10
print("Popped:", stack.pop())  # Output: Popped: 30
print(stack)  # Output: 20 -> 10
print("Top element:", stack.peek())  # Output: Top element: 20
stack.push(40)
print(stack)  # Output: 40 -> 20 -> 10
```

- **Time Complexity**:
  - Each `push`, `pop`, and `peek` operation is \(O(1)\).
  - The `__str__` operation is \(O(n)\), where \(n\) is the number of elements in the stack.

- **Space Complexity**:
  - The stack uses \(O(n)\) space to store the elements.
  - The `__str__` method uses \(O(n)\) auxiliary space to construct the string representation.

This implementation is efficient for stack operations, with constant time for most operations and linear time for string representation.
