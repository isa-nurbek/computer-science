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
