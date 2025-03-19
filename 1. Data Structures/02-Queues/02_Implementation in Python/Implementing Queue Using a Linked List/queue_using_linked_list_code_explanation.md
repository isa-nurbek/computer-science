# Code Explanation: Queue with Linked List Implementation in Python

The provided code defines a simple **Queue** data structure using a **singly linked list**. Below is a detailed explanation of how the code works, broken down into its components:

---

## 1. **Node Class**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

- The `Node` class represents a single node in the linked list.
- Each node has two attributes:
  - `data`: Stores the value of the node.
  - `next`: A pointer to the next node in the list. Initially, it is set to `None`.

---

## 2. **Queue Class**

```python
class Queue:
    def __init__(self):
        self.front = None  # Points to the front (first) element of the queue
        self.rear = None  # Points to the rear (last) element of the queue

    # Check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Add an element to the rear of the queue
    def enqueue(self, data):
        new_node = Node(data)  # Create a new node with the given data

        # If the queue is empty, both front and rear should point to new node
        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node  # Link the current rear node to the new node
        self.rear = new_node  # Update the rear pointer

    # Remove an element from the front of the queue
    def dequeue(self):
        if self.is_empty():  # Check if the queue is empty before removing
            raise IndexError("Dequeue from an empty queue")

        temp = self.front  # Store the front node to return its data later
        self.front = temp.next  # Move front to the next node

        if self.front is None:  # If the queue becomes empty, reset rear as well
            self.rear = None

        return temp.data  # Return the removed element's data

    # View the front element without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")

        return self.front.data  # Return the front element's data

    # Return a string representation of the queue
    def __str__(self):
        if self.is_empty():
            return "Queue is empty"

        temp = self.front  # Start from the front of the queue
        queue_str = []

        while temp:  # Traverse the queue
            queue_str.append(str(temp.data))  # Collect data values
            temp = temp.next

        return " -> ".join(queue_str)  # Format as a string
```

The `Queue` class implements the queue data structure using the `Node` class. A queue follows the **First-In-First-Out (FIFO)** principle, meaning the first element added is the first one to be removed.

### Attributes

- `front`: A pointer to the first node in the queue (the node to be dequeued next).
- `rear`: A pointer to the last node in the queue (the node most recently enqueued).

### Methods

#### a. **`__init__` (Constructor)**

```python
def __init__(self):
    self.front = None
    self.rear = None
```

- Initializes an empty queue by setting both `front` and `rear` to `None`.

---

#### b. **`is_empty`**

```python
def is_empty(self):
    return self.front is None
```

- Checks if the queue is empty by verifying if `front` is `None`.
- Returns `True` if the queue is empty, otherwise `False`.

---

#### c. **`enqueue`**

```python
def enqueue(self, data):
    new_node = Node(data)
    if self.rear is None:
        self.front = self.rear = new_node
        return
    self.rear.next = new_node
    self.rear = new_node
```

- Adds a new node to the end of the queue.
- Steps:
  1. Create a new node with the given `data`.
  2. If the queue is empty (`rear` is `None`), set both `front` and `rear` to the new node.
  3. If the queue is not empty:
     - Link the current `rear` node's `next` pointer to the new node.
     - Update `rear` to point to the new node.

---

#### d. **`dequeue`**

```python
def dequeue(self):
    if self.is_empty():
        raise IndexError("Dequeue from an empty queue")
    temp = self.front
    self.front = temp.next
    if self.front is None:
        self.rear = None
    return temp.data
```

- Removes and returns the node at the front of the queue.
- Steps:
  1. Check if the queue is empty. If it is, raise an `IndexError`.
  2. Store the current `front` node in a temporary variable `temp`.
  3. Move the `front` pointer to the next node in the queue.
  4. If the queue becomes empty after dequeueing (`front` is `None`), set `rear` to `None`.
  5. Return the `data` of the dequeued node.

---

#### e. **`peek`**

```python
def peek(self):
    if self.is_empty():
        raise IndexError("Peek from an empty queue")
    return self.front.data
```

- Returns the `data` of the node at the front of the queue without removing it.
- If the queue is empty, raises an `IndexError`.

---

#### f. **`__str__`**

