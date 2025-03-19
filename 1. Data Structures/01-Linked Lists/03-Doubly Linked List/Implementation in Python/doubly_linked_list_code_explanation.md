# Code Explanation: Doubly Linked List Implementation in Python

---

## **Understanding the Classes**

### **1. `Node` Class**

```python
class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value  # Store node value
        self.next_node = next_node  # Pointer to next node
        self.prev_node = prev_node  # Pointer to previous node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value
```

Each node in a doubly linked list has:

- A **value** to store data.
- A **pointer to the next node** (`next_node`).
- A **pointer to the previous node** (`prev_node`).

#### **Methods in `Node` Class**

| Method | Description |
|--------|------------|
| `__init__(self, value, next_node=None, prev_node=None)` | Constructor initializes the node with a value, and optional next and previous references. |
| `set_next_node(self, next_node)` | Sets the next node reference. |
| `get_next_node(self)` | Returns the next node reference. |
| `set_prev_node(self, prev_node)` | Sets the previous node reference. |
| `get_prev_node(self)` | Returns the previous node reference. |
| `get_value(self)` | Returns the value stored in the node. |

---

### **2. `DoublyLinkedList` Class**

```python
class DoublyLinkedList:
    def __init__(self):
        self.head_node = None  # Reference to head node
        self.tail_node = None  # Reference to tail node

    def add_to_head(self, new_value):
        new_head = Node(new_value)  # Create a new node
        current_head = self.head_node  # Get current head

        if current_head is not None:
            current_head.set_prev_node(new_head)  # Link old head to new head
            new_head.set_next_node(current_head)  # Link new head to old head

        self.head_node = new_head  # Update head reference

        if self.tail_node is None:  # If list was empty, set tail as well
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)  # Create a new node
        current_tail = self.tail_node  # Get current tail

        if current_tail is not None:
            current_tail.set_next_node(new_tail)  # Link old tail to new tail
            new_tail.set_prev_node(current_tail)  # Link new tail to old tail

        self.tail_node = new_tail  # Update tail reference

        if self.head_node is None:  # If list was empty, set head as well
            self.head_node = new_tail

    def insert(self, pos, new_value):
        if pos == 0:  # Insert at head if position is 0
            self.add_to_head(new_value)
        else:
            current_node = self.head_node
            for i in range(pos - 1):
                if current_node is None or current_node.get_next_node() is None:
                    self.add_to_tail(new_value)
                    return
                current_node = current_node.get_next_node()

            new_node = Node(new_value)
            new_node.set_next_node(current_node.get_next_node())
            new_node.set_prev_node(current_node)

            if current_node.get_next_node() is not None:
                current_node.get_next_node().set_prev_node(new_node)

            current_node.set_next_node(new_node)

            if new_node.get_next_node() is None:  # If inserted at end, update tail
                self.tail_node = new_node

    def remove_head(self):
        removed_head = self.head_node

        if removed_head is None:  # If list is empty
            return None

        self.head_node = removed_head.get_next_node()  # Update head

        if self.head_node is not None:
            self.head_node.set_prev_node(None)  # Remove backward link
        else:
            self.tail_node = None  # If list is empty after removal, update tail

        return removed_head.get_value()

    def remove_tail(self):
        removed_tail = self.tail_node

        if removed_tail is None:  # If list is empty
            return None

        self.tail_node = removed_tail.get_prev_node()  # Update tail

        if self.tail_node is not None:
            self.tail_node.set_next_node(None)  # Remove forward link
        else:
            self.head_node = None  # If list is empty after removal, update head

        return removed_tail.get_value()

    def remove_by_value(self, value_to_remove):
        current_node = self.head_node

        while current_node is not None:  # Traverse the list
            if current_node.get_value() == value_to_remove:
                if current_node == self.head_node:  # If it's the head
                    return self.remove_head()
                elif current_node == self.tail_node:  # If it's the tail
                    return self.remove_tail()
                else:  # Middle of the list
                    prev_node = current_node.get_prev_node()
                    next_node = current_node.get_next_node()

                    if prev_node:
                        prev_node.set_next_node(next_node)

                    if next_node:
                        next_node.set_prev_node(prev_node)

                    return value_to_remove  # Return removed value

            current_node = current_node.get_next_node()

        return None  # If value not found

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node

        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"

            current_node = current_node.get_next_node()

        return string_list
```

