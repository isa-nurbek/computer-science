# Implementation in Python:


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


# Create a new doubly linked list
dll = DoublyLinkedList()

# Add elements to the list
dll.add_to_head(5)
dll.add_to_tail(10)
dll.add_to_tail(15)
dll.add_to_head(1)

# Print the list
print("Doubly Linked List:")
print(dll.stringify_list())

# Insert an element at position 2
dll.insert(2, 7)
print("After inserting 7 at position 2:")
print(dll.stringify_list())

# Remove the head
dll.remove_head()
print("After removing head:")
print(dll.stringify_list())

# Remove the tail
dll.remove_tail()
print("After removing tail:")
print(dll.stringify_list())

# Remove an element by value (e.g., 7)
dll.remove_by_value(7)
print("After removing value 7:")
print(dll.stringify_list())


"""
Output:

Doubly Linked List:
1
5
10
15

After inserting 7 at position 2:
1
5
7
10
15

After removing head:
5
7
10
15

After removing tail:
5
7
10

After removing value 7:
5
10

"""

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the **time and space complexity** of the methods in the `DoublyLinkedList` class.

---

### **Time Complexity**

1. **`add_to_head(new_value)`**:
   - **Time Complexity**: **O(1)**
   
   - Explanation: Adding a node to the head involves creating a new node and updating a few pointers.
   This is a constant-time operation.

2. **`add_to_tail(new_value)`**:
   - **Time Complexity**: **O(1)**
   
   - Explanation: Adding a node to the tail also involves creating a new node and updating a few pointers.
   This is a constant-time operation.

3. **`insert(pos, new_value)`**:
   - **Time Complexity**: **O(n)**
   
   - Explanation: In the worst case, inserting at position `pos` requires traversing the list up to `pos` nodes.
   This makes it linear in the worst case.

4. **`remove_head()`**:
   - **Time Complexity**: **O(1)**
   
   - Explanation: Removing the head involves updating a few pointers. This is a constant-time operation.

5. **`remove_tail()`**:
   - **Time Complexity**: **O(1)**
   
   - Explanation: Removing the tail involves updating a few pointers. This is a constant-time operation.

6. **`remove_by_value(value_to_remove)`**:
   - **Time Complexity**: **O(n)**
   
   - Explanation: In the worst case, the value to remove could be at the tail or not present in the list,
   requiring traversal of the entire list.

7. **`stringify_list()`**:
   - **Time Complexity**: **O(n)**
   
   - Explanation: This method traverses the entire list to create a string representation, so it is linear in time.

---

### **Space Complexity**

1. **`add_to_head(new_value)`**:
   - **Space Complexity**: **O(1)**
   
   - Explanation: Only a constant amount of additional space is used for the new node.

2. **`add_to_tail(new_value)`**:
   - **Space Complexity**: **O(1)**
   
   - Explanation: Only a constant amount of additional space is used for the new node.

3. **`insert(pos, new_value)`**:
   - **Space Complexity**: **O(1)**
   
   - Explanation: Only a constant amount of additional space is used for the new node.

4. **`remove_head()`**:
   - **Space Complexity**: **O(1)**
   
   - Explanation: No additional space is used beyond a few pointers.

5. **`remove_tail()`**:
   - **Space Complexity**: **O(1)**
   
   - Explanation: No additional space is used beyond a few pointers.

6. **`remove_by_value(value_to_remove)`**:
   - **Space Complexity**: **O(1)**
   
   - Explanation: No additional space is used beyond a few pointers.

7. **`stringify_list()`**:
   - **Space Complexity**: **O(n)**
   
   - Explanation: The space required for the string representation grows linearly with the number of nodes in the list.

---

### **Summary**

| Method               | Time Complexity | Space Complexity |
|----------------------|-----------------|------------------|
| `add_to_head`        | O(1)            | O(1)             |
| `add_to_tail`        | O(1)            | O(1)             |
| `insert`             | O(n)            | O(1)             |
| `remove_head`        | O(1)            | O(1)             |
| `remove_tail`        | O(1)            | O(1)             |
| `remove_by_value`    | O(n)            | O(1)             |
| `stringify_list`     | O(n)            | O(n)             |

---

### **Key Observations**
- Most operations (e.g., `add_to_head`, `add_to_tail`, `remove_head`, `remove_tail`) are **O(1)** in both time and space.

- Traversal-based operations (e.g., `insert`, `remove_by_value`, `stringify_list`) are **O(n)** in time due to the
need to traverse the list.

- The space complexity is generally **O(1)** for most operations, except for `stringify_list`, which requires **O(n)**
space for the output string.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
                                            *** __init__() method: ***


Let's break down the `DoublyLinkedList` class and its initialization step by step to help you understand it better.

---

### **DoublyLinkedList Class**

The `DoublyLinkedList` class is a data structure that represents a **doubly linked list**. A doubly linked list is
a collection of nodes where each node contains:
1. A **value** (to store data).
2. A **pointer to the next node** (`next_node`).
3. A **pointer to the previous node** (`prev_node`).

