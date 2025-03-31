# Recursion Types

Recursion is a programming technique where a function calls itself to solve a problem. There are several types of recursion, each with its unique characteristics and use cases. Let's explore these types in detail along with Python examples.

## **1. Direct Recursion**

A function is directly recursive if it calls itself within its definition.

*How it Works:*

- The function calls itself with modified parameters until it reaches a base condition.
- Once the base condition is met, the function starts returning values.

### **Example: Factorial Calculation**

```python
def factorial(n):
    if n == 0 or n == 1:  # Base condition
        return 1
    return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Output: 120
```

---

## **2. Indirect Recursion**

A function is indirectly recursive if it calls another function, which then calls the original function.

*How it Works:*

- Function `A` calls function `B`, and function `B` calls function `A`, continuing this cycle.
- A base case ensures the recursion stops.

### **Example: Even-Odd Check**

```python
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)

print(is_even(10))  # Output: True
print(is_odd(11))   # Output: True
```

---

## **3. Tail Recursion**

A recursive function is tail-recursive if the recursive call is the last operation performed before returning.

*How it Works:*

- It optimizes memory usage because there is no need to keep track of previous states.
- Some programming languages optimize tail recursion to prevent excessive stack usage (Python does not perform this optimization).

### **Example: Tail Recursive Factorial**

```python
def tail_factorial(n, acc=1):
    if n == 0 or n == 1:
        return acc
    return tail_factorial(n - 1, acc * n)  # Tail recursion

print(tail_factorial(5))  # Output: 120
```

---

## **4. Non-Tail Recursion**

A function is non-tail recursive if the recursive call is **not** the last operation before returning.

*How it Works:*

- It requires additional stack space since intermediate computations need to be stored.
- The return expression contains computations after the recursive call.

### **Example: Fibonacci Series**

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Not a tail call

print(fibonacci(6))  # Output: 8
```

---

## **5. Linear Recursion**

A function is **linearly recursive** if it makes at most one recursive call per function execution.

### **Example: Sum of Digits**

```python
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(1234))  # Output: 10
```

---

## **6. Binary Recursion**

A function is **binary recursive** if it makes two recursive calls per execution.

### **Fibonacci Series Example**

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Two recursive calls

print(fibonacci(5))  # Output: 5
```

---

## **7. Mutual Recursion**

Mutual recursion occurs when two or more functions call each other in a recursive manner.

### **Example: Even-Odd Check (Alternate)**

```python
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)

print(is_even(4))  # Output: True
print(is_odd(5))   # Output: True
```

---

## **8. Nested Recursion**

A function has **nested recursion** when it makes a recursive call inside another recursive call.

### **Example: Nested Recursion**

```python
def nested_recursion(n):
    if n > 100:
        return n - 10
    return nested_recursion(nested_recursion(n + 11))

print(nested_recursion(95))  # Output: 91
```

---

## **Conclusion**

Recursion is a powerful concept in computer science, and different types of recursion are suited for different problems. Here’s a quick summary:

| **Recursion Type** | **Characteristics**                                 | **Example**       |
|--------------------|-----------------------------------------------------|-------------------|
| Direct Recursion   | Function calls itself directly                      | Factorial         |
| Indirect Recursion | Function A calls Function B, which calls Function A | Even-Odd Check    |
| Tail Recursion     | Recursive call is the last operation                | Tail Factorial    |
| Non-Tail Recursion | Operations occur after recursive call               | Fibonacci         |
| Linear Recursion   | Single recursive call per function execution        | Sum of Digits     |
| Binary Recursion   | Two recursive calls per function execution          | Fibonacci         |
| Mutual Recursion   | Two functions call each other                       | Even-Odd Check    |
| Nested Recursion   | Recursive calls within recursive calls              | Nested Function   |

---

## Recursion Types Detailed Explanations

Let's go through each type of recursion in detail, including its **working mechanism** and **time & space complexity analysis**.

## **01. Direct Recursion**

A function is **directly recursive** when it calls itself within its own definition.

### **Example - Factorial Calculation**

```python
def factorial(n):
    if n == 0 or n == 1:  # Base condition
        return 1
    return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Output: 120
```

**Working:**

- The function keeps calling itself with `n-1` until `n == 0`.
- At `n == 0`, it returns `1` and starts resolving the recursive calls.

**Time Complexity:**

- **T(n) = T(n-1) + O(1)**
- Since it makes **one** recursive call per step, it runs in **`O(n)`** time.

**Space Complexity:**

- **`O(n)`** because each call is stored on the call stack until the base case is reached.

---

## **02. Indirect Recursion**

In **indirect recursion**, function `A` calls function `B`, and function `B` calls function `A`.

