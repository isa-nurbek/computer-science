# What is a Node in Computer Science?

In computer science, a **node** is a fundamental unit of a data structure that serves as a building block for organizing, storing, and manipulating data. Nodes are typically used in hierarchical or linked data structures like **trees**, **graphs**, and **linked lists**.

In this article, we’ll discuss what a node is as well as how nodes link to other nodes.

An individual node contains data and links to other nodes. Each data structure adds additional constraints or behavior to these features to create the desired structure.

Consider the node depicted below. This node (node_a) contains a piece of data (the number 5) and a link to another node (node_b):

![Node representation showing data value 5 and a link to the next node](../Information%20about%20Nodes/node_images/node.webp)

## Node implementations

The data contained within a node can be a variety of types, depending on the language you are using. In the previous example, it was an integer (the number 5), but it could be a string ("five"), decimal (5.1), an array ([5,3,4]) or nothing (null).

The link or links within the node are sometimes referred to as pointers. This is because they “point” to another node.

Typically, data structures implement nodes with one or more links. If these links are null, it denotes that you have reached the end of the particular node or link path you were previously following.

A variety of node implementations are depicted in the following diagram. Examine the types of data and how some of the nodes are linked:

![Node Implementations](../Information%20about%20Nodes/node_images/node_implementation.svg)

## Node linking

Often, due to the data structure, nodes may only be linked to a single other node. This makes it very important to consider how you implement modifying or removing nodes from a data structure.

If you inadvertently remove the single link to a node, that node’s data and any linked nodes could be “lost” to your application. When this happens to a node, it is called an orphaned node.

Examine the nodes in the diagram:

![Node Linking](../Information%20about%20Nodes/node_images/nodes.gif)

## Components of a Node

A node generally consists of the following components:

1. **Data**:

    - The information or value that the node holds.
    - Example: In a binary tree, the data could be a number or string.

2. **References (or Pointers)**:

    - Links to other nodes in the structure.
    - Example:
        - In a linked list, a node has a single reference pointing to the next node.
        - In a binary tree, a node has two references, typically pointing to its left and right children.
        - In graphs, a node can have multiple references representing connections to other nodes.

3. **Additional Metadata (Optional)**:
    - Extra information, such as a "parent pointer" in some trees or a "visited" flag in graphs.

---

## How Nodes Work in Different Data Structures

### Linked List

-   A node contains data and a reference to the next node in the sequence.
-   Example:

```

Node 1 --> Node 2 --> Node 3 --> NULL

```

-   Node 1's reference points to Node 2.
-   Node 3's reference is `NULL`, marking the end of the list.

### Binary Tree

-   A node in a binary tree has three parts:
-   Data
-   Left child reference
-   Right child reference
-   Example:

```

        [10]
       /   \
     [5]   [15]

```

-   The root node (10) points to its left child (5) and right child (15).
-   Nodes without children have references set to `NULL`.

### Graphs

-   A node, often called a **vertex**, holds data and a list of references to other nodes (neighbors).
-   Example (Adjacency List Representation):

```

Node A: [B, C]
Node B: [A, D]
Node C: [A, D]
Node D: [B, C]

```

### Heap

-   A heap is a specialized tree where each node satisfies the **heap property**:
-   Max-Heap: Parent nodes are always greater than or equal to their children.
-   Min-Heap: Parent nodes are always smaller than or equal to their children.
-   Example (Min-Heap):

```

        [1]
       /   \
     [3]   [5]
    /  \

[4] [8]

```

---

## Key Characteristics of a Node

1. **Interconnectivity**:

-   Nodes connect to form the structure (e.g., chains in linked lists or hierarchies in trees).

2. **Dynamic Size**:

-   Nodes can be added or removed dynamically, making them versatile in dynamic data structures.

3. **Traversability**:

-   Nodes are traversed to access, search, or manipulate data.
-   Example: Traversing a tree uses methods like in-order, pre-order, or post-order traversal.

---

## Example Implementation in Python

Here’s an example of a node in a binary tree:

```python
class Node:
  def __init__(self, data):
      self.data = data
      self.left = None  # Reference to left child
      self.right = None  # Reference to right child

# Creating nodes
root = Node(10)
root.left = Node(5)
root.right = Node(15)

# Accessing data
print(root.data)        # Output: 10
print(root.left.data)   # Output: 5
print(root.right.data)  # Output: 15
```

---

## How Nodes Enable Functionality

Nodes are pivotal because they:

1. Provide modularity in building and managing data structures.
2. Enable traversal and searching algorithms.
3. Allow efficient memory usage by dynamically linking components.
4. Serve as a foundation for implementing complex algorithms like Dijkstra's or A\* in graphs.

Understanding nodes is essential for working with complex data structures and designing efficient algorithms!