Unlike a singly linked list, a doubly linked list allows traversal in both directions (forward and backward).

---

### **Initialization: `__init__(self)`**

```
def __init__(self):
    self.head_node = None  
    self.tail_node = None 
```

#### **What does this code do?**
1. **`self.head_node = None`**:
   - This initializes the `head_node` attribute of the `DoublyLinkedList` class to `None`.
   - The `head_node` is a reference to the **first node** in the list.
   - When the list is empty, there is no first node, so `head_node` is set to `None`.

2. **`self.tail_node = None`**:
   - This initializes the `tail_node` attribute of the `DoublyLinkedList` class to `None`.
   - The `tail_node` is a reference to the **last node** in the list.
   - When the list is empty, there is no last node, so `tail_node` is set to `None`.

---

### **Why are `head_node` and `tail_node` important?**
- **`head_node`**:
  - It allows us to access the **first element** of the list.
  - All operations that involve the beginning of the list (e.g., adding or removing the first element) use `head_node`.

- **`tail_node`**:
  - It allows us to access the **last element** of the list.
  - All operations that involve the end of the list (e.g., adding or removing the last element) use `tail_node`.

---

### **What happens when the list is empty?**
- When the list is empty:
  - Both `head_node` and `tail_node` are `None`.
  - This indicates that there are no nodes in the list.

---

### **What happens when nodes are added?**
- When the first node is added:
  - Both `head_node` and `tail_node` will point to this node (since it is the only node in the list).
- When more nodes are added:
  - The `head_node` and `tail_node` are updated accordingly to reflect the new first and last nodes.

---

### **Example**

Let's walk through an example to see how `head_node` and `tail_node` work.

#### **Step 1: Create an empty list**
```
dll = DoublyLinkedList()
```
- `head_node = None`
- `tail_node = None`

The list is empty.

---

#### **Step 2: Add the first node (value = 5)**
```
dll.add_to_head(5)
```
- A new node with `value = 5` is created.
- Since this is the first node:
  - `head_node` points to this node.
  - `tail_node` also points to this node.

The list now looks like this:
```
head_node -> [5] <- tail_node
```

---

#### **Step 3: Add a second node (value = 10) to the head**
```
dll.add_to_head(10)
```
- A new node with `value = 10` is created.
- This node becomes the new head, and its `next_node` points to the previous head (`5`).
- The previous head's (`5`) `prev_node` points to the new head (`10`).
- `head_node` is updated to point to the new node (`10`).
- `tail_node` remains pointing to the last node (`5`).

The list now looks like this:
```
head_node -> [10] <-> [5] <- tail_node
```

---

#### **Step 4: Add a third node (value = 15) to the tail**
```
dll.add_to_tail(15)
```
- A new node with `value = 15` is created.
- This node becomes the new tail, and its `prev_node` points to the previous tail (`5`).
- The previous tail's (`5`) `next_node` points to the new tail (`15`).
- `tail_node` is updated to point to the new node (`15`).
- `head_node` remains pointing to the first node (`10`).

The list now looks like this:
```
head_node -> [10] <-> [5] <-> [15] <- tail_node
```

---

### **Summary**
- **`head_node`**:
  - Always points to the **first node** in the list.
  - Used for operations at the beginning of the list (e.g., `add_to_head`, `remove_head`).

- **`tail_node`**:
  - Always points to the **last node** in the list.
  - Used for operations at the end of the list (e.g., `add_to_tail`, `remove_tail`).

- When the list is empty:
  - Both `head_node` and `tail_node` are `None`.

- When nodes are added:
  - `head_node` and `tail_node` are updated to reflect the new first and last nodes.

# =========================================================================================================================== #

                                        *** add_to_head() method: ***
                                               

Let's break down the `add_to_head` method step by step to help you understand how it works.

---

### **Purpose of `add_to_head`**
The `add_to_head` method adds a new node with the given `new_value` to the **beginning** of the doubly linked list.
This new node becomes the new **head** of the list.

---

### **Code Breakdown**

```
def add_to_head(self, new_value):
    new_head = Node(new_value)  
    current_head = self.head_node 
    if current_head is not None:
        current_head.set_prev_node(new_head)  
        new_head.set_next_node(current_head)  
    self.head_node = new_head  
    if self.tail_node is None: 
        self.tail_node = new_head
```

---

### **Step-by-Step Explanation**

#### **Step 1: Create a new node**
```
new_head = Node(new_value)
```
- A new node is created with the given `new_value`.
- This node will become the new head of the list.

---

#### **Step 2: Get the current head**
```
current_head = self.head_node
```
- `current_head` stores a reference to the current head of the list.
- If the list is empty, `current_head` will be `None`.

---

#### **Step 3: Link the old head to the new head**
```
if current_head is not None:
    current_head.set_prev_node(new_head)  # Link old head to new head
    new_head.set_next_node(current_head)  # Link new head to old head
```
- If the list is **not empty** (`current_head is not None`):
  1. **Link the old head to the new head**:
     - The `prev_node` of the old head (`current_head`) is set to point to the new head (`new_head`).
     - This establishes a backward link from the old head to the new head.
  2. **Link the new head to the old head**:
     - The `next_node` of the new head (`new_head`) is set to point to the old head (`current_head`).
     - This establishes a forward link from the new head to the old head.

