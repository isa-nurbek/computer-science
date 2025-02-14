# Queues: Conceptual

## **Queues Data Structure: A Detailed Explanation**

A **Queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle. This means that the first element added to the queue will be the first one to be removed, just like a line of people waiting at a ticket counter.

---

## **1. Characteristics of Queues**

- **FIFO Principle**: The element that enters first is processed first.
- **Linear Order**: Elements are arranged in a sequential manner.
- **Queues provide three methods for interaction**:
  - **Enqueue**: Adding an element to the rear (end) of the queue.
  - **Dequeue**: Removing an element from the front (beginning) of the queue.
  - **Peek**: Reveals data from the “front” of the queue without removing it.
  
This data structure mimics a physical queue of objects like a line of people buying movie tickets. Each person has a name (the data). The first person to enqueue, or get into line, is both at the front and back of the line. As each new person enqueues, they become the new back of the line.
  
![Queue Line](../01_Info%20about%20Queues/queues_images/queue_movie_line.webp)

When the cashier serves someone, they begin at the front of the line (or people would get very mad!). Each person served is dequeued from the front of the line, they purchase a ticket and leave.

If they just want to know who is next in line, they can peek and get their name without removing them from the queue.

The first person in the queue is the first to be served. Queues are a First In, First Out or FIFO structure.

---

## **2. Types of Queues**

### **a) Simple Queue (Linear Queue)**

- Follows FIFO strictly.
- Insertions occur at the rear, and deletions occur at the front.
- Example: People waiting in line at a bank.

### **b) Circular Queue**

- The last position is connected to the first position, forming a circle.
- Efficient memory utilization because empty spaces in front (caused by dequeuing) can be reused.
- Example: CPU scheduling in operating systems.

### **c) Priority Queue**

- Each element has a priority.
- Elements with higher priority are dequeued before those with lower priority, regardless of insertion order.
- Example: Task scheduling in an operating system.

### **d) Double-Ended Queue (Deque)**

- Allows insertion and deletion from both the front and rear.
- Can be **input-restricted** (insertion at only one end) or **output-restricted** (deletion at only one end).
- Example: Undo/Redo operations in text editors.

---

## **3. Queue Operations**

1. **Enqueue (Insertion)**
   - Adds an element to the rear.
   - If the queue is full, it results in an **overflow** condition.

2. **Dequeue (Deletion)**
   - Removes an element from the front.
   - If the queue is empty, it results in an **underflow** condition.

3. **Front (Peek)**
   - Returns the front element without removing it.

4. **Rear (Last Element)**
   - Returns the last element in the queue.

5. **isEmpty()**
   - Checks if the queue is empty.

6. **isFull()**
   - Checks if the queue is full (for fixed-size implementations).

---

## **4. Queue Implementation**

### **a) Using Arrays**

- A static approach where a fixed-size array is used.
- Simple but inefficient for large datasets due to fixed size.

### **b) Using Linked List**

- A dynamic approach, where memory is allocated as needed.
- Efficient for insertion and deletion.

Queues can be implemented using a linked list as the underlying data structure. The front of the queue is equivalent to the head node of a linked list and the back of the queue is equivalent to the tail node.

![Queue Implementation with Linked List](../01_Info%20about%20Queues/queues_images/queue_linked_list.svg)

Since operations are only allowed to affect the front or back of the queue, any traversal or modification to other nodes within the linked list is disallowed. Since both ends of the queue must be accessible, a reference to both the head node and the tail node must be maintained.

One last constraint that may be placed on a queue is its length. If a queue has a limit on the amount of data that can be placed into it, it is considered a bounded queue.

Similar to stacks, attempting to enqueue data onto an already full queue will result in a queue overflow. If you attempt to dequeue data from an empty queue, it will result in a queue underflow.

---

## **5. Applications of Queues**

### **a) CPU Scheduling**

- **Round-robin scheduling** uses circular queues.

### **b) Printer Spooling**

- Print jobs are queued before being sent to the printer.

### **c) Call Center Management**

- Calls are attended in the order they arrive.

### **d) Traffic Management**

- Vehicles are queued at signals or toll booths.

### **e) Data Packet Management**

- Packets in networking follow queue-based buffering.

---

## **6. Advantages & Disadvantages**

### ✅ **Advantages**

- Maintains order of processing.
- Used in real-time applications (CPU scheduling, traffic systems).
- Can be implemented efficiently using linked lists or circular arrays.

### ❌ **Disadvantages**

- **Static Queue (Array-based)**: Fixed size, leading to inefficient memory usage.
- **Dynamic Queue (Linked List-based)**: Extra memory required for pointers.
- **Priority Queue**: Sorting elements adds extra processing overhead.

---

## **8. Conclusion**

Queues are fundamental data structures widely used in computer science for managing ordered collections of data. Whether implemented as a simple queue, circular queue, or priority queue, they play a critical role in various applications such as scheduling, networking, and resource management.
