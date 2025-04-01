# Implementation in Python:


def merge_sort(arr):
    # Base case: If the array has more than one element, we need to split and sort it
    if len(arr) > 1:
        # Find the middle index to divide the array into two halves
        mid = len(arr) // 2

        # Divide the array elements into left and right halves
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort the left half
        merge_sort(left)
        # Recursively sort the right half
        merge_sort(right)

        # Merge the two sorted halves back together
        # Initialize pointers for left (i), right (j), and merged array (k)
        i = j = k = 0

        # Traverse both left and right arrays and compare elements
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # If left element is smaller, place it in the merged array
                arr[k] = left[i]
                i += 1
            else:
                # If right element is smaller or equal, place it in the merged array
                arr[k] = right[j]
                j += 1
            k += 1  # Move to the next position in the merged array

        # Copy any remaining elements from the left array (if any)
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy any remaining elements from the right array (if any)
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Test Case:
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(arr)  # Output: [3, 9, 10, 27, 38, 43, 82]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

Merge Sort is a divide-and-conquer algorithm. The time complexity can be analyzed as follows:

1. **Divide Step**: The array is recursively divided into two halves until the base case (subarrays of size 1 or 0) is reached.
This division takes O(log n) steps because the array is halved at each level of recursion.

2. **Merge Step**: At each level of recursion, merging two sorted subarrays takes O(n) time, where `n` is the size of the 
original array. This is because every element is compared and placed in the correct position exactly once per level.

Since there are O(log n) levels and each level takes O(n) time, the total time complexity is: O(n log n)

This holds for the best, average, and worst-case scenarios because the algorithm always divides the array into two halves
and merges them regardless of the initial order of the elements.

### Space Complexity:

The space complexity is determined by the additional space used during the sorting process:

1. **Recursive Calls**: The recursion depth is O(log n), which contributes to the call stack space. However,
the dominant factor is the temporary arrays created during merging.

2. **Temporary Arrays**: At each merge step, temporary subarrays (`left` and `right`) are created to store the halves of the
original array. The total additional space used at any point is O(n) because the sum of the sizes of all temporary arrays
at any recursion level is `n` (e.g., at the bottom level, you have ( n/2 + n/2 = n ), at the next level up,
( n/4 + n/4 + n/4 + n/4 = n, etc.).

Thus, the space complexity is: O(n)

This is because the algorithm requires additional space proportional to the size of the input array for the temporary subarrays.
If the merge were done in-place, the space complexity could be reduced, but the given implementation is not in-place.

### Summary:
- **Time Complexity**: O(n log n) (all cases).
- **Space Complexity**: O(n) (due to temporary arrays). 

"""
