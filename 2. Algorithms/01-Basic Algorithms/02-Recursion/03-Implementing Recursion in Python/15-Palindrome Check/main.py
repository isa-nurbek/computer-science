# Implementation in Python:


def is_palindrome(s, left=0, right=None):
    """
    Recursively checks if a string is a palindrome (reads the same forwards and backwards).

    Args:
        s: The string to check
        left: Starting index (defaults to 0)
        right: Ending index (defaults to None, which sets it to last character index)

    Returns:
        True if the string is a palindrome, False otherwise
    """

    # Initialize right index on first function call
    if right is None:
        right = len(s) - 1  # Set to last character index if not provided

    # Base case: we've checked all character pairs or empty string
    if left >= right:
        return True

    # Recursive case:
    # 1. Check if current left and right characters match
    # 2. Recursively check the next pair of characters (moving inward)
    return s[left] == s[right] and is_palindrome(s, left + 1, right - 1)


# Test Cases:
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### **Time Complexity:**

The function checks if a string `s` is a palindrome by comparing characters symmetrically from the start (`left`) and
end (`right`) of the string, moving towards the center.

- **Base Case:** If `left >= right`, the recursion stops, and this takes `O(1)` time.
- **Recursive Step:** Each recursive call compares `s[left]` and `s[right]` (`O(1)` operation) and then calls itself
with `left + 1` and `right - 1`.

Since the function processes each character in the string **at most once**, the total number of recursive calls is
proportional to half the length of the string (`n/2`), where `n = len(s)`. Therefore:

- **Time Complexity:** `O(n)` (linear time), where `n` is the length of the string.

### **Space Complexity:**

The space complexity is determined by the **maximum depth of the recursion stack**.

- In the worst case (when the string is a palindrome or when `left` and `right` meet in the middle), the recursion goes up
to `n/2` levels deep.
- Each recursive call consumes `O(1)` space (for storing `left` and `right`).

Thus:
- **Space Complexity:** `O(n)` (due to recursion stack).  
  *(In the worst case, it's `O(n)` for very long strings, but since we only recurse up to `n/2` times, it's still linear.)*

### **Optimization Note:**
If we were to implement this **iteratively** (using a loop instead of recursion), the space complexity would reduce to `O(1)`
(constant space), since we wouldn't use the call stack. However, the recursive approach is elegant and easy to understand.

### **Final Answer:**
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` (due to recursion stack)  
  *(Can be optimized to `O(1)` with an iterative approach.)*

"""
