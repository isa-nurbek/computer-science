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

"""
Output:

Queue: [10, 20, 30]
Dequeue: 10
Peek: 20
Is empty? False
Size: 2
Queue after operations: [20, 30]

"""

# Big O:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

1. **`enqueue(item)`**:
   - **Time Complexity**: O(1)
   - **Explanation**: Appending an element to the end of a list in Python is an amortized constant-time operation.
   This is because Python lists are dynamically resized arrays, and while occasional resizing may occur, the
   average time complexity remains O(1).

2. **`dequeue()`**:
   - **Time Complexity**: O(n)
   - **Explanation**: Removing the first element of a list (`pop(0)`) requires shifting all remaining elements
   one position to the left. This operation takes linear time relative to the number of elements in the list.

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
   - **Explanation**: Converting the list to a string involves iterating over all elements in the list,
   which takes linear time.

---

### Space Complexity Analysis

1. **Overall Space Complexity**: O(n)
   - **Explanation**: The space complexity is determined by the number of elements stored in the queue.
   The `self.queue` list stores all the elements, so the space required grows linearly
   with the number of elements in the queue.

"""

# ********************************************************************************************************************* #


# Code Explanation:
