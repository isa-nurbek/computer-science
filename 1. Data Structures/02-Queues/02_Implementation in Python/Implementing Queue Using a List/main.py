# Implementation in Python:


class Queue:
    def __init__(self):
        # Initialize an empty list to store queue elements
        self.queue = []

    def enqueue(self, item):
        """
        Add an element to the rear of the queue.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Remove and return the element at the front of the queue.
        Raises an exception if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")

        return self.queue.pop(0)  # Remove the first element

    def peek(self):
        """
        Return the element at the front of the queue without removing it.
        Raises an exception if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty queue")

        return self.queue[0]  # Return the first element

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return len(self.queue) == 0

    def size(self):
        """
        Return the number of elements in the queue.
        """
        return len(self.queue)

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self.queue)


# Example usage
if __name__ == "__main__":
    q = Queue()

    # Enqueue elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    # Display the queue
    print("Queue:", q)  # Output: Queue: [10, 20, 30]

    # Dequeue an element
    print("Dequeue:", q.dequeue())  # Output: Dequeue: 10

    # Peek at the front element
    print("Peek:", q.peek())  # Output: Peek: 20

    # Check if the queue is empty
    print("Is empty?", q.is_empty())  # Output: Is empty? False

    # Get the size of the queue
    print("Size:", q.size())  # Output: Size: 2

    # Display the queue after operations
    print("Queue after operations:", q)  # Output: Queue after operations: [20, 30]


# Output:

"""
Queue: [10, 20, 30]
Dequeue: 10
Peek: 20
Is empty? False
Size: 2
Queue after operations: [20, 30]

"""

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

1. **`enqueue(item)`**:
   - **Time Complexity**: O(1)
   
   - **Explanation**: Appending an element to the end of a list in Python is an O(1) operation on average. This is because
   Python lists are dynamically allocated arrays, and appending to the end usually doesn't require reallocating memory.

2. **`dequeue()`**:
   - **Time Complexity**: O(n)
   
   - **Explanation**: Removing the first element of a list (`pop(0)`) is an O(n) operation because all subsequent elements
   need to be shifted one position to the left. This makes the operation inefficient for large queues.

3. **`peek()`**:
   - **Time Complexity**: O(1)
   
   - **Explanation**: Accessing the first element of the list (`queue[0]`) is an O(1) operation since it directly accesses
   the element at the specified index.

4. **`is_empty()`**:
   - **Time Complexity**: O(1)
   
   - **Explanation**: Checking the length of the list (`len(self.queue)`) is an O(1) operation in Python.

5. **`size()`**:
   - **Time Complexity**: O(1)
   
   - **Explanation**: Similar to `is_empty()`, checking the length of the list is an O(1) operation.

6. **`__str__()`**:
   - **Time Complexity**: O(n)
   
   - **Explanation**: Converting the list to a string requires iterating over all elements, which is an O(n) operation.

### Space Complexity Analysis

- **Space Complexity**: O(n)
  - **Explanation**: The space complexity is O(n) where `n` is the number of elements in the queue. This is because
  the queue is stored in a list, and the space required grows linearly with the number of elements.

### Optimizations

- **Using `collections.deque`**:
  - If you need a more efficient queue implementation, consider using `collections.deque` from the Python standard library.
  A `deque` (double-ended queue) allows for O(1) time complexity for both `append` (enqueue) and `popleft` (dequeue)
  operations, making it more suitable for queue operations.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""

The `Queue` class is a simple implementation of a **First-In-First-Out (FIFO)** data structure. It uses
a Python list to store elements and provides methods to manipulate the queue. Below is a detailed
explanation of how the code works:

---

### 1. **Initialization (`__init__` method)**
```
def __init__(self):
    self.queue = []
```
- When a `Queue` object is created, an empty list (`self.queue`) is initialized to store the elements of the queue.

---

### 2. **Enqueue (`enqueue` method)**
```
def enqueue(self, item):
    self.queue.append(item)
```
- The `enqueue` method adds an element (`item`) to the **rear** (end) of the queue.
- This is done using the `append` method of the list, which adds the item to the end of the list.

---

### 3. **Dequeue (`dequeue` method)**
```
def dequeue(self):
    if self.is_empty():
        raise IndexError("Dequeue from an empty queue")
    return self.queue.pop(0)
```
- The `dequeue` method removes and returns the element at the **front** (beginning) of the queue.
- If the queue is empty, it raises an `IndexError` to indicate that no elements are available to remove.
- The `pop(0)` method is used to remove the first element of the list, which corresponds to the front of the queue.

---

### 4. **Peek (`peek` method)**
```
def peek(self):
    if self.is_empty():
        raise IndexError("Peek from an empty queue")
    return self.queue[0]
```
- The `peek` method returns the element at the **front** of the queue **without removing it**.
- If the queue is empty, it raises an `IndexError`.
- The first element of the list (`self.queue[0]`) is returned.

---

### 5. **Check if Empty (`is_empty` method)**
```
def is_empty(self):
    return len(self.queue) == 0
```
- The `is_empty` method checks if the queue is empty by verifying if the length of the list (`self.queue`) is `0`.
- It returns `True` if the queue is empty, otherwise `False`.

