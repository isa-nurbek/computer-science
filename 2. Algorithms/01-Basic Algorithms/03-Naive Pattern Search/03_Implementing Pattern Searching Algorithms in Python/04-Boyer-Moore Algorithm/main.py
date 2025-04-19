# Implementation in Python:


def bad_char_heuristic(pattern):
    """
    Preprocesses the pattern to create the bad character heuristic table.
    This table stores the last occurrence of each character in the pattern.
    If a character doesn't exist in the pattern, it's marked as -1.
    """
    # Initialize all characters as not found (-1)
    bad_char = [-1] * 256  # Assuming ASCII character set

    # Fill the table with the last occurrence of each character in pattern
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i  # Store the rightmost position

    return bad_char


def good_suffix_heuristic(pattern):
    """
    Preprocesses the pattern to create the good suffix heuristic table.
    This table determines how far we can shift the pattern when a mismatch occurs,
    based on the idea that a matching suffix might appear elsewhere in the pattern.
    """
    m = len(pattern)
    good_suffix = [0] * (m + 1)  # Shift table
    border_pos = [0] * (m + 1)  # Position of the border (prefix that matches suffix)

    # Case 1: The matching suffix appears somewhere else in the pattern
    i = m  # Start from end of pattern
    j = m + 1  # Position beyond the pattern
    border_pos[i] = j  # Initialize border position for the suffix

    while i > 0:
        # If characters don't match, keep moving j to find a border
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            # If no good suffix value is set yet, set it
            if good_suffix[j] == 0:
                good_suffix[j] = j - i
            j = border_pos[j]
        # Characters match, move both pointers left
        i -= 1
        j -= 1
        border_pos[i] = j  # Record the border position

    # Case 2: Only part of the matching suffix appears at the beginning
    j = border_pos[0]
    for i in range(m + 1):
        # If no good suffix value was set, use the border position
        if good_suffix[i] == 0:
            good_suffix[i] = j
        # If we reach the border, update j to the next border position
        if i == j:
            j = border_pos[j]

    return good_suffix


def boyer_moore_full(text, pattern):
    """
    Implements the Boyer-Moore string search algorithm using both
    the bad character and good suffix heuristics for maximum efficiency.
    Returns a list of starting indices where the pattern is found in the text.
    """
    n = len(text)
    m = len(pattern)

    # Handle edge cases
    if m == 0 or n < m:
        return []

    # Preprocess the pattern to create heuristic tables
    bad_char = bad_char_heuristic(pattern)  # Bad character table
    good_suffix = good_suffix_heuristic(pattern)  # Good suffix table
    result = []  # To store matching indices

    s = 0  # Current alignment of pattern with text
    while s <= n - m:
        j = m - 1  # Start comparing from the end of pattern

        # Keep moving left while characters match
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            # Full match found
            result.append(s)
            # Shift by the good suffix value for full match
            s += good_suffix[0]
        else:
            # Mismatch occurred - calculate both shifts
            # Bad character shift (can be negative, so we use max with 1)
            bad_char_shift = j - bad_char[ord(text[s + j])]
            # Good suffix shift for the current position
            good_suffix_shift = good_suffix[j + 1]
            # Use the maximum shift value (but at least 1)
            s += max(1, max(bad_char_shift, good_suffix_shift))

    return result


# Example usage

print("Full Boyer-Moore:", boyer_moore_full("AABAACAADAABAABA", "AABA"))

# Output:

"""
Full Boyer-Moore: [0, 9, 12]

"""
