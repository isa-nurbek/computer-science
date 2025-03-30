# **Time & Space Complexity Analysis in Computer Science**

Time and space complexity analysis helps us measure how efficiently an algorithm runs and how much memory it consumes. This is crucial for optimizing programs, especially when dealing with large datasets.

---

## **1. Time Complexity**

Time complexity refers to the computational time required by an algorithm as the input size grows. It is typically expressed using **Big-O notation**, which describes the worst-case scenario.

### **Big-O Notation Classes**

| Big-O Notation | Complexity Type   | Example Algorithm                     |
|----------------|-------------------|---------------------------------------|
| **O(1)**       | Constant Time     | Accessing an element in an array      |
| **O(log n)**   | Logarithmic Time  | Binary search                         |
| **O(n)**       | Linear Time       | Traversing an array                   |
| **O(n log n)** | Linearithmic Time | Merge sort, Quick sort (average case) |
| **O(n²)**      | Quadratic Time    | Bubble sort, Selection sort           |
| **O(2ⁿ)**      | Exponential Time  | Fibonacci (naive recursion)           |
| **O(n!)**      | Factorial Time    | Traveling Salesman Problem            |

---

### **Time Complexity Examples in Python**

#### **Example 1: O(1) - Constant Time**

Regardless of the input size, the execution time remains the same.

```python
def get_first_element(arr):
    return arr[0]  # Accessing the first element takes constant time O(1)

print(get_first_element([10, 20, 30, 40]))  # Output: 10
```

---

#### **Example 2: O(n) - Linear Time**

The execution time grows proportionally with input size.

```python
def print_elements(arr):
    for element in arr:
        print(element)  # Iterates through all elements → O(n)

print_elements([1, 2, 3, 4, 5])
```

---

#### **Example 3: O(n²) - Quadratic Time**

Nested loops cause execution time to grow quadratically.

```python
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)  # Two nested loops → O(n²)

print_pairs([1, 2, 3])
```

---

#### **Example 4: O(log n) - Logarithmic Time**

Binary search divides the input size by 2 in each step.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Found the element
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Element not found

arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))  # Output: 3 (index of 7 in the array)
```

Since the search space halves at each step, the complexity is **`O(log n)`**.

---

## **2. Space Complexity**

Space complexity refers to the memory required by an algorithm, including:

1. **Input storage**
2. **Auxiliary space (extra variables, data structures)**
3. **Recursive call stack space**

### **Big-O Notation for Space Complexity**

| Big-O Notation | Space Complexity Example               |
|----------------|----------------------------------------|
| **O(1)**       | Using a few variables (constant space) |
| **O(n)**       | Storing an array of size `n`           |
| **O(n²)**      | 2D matrix storage                      |

---

### **Space Complexity Examples in Python**

#### **Example 1: O(1) - Constant Space**

```python
def add_numbers(a, b):
    sum_val = a + b  # Uses only a few variables
    return sum_val  # O(1) space

print(add_numbers(3, 5))  # Output: 8
```

No extra data structures are used, so space complexity is **`O(1)`**.

---

#### **Example 2: O(n) - Linear Space**

```python
def create_list(n):
    arr = []  
    for i in range(n):
        arr.append(i)  # Stores n elements → O(n) space
    return arr

print(create_list(5))  # Output: [0, 1, 2, 3, 4]
```

Since an array of size **n** is used, the space complexity is **`O(n)`**.

---

#### **Example 3: O(n) - Recursive Function**

Recursion stores intermediate states in the function call stack.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Output: 120
```

The recursion depth is **n**, so the space complexity is **`O(n)`**.

---

## **3. Best, Worst & Average Case Complexity**

For some algorithms, different cases yield different time complexities.

| Case                         | Description                                                                          |
|------------------------------|--------------------------------------------------------------------------------------|
| **Best Case (Ω - Omega)**    | Minimum time an algorithm takes (e.g., Quick Sort in sorted data → `O(n log n)`)     |
| **Worst Case (O - Big-O)**   | Maximum time an algorithm takes (e.g., Bubble Sort on reverse-sorted data → `O(n²)`) |
| **Average Case (Θ - Theta)** | Expected time complexity for random inputs                                           |

### **Example: Quick Sort Complexity**

- **Best Case**: `O(n log n)` (When the pivot splits the array evenly)
- **Worst Case**: `O(n²)` (When the pivot is always the smallest or largest element)
- **Average Case**: `O(n log n)`

---

## **4. Practical Considerations**

1. **Choosing the right algorithm**: Avoid unnecessary inefficiencies.
2. **Data structures matter**: Using a hash map (`O(1)` lookup) vs. a list (`O(n)` lookup) can significantly impact performance.
3. **Optimize loops**: Avoid nested loops when possible.
4. **Recursion vs. Iteration**: Iteration is often more memory-efficient than recursion.

### **Conclusion**

Time and space complexity analysis helps determine how an algorithm will perform as input grows. Using **Big-O notation**, we can express and compare the efficiency of different approaches.

---

## Time & Space Complexity Analysis

Let's analyze the **time and space complexity** for each example in detail. 

