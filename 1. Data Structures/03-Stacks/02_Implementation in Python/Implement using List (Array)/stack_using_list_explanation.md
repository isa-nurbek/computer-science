# Code Explanation: Stack with List Implementation in Python

## Explanation of the `Stack` Class

A **stack** is a fundamental data structure that follows the **Last-In-First-Out (LIFO)** principle. This means that the last element added to the stack is the first one to be removed. The `Stack` class provided here is a simple implementation of this concept using a Python list.

---

### Key Components of the `Stack` Class

1. **`__init__` Method (Constructor):**

   ```python
   def __init__(self):
       self.items = []
   ```

   - This initializes an empty list called `items` to store the elements of the stack.
   - The list `items` acts as the underlying data structure for the stack.

2. **`is_empty` Method:**

   ```python
   def is_empty(self):
       return len(self.items) == 0
   ```

   - This method checks if the stack is empty.
   - It returns `True` if the length of the `items` list is `0`, otherwise `False`.

3. **`push` Method:**

   ```python
   def push(self, item):
       self.items.append(item)
   ```

   - This method adds an element (`item`) to the top of the stack.
   - It uses the `append` method of the list to add the item to the end of the list (which represents the top of the stack).

4. **`pop` Method:**

   ```python
   def pop(self):
       if self.is_empty():
           raise IndexError("pop from empty stack")
       return self.items.pop()
   ```

   - This method removes and returns the top element of the stack.
   - If the stack is empty, it raises an `IndexError` to prevent invalid operations.
   - The `pop` method of the list is used to remove and return the last element.

5. **`peek` Method:**

   ```python
   def peek(self):
       if self.is_empty():
           raise IndexError("peek from empty stack")
       return self.items[-1]
   ```

   - This method returns the top element of the stack without removing it.
   - If the stack is empty, it raises an `IndexError`.
   - It uses list indexing (`items[-1]`) to access the last element.

6. **`size` Method:**

   ```python
   def size(self):
       return len(self.items)
   ```

   - This method returns the number of elements in the stack.
   - It uses the `len` function to determine the length of the `items` list.

7. **`__str__` Method:**

   ```python
   def __str__(self):
       return str(self.items)
   ```

   - This method provides a string representation of the stack.
   - It converts the `items` list to a string for easy printing and debugging.

---

### How the Stack Works

1. **Initialization:**
   - When a `Stack` object is created, the `__init__` method initializes an empty list (`items`).

2. **Pushing Elements:**
   - The `push` method adds elements to the top of the stack. For example:

     ```python
     stack.push(10)  # Stack: [10]
     stack.push(20)  # Stack: [10, 20]
     stack.push(30)  # Stack: [10, 20, 30]
     ```

3. **Popping Elements:**
   - The `pop` method removes and returns the top element. For example:

     ```python
     stack.pop()  # Returns 30, Stack: [10, 20]
     ```

4. **Peeking at the Top Element:**
   - The `peek` method allows you to view the top element without removing it. For example:

     ```python
     stack.peek()  # Returns 20, Stack: [10, 20]
     ```

5. **Checking if the Stack is Empty:**
   - The `is_empty` method checks if the stack has no elements. For example:

     ```python
     stack.is_empty()  # Returns False
     ```

6. **Getting the Size of the Stack:**
   - The `size` method returns the number of elements in the stack. For example:

     ```python
     stack.size()  # Returns 2
     ```

7. **String Representation:**
   - The `__str__` method provides a readable representation of the stack. For example:

     ```python
     print(stack)  # Output: [10, 20]
     ```

---

### Example Usage

```python
if __name__ == "__main__":
    stack = Stack()

    # Push elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack after pushes:", stack)  # Output: [10, 20, 30]

    # Pop an element from the stack
    print("Popped:", stack.pop())  # Output: 30
    print("Stack after pop:", stack)  # Output: [10, 20]

    # Peek at the top element
    print("Top element:", stack.peek())  # Output: 20

    # Check if the stack is empty
    print("Is stack empty?", stack.is_empty())  # Output: False

    # Get the size of the stack
    print("Stack size:", stack.size())  # Output: 2
```

---

### Key Points to Remember

- The stack follows the **LIFO** principle.
- The `push` and `pop` operations are performed at the **top** of the stack.
- The `peek` operation allows you to inspect the top element without modifying the stack.
- The `size` and `is_empty` methods provide information about the stack's state.
- The `__str__` method makes it easy to visualize the stack's contents.

This implementation is simple and efficient for basic stack operations, making it a great starting point for understanding stacks in Python.

### Time and Space Complexity Analysis

Let's analyze the **time** and **space complexity** of each operation in the `Stack` class:

---

### **Time Complexity**

1. **`__init__`**:
   - **Time Complexity**: \(O(1)\)
   - Initializing an empty list is a constant-time operation.

2. **`is_empty`**:
   - **Time Complexity**: \(O(1)\)
   - Checking the length of a list is a constant-time operation.

3. **`push`**:
   - **Time Complexity**: \(O(1)\)
   - Appending an item to the end of a list is a constant-time operation in Python (amortized).

4. **`pop`**:
   - **Time Complexity**: \(O(1)\)
   - Removing the last item from a list is a constant-time operation.

5. **`peek`**:
   - **Time Complexity**: \(O(1)\)
   - Accessing the last element of a list is a constant-time operation.

6. **`size`**:
   - **Time Complexity**: \(O(1)\)
   - Getting the length of a list is a constant-time operation.

7. **`__str__`**:
   - **Time Complexity**: \(O(n)\), where \(n\) is the number of elements in the stack.
   - Converting the list to a string requires iterating over all elements.

---

### **Space Complexity**

1. **Overall Space Complexity**:
   - **Space Complexity**: \(O(n)\), where \(n\) is the number of elements in the stack.
   - The space is dominated by the list `self.items`, which stores all the elements of the stack.

2. **Auxiliary Space for Operations**:
   - All operations (except `__str__`) use \(O(1)\) auxiliary space.
   - The `__str__` method uses \(O(n)\) auxiliary space to create the string representation of the stack.

---

### **Summary**

| Operation      | Time Complexity | Space Complexity |
|----------------|-----------------|------------------|
| `__init__`     | \(O(1)\)        | \(O(1)\)         |
| `is_empty`     | \(O(1)\)        | \(O(1)\)         |
| `push`         | \(O(1)\)        | \(O(1)\)         |
| `pop`          | \(O(1)\)        | \(O(1)\)         |
| `peek`         | \(O(1)\)        | \(O(1)\)         |
| `size`         | \(O(1)\)        | \(O(1)\)         |
| `__str__`      | \(O(n)\)        | \(O(n)\)         |

---

### **Example Analysis**

For the example usage provided:

1. **Push Operations**:
   - `stack.push(10)`, `stack.push(20)`, `stack.push(30)` each take \(O(1)\) time.
2. **Pop Operation**:
   - `stack.pop()` takes \(O(1)\) time.
3. **Peek Operation**:
   - `stack.peek()` takes \(O(1)\) time.
4. **`__str__` Operation**:
   - `print("Stack after pushes:", stack)` takes \(O(n)\) time, where \(n = 3\) (since the stack has 3 elements).

The overall time complexity for the example is \(O(n)\), dominated by the `__str__` operation. The space complexity is \(O(n)\) due to the storage of the stack elements.
