# Doubly Linked Lists

## A conceptual overview of Doubly Linked Lists

A **doubly linked list** is a type of linked data structure that consists of nodes. Each node contains three elements:

1. **Data**: The actual value stored in the node.
2. **Next Pointer**: A pointer (or reference) to the **next node** in the sequence.
3. **Previous Pointer**: A pointer (or reference) to the **previous node** in the sequence.

This structure allows for **bidirectional traversal**, making it more versatile than a singly linked list, which can only be traversed in one direction.

Like a singly linked list, a doubly linked list is comprised of a series of nodes. Each node contains data and two links (or pointers) to the next and previous nodes in the list. The head node is the node at the beginning of the list, and the tail node is the node at the end of the list. The head node’s previous pointer is set to null and the tail node’s next pointer is set to null.

Think of your daily commute on the subway as a real-world example of a doubly linked list. Your home is the head of the list, your place of work is the tail, and every stop in between is another node in the list.

![Doubly Linked List](../Info%20about%20Doubly%20Linked%20List/doubly_linked_list_images/doubly_linked_list.svg)

### Structure of a Node in a Doubly Linked List

Here’s how a single node in a doubly linked list is structured:

```plaintext
| Prev | Data | Next |
```

- `Prev`: Points to the previous node (or `null`/`None` if it's the first node).
- `Data`: Contains the value stored in the node.
- `Next`: Points to the next node (or `null`/`None` if it's the last node).

---

### How a Doubly Linked List Works

1. **Initialization**:
   - The list starts with no nodes (head = `null`).
   - The **head** pointer points to the first node, and the **tail** pointer points to the last node.

2. **Insertion**:
   - **At the Beginning**: Create a new node. Update its `Next` pointer to point to the current head, and the current head's `Prev` pointer to point to the new node. Update the head pointer to the new node.
   - **At the End**: Create a new node. Update the current tail's `Next` pointer to point to the new node, and the new node's `Prev` pointer to point to the current tail. Update the tail pointer.
   - **At a Specific Position**: Traverse the list to find the target position. Update the `Prev` and `Next` pointers of the surrounding nodes to include the new node.

3. **Deletion**:
   - **At the Beginning**: Update the head pointer to the second node. Set the new head's `Prev` pointer to `null`.
   - **At the End**: Update the tail pointer to the second-last node. Set the new tail's `Next` pointer to `null`.
   - **At a Specific Position**: Update the `Prev` and `Next` pointers of the surrounding nodes to bypass the node being deleted.

4. **Traversal**:
   - **Forward Traversal**: Start at the head and follow the `Next` pointers until the tail is reached.
   - **Backward Traversal**: Start at the tail and follow the `Prev` pointers until the head is reached.

5. **Search**:
   - Traverse the list (either forward or backward) to find the node containing the desired data.

---

### Adding to the list

In a doubly linked list, adding to the list is a little complicated as we have to keep track of and set the node’s previous pointer as well as update the tail of the list if necessary.

#### Adding to the head

When adding to the head of the doubly linked list, we first need to check if there is a current head to the list. If there isn’t, then the list is empty, and we can simply make our new node both the head and tail of the list and set both pointers to null. If the list is not empty, then we will:

- Set the current head’s previous pointer to our new head.
- Set the new head’s next pointer to the current head.
- Set the new head’s previous pointer to null.

#### Adding to the tail

Similarly, there are two cases when adding a node to the tail of a doubly linked list. If the list is empty, then we make the new node the head and tail of the list and set the pointers to null. If the list is not empty, then we:

- Set the current tail’s next pointer to the new tail
- Set the new tail’s previous pointer to the current tail
- Set the new tail’s next pointer to null

![Doubly Linked List Insertion](../Info%20about%20Doubly%20Linked%20List/doubly_linked_list_images/add_doubly_linked_list.svg)

### Removing from the list

Due to the extra pointer and tail property, removing the head from a doubly linked list is slightly more complicated than removing the head from a singly linked list. However, the previous pointer and tail property make it much simpler to remove the tail of the list, as we don’t have to traverse the entire list to be able to do it.

#### Removing the head

Removing the head involves updating the pointer at the beginning of the list. We will set the previous pointer of the new head (the element directly after the current head) to null, and update the head property of the list. If the head was also the tail, the tail removal process will occur as well.

#### Removing the tail

Similarly, removing the tail involves updating the pointer at the end of the list. We will set the next pointer of the new tail (the element directly before the tail) to null, and update the tail property of the list. If the tail was also the head, the head removal process will occur as well.

![Doubly Linked List Remove Head & Tail](../Info%20about%20Doubly%20Linked%20List/doubly_linked_list_images/remove_head_doubly_linked_list.svg)

### Removing from the middle of the list

It is also possible to remove a node from the middle of the list. Since that node is neither the head nor the tail of the list, there are two pointers that must be updated:

- We must set the removed node’s preceding node’s next pointer to its following node.
- We must set the removed node’s following node’s previous pointer to its preceding node.

There is no need to change the pointers of the removed node, as updating the pointers of its neighboring nodes will remove it from the list. If no nodes in the list are pointing to it, the node is orphaned.

![Doubly Linked List Remove Middle](../Info%20about%20Doubly%20Linked%20List/doubly_linked_list_images/remove_middle_doubly_linked_list.svg)

### Advantages of Doubly Linked Lists

- **Bidirectional Traversal**: Unlike singly linked lists, a doubly linked list can be traversed in both directions.
- **Efficient Deletion and Insertion**:
  - Deletion and insertion at both ends or any arbitrary position are faster since you can use the `Prev` pointer to easily adjust connections.

---

### Disadvantages

- **Increased Memory Usage**: Each node requires extra memory for the `Prev` pointer.
- **Complexity**: Maintaining `Prev` and `Next` pointers requires additional care, increasing implementation complexity.

---

### Example Use Cases

1. **Undo/Redo Functionality**: Applications like text editors use doubly linked lists to keep track of actions, allowing users to move back (undo) and forth (redo).
2. **Navigating Browsers**: The browser's history (back and forward navigation) can be implemented using a doubly linked list.
3. **Music Playlist**: It allows both forward and backward traversal of songs in a playlist.