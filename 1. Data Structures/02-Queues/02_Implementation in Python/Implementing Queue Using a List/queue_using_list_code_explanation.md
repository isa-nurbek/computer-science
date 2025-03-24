# Code Explanation: Queue with List Implementation in Python

## Explanation of the Queue Class and Its Methods

The `Queue` class is a simple implementation of a **First-In-First-Out (FIFO)** data structure. It uses a Python list to store elements and provides methods to manipulate the queue. Below is a detailed explanation of how the code works:

### **`Queue` Class**

```python
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
```

---

### 1. **Initialization (`__init__` method)**

```python
def __init__(self):
    self.queue = []
```

- When a `Queue` object is created, an empty list (`self.queue`) is initialized to store the elements of the queue.

---

### 2. **Enqueue (`enqueue` method)**

```python
def enqueue(self, item):
    self.queue.append(item)
```

- The `enqueue` method adds an element (`item`) to the **rear** (end) of the queue.
- This is done using the `append` method of the list, which adds the item to the end of the list.

---

### 3. **Dequeue (`dequeue` method)**

```python
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

```python
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

```python
def is_empty(self):
    return len(self.queue) == 0
```

- The `is_empty` method checks if the queue is empty by verifying if the length of the list (`self.queue`) is `0`.
- It returns `True` if the queue is empty, otherwise `False`.

---

### 6. **Size of the Queue (`size` method)**

```python
def size(self):
    return len(self.queue)
```

- The `size` method returns the number of elements in the queue by returning the length of the list (`self.queue`).

---

### 7. **String Representation (`__str__` method)**

```python
def __str__(self):
    return str(self.queue)
```

- The `__str__` method provides a string representation of the queue.
- When the `print` function is called on a `Queue` object, this method is invoked, and it returns the list (`self.queue`) as a string.

---

### Example Usage

```python
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

***Output:***

```plaintext
Queue: [10, 20, 30]
Dequeue: 10
Peek: 20
Is empty? False
Size: 2
Queue after operations: [20, 30]
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
- The implementation uses a Python list, which makes it simple but may not be the most efficient for large queues (due to `pop(0)` being O(n) in time complexity).

---

## **Big O Analysis:**

### Time and Space Complexity Analysis

#### Time Complexity Analysis

1. **`enqueue(item)`**:
   - **Time Complexity**: O(1)
   - **Explanation**: Appending an element to the end of a list in Python is an amortized constant-time operation. This is because Python lists are dynamically resized arrays, and while occasional resizing may occur, the average time complexity remains O(1).

2. **`dequeue()`**:
   - **Time Complexity**: O(n)
   - **Explanation**: Removing the first element of a list (`pop(0)`) requires shifting all remaining elements one position to the left. This operation takes linear time relative to the number of elements in the list.

3. **`peek()`**:
   - **Time Complexity**: O(1)
   - **Explanation**: Accessing the first element of the list (`self.queue[0]`) is a constant-time operation.

4. **`is_empty()`**:
   - **Time Complexity**: O(1)
   - **Explanation**: Checking the length of the list (`len(self.queue)`) is a constant-time operation.

5. **`size()`**:
   - **Time Complexity**: O(1)
   - **Explanation**: Similar to `is_empty()`, checking the length of the list is a constant-time operation.

6. **`__str__()`**:
   - **Time Complexity**: O(n)
   - **Explanation**: Converting the list to a string involves iterating over all elements in the list, which takes linear time.

---

#### Space Complexity Analysis

1. **Overall Space Complexity**: O(n)
   - **Explanation**: The space complexity is determined by the number of elements stored in the queue. The `self.queue` list stores all the elements, so the space required grows linearly with the number of elements in the queue.

---

### Optimizing `dequeue()` for O(1) Time Complexity

The current implementation of `dequeue()` has a time complexity of O(n) due to the use of `pop(0)`. To achieve O(1) time complexity for both `enqueue()` and `dequeue()`, you can use a **double-ended queue (deque)** from Python's `collections` module. A deque allows efficient appends and pops from both ends.

Here’s how we can modify the `Queue` class to use a deque:

```python
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
```

---

## **Big O Analysis:**

### Updated Time & Space Complexity Analysis with Deque

#### Time Complexity Analysis

1. **`enqueue(item)`**:
   - **Time Complexity**: O(1)
   - **Explanation**: Appending an element to the end of a `deque` is a constant-time operation.

2. **`dequeue()`**:
   - **Time Complexity**: O(1)
   - **Explanation**: Removing an element from the front of a `deque` is a constant-time operation.

3. **`peek()`**:
   - **Time Complexity**: O(1)
   - **Explanation**: Accessing the first element of a `deque` is a constant-time operation.

4. **`is_empty()`**:
   - **Time Complexity**: O(1)
   - **Explanation**: Checking the length of a `deque` is a constant-time operation.

5. **`size()`**:
   - **Time Complexity**: O(1)
   - **Explanation**: Returning the length of a `deque` is a constant-time operation.

6. **`__str__()`**:
   - **Time Complexity**: O(n)
   - **Explanation**: Converting the `deque` to a list and then to a string requires iterating over all elements, which takes linear time relative to the number of elements (`n`) in the queue.

---

#### Space Complexity Analysis

1. **Overall Space Complexity**:
   - **Space Complexity**: O(n)
   - **Explanation**: The space required by the queue is proportional to the number of elements (`n`) stored in the `deque`. Each element occupies a constant amount of space, so the total space complexity is linear.

---

### Summary

| Operation       | Time Complexity | Space Complexity |
|-----------------|-----------------|------------------|
| `enqueue(item)` | O(1)            | O(1)             |
| `dequeue()`     | O(1)            | O(1)             |
| `peek()`        | O(1)            | O(1)             |
| `is_empty()`    | O(1)            | O(1)             |
| `size()`        | O(1)            | O(1)             |
| `__str__()`     | O(n)            | O(n)             |

The `deque` data structure is highly efficient for implementing a queue, as all core operations (`enqueue`, `dequeue`, `peek`, etc.) are performed in constant time. The space complexity is linear, as it scales with the number of elements in the queue.
