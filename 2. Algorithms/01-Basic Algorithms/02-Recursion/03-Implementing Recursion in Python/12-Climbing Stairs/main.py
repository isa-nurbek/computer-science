# Implementation in Python:


def climb_stairs(n):
    # Base cases:
    # - If there's only 1 step, there's only 1 way to climb it
    # - If there are 2 steps, there are 2 ways (1+1 or 2)
    if n <= 2:
        return n
    # Recursive case:
    # The number of ways to climb 'n' steps is the sum of:
    # - Ways to climb (n-1) steps (if your first step is 1)
    # - Ways to climb (n-2) steps (if your first step is 2)
    else:
        return climb_stairs(n - 1) + climb_stairs(n - 2)


# Test Case:
print(climb_stairs(5))  # Output: 8
