# Article - Two-Pointer Linked List Techniques

Two-pointer techniques are powerful and commonly used in solving linked list problems efficiently. They involve maintaining two pointers that traverse the list at different speeds or starting positions to solve problems like detecting cycles, finding the middle of a list, or removing nodes.

## **Detailed Explanation**

### Key Scenarios for Two-Pointer Techniques:

1. **Detecting a Cycle (Floyd's Cycle Detection Algorithm)**:
   - Use two pointers: a slow pointer (`slow`) and a fast pointer (`fast`).
   - `slow` moves one step at a time, while `fast` moves two steps.
   - If the linked list has a cycle, the two pointers will meet.

2. **Finding the Middle of a Linked List**:
   - Use two pointers: one (`slow`) that moves one step at a time, and another (`fast`) that moves two steps at a time.
   - When `fast` reaches the end, `slow` will be at the middle.

3. **Removing the N-th Node from the End**:
   - Use two pointers starting at the head.
   - Move the first pointer `n` steps ahead.
   - Then, move both pointers simultaneously until the first pointer reaches the end.
   - The second pointer will be at the node before the N-th node from the end.

4. **Checking if a List is a Palindrome**:
   - Use two pointers to find the middle of the list, reverse the second half, and then compare both halves.

5. **Merging Two Sorted Linked Lists**:
   - Use two pointers, one for each list, and merge the nodes in sorted order.

---

## **Python Implementation**

```python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


# 1. Detecting a Cycle in a Linked List
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Cycle detected
            return True
    return False


# 2. Finding the Middle of a Linked List
def find_middle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # The slow pointer points to the middle node


# 3. Removing the N-th Node from the End
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    first, second = dummy, dummy
    # Move the first pointer `n+1` steps ahead
    for _ in range(n + 1):
        first = first.next
    # Move both pointers until the first pointer reaches the end
    while first:
        first = first.next
        second = second.next
    # Remove the N-th node
    second.next = second.next.next
    return dummy.next


# 4. Checking if a Linked List is a Palindrome
def is_palindrome(head):
    if not head:
        return True

    # Step 1: Find the middle of the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # Step 3: Compare the two halves
    left, right = head, prev
    while right:  # Only need to compare until the end of the second half
        if left.value != right.value:
            return False
        left = left.next
        right = right.next

    return True


# 5. Merging Two Sorted Linked Lists
def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    # Append the remaining nodes
    current.next = l1 or l2
    return dummy.next


# Helper function to create a linked list from a list
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    print(" -> ".join(map(str, values)))


# Example usage
if __name__ == "__main__":
    # Find the middle of a linked list
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Middle Node:", find_middle(head).value)

    # Check for cycle
    cycle_head = create_linked_list([1, 2, 3])
    cycle_head.next.next.next = cycle_head.next  # Create a cycle
    print("Has Cycle:", has_cycle(cycle_head))

    # Remove N-th node
    head = create_linked_list([1, 2, 3, 4, 5])
    head = remove_nth_from_end(head, 2)
    print("After Removing N-th Node:")
    print_linked_list(head)

    # Check Palindrome
    palindrome_head = create_linked_list([1, 2, 3, 2, 1])
    print("Is Palindrome:", is_palindrome(palindrome_head))

    # Merge Two Sorted Lists
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([2, 4, 6])
    merged_head = merge_two_sorted_lists(l1, l2)
    print("Merged List:")
    print_linked_list(merged_head)


Output:

Middle Node: 3
Has Cycle: True
After Removing N-th Node:
1 -> 2 -> 3 -> 5
Is Palindrome: True
Merged List:
1 -> 2 -> 3 -> 4 -> 5 -> 6

```

### Detailed Explanation of the Code

This code implements five common operations for working with singly linked lists. Each function solves a specific problem related to linked lists. Let’s break it down function by function:

---

### 1. **Detecting a Cycle in a Linked List (`has_cycle`)**
This function uses **Floyd's Cycle Detection Algorithm** (also called the "Tortoise and Hare" algorithm).

- **How it works**:
  - Two pointers, `slow` and `fast`, traverse the list.
  - `slow` moves one step at a time, while `fast` moves two steps.
  - If there’s a cycle, the two pointers will eventually meet.
  - If `fast` reaches the end (`None`), there is no cycle.

- **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes in the list.
- **Space Complexity**: \(O(1)\), since no extra memory is used.

---

### 2. **Finding the Middle of a Linked List (`find_middle`)**
This function also uses two pointers (`slow` and `fast`).

- **How it works**:
  - Both pointers start at the head.
  - `slow` moves one step at a time, while `fast` moves two steps.
  - When `fast` reaches the end of the list, `slow` will be at the middle node.

- **Edge Cases**:
  - If the list has an even number of nodes, `slow` returns the second middle node.

- **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes.
- **Space Complexity**: \(O(1)\).

---

### 3. **Removing the N-th Node from the End (`remove_nth_from_end`)**
This function uses the **two-pointer technique** to identify and remove the \(n\)-th node from the end in one pass.

- **How it works**:
  1. A `dummy` node is created and points to the head (to handle edge cases like removing the first node).
  2. `first` pointer moves \(n+1\) steps ahead of the `second` pointer.
  3. Both pointers are moved forward together until `first` reaches the end.
  4. At this point, `second.next` points to the node to be removed, so we update it to skip the node.

- **Time Complexity**: \(O(n)\).
- **Space Complexity**: \(O(1)\).

---

### 4. **Checking if a Linked List is a Palindrome (`is_palindrome`)**
This function determines if the linked list reads the same forward and backward.

- **How it works**:
  1. **Find the middle**: Using the `slow` and `fast` pointers, find the middle of the list.
  2. **Reverse the second half**: Reverse the nodes from the middle to the end of the list.
  3. **Compare two halves**: Start from the head and the reversed second half. Compare node values until the end of the reversed list.
  4. If all values match, the list is a palindrome.

- **Edge Cases**:
  - Empty list (`head = None`) is considered a palindrome.

- **Time Complexity**: \(O(n)\), as we traverse the list multiple times.
- **Space Complexity**: \(O(1)\), as we reverse the list in place.

---

### 5. **Merging Two Sorted Linked Lists (`merge_two_sorted_lists`)**
This function merges two sorted linked lists into a single sorted linked list.

- **How it works**:
  1. Create a dummy node to simplify list construction.
  2. Use a `current` pointer to track the last node of the merged list.
  3. Compare the heads of `l1` and `l2`:
     - Append the smaller node to `current.next`.
     - Move the pointer (`l1` or `l2`) forward.
  4. Once one list is exhausted, append the remaining nodes from the other list.

- **Time Complexity**: \(O(m + n)\), where \(m\) and \(n\) are the lengths of the two lists.
- **Space Complexity**: \(O(1)\).

---

### Helper Functions

1. **`create_linked_list(values)`**:
   - Creates a linked list from a Python list of values.
   - Returns the head of the new linked list.

2. **`print_linked_list(head)`**:
   - Traverses the list and prints the values in a readable format.

---

### Example Usage Walkthrough

1. **Finding the Middle Node**:
   ```python
   head = create_linked_list([1, 2, 3, 4, 5])
   print("Middle Node:", find_middle(head).value)  # Output: 3
   ```
   - The list is `[1 -> 2 -> 3 -> 4 -> 5]`.
   - The `slow` pointer stops at `3`.

2. **Cycle Detection**:
   ```python
   cycle_head = create_linked_list([1, 2, 3])
   cycle_head.next.next.next = cycle_head.next  # Creates a cycle
   print("Has Cycle:", has_cycle(cycle_head))  # Output: True
   ```
   - A cycle is created between nodes `3` and `2`.

3. **Removing the N-th Node**:
   ```python
   head = create_linked_list([1, 2, 3, 4, 5])
   head = remove_nth_from_end(head, 2)
   print_linked_list(head)  # Output: 1 -> 2 -> 3 -> 5
   ```
   - The 2nd node from the end (`4`) is removed.

4. **Palindrome Check**:
   ```python
   palindrome_head = create_linked_list([1, 2, 3, 2, 1])
   print("Is Palindrome:", is_palindrome(palindrome_head))  # Output: True
   ```

5. **Merging Two Sorted Lists**:
   ```python
   l1 = create_linked_list([1, 3, 5])
   l2 = create_linked_list([2, 4, 6])
   merged_head = merge_two_sorted_lists(l1, l2)
   print_linked_list(merged_head)  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
   ```

---

### Key Takeaways

- The **two-pointer technique** is a common pattern for solving linked list problems.
- Understanding **edge cases** (empty list, single-node list, etc.) is crucial for correctness.
- Efficient manipulation of pointers helps keep time and space complexity optimal.

---

### 1. **Time and Space Complexity of Each Function**

1. **`has_cycle(head)`**:
   - **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes in the list.
   - **Space Complexity**: \(O(1)\), as no additional data structures are used.

2. **`find_middle(head)`**:
   - **Time Complexity**: \(O(n)\), as it traverses the list once.
   - **Space Complexity**: \(O(1)\).

3. **`remove_nth_from_end(head, n)`**:
   - **Time Complexity**: \(O(n)\), as it traverses the list once.
   - **Space Complexity**: \(O(1)\).

4. **`is_palindrome(head)`**:
   - **Time Complexity**: \(O(n)\):
     - \(O(n)\) to find the middle.
     - \(O(n)\) to reverse the second half.
     - \(O(n)\) to compare the two halves.
   - **Space Complexity**: \(O(1)\), as the reversal is done in place.

5. **`merge_two_sorted_lists(l1, l2)`**:
   - **Time Complexity**: \(O(m + n)\), where \(m\) and \(n\) are the lengths of the two lists.
   - **Space Complexity**: \(O(1)\), as the merged list is built in place.

6. **Helper Functions**:
   - **`create_linked_list(values)`**:
     - **Time Complexity**: \(O(n)\), where \(n\) is the length of the input list.
     - **Space Complexity**: \(O(1)\), as it constructs nodes in place.
   - **`print_linked_list(head)`**:
     - **Time Complexity**: \(O(n)\).
     - **Space Complexity**: \(O(1)\).

---

### 2. **Cumulative Complexity for Example Usage**

In the provided example:

1. **`find_middle(head)`**:
   - \(O(5)\) time (for a list of size 5).
   - \(O(1)\) space.

2. **`has_cycle(cycle_head)`**:
   - \(O(3)\) time (for a list of size 3 with a cycle).
   - \(O(1)\) space.

3. **`remove_nth_from_end(head, 2)`**:
   - \(O(5)\) time (for a list of size 5).
   - \(O(1)\) space.

4. **`is_palindrome(palindrome_head)`**:
   - \(O(5)\) time (for a list of size 5).
   - \(O(1)\) space.

5. **`merge_two_sorted_lists(l1, l2)`**:
   - \(O(3 + 3)\) time (for two lists of size 3 each).
   - \(O(1)\) space.

6. **Helper Functions**:
   - `create_linked_list` is called multiple times, each with time complexity \(O(n)\):
     - \(O(5 + 3 + 5 + 3 + 3) = O(19)\) for all calls combined.
   - `print_linked_list` is used to display results, with time complexity \(O(n)\) for each call.

---

### 3. **Total Time and Space Complexity**

- **Time Complexity**:
  - Summing all operations: 
    \(O(5 + 3 + 5 + 5 + 6 + 19) = O(43)\).
  - This reduces to \(O(n)\) in terms of the total number of nodes processed, where \(n\) is the total size of all lists.

- **Space Complexity**:
  - Every function uses \(O(1)\) space.
  - Therefore, the overall **space complexity** remains \(O(1)\).

---

### Summary

- **Overall Time Complexity**: \(O(n)\), where \(n\) is the total number of nodes processed across all operations.
- **Overall Space Complexity**: \(O(1)\), as no additional space is used except for a few pointers.