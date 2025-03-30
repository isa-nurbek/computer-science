# **Asymptotic Notation: Adding Runtimes**  

When analyzing the time complexity of an algorithm, we often break it down into different parts and sum their complexities. Understanding how to add runtimes is essential when evaluating the efficiency of multi-step algorithms.

## **Basic Idea of Adding Runtimes**

If an algorithm consists of multiple independent steps, the total runtime is the sum of the runtimes of individual steps.

### **Rules to Follow**

1. **Addition Rule**: If an algorithm consists of multiple consecutive steps, their complexities are added.  
   - *Example*: If one step runs in `O(f(n))` time and another in `O(g(n))`, the total complexity is `O(f(n) + g(n))`.  
   - However, in *Big-O* notation, we keep only the *dominant term*, ignoring lower-order terms and constant factors.

2. **Multiplication Rule**: If an algorithm consists of nested loops or recursive calls, the complexities multiply.

---

### **Examples of Adding Runtimes in Python**

#### **Example 1: Two Independent Loops (Addition)**

```python
def example1(n):
    # First loop: O(n)
    for i in range(n):
        print(i)  
    
    # Second loop: O(n)
    for j in range(n):
        print(j)

example1(5)
```

**Analysis:**  

- The first loop runs **n** times → `O(n)`.  
- The second loop runs **n** times → `O(n)`.  
- Since they are sequential (not nested), the total time complexity is:  

```plaintext
O(n) + O(n) = O(2n)
```

- Since we ignore constants in *Big-O* notation, this simplifies to **O(n).**

---

#### **Example 2: Different Growth Rates**

```python
def example2(n):
    # O(n) loop
    for i in range(n):
        print(i)

    # O(n²) loop
    for j in range(n):
        for k in range(n):
            print(j, k)

example2(5)
```

**Analysis:**  

- The first loop runs in **O(n)**.  
- The second nested loop runs in **O(n²)** (since it has two nested loops).  
- The total runtime:  

```plaintext
O(n) + O(n²) = O(n² + n)
```

- The dominant term is `O(n²)`, so we drop the lower-order term `O(n)`:  

```plaintext
O(n² + n) ⇒ O(n²)
```

---

#### **Example 3: Logarithmic and Linear Growth**

```python
import math

def example3(n):
    # O(n) loop
    for i in range(n):
        print(i)

    # O(log n) loop
    j = 1
    while j < n:
        print(j)
        j *= 2

example3(16)
```

**Analysis:**  

- The first loop runs **O(n)** times.  
- The second loop runs **O(log n)** times (since `j` doubles each time).  
- The total runtime:  

```plaintext
O(n) + O(log n)
```

- Since `O(n)` grows much faster than `O(log n)`, the dominant term is **O(n).**

---

#### **Example 4: Multiplication of Runtimes**

```python
def example4(n, m):
    # O(n) loop
    for i in range(n):
        print(i)
    
    # O(m) loop
    for j in range(m):
        print(j)

example4(4, 5)
```

**Analysis:**  

- First loop runs in **O(n)**.  
- Second loop runs in **O(m)**.  
- Since they are sequential, the total runtime is:
  \[
  O(n) + O(m)
  \]
- We cannot simplify further unless we know a relationship between \(n\) and \(m\).

---

### **Conclusion**

- When adding runtimes, **keep the dominant term** (the one that grows the fastest).  
- If multiple steps run sequentially, **their complexities add up**: \(O(f(n)) + O(g(n))\).  
- If one term grows significantly faster, **lower-order terms can be ignored**.  
- **Multiplication** occurs when steps are nested.

---

### **Adding Runtimes with Recursion**  

When dealing with recursive functions, we analyze their runtime using recurrence relations. Adding runtimes in recursion follows similar principles as before:  

- **Sequential recursive calls** → Complexity adds up.  
- **Nested recursive calls (branching recursion)** → Complexity grows multiplicatively.

---

### **Example 1: Simple Recursion (Addition)**

```python
def example1(n):
    if n <= 0:
        return
    print(n)
    example1(n - 1)  # Recursive call

    for i in range(n):  # O(n) loop
        print(i)

example1(5)
```

**Analysis:**

- The recursive function **prints `n` and then calls itself with `n-1`**. This runs **O(n)** times.
- The for-loop runs **O(n)** times at each level.
- The recurrence relation is:
  \[
  T(n) = T(n-1) + O(n)
  \]
- This expands to:
  \[
  O(n) + O(n-1) + O(n-2) + ... + O(1) = O(n^2)
  \]
- Final complexity: **O(n²) (Quadratic Time).**

---

### **Example 2: Tree Recursion (Multiplication of Runtimes)**

```python
def example2(n):
    if n <= 1:
        return
    print(n)
    example2(n - 1)
    example2(n - 1)

example2(3)
```

**Analysis:**

- The function makes **two recursive calls per step**.
- The recurrence relation is:
  \[
  T(n) = 2T(n-1) + O(1)
  \]
- Expanding it:
  \[
  2T(n-1) + 2T(n-2) + 2T(n-3) + ... = O(2^n)
  \]
- Final complexity: **O(2ⁿ) (Exponential Time).**

---

### **Example 3: Mixed Recursive and Iterative Steps**

```python
def example3(n):
    if n <= 0:
        return
    print(n)
    example3(n - 1)  # O(n) recursive call
    for i in range(n):  # O(n) loop
        print(i)

example3(5)
```

