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

### Purpose

The `Node` class represents a single element in the linked list, containing:

1. **A value (`value`)**: The data the node holds.
2. **A reference to the next node (`next_node`)**: A pointer to the next `Node` in the list.

### Key Methods

1. **`__init__(value, next_node=None)`**: Constructor to initialize a node with a given value and an optional reference to the next node.
2. **`get_value()`**: Returns the value stored in the node.
3. **`get_next_node()`**: Returns the reference to the next node.
4. **`set_next_node(next_node)`**: Updates the reference to point to another node.
5. **`__str__()`**: Returns a string representation of the node (`Node(value)`).

---

## **Understanding the `Node` Class**

A **node** is a building block of a **linked list**. Each node stores:

1. **A value** (the actual data).
2. **A reference (pointer) to the next node** in the list.

```python
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
```

- `value`: Stores the actual data.
- `next_node`: Points to the next node in the list (default is `None`).

### **Methods in the `Node` Class**

#### 1️⃣ `get_value(self)`

```python
def get_value(self):
    return self.value
```

- Returns the **value** stored in the node.

#### 2️⃣ `get_next_node(self)`

```python
def get_next_node(self):
    return self.next_node
```

- Returns the **reference** (pointer) to the next node.

#### 3️⃣ `set_next_node(self, next_node)`

```python
def set_next_node(self, next_node):
    self.next_node = next_node
```

- Updates the `next_node` reference, linking this node to another node.

#### 4️⃣ `__str__(self)`

```python
def __str__(self):
    return f"Node({self.value})"
```

- Returns a string representation of the node for easy debugging.

---

## **Linked List Class**

---

```python
class LinkedList:
    def __init__(self, value=None):
        # Initialize the linked list with a head node if a value is provided
        self.head_node = Node(value) if value is not None else None

    def get_head_node(self):
        # Return the head node of the linked list
        return self.head_node

    def insert_beginning(self, new_value):
        # Insert a new node at the beginning of the linked list
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_end(self, value):
        # Insert a new node at the end of the linked list
        new_node = Node(value)
        if self.head_node is None:
            # If the list is empty, set the new node as the head node
            self.head_node = new_node
            return

        # Traverse to the end of the list
        current_node = self.head_node
        while current_node.get_next_node():
            current_node = current_node.get_next_node()
        # Set the new node as the next node of the last node
        current_node.set_next_node(new_node)

    def remove_node(self, value_to_remove):
        # Remove the first node with the specified value
        current_node = self.head_node

        if current_node and current_node.get_value() == value_to_remove:
            # If the head node is the one to be removed, update the head node
            self.head_node = current_node.get_next_node()
            return

        # Traverse the list to find the node to remove
        while current_node and current_node.get_next_node():
            next_node = current_node.get_next_node()
            if next_node.get_value() == value_to_remove:
                # Skip the node to remove by updating the next node reference
                current_node.set_next_node(next_node.get_next_node())
                return
            current_node = next_node

    def stringify_list(self):
        # Return a string representation of the linked list
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + " -> "
            current_node = current_node.get_next_node()
        return string_list[:-4] if string_list else "Empty List"

    def search(self, value):
        # Search for a node with the specified value
        current_node = self.head_node
        while current_node:
            if current_node.get_value() == value:
                return True
            current_node = current_node.get_next_node()
        return False

    def reverse(self):
        # Reverse the linked list
        prev = None
        current = self.head_node
        while current:
            next_node = current.get_next_node()
            current.set_next_node(prev)
            prev = current
            current = next_node
        # Update the head node to the new first node
        self.head_node = prev

    def find_middle(self):
        # Find the middle node of the linked list using the two-pointer technique
        slow = self.head_node
        fast = self.head_node
        while fast and fast.get_next_node():
            slow = slow.get_next_node()
            fast = fast.get_next_node().get_next_node()
        return slow.get_value() if slow else None

    def has_cycle(self):
        # Check if the linked list has a cycle using the two-pointer technique
        slow = self.head_node
        fast = self.head_node
        while fast and fast.get_next_node():
            slow = slow.get_next_node()
            fast = fast.get_next_node().get_next_node()
            if slow == fast:
                return True
        return False

    def find_cycle_start(self):
        # Find the starting node of a cycle in the linked list
        slow = self.head_node
        fast = self.head_node
        cycle_detected = False

        # Detect if there is a cycle
        while fast and fast.get_next_node():
            slow = slow.get_next_node()
            fast = fast.get_next_node().get_next_node()
            if slow == fast:
                cycle_detected = True
                break

        if not cycle_detected:
            return None

        # Find the start of the cycle
        slow = self.head_node
        while slow != fast:
            slow = slow.get_next_node()
            fast = fast.get_next_node()

        return slow.get_value()

    def remove_duplicates(self):
        # Remove duplicate values from the linked list
        if not self.head_node:
            return

        # Use a set to keep track of seen values
        seen_values = set()
        current_node = self.head_node
        seen_values.add(current_node.get_value())

        while current_node.get_next_node():
            next_node = current_node.get_next_node()
            if next_node.get_value() in seen_values:
                # Remove the duplicate node
                current_node.set_next_node(next_node.get_next_node())
            else:
                # Add the new value to the set and move to the next node
                seen_values.add(next_node.get_value())
                current_node = next_node


# Example Usage

ll = LinkedList()

ll.insert_end(1)
ll.insert_end(2)
ll.insert_end(3)
ll.insert_end(4)
ll.insert_end(5)

print("Original List:")
print(ll.stringify_list())  # Output: 1 -> 2 -> 3 -> 4 -> 5

# Test Searching
print("\nSearch for 3:", ll.search(3))  # Output: True
print("Search for 10:", ll.search(10))  # Output: False

# Test Finding Middle Node
print("\nMiddle Node:", ll.find_middle())  # Output: 3

# Test Reversing
ll.reverse()
print("\nReversed List:")
print(ll.stringify_list())  # Output: 5 -> 4 -> 3 -> 2 -> 1

# Test Cycle Detection
print("\nCycle Detected:", ll.has_cycle())  # Output: False

# Creating a cycle manually
ll.get_head_node().get_next_node().get_next_node().set_next_node(
    ll.get_head_node()
)  # Cycle at node 1
print("Cycle Detected after introducing cycle:", ll.has_cycle())  # Output: True
print("Cycle Start Node:", ll.find_cycle_start())  # Output: 1

# Remove cycle for further testing
ll.get_head_node().get_next_node().get_next_node().set_next_node(None)

# Test Removing Duplicates
ll.insert_end(3)
ll.insert_end(4)
ll.insert_end(4)
print("\nList before removing duplicates:")
print(ll.stringify_list())  # Output: 5 -> 4 -> 3 -> 2 -> 1 -> 3 -> 4 -> 4

ll.remove_duplicates()
print("\nList after removing duplicates:")
print(ll.stringify_list())  # Output: 5 -> 4 -> 3 -> 2 -> 1

```

