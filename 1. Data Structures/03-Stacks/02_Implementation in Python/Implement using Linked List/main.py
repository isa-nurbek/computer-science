# Node class represents an element in the stack
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node (initially None)


# Stack class implements a stack using a linked list
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


# Example usage of the Stack class
stack = Stack()  # Create a new stack

stack.push(10)  # Push 10 onto the stack
stack.push(20)  # Push 20 onto the stack
stack.push(30)  # Push 30 onto the stack

print(stack)  # Output: 30 -> 20 -> 10 (Last In, First Out order)

print("Popped:", stack.pop())  # Output: Popped: 30 (removes top element)
print(stack)  # Output: 20 -> 10 (Stack after popping 30)

print("Top element:", stack.peek())  # Output: Top element: 20 (peek at the top)

stack.push(40)  # Push 40 onto the stack
print(stack)  # Output: 40 -> 20 -> 10 (40 is now the new top)

"""
Output:

30 -> 20 -> 10
Popped: 30
20 -> 10
Top element: 20
40 -> 20 -> 10

"""

# Big O:

"""
## Time and Space Complexity Analysis:

"""

# ********************************************************************************************************************* #

# Code Explanation:

"""
Let's break down the code and understand how the `Stack` class works in detail.

### 1. **Node Class**

The `Node` class is a basic building block for the stack. It has two attributes:
- `data`: This holds the value of the node.
- `next`: This is a pointer to the next node in the stack.

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### 2. **Stack Class**
The `Stack` class implements the stack data structure using a linked list. It has the following methods:

#### **Attributes**
- `top`: This is a pointer to the top node of the stack. Initially, it is set to `None` because the stack is empty.

```
class Stack:
    def __init__(self):
        self.top = None
```

#### **Methods**

1. **`is_empty()`**
   - This method checks if the stack is empty by checking if `self.top` is `None`.
   - Returns `True` if the stack is empty, otherwise `False`.

```
def is_empty(self):
    return self.top is None
```

2. **`push(data)`**
   - This method adds a new node with the given `data` to the top of the stack.
   - A new `Node` object is created with the provided `data`.
   - The `next` attribute of the new node is set to the current `top` node.
   - The `top` pointer is updated to point to the new node.

```
def push(self, data):
    new_node = Node(data)
    new_node.next = self.top
    self.top = new_node
```

3. **`pop()`**
   - This method removes and returns the top element of the stack.
   - If the stack is empty, it raises an `IndexError`.
   - The `data` of the top node is stored in `popped_data`.
   - The `top` pointer is updated to point to the next node in the stack.
   - The `popped_data` is returned.

```
def pop(self):
    if self.is_empty():
        raise IndexError("pop from empty stack")
    popped_data = self.top.data
    self.top = self.top.next
    return popped_data
```

4. **`peek()`**
   - This method returns the `data` of the top node without removing it.
   - If the stack is empty, it raises an `IndexError`.

```
def peek(self):
    if self.is_empty():
        raise IndexError("peek from empty stack")
    return self.top.data
```

5. **`__str__()`**
   - This method provides a string representation of the stack.
   - If the stack is empty, it returns "Stack is empty".
   - Otherwise, it traverses the stack from the top to the bottom, appending each node's data to a string separated by " -> ".
   - The last " -> " is removed before returning the string.

```
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

### 3. **Example Usage**

Let's go through the example usage step by step:

```
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

This implementation is efficient for stack operations, with `push`, `pop`, and
`peek` all running in **O(1)** time complexity.

"""
