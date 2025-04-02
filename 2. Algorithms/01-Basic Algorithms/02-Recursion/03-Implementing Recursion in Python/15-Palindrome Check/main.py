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