---

## **Understanding the `LinkedList` Class**

A **linked list** is a sequence of nodes where:

- Each node stores a value and a reference to the next node.
- The list starts at a special node called the **head**.

```python
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value) if value is not None else None
```

- If a value is given, the list starts with a **head node**.
- Otherwise, the list is **empty**.

---

### **Methods in the `LinkedList` Class**

### 1️⃣ `get_head_node(self)`

```python
def get_head_node(self):
    return self.head_node
```

- Returns the **head node** (first node) of the list.

---

### 2️⃣ `insert_beginning(self, new_value)`

```python
def insert_beginning(self, new_value):
    new_node = Node(new_value)  # Create a new node
    new_node.set_next_node(self.head_node)  # Point new node to current head
    self.head_node = new_node  # Update head to new node
```

**How it works:**

- Creates a new node with `new_value`.
- Links it to the **current head node**.
- Updates the head to the new node.

**Example:**

```python
ll = LinkedList()
ll.insert_beginning(3)  # List: 3
ll.insert_beginning(2)  # List: 2 -> 3
ll.insert_beginning(1)  # List: 1 -> 2 -> 3
```

---

### 3️⃣ `insert_end(self, value)`

```python
def insert_end(self, value):
    new_node = Node(value)
    if self.head_node is None:  # If list is empty
        self.head_node = new_node
        return

    current_node = self.head_node
    while current_node.get_next_node():  # Traverse to last node
        current_node = current_node.get_next_node()
    current_node.set_next_node(new_node)  # Add new node at end
```

**How it works:**

- If the list is **empty**, set `head_node` to the new node.
- Otherwise, traverse to the **last node** and attach the new node.

**Example:**

