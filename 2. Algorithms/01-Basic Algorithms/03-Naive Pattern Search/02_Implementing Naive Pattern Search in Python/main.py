# Implementation in Python:


def naive_pattern_search(text, pattern):
    """
    Performs a naive (brute-force) pattern search in a given text.

    Args:
        text: The string to search within
        pattern: The string pattern to search for

    Returns:
        A list of starting indices where the pattern is found in the text
    """

    n = len(text)  # Length of the text
    m = len(pattern)  # Length of the pattern
    result = []  # To store the starting indices of matches

    # Slide the pattern over the text one by one
    for i in range(n - m + 1):
        match = True  # Assume there's a match initially

        # Check character by character for current position i
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False  # Mismatch found
                break  # No need to check further for this i

        # If entire pattern matched, record the starting index
        if match:
            result.append(i)

    return result


# Example usage
text = "AABAACAADAABAABA"
pattern = "AABA"
matches = naive_pattern_search(text, pattern)
print("Pattern found at indices:", matches)
