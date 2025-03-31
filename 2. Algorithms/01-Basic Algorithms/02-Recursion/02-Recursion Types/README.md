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

