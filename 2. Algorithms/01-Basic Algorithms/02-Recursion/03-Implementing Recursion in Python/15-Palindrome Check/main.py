# Implementation in Python:


def is_palindrome(s):
    # Base case: strings of length 0 or 1 are always palindromes
    if len(s) <= 1:
        return True
    else:
        # Check if first and last characters match
        first_last_match = s[0] == s[-1]
        # Get the inner substring (excluding first and last characters)
        inner_substring = s[1:-1]
        # Recursively check if inner substring is a palindrome
        return first_last_match and is_palindrome(inner_substring)


# Test Cases:
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
