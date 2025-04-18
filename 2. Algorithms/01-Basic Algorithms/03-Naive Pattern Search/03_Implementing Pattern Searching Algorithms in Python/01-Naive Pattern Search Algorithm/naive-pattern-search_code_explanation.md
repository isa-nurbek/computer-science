# Code Explanation: Naive *Pattern Search Algorithm*

## 1. **naive_pattern_search() Function**

```python
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

Output:
Pattern found at indices: [0, 9, 12]
```

---

### 🔍 **Purpose of the Code**

The goal of this function is to **find all occurrences** of a `pattern` string inside a larger `text` string using a **naive pattern matching algorithm**.

---

### 📦 Function Definition

```python
def naive_pattern_search(text, pattern):
```

- Takes two arguments:
  - `text`: the main string where you are searching.
  - `pattern`: the string (substring) you want to find in `text`.

---

### 📏 Variable Initialization

```python
n = len(text)
m = len(pattern)
result = []
```

- `n`: length of the text.
- `m`: length of the pattern.
- `result`: list that will store the starting indices where the pattern matches the text.

---

### 🔁 Loop Through All Possible Start Positions

```python
for i in range(n - m + 1):
```

- You slide the pattern across the text from left to right.
- `i` is the starting index in `text` where we try to match the pattern.
- We only loop up to `n - m` because if `i` goes beyond that, the pattern won't fully fit.

---

### ✅ Matching Pattern at Each Position

```python
    match = True
    for j in range(m):
        if text[i + j] != pattern[j]:
            match = False
            break
```

- For each `i`, it tries to match all characters in the pattern:
  - `text[i + j]` compares the text character with the corresponding character in the pattern.
  - If **any character mismatches**, set `match = False` and break out of the loop.

---

### 📌 If Pattern Matches, Save the Index

```python
    if match:
        result.append(i)
```

- If `match` is still `True` after checking all characters, it means the pattern matched the text starting at index `i`.
- Append `i` to `result`.

---

### 🔚 Return the Result List

```python
return result
```

- Finally, it returns the list of all starting indices where the pattern was found.

---

### ▶️ Example Usage

```python
text = "AABAACAADAABAABA"
pattern = "AABA"
matches = naive_pattern_search(text, pattern)
print("Pattern found at indices:", matches)
```

Let’s manually verify how it finds matches:

#### Text: `"AABAACAADAABAABA"`

- Indices: `012345678901234`

#### Pattern: `"AABA"` (length = 4)

We try matching at each index from 0 to 12:

- `i = 0`: `text[0:4] = "AABA"` ✅
- `i = 1`: `text[1:5] = "ABAA"` ❌
- `i = 2`: `text[2:6] = "BAAC"` ❌
- `i = 3`: `text[3:7] = "AACA"` ❌
- `i = 4`: `text[4:8] = "ACAA"` ❌
- `i = 5`: `text[5:9] = "CAAD"` ❌
- `i = 6`: `text[6:10] = "AADA"` ❌
- `i = 7`: `text[7:11] = "ADAA"` ❌
- `i = 8`: `text[8:12] = "DAAB"` ❌
- `i = 9`: `text[9:13] = "AABA"` ✅
- `i = 10`: `text[10:14] = "ABAA"` ❌
- `i = 11`: `text[11:15] = "BAAB"` ❌
- `i = 12`: `text[12:16] = "AABA"` ✅

So, matches at:

- `0`
- `9`
- `12`

Hence, output:

```plaintext
Pattern found at indices: [0, 9, 12]
```

---

### 💡 Summary

- This is a simple **brute-force pattern matching** method.
- Time Complexity: **O((n−m+1) × m)** in worst case (n = text length, m = pattern length).
- Works well for small strings or for learning, but **inefficient** for large inputs.
- For more efficiency, algorithms like **KMP**, **Boyer-Moore**, or **Rabin-Karp** are used.

---

## **Big O Analysis:**

### Time and Space Complexity Analysis

Let's analyze the time and space complexity of the `naive_pattern_search` function.

### Time Complexity

- **Outer Loop**: The outer loop runs from `i = 0` to `i = n - m`, where `n` is the length of the text and `m` is the length of the pattern. This loop runs `(n - m + 1)` times.
- **Inner Loop**: For each `i`, the inner loop checks if the substring `text[i..i+m-1]` matches the pattern. In the worst case, it performs `m` comparisons (if there's a full match or a mismatch only at the last character).

**Worst Case Time Complexity**:  
The worst case occurs when:

- The pattern is present at all possible starting positions (e.g., `text = "AAAAA"`, `pattern = "AA"`), or  
- The pattern is not present, but the algorithm checks all possible positions (e.g., `text = "ABCDEF"`, `pattern = "XYZ"`).

In this case, the total number of comparisons is:  
`(n - m + 1) * m ≈ n * m` (if `m << n`).  
Thus, the worst-case time complexity is **`O(n · m)`**.

**Best Case Time Complexity**:  
The best case occurs when the pattern does not match at all in the first character itself (e.g., `text = "ABCDEF"`, `pattern = "XYZ"`).  
In this case, the inner loop breaks after just 1 comparison for each `i`.  
Total comparisons: `(n - m + 1) * 1 ≈ n`.  
Thus, the best-case time complexity is **`O(n)`**.

**Average Case Time Complexity**:  
On average, the inner loop does not run for all `m` characters. Assuming random text and pattern, the average case is closer to **`O(n)`**.

---

### Space Complexity

- The function uses a list `result` to store the starting indices of matches. In the worst case, this list can have up to `O(n)` entries (e.g., `text = "AAAAA"`, `pattern = "A"` → matches at every position).
- Apart from this, only a few variables (`i`, `j`, `match`, `n`, `m`) are used, which take constant space.

Thus, the space complexity is **`O(n)`** in the worst case (due to the `result` list).  
If we ignore the space required for the output (`result`), the auxiliary space complexity is **`O(1)`**.

---

### Summary

- **Time Complexity**:
  - Worst Case: `O(n · m)`
  - Best Case: `O(n)`
  - Average Case: `~O(n)` (for random text/pattern)
- **Space Complexity**:
  - `O(n)` (including output storage)
  - `O(1)` (auxiliary space, excluding output)
