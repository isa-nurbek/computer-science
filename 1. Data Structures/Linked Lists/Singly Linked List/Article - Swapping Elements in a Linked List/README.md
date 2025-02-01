Swapping elements in a linked list involves updating the links between nodes rather than swapping the data directly (though you can swap data if that's simpler). Here's how it works in detail, along with examples in Python:

---

## **Concept of Swapping in a Linked List**

### **Key Points:**

1. A **linked list** is made of nodes where each node contains data and a reference (or pointer) to the next node.
2. Swapping elements can mean:
    - Swapping the **data** between two nodes.
    - Swapping the **nodes themselves**, which involves changing their pointers.

### **Steps for Swapping Nodes:**

1. **Identify the nodes to swap**:
    - Traverse the list to find the nodes containing the values to swap (`node1` and `node2`).
2. **Handle pointers**:
    - If swapping nodes, update the `next` pointers of their respective previous nodes to point to the opposite node.
3. **Edge cases**:
    - If either node is the `head` or `tail` of the list.
    - If the nodes are adjacent.
    - If one or both nodes don't exist in the list.

---

### **Implementation: Swapping Nodes**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def swap_nodes(self, x, y):
        # If x and y are the same, no need to swap
        if x == y:
            return

        # Find nodes with values x and y
        prevX, currX = None, self.head
        while currX and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY, currY = None, self.head
        while currY and currY.data != y:
            prevY = currY
            currY = currY.next

        # If either x or y is not present, return
        if not currX or not currY:
            print(f"Cannot swap: one or both elements ({x}, {y}) not found.")
            return

        # If x is not head, update prevX's next
        if prevX:
            prevX.next = currY
        else:  # Else make y the new head
            self.head = currY

        # If y is not head, update prevY's next
        if prevY:
            prevY.next = currX
        else:  # Else make x the new head
            self.head = currX

        # Swap next pointers
        currX.next, currY.next = currY.next, currX.next

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original List:")
ll.display()

# Swap nodes with values 2 and 4
ll.swap_nodes(2, 4)
print("\nList after swapping 2 and 4:")
ll.display()

# Swap head and tail nodes (1 and 5)
ll.swap_nodes(1, 5)
print("\nList after swapping 1 and 5:")
ll.display()
```

---

### **Output of the Example**

1. **Original List**:  
   `1 -> 2 -> 3 -> 4 -> 5 -> None`

2. **After swapping 2 and 4**:  
   `1 -> 4 -> 3 -> 2 -> 5 -> None`

3. **After swapping 1 and 5**:  
   `5 -> 4 -> 3 -> 2 -> 1 -> None`

---

### **Explanation of the Code**

This code defines a **singly linked list** with functionality to add elements, display the list, and swap two nodes based on their values.

---

### **1. Node Class**

The `Node` class represents an individual element (node) in the linked list. Each node contains:

-   `data`: Stores the value of the node.
-   `next`: A reference (pointer) to the next node in the list. Initialized to `None`.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

### **2. LinkedList Class**

The `LinkedList` class manages the linked list. It contains:

-   `self.head`: Points to the first node in the list (or `None` if the list is empty).

#### **Constructor**

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

When a `LinkedList` object is created, `self.head` is initialized to `None`, indicating an empty list.

---

### **3. append(data) Method**

Adds a new node with the specified `data` to the **end** of the list.

1. A new node is created using the `Node` class.
2. If the list is empty (`self.head` is `None`), the new node becomes the `head`.
3. Otherwise, the method traverses the list to find the last node and updates its `next` pointer to the new node.

**Example**:

```python
ll = LinkedList()
ll.append(1)  # Creates the first node, head points to Node(1)
ll.append(2)  # Adds Node(2) after Node(1)
```

---

### **4. display() Method**

Prints the elements of the linked list in a readable format.

-   Starts from the `head` and traverses the list, printing the `data` of each node.
-   Stops when it reaches a node with `next = None`.

---

### **5. swap_nodes(x, y) Method**

Swaps two nodes with values `x` and `y` **without swapping the data directly**.

#### **Steps to Swap Nodes**

1. **Check if x and y are the same**:
   If `x == y`, no swap is needed, and the method returns immediately.

2. **Locate x and y in the list**:

    - Use two pointer pairs (`prevX, currX` for `x` and `prevY, currY` for `y`) to find the target nodes and their preceding nodes.

    ```python
    while currX and currX.data != x:
        prevX = currX
        currX = currX.next
    ```

    If `x` or `y` is not found, the method prints an error message and exits.

3. **Update pointers for swapping**:

    - **Adjust the preceding nodes**:

        - If `prevX` is not `None`, point it to `currY`. If `x` is the `head`, update the `head` to `currY`.
        - Similarly, adjust `prevY` to point to `currX`.

    - **Swap `next` pointers**:
      Exchange the `next` pointers of `currX` and `currY`.

    ```python
    currX.next, currY.next = currY.next, currX.next
    ```

---

### **Example Usage**

#### **Creating the List**

```python
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
```

The list is now:

```
1 -> 2 -> 3 -> 4 -> 5 -> None
```

#### **Swapping Nodes with Values 2 and 4**

1. Locate `2` (`currX`) and `4` (`currY`), along with their preceding nodes `1` (`prevX`) and `3` (`prevY`).
2. Adjust pointers:
    - `prevX.next = currY` and `prevY.next = currX`.
    - Swap `currX.next` and `currY.next`.

After swapping:

```
1 -> 4 -> 3 -> 2 -> 5 -> None
```

#### **Swapping Head (1) and Tail (5)**

1. Locate `1` (`currX`) and `5` (`currY`), with `None` as `prevX` and `4` as `prevY`.
2. Adjust pointers:
    - Update `head` to `currY` (`5`).
    - `prevY.next = currX`.
    - Swap `currX.next` and `currY.next`.

After swapping:

```
5 -> 4 -> 3 -> 2 -> 1 -> None
```

---

### **Key Points**

-   The method avoids swapping data directly, which is a good practice when the node structure may contain more fields or constraints.
-   The code handles edge cases like swapping the `head`, the `tail`, or nodes not present in the list.

---

### **Alternative: Swapping Data Only**

If you only need to swap values and not the nodes themselves:

```python
def swap_data(self, x, y):
    nodeX, nodeY = None, None
    current = self.head

    # Find nodes with values x and y
    while current:
        if current.data == x:
            nodeX = current
        if current.data == y:
            nodeY = current
        current = current.next

    # If both nodes are found, swap their data
    if nodeX and nodeY:
        nodeX.data, nodeY.data = nodeY.data, nodeX.data
    else:
        print(f"Cannot swap: one or both elements ({x}, {y}) not found.")
```

This approach is simpler but doesn't change the structure of the linked list, only the data.

### **Explanation of the Code**

This code snippet is a method called `swap_data` that swaps the data of two nodes in a **singly linked list**, given the values `x` and `y` to swap. Here's a detailed explanation of how it works:

---

### Key Points:

1. **Purpose:**

    - The method swaps the **data** of the nodes in a singly linked list that contain the specified values `x` and `y`.

2. **Variables:**

    - `nodeX` and `nodeY`: Pointers to store references to the nodes containing `x` and `y`.
    - `current`: A pointer used to traverse the linked list, starting from the head.

3. **Steps:**

    #### 1. Initialize `nodeX` and `nodeY`:

    - Both are set to `None` initially. They will later store the nodes containing the values `x` and `y`, if found.

    #### 2. Traverse the linked list to find the nodes containing `x` and `y`:

    - The `while` loop iterates through the linked list, checking each node's `data` value:
        - If `current.data == x`, `nodeX` is set to the current node.
        - If `current.data == y`, `nodeY` is set to the current node.
    - The traversal continues until the end of the list (`current` becomes `None`).

    #### 3. Check if both nodes were found:

    - If both `nodeX` and `nodeY` are non-`None`, it means nodes containing `x` and `y` were found.

    #### 4. Swap the `data` fields of the nodes:

    - `nodeX.data, nodeY.data = nodeY.data, nodeX.data` swaps the `data` values of the two nodes.

    #### 5. Handle missing nodes:

    - If either `nodeX` or `nodeY` is still `None`, the method prints an error message stating that one or both elements could not be found, and the swap is not performed.

---

### Code Execution Flow Example:

#### Example Linked List:

-   Suppose the list is: `10 -> 20 -> 30 -> 40 -> 50`

#### Input:

-   `x = 20`, `y = 50`

#### Execution:

1. **Traverse the list**:

    - The method starts at the `head` and iterates through the list:
        - When `current.data == 20`, `nodeX` is set to the node with value `20`.
        - When `current.data == 50`, `nodeY` is set to the node with value `50`.

2. **Check if nodes are found**:

    - Both `nodeX` and `nodeY` are non-`None`.

3. **Swap data**:
    - `nodeX.data` becomes `50`, and `nodeY.data` becomes `20`.

#### Result:

-   The updated list becomes: `10 -> 50 -> 30 -> 40 -> 20`

---

### Notes:

1. **Data Swap vs. Node Swap:**

    - This method swaps only the **data** values of the nodes, not the actual nodes themselves.
    - The structure and order of the linked list remain unchanged.

2. **Edge Cases:**

    - If either `x` or `y` is not in the list, the method prints an error message and does nothing.

3. **Efficiency:**
    - The method requires only a single traversal of the list, making its time complexity **O(n)**, where `n` is the number of nodes in the list.
