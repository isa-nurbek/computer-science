# Big O Notation: Detailed Explanation

Big O notation is a mathematical concept used in computer science to describe the performance or complexity of an algorithm. Specifically, it characterizes the time complexity (how long an algorithm takes to run) or space complexity (how much memory an algorithm uses) as a function of the input size n. Big O notation focuses on the worst-case scenario and provides an upper bound on the growth rate of an algorithm.

**Important Point:**

- *Big O *notation* only describes the asymptotic behavior of a function, not its exact value.
- The *Big O notation* can be used to compare the efficiency of different algorithms or data structures.

Given two functions `f(n)` and `g(n)`, we say that `f(n)` is `O(g(n))` if there exist constants `c > 0` and `n₀ >= 0` such that:

```text
f(n) <= c * g(n) for all n >= n₀
```

In simpler terms, `f(n)` is `O(g(n))` if `f(n)` grows no faster than `c * g(n) for all n >= n₀` where `c` and `n₀` are constants.

*Graphic example for Big O*:

![Big O]()

---

### **1. How It Works**

Big O notation describes the upper bound (worst-case scenario) of an algorithm’s growth rate. It simplifies performance analysis by focusing on the dominant term and ignoring constant factors and lower-order terms.

#### **Key Rules of Big O**

- **Constant factors are ignored** → `O(5n²) → O(n²)`
- **Lower order terms are ignored** → `O(n² + n) → O(n²)`
- **Only the dominant term matters** → The fastest-growing term determines complexity.

---

### **2. Common Big O Complexities**

| Complexity  | Name                  | Example Algorithm     |
|------------|----------------------|----------------------|
| `O(1)`     | Constant Time         | Hash table lookup    |
| `O(log n)` | Logarithmic Time      | Binary search       |
| `O(n)`     | Linear Time           | Looping through an array |
| `O(n log n)` | Linearithmic Time  | Merge Sort, QuickSort (average case) |
| `O(n²)`    | Quadratic Time        | Bubble Sort, Insertion Sort |
| `O(2^n)`   | Exponential Time      | Recursive Fibonacci |
| `O(n!)`    | Factorial Time        | Traveling Salesman Problem |

---

### **3. Examples in Python**

#### **(a) O(1) - Constant Time**

Regardless of input size, the function executes a fixed number of operations.

```python
def constant_time_example(arr):
    return arr[0]  # Always returns the first element
```

✅ **Efficiency:** Always executes in the same amount of time.

---

#### **(b) O(log n) - Logarithmic Time**

Efficient algorithms like binary search reduce the problem size by half each step.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found
```

✅ **Efficiency:** `O(log n)` because the search space is halved at each step.

---

#### **(c) O(n) - Linear Time**

A function that iterates through all elements in an array.

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Not found
```

✅ **Efficiency:** `O(n)`, as the number of operations grows linearly with `n`.

---

#### **(d) O(n log n) - Linearithmic Time**

Sorting algorithms like **Merge Sort**.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

✅ **Efficiency:** `O(n log n)`, as the array is divided recursively (`log n` splits) and merged in `O(n)` time.

---

#### **(e) O(n²) - Quadratic Time**

Nested loops, like **Bubble Sort**.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

✅ **Efficiency:** `O(n²)`, because of two nested loops iterating over `n`.

---

#### **(f) O(2^n) - Exponential Time**

Recursive Fibonacci.

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

✅ **Efficiency:** `O(2^n)`, as each function call branches into two.

---

### **4. Why Big O Matters**

- Helps compare algorithms before implementation.
- Guides optimization efforts.
- Essential for competitive programming and technical interviews.