---

#### **Step 4: Update the head reference**
```
self.head_node = new_head
```
- The `head_node` of the list is updated to point to the new head (`new_head`).
- Now, the new node is officially the first node in the list.

---

#### **Step 5: Update the tail reference (if the list was empty)**
```
if self.tail_node is None:
    self.tail_node = new_head
```
- If the list was **empty** before adding the new node (`self.tail_node is None`):
  - The `tail_node` is also updated to point to the new head (`new_head`).
  - This is because the new node is both the first and last node in the list.

---

### **Example Walkthrough**

Let's walk through an example to see how this works.

#### **Initial State**
- The list is empty:
  - `head_node = None`
  - `tail_node = None`

---

#### **Step 1: Add `5` to the head**
```
dll.add_to_head(5)
```
1. A new node with `value = 5` is created:
   - `new_head = Node(5)`
2. `current_head = self.head_node = None` (list is empty).
3. Since `current_head is None`, the `if` block is skipped.
4. `self.head_node` is updated to point to the new node:
   - `head_node -> [5]`
5. Since `self.tail_node is None`, `self.tail_node` is also updated:
   - `tail_node -> [5]`

The list now looks like this:
```
head_node -> [5] <- tail_node
```

---

#### **Step 2: Add `10` to the head**
```
dll.add_to_head(10)
```
1. A new node with `value = 10` is created:
   - `new_head = Node(10)`
2. `current_head = self.head_node` (points to `[5]`).
3. Since `current_head is not None`:
   - `current_head.set_prev_node(new_head)`:
     - The `prev_node` of `[5]` is set to `[10]`.
   - `new_head.set_next_node(current_head)`:
     - The `next_node` of `[10]` is set to `[5]`.
4. `self.head_node` is updated to point to the new node:
   - `head_node -> [10]`
5. `self.tail_node` is not updated because the list is not empty.

The list now looks like this:
```
head_node -> [10] <-> [5] <- tail_node
```

---

### **Final State**
After adding `5` and `10` to the head, the list looks like this:
```
head_node -> [10] <-> [5] <- tail_node
```

---

### **Key Points**
1. **Adding to an empty list**:
   - The new node becomes both the `head_node` and the `tail_node`.

2. **Adding to a non-empty list**:
   - The new node becomes the `head_node`.
   - The old head's `prev_node` is updated to point to the new head.
   - The new head's `next_node` is updated to point to the old head.

3. **Why update `tail_node`?**
   - If the list was empty, the new node is both the first and last node, so `tail_node` must also be updated.

# =========================================================================================================================== #

                                            *** insert() method: ***
                                               
Let's break down the `insert` method step by step to help you understand how it works.

---

### **Purpose of `insert`**
The `insert` method adds a new node with the given `new_value` at a specific position (`pos`) in the doubly linked list.
If the position is `0`, it adds the node to the head. If the position is beyond the list's length, it adds the node to the tail.

---

### **Code Breakdown**

```
def insert(self, pos, new_value):
    if pos == 0:  
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
        if new_node.get_next_node() is None:
            self.tail_node = new_node
```

---

### **Step-by-Step Explanation**

#### **Step 1: Check if the position is 0**
```
if pos == 0:
    self.add_to_head(new_value)
```
- If the position (`pos`) is `0`, the new node should be inserted at the **head** of the list.
- The `add_to_head` method is called to handle this case.

---

