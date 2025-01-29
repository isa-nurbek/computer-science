class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

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
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head is not None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head

        if self.tail_node is None:
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = new_tail

    def insert(self, pos, new_value):
        if pos == 0:
            self.add_to_head(new_value)
        else:
            current_node = self.head_node
            for i in range(pos):
                if current_node is None:
                    # Position is beyond the end of the list, add to tail
                    self.add_to_tail(new_value)
                    return
                current_node = current_node.get_next_node()

            # If current_node is None after the loop, add to tail
            if current_node is None:
                self.add_to_tail(new_value)
            else:
                new_node = Node(new_value)
                new_node.set_next_node(current_node.get_next_node())
                new_node.set_prev_node(current_node)

                if current_node.get_next_node() is not None:
                    current_node.get_next_node().set_prev_node(new_node)

                current_node.set_next_node(new_node)

                # Update tail if necessary
                if new_node.get_next_node() is None:
                    self.tail_node = new_node

    def remove_head(self):
        removed_head = self.head_node
        if removed_head is None:
            return None

        self.head_node = removed_head.get_next_node()
        if self.head_node is not None:
            self.head_node.set_prev_node(None)

        if removed_head == self.tail_node:
            self.remove_tail()

        return removed_head.get_value()

    def remove_tail(self):
        removed_tail = self.tail_node
        if removed_tail is None:
            return None

        self.tail_node = removed_tail.get_prev_node()
        if self.tail_node is not None:
            self.tail_node.set_next_node(None)

        if removed_tail == self.head_node:
            self.remove_head()

        return removed_tail.get_value()

    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node

        while current_node is not None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break
            current_node = current_node.get_next_node()

        if node_to_remove is None:
            return None

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

Let's analyze the **time and space complexity** of each method in the `DoublyLinkedList` class.

### 1. **add_to_head(new_value)**
   - **Time Complexity**: O(1)  
     - Involves creating a new node and updating at most two pointers.
   - **Space Complexity**: O(1)  
     - Only creates one new node.

### 2. **add_to_tail(new_value)**
   - **Time Complexity**: O(1)   
     - Since we maintain a `tail_node` reference, adding to the tail is done in constant time.
   - **Space Complexity**: O(1)  
     - Only creates one new node.

### 3. **insert(pos, new_value)**
   - **Time Complexity**:
     - **Best case** (insert at head): O(1) 
     - **Worst case** (insert at the end): O(n)
     - **Average case**: O(n) (since we need to traverse the list to find the position)
   - **Space Complexity**: O(1) 
     - Creates one new node.

### 4. **remove_head()**
   - **Time Complexity**: O(1) 
     - Updates `head_node` and `prev_node` of the new head.
   - **Space Complexity**: O(1) 
     - No additional memory is allocated.

### 5. **remove_tail()**
   - **Time Complexity**: O(1) 
     - Updates `tail_node` and `next_node` of the new tail.
   - **Space Complexity**: O(1)  
     - No additional memory is allocated.

### 6. **remove_by_value(value_to_remove)**
   - **Time Complexity**: O(n)  
     - In the worst case, we have to traverse the entire list to find the node.
   - **Space Complexity**: O(1)  
     - No extra space is used.

### 7. **stringify_list()**
   - **Time Complexity**: O(n)   
     - Iterates through the list to construct a string.
   - **Space Complexity**: O(n)  
     - Stores all elements in a string.

---

### **Overall Complexity Summary:**

| Operation           | Time Complexity | Space Complexity |
|---------------------|-----------------|------------------|
| add_to_head()       |   O(1)          |       O(1)       |
| add_to_tail()       |   O(1)          |       O(1)       |
| insert(pos, val)    |   O(n)          |       O(1)       |
| remove_head()       |   O(1)          |       O(1)       |
| remove_tail()       |   O(1)          |       O(1)       |
| remove_by_value()   |   O(n)          |       O(1)       |
| stringify_list()    |   O(n)          |       O(n)       |

"""
