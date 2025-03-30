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