---

### 6. **Size of the Queue (`size` method)**
```
def size(self):
    return len(self.queue)
```
- The `size` method returns the number of elements in the queue by returning the length of the list (`self.queue`).

---

### 7. **String Representation (`__str__` method)**
```
def __str__(self):
    return str(self.queue)
```
- The `__str__` method provides a string representation of the queue.
- When the `print` function is called on a `Queue` object, this method is invoked, and it returns
the list (`self.queue`) as a string.

---

### Example Usage
```
if __name__ == "__main__":
    q = Queue()

    # Enqueue elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    # Display the queue
    print("Queue:", q)  # Output: Queue: [10, 20, 30]

    # Dequeue an element
    print("Dequeue:", q.dequeue())  # Output: Dequeue: 10

    # Peek at the front element
    print("Peek:", q.peek())  # Output: Peek: 20

    # Check if the queue is empty
    print("Is empty?", q.is_empty())  # Output: Is empty? False

    # Get the size of the queue
    print("Size:", q.size())  # Output: Size: 2

    # Display the queue after operations
    print("Queue after operations:", q)  # Output: Queue after operations: [20, 30]
```

---

### How It Works

1. **Enqueue**: Elements are added to the rear of the queue using the `enqueue` method.
2. **Dequeue**: Elements are removed from the front of the queue using the `dequeue` method.
3. **Peek**: The front element is viewed without removing it using the `peek` method.
4. **Check if Empty**: The `is_empty` method checks if the queue has no elements.
5. **Size**: The `size` method returns the number of elements in the queue.
6. **String Representation**: The `__str__` method allows the queue to be printed in a readable format.

---

### Key Points

- The queue follows the **FIFO** principle: the first element added is the first one to be removed.
- The `dequeue` and `peek` methods raise exceptions if the queue is empty to prevent invalid operations.
- The implementation uses a Python list, which makes it simple but may not be the most efficient
for large queues (due to `pop(0)` being O(n) in time complexity).

"""

# =========================================================================================================================== #

# Optimized Version:

"""
### Optimizing `dequeue()` for O(1) Time Complexity

The current implementation of `dequeue()` has a time complexity of O(n) due to the use of `pop(0)`.
To achieve O(1) time complexity for both `enqueue()` and `dequeue()`, we can use a **double-ended
queue (deque)** from Python's `collections` module. A deque allows efficient appends and pops from both ends.

Here’s how you can modify the `Queue` class to use a deque:

"""

# Implementation in Python:

from collections import deque


class Queue:
    def __init__(self):
        # Initialize a deque to store queue elements
        self.queue = deque()

    def enqueue(self, item):
        """
        Add an element to the rear of the queue.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Remove and return the element at the front of the queue.
        Raises an exception if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.popleft()  # Remove the first element in O(1) time

    def peek(self):
        """
        Return the element at the front of the queue without removing it.
        Raises an exception if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[0]  # Return the first element in O(1) time

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return len(self.queue) == 0

    def size(self):
        """
        Return the number of elements in the queue.
        """
        return len(self.queue)

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(list(self.queue))


# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of each method in the `Queue` class:

---

### 1. **`enqueue(item)`**
   - **Time Complexity**: O(1)
   
     - Appending an element to the end of a `deque` is a constant-time operation.
     
   - **Space Complexity**: O(1)
   
     - No additional space is used apart from storing the item in the `deque`.

---

### 2. **`dequeue()`**
   - **Time Complexity**: O(1)
   
     - Removing an element from the front of a `deque` is a constant-time operation.
     
   - **Space Complexity**: O(1)
   
     - No additional space is used.

---

### 3. **`peek()`**
   - **Time Complexity**: O(1)
   
     - Accessing the first element of a `deque` is a constant-time operation.
     
   - **Space Complexity**: O(1)
   
     - No additional space is used.

---

### 4. **`is_empty()`**
   - **Time Complexity**: O(1)
   
     - Checking the length of a `deque` is a constant-time operation.
     
   - **Space Complexity**: O(1)
   
     - No additional space is used.

---

### 5. **`size()`**
   - **Time Complexity**: O(1)
   
     - Checking the length of a `deque` is a constant-time operation.
     
   - **Space Complexity**: O(1)
   
     - No additional space is used.

---

### 6. **`__str__()`**
   - **Time Complexity**: O(n)
   
     - Converting the `deque` to a list requires iterating over all `n` elements.
     
   - **Space Complexity**: O(n)
   
     - A new list of size `n` is created to represent the queue.

---

### Summary of Time and Space Complexity:

| Method       | Time Complexity | Space Complexity |
|--------------|-----------------|------------------|
| `enqueue`    | O(1)            | O(1)             |
| `dequeue`    | O(1)            | O(1)             |
| `peek`       | O(1)            | O(1)             |
| `is_empty`   | O(1)            | O(1)             |
| `size`       | O(1)            | O(1)             |
| `__str__`    | O(n)            | O(n)             |

---

### Notes:
- The `deque` data structure is optimized for fast appends and pops from both ends, making it ideal for implementing a queue.
- The `__str__` method is the only operation with O(n) time and space complexity because it creates a new list representation
of the queue. All other operations are constant time and space.

"""
