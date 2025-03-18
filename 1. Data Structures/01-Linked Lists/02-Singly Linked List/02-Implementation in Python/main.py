# Implementation in Python:

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def __str__(self):
        return f"Node({self.value})"


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value) if value is not None else None

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_end(self, value):
        new_node = Node(value)
        if self.head_node is None:
            self.head_node = new_node
            return

        current_node = self.head_node
        while current_node.get_next_node():
            current_node = current_node.get_next_node()
        current_node.set_next_node(new_node)

    def remove_node(self, value_to_remove):
        current_node = self.head_node

        if current_node and current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            return

        while current_node and current_node.get_next_node():
            next_node = current_node.get_next_node()
            if next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                return
            current_node = next_node

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + " -> "
            current_node = current_node.get_next_node()
        return string_list[:-4] if string_list else "Empty List"

    def search(self, value):
        current_node = self.head_node
        while current_node:
            if current_node.get_value() == value:
                return True
            current_node = current_node.get_next_node()
        return False

    def reverse(self):
        prev = None
        current = self.head_node
        while current:
            next_node = current.get_next_node()
            current.set_next_node(prev)
            prev = current
            current = next_node
        self.head_node = prev

    def find_middle(self):
        slow = self.head_node
        fast = self.head_node
        while fast and fast.get_next_node():
            slow = slow.get_next_node()
            fast = fast.get_next_node().get_next_node()
        return slow.get_value() if slow else None

    def has_cycle(self):
        slow = self.head_node
        fast = self.head_node
        while fast and fast.get_next_node():
            slow = slow.get_next_node()
            fast = fast.get_next_node().get_next_node()
            if slow == fast:
                return True
        return False

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

    def remove_duplicates(self):
        if not self.head_node:
            return

        seen_values = set()
        current_node = self.head_node
        seen_values.add(current_node.get_value())

        while current_node.get_next_node():
            next_node = current_node.get_next_node()
            if next_node.get_value() in seen_values:
                current_node.set_next_node(next_node.get_next_node())
            else:
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
ll.get_head_node().get_next_node().get_next_node().set_next_node(ll.get_head_node())  # Cycle at node 1
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


# Output:

"""
Original List:
1 -> 2 -> 3 -> 4 -> 5

Search for 3: True
Search for 10: False

Middle Node: 3

Reversed List:
5 -> 4 -> 3 -> 2 -> 1

Cycle Detected: False
Cycle Detected after introducing cycle: True
Cycle Start Node: 5

List before removing duplicates:
5 -> 4 -> 3 -> 3 -> 4 -> 4

List after removing duplicates:
5 -> 4 -> 3

"""


# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Node Class

1. **`__init__` Method:**
   - **Time Complexity:** O(1)
   - **Space Complexity:** O(1)
   
   - **Explanation:** Initializing a node with a value and an optional next node reference is a constant-time operation.
   The space required is also constant since we are just creating a single node.

2. **`get_value` Method:**
   - **Time Complexity:** O(1)
   - **Space Complexity:** O(1)
   
   - **Explanation:** Accessing the value of a node is a constant-time operation.

3. **`get_next_node` Method:**
   - **Time Complexity:** O(1)
   - **Space Complexity:** O(1)
   
   - **Explanation:** Accessing the next node reference is a constant-time operation.

4. **`set_next_node` Method:**
   - **Time Complexity:** O(1)
   - **Space Complexity:** O(1)
   
   - **Explanation:** Setting the next node reference is a constant-time operation.

5. **`__str__` Method:**
   - **Time Complexity:** O(1)
   - **Space Complexity:** O(1)
   
   - **Explanation:** Converting the node to a string representation is a constant-time operation.

### LinkedList Class

#### 1. **`__init__`**
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)

- Explanation: Initializing the `head_node` is a constant-time operation.

---

#### 2. **`get_head_node`**
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)

- Explanation: Simply returns the `head_node`, which is a constant-time operation.

---

#### 3. **`insert_beginning`**
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)

- Explanation: Inserting a new node at the beginning involves creating a new node and updating the `head_node`,
which is a constant-time operation.

---

#### 4. **`insert_end`**
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

- Explanation: In the worst case, you need to traverse the entire list to find the last node, which takes O(n) time.
The space complexity is constant because only a fixed number of variables are used.

---

#### 5. **`remove_node`**
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

- Explanation: In the worst case, you need to traverse the entire list to find the node to remove, which takes O(n) time.
The space complexity is constant because no additional data structures are used.

---

#### 6. **`stringify_list`**
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

- Explanation: You need to traverse the entire list to build the string representation, which takes O(n) time.
The space complexity is O(n) because the string grows linearly with the number of nodes.

---

#### 7. **`search`**
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

- Explanation: In the worst case, you need to traverse the entire list to find the value, which takes O(n) time.
The space complexity is constant because no additional data structures are used.

---

#### 8. **`reverse`**
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

- Explanation: Reversing the list requires traversing the entire list once, which takes O(n) time.
The space complexity is constant because only a fixed number of variables are used.

---

#### 9. **`find_middle`**
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

- Explanation: The "two-pointer" technique (slow and fast pointers) traverses the list in O(n) time.
The space complexity is constant because only two pointers are used.

---

#### 10. **`has_cycle`**
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

- Explanation: The "two-pointer" technique (slow and fast pointers) traverses the list in O(n) time.
The space complexity is constant because only two pointers are used.

---

#### 11. **`find_cycle_start`**
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

- Explanation: Detecting the cycle and finding its start involves traversing the list with two pointers,
which takes O(n) time. The space complexity is constant because only a fixed number of variables are used.

---

#### 12. **`remove_duplicates`**
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

- Explanation: Traversing the list takes O(n) time. The space complexity is O(n) because a set is used to store
seen values, which can grow up to the size of the list in the worst case (if all values are unique).