This class manages the **doubly linked list** structure. It maintains:

- A **head pointer** (`self.head_node`) pointing to the first node.
- A **tail pointer** (`self.tail_node`) pointing to the last node.

#### **Methods in `DoublyLinkedList` Class**

| Method | Description |
|--------|------------|
| `__init__(self)` | Initializes an empty doubly linked list. |
| `add_to_head(self, new_value)` | Adds a new node at the head (beginning) of the list. |
| `add_to_tail(self, new_value)` | Adds a new node at the tail (end) of the list. |
| `insert(self, pos, new_value)` | Inserts a node at a specified position in the list. |
| `remove_head(self)` | Removes the head node and returns its value. |
| `remove_tail(self)` | Removes the tail node and returns its value. |
| `remove_by_value(self, value_to_remove)` | Removes a node containing a specific value. |
| `stringify_list(self)` | Converts the list into a string format for easy printing. |

---

## **Breaking Down the Methods in Detail**

### **1. `add_to_head(self, new_value)`**

- Creates a new node.
- If the list is not empty:
  - Links the new node to the current head.
  - Updates the previous pointer of the current head.
- Updates the head pointer.
- If the list was empty, updates the tail pointer.

#### **Example**

```python
dll = DoublyLinkedList()
dll.add_to_head(5)
dll.add_to_head(1)  
# List: 1 <-> 5
```

---

### **2. `add_to_tail(self, new_value)`**

- Creates a new node.
- If the list is not empty:
  - Links the new node to the current tail.
  - Updates the next pointer of the current tail.
- Updates the tail pointer.
- If the list was empty, updates the head pointer.

#### **Example**

```python
dll.add_to_tail(10)  
dll.add_to_tail(15)  
# List: 1 <-> 5 <-> 10 <-> 15
```

---

### **3. `insert(self, pos, new_value)`**

- If `pos == 0`, insert at the head.
- Otherwise, traverse to the position.
- If position is beyond the list length, add to tail.
- Otherwise, insert the node between two existing nodes.

#### **Example**

```python
dll.insert(2, 7)
# List: 1 <-> 5 <-> 7 <-> 10 <-> 15
```

---

### **4. `remove_head(self)`**

- If the list is empty, return `None`.
- Otherwise:
  - Update the head to the next node.
  - Remove backward reference.
  - If list becomes empty, update tail as `None`.

#### **Example**

```python
dll.remove_head()
# Removes 1
# List: 5 <-> 7 <-> 10 <-> 15
```

---

### **5. `remove_tail(self)`**

- If the list is empty, return `None`.
- Otherwise:
  - Update the tail to the previous node.
  - Remove forward reference.
  - If list becomes empty, update head as `None`.

#### **Example**

```python
dll.remove_tail()
# Removes 15
# List: 5 <-> 7 <-> 10
```

---

### **6. `remove_by_value(self, value_to_remove)`**

- Traverses the list to find the node.
- If found:
  - If it's the head or tail, call `remove_head()` or `remove_tail()`.
  - Otherwise, update links to remove the node.
- If not found, return `None`.

#### **Example**

```python
dll.remove_by_value(7)
# Removes 7
# List: 5 <-> 10
```

---

### **7. `stringify_list(self)`**

- Traverses the list, appending node values to a string.

#### **Example**

```python
print(dll.stringify_list())
# Output:
# 5
# 10
```

---

## **Full Execution Walkthrough**

