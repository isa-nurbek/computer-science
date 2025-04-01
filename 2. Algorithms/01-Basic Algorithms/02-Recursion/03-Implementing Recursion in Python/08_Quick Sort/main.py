# Implementation in Python:


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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### **Time Complexity**:

1. **Best Case**: 
   - Occurs when the pivot always divides the array into two nearly equal halves.
   - Recurrence relation: T(n) = 2T(n/2) + O(n) 
   - By the Master Theorem, this is O(n log n).

2. **Average Case**: 
   - On average, the pivot will split the array into balanced parts.
   - Time complexity is still O(n log n).

3. **Worst Case**: 
   - Occurs when the pivot is always the smallest or largest element (e.g., already sorted/reverse-sorted array).
   - Recurrence relation: T(n) = T(n-1) + O(n)
   - This results in O(n²).

### **Space Complexity**:
1. **Worst Case Space Complexity**:
   - Due to recursion, the call stack can grow up to O(n) in the worst case (unbalanced partitions).
   - Additionally, each recursive call creates new subarrays (`left`, `middle`, `right`), which in the worst case can
   take O(n) extra space.
   - **Total space**: O(n).

2. **Best/Average Case Space Complexity**:
   - The depth of recursion is O(log n), and the extra space per level is O(n).
   - **Total space**: O(log n) (if optimized, but in this implementation, it's O(n) due to creating new lists).

### **Optimization Note**:
- The given implementation is not in-place and uses extra space for `left`, `middle`, and `right`. An in-place version
(Lomuto/Hoare partitioning) would reduce space complexity to O(log n) (for recursion stack) in the best/average case.

### **Final Answer**:
- **Time Complexity**:
  - Best/Average Case: O(n log n)
  - Worst Case: O(n²)
- **Space Complexity**:
  - Worst Case: O(n)
  - Best/Average Case: O(n) (due to creating new lists; can be optimized to O(log n) with in-place partitioning).

"""