---

### Summary Table

| Method               | Time Complexity | Space Complexity |
|----------------------|-----------------|------------------|
| `__init__`           | O(1)            | O(1)             |
| `get_head_node`      | O(1)            | O(1)             |
| `insert_beginning`   | O(1)            | O(1)             |
| `insert_end`         | O(n)            | O(1)             |
| `remove_node`        | O(n)            | O(1)             |
| `stringify_list`     | O(n)            | O(n)             |
| `search`             | O(n)            | O(1)             |
| `reverse`            | O(n)            | O(1)             |
| `find_middle`        | O(n)            | O(1)             |
| `has_cycle`          | O(n)            | O(1)             |
| `find_cycle_start`   | O(n)            | O(1)             |
| `remove_duplicates`  | O(n)            | O(n)             |

---

### Key Takeaways
- Most operations that involve traversing the list (e.g., `insert_end`, `remove_node`, `search`, `reverse`, etc.)
have a **time complexity of O(n)**.

- Operations that modify the head of the list (e.g., `insert_beginning`) have a **time complexity of O(1)**.

- The **space complexity** is generally O(1) for most operations, except for `stringify_list` and `remove_duplicates`,
which use additional space proportional to the size of the list.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""

                                                     # **Node Class**

## **Understanding the `Node` Class**

A **node** is a building block of a **linked list**. Each node stores:
1. **A value** (the actual data).
2. **A reference (pointer) to the next node** in the list.

```
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
```
- `value`: Stores the actual data.
- `next_node`: Points to the next node in the list (default is `None`).

- **Example**:
```
node = Node(10)  # Creates a node with value 10 and next_node as None
```


### **Methods in the `Node` Class**

#### 1️⃣ `get_value(self)`
```
def get_value(self):
    return self.value
```
- Returns the **value** stored in the node.

- **Example**:
```
node = Node(10)
print(node.get_value())  # Output: 10
```


#### 2️⃣ `get_next_node(self)`
```
def get_next_node(self):
    return self.next_node
```
- Returns the **reference** (pointer) to the next node.

- **Example**:
```
node1 = Node(10)
node2 = Node(20, node1)  # node2 points to node1
print(node2.get_next_node())  # Output: <Node object at memory_location>
```


#### 3️⃣ `set_next_node(self, next_node)`
```
def set_next_node(self, next_node):
    self.next_node = next_node
```
- Updates the `next_node` reference, linking this node to another node.

- **Example**:
```
node1 = Node(10)
node2 = Node(20)
node1.set_next_node(node2)  # node1 now points to node2
```


#### 4️⃣ `__str__(self)`
```
def __str__(self):
    return f"Node({self.value})"
```
- Returns a string representation of the node for easy debugging.

- **Example**:
```
node = Node(10)
print(node)  # Output: Node(10)
```

# =========================================================================================================================== #

                                                # **LinkedList Class**
    
## **Understanding the `LinkedList` Class**

A **linked list** is a sequence of nodes where:
- Each node stores a value and a reference to the next node.
- The list starts at a special node called the **head**.

```
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value) if value is not None else None
```

- If a value is given, the list starts with a **head node**.
- Otherwise, the list is **empty**.

# =========================================================================================================================== #

                                           **Methods in the `LinkedList` Class**
                                           
                                                    get_head_node(self)

```
def get_head_node(self):
    return self.head_node
```

- Returns the **head node** (first node) of the list.

# =========================================================================================================================== #

                                                insert_beginning(self, new_value)
                                                
**How it works:**
- Creates a new node with `new_value`.
- Links it to the **current head node**.
- Updates the head to the new node.

**Example:**
```
ll = LinkedList()
ll.insert_beginning(3)  # List: 3
ll.insert_beginning(2)  # List: 2 -> 3
ll.insert_beginning(1)  # List: 1 -> 2 -> 3
```

# =========================================================================================================================== #

                                                    insert_end(self, value)

## **Understanding `insert_end(self, value)`**
This method **inserts a new node at the end** of the linked list.

### **Code Breakdown**
```
def insert_end(self, value):
    new_node = Node(value)  # Step 1: Create a new node with the given value
```
- A new node is created with `value`.  
- At this point, `new_node.next_node` is `None` (because we are just creating the node).  

---

```
    if self.head_node is None:  # Step 2: If list is empty
        self.head_node = new_node  # Make new_node the head
        return
```
- If the **list is empty** (`self.head_node is None`),  
  - The new node becomes the **head** of the linked list.
  - The function **returns immediately**, since the node has been added.

---

```
    current_node = self.head_node  # Step 3: Start from the head node
```
- If the list **is not empty**,  
  - We start from the **head node** and traverse the list.

---

```
    while current_node.get_next_node():  # Step 4: Traverse to the last node
        current_node = current_node.get_next_node()
```
- This **loop moves through** each node in the linked list.  
- It stops when it reaches the **last node**, which is the node whose `next_node` is `None`.  

---

```
    current_node.set_next_node(new_node)  # Step 5: Link last node to new node
```
- Once the **last node** is found,  
  - We **set its `next_node`** to point to the new node.  
- Now, the new node is **added at the end** of the list.

---

## **Example Walkthrough**

Let’s see how this works with an example.

### **Step 1: Create an Empty Linked List**
```
ll = LinkedList()
```
- `head_node` is `None` because the list is empty.

---

### **Step 2: Insert `1`**
```
ll.insert_end(1)
```
- Since the list is **empty**, the new node with value `1` becomes the **head**.
- **List after operation**:  
  ```
  1
  ```

---

### **Step 3: Insert `2`**
```
ll.insert_end(2)
```
- The method starts at `head_node` (which contains `1`).
- Since `1` is the **only node**, we **set its `next_node`** to the new node `2`.
- **List after operation**:
  ```
  1 -> 2
  ```

