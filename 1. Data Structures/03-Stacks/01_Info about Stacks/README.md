# Stacks Data Structure: Conceptual

A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle. This means that the last element added to the stack is the first one to be removed. It is analogous to a stack of plates—when you add a new plate, it goes on top, and when you take one off, you remove the topmost plate first.

---

## **1. Operations in a Stack**

A stack mainly supports three primary operations:

1. **Push (Insertion)**  
   - Adds an element to the top of the stack.
   - If the stack is full (in a fixed-size array implementation), it results in a "Stack Overflow."

2. **Pop (Deletion)**  
   - Removes and returns the top element of the stack.
   - If the stack is empty, it results in a "Stack Underflow."

3. **Peek (Top or Peek)**  
   - Returns the top element without removing it.

Additional operations:

- **isEmpty()** – Checks if the stack is empty.
- **isFull()** – Checks if the stack is full (for array-based stacks).
- **Size()** – Returns the number of elements in the stack.

Stacks mimic a physical “stack” of objects. Consider a set of gym weights:

![Stacks Description](../01_Info%20about%20Stacks/stack_images/weight_stacking.webp)

Each plate has a weight (the data). The first plate you add, or push, onto the floor is both the bottom and top of the stack. Each weight added becomes the new top of the stack.

At any point, the only weight you can remove, or pop, from the stack is the top one. You can peek and read the top weight without removing it from the stack.

The last plate that you put down becomes the first, and only, one that you can access. This is a Last In, First Out or LIFO structure. A less frequently used term is First In, Last Out, or FILO.

---

## **2. Stack Representation**

A stack can be represented as:

```text
Stack:
Top →  [  5  ]
         [  8  ]
         [  3  ]
Bottom → [  1  ]
```

- If we perform `pop()`, the element `5` is removed.
- If we perform `push(10)`, it gets placed on top.

---

## **3. Implementation**

A stack is typically implemented using:

- **Arrays** (Fixed size, efficient, but requires resizing if full)
- **Linked Lists** (Dynamic size, uses extra memory for pointers)

Stacks can be implemented using a linked list as the underlying data structure because it’s more efficient than a list or array.

![Stacks Implementation with Linked List](../01_Info%20about%20Stacks/stack_images/stack_linked_list.svg)

Depending on the implementation, the top of the stack is equivalent to the head node of a linked list and the bottom of the stack is equivalent to the tail node.

A constraint that may be placed on a stack is its size. This is done to limit and quantify the resources the data structure will take up when it is “full.”

Attempting to push data onto an already full stack will result in a stack overflow. Similarly, if you attempt to pop data from an empty stack, it will result in a stack underflow.

## **4. Applications of Stacks**

Stacks are used in various real-world and computer science applications, including:

### **1. Function Calls (Recursion)**

- The call stack manages function calls in programming.
- When a function is called, it is pushed onto the stack.
- When it finishes execution, it is popped.

### **2. Undo/Redo Operations**

- Applications like text editors store actions in a stack to enable undo/redo functionality.

### **3. Expression Evaluation (Postfix/Infix/Prefix)**

- Stacks are used to evaluate and convert expressions (e.g., infix to postfix notation).

### **4. Backtracking Algorithms**

- Used in solving maze problems, depth-first search (DFS), and pathfinding.

### **5. Browser History**

- Back and forward operations in a web browser use stacks.

---

## **5. Stack vs. Queue**

| Feature        | Stack (LIFO)  | Queue (FIFO)  |
|---------------|--------------|--------------|
| Order        | Last In, First Out | First In, First Out |
| Insert (Push/Enqueue) | At the top | At the rear |
| Remove (Pop/Dequeue) | From the top | From the front |
| Example Use  | Function calls, undo-redo | Task scheduling, print queue |

---

### **Conclusion**

Stacks are an essential data structure widely used in software development and system operations. Understanding their LIFO behavior and applications will help in writing efficient algorithms, especially when dealing with recursive functions, expression evaluations, and backtracking problems.
