# **Recursion in Computer Science**

Recursion is a technique in computer science where a function calls itself in order to solve a larger problem by breaking it down into smaller, similar subproblems. Each recursive function must have:

1. **Base Case**: The condition that stops the recursion.
2. **Recursive Case**: The part of the function where it calls itself.

---

## **How Recursion Works**

When a function calls itself, it creates a **new function call** on the call stack. Each function call has its **own execution context** (its own local variables and parameters). The recursion continues until it reaches the **base case**, at which point it starts returning values back up the call stack.

![Recursion Steps](./images_of_recursion/recursion.gif)

---

### **Example 1: Factorial Calculation**

The factorial of a number `n` (denoted as `n!`) is:

```plaintext
n! = n * (n-1) * (n-2) * ... * 1
```

#### **Recursive Implementation**

```python
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120
```

**How It Works:**

1. `factorial(5)` → Calls `factorial(4)`, waiting for the result.
2. `factorial(4)` → Calls `factorial(3)`, waiting for the result.
3. `factorial(3)` → Calls `factorial(2)`, waiting for the result.
4. `factorial(2)` → Calls `factorial(1)`, waiting for the result.
5. `factorial(1)` → Hits the **base case** and returns `1`.
6. Now, the functions **return back up**:
   - `factorial(2) = 2 * 1 = 2`
   - `factorial(3) = 3 * 2 = 6`
   - `factorial(4) = 4 * 6 = 24`
   - `factorial(5) = 5 * 24 = 120`

---

### **Example 2: Fibonacci Series**

The Fibonacci sequence is defined as:

```plaintext
F(n) = F(n-1) + F(n-2)
```

Where:

- `F(0) = 0`
- `F(1) = 1`

**Recursive Implementation:**

```python
def fibonacci(n):
    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

print(fibonacci(6))  # Output: 8
```

**How It Works:**

1. `fibonacci(6)` calls `fibonacci(5)` and `fibonacci(4)`.
2. `fibonacci(5)` calls `fibonacci(4)` and `fibonacci(3)`.
3. This process continues until the base cases are reached (`fibonacci(0)` and `fibonacci(1)`).
4. The results are then summed up to get the final result.

> **Issue:** This implementation is inefficient due to **overlapping subproblems** (it calculates `fibonacci(4)` multiple times). We can optimize it using **memoization** (storing results).

---

### **Example 3: Recursively Reverse a String**

```python
def reverse_string(s):
    if len(s) == 0:  # Base case
        return s
    return reverse_string(s[1:]) + s[0]  # Recursive case

print(reverse_string("hello"))  # Output: "olleh"
```

**How It Works:**

1. `reverse_string("hello")` calls `reverse_string("ello") + "h"`.
2. `reverse_string("ello")` calls `reverse_string("llo") + "e"`.
3. This continues until the base case (`""`).
4. The characters are concatenated in **reverse order**.

---

### **Example 4: Recursively Traverse a Directory**

A common use of recursion is traversing a file system.

```python
import os

def list_files(directory):
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):  # If it's a folder, recurse into it
            list_files(full_path)
        else:
            print(full_path)  # If it's a file, print it

# Call the function on a directory
list_files("/path/to/directory")
```

This recursively **explores** subdirectories and prints file paths.

---

## **Recursion vs. Iteration**

| Feature             | Recursion                                       | Iteration         |
|---------------------|-------------------------------------------------|-------------------|
| Uses function calls | Yes                                             | No                |
| Memory usage        | High (call stack)                               | Low               |
| Performance         | Can be slow (without optimization)              | Usually faster    |
| Readability         | More intuitive for problems like tree traversal | Simpler for loops |

---

## **Optimizing Recursion**

1. **Memoization (Caching Results)**
   - Used to **avoid redundant calculations** in Fibonacci and other problems.

   ```python
   from functools import lru_cache

   @lru_cache(None)  # Automatically caches results
   def fibonacci(n):
       if n < 2:
           return n
       return fibonacci(n - 1) + fibonacci(n - 2)

   print(fibonacci(50))  # Fast due to caching
   ```

2. **Tail Recursion (Optimization in Some Languages)**
   - Python does not optimize tail recursion, but some languages (like Scheme) do.

---

### **Conclusion**

Recursion is a powerful technique that simplifies problems by breaking them down into smaller instances of the same problem. However, it can lead to high memory usage if not optimized. For efficiency, **memoization** and **iterative alternatives** are often used.

---

## **Pitfalls of Recursion**

Recursion is a powerful technique, but it comes with several pitfalls that can lead to inefficiencies, excessive memory usage, and even runtime errors.

### **1. Stack Overflow (Excessive Recursion Depth)**

- Every recursive call adds a new frame to the call stack.
- If recursion goes too deep, it can **exceed the maximum recursion depth**, leading to a **stack overflow error**.

#### **Example: Uncontrolled Recursion (Infinite Recursion)**

```python
def infinite_recursion(n):
    print(n)
    infinite_recursion(n + 1)  # No base case!

# Uncommenting this will cause a RecursionError
# infinite_recursion(1)
```

