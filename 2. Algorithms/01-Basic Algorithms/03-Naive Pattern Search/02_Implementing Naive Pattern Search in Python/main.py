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

# Output:

"""
Pattern found at indices: [0, 9, 12]

"""

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:
- **Outer Loop**: The outer loop runs from `i = 0` to `i = n - m`, where `n` is the length of the text and `m` is the length
of the pattern. This loop runs `(n - m + 1)` times.
- **Inner Loop**: For each `i`, the inner loop checks if the substring `text[i..i+m-1]` matches the pattern. In the worst case,
it performs `m` comparisons (if there's a full match or a mismatch only at the last character).

**Worst Case Time Complexity**:  
The worst case occurs when:
- The pattern is present at all possible starting positions (e.g., `text = "AAAAA"`, `pattern = "AA"`), or  
- The pattern is not present, but the algorithm checks all possible positions (e.g., `text = "ABCDEF"`, `pattern = "XYZ"`).

In this case, the total number of comparisons is:  
`(n - m + 1) * m ≈ n * m` (if `m << n`).  

Thus, the worst-case time complexity is **O(n · m)**.

**Best Case Time Complexity**:  
The best case occurs when the pattern does not match at all in the first character itself (e.g., `text = "ABCDEF"`,
`pattern = "XYZ"`).  
In this case, the inner loop breaks after just 1 comparison for each `i`.  
Total comparisons: `(n - m + 1) * 1 ≈ n`.  

Thus, the best-case time complexity is **O(n)**.

**Average Case Time Complexity**:  
On average, the inner loop does not run for all `m` characters. Assuming random text and pattern, the average case
is closer to **O(n)**.

---

### Space Complexity:
- The function uses a list `result` to store the starting indices of matches. In the worst case, this list can have
up to `O(n)` entries (e.g., `text = "AAAAA"`, `pattern = "A"` → matches at every position).
- Apart from this, only a few variables (`i`, `j`, `match`, `n`, `m`) are used, which take constant space.

Thus, the space complexity is **O(n)** in the worst case (due to the `result` list).  
If we ignore the space required for the output (`result`), the auxiliary space complexity is **O(1)**.

---

### Summary:

- **Time Complexity**:
  - Worst Case: O(n · m)
  - Best Case: O(n)
  - Average Case: ~O(n) (for random text/pattern)
  
- **Space Complexity**:
  - O(n) (including output storage)
  - O(1) (auxiliary space, excluding output)

"""
