# Implementation in Python:


def factorial(n):
    # Base case:
    # If n is 0, return 1 because 0! is defined as 1
    # This also serves as the stopping condition for the recursion
    if n == 0:
        return 1
    else:
        # Recursive case:
        # For n > 0, return n multiplied by factorial of (n-1)
        # This recursively breaks down the problem into smaller subproblems
        # until it reaches the base case
        return n * factorial(n - 1)


# Test Case:
print(factorial(5))  # Output: 120

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:
- **Base Case:** When `n == 0`, the function returns `1` in constant time, `O(1)`.
- **Recursive Case:** For `n > 0`, the function makes one recursive call to `factorial(n - 1)` and performs one
multiplication operation (`n * ...`), which is also `O(1)`.
- The function makes a total of `n + 1` calls (from `n` down to `0`), and each call does `O(1)` work (excluding the recursive part).

- Thus, the total time complexity is `O(n)`.

---

### Space Complexity:
- **Recursive Calls:** Each recursive call adds a new stack frame to the call stack. Since there are `n + 1` calls
(from `n` down to `0`), the maximum depth of the call stack is `O(n)`.
- No additional data structures or memory allocations are used beyond the call stack.

- Thus, the space complexity is `O(n)` due to the recursion stack.

---

### Summary:
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` (due to recursion stack)

### Iterative Alternative (Optimized Space):

- **Time Complexity:** `O(n)` (same as recursive)
- **Space Complexity:** `O(1)` (no recursion stack, just one variable `result`).

The recursive version is less space-efficient due to the call stack, but both versions are linear in time.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break it down step by step.

## **Understanding the Code**

### **1. Base Case**
The function checks if `n` is `0`:
```
if n == 0:
    return 1
```
- This is the base case, which stops the recursion.
- The factorial of `0` is defined as `1` (by convention: `0! = 1`).

### **2. Recursive Case**
If `n` is not `0`, the function calculates:
```
return n * factorial(n - 1)
```
- This means that the function calls itself with `n - 1`.
- It continues calling itself until it reaches the base case (`n == 0`).

---

## **How the Recursion Works (Step-by-Step for `factorial(5)`)**

### **Step 1: Initial Call**
```
factorial(5) 
```
- `5` is not `0`, so we compute:
  ```
  5 * factorial(4)
  ```
  
### **Step 2: Recursive Calls**
Each call reduces `n` by `1`:

1. `factorial(5) = 5 * factorial(4)`
2. `factorial(4) = 4 * factorial(3)`
3. `factorial(3) = 3 * factorial(2)`
4. `factorial(2) = 2 * factorial(1)`
5. `factorial(1) = 1 * factorial(0)`

### **Step 3: Base Case**
When `n == 0`:
```
factorial(0) = 1
```
Now, we start returning values.

---

## **Returning Values (Backtracking Phase)**
The function now returns values step by step:

1. `factorial(0) = 1`
2. `factorial(1) = 1 * 1 = 1`
3. `factorial(2) = 2 * 1 = 2`
4. `factorial(3) = 3 * 2 = 6`
5. `factorial(4) = 4 * 6 = 24`
6. `factorial(5) = 5 * 24 = 120`

### **Final Answer:**
```
factorial(5) = 120
```

---

## **Summary**
1. **Base Case:** Stops recursion when `n == 0`.
2. **Recursive Case:** Calls itself with `n - 1`.
3. **Stack Unwinding:** Once the base case is reached, results are multiplied back up.
4. **Final Answer:** `factorial(5) = 120`.

"""
