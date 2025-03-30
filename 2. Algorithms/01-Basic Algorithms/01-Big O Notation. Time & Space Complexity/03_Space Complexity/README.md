# **Space Complexity in Computer Science**

Space complexity refers to the amount of memory an algorithm uses relative to the input size. It includes:

1. **Fixed Part:** Constant memory required by the algorithm (e.g., program instructions, constants, and variables).
2. **Variable Part:** Memory required for dynamic structures such as arrays, recursion stacks, and hash tables.

Space complexity is denoted as **`O(f(n))`**, where **n** is the size of the input.

---

## **Components of Space Complexity**

1. **Constant Space `O(1)`**  
   - Uses a fixed amount of memory, regardless of input size.
   - Example: A function with a few variables.

2. **Linear Space `O(n)`**  
   - Memory grows proportionally with input size.
   - Example: Storing an array of `n` elements.

3. **Quadratic Space `O(n²)`**  
   - Memory grows as the square of the input size.
   - Example: A 2D matrix of size `n x n`.

4. **Logarithmic Space `O(log n)`**  
   - Memory increases logarithmically.
   - Example: Divide-and-conquer algorithms like binary search.

5. **Recursive Stack Space**  
   - Recursive functions use extra space for stack frames.
   - Example: Depth of recursion determines memory usage.

---

## **Examples in Python**

### **1. Constant Space - O(1)**

Regardless of input size, this function only uses a few variables.

```python
def sum_of_two_numbers(a, b):
    sum_value = a + b  # Uses constant space
    return sum_value

print(sum_of_two_numbers(10, 20))
```

- Memory usage is **`O(1)`** because it does not allocate additional memory based on input size.

---

### **2. Linear Space - O(n)**

A function that creates a list proportional to `n` elements.

```python
def create_list(n):
    arr = []  # Uses additional memory
    for i in range(n):
        arr.append(i)  # Space grows as O(n)
    return arr

print(create_list(5))
```

- Memory usage is **`O(n)`** because it stores `n` elements.

---

### **3. Quadratic Space - O(n²)**

A function that creates an `n x n` matrix.

```python
def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]  # O(n²) space
    return matrix

print(create_matrix(3))
```

- Memory usage is **`O(n²)`** because it stores `n²` elements.

---

### **4. Logarithmic Space - O(log n)**

Binary search uses **`O(log n)`** space due to recursion depth.

```python
def binary_search(arr, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)

arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 0, len(arr) - 1, 7))
```

- Recursive depth is **`log(n)`**, so space complexity is **`O(log n)`**.

---

### **5. Recursive Stack Space - O(n)**

Recursion adds function calls to the stack.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)  # Uses O(n) stack space

print(factorial(5))
```

- Recursive depth is **`O(n)`**, leading to **`O(n)`** space complexity.

---

## **Optimizing Space Complexity**

- **Use Iterative Methods Instead of Recursion:** Reduces stack space.
- **Modify Inputs In-Place:** Avoids extra memory allocation.
- **Use Generators Instead of Lists:** Saves memory.
  
### **Example: Using Generators to Reduce Space**

```python
def generate_numbers(n):
    for i in range(n):
        yield i  # Yields values one by one instead of storing in memory

for num in generate_numbers(5):
    print(num)
```

- Instead of storing a list, it **yields** numbers, reducing space complexity to **`O(1)`**.

---

## **Conclusion**

- Space complexity helps analyze memory usage.
- Efficient algorithms optimize space and time.
- Choosing the right data structures and algorithms reduces memory overhead.

---

## Space Complexity Analysis

### **Detailed Space Complexity Analysis for Each Example**

Let’s go through each example and analyze its **space complexity** in detail.

### **1. Constant Space Complexity - O(1)**

```python
def sum_of_two_numbers(a, b):
    sum_value = a + b  # Uses constant space
    return sum_value

print(sum_of_two_numbers(10, 20))
```

**Analysis:**

- Variables `a`, `b`, and `sum_value` take a **fixed** amount of memory.
- No additional data structures (lists, dictionaries, etc.) are used.
- Regardless of the input size, the memory consumption stays the same.

✅ **Space Complexity: `O(1)`** (constant space)

---

### **2. Linear Space Complexity - O(n)**

```python
def create_list(n):
    arr = []  # Uses additional memory
    for i in range(n):
        arr.append(i)  # Space grows as O(n)
    return arr

