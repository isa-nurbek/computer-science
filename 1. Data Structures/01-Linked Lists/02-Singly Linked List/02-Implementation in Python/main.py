# Node class represents a single node in the linked list
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


# LinkedList class manages a collection of nodes
class LinkedList:
    # Initialize a new linked list with an optional starting value
    def __init__(self, value=None):
        self.head_node = Node(value)

    # Return the first node in the list
    def get_head_node(self):
        return self.head_node

    # Add a new node at the beginning of the list
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)  # Link new node to current head
        self.head_node = new_node  # Update head to new node

    # Add a new node at the end of the list
    def insert_end(self, value):
        new_node = Node(value)
        # Handle empty list case
        if self.head_node is None:
            self.head_node = new_node
            return

        # Find the last node in the list
        current_node = self.head_node
        while current_node.get_next_node() is not None:
            current_node = current_node.get_next_node()

        # Link the last node to our new node
        current_node.set_next_node(new_node)

    # Remove the first occurrence of a node with the specified value
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()

        # Special case: removing head node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            # Traverse list looking for the value to remove
            while current_node:
                next_node = current_node.get_next_node()
                if next_node and next_node.get_value() == value_to_remove:
                    current_node.set_next_node(
                        next_node.get_next_node()
                    )  # Skip over the removed node
                    current_node = None  # Exit the loop
                else:
                    current_node = next_node

    # Convert the linked list to a string representation
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        # Traverse the list and build string representation
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()

        return string_list


# Test the LinkedList implementation
ll = LinkedList("D")  # Create new list with 'D' as head
ll.insert_beginning("C")  # Add 'C' to the beginning
ll.insert_beginning("B")  # Add 'B' to the beginning
ll.insert_beginning("A")  # Add 'A' to the beginning
print(ll.stringify_list())  # Print the list: A->B->C->D

ll.remove_node("B")  # Remove node with value 'B'
print(ll.stringify_list())  # Print the modified list: A->C->D


# Big O:

"""

### Time and Space Complexity Analysis

Let's break down the time and space complexity of the key operations in the `LinkedList` class:

#### 1. **Insert at the Beginning (`insert_beginning`)**
   - **Time Complexity:** O(1)
     - Inserting at the beginning of the linked list involves creating a new node and updating the `head_node` reference.
     This operation is constant time because it doesn't depend on the size of the list.
   - **Space Complexity:** O(1)
     - The space required is constant because we only create a single new node, regardless of the size of the list.

#### 2. **Insert at the End (`insert_end`)**
   - **Time Complexity:** O(n)
     - Inserting at the end of the linked list requires traversing the entire list to find the last node. This operation
     takes linear time because it depends on the number of nodes in the list.
   - **Space Complexity:** O(1)
     - The space required is constant because we only create a single new node, regardless of the size of the list.

#### 3. **Remove a Node (`remove_node`)**
   - **Time Complexity:** O(n)
     - Removing a node involves traversing the list to find the node with the specified value. In the worst case, this
     operation takes linear time because it may need to traverse the entire list.
   - **Space Complexity:** O(1)
     - The space required is constant because we only need a few pointers to manage the removal, regardless of the size of the list.

#### 4. **Convert to String (`stringify_list`)**
   - **Time Complexity:** O(n)
     - Converting the linked list to a string involves traversing the entire list to build the string representation.
     This operation takes linear time because it depends on the number of nodes in the list.
   - **Space Complexity:** O(n)
     - The space required is linear because the string representation grows with the number of nodes in the list.

### Summary of Complexities

| Operation            | Time Complexity | Space Complexity |
|----------------------|-----------------|------------------|
| `insert_beginning`   | O(1)            | O(1)             |
| `insert_end`         | O(n)            | O(1)             |
| `remove_node`        | O(n)            | O(1)             |
| `stringify_list`     | O(n)            | O(n)             |

### Example Walkthrough

Given the test code:
```
ll = LinkedList("D")  # Create new list with 'D' as head
ll.insert_beginning("C")  # Add 'C' to the beginning
ll.insert_beginning("B")  # Add 'B' to the beginning
ll.insert_beginning("A")  # Add 'A' to the beginning
print(ll.stringify_list())  # Print the list: A->B->C->D

ll.remove_node("B")  # Remove node with value 'B'
print(ll.stringify_list())  # Print the modified list: A->C->D
```

- **Initial List Construction:**
  - `insert_beginning("C")`, `insert_beginning("B")`, and `insert_beginning("A")` each take O(1) time.
  - The list becomes `A -> B -> C -> D`.

- **Removing Node "B":**
  - `remove_node("B")` takes O(n) time in the worst case (traversing the list to find "B").
  - The list becomes `A -> C -> D`.

- **Printing the List:**
  - `stringify_list()` takes O(n) time and O(n) space to build the string representation.

### Conclusion
The linked list implementation provided has efficient O(1) insertion at the beginning and O(n) insertion at the end,
removal, and string conversion. The space complexity is generally O(1) for modifications and O(n) for the string representation.

"""