### **Example - Even-Odd Check**

```python
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)

print(is_even(10))  # Output: True
print(is_odd(11))   # Output: True
```

**Working:**

- `is_even(10)` calls `is_odd(9)`, which calls `is_even(8)`, and so on, until `n == 0`.

**Time Complexity:**

- Each call reduces `n` by 1.
- **`O(n)`** time.

**Space Complexity:**

- The recursion depth is `O(n)`, so space complexity is **`O(n)`**.

---

## **03. Tail Recursion**

A function is **tail-recursive** if the **recursive call is the last operation** before returning.

### **Example - Tail Recursive Factorial**

```python
def tail_factorial(n, acc=1):
    if n == 0 or n == 1:
        return acc
    return tail_factorial(n - 1, acc * n)

print(tail_factorial(5))  # Output: 120
```

**Working:**

- Instead of storing intermediate results on the call stack, we pass them as parameters (`acc`).
- Some languages optimize tail recursion to avoid extra stack frames (Python **does not** do this).

**Time Complexity:**

- **`O(n)`**, since it makes `n` calls.

**Space Complexity:**

- If optimized (Tail Recursion Optimization - TRO): **`O(1)`**
- In Python (no TRO): **`O(n)`**

---

## **04. Non-Tail Recursion**

A function is **non-tail recursive** when operations occur **after** the recursive call.

### **Example - Fibonacci Series**

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8
```

**Working:**

- It calls `fibonacci(n-1)` and `fibonacci(n-2)`, creating a **tree-like recursion**.

**Time Complexity:**

- **T(n) = T(n-1) + T(n-2) + O(1)**
- Exponential complexity: **`O(2ⁿ)`**

**Space Complexity:**

- Maximum recursion depth: **`O(n)`** (due to the call stack).

---

## **05. Linear Recursion**

A function is **linearly recursive** if it makes **only one recursive call** per function execution.

### **Example - Sum of Digits**

```python
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(1234))  # Output: 10
```

**Working:**

- Extracts last digit `(n % 10)`, adds it, and calls itself with `n // 10`.

**Time Complexity:**

- **`O(log n)`** (number of digits in `n`).

**Space Complexity:**

- **`O(log n)`** (stack size for recursive calls).

---

## **06. Binary Recursion**

A function is **binary recursive** if it makes **two recursive calls** per function execution.

### **Example Fibonacci Series**

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # Output: 5
```

**Working:**

- Two recursive calls per function execution.
- Forms a binary tree of calls.

**Time Complexity:**

- **O(2ⁿ)** (Exponential growth)

**Space Complexity:**

- **`O(n)`** (Call stack depth)

---

## **07. Mutual Recursion**

Two or more functions call each other in a recursive manner.

### **Example Even-Odd Check**

```python
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)

print(is_even(4))  # Output: True
print(is_odd(5))   # Output: True
```

**Working:**

- Each function calls the other until `n == 0`.

**Time Complexity:**

- **`O(n)`** (Each call reduces `n` by 1).

**Space Complexity:**

- **`O(n)`** (Stack depth).

---

## **08. Nested Recursion**

A function has **nested recursion** when it makes a **recursive call inside another recursive call**.

### **Example - Nested Recursion**

```python
def nested_recursion(n):
    if n > 100:
        return n - 10
    return nested_recursion(nested_recursion(n + 11))

print(nested_recursion(95))  # Output: 91
```

**Working:**

- Calls itself with `n + 11`, and then recursively calls that result.

**Time Complexity:**

- **`O(log n)`** (Since `n` jumps in large steps).

**Space Complexity:**

- **`O(log n)`** (Call stack depth).

---

## **Summary of Time & Space Complexity**

| Recursion Type         | Time Complexity | Space Complexity            |
|------------------------|-----------------|-----------------------------|
| **Direct Recursion**   | `O(n)`          | `O(n)`                      |
| **Indirect Recursion** | `O(n)`          | `O(n)`                      |
| **Tail Recursion**     | `O(n)`          | `O(n)` `O(1)` if optimized  |
| **Non-Tail Recursion** | `O(2ⁿ)`         | `O(n)`                      |
| **Linear Recursion**   | `O(log n)`      | `O(log n)`                  |
| **Binary Recursion**   | `O(2^n)`        | `O(n)`                      |
| **Mutual Recursion**   | `O(n)`          | `O(n)`                      |
| **Nested Recursion**   | `O(log n)`      | `O(log n)`                  |

### **Summary**

- **Tail recursion** is memory efficient (if optimized).
- **Binary recursion** is expensive.
- **Nested recursion** reduces function calls efficiently.
- **Linear recursion** is commonly used in numerical problems.