```python
ll = LinkedList()
ll.insert_end(1)  # List: 1
ll.insert_end(2)  # List: 1 -> 2
ll.insert_end(3)  # List: 1 -> 2 -> 3
```

---

### 4️⃣ `remove_node(self, value_to_remove)`

```python
def remove_node(self, value_to_remove):
    current_node = self.head_node

    if current_node and current_node.get_value() == value_to_remove:
        self.head_node = current_node.get_next_node()
        return

    while current_node and current_node.get_next_node():
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
            current_node.set_next_node(next_node.get_next_node())  # Skip node
            return
        current_node = next_node
```

**How it works:**

- If the **head node** contains `value_to_remove`, update the head.
- Otherwise, traverse the list and **skip the node** to remove it.

**Example:**

```python
ll = LinkedList()
ll.insert_end(1)
ll.insert_end(2)
ll.insert_end(3)
ll.remove_node(2)  # List: 1 -> 3
```

---

### 5️⃣ `stringify_list(self)`

```python
def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
        string_list += str(current_node.get_value()) + " -> "
        current_node = current_node.get_next_node()
    return string_list[:-4] if string_list else "Empty List"
```

**How it works:**

- Converts the linked list into a **string representation**.

---

### 6️⃣ `search(self, value)`

```python
def search(self, value):
    current_node = self.head_node
    while current_node:
        if current_node.get_value() == value:
            return True
        current_node = current_node.get_next_node()
    return False
```

- Returns `True` if the value exists, `False` otherwise.

---

### 7️⃣ `reverse(self)`

```python
def reverse(self):
    prev = None
    current = self.head_node
    while current:
        next_node = current.get_next_node()
        current.set_next_node(prev)  # Reverse link
        prev = current
        current = next_node
    self.head_node = prev
```

- Reverses the linked list **in place**.

**Example:**

```python
ll.reverse()  # List: 3 -> 2 -> 1  (Reversed)
```

---

### 8️⃣ `find_middle(self)`

```python
def find_middle(self):
    slow = self.head_node
    fast = self.head_node
    while fast and fast.get_next_node():
        slow = slow.get_next_node()
        fast = fast.get_next_node().get_next_node()
    return slow.get_value() if slow else None
```

- Uses **two pointers** to find the middle node.

---

### 9️⃣ `has_cycle(self)`

```python
def has_cycle(self):
    slow = self.head_node
    fast = self.head_node
    while fast and fast.get_next_node():
        slow = slow.get_next_node()
        fast = fast.get_next_node().get_next_node()
        if slow == fast:
            return True
    return False
```

- Detects **if a cycle exists** in the linked list.

---

### 🔟 `find_cycle_start(self)`

```python
def find_cycle_start(self):
    slow = self.head_node
    fast = self.head_node
    cycle_detected = False

    while fast and fast.get_next_node():
        slow = slow.get_next_node()
        fast = fast.get_next_node().get_next_node()
        if slow == fast:
            cycle_detected = True
            break

    if not cycle_detected:
        return None

    slow = self.head_node
    while slow != fast:
        slow = slow.get_next_node()
        fast = fast.get_next_node()

    return slow.get_value()
```

- **Finds where the cycle begins**.

---

### 🔟 `remove_duplicates(self)`

```python
def remove_duplicates(self):
    if not self.head_node:
        return

    seen_values = set()
    current_node = self.head_node
    seen_values.add(current_node.get_value())

    while current_node.get_next_node():
        next_node = current_node.get_next_node()
        if next_node.get_value() in seen_values:
            current_node.set_next_node(next_node.get_next_node())  # Remove duplicate
        else:
            seen_values.add(next_node.get_value())
            current_node = next_node
```

- Uses a **set** to remove duplicate values.

### Conclusion

This linked list supports many useful operations and provides a full set of operations for common tasks.

---

## **Big O Analysis:**

### Time and Space Complexity Analysis

Let's analyze the time and space complexity of each method in the `LinkedList` class.

---

#### 1. **`__init__`**

- **Time Complexity**: \(O(1)\)
- **Space Complexity**: \(O(1)\)
- Explanation: Initializing the `head_node` is a constant-time operation.

---

#### 2. **`get_head_node`**

- **Time Complexity**: \(O(1)\)
- **Space Complexity**: \(O(1)\)
- Explanation: Simply returns the `head_node`, which is a constant-time operation.

---

#### 3. **`insert_beginning`**

