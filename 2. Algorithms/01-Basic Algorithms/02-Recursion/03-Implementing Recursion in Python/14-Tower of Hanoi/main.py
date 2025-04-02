# Implementation in Python:


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
"""
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
"""

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

The time complexity can be derived from the recurrence relation:
- For `n == 1`, the time is constant: T(1) = 1.
- For `n > 1`, the time is: T(n) = 2 ⋅ T(n - 1) + 1.

This is because the function makes two recursive calls with `n - 1` disks and performs a constant amount of work
(the `if` check and the `return`).

#### Solving the Recurrence:
The recurrence T(n) = 2 ⋅ T(n - 1) + 1 is a standard recurrence for Tower of Hanoi. Its solution is: T(n) = 2ⁿ - 1

Thus, the time complexity is O(2ⁿ).

### Space Complexity:

The space complexity is determined by the maximum depth of the recursion stack. 
- The recursion depth is `n` because each recursive call reduces `n` by 1 until `n == 1`.
- At each recursion level, a constant amount of space is used (for the function call stack frame).

Thus, the space complexity is O(n).

### Summary:
- **Time Complexity:** O(2ⁿ) (exponential time).
- **Space Complexity:** O(n) (linear space, due to recursion depth).

"""
