# Implementation in Python:


def bad_char_heuristic(pattern):
    bad_char = [-1] * 256
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    return bad_char


def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    bad_char = bad_char_heuristic(pattern)
    result = []

    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            result.append(s)
            s += m - bad_char[ord(text[s + m])] if s + m < n else 1
        else:
            s += max(1, j - bad_char[ord(text[s + j])])

    return result


# Example usage

print("Boyer-Moore:", boyer_moore_search("AABAACAADAABAABA", "AABA"))

# Output:

"""
Boyer-Moore: [0, 9, 12]

"""
