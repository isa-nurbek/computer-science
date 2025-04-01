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

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This Python function `climb_stairs(n)` is solving the classic "Climbing Stairs" problem using recursion. 
Let's break it down step by step:

### **Problem Statement**
You have `n` steps to climb. At each step, you can either take 1 step or 2 steps at a time. How many distinct ways
can you climb to the top?

For example:
- `n = 1` → Only 1 way: `[1]`
- `n = 2` → Two ways: `[1,1]` or `[2]`
- `n = 3` → Three ways: `[1,1,1]`, `[1,2]`, `[2,1]`

### **Code Explanation**
```
def climb_stairs(n):
    if n <= 2:
        return n  # Base case
    else:
        return climb_stairs(n - 1) + climb_stairs(n - 2)
```

#### **Step-by-step Execution for `n = 5`**

The function follows a recursive approach, breaking the problem into smaller subproblems.

1. `climb_stairs(5)`  
   → `climb_stairs(4) + climb_stairs(3)`

2. `climb_stairs(4)`  
   → `climb_stairs(3) + climb_stairs(2)`

3. `climb_stairs(3)`  
   → `climb_stairs(2) + climb_stairs(1)`

4. **Base Cases**:  
   - `climb_stairs(2) = 2`  
   - `climb_stairs(1) = 1`

Now, we can evaluate step by step:

```
climb_stairs(3) = climb_stairs(2) + climb_stairs(1)
                 = 2 + 1
                 = 3
```

```
climb_stairs(4) = climb_stairs(3) + climb_stairs(2)
                 = 3 + 2
                 = 5
```

```
climb_stairs(5) = climb_stairs(4) + climb_stairs(3)
                 = 5 + 3
                 = 8
```

### **Final Output**
```
print(climb_stairs(5))  # Output: 8
```
There are **8 ways** to climb 5 stairs.

---

### **Optimized Approach: Dynamic Programming**

To avoid redundant calculations, we can use **memoization (Top-Down)** or **tabulation (Bottom-Up)**.

Here’s a better **Bottom-Up DP (Iterative) solution**:

"""

# Optimized Approach:


def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


"""
- **Time Complexity:** **O(n)**
- **Space Complexity:** **O(1)** (only two variables `a` and `b` are used)

This is much faster and avoids deep recursion!

"""