---

### **Step 4: Insert `3`**
```
ll.insert_end(3)
```
- The method starts at `head_node` (which contains `1`).
- It moves to the **next node** (`2`), which is the last node.
- It **sets `2.next_node` to `3`**.
- **List after operation**:
  ```
  1 -> 2 -> 3
  ```

---

## **Final Thoughts**
- If the list is **empty**, we **set the head** to the new node.
- If the list has **nodes**, we **traverse** to the last node and **attach** the new node at the end.

# =========================================================================================================================== #

                                             remove_node(self, value_to_remove)

## **Understanding `remove_node(self, value_to_remove)`**
This method **removes the first node** that contains the given `value_to_remove` from the linked list.

### **Code Breakdown**
```
def remove_node(self, value_to_remove):
    current_node = self.head_node
```
- We start at the **head node** and assign it to `current_node`.

---

### **Step 1: Check if the Head Node is the One to Remove**
```
    if current_node and current_node.get_value() == value_to_remove:
        self.head_node = current_node.get_next_node()  # Move head to next node
        return
```
- If the **head node** itself has the value we need to remove:
  - We update `self.head_node` to the **next node**.
  - This effectively **removes the head node** from the list.
  - **Function returns early** (no need to continue).

---

### **Step 2: Traverse the List to Find the Node to Remove**
```
    while current_node and current_node.get_next_node():
```
- If the **head node wasn't removed**, we **traverse the list** to find the node containing `value_to_remove`.
- The loop **stops** when:
  - We reach the **end of the list** (`current_node` becomes `None`).
  - OR we find a **matching node to remove**.

---

### **Step 3: Check the Next Node**
```
next_node = current_node.get_next_node()
if next_node.get_value() == value_to_remove:
```
- `next_node` stores the **next node** in the list.
- If `next_node` contains `value_to_remove`, we **remove it**.

---

### **Step 4: Remove the Node**
```
current_node.set_next_node(next_node.get_next_node())  # Skip node
return
```
- We **skip the node** by making `current_node.next_node` point to `next_node.next_node`.  
- This effectively removes `next_node` from the list.
- The function **returns early** after removal.

---

### **Step 5: Move to the Next Node**
```
current_node = next_node  # Move to next node
```
- If the current node **wasn't** the one we removed,  
  - We continue moving to the next node until we find and remove the target value.

---

## **Example Walkthrough**

Let's go step by step through an example.

### **Step 1: Create a Linked List**
```
ll = LinkedList()
ll.insert_end(1)
ll.insert_end(2)
ll.insert_end(3)
ll.insert_end(4)
ll.insert_end(5)
```
**Initial List:**
```
1 -> 2 -> 3 -> 4 -> 5
```

---

### **Step 2: Remove `3`**
```
ll.remove_node(3)
```
1. `current_node = head_node (1)`
2. **`1` is not `3`**, move to next.
3. `current_node = 2`
4. `next_node = 3` (matches `3`), so we **skip `3`**:
   ```
   1 -> 2 -> 4 -> 5
   ```

---

### **Step 3: Remove `1` (Head Node)**
```
ll.remove_node(1)
```
1. `current_node = head_node (1)`
2. **`1` is the target**, so we set the **head to `2`**:
   ```
   2 -> 4 -> 5
   ```

---

## **Final Thoughts**
- If the **head node** matches, we **update the head**.
- Otherwise, we **traverse the list**, find the first match, and **skip that node**.
- The method **removes only the first occurrence** of the value.

# =========================================================================================================================== #

                                                stringify_list(self)

This method **creates a string representation of the linked list**, which helps us see the contents of the list
in a readable format.

### **Method Explanation**
```
def stringify_list(self):
    string_list = ""  # Initialize an empty string
    current_node = self.head_node  # Start with the head node
```
1. **`string_list = ""`**:  
   We start with an empty string `string_list`. This will hold the final string representation of the linked list.

2. **`current_node = self.head_node`**:  
   The `current_node` starts at the **head node** of the linked list. We will use this to traverse the list.

---