**Analysis:**

- Recursive depth is **O(n)**.
- Each level runs a **loop of size `O(n)`**.
- Recurrence relation:
  \[
  T(n) = T(n-1) + O(n)
  \]
- This results in **O(n²)**.

---

### **Key Takeaways**

1. **Single recursion (linear reduction) adds up linearly** → O(n).  
2. **If each step adds a growing workload, it becomes quadratic** → O(n²).  
3. **Tree recursion (multiple calls per step) grows exponentially** → O(2ⁿ).  
4. **Always focus on dominant terms when summing complexities.**  

---

Let's analyze all the recursion cases in detail, breaking down their time complexity step by step.

---

## **Case 1: Simple Recursion (Linear Reduction)**

### **Code:**

```python
def example1(n):
    if n <= 0:
        return
    print(n)  # O(1) operation
    example1(n - 1)  # Recursive call
```

### **Analysis:**

1. The function calls itself **n times** (each time reducing `n` by 1).
2. Each call performs **O(1)** work (printing a number).
3. The recurrence relation is:
   \[
   T(n) = T(n-1) + O(1)
   \]
4. Expanding this recurrence:
   \[
   T(n) = T(n-1) + O(1)
   \]
   \[
   = T(n-2) + O(1) + O(1)
   \]
   \[
   = T(n-3) + O(1) + O(1) + O(1)
   \]
   \[
   = O(n)
   \]
5. **Final Complexity: O(n) (Linear Time).**

---

## **Case 2: Simple Recursion + Iteration (Quadratic Growth)**

### **Code:**

```python
def example2(n):
    if n <= 0:
        return
    print(n)  
    example2(n - 1)  # O(n) recursive call

    for i in range(n):  # O(n) loop
        print(i)
```

### **Analysis:**

1. **Recursive calls:** The function calls itself **n times** → **O(n)** depth.
2. **For-loop execution:** At each level, the loop runs **O(n)** times.
3. The recurrence relation:
   \[
   T(n) = T(n-1) + O(n)
   \]
4. Expanding:
   \[
   T(n) = T(n-1) + O(n)
   \]
   \[
   = T(n-2) + O(n-1) + O(n)
   \]
   \[
   = T(n-3) + O(n-2) + O(n-1) + O(n)
   \]
   \[
   = O(n + (n-1) + (n-2) + ... + 1) = O(n^2)
   \]
5. **Final Complexity: O(n²) (Quadratic Time).**

---

## **Case 3: Tree Recursion (Exponential Growth)**

### **Code:**

```python
def example3(n):
    if n <= 1:
        return
    print(n)
    example3(n - 1)  # First recursive call
    example3(n - 1)  # Second recursive call
```

### **Analysis:**

1. **Recursive calls:** Each function call makes **two new calls**.
2. **Recursive depth:** Since `n` decreases by 1 at each step, the recursion tree has **n levels**.
3. The recurrence relation:
   \[
   T(n) = 2T(n-1) + O(1)
   \]
4. Expanding:
   \[
   T(n) = 2T(n-1) + O(1)
   \]
   \[
   = 2(2T(n-2) + O(1)) + O(1)
   \]
   \[
   = 4T(n-2) + 2O(1) + O(1)
   \]
   \[
   = 8T(n-3) + 4O(1) + 2O(1) + O(1)
   \]
   - Expanding further, this follows the pattern:
   \[
   T(n) = 2^n O(1) = O(2^n)
   \]
5. **Final Complexity: O(2ⁿ) (Exponential Time).**

---

## **Case 4: Mixed Recursion and Iteration**

### **Code:**

```python
def example4(n):
    if n <= 0:
        return
    print(n)
    example4(n - 1)  # O(n) recursive call

    for i in range(n):  # O(n) loop
        print(i)

example4(5)
```

### **Analysis:**

1. **Recursive calls:** The function calls itself **n times** → **O(n)** depth.
2. **For-loop execution:** At each level, the loop runs **O(n)** times.
3. The recurrence relation is the same as **Case 2**:
   \[
   T(n) = T(n-1) + O(n)
   \]
4. Expanding:
   \[
   T(n) = O(n + (n-1) + (n-2) + ... + 1) = O(n^2)
   \]
5. **Final Complexity: O(n²) (Quadratic Time).**

---

## **Summary of Complexity for All Cases**

| **Example** | **Recurrence Relation** | **Time Complexity** | **Growth Rate** |
|------------|------------------------|---------------------|----------------|
| **Simple Recursion** | \(T(n) = T(n-1) + O(1)\) | **O(n)** | **Linear** |
| **Recursion + Iteration** | \(T(n) = T(n-1) + O(n)\) | **O(n²)** | **Quadratic** |
| **Tree Recursion** | \(T(n) = 2T(n-1) + O(1)\) | **O(2ⁿ)** | **Exponential** |
| **Mixed Recursion & Iteration** | \(T(n) = T(n-1) + O(n)\) | **O(n²)** | **Quadratic** |

---

### **Key Takeaways**

1. **Linear recursion (O(n))** occurs when each recursive call makes only **one additional call** and does **O(1) work**.  
2. **Quadratic recursion (O(n²))** occurs when recursion depth is **O(n)** and each step has a **loop of O(n)** work.  
3. **Exponential recursion (O(2ⁿ))** occurs when **each recursive step branches into two or more recursive calls**.  
4. **Always use recurrence relations to break down the complexity.**  
