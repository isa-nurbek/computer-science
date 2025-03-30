# Implementation in Python:


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

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Understanding the Fibonacci Sequence**
The Fibonacci sequence is defined as:

```
        0,                 if n = 0
F(n) =  1,                 if n = 1
        F(n-1) + F(n-2),   if n ≥ 2
```

This means:
- The **0th Fibonacci number** is **0**.
- The **1st Fibonacci number** is **1**.
- Any other Fibonacci number **F(n)** is the sum of the two previous Fibonacci numbers:  

```
F(n) = F(n-1) + F(n-2)
```

Example sequence:  

```
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```

---

### **How the Code Works**

#### **Recursive Breakdown**
The function works recursively by calling itself until it reaches the base case.

1. **Base Case:**  
   If `n` is `0` or `1`, return `n` directly.
   ```
   return n if n <= 1 
   ```
   This prevents infinite recursion.

2. **Recursive Case:**  
   Otherwise, compute Fibonacci using:
   ```
   fibonacci(n - 1) + fibonacci(n - 2)
   ```
   This means the function calls itself twice for each `n` until it reaches the base case.

---

### **Step-by-Step Execution for `fibonacci(6)`**

Let's manually calculate `fibonacci(6)`.

```
fibonacci(6) = fibonacci(5) + fibonacci(4)

   fibonacci(5) = fibonacci(4) + fibonacci(3)
      fibonacci(4) = fibonacci(3) + fibonacci(2)
         fibonacci(3) = fibonacci(2) + fibonacci(1)
            fibonacci(2) = fibonacci(1) + fibonacci(0)
               fibonacci(1) = 1
               fibonacci(0) = 0
            fibonacci(2) = 1 + 0 = 1
         fibonacci(3) = 1 + 1 = 2
      fibonacci(4) = 2 + 1 = 3
   fibonacci(5) = 3 + 2 = 5
fibonacci(6) = 5 + 3 = 8
```

### **Final Output**
```
print(fibonacci(6))  # Output: 8
```

"""

# =========================================================================================================================== #

# Optimized Fibonacci Approach:

from functools import lru_cache


@lru_cache(None)
def fibonacci_optimized(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


# Test Case:
print(fibonacci_optimized(6))  # Output: 8

# =========================================================================================================================== #

# Big O Analysis for Optimized Approach:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `fibonacci_optimized` function that uses `lru_cache` for memoization.

### Time Complexity:

With `@lru_cache(None)`, the function memoizes all previously computed results. This means each unique `fibonacci_optimized(k)`
for `k` from `0` to `n` is computed exactly once.

1. **First call for a given `n`:** The function recursively computes `fibonacci_optimized(n-1)` and `fibonacci_optimized(n-2)`,
but these are stored in the cache after the first computation.

2. **Subsequent calls:** If the same `k` is encountered again (e.g., `fibonacci_optimized(n-2)` is called while computing
`fibonacci_optimized(n-1)`), the result is retrieved from the cache in `O(1)` time.

Thus, the total number of unique computations is `O(n)` (since we compute `fibonacci_optimized(0)` to `fibonacci_optimized(n)`
exactly once each). Each computation (ignoring recursive calls) is `O(1)` (just a lookup or addition).

**Final Time Complexity:** `O(n)`.

---

### Space Complexity:

The space complexity is determined by:
1. The depth of the recursion stack.
2. The size of the cache.

1. **Recursion Stack:** The maximum depth of the recursion is `O(n)` (e.g., when computing `fibonacci_optimized(n)`,
the longest chain of recursive calls is `n -> n-1 -> n-2 -> ... -> 0`).

2. **Cache Size:** The cache stores all results from `fibonacci_optimized(0)` to `fibonacci_optimized(n)`, which is `O(n)` space.

**Final Space Complexity:** `O(n)` (due to the cache and recursion stack).

---

### Summary:
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` 

"""