- **Time Complexity**: \(O(1)\)
- **Space Complexity**: \(O(1)\)
- Explanation: Inserting a new node at the beginning involves creating a new node and updating the `head_node`, which is a constant-time operation.

---

#### 4. **`insert_end`**

- **Time Complexity**: \(O(n)\)
- **Space Complexity**: \(O(1)\)
- Explanation: In the worst case, you need to traverse the entire list to find the last node, which takes \(O(n)\) time. The space complexity is constant because only a fixed number of variables are used.

---

#### 5. **`remove_node`**

- **Time Complexity**: \(O(n)\)
- **Space Complexity**: \(O(1)\)
- Explanation: In the worst case, you need to traverse the entire list to find the node to remove, which takes \(O(n)\) time. The space complexity is constant because no additional data structures are used.

---

#### 6. **`stringify_list`**

- **Time Complexity**: \(O(n)\)
- **Space Complexity**: \(O(n)\)
- Explanation: You need to traverse the entire list to build the string representation, which takes \(O(n)\) time. The space complexity is \(O(n)\) because the string grows linearly with the number of nodes.

---

#### 7. **`search`**

- **Time Complexity**: \(O(n)\)
- **Space Complexity**: \(O(1)\)
- Explanation: In the worst case, you need to traverse the entire list to find the value, which takes \(O(n)\) time. The space complexity is constant because no additional data structures are used.

---

#### 8. **`reverse`**

- **Time Complexity**: \(O(n)\)
- **Space Complexity**: \(O(1)\)
- Explanation: Reversing the list requires traversing the entire list once, which takes \(O(n)\) time. The space complexity is constant because only a fixed number of variables are used.

---

#### 9. **`find_middle`**

- **Time Complexity**: \(O(n)\)
- **Space Complexity**: \(O(1)\)
- Explanation: The "two-pointer" technique (slow and fast pointers) traverses the list in \(O(n)\) time. The space complexity is constant because only two pointers are used.

---

#### 10. **`has_cycle`**

- **Time Complexity**: \(O(n)\)
- **Space Complexity**: \(O(1)\)
- Explanation: The "two-pointer" technique (slow and fast pointers) traverses the list in \(O(n)\) time. The space complexity is constant because only two pointers are used.

---

#### 11. **`find_cycle_start`**

- **Time Complexity**: \(O(n)\)
- **Space Complexity**: \(O(1)\)
- Explanation: Detecting the cycle and finding its start involves traversing the list with two pointers, which takes \(O(n)\) time. The space complexity is constant because only a fixed number of variables are used.

---

#### 12. **`remove_duplicates`**

- **Time Complexity**: \(O(n)\)
- **Space Complexity**: \(O(n)\)
- Explanation: Traversing the list takes \(O(n)\) time. The space complexity is \(O(n)\) because a set is used to store seen values, which can grow up to the size of the list in the worst case (if all values are unique).

---

### Summary Table

| Method               | Time Complexity | Space Complexity |
|----------------------|-----------------|------------------|
| `__init__`           | \(O(1)\)        | \(O(1)\)         |
| `get_head_node`      | \(O(1)\)        | \(O(1)\)         |
| `insert_beginning`   | \(O(1)\)        | \(O(1)\)         |
| `insert_end`         | \(O(n)\)        | \(O(1)\)         |
| `remove_node`        | \(O(n)\)        | \(O(1)\)         |
| `stringify_list`     | \(O(n)\)        | \(O(n)\)         |
| `search`             | \(O(n)\)        | \(O(1)\)         |
| `reverse`            | \(O(n)\)        | \(O(1)\)         |
| `find_middle`        | \(O(n)\)        | \(O(1)\)         |
| `has_cycle`          | \(O(n)\)        | \(O(1)\)         |
| `find_cycle_start`   | \(O(n)\)        | \(O(1)\)         |
| `remove_duplicates`  | \(O(n)\)        | \(O(n)\)         |

---

### Key Takeaways

- Most operations that involve traversing the list (e.g., `insert_end`, `remove_node`, `search`, `reverse`, etc.) have a **time complexity of \(O(n)\)**.
- Operations that modify the head of the list (e.g., `insert_beginning`) have a **time complexity of \(O(1)\)**.
- The **space complexity** is generally \(O(1)\) for most operations, except for `stringify_list` and `remove_duplicates`, which use additional space proportional to the size of the list.