# ******************************************************************************************************************************** #

# Code Explanation:

"""
                                                *** __init__() method: ***

# Code:

```
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
```

This line of code is from the constructor method (`__init__`) of the `LinkedList` class. Let’s break it down step by step:

### **Purpose of the Constructor (`__init__`)**
- The constructor initializes a new linked list object.
- When you create a new `LinkedList` instance, this method is called automatically.

---

### **Key Components of the Line**
```
self.head_node = Node(value)
```
- **`self`**:
  - Refers to the specific instance of the `LinkedList` class being created.
  - `self.head_node` is an attribute of the `LinkedList` instance. It represents the first node (head) in the linked list.
  
- **`Node(value)`**:
  - This creates a new `Node` object with the specified `value`.
  - The `Node` class constructor (`Node.__init__`) expects a value (`value`) and optionally a `next_node` reference (default is `None`).
  - For example:
    ```
    Node("A")  # Creates a node with value "A" and no next node.
    ```
  
- **`self.head_node = Node(value)`**:
  - Assigns the newly created `Node` object to `self.head_node`.
  - This means the linked list starts with one node, and its value is set to `value`.

---

### **Behavior Based on the Input**
#### 1. **When `value` is Provided**
If you initialize the linked list with a value:
```
ll = LinkedList("A")
```
- `Node("A")` is created.
- `self.head_node` is set to this new node.
- The linked list now contains one node:
  ```
  Head -> A
  ```

#### 2. **When `value` is `None` (Default)**
If you don't provide a value:
```
ll = LinkedList()
```
- `Node(None)` is created.
- `self.head_node` is set to this node.
- The linked list contains one node, but the value is `None`:
  ```
  Head -> None
  ```

---

### **Why Initialize `head_node` with a `Node`?**
- A linked list requires a starting point, known as the **head node**.
- Even if the list starts empty (`value=None`), it’s useful to have a placeholder node, which simplifies further operations like insertion.

---

### **Illustration of the Process**
Let’s visualize:

#### When `LinkedList("A")` is created:
1. The `__init__` method is called with `value="A"`.
2. A new `Node` is created:
   ```
   Node(value="A", next_node=None)
   ```
3. This node becomes the `head_node`.

Resulting structure:
```
LinkedList:
Head -> A
```

#### When `LinkedList()` is created:
1. The `__init__` method is called with `value=None`.
2. A new `Node` is created:
   ```
   Node(value=None, next_node=None)
   ```
3. This node becomes the `head_node`.

Resulting structure:
```
LinkedList:
Head -> None
```

---

### Summary
```
self.head_node = Node(value)
```
- Creates the first node of the linked list (`head_node`) with the given value (`value`).
- If no value is provided, the list starts with a single node containing `None`.

*********************************************************************************************************************************

                                            *** insert_beginning() method: ***

# Code:

```
def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node) 
    self.head_node = new_node  
```

This is the `insert_beginning` method from the `LinkedList` class. Its purpose is to add a new node to the **beginning** of
the linked list. Let's break it down step by step:

---

### **Method Purpose**
The method inserts a new node with a given value (`new_value`) at the start of the linked list, making it the new **head node**.

---

### **Breaking Down the Code**

#### 1. **Creating a New Node**
```
new_node = Node(new_value)
```
- **`Node(new_value)`**:
  - This creates a new `Node` object with the value `new_value`.
  - The `next_node` attribute of this new node is `None` by default (as per the `Node` class constructor).

For example:
```
new_node = Node("A")
```
creates a new node:
```
Node("A")  ->  None
```

---

#### 2. **Setting the Next Node for the New Node**
```
new_node.set_next_node(self.head_node)
```
- **`self.head_node`**:
  - Refers to the current head node of the linked list (before adding the new node).
- **`new_node.set_next_node(self.head_node)`**:
  - Updates the `next_node` reference of the new node to point to the current head node.
  - This ensures the new node is linked to the rest of the list.

For example:
- Suppose the linked list looks like this:
  ```
  Head -> B -> C -> D
  ```
- After:
  ```
  new_node.set_next_node(self.head_node)
  ```
  The new node now points to the current head:
  ```
  New Node ("A") -> B -> C -> D
  ```

---

#### 3. **Updating the Head Node**
```
self.head_node = new_node
```
- This makes the new node the new **head node** of the linked list.
- The linked list structure is updated, so the new node is now the first node in the list.

For example:
- After this step, the list looks like:
  ```
  Head -> A -> B -> C -> D
  ```

---

### **Putting It All Together**
Here’s what happens step by step when `insert_beginning("A")` is called:

1. **Create a New Node (`new_node`)**:
   - A new node with value `"A"` is created.
   - Initially, it looks like:
     ```
     Node("A") -> None
     ```

2. **Link the New Node to the Current Head**:
   - The `next_node` of `new_node` is set to the current head node (`B`).
   - Now:
     ```
     Node("A") -> B -> C -> D
     ```

3. **Update the Head**:
   - The `head_node` of the linked list is updated to point to `new_node`.
   - The linked list now starts with the new node:
     ```
     Head -> A -> B -> C -> D
     ```

---

### **Example**

#### Initial State:
Linked list:
```
Head -> B -> C -> D
```

#### Code Execution:
```
ll.insert_beginning("A")
```

#### After Execution:
Linked list:
```
Head -> A -> B -> C -> D
```

---

### **Why Each Step is Necessary**
1. **Create a New Node**:
   - The new value must be stored in a node object to integrate it into the list.

2. **Set the Next Node**:
   - The new node needs to point to the rest of the list so that the chain of nodes remains intact.

3. **Update the Head Node**:
   - The new node becomes the first node, so the `head_node` must be updated.

---

### **Summary**
The `insert_beginning` method:
1. Creates a new node with the given value.
2. Links this new node to the current head node of the list.
3. Updates the `head_node` to point to the new node, making it the first node in the list.

*********************************************************************************************************************************

                                            *** insert_end() method: ***

# Code:

```
def insert_end(self, value):
    new_node = Node(value)
    if self.head_node is None:
        self.head_node = new_node
        return

    current_node = self.head_node
    while current_node.get_next_node() is not None:
        current_node = current_node.get_next_node()

    current_node.set_next_node(new_node) 
```

This method, `insert_end`, is part of the `LinkedList` class. Its purpose is to add a new node with a specified value (`value`)
at the **end** of the linked list. Let’s break it down step by step.

---

### **Method Purpose**
- Adds a new node with the given value to the end of the linked list.
- If the list is empty, the new node becomes the head node.

---

### **Code Breakdown**

#### 1. **Create a New Node**
```
new_node = Node(value)
```
- This creates a new instance of the `Node` class with the specified `value`.
- By default, the `next_node` attribute of the new node is `None` (as per the `Node` class constructor).

For example:
```
new_node = Node("A")
```
creates a node:
```
Node("A") -> None
```

---

#### 2. **Check if the List is Empty**
```
if self.head_node is None:
    self.head_node = new_node
    return
```
- **`self.head_node`**:
  - Refers to the first node in the list.
- **If `self.head_node is None`**:
  - The list is empty (no nodes exist yet).
- **Set `self.head_node` to `new_node`**:
  - The new node becomes the first (and only) node in the list.
- **`return`**:
  - Ends the method because the node has been inserted, and no further steps are needed.

For example:
- Before insertion:
  ```
  Head -> None
  ```
- After:
  ```
  Head -> A
  ```

---

#### 3. **Traverse to the Last Node**
```
current_node = self.head_node
while current_node.get_next_node() is not None:
    current_node = current_node.get_next_node()
```
- If the list is not empty, this part of the code finds the last node in the list.
- **`current_node`**:
  - Starts as the head node.
- **`current_node.get_next_node()`**:
  - Returns the reference to the next node in the list.
- **While Loop**:
  - Continues moving to the next node until `get_next_node()` returns `None`, indicating the current node is the last node.

For example:
- Consider the list:
  ```
  Head -> A -> B -> C
  ```
- Initially, `current_node` points to `A`.
- The loop updates `current_node` to point to `B`, then `C`, and stops when it reaches `C` (because `C.get_next_node()` is `None`).

---

#### 4. **Set the Last Node’s `next_node`**
```
current_node.set_next_node(new_node)
```
- **`current_node`**:
  - At this point, `current_node` refers to the last node in the list.
- **`set_next_node(new_node)`**:
  - Updates the `next_node` of the current last node to point to the new node.
  - This adds the new node to the end of the list.

For example:
- Before:
  ```
  Head -> A -> B -> C
  ```
- After adding `D`:
  ```
  Head -> A -> B -> C -> D
  ```

---

### **Example Execution**
Let’s say we have the following initial list:
```
Head -> A -> B
```

#### Code Execution:
```
ll.insert_end("C")
```

**Step 1**: Create a new node:
```
new_node = Node("C")
```
The new node:
```
Node("C") -> None
```

**Step 2**: Check if the list is empty:
- `self.head_node` is not `None` (the head is `A`), so skip this step.

**Step 3**: Traverse to the last node:
- Start at `A` (`current_node = self.head_node`).
- Move to `B` (`current_node = current_node.get_next_node()`).
- Stop at `B` because `B.get_next_node()` is `None`.

**Step 4**: Add the new node:
- Update `B`’s `next_node`:
  ```
  current_node.set_next_node(new_node)
  ```

Final list:
```
Head -> A -> B -> C
```

---

### **Why Each Step is Necessary**
1. **Create a New Node**:
   - The new value must be stored in a node object.

2. **Check if the List is Empty**:
   - Handles the edge case where no nodes exist in the list.

3. **Traverse to the Last Node**:
   - Ensures the new node is added to the very end of the list.

4. **Set the Last Node’s `next_node`**:
   - Links the new node to the end of the list.

---

### **Summary**
The `insert_end` method works as follows:
1. Creates a new node with the specified value.
2. If the list is empty, the new node becomes the head node.
3. Otherwise, it traverses the list to find the last node.
4. Updates the last node’s `next_node` to point to the new node, appending it to the end of the list.

*********************************************************************************************************************************

                                            *** remove_node() method: ***

# Code:

```
def remove_node(self, value_to_remove):
    current_node = self.get_head_node()

    if current_node.get_value() == value_to_remove:
        self.head_node = current_node.get_next_node()
    else:
        while current_node:
            next_node = current_node.get_next_node()
            if next_node and next_node.get_value() == value_to_remove:
                current_node.set_next_node(
                    next_node.get_next_node()
                )  
                current_node = None  
            else:
                current_node = next_node
```

This method, `remove_node`, removes the first occurrence of a node with a specified value (`value_to_remove`) from the linked list.
Let’s break it down step by step to understand how it works.

---

### **Method Purpose**
The method finds a node with the specified value (`value_to_remove`) in the linked list and removes it while maintaining the integrity of the linked list.

---

### **Code Breakdown**

#### 1. **Get the Head Node**
```
current_node = self.get_head_node()
```
- **`self.get_head_node()`**:
  - Retrieves the head node of the linked list.
- **`current_node`**:
  - Starts as the head node and will be used to traverse the list.

For example:
- Given a list:
  ```
  Head -> A -> B -> C -> D
  ```
  `current_node` initially refers to `A` (the head node).

---

#### 2. **Check if the Head Node Matches the Value**
```
if current_node.get_value() == value_to_remove:
    self.head_node = current_node.get_next_node()
```
- **`current_node.get_value()`**:
  - Returns the value stored in the current node.
- **If the head node matches `value_to_remove`**:
  - Update the `head_node` to point to the next node, effectively removing the head node.
- This handles the special case where the node to be removed is the head.

For example:
- Removing `A` from the list:
  ```
  Head -> A -> B -> C -> D
  ```
  After:
  ```
  Head -> B -> C -> D
  ```

---

#### 3. **Traverse the List to Find the Node**
```
else:
    while current_node:
        next_node = current_node.get_next_node()
        ...
```
- **`while current_node`**:
  - Continues traversing the list until it reaches the end (`current_node` becomes `None`).
- **`next_node = current_node.get_next_node()`**:
  - Gets a reference to the next node in the list.
  - This allows checking the value of the next node and updating pointers as needed.

For example:
- Start with `current_node = A`:
  ```
  A -> B -> C -> D
  ```
- `next_node` is set to `B`.

---

#### 4. **Check if the Next Node Matches the Value**
```
if next_node and next_node.get_value() == value_to_remove:
```
- **`next_node.get_value()`**:
  - Checks if the next node contains the value to be removed.
- **If `next_node` matches `value_to_remove`**:
  - The node after `current_node` is the one to be removed.

For example:
- To remove `C`:
  ```
  A -> B -> C -> D
  ```
  When `current_node = B`, `next_node = C`, and `C.get_value() == value_to_remove`.

---

#### 5. **Remove the Node**
```
current_node.set_next_node(next_node.get_next_node())
```
- **`current_node.set_next_node(next_node.get_next_node())`**:
  - Updates the `next_node` of `current_node` to skip over the node to be removed.
  - This effectively removes `next_node` from the list.

For example:
- Removing `C`:
  ```
  A -> B -> C -> D
  ```
  Update `B`’s `next_node` to point to `D`:
  ```
  A -> B -> D
  ```

---

#### 6. **Stop Traversal After Removing**
```
current_node = None
```
- **`current_node = None`**:
  - Stops the loop because the node has been removed. No further traversal is needed.

---

#### 7. **Continue Traversal If No Match**
```
else:
    current_node = next_node
```
- If the current `next_node` does not match `value_to_remove`, move `current_node` to the next node and continue traversing.

For example:
- Removing `D`:
  ```
  A -> B -> C -> D
  ```
  The loop continues until `current_node = C` and `next_node = D`.

---

### **Example Execution**

#### Given List:
```
Head -> A -> B -> C -> D
```

#### Removing `C`:
```
ll.remove_node("C")
```

1. **Initial Setup**:
   - `current_node = A`.

2. **Head Node Check**:
   - `A.get_value() != "C"`, so move to the `else` block.

3. **Traverse the List**:
   - `current_node = A`, `next_node = B`. No match, continue.
   - `current_node = B`, `next_node = C`. Match found.

4. **Remove the Node**:
   - `B.set_next_node(C.get_next_node())`.
   - `B`’s `next_node` now points to `D`.

5. **Stop Traversal**:
   - `current_node = None`.

#### Resulting List:
```
Head -> A -> B -> D
```

---

### **Key Points**
1. **Edge Case (Head Node Removal)**:
   - If the node to remove is the head, update `self.head_node` to point to the next node.

2. **Traversal**:
   - Iterate through the list, checking the value of each node’s `next_node`.

3. **Remove the Node**:
   - Update the `next_node` reference of the current node to skip the node being removed.

---

### **Summary**
The `remove_node` method:
1. Checks if the head node matches the value to remove.
2. If not, traverses the list while checking each `next_node`.
3. When a match is found, updates the `next_node` of the preceding node to skip over the matched node,
effectively removing it from the list.

*********************************************************************************************************************************

                                             *** stringify_list() method: ***

# Code:

```
def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
        if current_node.get_value() is not None:
            string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()

    return string_list
```

This method, `stringify_list`, is part of the `LinkedList` class. Its purpose is to traverse the linked list and
build a string representation of the list’s elements. Here’s a detailed explanation of how it works:

---

### **Method Purpose**
- The method creates a string containing the values of all nodes in the linked list, each separated by a newline (`\n`).
- It iterates through the list, appending the value of each node to the string.

---

### **Breaking Down the Code**

#### 1. **Initialize an Empty String**
```
string_list = ""
```
- **`string_list`**:
  - This variable will hold the concatenated values of all nodes as a string.

For example:
- Initially:
  ```
  string_list = ""
  ```

---

#### 2. **Start Traversal from the Head Node**
```
current_node = self.get_head_node()
```
- **`self.get_head_node()`**:
  - Retrieves the first node (head) of the linked list.
- **`current_node`**:
  - A pointer used to traverse the list. It starts at the head and moves to the next node in each iteration.

For example:
- For a list:
  ```
  Head -> A -> B -> C
  ```
  `current_node` initially refers to `A`.

---

#### 3. **Traverse the Linked List**
```
while current_node:
```
- **`while current_node`**:
  - The loop continues as long as `current_node` is not `None`.
  - This ensures that the method processes every node in the list.

For example:
- For a list:
  ```
  Head -> A -> B -> C
  ```
  The loop will iterate through nodes `A`, `B`, and `C`, stopping when `current_node` becomes `None`.

---

#### 4. **Check if the Current Node Has a Value**
```
if current_node.get_value() is not None:
```
- **`current_node.get_value()`**:
  - Retrieves the value of the current node.
- **`is not None`**:
  - Ensures that the node’s value is not `None` before appending it to the string.
- This check is useful because some linked list implementations allow nodes to exist without meaningful values.

---

#### 5. **Append the Value to the String**
```
string_list += str(current_node.get_value()) + "\n"
```
- **`str(current_node.get_value())`**:
  - Converts the value of the current node to a string.
- **`string_list += ...`**:
  - Appends the value to `string_list`, followed by a newline character (`\n`).

For example:
- If `current_node.get_value()` is `"A"`, after this step:
  ```
  string_list = "A\n"
  ```

---

#### 6. **Move to the Next Node**
```
current_node = current_node.get_next_node()
```
- **`current_node.get_next_node()`**:
  - Retrieves the reference to the next node in the list.
- **`current_node = ...`**:
  - Updates `current_node` to point to the next node for the next iteration of the loop.

For example:
- If the current list is:
  ```
  Head -> A -> B -> C
  ```
  - After processing `A`, `current_node` is updated to point to `B`.

---

#### 7. **Return the Final String**
```
return string_list
```
- After the loop completes (i.e., when `current_node` is `None`), the method returns the concatenated string of all node values.

---

### **Example Execution**

#### Given Linked List:
```
Head -> A -> B -> C
```

#### Code Execution:
```
ll.stringify_list()
```

1. **Initial Setup**:
   - `string_list = ""`.
   - `current_node = Head` (node `A`).

2. **First Iteration**:
   - `current_node.get_value()` is `"A"`.
   - Append `"A\n"` to `string_list`:
     ```
     string_list = "A\n"
     ```
   - Move to the next node: `current_node = B`.

3. **Second Iteration**:
   - `current_node.get_value()` is `"B"`.
   - Append `"B\n"` to `string_list`:
     ```
     string_list = "A\nB\n"
     ```
   - Move to the next node: `current_node = C`.

4. **Third Iteration**:
   - `current_node.get_value()` is `"C"`.
   - Append `"C\n"` to `string_list`:
     ```
     string_list = "A\nB\nC\n"
     ```
   - Move to the next node: `current_node = None`.

5. **End of Loop**:
   - The loop exits because `current_node` is `None`.

6. **Return the Result**:
   - The method returns:
     ```
     "A\nB\nC\n"
     ```

---

### **Key Points**
1. **String Concatenation**:
   - Each node’s value is appended to `string_list`, followed by a newline character.

2. **Traversal**:
   - The method uses `current_node` to traverse the linked list from the head to the last node.

3. **Termination**:
   - The loop ends when `current_node` becomes `None`, indicating the end of the list.

---

### **Summary**
The `stringify_list` method:
1. Starts at the head node of the linked list.
2. Iterates through each node, appending its value to a string with a newline.
3. Stops when all nodes have been processed.
4. Returns the final string, representing the linked list’s contents.

"""
