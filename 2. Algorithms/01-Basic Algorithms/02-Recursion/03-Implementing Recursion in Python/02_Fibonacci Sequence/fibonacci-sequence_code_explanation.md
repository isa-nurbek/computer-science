# Code Explanation: *Fibonacci Sequence*

Let's break down the code in detail.

## **Fibonacci Sequence function**

```python
def fibonacci(n):
    # Base case: if n is 0 or 1, return n directly
    # This is because Fibonacci(0) = 0 and Fibonacci(1) = 1
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)
    # Recursive case: for n > 1, return the sum of the two previous Fibonacci numbers
    # This implements the mathematical definition F(n) = F(n-1) + F(n-2)


# Test Case:
print(fibonacci(6))  # Output: 8
```

This code defines a recursive function called `fibonacci(n)` that calculates the **nth Fibonacci number** using **recursion**.

---

### **Understanding the Fibonacci Sequence**

The Fibonacci sequence is defined as:

```plaintext
        0,                 if n = 0
F(n) =  1,                 if n = 1
        F(n-1) + F(n-2),   if n ≥ 2
```

This means:

- The **0th Fibonacci number** is **0**.
- The **1st Fibonacci number** is **1**.
- Any other Fibonacci number **F(n)** is the sum of the two previous Fibonacci numbers:  

```plaintext
F(n) = F(n-1) + F(n-2)
```

Example sequence:  

```plaintext
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```

---

### **How the Code Works**

#### **Recursive Breakdown**

The function works recursively by calling itself until it reaches the base case.

1. **Base Case:**  
   If `n` is `0` or `1`, return `n` directly.

   ```python
   return n if n <= 1 
   ```

   This prevents infinite recursion.

2. **Recursive Case:**  
   Otherwise, compute Fibonacci using:

   ```python
   fibonacci(n - 1) + fibonacci(n - 2)
   ```

   This means the function calls itself twice for each `n` until it reaches the base case.

---

### **Step-by-Step Execution for `fibonacci(6)`**

Let's manually calculate `fibonacci(6)`.

```plaintext
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

```python
print(fibonacci(6))  # Output: 8
```

---

## Big O Analysis

### Time and Space Complexity Analysis

Let's analyze the time and space complexity of the given recursive Fibonacci function:

### Time Complexity

The time complexity of this recursive Fibonacci implementation is **O(2ⁿ)** (exponential). Here's why:

1. The function makes two recursive calls for each `n > 1`: `fibonacci(n - 1)` and `fibonacci(n - 2)`.
2. This leads to a binary tree of recursive calls, where the number of nodes roughly doubles at each level.
3. The total number of calls is approximately `2ⁿ`, as the recursion tree has a depth of `n` and branches exponentially.

For example:

- `fibonacci(5)` calls `fibonacci(4)` and `fibonacci(3)`.
- `fibonacci(4)` calls `fibonacci(3)` and `fibonacci(2)`, and so on.

This results in redundant calculations (e.g., `fibonacci(3)` is computed multiple times), leading to inefficiency.

### Space Complexity

The space complexity is **O(n)** (linear). Here's why:

1. The space is determined by the maximum depth of the recursion stack.
2. At its deepest, the recursion goes `n` levels down (e.g., `fibonacci(n)` → `fibonacci(n-1)` → ... → `fibonacci(0)` or `fibonacci(1)`).
3. Each recursive call adds a new stack frame, so the maximum stack size is proportional to `n`.

### Summary

- **Time Complexity:** `O(2ⁿ)`
- **Space Complexity:** `O(n)`

### Additional Notes

- This is the naive recursive approach, and its exponential time complexity makes it impractical for large `n`.
- You can improve the time complexity to **O(n)** using memoization (caching previously computed results) or to **O(1)** space and **O(n)** time using an iterative approach with constant space. For even better performance, matrix exponentiation or Binet's formula can reduce the time to **O(log n)** or **O(1)**, respectively (though with some precision trade-offs for Binet's formula).

---

## **Optimized Fibonacci Approach**

A better way is to use **memoization (caching)** to store already computed results and avoid redundant calculations.

**Using Memoization with Python `functools.lru_cache`:**

## **Fibonacci Sequence Optimized function**

```python
# Import the lru_cache decorator from functools module
# lru_cache stands for "Least Recently Used Cache"
from functools import lru_cache


