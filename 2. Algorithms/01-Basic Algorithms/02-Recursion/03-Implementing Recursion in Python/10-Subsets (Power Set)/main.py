# Implementation in Python:


def subsets(nums):
    """
    Generates all possible subsets (the power set) of a given list of unique numbers.
    Uses a recursive approach to build subsets by including/excluding each element.

    Args:
        nums: List of unique integers

    Returns:
        List of lists containing all possible subsets
    """

    # Base case: if input list is empty, return list containing only the empty subset
    if not nums:
        return [[]]

    # Recursive case:
    # 1. Get all subsets without the first element (recursive call on nums[1:])
    without_first = subsets(nums[1:])

    # 2. Generate all subsets that include the first element:
    #    - Take each subset from the 'without_first' result
    #    - Add the first element to it
    with_first = [[nums[0]] + subset for subset in without_first]

    # Combine subsets that include first element with those that don't
    return with_first + without_first


# Test Case:

print(subsets([1, 2, 3]))
# Output: [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
