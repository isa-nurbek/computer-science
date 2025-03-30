def fibonacci(n):
    # Base case: if n is 0 or 1, return n directly
    # This is because Fibonacci(0) = 0 and Fibonacci(1) = 1
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)
    # Recursive case: for n > 1, return the sum of the two previous Fibonacci numbers
    # This implements the mathematical definition F(n) = F(n-1) + F(n-2)


# Test Case:
print(fibonacci(6))  # Output: 8

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:
The time complexity of this recursive Fibonacci implementation is **O(2ⁿ)** (exponential).

Here's why:

1. The function makes two recursive calls for each `n > 1`: `fibonacci(n - 1)` and `fibonacci(n - 2)`.
2. This leads to a binary tree of recursive calls, where the number of nodes roughly doubles at each level.
3. The total number of calls is approximately `2^n`, as the recursion tree has a depth of `n` and branches exponentially.

For example:
- `fibonacci(5)` calls `fibonacci(4)` and `fibonacci(3)`.
- `fibonacci(4)` calls `fibonacci(3)` and `fibonacci(2)`, and so on.

This results in redundant calculations (e.g., `fibonacci(3)` is computed multiple times), leading to inefficiency.

---

### Space Complexity:
The space complexity is **O(n)** (linear).

Here's why:

1. The space is determined by the maximum depth of the recursion stack.
2. At its deepest, the recursion goes `n` levels down (e.g., `fibonacci(n)` → `fibonacci(n-1)` → ... → `fibonacci(0)`
or `fibonacci(1)`).
3. Each recursive call adds a new stack frame, so the maximum stack size is proportional to `n`.

### Summary:
- **Time Complexity:** `O(2ⁿ)`
- **Space Complexity:** `O(n)`

---

### Additional Notes:
- This is the naive recursive approach, and its exponential time complexity makes it impractical for large `n`.
- You can improve the time complexity to **O(n)** using memoization (caching previously computed results) or to **O(1)**
space and **O(n)** time using an iterative approach with constant space. For even better performance, matrix exponentiation
or Binet's formula can reduce the time to **O(log n)** or **O(1)**, respectively (though with some precision trade-offs
for Binet's formula).

"""