```
while current_node:  # Traverse the linked list
    string_list += str(current_node.get_value()) + " -> "  # Add node's value to the string
    current_node = current_node.get_next_node()  # Move to the next node
```
3. **`while current_node:`**:  
   This loop will run as long as `current_node` is not `None` (i.e., it hasn't reached the end of the list).

4. **`string_list += str(current_node.get_value()) + " -> "`**:  
   - For each node, we get its **value** using `current_node.get_value()`.
   - We **convert** the value to a string (in case it’s not a string).
   - We then add the node’s value followed by `" -> "` to the `string_list`.  
     This creates the visual "link" between nodes in the string.

5. **`current_node = current_node.get_next_node()`**:  
   After adding the current node’s value, we move to the **next node** by updating `current_node`.

---

```
return string_list[:-4] if string_list else "Empty List"
```
6. **`string_list[:-4]`**:  
   After the loop finishes, `string_list` will have a trailing `" -> "` at the end.  
   We **remove** the last four characters (`" -> "`) using slicing: `[:-4]`.

7. **`if string_list else "Empty List"`**:  
   - If `string_list` is empty (i.e., the list is empty), it returns `"Empty List"`.
   - Otherwise, it returns the final string representation of the linked list.

---

## **Example Walkthrough**

Let’s walk through an example.

### **Example 1: A List with Nodes**
```
ll = LinkedList()
ll.insert_end(1)
ll.insert_end(2)
ll.insert_end(3)
```

- **Initial list**:  
  ```
  1 -> 2 -> 3
  ```

- When we call `ll.stringify_list()`, it performs the following:
  - Starts with `current_node` as the **head node** (`1`).
  
  - Adds `1` to `string_list`:  
    `"1 -> "`
    
  - Moves to the next node (`2`), adds `2`:  
    `"1 -> 2 -> "`
    
  - Moves to the next node (`3`), adds `3`:  
    `"1 -> 2 -> 3 -> "`
    
  - The loop ends because `current_node` is now `None`.
  
  - We slice off the last `" -> "`, resulting in:  
    `"1 -> 2 -> 3"`

### **Example 2: An Empty List**
```
empty_ll = LinkedList()
```

- **List is empty**:  
  The `stringify_list` method returns `"Empty List"`.

---

## **Final Thoughts**
- The method **traverses the linked list** node by node, appending each node's value to a string.
- The final result is a string representation of the list (e.g., `"1 -> 2 -> 3"`).
- If the list is empty, it returns `"Empty List"`.

# =========================================================================================================================== #

                                                search(self, value)
                                                
### **What does this method do?**

The `search` method is used to **search for a value** in the linked list. It returns `True` if it finds the value
in any of the nodes and `False` if the value is not found.

### **Code Explanation**

```
def search(self, value):
    current_node = self.head_node  # Start with the head node
```
- **`current_node = self.head_node`**:  
  We start by setting `current_node` to the **head node** of the linked list. This is where the search begins.
  
---

```
while current_node:  # Traverse through the list until we reach the end (None)
```
- **`while current_node:`**:  
  This `while` loop will continue as long as `current_node` is not `None`.  
  - If `current_node` is `None`, it means we’ve reached the end of the list.
  
---

```
if current_node.get_value() == value:  # Check if current node's value matches
    return True  # Value found, return True
```
- **`if current_node.get_value() == value:`**:  
  This checks if the value in the **current node** matches the value we are looking for (`value`).
  - If the values match, it **returns `True`**, indicating that the value was found.

---

```
current_node = current_node.get_next_node()  # Move to the next node
```
- **`current_node = current_node.get_next_node()`**:  
  If the value didn't match, we move to the **next node** in the list and repeat the process.
  
---

```
return False  # If we reach the end and didn't find the value, return False
```
- If we **reach the end of the list** (i.e., `current_node` becomes `None`) without finding the value, we **return `False`**.

---

### **Example Walkthrough**

Let’s go through a few examples to see how this method works.

### **Example 1: Searching for a Value that Exists in the List**
```
ll = LinkedList()
ll.insert_end(1)
ll.insert_end(2)
ll.insert_end(3)

print(ll.search(2))  # Output: True
```

- **Step-by-Step Search**:
  1. We start at the **head node**, which contains `1`.
  2. The value `1` is not equal to `2`, so we move to the next node (which contains `2`).
  3. Now, the value `2` is equal to the search value, so we **return `True`**.

- **Final Output**: `True`.

---

### **Example 2: Searching for a Value that Does Not Exist in the List**
```
print(ll.search(4))  # Output: False
```

- **Step-by-Step Search**:
  1. We start at the **head node**, which contains `1`.
  2. The value `1` is not equal to `4`, so we move to the next node (which contains `2`).
  3. The value `2` is not equal to `4`, so we move to the next node (which contains `3`).
  4. The value `3` is not equal to `4`, and there are no more nodes to check.
  5. Since we've reached the end of the list without finding `4`, we **return `False`**.

- **Final Output**: `False`.

---

### **Final Thoughts**

- The `search` method **traverses** the entire linked list from the head to the last node.
- It checks if each node's value matches the one we are looking for.
- If it finds a match, it returns `True`. If it doesn't, it returns `False`.

# =========================================================================================================================== #

                                                reverse(self)

### **What does the method do?**
The `reverse` method changes the direction of the "links" between nodes so that they point backward instead of forward.

### **Code Breakdown**

```
def reverse(self):
    prev = None  # Initialize a variable to hold the previous node (starts as None)
    current = self.head_node  # Start with the head node of the list
```
1. **`prev = None`**:  
   We initialize `prev` to `None` because, at the start, the **head node** will become the **last node** after
   reversal, and its `next_node` should point to `None`.

2. **`current = self.head_node`**:  
   `current` is initialized to the **head node**, and this will be the node we are currently working with during
   the reversal process.

---

```
while current:  # Continue until we reach the end of the list (when current is None)
```
3. **`while current:`**:  
   This loop will continue as long as `current` is not `None`, meaning we haven’t reached the end of the linked
   list yet. It allows us to process each node.

---

```
next_node = current.get_next_node()  # Save the next node (to avoid losing track of it)
```
4. **`next_node = current.get_next_node()`**:  
   - Before changing the `next_node` of the current node, we store it in a temporary variable called `next_node`.  
   - This ensures that we don't lose track of the **next node** in the list after we modify the current node's `next_node`.

---

```
current.set_next_node(prev)  # Reverse the link: current’s next node should point to the previous node
```
5. **`current.set_next_node(prev)`**:  
   - We change the **next pointer** of the current node to point to the previous node (`prev`).  
   - This **reverses the direction** of the link between the nodes.
   - Initially, the current node’s `next_node` pointed to the next node in the list, but now it points to the
   node we just processed (i.e., `prev`).

---

```
prev = current  # Move prev to current for the next iteration
current = next_node  # Move to the next node in the list
```
6. **`prev = current`**:  
   - After reversing the link, we move `prev` to point to the current node. This is necessary for the next node
   we process, as it will need to point backward to the current node.

7. **`current = next_node`**:  
   - We move to the next node in the list by setting `current` to `next_node`. This ensures that we continue the
   process until we reach the end of the list.

---

```
self.head_node = prev  # Update the head node to be the last processed node (new head)
```
8. **`self.head_node = prev`**:  
   - After the loop finishes (when `current` becomes `None`), `prev` will be pointing to the **last node** in the
   list, which is now the new head of the reversed list.
   - We set the `head_node` of the linked list to `prev`.

---

### **Example Walkthrough**

Let’s walk through an example to see how this works with a linked list.

### **Initial Linked List**
```
1 -> 2 -> 3 -> 4 -> 5
```

### **Step-by-Step Reversal**

1. **First Iteration:**
   - **current** is `1`, **prev** is `None`.
   - `next_node` is `2`.
   
   - We set `current.next_node` (node `1`) to `prev` (`None`), so now node `1` points to `None`.
   - `prev` becomes node `1`, `current` moves to node `2`.

   New list after first iteration:
   ```
   1 -> None
   ```

2. **Second Iteration:**

   - **current** is `2`, **prev** is `1`.
   - `next_node` is `3`.
   
   - We set `current.next_node` (node `2`) to `prev` (`1`), so node `2` now points to `1`.
   - `prev` becomes node `2`, `current` moves to node `3`.

   New list after second iteration:
   ```
   2 -> 1 -> None
   ```

3. **Third Iteration:**

   - **current** is `3`, **prev** is `2`.
   - `next_node` is `4`.
   
   - We set `current.next_node` (node `3`) to `prev` (`2`), so node `3` now points to `2`.
   - `prev` becomes node `3`, `current` moves to node `4`.

   New list after third iteration:
   ```
   3 -> 2 -> 1 -> None
   ```

4. **Fourth Iteration:**

   - **current** is `4`, **prev** is `3`.
   - `next_node` is `5`.
   
   - We set `current.next_node` (node `4`) to `prev` (`3`), so node `4` now points to `3`.
   - `prev` becomes node `4`, `current` moves to node `5`.

   New list after fourth iteration:
   ```
   4 -> 3 -> 2 -> 1 -> None
   ```

5. **Fifth Iteration:**

   - **current** is `5`, **prev** is `4`.
   - `next_node` is `None` (end of the list).
   
   - We set `current.next_node` (node `5`) to `prev` (`4`), so node `5` now points to `4`.
   - `prev` becomes node `5`, `current` moves to `None` (end of the list).

   New list after fifth iteration:
   ```
   5 -> 4 -> 3 -> 2 -> 1 -> None
   ```

### **Result:**

After all the iterations, `prev` points to the node `5`, which is now the head of the reversed list.
We update `self.head_node` to `prev`.

### **Final Reversed List:**
```
5 -> 4 -> 3 -> 2 -> 1
```

### **Final Thoughts**

- The `reverse` method works by **reversing the links** between nodes. It starts with the head node and
progressively makes each node point to the previous one.
- Once the list is completely reversed, the new head is the last node in the original list.

Does that clear things up? Let me know if anything is still confusing! 😊

# =========================================================================================================================== #

                                                    find_middle(self)
 
### **What does the method do?**

The `find_middle` method finds the **middle node** in a linked list. If the list has an odd number of nodes, it returns
the middle node. If the list has an even number of nodes, it returns the second middle node (since there isn't one "exact"
middle in that case). This method uses a technique called the **two-pointer technique**.

### **Code Breakdown**

```
def find_middle(self):
    slow = self.head_node  # Start slow pointer at the head node
    fast = self.head_node  # Start fast pointer at the head node
```

1. **`slow = self.head_node`**:  
   The `slow` pointer starts at the **head node**. This pointer will move **one step at a time** through the list.
   
2. **`fast = self.head_node`**:  
   The `fast` pointer also starts at the **head node**, but this pointer will move **two steps at a time** through the list.

---

```
while fast and fast.get_next_node():  # Continue until fast reaches the end
    slow = slow.get_next_node()  # Move slow pointer one step forward
    fast = fast.get_next_node().get_next_node()  # Move fast pointer two steps forward
```

3. **`while fast and fast.get_next_node():`**:  
   This loop runs until `fast` reaches the end of the list. The condition checks if `fast` exists and if
   `fast.get_next_node()` is not `None` (meaning there’s still another node to move to).
   
4. **`slow = slow.get_next_node()`**:  
   In each iteration, the `slow` pointer moves **one step forward**, so it advances one node at a time.

5. **`fast = fast.get_next_node().get_next_node()`**:  
   In each iteration, the `fast` pointer moves **two steps forward**. It first moves to `fast.get_next_node()` and
   then again to `fast.get_next_node().get_next_node()`. This way, `fast` skips over one node each time.

---

```
return slow.get_value() if slow else None  # Return the value of the middle node
```

6. **`return slow.get_value() if slow else None`**:  
   After the loop finishes, the `slow` pointer will be at the middle node. We return the **value** of that
   middle node with `slow.get_value()`.
   - If the list is empty (i.e., `slow` is `None`), the method will return `None`.

---

### **Why does this work?**

The key to understanding this method is how the **slow** and **fast** pointers move:
- **Fast pointer** moves **two steps at a time**.
- **Slow pointer** moves **one step at a time**.

Because the `fast` pointer moves twice as fast as the `slow` pointer, when `fast` reaches the end of the list,
`slow` will have reached the **middle**.

### **Example Walkthrough**

Let’s walk through an example with a list of 5 nodes: `[1, 2, 3, 4, 5]`.

1. **Initial Setup**:  
   - `slow = 1` (head node)
   - `fast = 1` (head node)

2. **First Iteration**:
   - `slow` moves 1 step: `slow = 2`
   - `fast` moves 2 steps: `fast = 3`
   
   So after the first iteration:
   - `slow = 2`
   - `fast = 3`
   
3. **Second Iteration**:
   - `slow` moves 1 step: `slow = 3`
   - `fast` moves 2 steps: `fast = 5`
   
   So after the second iteration:
   - `slow = 3`
   - `fast = 5`

4. **End of Loop**:
   - The `fast` pointer now reaches the end of the list (`None`), so the loop stops.
   - At this point, `slow` is at the middle node (`3`), so the method returns `slow.get_value()`, which is `3`.

### **Example with an Even Number of Nodes**

Now, let’s try a list with 4 nodes: `[1, 2, 3, 4]`.

1. **Initial Setup**:  
   - `slow = 1` (head node)
   - `fast = 1` (head node)

2. **First Iteration**:
   - `slow` moves 1 step: `slow = 2`
   - `fast` moves 2 steps: `fast = 3`
   
   So after the first iteration:
   - `slow = 2`
   - `fast = 3`
   
3. **Second Iteration**:
   - `slow` moves 1 step: `slow = 3`
   - `fast` moves 2 steps: `fast = None`
   
   The loop ends since `fast` reached the end of the list.

4. **Final Result**:
   - Now, the `slow` pointer is at node `3`. Since the list has an **even number of nodes**, the method
   returns `3` as the second middle node.

---

### **Summary**
- The `slow` pointer moves one step at a time, and the `fast` pointer moves two steps at a time.
- When `fast` reaches the end, `slow` will be at the middle node.
- If the list has an odd number of nodes, it returns the middle node. If the list has an even number,
it returns the second middle node.

# =========================================================================================================================== #

                                                    has_cycle(self)

This method is designed to detect if a **linked list contains a cycle**. A **cycle** happens when a node’s `next` pointer 
points back to one of the previous nodes, creating a loop.

The method uses the **Floyd's Tortoise and Hare algorithm**, which is a common and efficient way to detect cycles
in a linked list. This algorithm uses two pointers moving at different speeds to detect the cycle. Here's the breakdown:

### **What does the method do?**

The `has_cycle` method checks if the linked list contains a cycle. It uses two pointers:
1. **`slow` pointer**: Moves one step at a time.
2. **`fast` pointer**: Moves two steps at a time.

If the list has a cycle, the `slow` and `fast` pointers will eventually meet inside the cycle. If there’s no cycle,
the `fast` pointer will reach the end of the list.

### **Code Breakdown**

```
def has_cycle(self):
    slow = self.head_node  # Start slow pointer at the head node
    fast = self.head_node  # Start fast pointer at the head node
```
1. **`slow = self.head_node`**:  
   The `slow` pointer starts at the **head node** of the list.

2. **`fast = self.head_node`**:  
   The `fast` pointer also starts at the **head node** of the list.

---

```
while fast and fast.get_next_node():  # Continue as long as fast and next node exist
```
3. **`while fast and fast.get_next_node():`**:  
   The loop continues as long as:
   - `fast` exists (not `None`).
   - `fast.get_next_node()` exists (meaning `fast` isn't at the end of the list yet).

   This condition ensures the loop will terminate if there is no cycle and the list reaches the end (i.e., `fast` becomes `None`).

---

```
slow = slow.get_next_node()  # Move slow pointer one step forward
fast = fast.get_next_node().get_next_node()  # Move fast pointer two steps forward
```
4. **`slow = slow.get_next_node()`**:  
   The `slow` pointer moves **one step forward**.

5. **`fast = fast.get_next_node().get_next_node()`**:  
   The `fast` pointer moves **two steps forward**. It first moves to `fast.get_next_node()` (the next node), then to `fast.get_next_node().get_next_node()` (the node after that).

---

```
if slow == fast:  # If slow and fast meet, there's a cycle
    return True  # Cycle detected
```
6. **`if slow == fast:`**:  
   If the `slow` pointer and the `fast` pointer meet (i.e., point to the same node), this means that both pointers
   have **entered the cycle**. Since the `fast` pointer moves faster than the `slow` pointer, it will eventually
   "catch up" with the `slow` pointer if a cycle exists.

   - If this happens, the method returns **`True`**, indicating that a cycle has been detected.

---

```
return False  # No cycle detected, fast pointer reached the end
```
7. **`return False`**:  
   If the loop finishes (i.e., `fast` reaches the end of the list), this means that there is **no cycle** in the list.
   Therefore, the method returns **`False`**, indicating no cycle.

---

### **Why does this work?**

- The `slow` pointer moves one step at a time, and the `fast` pointer moves two steps at a time. 
- If there’s a cycle, the `fast` pointer will eventually catch up to the `slow` pointer, because the `fast` pointer
is moving faster.
- If there’s no cycle, the `fast` pointer will eventually reach the end of the list, and the method will return `False`.

### **Example Walkthrough**

Let’s walk through an example with a linked list that has a cycle.

### **Linked List:**
```
1 -> 2 -> 3 -> 4 -> 5
          ^         |
          |_________|
```

### **Step-by-Step Detection**

1. **Initial Setup**:  
   - `slow = 1` (head node)
   - `fast = 1` (head node)

2. **First Iteration**:
   - `slow` moves 1 step: `slow = 2`
   - `fast` moves 2 steps: `fast = 3`

3. **Second Iteration**:
   - `slow` moves 1 step: `slow = 3`
   - `fast` moves 2 steps: `fast = 5`

4. **Third Iteration**:
   - `slow` moves 1 step: `slow = 4`
   - `fast` moves 2 steps: `fast = 4`

5. **Cycle Detection**:
   - At this point, `slow` and `fast` both point to node `4`, which means they've **met** inside the cycle. 
   - The method returns `True`, indicating that there is a cycle in the list.

### **Example with No Cycle**

Now, let's try a list with no cycle: `[1, 2, 3, 4, 5]`.

1. **Initial Setup**:  
   - `slow = 1`
   - `fast = 1`

2. **First Iteration**:
   - `slow` moves 1 step: `slow = 2`
   - `fast` moves 2 steps: `fast = 3`

3. **Second Iteration**:
   - `slow` moves 1 step: `slow = 3`
   - `fast` moves 2 steps: `fast = 5`

4. **Third Iteration**:
   - `slow` moves 1 step: `slow = 4`
   - `fast` moves 2 steps: `fast = None` (reached the end of the list)

Since `fast` is now `None`, the loop ends and the method returns **`False`**, indicating that there is no cycle.

### **Summary**

- The `has_cycle` method uses two pointers: `slow` (moves 1 step at a time) and `fast` (moves 2 steps at a time).
- If there’s a cycle, the `fast` pointer will eventually meet the `slow` pointer.
- If the list ends (i.e., `fast` becomes `None`), then there’s no cycle.

# =========================================================================================================================== #

                                                find_cycle_start(self)

This method is used to find the **starting node** of the cycle in a linked list, assuming that a cycle already exists.

### **What does the method do?**

The `find_cycle_start` method is designed to detect where the cycle begins in a linked list. If there is no cycle,
it returns `None`. If there is a cycle, it returns the value of the node where the cycle starts.

### **Code Breakdown**

```
def find_cycle_start(self):
    slow = self.head_node  # Start slow pointer at the head node
    fast = self.head_node  # Start fast pointer at the head node
    cycle_detected = False  # Flag to check if a cycle is detected
```

1. **`slow = self.head_node`**:  
   The `slow` pointer starts at the **head node** of the list.

2. **`fast = self.head_node`**:  
   The `fast` pointer also starts at the **head node**.

3. **`cycle_detected = False`**:  
   A flag `cycle_detected` is initialized to `False`. This flag will be used to determine if a cycle exists in the list.

---

```
while fast and fast.get_next_node():  # Continue as long as fast and next node exist
    slow = slow.get_next_node()  # Move slow pointer one step forward
    fast = fast.get_next_node().get_next_node()  # Move fast pointer two steps forward
    if slow == fast:  # If slow and fast meet, there's a cycle
        cycle_detected = True  # Set cycle_detected to True
        break  # Exit the loop
```

4. **`while fast and fast.get_next_node():`**:  
   The loop runs as long as:
   - `fast` exists (i.e., it's not `None`).
   - `fast.get_next_node()` exists (ensuring `fast` is not at the last node).

   This condition ensures that the loop will terminate if there is no cycle and the `fast` pointer reaches the end of the list.

5. **`slow = slow.get_next_node()`**:  
   The `slow` pointer moves **one step forward**. This means that in each iteration, it advances by 1 node.

6. **`fast = fast.get_next_node().get_next_node()`**:  
   The `fast` pointer moves **two steps forward**. It first moves to `fast.get_next_node()` and then to
   `fast.get_next_node().get_next_node()`.

7. **`if slow == fast:`**:  
   If the `slow` pointer and the `fast` pointer meet (i.e., they point to the same node), this means that
   a **cycle** exists in the list. The two pointers have entered the cycle.

   - If a cycle is detected, the `cycle_detected` flag is set to `True`, and the loop is **broken** to proceed 
   to the next part of the code.

---

```
if not cycle_detected:  # If no cycle was detected
    return None  # Return None indicating no cycle
```

8. **`if not cycle_detected:`**:  
   If the `cycle_detected` flag is still `False`, this means no cycle was found in the list. Therefore, the method
   returns `None`, indicating there is no cycle in the list.

---

```
slow = self.head_node  # Reset slow pointer to the head node
while slow != fast:  # Continue until slow and fast meet at the cycle's start
    slow = slow.get_next_node()  # Move slow pointer one step forward
    fast = fast.get_next_node()  # Move fast pointer one step forward
```

9. **`slow = self.head_node`**:  
   After detecting a cycle, we **reset** the `slow` pointer back to the head node. This is because we want to find
   the **starting point** of the cycle.

10. **`while slow != fast:`**:  
   This loop continues until the `slow` pointer and `fast` pointer meet at the same node, which will be the **start of the cycle**.

   - **Why do we use two pointers?** The idea is that when the `slow` pointer starts from the head of the list and the `fast`
   pointer is already inside the cycle, both pointers will meet at the starting node of the cycle after moving through the list.
   
   - Each pointer moves **one step forward** in this second loop. The `slow` pointer moves one step at a time, and the `fast`
   pointer, which is already inside the cycle, also moves one step at a time.

---

```
return slow.get_value()  # Return the value of the node where the cycle starts
```

11. **`return slow.get_value()`**:  
   Once the `slow` and `fast` pointers meet, they will be at the **starting node** of the cycle. The method then returns
   the **value** of the node where the cycle begins.

### **Why does this work?**

The key idea here is that once a cycle is detected, resetting the `slow` pointer to the head node and moving both
`slow` and `fast` pointers one step at a time will eventually lead them to the **starting node of the cycle**.

Here's why:

- When `slow` and `fast` meet in the cycle, it means they are inside the cycle.
- Resetting `slow` to the head node and moving both pointers at the same speed (one step at a time) ensures that they
will meet at the node where the cycle starts.

### **Example Walkthrough**

Let’s walk through an example with a linked list that has a cycle:

### **Linked List:**
```
1 -> 2 -> 3 -> 4 -> 5
          ^         |
          |_________|
```

1. **First Loop (Cycle Detection)**:

   - `slow` and `fast` start at node `1`.
   - `slow` moves 1 step at a time, `fast` moves 2 steps at a time.
   - Eventually, `slow` and `fast` meet at node `4`, indicating that a cycle exists.

2. **Second Loop (Find Cycle Start)**:

   - We reset `slow` to node `1` and leave `fast` at node `4`.
   - Both `slow` and `fast` move 1 step at a time:
     - `slow` moves from `1` to `2`, then to `3`, then to `4`.
     - `fast` moves from `4` to `5`, then to `1`, and finally to `2`.
   - Eventually, they both meet at node `3`, the **start** of the cycle.

### **Summary**

- The first loop detects if a cycle exists by moving the `slow` and `fast` pointers at different speeds.
- The second loop finds the start of the cycle by resetting `slow` to the head and moving both `slow` and `fast`
pointers one step at a time until they meet at the start of the cycle.

# =========================================================================================================================== #

                                            remove_duplicates(self)

This method is designed to remove **duplicate values** from a linked list. After calling this method, the list will
contain only unique values (i.e., duplicates will be removed).

### **What does the method do?**

The `remove_duplicates` method ensures that all nodes in the linked list contain unique values by iterating through
the list and removing nodes with duplicate values.

### **Code Breakdown**

```
def remove_duplicates(self):
    if not self.head_node:  # If the list is empty, do nothing
        return
```

1. **`if not self.head_node:`**  
   This checks if the linked list is empty by verifying if the **head node** is `None`. If the list is empty, the method
   simply returns because there are no duplicates to remove.

---

```
seen_values = set()  # Set to track the values we've already seen
current_node = self.head_node  # Start from the head node
seen_values.add(current_node.get_value())  # Add the first node's value to the set
```

2. **`seen_values = set()`**  
   We create a `set` called `seen_values` to keep track of the unique values we encounter while traversing the list.
   Sets are used here because they automatically handle duplicates (i.e., they don’t allow duplicate entries).

3. **`current_node = self.head_node`**  
   The `current_node` pointer starts at the **head node** of the list, as this is where we will begin our traversal.

4. **`seen_values.add(current_node.get_value())`**  
   The value of the **head node** is added to the `seen_values` set. This ensures that the first node's value is not removed.

---

```
while current_node.get_next_node():  # Continue as long as there is a next node
    next_node = current_node.get_next_node()  # Get the next node
```

5. **`while current_node.get_next_node():`**  
   This loop will continue as long as the `current_node` has a **next node** (i.e., it hasn't reached the end of the list).

6. **`next_node = current_node.get_next_node()`**  
   `next_node` is a pointer to the **next node** after the `current_node`.
   We will check if the value of `next_node` is a duplicate.

---

```
if next_node.get_value() in seen_values:  # If the value is a duplicate
    current_node.set_next_node(next_node.get_next_node())  # Remove duplicate
```

7. **`if next_node.get_value() in seen_values:`**  
   This checks if the value of the `next_node` is already in the `seen_values` set. If it is, this means
   that the `next_node` has a **duplicate value**, so we need to remove it.

8. **`current_node.set_next_node(next_node.get_next_node())`**  
   This is the key line for removing the duplicate. It updates the `current_node`'s `next` pointer to skip the `next_node`,
   effectively removing it from the list.
   
   - **Before**:  
     `current_node -> next_node -> next_next_node`
   
   - **After**:  
     `current_node -> next_next_node`
   
   The `current_node` now points directly to the node after the `next_node`, thus skipping over the duplicate.

---

```
else:  # If it's not a duplicate, add the value to the set and move to the next node
    seen_values.add(next_node.get_value())  # Add to seen values
    current_node = next_node  # Move current_node to the next node
```

9. **`else:`**  
   If the value of `next_node` is **not** in `seen_values`, it means this is the first time we have encountered this value.
   So, we:
   - Add the `next_node`'s value to the `seen_values` set.
   - Move the `current_node` pointer to the `next_node`, so we can continue checking the next node in the list.

---

### **Why does this work?**

- The `seen_values` set is used to track which values have already been encountered while traversing the list.
If a value appears more than once, it will be removed from the list (by updating the `current_node`'s `next` pointer).

- By updating the `next` pointer, the duplicate node is effectively **skipped** and not included in the final list.
- We only add a value to the set if it has not been seen before, ensuring that only unique values remain.

### **Example Walkthrough**

Let’s walk through an example linked list to see how this works.

### **Linked List:**
```
1 -> 2 -> 3 -> 2 -> 4 -> 1
```

### **Step-by-Step Execution**

1. **Initial Setup**:
   - `seen_values = {}` (empty set)
   - `current_node = 1` (head node)

2. **First Iteration** (current_node = 1):
   - `next_node = 2`
   - `next_node.get_value() = 2` is not in `seen_values`, so:
     - Add `2` to `seen_values`.
     - Move `current_node` to `2`.

   `seen_values = {1, 2}`

3. **Second Iteration** (current_node = 2):
   - `next_node = 3`
   - `next_node.get_value() = 3` is not in `seen_values`, so:
     - Add `3` to `seen_values`.
     - Move `current_node` to `3`.

   `seen_values = {1, 2, 3}`

4. **Third Iteration** (current_node = 3):
   - `next_node = 2`
   - `next_node.get_value() = 2` **is** in `seen_values`, so:
     - Remove `next_node` by updating `current_node.next` to `next_node.next` (skip the duplicate).
     - Don't move `current_node`, as we don't want to advance to the duplicate.

   `seen_values = {1, 2, 3}` (no change in the set)

5. **Fourth Iteration** (current_node = 3):
   - `next_node = 4`
   - `next_node.get_value() = 4` is not in `seen_values`, so:
     - Add `4` to `seen_values`.
     - Move `current_node` to `4`.

   `seen_values = {1, 2, 3, 4}`

6. **Fifth Iteration** (current_node = 4):
   - `next_node = 1`
   - `next_node.get_value() = 1` **is** in `seen_values`, so:
     - Remove `next_node` by updating `current_node.next` to `next_node.next` (skip the duplicate).

   `seen_values = {1, 2, 3, 4}` (no change in the set)

---

### **Final Linked List**:
After all iterations, the linked list looks like this:
```
1 -> 2 -> 3 -> 4
```

Duplicates (the second `2` and `1`) have been removed.

### **Summary**

- The `remove_duplicates` method traverses the list and uses a set to track seen values.
- If it encounters a node with a duplicate value, it skips that node by adjusting the `next` pointer.
- The final result is a linked list with unique values, and the duplicates are removed.

"""
