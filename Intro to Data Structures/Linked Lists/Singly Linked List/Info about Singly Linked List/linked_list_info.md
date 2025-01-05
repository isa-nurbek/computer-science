# Singly Linked List

A **Singly Linked List** is a fundamental data structure in Computer Science that consists of a sequence of elements, called **nodes**, where each node stores data and a reference (or pointer) to the next node in the sequence. Unlike arrays, Singly Linked Lists do not store elements in contiguous memory locations, making them dynamic and flexible in terms of memory usage.

![Linked List](../Info%20about%20Singly%20Linked%20List/linked_list_images/linked_list_1.svg)

The list is comprised of a series of nodes as shown in the diagram above. The head node is the node at the beginning of the list. Each node contains data and a link (or pointer) to the next node in the list. The list is terminated when a node’s link is null. This last node is called the tail node.

Consider a one-way air travel itinerary. The trip could involve traveling through several airports (nodes) connected by air travel segments (links). In this example, the initial departure city is the head node and the final arrival city is the tail node.

Since the nodes use links to denote the next node in the sequence, the nodes are not required to be sequentially located in memory. These links also allow for quick insertion and removal of nodes as you will see in future exercises.

---

## Structure of a Singly Linked List

Each node in a singly linked list typically has two components:

1. **Data**: The value or information the node contains.
2. **Next (Pointer)**: A reference to the next node in the sequence. The last node in the list has the `next` pointer set to `null` (or `None` in Python), indicating the end of the list.

---

## Key Concepts

1. **Head**: The starting node of the list. If the list is empty, the head is `null` or `None`.
2. **Traversal**: To access or process elements, you must traverse the list starting from the head, following the `next` pointers until you reach the end.
3. **Dynamic Size**: Singly linked lists can grow or shrink in size dynamically, as memory allocation happens on a per-node basis.

---

## Advantages of Singly Linked Lists

1. **Dynamic Memory Usage**: Unlike arrays, there is no need to define the size of the list in advance.
2. **Efficient Insertions and Deletions**: Adding or removing elements (especially at the beginning) is efficient, with O(1) time complexity, as no shifting of elements is required.

---

## Disadvantages of Singly Linked Lists

1. **Sequential Access**: Accessing an element requires traversing from the head, leading to \(O(n)\) time complexity for search or access.
2. **Extra Memory for Pointers**: Each node requires additional memory for storing the pointer.

---

## Basic Operations

1. **Insertion**:

    - **At the beginning**: Create a new node, set its `next` pointer to the current head, and update the head to the new node.
    - **At the end**: Traverse to the last node, set its `next` pointer to the new node.
    - **At a specific position**: Traverse to the desired position and adjust pointers accordingly.

2. **Deletion**:

    - **At the beginning**: Update the head to point to the second node.
    - **At the end**: Traverse to the second last node and set its `next` to `null`.
    - **At a specific position**: Traverse to the node before the one to delete and adjust pointers.

3. **Traversal**:
   Start at the head and follow the `next` pointers while processing the data of each node.

4. **Search**:
   Traverse the list to find an element that matches a given value.

As an example, we added values to the linked list diagram from above:

![Linked List Insertion](../Info%20about%20Singly%20Linked%20List/linked_list_images/linked_list_2.webp)

This linked list contains three nodes (node_a, node_b, and node_c).

Each node in this particular list contains a string as its data. As the sequence is defined, the order is "cats", "dogs", and "birds".

The list ends at node_c since the link within that node is set to null.

### Adding to and Removing from the Linked List:

With linked lists, because nodes are linked to from only one other node, you can’t just go adding and removing nodes willy-nilly without doing a bit of maintenance.

### Adding a New Node:

Adding a new node to the beginning of the list requires you to link your new node to the current head node. This way, you maintain your connection with the following nodes in the list.

### Removing a Node:

If you accidentally remove the single link to a node, that node’s data and any following nodes could be lost to your application, leaving you with orphaned nodes.

To properly maintain the list when removing a node from the middle of a linked list, you need to be sure to adjust the link on the previous node so that it points to the following node.

Depending on the language, nodes that are not referenced are removed automatically. “Removing” a node is equivalent to removing all references to the node.

Look at the diagram below to see the proper manner of removing a node:

![Linked List Deletion](../Info%20about%20Singly%20Linked%20List/linked_list_images/linked_list_3.webp)

In order to remove node_b, you must first link node_a to node_c (where node_b was linking). Then you can remove node_b.

---

## Applications of Singly Linked Lists

1. **Dynamic memory allocation**: Used in scenarios where the size of the dataset changes dynamically.
2. **Stacks and Queues**: Singly linked lists are a common choice for implementing stacks and queues.
3. **Adjacency lists in Graphs**: Representing graph edges efficiently.
4. **Polynomial representation**: Used to represent polynomials where each term is a node.

---

Understanding singly linked lists is foundational to learning more complex data structures like doubly linked lists, circular linked lists, and beyond.
