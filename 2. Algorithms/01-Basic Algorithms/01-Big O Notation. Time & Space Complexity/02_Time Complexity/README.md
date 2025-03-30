# **Time Complexity in Computer Science**

## **What is Time Complexity?**

Time complexity is a measure of the amount of time an algorithm takes to complete as a function of the size of its input. It describes the efficiency of an algorithm and helps us understand how it will scale as input size increases.

Time complexity is typically expressed using **Big O notation**, which describes the upper bound of an algorithm’s running time.

---

## **Big O Notation: Types of Time Complexities**

Here are the most common time complexities:

1. **`O(1)` - Constant Time**
2. **`O(log n)` - Logarithmic Time**
3. **`O(n)` - Linear Time**
4. **`O(n log n)` - Linearithmic Time**
5. **`O(n²)` - Quadratic Time**
6. **`O(2ⁿ)` - Exponential Time**
7. **`O(n!)` - Factorial Time**

Now, let's go over each with Python examples.

---

## **1. O(1) - Constant Time**

An algorithm runs in **constant time** if its execution time does not depend on the input size.

**Example:**

```python
def get_first_element(lst):
    return lst[0]  # Always takes the same time

arr = [10, 20, 30, 40]
print(get_first_element(arr))  # Output: 10
```

✅ **Time Complexity: `O(1)`**  
Regardless of how large `lst` is, the function always accesses the first element in **constant time**.

---

## **2. O(log n) - Logarithmic Time**

An algorithm runs in **logarithmic time** if the input size is reduced by half in each step.

