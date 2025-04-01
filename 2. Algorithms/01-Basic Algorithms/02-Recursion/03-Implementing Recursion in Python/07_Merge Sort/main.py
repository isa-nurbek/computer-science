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