# Apply the lru_cache decorator with no size limit (None means unlimited cache)
# This will memoize function calls to avoid redundant calculations
@lru_cache(None)
def fibonacci_optimized(n):
    # Base case: Fibonacci of 0 is 0, and Fibonacci of 1 is 1
    return n if n <= 1 else fibonacci_optimized(n - 1) + fibonacci_optimized(n - 2)
    # Recursive case: F(n) = F(n-1) + F(n-2)


# Test Case:
print(fibonacci_optimized(6))  # Output: 8
```

Let's break down this optimized Fibonacci function using **memoization** with `functools.lru_cache`.

### **How It Works**

1. **`@lru_cache(None)` (Memoization)**  
   - `lru_cache` is a built-in **decorator** in Python that **stores (caches)** function results.  
   - When a function call is repeated with the same input, it **returns the cached result** instead of recalculating it.  
   - `None` means an **unlimited cache size** (it can store all previously computed values).

2. **Recursive Fibonacci Calculation**
   - The function uses **recursion** to compute `fibonacci(n)`.
   - The base cases:

     ```python
     return n if n <= 1
     ```

     If `n` is `0` or `1`, return `n` directly.
   - Otherwise, compute Fibonacci recursively:

     ```python
     fibonacci(n - 1) + fibonacci(n - 2)
     ```

     It breaks the problem into smaller Fibonacci numbers until it reaches the base cases.

---

**Step-by-Step Execution for `fibonacci(6)`**

#### **Without Memoization (Normal Recursion)**

```plaintext
fibonacci(6) = fibonacci(5) + fibonacci(4)
fibonacci(5) = fibonacci(4) + fibonacci(3)
fibonacci(4) = fibonacci(3) + fibonacci(2)
fibonacci(3) = fibonacci(2) + fibonacci(1)
fibonacci(2) = fibonacci(1) + fibonacci(0)
```

This leads to **redundant calculations**.

#### **With `@lru_cache` (Memoization)**

- The first time `fibonacci(6)` is computed, all required subproblems are solved and **stored** in the cache.
- The next time any of these subproblems are needed, the function **returns cached results instantly** instead of recalculating.

---

## Big O Analysis for Optimized Approach

**Time and Space Complexity Analysis:**

Let's analyze the time and space complexity of the `fibonacci_optimized` function that uses `lru_cache` for memoization.

**Time Complexity:**

With `@lru_cache(None)`, the function memoizes all previously computed results. This means each unique `fibonacci_optimized(k)` for `k` from `0` to `n` is computed exactly once.

1. **First call for a given `n`:** The function recursively computes `fibonacci_optimized(n-1)` and `fibonacci_optimized(n-2)`, but these are stored in the cache after the first computation.
2. **Subsequent calls:** If the same `k` is encountered again (e.g., `fibonacci_optimized(n-2)` is called while computing `fibonacci_optimized(n-1)`), the result is retrieved from the cache in `O(1)` time.

Thus, the total number of unique computations is `O(n)` (since we compute `fibonacci_optimized(0)` to `fibonacci_optimized(n)` exactly once each). Each computation (ignoring recursive calls) is `O(1)` (just a lookup or addition).

**Final Time Complexity:** `O(n)`.

**Space Complexity:**

The space complexity is determined by:

1. The depth of the recursion stack.
2. The size of the cache.

3. **Recursion Stack:** The maximum depth of the recursion is `O(n)` (e.g., when computing `fibonacci_optimized(n)`, the longest chain of recursive calls is `n -> n-1 -> n-2 -> ... -> 0`).
4. **Cache Size:** The cache stores all results from `fibonacci_optimized(0)` to `fibonacci_optimized(n)`, which is `O(n)` space.

**Final Space Complexity:** `O(n)` (due to the cache and recursion stack).

**Summary:**

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Key Points

- Without memoization, the time complexity would be exponential (`O(2^n)`), but `lru_cache` reduces it to `O(n)`.
- The space complexity is `O(n)` due to the cache and recursion stack. If you used an iterative approach with memoization, you could reduce the space complexity to `O(1)` (using just two variables to store the last two Fibonacci numbers), but the recursive version here uses `O(n)` space.

---

### **Performance Improvement**

- **Without Memoization:** Time complexity **O(2ⁿ)** (exponential).
- **With `@lru_cache`:** Time complexity **O(n)** (linear), since each Fibonacci number is computed **only once**.

This makes the function **much faster** for large values of `n`.
