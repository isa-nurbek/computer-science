# Implementation in Python:


def naive_pattern_search(text, pattern):
    n = len(text)
    m = len(pattern)
    result = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            result.append(i)

    return result


# Example usage
text = "AABAACAADAABAABA"
pattern = "AABA"
matches = naive_pattern_search(text, pattern)
print("Pattern found at indices:", matches)