```python
dll = DoublyLinkedList()
dll.add_to_head(5)   # List: 5
dll.add_to_tail(10)  # List: 5 <-> 10
dll.add_to_tail(15)  # List: 5 <-> 10 <-> 15
dll.add_to_head(1)   # List: 1 <-> 5 <-> 10 <-> 15

dll.insert(2, 7)     # List: 1 <-> 5 <-> 7 <-> 10 <-> 15

dll.remove_head()    # List: 5 <-> 7 <-> 10 <-> 15
dll.remove_tail()    # List: 5 <-> 7 <-> 10
dll.remove_by_value(7)  # List: 5 <-> 10

print(dll.stringify_list())  
# Output:
# 5
# 10
```

---

## **Big O Analysis:**

### Time and Space Complexity Analysis

Below is the time and space complexity analysis for each method in the `DoublyLinkedList` class:

---

#### **Node Class**

- **Time Complexity**: All operations in the `Node` class (e.g., `get_next_node`, `set_next_node`, etc.) are **O(1)** because they involve simple pointer assignments or retrievals.
- **Space Complexity**: The `Node` class uses **O(1)** space per node, as it only stores the value and pointers to the next and previous nodes.

---

#### **DoublyLinkedList Class**

1. **`add_to_head(new_value)`**
   - **Time Complexity**: **O(1)**  
     - Creating a new node and updating pointers (head and previous head) are constant-time operations.
   - **Space Complexity**: **O(1)**  
     - Only a single new node is created, and no additional space is used.

2. **`add_to_tail(new_value)`**
   - **Time Complexity**: **O(1)**  
     - Similar to `add_to_head`, creating a new node and updating pointers (tail and previous tail) are constant-time operations.
   - **Space Complexity**: **O(1)**  
     - Only a single new node is created, and no additional space is used.

3. **`insert(pos, new_value)`**
   - **Time Complexity**: **O(n)** in the worst case, where `n` is the length of the list.  
     - In the worst case, you may need to traverse the entire list to find the insertion position.
   - **Space Complexity**: **O(1)**  
     - Only a single new node is created, and no additional space is used.

4. **`remove_head()`**
   - **Time Complexity**: **O(1)**  
     - Updating the head pointer and removing the backward link are constant-time operations.
   - **Space Complexity**: **O(1)**  
     - No additional space is used.

5. **`remove_tail()`**
   - **Time Complexity**: **O(1)**  
     - Updating the tail pointer and removing the forward link are constant-time operations.
   - **Space Complexity**: **O(1)**  
     - No additional space is used.

6. **`remove_by_value(value_to_remove)`**
   - **Time Complexity**: **O(n)** in the worst case, where `n` is the length of the list.  
     - In the worst case, you may need to traverse the entire list to find the node with the specified value.
   - **Space Complexity**: **O(1)**  
     - No additional space is used.

7. **`stringify_list()`**
   - **Time Complexity**: **O(n)**, where `n` is the length of the list.  
     - You need to traverse the entire list to construct the string representation.
   - **Space Complexity**: **O(n)**  
     - The string representation of the list requires space proportional to the number of nodes.

---

#### **Overall Summary**

- **Time Complexity**:
  - Most operations (e.g., `add_to_head`, `add_to_tail`, `remove_head`, `remove_tail`) are **O(1)**.
  - Operations that involve traversal (e.g., `insert`, `remove_by_value`, `stringify_list`) are **O(n)**.
- **Space Complexity**:
  - All operations use **O(1)** additional space, except for `stringify_list`, which uses **O(n)** space to store the string representation.

---

#### **Additional Notes**

- The doubly linked list allows for efficient insertion and deletion at both ends (head and tail) due to the presence of both `next` and `prev` pointers.
- Traversal-based operations (e.g., `insert`, `remove_by_value`) are less efficient than in arrays or array-based lists because they require sequential access.
- The space overhead of a doubly linked list is higher than that of a singly linked list due to the additional `prev` pointer in each node.

---

## **Key Takeaways**

- **Doubly Linked Lists** allow **bidirectional traversal** (both forward & backward).
- **Head & Tail pointers** help efficient insertion and deletion.
- **Each node links to both next and previous nodes**, unlike singly linked lists.
- **Dynamic operations** like insertion, deletion, and searching are handled efficiently.
