# Implementation in Python:


def rabin_karp_search(text, pattern, prime=101):
    n = len(text)
    m = len(pattern)
    d = 256  # number of characters in the input alphabet
    h = pow(d, m - 1) % prime
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    result = []

    # Calculate hash value for pattern and first window
    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p == t:
            if text[i : i + m] == pattern:
                result.append(i)

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t < 0:
                t += prime

    return result


# Example usage

print("Rabin-Karp:", rabin_karp_search("AABAACAADAABAABA", "AABA"))

# Output:

"""
Rabin-Karp: [0, 9, 12]

"""
