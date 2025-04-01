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
