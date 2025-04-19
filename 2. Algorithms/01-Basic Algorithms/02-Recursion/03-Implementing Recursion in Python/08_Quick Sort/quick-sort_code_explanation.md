# Code Explanation: *Quick Sort*

## **Quick Sort function**

```python
def quick_sort(arr):
    """
    Sorts a list using the QuickSort algorithm.

    QuickSort is a divide-and-conquer algorithm that works by:
    1. Selecting a 'pivot' element from the array
    2. Partitioning the other elements into two sub-arrays:
       - Elements less than the pivot
       - Elements greater than the pivot
    3. Recursively sorting the sub-arrays

    Args:
        arr: List of elements to be sorted

    Returns:
        A new list containing the sorted elements
    """

    # Base case: if array has 0 or 1 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose pivot element (middle element in this implementation)
    pivot = arr[len(arr) // 2]

    # Partition the array into three parts:
    # 1. Elements less than the pivot
    left = [x for x in arr if x < pivot]

    # 2. Elements equal to the pivot (handles duplicate values)
    middle = [x for x in arr if x == pivot]

    # 3. Elements greater than the pivot
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right partitions,
    # then combine with the middle for final sorted result
    return quick_sort(left) + middle + quick_sort(right)


# Test Case:

print(quick_sort([3, 6, 8, 10, 1, 2, 1]))
# Output: [1, 1, 2, 3, 6, 8, 10]
```

## **Understanding QuickSort**

QuickSort is a **divide-and-conquer** sorting algorithm that:

1. Selects a **pivot** element.
2. Partitions the list into three parts:
   - Elements **less than** the pivot.
   - Elements **equal to** the pivot.
   - Elements **greater than** the pivot.
3. Recursively sorts the smaller sublists.
4. Combines the sorted sublists to produce the final sorted array.

---

### **Code Breakdown**

#### **Step 1: Base Case**

```python
if len(arr) <= 1:
    return arr
```

- If the list has **one or zero** elements, it is already sorted.
- The function returns the array as is.

#### **Step 2: Choosing the Pivot**

```python
pivot = arr[len(arr) // 2]
```

- The pivot is chosen as the middle element of the list.

#### **Step 3: Partitioning**

```python
left = [x for x in arr if x < pivot]   # All elements less than the pivot
middle = [x for x in arr if x == pivot]  # All elements equal to the pivot
right = [x for x in arr if x > pivot]   # All elements greater than the pivot
```

- The list is divided into three parts:
  - `left` contains elements smaller than the pivot.
  - `middle` contains elements equal to the pivot.
  - `right` contains elements greater than the pivot.

#### **Step 4: Recursively Sorting**

```python
return quick_sort(left) + middle + quick_sort(right)
```

- The function recursively sorts `left` and `right` sublists.
- Finally, it concatenates `left + middle + right` to get the sorted array.

---

### **Example Walkthrough**

#### **Input:**

```python
quick_sort([3, 6, 8, 10, 1, 2, 1])
```

#### **First Call**

- `arr = [3, 6, 8, 10, 1, 2, 1]`
- `pivot = arr[len(arr) // 2] = 8`
- Partitioning:
  - `left = [3, 6, 1, 2, 1]`
  - `middle = [8]`
  - `right = [10]`
- Recursively call `quick_sort(left)` and `quick_sort(right)`.

#### **Second Call (Sorting Left: [3, 6, 1, 2, 1])**

- `pivot = 1`
- Partitioning:
  - `left = []`
  - `middle = [1, 1]`
  - `right = [3, 6, 2]`
- Recursively call `quick_sort(left)` (returns `[]`) and `quick_sort(right)`.

#### **Third Call (Sorting Right: [3, 6, 2])**

- `pivot = 6`
- Partitioning:
  - `left = [3, 2]`
  - `middle = [6]`
  - `right = []`
- Recursively call `quick_sort(left)` and `quick_sort(right)`.

#### **Fourth Call (Sorting Left: [3, 2])**

- `pivot = 2`
- Partitioning:
  - `left = []`
  - `middle = [2]`
  - `right = [3]`
- Recursively call `quick_sort(left)` (returns `[]`) and `quick_sort(right)` (returns `[3]`).

---

### **Final Sorted Output**

Combining all recursive calls:

```plaintext
[] + [1, 1] + [2] + [3] + [6] + [8] + [10] = [1, 1, 2, 3, 6, 8, 10]
```

So, the final sorted array is:

```python
[1, 1, 2, 3, 6, 8, 10]
```

---

## Big O Analysis

### Time and Space Complexity Analysis

### **Time Complexity**

1. **Best Case**:
   - Occurs when the pivot always divides the array into two nearly equal halves.
   - Recurrence relation: `T(n) = 2T(n/2) + O(n)`
   - By the Master Theorem, this is `O(n log n)`.

2. **Average Case**:
   - On average, the pivot will split the array into balanced parts.
   - Time complexity is still `O(n log n)`.

3. **Worst Case**:
   - Occurs when the pivot is always the smallest or largest element (e.g., already sorted/reverse-sorted array).
   - Recurrence relation: `T(n) = T(n-1) + O(n)`
   - This results in `O(n²)`.

### **Space Complexity**

1. **Worst Case Space Complexity**:
   - Due to recursion, the call stack can grow up to `O(n)` in the worst case (unbalanced partitions).
   - Additionally, each recursive call creates new subarrays (`left`, `middle`, `right`), which in the worst case can take `O(n)` extra space.
   - **Total space**: `O(n)`.

2. **Best/Average Case Space Complexity**:
   - The depth of recursion is `O(log n)`, and the extra space per level is `O(n)`.
   - **Total space**: `O(log n)` (if optimized, but in this implementation, it's `O(n)` due to creating new lists).

### **Optimization Note**

- The given implementation is not in-place and uses extra space for `left`, `middle`, and `right`. An in-place version (Lomuto/Hoare partitioning) would reduce space complexity to `O(log n)` (for recursion stack) in the best/average case.

### **Final Answer**

- **Time Complexity**:
  - Best/Average Case: `O(n log n)`
  - Worst Case: `O(n²)`
- **Space Complexity**:
  - Worst Case: `O(n)`
  - Best/Average Case: `O(n)` (due to creating new lists; can be optimized to `O(log n)` with in-place partitioning).