```python
def __str__(self):
    if self.is_empty():
        return "Queue is empty"
    temp = self.front
    queue_str = []
    while temp:
        queue_str.append(str(temp.data))
        temp = temp.next
    return " -> ".join(queue_str)
```

- Provides a string representation of the queue.
- Steps:
  1. If the queue is empty, return `"Queue is empty"`.
  2. Otherwise, traverse the queue from `front` to `rear`, appending each node's `data` to a list.
  3. Join the list elements with `" -> "` to represent the queue as a string.

---

## 3. **Example Usage**

```python
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue:", queue)  # Output: Queue: 10 -> 20 -> 30

print("Dequeue:", queue.dequeue())  # Output: Dequeue: 10

print("Queue after dequeue:", queue)  # Output: Queue after dequeue: 20 -> 30

print("Peek:", queue.peek())  # Output: Peek: 20
```

- **Step-by-Step Execution:**
  1. Create an empty queue.
  2. Enqueue `10`, `20`, and `30` into the queue. The queue now looks like: `10 -> 20 -> 30`.
  3. Print the queue: `Queue: 10 -> 20 -> 30`.
  4. Dequeue the front element (`10`). The queue now looks like: `20 -> 30`.
  5. Print the queue after dequeue: `Queue after dequeue: 20 -> 30`.
  6. Peek at the front element (`20`) without removing it.

---

## 4. **Key Points**

- The queue is implemented using a singly linked list, where `front` points to the first node and `rear` points to the last node.
- Enqueueing adds a node to the `rear`, and dequeueing removes a node from the `front`.
- The `__str__` method provides a visual representation of the queue.
- The `is_empty` method is used to handle edge cases (e.g., dequeueing or peeking from an empty queue).

This implementation is efficient and adheres to the FIFO principle of a queue.

---

## **Big O Analysis:**

### Time and Space Complexity Analysis

#### Time Complexity

1. **`is_empty()`**:
   - **Time Complexity**: O(1)
   - **Explanation**: This method simply checks if `self.front` is `None`, which is a constant-time operation.

2. **`enqueue(data)`**:
   - **Time Complexity**: O(1)
   - **Explanation**: Adding an element to the rear of the queue involves creating a new node and updating the `rear` pointer. This is a constant-time operation since no traversal is needed.

3. **`dequeue()`**:
   - **Time Complexity**: O(1)
   - **Explanation**: Removing an element from the front of the queue involves updating the `front` pointer to the next node. This is also a constant-time operation.

4. **`peek()`**:
   - **Time Complexity**: O(1)
   - **Explanation**: Peeking at the front element involves accessing the `data` attribute of the `front` node, which is a constant-time operation.

5. **`__str__()`**:
   - **Time Complexity**: O(n)
   - **Explanation**: This method traverses the entire queue to collect the data values of all nodes, where `n` is the number of elements in the queue. Therefore, the time complexity is linear with respect to the number of elements.

#### Space Complexity

1. **`is_empty()`**:
   - **Space Complexity**: O(1)
   - **Explanation**: This method uses a constant amount of space.

2. **`enqueue(data)`**:
   - **Space Complexity**: O(1)
   - **Explanation**: This method creates a single new node, so the space complexity is constant.

3. **`dequeue()`**:
   - **Space Complexity**: O(1)
   - **Explanation**: This method uses a constant amount of space to store the temporary node.

4. **`peek()`**:
   - **Space Complexity**: O(1)
   - **Explanation**: This method uses a constant amount of space.

5. **`__str__()`**:
   - **Space Complexity**: O(n)
   - **Explanation**: This method stores the string representation of each element in the queue, which requires space proportional to the number of elements `n`.

### Summary

- **Time Complexity**:
  - `is_empty()`, `enqueue()`, `dequeue()`, and `peek()` are all O(1).
  - `__str__()` is O(n).

- **Space Complexity**:
  - `is_empty()`, `enqueue()`, `dequeue()`, and `peek()` are all O(1).
  - `__str__()` is O(n).

This implementation of a queue using a linked list is efficient for most operations, with constant time complexity for adding and removing elements, and linear time complexity for generating a string representation of the queue.