print(create_list(5))
```

**Analysis:**

- `arr` is an array that stores `n` elements.
- Each integer requires **O(1)** space, and since we store `n` elements, total space used is **`O(n)`**.
- Apart from `arr`, the function only uses a few variables (`i`), which take **`O(1)`** space.
- The total space complexity is determined by `arr`.

✅ **Space Complexity: `O(n)`** (proportional to input size)

---

### **3. Quadratic Space Complexity - O(n²)**

```python
def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]  # O(n²) space
    return matrix

print(create_matrix(3))
```

**Analysis:**

- A **2D matrix** is created with `n` rows and `n` columns.
- Each row contains `n` elements → total elements = `n * n = n²`.
- Each integer takes **`O(1)`** space, so the total memory usage is **`O(n²)`**.
- Other variables (`matrix` reference) take constant space **`O(1)`**.

✅ **Space Complexity: `O(n²)`** (square of input size)

---

### **4. Logarithmic Space Complexity - O(log n)**

```python
def binary_search(arr, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)

arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 0, len(arr) - 1, 7))
```

**Analysis:**

- This is a recursive implementation of **Binary Search**.
- Each recursive call reduces the problem size by **half** (`n → n/2 → n/4 → ... → 1`).
- Maximum recursion depth is **`log₂(n)`** because the input size is divided by 2 at each step.
- Each recursive call stores a few local variables (e.g., `left`, `right`, `mid`), which take **`O(1)`** space.
- The total memory usage is determined by the recursion depth.

✅ **Space Complexity: `O(log n)`** (logarithmic space due to recursion depth)

---

### **5. Recursive Stack Space Complexity - O(n)**

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)  # Uses O(n) stack space

print(factorial(5))
```

**Analysis:**

- This function calls itself recursively until `n == 0`.
- Each recursive call **adds a new stack frame** to memory.
- The maximum recursion depth is **n**, meaning there are **n** stack frames.
- Each function call stores a few local variables (like `n`), taking **`O(1)`** space per call.
- Total memory usage is **`O(n)` `stack frames × O(1)` space per frame**.

✅ **Space Complexity: `O(n)`** (due to recursion stack depth)

**🔹 Optimized Approach (Iterative Factorial)**  
We can reduce space complexity to **`O(1)`** using an iterative approach:

```python
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_iterative(5))
```

- No recursion stack is used.
- Only a few variables (`result`, `i`) are stored in memory.

✅ **Optimized Space Complexity: `O(1)`** (constant space)

---

### **6. Space-Optimized Approach Using Generators**

```python
def generate_numbers(n):
    for i in range(n):
        yield i  # Yields values one by one instead of storing in memory

for num in generate_numbers(5):
    print(num)
```

**Analysis:**

- The function **does not** store a list.
- Instead, it **yields** numbers **one by one**, reducing memory usage.
- At any given time, **only one number** is in memory.
- This makes it highly memory-efficient.

✅ **Space Complexity: `O(1)`** (since it does not store `n` elements)

---

## **Comparison Table of Space Complexity**

| Example                   | Description                        | Space Complexity |
|---------------------------|------------------------------------|------------------|
| Sum of Two Numbers        | Uses a few variables               | **O(1)**         |
| Create List               | Stores `n` elements in a list      | **O(n)**         |
| Create Matrix             | Stores `n²` elements in a 2D array | **O(n²)**        |
| Binary Search (Recursive) | Uses **log(n)** recursion depth    | **O(log n)**     |
| Factorial (Recursive)     | Uses **n** recursion depth         | **O(n)**         |
| Factorial (Iterative)     | Uses a few variables               | **O(1)**         |
| Generator Function        | Yields one value at a time         | **O(1)**         |

---

## **Key Takeaways**

- **`O(1)` Space:** Best case scenario (constant memory usage).
- **`O(n)` Space:** Common in problems storing results in lists or recursion-based solutions.
- **`O(n²)` Space:** Seen in problems involving matrices or graphs.
- **`O(log n)` Space:** Found in recursive algorithms that reduce the problem size exponentially.
- **`O(n)` Recursion:** Can be optimized using **iteration** or **tail-recursion elimination**.
- **Generators save memory** by yielding values instead of storing them.
