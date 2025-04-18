# Implementation in Python:


def rabin_karp_search(text, pattern, prime=101):
    """
    Rabin-Karp algorithm for pattern searching in text.

    Parameters:
        text (str): The text to search within
        pattern (str): The pattern to search for
        prime (int): A prime number used for hashing (helps reduce collisions)

    Returns:
        list: Indices where the pattern is found in the text
    """
    n = len(text)
    m = len(pattern)
    d = 256  # Number of characters in the input alphabet (ASCII)
    h = pow(d, m - 1) % prime  # Precompute h = d^(m-1) for rolling hash
    p = 0  # Hash value for the pattern
    t = 0  # Hash value for current text window
    result = []  # To store matching indices

    # Calculate hash value for pattern and first window of text
    for i in range(m):
        # Pattern hash: (d * previous hash + ASCII of current char) mod prime
        p = (d * p + ord(pattern[i])) % prime
        # Text hash: same calculation for first m characters of text
        t = (d * t + ord(text[i])) % prime

    # Slide the pattern over the text one by one
    for i in range(n - m + 1):
        # If hash values match, check characters one by one
        if p == t:
            # Verify actual characters to handle hash collisions
            if text[i : i + m] == pattern:
                result.append(i)  # Pattern found at index i

        # Calculate hash for next window of text
        if i < n - m:
            # Remove leading character hash, add trailing character hash
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % prime
            # Ensure t is positive (mod can return negative in some languages)
            if t < 0:
                t += prime

    return result


# Example usage

print("Rabin-Karp:", rabin_karp_search("AABAACAADAABAABA", "AABA"))

# Output:

"""
Rabin-Karp: [0, 9, 12]

"""
