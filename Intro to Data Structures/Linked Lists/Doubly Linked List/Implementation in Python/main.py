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

# Big O:

"""

Let's analyze the **time and space complexity** of the **DoublyLinkedList** operations.

---

### **1. `add_to_head(new_value)` & `add_to_tail(new_value)`**
- These operations create a new node and adjust a few pointers.
- **Time Complexity:** O(1) (Constant time, as only a few pointer changes are required)
- **Space Complexity:** O(1) (No extra space except for the new node)

---

### **2. `insert(pos, new_value)`**
- If inserting at the head: O(1).
- If inserting at an arbitrary position:
  - In the worst case, we traverse O(n) elements.
  - The insertion itself (pointer adjustments) takes O(1).
- **Time Complexity:** O(n) (Worst case: inserting at the end)
- **Space Complexity:** O(1) (Only a new node is added)

---

### **3. `remove_head()` & `remove_tail()`**
- These operations adjust a few pointers and return a value.
- **Time Complexity:** O(1) (No traversal required)
- **Space Complexity:** O(1) (No extra space used)

---

### **4. `remove_by_value(value_to_remove)`**
- In the worst case, we traverse the entire list if the value is at the end or not present.
- Removing the node itself takes O(1) (pointer changes).
- **Time Complexity:** O(n) (Worst case: searching the entire list)
- **Space Complexity:** O(1) (No extra space used)

---

### **5. `stringify_list()`**
- Traverses the entire list and builds a string.
- **Time Complexity:** O(n) (Iterating through all elements)
- **Space Complexity:** O(n) (Storing the output string)

---

### **Overall Summary**

| Operation                     | Time Complexity    | Space Complexity |
|-------------------------------|--------------------|------------------|
| add_to_head() / add_to_tail() |  O(1)              |  O(1)            |
| insert(pos, value)            |  O(n) (worst case) |  O(1)            |
| remove_head() / remove_tail() |  O(1)              |  O(1)            |
| remove_by_value(value)        |  O(n) (worst case) |  O(1)            |
| stringify_list()              |  O(n)              |  O(n)            |

The **space complexity remains O(1) for most operations** since we do not allocate extra memory
apart from the new nodes themselves.

"""
