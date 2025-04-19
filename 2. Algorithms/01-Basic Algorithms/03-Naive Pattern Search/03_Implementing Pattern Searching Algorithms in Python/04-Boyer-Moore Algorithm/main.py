# Implementation in Python:


def bad_char_heuristic(pattern):
    """
    Preprocesses the pattern to create the bad character heuristic table.
    This table stores the last occurrence of each character in the pattern.
    If a character doesn't exist in the pattern, it's marked as -1.
    """
    # Initialize all characters as not found (-1)
    bad_char = [-1] * 256  # Using 256 for all possible ASCII characters

    # Fill the table with the last occurrence of each character in the pattern
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i  # Store the rightmost position of each character

    return bad_char


def boyer_moore_search(text, pattern):
    """
    Searches for all occurrences of pattern in text using the Boyer-Moore algorithm
    with the bad character heuristic.
    Returns a list of starting indices where the pattern is found in the text.
    """
    n = len(text)
    m = len(pattern)
    bad_char = bad_char_heuristic(pattern)  # Preprocess the bad character table
    result = []  # To store the starting positions of matches

    s = 0  # s is the shift of the pattern with respect to text
    while s <= n - m:
        j = m - 1  # Start comparing from the end of the pattern

        # Keep moving left while characters match
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            # If we've passed the start of the pattern, we found a match
            result.append(s)

            # Shift the pattern so that the next character in text
            # aligns with the last occurrence of it in pattern
            if s + m < n:  # Check if we're not at the end of the text
                s += m - bad_char[ord(text[s + m])]
            else:
                s += 1
        else:
            # If there's a mismatch, shift the pattern to align the bad character
            # in the text with the last occurrence of it in the pattern
            # The shift is at least 1 to ensure we make progress
            shift = j - bad_char[ord(text[s + j])]
            s += max(1, shift)

    return result


# Example usage

print("Boyer-Moore:", boyer_moore_search("AABAACAADAABAABA", "AABA"))

# Output:

"""
Boyer-Moore: [0, 9, 12]

"""