**Example: Binary Search**

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
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 9))  # Output: 4
```

✅ **Time Complexity: `O(log n)`**  
Each iteration halves the search space, making it very efficient for large inputs.

---

## **3. O(n) - Linear Time**

An algorithm runs in **linear time** if the execution time grows proportionally with the input size.

**Example:**

```python
def find_max(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

arr = [10, 50, 20, 40, 30]
print(find_max(arr))  # Output: 50
```

✅ **Time Complexity: `O(n)`**  
We iterate through all `n` elements, so time grows linearly with input size.

---

## **4. O(n log n) - Linearithmic Time**

Common in **efficient sorting algorithms**, like Merge Sort or Quick Sort.

**Example: Merge Sort**

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  # Output: [3, 9, 10, 27, 38, 43, 82]
```

✅ **Time Complexity: `O(n log n)`**  
Divide and conquer reduces the problem size logarithmically, and merging takes O(n).

---

## **5. O(n²) - Quadratic Time**

Algorithms with **nested loops** often have **quadratic time complexity**.

**Example: Bubble Sort**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [5, 3, 8, 4, 2]
print(bubble_sort(arr))  # Output: [2, 3, 4, 5, 8]
```

✅ **Time Complexity: `O(n²)`**  
For each element, we compare it with every other element in a nested loop.

---

## **6. O(2ⁿ) - Exponential Time**

An algorithm runs in **exponential time** if its growth rate doubles at each step.

**Example: Recursive Fibonacci**

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # Output: 5
```

✅ **Time Complexity: `O(2ⁿ)`**  
Each function call branches into two new calls, leading to **exponential growth**.

---

## **7. O(n!) - Factorial Time**

Some brute-force algorithms have **factorial time complexity**, such as generating all permutations.

**Example: Generating Permutations**

```python
from itertools import permutations

def generate_permutations(s):
    return list(permutations(s))

print(generate_permutations("ABC"))
# Output: [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```

✅ **Time Complexity: `O(n!)`**  
As `n` increases, the number of permutations grows **factorially**.

---

## **Conclusion**

| Complexity     | Example Algorithm                | Performance               |
|----------------|----------------------------------|---------------------------|
| **O(1)**       | Accessing an element in an array | 🔥 Fast                   |
| **O(log n)**   | Binary Search                    | ⚡ Very Fast              |
| **O(n)**       | Linear Search                    | ✅ Good                   |
| **O(n log n)** | Merge Sort                       | 🔄 Decent                 |
| **O(n²)**      | Bubble Sort                      | ⚠️ Slow for large `n`     |
| **O(2ⁿ)**      | Fibonacci (Recursive)            | 🚨 Very slow              |
| **O(n!)**      | Permutations                     | ❌ Unusable for large `n` |

Knowing time complexity helps in selecting the most **efficient** algorithm for a given problem.

---

## Time Complexity Analysis

Let's dive deeper into the **Time Complexity Analysis** of each of the examples provided above. I'll break down each algorithm's behavior and how we determine its time complexity.

### **A. O(1) - Constant Time**

#### **Example: Accessing the First Element in an Array**

```python
def get_first_element(lst):
    return lst[0]
```

**Time Complexity Analysis:**

- **What happens inside the function?** The function simply accesses the first element in the list, which is a direct memory lookup.
- **Does the input size matter?** No. Whether the list has 1 element or 1 million, the time to access the first element is constant.
- **Conclusion:** The time taken by this operation does not depend on the size of the input (`lst`). Hence, it's **`O(1)`**.

---

### **B. O(log n) - Logarithmic Time**

#### **Example: Binary Search**

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
    return -1
```

**Time Complexity Analysis:**

- **What happens inside the function?**
  - We start by dividing the list in half and checking the middle element.
  - If the middle element is the target, we return it.
  - If the target is smaller, we search the left half, and if it's larger, we search the right half.
  - Each step cuts the search space in half.

- **How many times can we halve the list?** The number of times we can divide the list by 2 before the search space becomes empty is approximately **`log₂(n)`**.
- **Conclusion:** The number of operations grows logarithmically with respect to the size of the input. Hence, the time complexity is **`O(log n)`**.

---

### **C. O(n) - Linear Time**

#### **Example: Finding the Maximum in a List**

```python
def find_max(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value
```

**Time Complexity Analysis:**

- **What happens inside the function?** We initialize the `max_value` to the first element and then iterate over the list. For each element, we check if it's greater than the current `max_value` and update it if necessary.
- **Does the input size matter?** Yes. In the worst case, we need to check every element in the list.
- **How many iterations?** We perform **n** comparisons, where **n** is the length of the list.
- **Conclusion:** Since the time taken grows linearly with the size of the input, the time complexity is **`O(n)`**.

---

### **D. O(n log n) - Linearithmic Time**

#### **Example: Merge Sort**

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr
```

**Time Complexity Analysis:**

- **What happens inside the function?**
  - **Divide Step:** The list is recursively split into two halves until each sublist has only one element. This step requires **`log₂(n)`** divisions (since the list is halved at each step).
  - **Conquer Step (Merging):** After the splitting is done, the sublists are merged in sorted order. Merging two sublists takes **`O(n)`** time.
- **Total Time Complexity:**
  - At each level of recursion, we merge sublists, which takes **`O(n)`** time.
  - The depth of the recursion is **`log₂(n)`** (since the list is halved each time).
  - Hence, the total time complexity is **`O(n log n)`** because you merge **n** elements across **log n** levels.

---

### **E. O(n²) - Quadratic Time**

#### **Example: Bubble Sort**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

**Time Complexity Analysis:**

- **What happens inside the function?**
  - The function uses two nested loops:
    - The outer loop runs **n** times (once for each element).
    - The inner loop runs **n-i-1** times, where **i** is the current index of the outer loop. This is because, after each pass, the largest element gets "bubbled" to the end.
- **Number of comparisons:**
  - In the worst case, the inner loop runs about **n** times for the first iteration, **n-1** times for the second, and so on.
  - This gives a total of **n + (n-1) + (n-2) + ... + 1** comparisons, which is the sum of the first **n** integers.
- **Conclusion:** The sum of the first **n** integers is **`O(n²)`**, so the time complexity is **`O(n²)`**.

---

### **F. O(2ⁿ) - Exponential Time**

#### **Example: Recursive Fibonacci**

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # Output: 5
```

**Time Complexity Analysis:**

- **What happens inside the function?**
  - The function recursively calls itself to calculate the **n**-th Fibonacci number.
  - The number of function calls grows exponentially, as each call spawns two more calls.
- **How many calls are made?**
  - At each level of recursion, two new calls are made. The total number of function calls grows exponentially as **2ⁿ**.
- **Conclusion:** The time complexity is **`O(2ⁿ)`**, as the number of function calls doubles with each increase in **n**.

---

### **G. O(n!) - Factorial Time**

#### **Example: Generating Permutations**

```python
from itertools import permutations

def generate_permutations(s):
    return list(permutations(s))

print(generate_permutations("ABC"))
```

**Time Complexity Analysis:**

- **What happens inside the function?**
  - The function generates all possible permutations of the input string `s`.
  - If the string has **n** characters, the number of possible permutations is **n!** (factorial).
- **How many permutations?**
  - There are **n!** different ways to arrange **n** elements.
- **Conclusion:** Since there are **n!** permutations to generate, the time complexity is **`O(n!)`**.

---

### **Summary Table of Time Complexities**

| Algorithm                | Time Complexity | Explanation                                        |
|--------------------------|-----------------|----------------------------------------------------|
| **get_first_element**    | **O(1)**        | Constant time operation                            |
| **binary_search**        | **O(log n)**    | Halving the search space each time                 |
| **find_max**             | **O(n)**        | Iterate through every element                      |
| **merge_sort**           | **O(n log n)**  | Divide and conquer approach with linear merge step |
| **bubble_sort**          | **O(n²)**       | Nested loops, comparing adjacent elements          |
| **fibonacci**            | **O(2ⁿ)**       | Exponential growth due to recursion                |
| **generate_permutations**| **O(n!)**       | Generating all possible permutations               |

Each algorithm's time complexity provides insight into how the algorithm behaves as the input size grows. Understanding time complexity helps in selecting efficient algorithms for solving problems with large inputs.
