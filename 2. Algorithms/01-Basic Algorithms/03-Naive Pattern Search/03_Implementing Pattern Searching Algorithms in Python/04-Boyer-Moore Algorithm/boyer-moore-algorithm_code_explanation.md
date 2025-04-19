# Code Explanation: *Knuth-Morris-Pratt (KMP) Algorithm*

## 1. **kmp_search() Function**

```python
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

Full Boyer-Moore: [0, 9, 12]

```

---

## 🧠 **Overview of the Problem**

The provided code implements the **Boyer-Moore string search algorithm**, one of the most efficient string matching algorithms. Let's break it down **step-by-step**, explain **each component**, and understand **how it all works together**.

## 🚀 Goal

To find all occurrences of a **pattern** string inside a **text** string using the Boyer-Moore algorithm, which uses two main heuristics:

1. **Bad Character Heuristic**
2. **Good Suffix Heuristic**

---

## 🔧 Part 1: Bad Character Heuristic

```python
def bad_char_heuristic(pattern):
    bad_char = [-1] * 256
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    return bad_char
```

### 🔍 How it works

- Creates a lookup table `bad_char` of size 256 (ASCII character set).
- For each character in the `pattern`, it stores the **last occurrence** (index) of that character.
- If a mismatch occurs at index `j`, we can shift the pattern so that the mismatched character in `text` aligns with its **last occurrence in pattern**.

### 💡 Example

For pattern `"AABA"`, the table will store:

- `bad_char[ord('A')] = 3` (last 'A' at index 3)
- `bad_char[ord('B')] = 2` (last 'B' at index 2)

If mismatch on 'B' at position `j = 2`, shift pattern accordingly.

---

## 🔧 Part 2: Good Suffix Heuristic

```python
def good_suffix_heuristic(pattern):
    m = len(pattern)
    good_suffix = [0] *(m + 1)
    border_pos = [0]* (m + 1)

    i = m
    j = m + 1
    border_pos[i] = j
```

This part computes the **good suffix shift** values.

### 👣 Step-by-step breakdown

#### Step 1: Build `border_pos` table (similar to Z-algorithm idea)

```python
    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if good_suffix[j] == 0:
                good_suffix[j] = j - i
            j = border_pos[j]
        i -= 1
        j -= 1
        border_pos[i] = j
```

This loop finds the **longest border** (i.e., prefix == suffix) and uses it to figure out how far we can safely shift.

#### Step 2: Fill remaining good suffix shifts

```python
    j = border_pos[0]
    for i in range(m + 1):
        if good_suffix[i] == 0:
            good_suffix[i] = j
        if i == j:
            j = border_pos[j]
```

This ensures that any suffix without a proper border still gets a valid shift.

### 💡 Use

- When a mismatch happens after a partial match, shift the pattern based on the longest suffix that is also a prefix.

---

## 🧠 Part 3: Boyer-Moore Full Matcher

```python
def boyer_moore_full(text, pattern):
```

### Inputs

- `text`: main string to search in
- `pattern`: substring to search for

---

### Initial setup

```python
    if m == 0 or n < m:
        return []

    bad_char = bad_char_heuristic(pattern)
    good_suffix = good_suffix_heuristic(pattern)
    result = []
```

- Handles edge cases.
- Precomputes both heuristics.
- Prepares to collect results.

---

### Main loop

```python
    s = 0
    while s <= n - m:
        j = m - 1
```

- `s`: current alignment (start) of pattern with text
- `j`: current index in pattern (start matching from right to left)

#### Character Matching Loop

```python
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
```

- Continues moving left while characters match.

#### If Full Match

```python
        if j < 0:
            result.append(s)
            s += good_suffix[0]
```

- If `j < 0`, pattern is completely matched.
- Add current shift `s` to results.
- Shift pattern using `good_suffix[0]` (since entire pattern matched).

---

### If Mismatch

```python
        else:
            bad_char_shift = j - bad_char[ord(text[s + j])]
            good_suffix_shift = good_suffix[j + 1]
            s += max(1, max(bad_char_shift, good_suffix_shift))
```

- **Bad character shift**: how far to move so mismatched character aligns with last occurrence.
- **Good suffix shift**: how far to move based on already matched suffix.
- Choose the **maximum** of the two to avoid unnecessary rechecking.

---

## ✅ Final Output

```python
return result
```

Returns a list of starting positions in `text` where `pattern` is found.

---

## 🧪 Example

```python
print("Full Boyer-Moore:", boyer_moore_full("AABAACAADAABAABA", "AABA"))
```

Matches found at:

- Index `0`: "AABA"
- Index `9`: "AABA"
- Index `12`: "AABA"

---

## 🧠 Summary

| Component               | Purpose                                                         |
|-------------------------|-----------------------------------------------------------------|
| `bad_char_heuristic`    | Aligns pattern based on last seen character in mismatch         |
| `good_suffix_heuristic` | Aligns pattern based on matched suffix that’s also a prefix     |
| `boyer_moore_full`      | Combines both heuristics to efficiently scan through the text   |

---

## **Big O Analysis:**

### Time and Space Complexity Analysis

### Time Complexity

1. **Preprocessing (Heuristic Calculations):**
   - `bad_char_heuristic`: O(m + 256) → `O(m)` (since 256 is a constant)
   - `good_suffix_heuristic`: `O(m)` (the while loops and for loop all operate in linear time relative to `m`)

2. **Searching Phase:**
   - The main searching loop can have different behaviors:
     - **Best Case:** `O(n/m)` when the pattern doesn't appear in the text and we get maximum shifts every time (e.g., when the last character of the pattern never matches any character in the text).
     - **Average Case:** `O(n)` for typical inputs (better than linear in practice due to skipping characters).
     - **Worst Case:** `O(n*m)` when the pattern and text have many matching characters but the pattern isn't found (e.g., text = "AAAAAA", pattern = "BAAA"). However, with the good suffix rule, the worst case can be improved to O(n + m) in most practical implementations.

### Space Complexity

1. **Preprocessing:**
   - `bad_char_heuristic`: O(256) → `O(1)` (fixed-size array for all ASCII characters).
   - `good_suffix_heuristic`: `O(m)` (stores arrays of size `m + 1`).

2. **Overall Space Complexity:**
   - `O(m)` (dominated by the good suffix heuristic storage).

### Summary

- **Time Complexity:**
  - Best Case: `O(n/m)`
  - Average Case: `O(n)` (often better in practice due to skips)
  - Worst Case: O`(n*m)` (but can be improved to `O(n + m)` with proper optimizations)
- **Space Complexity:** `O(m)` (for storing the heuristics).

The Boyer-Moore algorithm is highly efficient in practice, especially for large texts and patterns, because it often skips large portions of the text. The worst-case scenario is rare in real-world applications.
