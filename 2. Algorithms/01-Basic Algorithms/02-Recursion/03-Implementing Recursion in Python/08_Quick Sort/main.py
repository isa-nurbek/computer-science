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
