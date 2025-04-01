# Implementation in Python:


def binary_search(arr, low, high, target):
    """
    Performs binary search on a sorted array to find the target element.

    Parameters:
    arr (list): A sorted list of elements to search through
    low (int): The starting index of the current search range
    high (int): The ending index of the current search range
    target: The element to search for in the array

    Returns:
    int: The index of the target element if found, otherwise -1
    """

    # Base case: if low exceeds high, the target is not in the array
    if low > high:
        return -1

    # Calculate the middle index of the current search range
    mid = (low + high) // 2

    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid

    # If the middle element is less than the target,
    # recursively search the right half of the current range
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, high, target)

    # If the middle element is greater than the target,
    # recursively search the left half of the current range
    else:
        return binary_search(arr, low, mid - 1, target)


# Test Case:
arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 0, len(arr) - 1, 5))  # Output: 2

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### **Time Complexity Analysis**

The time complexity of the given binary search algorithm is **O(log n)**, where **n** is the number of elements in the array `arr`.

#### **Explanation:**
1. **Divide and Conquer Approach**:  
   - In each recursive call, the search space (the range `[low, high]`) is halved.  
   - This means the problem size reduces by a factor of 2 at each step.

2. **Recurrence Relation**:  
   The recurrence relation for binary search is:  

    T(n) = T(n / 2) + O(1)
   
   - The **O(1)** term accounts for the constant work done in each call (computing `mid`, comparisons, and returning the result).

3. **Solving the Recurrence**:  
   - Applying the Master Theorem (Case 2), or by repeated substitution:  
     
        T(n) = T(n / 2) + 1

        T(n) = T(n / 4) + 1 + 1

    After **k** steps, the problem size reduces to **1**:  

        n / 2^k = 1 ⟹ k = log₂ n  
        
   - Thus, the total time complexity is **O(log n)**.

---

### **Space Complexity Analysis**

The space complexity of this recursive binary search implementation is **O(log n)** in the worst case.

#### **Explanation:**
1. **Recursive Call Stack**:  
   - Each recursive call adds a new stack frame.  
   - The maximum depth of recursion is **log₂ n** (since the problem size halves each time).  

2. **Auxiliary Space**:  
   - No additional data structures are used (only a few variables like `low`, `high`, `mid`).  
   - The dominant factor is the recursion stack, leading to **O(log n)** space.

#### **Comparison with Iterative Binary Search:**
- An **iterative** binary search (using a loop instead of recursion) would have **O(1)** space complexity since
it doesn’t use extra space for recursion.

### **Summary**

| Complexity            | Value    |
|-----------------------|----------|
| **Time**              | O(log n) |
| **Space** (recursive) | O(log n) |
| **Space** (iterative) | O(1)     |

The recursive version is elegant but slightly less space-efficient than the iterative approach. However,
both have the same **O(log n)** time complexity.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Understanding the Binary Search Code**

The given code implements a **recursive** binary search algorithm, which efficiently searches for a target element
in a **sorted** list.

### **Code Breakdown**
```
def binary_search(arr, low, high, target):
```
- This function takes four parameters:
  - `arr`: The sorted list in which we search for the target.
  - `low`: The starting index of the search range.
  - `high`: The ending index of the search range.
  - `target`: The value we are searching for.

---

#### **Base Case: Stopping Condition**
```
if low > high:
    return -1
```
- If `low` is greater than `high`, it means the element is not found, so we return `-1`.

---

#### **Finding the Middle Index**
```
mid = (low + high) // 2
```
- The middle index `mid` is calculated using integer division.

---

#### **Checking the Middle Element**
```
if arr[mid] == target:
    return mid
```
- If the middle element is equal to `target`, we return `mid`, as we have found the target.

---

#### **Recursive Cases**

If the target is greater than the middle element:
```
elif arr[mid] < target:
    return binary_search(arr, mid + 1, high, target)
```
- This means the target is in the right half of the array.
- We call `binary_search` on the right half (`mid + 1` to `high`).

If the target is smaller than the middle element:
```
else:
    return binary_search(arr, low, mid - 1, target)
```
- This means the target is in the left half of the array.
- We call `binary_search` on the left half (`low` to `mid - 1`).

---

### **Example Execution**

Let's analyze how the function works when searching for `5` in `arr = [1, 3, 5, 7, 9]`.

#### **First Call**
```
binary_search([1, 3, 5, 7, 9], 0, 4, 5)
```
- `low = 0`, `high = 4`
- `mid = (0 + 4) // 2 = 2`
- `arr[2] = 5`, which matches the target.
- **Return `2`** (Index of `5` in the array).

#### **Final Output**
```
2
```

### **Conclusion**
- This is an efficient search algorithm for sorted lists.
- The recursive approach is elegant but has extra function call overhead.
- An **iterative** version can reduce space complexity to **O(1)**.

"""
