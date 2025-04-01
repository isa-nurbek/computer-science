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
