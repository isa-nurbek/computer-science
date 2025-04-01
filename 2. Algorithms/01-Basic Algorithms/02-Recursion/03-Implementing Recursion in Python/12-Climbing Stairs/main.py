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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

The time complexity of this recursive solution is exponential, specifically **O(2ⁿ)**.

Here's why:

1. The function makes two recursive calls for each `n > 2`: `climb_stairs(n - 1)` and `climb_stairs(n - 2)`.
2. This leads to a binary tree of recursive calls, where each node branches into two (except the base cases).
3. The height of the tree is roughly `n`, and the number of nodes grows exponentially with `n`.

4. The exact recurrence relation is:

        T(n) = T(n-1) + T(n-2) + O(1)

   This is similar to the Fibonacci sequence, which has an exponential time complexity.


### Space Complexity:

The space complexity is **O(n)** due to the recursion stack.

Here's why:

1. The maximum depth of the recursion stack is `n` (when you go all the way down to `n = 1` or `n = 0`).
2. Each recursive call adds a new frame to the call stack, and the stack grows linearly with `n`.

### Example:
For `n = 5`, the call stack looks like:
- `climb_stairs(5)`
  - `climb_stairs(4)`
    - `climb_stairs(3)`
      - `climb_stairs(2)`
      - `climb_stairs(1)`
    - `climb_stairs(2)`
  - `climb_stairs(3)`
    - `climb_stairs(2)`
    - `climb_stairs(1)`

The maximum depth here is 5 (e.g., `5 → 4 → 3 → 2 → 1`), so the space complexity is O(n).


### Summary:
- **Time Complexity**: O(2ⁿ)
- **Space Complexity**: O(n)

### Optimization Note:

This recursive approach is inefficient due to repeated calculations (e.g., `climb_stairs(3)` is computed multiple times
for `n = 5`). You can optimize it using:

1. **Memoization (Top-Down DP)**: Store computed results to avoid redundant work. This reduces time to O(n) and space to O(n).
2. **Bottom-Up DP (Iterative)**: Compute values iteratively from `1` to `n`. This also gives O(n) time and O(1) space
if optimized further.

"""