### **1. O(1) - Constant Time Complexity**

```python
def get_first_element(arr):
    return arr[0]  # Accessing the first element takes constant time O(1)

print(get_first_element([10, 20, 30, 40]))  # Output: 10
```

**Time Complexity Analysis:**

- The function **directly accesses** the first element of the array (`arr[0]`).
- Accessing an element in an array using an index takes **`O(1)`** time.

**Space Complexity Analysis:**

- The function only uses a single variable for the return value.
- No additional memory is allocated except for the input array.
- **Space Complexity: `O(1)`**.

---

### **2. O(n) - Linear Time Complexity**

```python
def print_elements(arr):
    for element in arr:
        print(element)  # Iterates through all elements → O(n)

print_elements([1, 2, 3, 4, 5])
```

**Time Complexity Analysis:**

- The function iterates through all `n` elements once.
- Each element is printed in **`O(1)`** time.
- Since the loop runs **n** times, the total time complexity is **`O(n)`**.

**Space Complexity Analysis:**

- The function does not create any new data structures.
- It only uses a loop variable (`element`), which takes constant space.
- **Space Complexity: `O(1)`**.

---

### **3. O(n²) - Quadratic Time Complexity**

```python
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)  # Two nested loops → O(n²)

print_pairs([1, 2, 3])
```

**Time Complexity Analysis:**

- The outer loop runs **n** times.
- The inner loop runs **n** times for each iteration of the outer loop.
- Total iterations = **n × n = n²**.
- Hence, the time complexity is **`O(n²)`**.

**Space Complexity Analysis:**

- No extra data structures are used.
- The function only uses loop variables (`i` and `j`).
- **Space Complexity: `O(1)`**.

---

### **4. O(log n) - Logarithmic Time Complexity (Binary Search)**

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Found the element
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Element not found

arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))  # Output: 3 (index of 7 in the array)
```

**Time Complexity Analysis:**

- The search space is **halved** after every iteration.
- Number of iterations ≈ **log₂(n)**.
- The total time complexity is **`O(log n)`**.

**Space Complexity Analysis:**

- The function only uses a few integer variables (`left`, `right`, `mid`).
- No extra data structures are used.
- **Space Complexity: `O(1)`**.

---

### **5. O(1) - Constant Space Complexity**

```python
def add_numbers(a, b):
    sum_val = a + b  # Uses only a few variables
    return sum_val  # O(1) space

print(add_numbers(3, 5))  # Output: 8
```

**Time Complexity Analysis:**

- A single addition operation is performed in **`O(1)`** time.
- No loops or recursion are used.
- **Time Complexity: `O(1)`**.

**Space Complexity Analysis:**

- The function only uses three variables (`a`, `b`, `sum_val`).
- No extra memory is used.
- **Space Complexity: `O(1)`**.

---

### **6. O(n) - Linear Space Complexity**

```python
def create_list(n):
    arr = []  
    for i in range(n):
        arr.append(i)  # Stores n elements → O(n) space
    return arr

print(create_list(5))  # Output: [0, 1, 2, 3, 4]
```

**Time Complexity Analysis:**

- The loop runs **n** times.
- Each `append()` operation takes **`O(1)`** time.
- Total time complexity: **`O(n)`**.

**Space Complexity Analysis:**

- The function creates a **list of size n**.
- The memory required is proportional to `n`.
- **Space Complexity: `O(n)`**.

---

### **7. O(n) - Recursive Function (Factorial)**

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Output: 120
```

**Time Complexity Analysis:**

- The function makes **n** recursive calls.
- Each recursive call takes **`O(1)`** time.
- Total time complexity: **`O(n)`**.

**Space Complexity Analysis:**

- Each recursive call adds a frame to the function call stack.
- The depth of recursion is **n**.
- **Space Complexity: `O(n)`**.

---

## **Comparison Table of Time & Space Complexity**

| Example                        | Time Complexity      | Space Complexity |
|--------------------------------|----------------------|------------------|
| Accessing first element `O(1)` | **`O(1)`**           | **`O(1)`**       |
| Printing elements `O(n)`       | **`O(n)`**           | **`O(1)`**       |
| Printing pairs `O(n²)`         | **`O(n²)`**          | **`O(1)`**       |
| Binary search `O(log n)`       | **`O(log n)`**       | **`O(1)`**       |
| Adding numbers `O(1)`          | **`O(1)`**           | **`O(1)`**       |
| Creating a list `O(n)`         | **`O(n)`**           | **`O(n)`**       |
| Factorial recursion `O(n)`     | **`O(n)`**           | **`O(n)`**       |

---

## **Key Takeaways**

1. **Constant Time `O(1)`** is ideal but not always achievable.
2. **Linear Time `O(n)`** is common when processing all elements in an array.
3. **Quadratic Time `O(n²)`** should be avoided if possible, especially for large inputs.
4. **Logarithmic Time `O(log n)`** is optimal for searching (e.g., binary search).
5. **Recursive Algorithms** often have **`O(n)` space complexity** due to the call stack.
6. **Iterative solutions** are often more space-efficient than recursive ones.