#### **Step 2: Traverse to the correct position**
```
else:
    current_node = self.head_node
    for i in range(pos - 1):
        if current_node is None or current_node.get_next_node() is None:
            self.add_to_tail(new_value)
            return
        current_node = current_node.get_next_node()
```
- If the position is not `0`, we need to traverse the list to find the node **just before** the desired position.
- Start from the `head_node` and move forward `(pos - 1)` steps.
- If at any point:
  - `current_node` becomes `None` (end of the list is reached), or
  - `current_node.get_next_node()` is `None` (next node doesn't exist),
- It means the position is beyond the list's length. In this case, the new node is added to the **tail** using `add_to_tail`.

---

#### **Step 3: Create the new node**
```
new_node = Node(new_value)
```
- A new node is created with the given `new_value`.

---

#### **Step 4: Link the new node to its neighbors**
```
new_node.set_next_node(current_node.get_next_node())
new_node.set_prev_node(current_node)
```
- Set the `next_node` of the new node to the node that currently comes after `current_node`.
- Set the `prev_node` of the new node to `current_node`.

---

#### **Step 5: Update the previous node's `next_node`**
```
if current_node.get_next_node() is not None:
    current_node.get_next_node().set_prev_node(new_node)
```
- If the node after `current_node` exists:
  - Update its `prev_node` to point to the new node.

---

#### **Step 6: Update `current_node`'s `next_node`**
```
current_node.set_next_node(new_node)
```
- Set the `next_node` of `current_node` to the new node.

---

#### **Step 7: Update the tail if necessary**
```
if new_node.get_next_node() is None:
    self.tail_node = new_node
```
- If the new node's `next_node` is `None`, it means the new node is now the **last node** in the list.
- Update the `tail_node` to point to the new node.

---

### **Example Walkthrough**

Let's walk through an example to see how this works.

#### **Initial State**
- The list contains the following nodes:
  ```
  head_node -> [1] <-> [3] <- tail_node
  ```

---

#### **Step 1: Insert `2` at position 1**
```
dll.insert(1, 2)
```
1. Since `pos = 1` (not `0`), we start traversing from the `head_node` (`[1]`).
2. Move forward `(pos - 1) = 0` steps, so `current_node` remains `[1]`.
3. Create a new node with `value = 2`.
4. Link the new node:
   - `new_node.set_next_node(current_node.get_next_node())`:
     - `next_node` of `[2]` is set to `[3]`.
   - `new_node.set_prev_node(current_node)`:
     - `prev_node` of `[2]` is set to `[1]`.
5. Update the `next_node` of `[1]` to point to `[2]`.
6. Update the `prev_node` of `[3]` to point to `[2]`.
7. Since `new_node.get_next_node()` is `[3]` (not `None`), the `tail_node` is not updated.

The list now looks like this:
```
head_node -> [1] <-> [2] <-> [3] <- tail_node
```

---

#### **Step 2: Insert `4` at position 3**
```
dll.insert(3, 4)
```
1. Since `pos = 3` (not `0`), we start traversing from the `head_node` (`[1]`).
2. Move forward `(pos - 1) = 2` steps:
   - Step 1: `current_node = [1]` -> `current_node = [2]`.
   - Step 2: `current_node = [2]` -> `current_node = [3]`.
3. Create a new node with `value = 4`.
4. Link the new node:
   - `new_node.set_next_node(current_node.get_next_node())`:
     - `next_node` of `[4]` is set to `None` (since `[3]` is the tail).
   - `new_node.set_prev_node(current_node)`:
     - `prev_node` of `[4]` is set to `[3]`.
5. Update the `next_node` of `[3]` to point to `[4]`.
6. Since `new_node.get_next_node()` is `None`, update the `tail_node` to point to `[4]`.

The list now looks like this:
```
head_node -> [1] <-> [2] <-> [3] <-> [4] <- tail_node
```

---

### **Key Points**
1. **Inserting at position 0**:
   - Calls `add_to_head` to insert the node at the head.

2. **Inserting at a specific position**:
   - Traverses the list to find the correct position.
   - Links the new node to its neighbors.
   - Updates the `tail_node` if the new node is inserted at the end.

3. **Handling out-of-bounds positions**:
   - If the position is beyond the list's length, the node is added to the tail using `add_to_tail`.

# =========================================================================================================================== #

                                        *** remove_head() method: ***

Let's break down the `remove_head` method step by step to help you understand how it works.

---

### **Purpose of `remove_head`**
The `remove_head` method removes the **head node** (the first node) of the doubly linked list and returns its value.
If the list is empty, it returns `None`.

---

### **Code Breakdown**

```
def remove_head(self):
    removed_head = self.head_node  
    if removed_head is None:  
        return None
    self.head_node = removed_head.get_next_node()
    if self.head_node is not None:
        self.head_node.set_prev_node(None)  
    else:
        self.tail_node = None  
    return removed_head.get_value()  
```

---

### **Step-by-Step Explanation**

#### **Step 1: Store the current head node**
```
removed_head = self.head_node
```
- `removed_head` stores a reference to the current head node.
- This is the node that will be removed from the list.

---

#### **Step 2: Check if the list is empty**
```
if removed_head is None:
    return None
```
- If `removed_head` is `None`, it means the list is empty.
- In this case, there is nothing to remove, so the method returns `None`.

---

#### **Step 3: Update the head reference**
```
self.head_node = removed_head.get_next_node()
```
- The `head_node` of the list is updated to point to the **next node** in the list.
- This effectively removes the current head node from the list.

---

#### **Step 4: Remove the backward link**
```
if self.head_node is not None:
    self.head_node.set_prev_node(None)
```
- If the new head node (`self.head_node`) is not `None`:
  - The `prev_node` of the new head is set to `None`.
  - This removes the backward link from the new head to the old head.

---

#### **Step 5: Update the tail reference (if the list becomes empty)**
```
else:
    self.tail_node = None
```
- If the new head node is `None`, it means the list is now empty after removing the head.
- In this case, the `tail_node` is also set to `None`.

---

#### **Step 6: Return the value of the removed head**
```
return removed_head.get_value()
```
- The value of the removed head node is returned.

---

### **Example Walkthrough**

Let's walk through an example to see how this works.

#### **Initial State**
- The list contains the following nodes:
  ```
  head_node -> [1] <-> [2] <-> [3] <- tail_node
  ```

---

#### **Step 1: Remove the head**
```
dll.remove_head()
```
1. `removed_head` is set to the current head node (`[1]`).
2. The `head_node` is updated to point to the next node (`[2]`):
   - `head_node -> [2] <-> [3] <- tail_node`
3. The `prev_node` of the new head (`[2]`) is set to `None`:
   - `head_node -> [2] <-> [3] <- tail_node`
4. The value of the removed head (`1`) is returned.

The list now looks like this:
```
head_node -> [2] <-> [3] <- tail_node
```

---

#### **Step 2: Remove the head again**
```
dll.remove_head()
```
1. `removed_head` is set to the current head node (`[2]`).
2. The `head_node` is updated to point to the next node (`[3]`):
   - `head_node -> [3] <- tail_node`
3. The `prev_node` of the new head (`[3]`) is set to `None`:
   - `head_node -> [3] <- tail_node`
4. The value of the removed head (`2`) is returned.

The list now looks like this:
```
head_node -> [3] <- tail_node
```

---

#### **Step 3: Remove the head again**
```
dll.remove_head()
```
1. `removed_head` is set to the current head node (`[3]`).
2. The `head_node` is updated to point to the next node (`None`):
   - `head_node -> None`
3. Since the new head is `None`, the `tail_node` is also set to `None`:
   - `tail_node -> None`
4. The value of the removed head (`3`) is returned.

The list is now empty:
```
head_node -> None
tail_node -> None
```

---

#### **Step 4: Try to remove the head again**
```
dll.remove_head()
```
1. `removed_head` is set to the current head node (`None`).
2. Since the list is empty, the method returns `None`.

---

### **Key Points**
1. **Removing the head**:
   - The head node is removed, and the `head_node` is updated to point to the next node.
   - The `prev_node` of the new head is set to `None`.

2. **Handling an empty list**:
   - If the list is empty, the method returns `None`.

3. **Updating the tail**:
   - If the list becomes empty after removing the head, the `tail_node` is also set to `None`.

# =========================================================================================================================== #

                                        *** remove_tail() method: ***

Let's break down the `remove_tail` method step by step to help you understand how it works.

---

### **Purpose of `remove_tail`**
The `remove_tail` method removes the **tail node** (the last node) of the doubly linked list and returns its value.
If the list is empty, it returns `None`.

---

### **Code Breakdown**

```
def remove_tail(self):
    removed_tail = self.tail_node  
    if removed_tail is None:  
        return None
    self.tail_node = removed_tail.get_prev_node() 
    if self.tail_node is not None:
        self.tail_node.set_next_node(None) 
    else:
        self.head_node = None  
    return removed_tail.get_value() 
```

---

### **Step-by-Step Explanation**

#### **Step 1: Store the current tail node**
```
removed_tail = self.tail_node
```
- `removed_tail` stores a reference to the current tail node.
- This is the node that will be removed from the list.

---

#### **Step 2: Check if the list is empty**
```
if removed_tail is None:
    return None
```
- If `removed_tail` is `None`, it means the list is empty.
- In this case, there is nothing to remove, so the method returns `None`.

---

#### **Step 3: Update the tail reference**
```
self.tail_node = removed_tail.get_prev_node()
```
- The `tail_node` of the list is updated to point to the **previous node** in the list.
- This effectively removes the current tail node from the list.

---

#### **Step 4: Remove the forward link**
```
if self.tail_node is not None:
    self.tail_node.set_next_node(None)
```
- If the new tail node (`self.tail_node`) is not `None`:
  - The `next_node` of the new tail is set to `None`.
  - This removes the forward link from the new tail to the old tail.

---

#### **Step 5: Update the head reference (if the list becomes empty)**
```
else:
    self.head_node = None
```
- If the new tail node is `None`, it means the list is now empty after removing the tail.
- In this case, the `head_node` is also set to `None`.

---

#### **Step 6: Return the value of the removed tail**
```
return removed_tail.get_value()
```
- The value of the removed tail node is returned.

---

### **Example Walkthrough**

Let's walk through an example to see how this works.

#### **Initial State**
- The list contains the following nodes:
  ```
  head_node -> [1] <-> [2] <-> [3] <- tail_node
  ```

---

#### **Step 1: Remove the tail**
```
dll.remove_tail()
```
1. `removed_tail` is set to the current tail node (`[3]`).
2. The `tail_node` is updated to point to the previous node (`[2]`):
   - `head_node -> [1] <-> [2] <- tail_node`
3. The `next_node` of the new tail (`[2]`) is set to `None`:
   - `head_node -> [1] <-> [2] <- tail_node`
4. The value of the removed tail (`3`) is returned.

The list now looks like this:
```
head_node -> [1] <-> [2] <- tail_node
```

---

#### **Step 2: Remove the tail again**
```
dll.remove_tail()
```
1. `removed_tail` is set to the current tail node (`[2]`).
2. The `tail_node` is updated to point to the previous node (`[1]`):
   - `head_node -> [1] <- tail_node`
3. The `next_node` of the new tail (`[1]`) is set to `None`:
   - `head_node -> [1] <- tail_node`
4. The value of the removed tail (`2`) is returned.

The list now looks like this:
```
head_node -> [1] <- tail_node
```

---

#### **Step 3: Remove the tail again**
```
dll.remove_tail()
```
1. `removed_tail` is set to the current tail node (`[1]`).
2. The `tail_node` is updated to point to the previous node (`None`):
   - `head_node -> None`
3. Since the new tail is `None`, the `head_node` is also set to `None`:
   - `tail_node -> None`
4. The value of the removed tail (`1`) is returned.

The list is now empty:
```
head_node -> None
tail_node -> None
```

---

#### **Step 4: Try to remove the tail again**
```
dll.remove_tail()
```
1. `removed_tail` is set to the current tail node (`None`).
2. Since the list is empty, the method returns `None`.

---

### **Key Points**
1. **Removing the tail**:
   - The tail node is removed, and the `tail_node` is updated to point to the previous node.
   - The `next_node` of the new tail is set to `None`.

2. **Handling an empty list**:
   - If the list is empty, the method returns `None`.

3. **Updating the head**:
   - If the list becomes empty after removing the tail, the `head_node` is also set to `None`.

# =========================================================================================================================== #

                                        *** remove_by_value() method: ***

Let's break down the `remove_by_value` method step by step to help you understand how it works.

---

### **Purpose of `remove_by_value`**
The `remove_by_value` method removes the **first node** in the doubly linked list that contains the specified
`value_to_remove`. If the node is found and removed, the method returns the value. If the node is not found, it returns `None`.

---

### **Code Breakdown**

```
def remove_by_value(self, value_to_remove):
    current_node = self.head_node 
    while current_node is not None:  
        if current_node.get_value() == value_to_remove:
            if current_node == self.head_node:  
                return self.remove_head()
            elif current_node == self.tail_node: 
                return self.remove_tail()
            else:  # Middle of the list
                prev_node = current_node.get_prev_node()
                next_node = current_node.get_next_node()
                if prev_node:
                    prev_node.set_next_node(next_node)
                if next_node:
                    next_node.set_prev_node(prev_node)
                return value_to_remove  
        current_node = current_node.get_next_node()
    return None  
```

---

### **Step-by-Step Explanation**

#### **Step 1: Start from the head**
```
current_node = self.head_node
```
- Start traversing the list from the `head_node`.

---

#### **Step 2: Traverse the list**
```
while current_node is not None:
```
- Use a `while` loop to traverse the list until the end (`current_node` becomes `None`).

---

#### **Step 3: Check if the current node's value matches**
```
if current_node.get_value() == value_to_remove:
```
- If the value of the current node matches `value_to_remove`, proceed to remove the node.

---

#### **Step 4: Handle removal of the head node**
```
if current_node == self.head_node:
    return self.remove_head()
```
- If the node to be removed is the **head node**, call the `remove_head` method to handle the removal.
- The `remove_head` method updates the `head_node` and returns the removed value.

---

#### **Step 5: Handle removal of the tail node**
```
elif current_node == self.tail_node:
    return self.remove_tail()
```
- If the node to be removed is the **tail node**, call the `remove_tail` method to handle the removal.
- The `remove_tail` method updates the `tail_node` and returns the removed value.

---

#### **Step 6: Handle removal of a middle node**
```
else:
    prev_node = current_node.get_prev_node()
    next_node = current_node.get_next_node()

    if prev_node:
        prev_node.set_next_node(next_node)
    if next_node:
        next_node.set_prev_node(prev_node)

    return value_to_remove
```
- If the node to be removed is in the **middle** of the list:
  1. Get the `prev_node` and `next_node` of the current node.
  2. Update the `next_node` of `prev_node` to point to `next_node`.
  3. Update the `prev_node` of `next_node` to point to `prev_node`.
  4. This effectively removes the current node from the list.
  5. Return the value of the removed node.

---

#### **Step 7: Move to the next node**
```
current_node = current_node.get_next_node()
```
- If the current node does not match `value_to_remove`, move to the next node in the list.

---

#### **Step 8: Return `None` if the value is not found**
```
return None
```
- If the loop ends without finding a node with `value_to_remove`, return `None`.

---

### **Example Walkthrough**

Let's walk through an example to see how this works.

#### **Initial State**
- The list contains the following nodes:
  ```
  head_node -> [1] <-> [2] <-> [3] <- tail_node
  ```

---

#### **Step 1: Remove `2` from the list**
```
dll.remove_by_value(2)
```
1. Start from the head (`[1]`).
2. Check if `[1]`'s value matches `2` → No.
3. Move to the next node (`[2]`).
4. Check if `[2]`'s value matches `2` → Yes.
5. Since `[2]` is in the middle of the list:
   - `prev_node = [1]`
   - `next_node = [3]`
   - Update `[1]`'s `next_node` to point to `[3]`.
   - Update `[3]`'s `prev_node` to point to `[1]`.
6. Return the removed value (`2`).

The list now looks like this:
```
head_node -> [1] <-> [3] <- tail_node
```

---

#### **Step 2: Remove `1` from the list**
```
dll.remove_by_value(1)
```
1. Start from the head (`[1]`).
2. Check if `[1]`'s value matches `1` → Yes.
3. Since `[1]` is the head node, call `remove_head`.
4. `remove_head` updates the `head_node` to `[3]` and returns the removed value (`1`).

The list now looks like this:
```
head_node -> [3] <- tail_node
```

---

#### **Step 3: Remove `3` from the list**
```
dll.remove_by_value(3)
```
1. Start from the head (`[3]`).
2. Check if `[3]`'s value matches `3` → Yes.
3. Since `[3]` is the tail node, call `remove_tail`.
4. `remove_tail` updates the `tail_node` to `None` and returns the removed value (`3`).

The list is now empty:
```
head_node -> None
tail_node -> None
```

---

#### **Step 4: Try to remove `4` from the list**
```
dll.remove_by_value(4)
```
1. Start from the head (`None`).
2. Since the list is empty, the method returns `None`.

---

### **Key Points**
1. **Removing the head node**:
   - Calls `remove_head` to handle the removal.

2. **Removing the tail node**:
   - Calls `remove_tail` to handle the removal.

3. **Removing a middle node**:
   - Updates the `next_node` of the previous node and the `prev_node` of the next node to bypass the removed node.

4. **Handling value not found**:
   - If the value is not found in the list, the method returns `None`.

# =========================================================================================================================== #

                                        *** stringify_list() method: ***

Let's break down the `stringify_list` method step by step to help you understand how it works.

---

### **Purpose of `stringify_list`**
The `stringify_list` method converts the doubly linked list into a **string representation**, where each node's value is on a new line. This is useful for printing or displaying the contents of the list.

---

### **Code Breakdown**

```
def stringify_list(self):
    string_list = ""  
    current_node = self.head_node  # Start from the head of the list
    while current_node:
        if current_node.get_value() is not None:
            string_list += str(current_node.get_value()) + "\n"
        current_node = current_node.get_next_node()
    return string_list  
```

---

### **Step-by-Step Explanation**

#### **Step 1: Initialize an empty string**
```
string_list = ""
```
- `string_list` is initialized as an empty string. This will store the final string representation of the list.

---

#### **Step 2: Start from the head of the list**
```
current_node = self.head_node
```
- `current_node` is set to the `head_node` of the list. This is the starting point for traversing the list.

---

#### **Step 3: Traverse the list**
```
while current_node:
```
- Use a `while` loop to traverse the list until the end (`current_node` becomes `None`).

---

#### **Step 4: Append the current node's value to the string**
```
if current_node.get_value() is not None:
    string_list += str(current_node.get_value()) + "\n"
```
- If the current node's value is not `None`:
  - Convert the value to a string using `str()`.
  - Append the value to `string_list`, followed by a newline character (`\n`).

---

#### **Step 5: Move to the next node**
```
current_node = current_node.get_next_node()
```
- Update `current_node` to the next node in the list using `get_next_node()`.

---

#### **Step 6: Return the final string**
```
return string_list
```
- After the loop ends, return the `string_list` containing all the node values, each on a new line.

---

### **Example Walkthrough**

Let's walk through an example to see how this works.

#### **Initial State**
- The list contains the following nodes:
  ```
  head_node -> [1] <-> [2] <-> [3] <- tail_node
  ```

---

#### **Step 1: Initialize `string_list`**
```
string_list = ""
```

---

#### **Step 2: Start from the head**
```
current_node = self.head_node  # current_node = [1]
```

---

#### **Step 3: Traverse the list**
1. **First iteration**:
   - `current_node = [1]`
   - Append `1` to `string_list`:
     ```
     string_list = "1\n"
     ```
   - Move to the next node:
     ```
     current_node = [2]
     ```

2. **Second iteration**:
   - `current_node = [2]`
   - Append `2` to `string_list`:
     ```
     string_list = "1\n2\n"
     ```
   - Move to the next node:
     ```
     current_node = [3]
     ```

3. **Third iteration**:
   - `current_node = [3]`
   - Append `3` to `string_list`:
     ```
     string_list = "1\n2\n3\n"
     ```
   - Move to the next node:
     ```
     current_node = None
     ```

---

#### **Step 4: Return the final string**
```
return string_list
```
- The final value of `string_list` is:
  ```
  "1\n2\n3\n"
  ```
- When printed, it will look like:
  ```
  1
  2
  3
  ```

---

### **Key Points**
1. **Traversing the list**:
   - The method starts from the `head_node` and moves to the next node until the end of the list (`current_node` becomes `None`).

2. **Appending values to the string**:
   - Each node's value is converted to a string and appended to `string_list`, followed by a newline character (`\n`).

3. **Handling `None` values**:
   - If a node's value is `None`, it is skipped and not added to the string.

4. **Returning the result**:
   - The method returns the final string representation of the list.

---

### **Example Output**
For the list:
```
head_node -> [1] <-> [2] <-> [3] <- tail_node
```
The output of `stringify_list` will be:
```
1
2
3
```
 
# =========================================================================================================================== #

                              *** Creating a New Doubly Linked List ***
                              
Let’s break it down step by step so you understand exactly what’s happening. 🚀

---

## **Understanding the Code Step by Step**

### **1. Creating a New Doubly Linked List**
```
dll = DoublyLinkedList()
```
- This initializes an **empty** doubly linked list.
- At this point:
  ```
  head_node → None
  tail_node → None
  ```
  Since no nodes have been added, both `head_node` and `tail_node` are `None`.

---

### **2. Adding Elements to the List**
```
dll.add_to_head(5)
```
- Adds `5` to the head.
- Since this is the first node, both `head_node` and `tail_node` point to it:
  ```
  head_node → [ 5 ] ← tail_node
  ```

```
dll.add_to_tail(10)
```
- Adds `10` to the tail.
- The `next` of `5` now points to `10`, and `prev` of `10` points to `5`:
  ```plaintext
  head_node → [ 5 ] ⇄ [ 10 ] ← tail_node
  ```

```
dll.add_to_tail(15)
```
- Adds `15` to the tail.
- Updates `next` and `prev` links:
  ```plaintext
  head_node → [ 5 ] ⇄ [ 10 ] ⇄ [ 15 ] ← tail_node
  ```

```
dll.add_to_head(1)
```
- Adds `1` to the head.
- Updates the `prev` of `5` and `next` of `1`:
  ```plaintext
  head_node → [ 1 ] ⇄ [ 5 ] ⇄ [ 10 ] ⇄ [ 15 ] ← tail_node
  ```

---

### **3. Printing the List**
```
print(dll.stringify_list())
```
- This prints:
  ```plaintext
  1
  5
  10
  15
  ```

---

### **4. Inserting an Element at Position 2**
```
dll.insert(2, 7)
```
- Inserts `7` at index `2` (0-based index).
- Updates the links:
  ```
  head_node → [ 1 ] ⇄ [ 5 ] ⇄ [ 7 ] ⇄ [ 10 ] ⇄ [ 15 ] ← tail_node
  ```

**New list printout:**
```
1
5
7
10
15
```

---

### **5. Removing the Head**
```
dll.remove_head()
```
- Removes `1`.
- Updates the `head_node` to `5` and removes the `prev` link of `5`:
  ```
  head_node → [ 5 ] ⇄ [ 7 ] ⇄ [ 10 ] ⇄ [ 15 ] ← tail_node
  ```

**New list printout:**
```
5
7
10
15
```

---

### **6. Removing the Tail**
```
dll.remove_tail()
```
- Removes `15`.
- Updates the `tail_node` to `10` and removes the `next` link of `10`:
  ```
  head_node → [ 5 ] ⇄ [ 7 ] ⇄ [ 10 ] ← tail_node
  ```

**New list printout:**
```
5
7
10
```

---

### **7. Removing an Element by Value**
```
dll.remove_by_value(7)
```
- Finds `7` and removes it by updating links:
  ```
  head_node → [ 5 ] ⇄ [ 10 ] ← tail_node
  ```

**Final list printout:**
```
5
10
```

Here’s an **ASCII representation** of your **doubly linked list** at different stages. 🚀  

---

### **1️⃣ Initial Empty List**
```
(None)
```

---

### **2️⃣ After `add_to_head(5)`**
```
(None) <- [ 5 ] -> (None)
head_node & tail_node point here
```

---

### **3️⃣ After `add_to_tail(10)`**
```
(None) <- [ 5 ] <--> [ 10 ] -> (None)
head_node              tail_node
```

---

### **4️⃣ After `add_to_tail(15)`**
```
(None) <- [ 5 ] <--> [ 10 ] <--> [ 15 ] -> (None)
head_node                                tail_node
```

---

### **5️⃣ After `add_to_head(1)`**
```
(None) <- [ 1 ] <--> [ 5 ] <--> [ 10 ] <--> [ 15 ] -> (None)
head_node                                         tail_node
```

---

### **6️⃣ After `insert(2, 7)`**
```
(None) <- [ 1 ] <--> [ 5 ] <--> [ 7 ] <--> [ 10 ] <--> [ 15 ] -> (None)
head_node                                                tail_node
```

---

### **7️⃣ After `remove_head()` (Removing `1`)**
```
(None) <- [ 5 ] <--> [ 7 ] <--> [ 10 ] <--> [ 15 ] -> (None)
head_node                                        tail_node
```

---

### **8️⃣ After `remove_tail()` (Removing `15`)**
```
(None) <- [ 5 ] <--> [ 7 ] <--> [ 10 ] -> (None)
head_node                        tail_node
```

---

### **9️⃣ After `remove_by_value(7)`**
```
(None) <- [ 5 ] <--> [ 10 ] -> (None)
head_node        tail_node
```

---

### **🔚 Final List**
```
(None) <- [ 5 ] <--> [ 10 ] -> (None)
head_node        tail_node
```

This visually represents how the list changes step by step!

"""
