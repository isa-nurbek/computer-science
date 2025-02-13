# Code Explanation: Doubly Linked List Implementation in Python

---

## **Understanding the Classes**

### **1. `Node` Class**

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

## Let's analyze the **time and space complexity** of the **DoublyLinkedList** operations

### **1. `add_to_head(new_value)` & `add_to_tail(new_value)`**

- These operations create a new node and adjust a few pointers.
- **Time Complexity:** \( O(1) \) (Constant time, as only a few pointer changes are required)
- **Space Complexity:** \( O(1) \) (No extra space except for the new node)

---

### **2. `insert(pos, new_value)`**

- If inserting at the head: \( O(1) \).
- If inserting at an arbitrary position:
  - In the worst case, we traverse \( O(n) \) elements.
  - The insertion itself (pointer adjustments) takes \( O(1) \).
- **Time Complexity:** \( O(n) \) (Worst case: inserting at the end)
- **Space Complexity:** \( O(1) \) (Only a new node is added)

---

### **3. `remove_head()` & `remove_tail()`**

- These operations adjust a few pointers and return a value.
- **Time Complexity:** \( O(1) \) (No traversal required)
- **Space Complexity:** \( O(1) \) (No extra space used)

---

### **4. `remove_by_value(value_to_remove)`**

- In the worst case, we traverse the entire list if the value is at the end or not present.
- Removing the node itself takes \( O(1) \) (pointer changes).
- **Time Complexity:** \( O(n) \) (Worst case: searching the entire list)
- **Space Complexity:** \( O(1) \) (No extra space used)

---

### **5. `stringify_list()`**

- Traverses the entire list and builds a string.
- **Time Complexity:** \( O(n) \) (Iterating through all elements)
- **Space Complexity:** \( O(n) \) (Storing the output string)

---

### **Overall Summary**

| Operation           | Time Complexity | Space Complexity |
|---------------------|----------------|-----------------|
| `add_to_head()` / `add_to_tail()` | \( O(1) \) | \( O(1) \) |
| `insert(pos, value)` | \( O(n) \) (worst case) | \( O(1) \) |
| `remove_head()` / `remove_tail()` | \( O(1) \) | \( O(1) \) |
| `remove_by_value(value)` | \( O(n) \) (worst case) | \( O(1) \) |
| `stringify_list()` | \( O(n) \) | \( O(n) \) |

The **space complexity remains \( O(1) \) for most operations** since we do not allocate extra memory apart from the new nodes themselves.

---

## **Key Takeaways**

- **Doubly Linked Lists** allow **bidirectional traversal** (both forward & backward).
- **Head & Tail pointers** help efficient insertion and deletion.
- **Each node links to both next and previous nodes**, unlike singly linked lists.
- **Dynamic operations** like insertion, deletion, and searching are handled efficiently.