#### **Error Message**

```plaintext
RecursionError: maximum recursion depth exceeded
```

🔹 **Fix**: Always define a **base case** to stop recursion.

---

### **2. Overlapping Subproblems (Redundant Computation)**

- Some recursive solutions repeat calculations unnecessarily, leading to **exponential time complexity**.

#### **Example: Fibonacci Sequence (Inefficient)**

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recomputes values!

print(fibonacci(40))  # Takes a long time
```

#### **Time Complexity**

- **`T(n) = T(n-1) + T(n-2)`**
- **Exponential:** `O(2ⁿ)`

🔹 **Fix**: Use **Memoization** or **Dynamic Programming**.

```python
from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(40))  # Runs instantly!
```

#### **Optimized Time Complexity**

- **`O(n)` with memoization** instead of **`O(2ⁿ)`**.

---

### **3. High Space Complexity (Call Stack Growth)**

Each recursive call **stores variables in memory**. If the recursion depth is **too large**, it consumes a lot of space.

#### **Example: Factorial Function**

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(1000))  # Causes stack overflow!
```

#### **Space Complexity Analysis**

- **`O(n)`** → Each recursive call takes space on the call stack.
- **Fix:** Use an **iterative approach** to reduce memory usage.

🔹 **Iterative Alternative**

```python
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_iterative(1000))  # No stack overflow
```

✅ **Space Complexity: `O(1)`** (constant memory usage).

---

### **4. Tail Recursion is NOT Optimized in Python**

- Some languages **optimize tail recursion**, converting it into iteration internally.
- **Python does NOT support tail call optimization**, leading to stack overflow in deep recursion.

#### **Example: Tail Recursive Function**

```python
def tail_recursive_sum(n, acc=0):
    if n == 0:
        return acc
    return tail_recursive_sum(n - 1, acc + n)

# Python does NOT optimize this
print(tail_recursive_sum(10000))  # Stack Overflow!
```

🔹 **Fix**: Use **iteration instead of tail recursion**.

```python
def iterative_sum(n):
    acc = 0
    while n > 0:
        acc += n
        n -= 1
    return acc

print(iterative_sum(10000))  # Works fine
```

✅ **Space Complexity: `O(1)`** instead of **`O(n)`**.

---

### **5. Difficulty in Debugging and Understanding**

- Recursive functions can be **harder to debug** than iterative ones, as they involve multiple function calls.
- Tracking recursive calls in **deep recursion** can be complex.

#### **Example: Tracing Recursive Calls**

```python
def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(5)
```

#### **Execution Trace**

```plaintext
5
4
3
2
1
Done!
```

✅ While this example is simple, debugging recursive tree traversal or dynamic programming recursion can be tricky.

🔹 **Fix**: Use **print statements**, **recursion trees**, or **debuggers** to track calls.

---

### **6. Recursion Can Be Slower than Iteration**

- Each function call has **overhead** in storing stack frames.
- Iteration can be **faster and more memory-efficient**.

#### **Example: Sum of Numbers**

🔹 **Recursive Version**

```python
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)
```

🔹 **Iterative Version**

```python
def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```

✅ **Performance Comparison**

- Recursive: **`O(n)` time, `O(n)` space** (stack calls)
- Iterative: **`O(n)` time, `O(1)` space**

---

## **Time & Space Complexity Analysis of Recursion**

| Function             | Time Complexity | Space Complexity | Issue                  |
|----------------------|---------------- |------------------|------------------------|
| Factorial `n!`       | **`O(n)`**      | **`O(n)`**       | Stack overflow         |
| Fibonacci (naive)    | **`O(2ⁿ)`**     | **`O(n)`**       | Redundant computations |
| Fibonacci (memoized) | **`O(n)`**      | **`O(n)`**       | Efficient              |
| Tree Traversal (DFS) | **`O(n)`**      | **`O(h)`**       | `h` = tree height      |
| Recursive Sum        | **`O(n)`**      | **`O(n)`**       | Stack overhead         |
| Iterative Sum        | **`O(n)`**      | **`O(1)`**       | Faster                 |

---

## **Best Practices for Recursion**

✅ **1. Always Define a Base Case**  

- Without a base case, recursion **never stops** and causes a stack overflow.

✅ **2. Use Memoization for Overlapping Subproblems**  

- Helps avoid **exponential complexity** (e.g., Fibonacci).

✅ **3. Convert to Iteration When Possible**  

- Iteration is **faster** and **memory-efficient** in many cases.

✅ **4. Avoid Deep Recursion in Python**  

- Python has a **recursion limit** (`sys.getrecursionlimit()` defaults to **1000**).

✅ **5. Use Tail Recursion Only in Optimized Languages**  

- Python **does NOT optimize** tail recursion.

### **Summary**

While recursion is a powerful tool for solving problems like tree traversal, backtracking, and divide-and-conquer algorithms, it comes with pitfalls like **stack overflow, redundant computations, and high memory usage**.  
In many cases, **iteration** is preferable for efficiency, especially when tail recursion is not optimized. **Memoization** can also significantly improve performance in recursive solutions.
