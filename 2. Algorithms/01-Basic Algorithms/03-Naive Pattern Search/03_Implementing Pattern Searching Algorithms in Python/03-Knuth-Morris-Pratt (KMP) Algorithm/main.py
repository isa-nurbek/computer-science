# Implementation in Python:


def kmp_search(text, pattern):
    """Knuth-Morris-Pratt (KMP) string search algorithm implementation.

    Args:
        text: The text string to search within
        pattern: The pattern string to search for

    Returns:
        A list of starting indices where the pattern is found in the text
    """

    def compute_lps(pattern):
        """Compute the Longest Prefix Suffix (LPS) array for the pattern.

        The LPS array stores the length of the longest proper prefix which is
        also a proper suffix for each prefix of the pattern.

        Args:
            pattern: The pattern string to preprocess

        Returns:
            The LPS array for the given pattern
        """
        m = len(pattern)
        lps = [0] * m  # Initialize LPS array with zeros
        length = 0  # Length of the previous longest prefix suffix
        i = 1  # Current position in pattern

        # Loop to fill the LPS array
        while i < m:
            if pattern[i] == pattern[length]:
                # Characters match, increment length and store in LPS
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # Try shorter prefix/suffix
                    length = lps[length - 1]
                else:
                    # No matching prefix/suffix, set to 0
                    lps[i] = 0
                    i += 1
        return lps

    n = len(text)
    m = len(pattern)

    # Handle edge case of empty pattern
    if m == 0:
        return []

    lps = compute_lps(pattern)  # Preprocess the pattern
    result = []  # Store starting indices of matches
    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < n:
        if pattern[j] == text[i]:
            # Characters match, move both pointers forward
            i += 1
            j += 1

        if j == m:
            # Full pattern matched, record the starting position
            result.append(i - j)
            # Use LPS to skip ahead in the pattern for next potential match
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            # Mismatch after some matches
            if j != 0:
                # Skip the already matched prefix using LPS
                j = lps[j - 1]
            else:
                # No prefix to skip, just move text pointer
                i += 1

    return result


# Example usage

print("KMP:", kmp_search("AABAACAADAABAABA", "AABA"))

# Output:

"""
KMP: [0, 9, 12]

"""
