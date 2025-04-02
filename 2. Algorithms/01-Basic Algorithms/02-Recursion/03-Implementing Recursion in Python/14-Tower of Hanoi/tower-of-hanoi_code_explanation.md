# Code Explanation: Tower of Hanoi Implementing in Python

## **Tower of Hanoi function**

```python
def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solves the Tower of Hanoi puzzle recursively.

    Args:
        n: Number of disks to move
        source: The starting peg (where the disks are initially placed)
        target: The destination peg (where the disks should be moved to)
        auxiliary: The helper peg (used for temporary storage during moving)
    """

    # Base case: If there's only one disk, move it directly from source to target
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Step 1: Move n-1 disks from source to auxiliary peg (using target as temporary storage)
    # This clears the way to access the bottom disk
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # Step 2: Move the remaining largest disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Step 3: Move the n-1 disks from auxiliary peg to target (using source as temporary storage)
    # This completes the stack on the target peg
    tower_of_hanoi(n - 1, auxiliary, target, source)


# Test Case:

tower_of_hanoi(3, "A", "C", "B")

# Output:

Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C

```

The **Tower of Hanoi** is a classic problem in recursion. Let's break the code down step by step and understand how it works.

## **Understanding the Problem**

There are three rods: **Source (A)**, **Target (C)**, and **Auxiliary (B)**. The goal is to move **n** disks from the Source rod to the Target rod, following these rules:

1. Only one disk can be moved at a time.
2. A disk can only be placed on an empty rod or on top of a larger disk.
3. You must use the Auxiliary rod as an intermediate step.

---

## **Breaking Down the Code**

### **Function Definition**

```python
def tower_of_hanoi(n, source, target, auxiliary):
```

- `n`: Number of disks.
- `source`: The rod from which the disks are moved.
- `target`: The rod to which the disks need to be moved.
- `auxiliary`: The rod used as a helper.

### **Base Case**

```python
if n == 1:
    print(f"Move disk 1 from {source} to {target}")
    return
```

- If there is only **one disk**, it is directly moved from `source` to `target`.

### **Recursive Case**

```python
tower_of_hanoi(n - 1, source, auxiliary, target)
```

- Move **n - 1 disks** from `source` to `auxiliary` using `target` as the helper.

```python
print(f"Move disk {n} from {source} to {target}")
```

- Move the **nth (largest) disk** directly from `source` to `target`.

```python
tower_of_hanoi(n - 1, auxiliary, target, source)
```

- Move the **n - 1 disks** from `auxiliary` to `target`, using `source` as the helper.

---

## **Recursive Execution for `tower_of_hanoi(3, 'A', 'C', 'B')`**

Let's go step by step with **n = 3**:

### **Step 1: Move `n-1 = 2` disks from `A` to `B` using `C`**

1. Move **disk 1** from **A → C**.
2. Move **disk 2** from **A → B**.
3. Move **disk 1** from **C → B**.

### **Step 2: Move `disk 3` from `A` to `C`**

1. Move **disk 3** from **A → C**.

### **Step 3: Move `n-1 = 2` disks from `B` to `C` using `A`**

1. Move **disk 1** from **B → A**.
2. Move **disk 2** from **B → C**.
3. Move **disk 1** from **A → C**.

### **Final Output**

```plaintext
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

---

## **How Recursion Works Here**

At each step, we reduce the problem size (`n` decreases) until we reach the base case (`n == 1`). The recursion tree for `n = 3` looks like this:

```plaintext
tower_of_hanoi(3, A, C, B)
│
├── tower_of_hanoi(2, A, B, C) 
│   ├── tower_of_hanoi(1, A, C, B) → "Move disk 1 from A to C"
│   ├── Move disk 2 from A to B
│   ├── tower_of_hanoi(1, C, B, A) → "Move disk 1 from C to B"
│
├── Move disk 3 from A to C
│
├── tower_of_hanoi(2, B, C, A)
│   ├── tower_of_hanoi(1, B, A, C) → "Move disk 1 from B to A"
│   ├── Move disk 2 from B to C
│   ├── tower_of_hanoi(1, A, C, B) → "Move disk 1 from A to C"
```

Each call follows the same pattern, moving **smaller subproblems** until reaching the simplest case (`n = 1`).

---

## **Time Complexity**

Since each move follows a recursive pattern of **T(n) = 2T(n-1) + 1**, the **time complexity** is **O(2ⁿ - 1) ≈ O(2ⁿ)**, which grows exponentially.

## **Key Takeaways**

- The algorithm **recursively** breaks the problem into **smaller subproblems**.
- The **base case** is `n == 1`, which is directly moved.
- The **recursive case** follows:
  1. Move `n-1` disks from Source → Auxiliary.
  2. Move the largest disk from Source → Target.
  3. Move `n-1` disks from Auxiliary → Target.

This problem is a great way to understand **recursion** and **divide-and-conquer strategies**! 🚀

---

## Big O Analysis

## Time and Space Complexity Analysis

Let's analyze the time and space complexity of the given Tower of Hanoi function.

### Time Complexity

The time complexity can be derived from the recurrence relation:

- For `n == 1`, the time is constant: `T(1) = 1`.
- For `n > 1`, the time is: `T(n) = 2 ⋅ T(n - 1) + 1`.

This is because the function makes two recursive calls with `n - 1` disks and performs a constant amount of work (the `if` check and the `return`).

#### Solving the Recurrence

The recurrence `T(n) = 2 ⋅ T(n - 1) + 1` is a standard recurrence for Tower of Hanoi. Its solution is: `T(n) = 2ⁿ - 1`

Thus, the time complexity is `O(2ⁿ)`.

### Space Complexity

The space complexity is determined by the maximum depth of the recursion stack.

- The recursion depth is `n` because each recursive call reduces `n` by 1 until `n == 1`.
- At each recursion level, a constant amount of space is used (for the function call stack frame).

Thus, the space complexity is `O(n)`.

### Summary

- **Time Complexity:** `O(2ⁿ)` (exponential time).
- **Space Complexity:** `O(n)` (linear space, due to recursion depth).
