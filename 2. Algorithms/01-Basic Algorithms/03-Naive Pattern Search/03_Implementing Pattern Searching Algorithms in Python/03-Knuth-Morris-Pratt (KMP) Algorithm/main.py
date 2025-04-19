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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **1. Preprocessing (LPS Array Construction)**
- **Time Complexity**: `O(m)`  
  - The `compute_lps` function processes the pattern of length `m` in a single pass with `i` and `length` pointers.
  - The `while` loop runs in `O(m)` because `i` increments at least once in every iteration, and `length` adjustments
  (due to mismatches) do not cause more than `O(m)` work in total.
  
- **Space Complexity**: `O(m)`  
  - The LPS array stores `m` integers (one for each character in the pattern).

### **2. Pattern Matching Phase**
- **Time Complexity**: `O(n)`  
  - The main loop processes the text of length `n` with `i` and `j` pointers.
  - `i` only increments (max `n` steps), and `j` adjustments (via `lps`) do not exceed `O(n)` total steps because `j`
  cannot decrease more than it increments.
  
- **Space Complexity**: `O(1)` (additional space)  
  - Only a few variables (`i`, `j`, `result`) are used, and the LPS array was already constructed in preprocessing.

### **Total Complexity**
- **Time**: `O(n + m)`  
  - Preprocessing: `O(m)`  
  - Matching: `O(n)`  
- **Space**: `O(m)` (due to the LPS array)  

### **Why KMP is Efficient**
- Avoids re-checking characters unnecessarily by leveraging the LPS array to skip ahead intelligently after mismatches.
- Brute-force would take `O(n*m)` in the worst case, but KMP guarantees linear time.  

### **Example**
For `text = "ABABDABACDABABCABAB"`, `pattern = "ABABCABAB"`:  
- LPS = `[0, 0, 1, 2, 0, 1, 2, 3, 4]`  
- Matching phase skips redundant comparisons using LPS, resulting in `O(n + m)` time.  

Thus, KMP is optimal for pattern matching with linear scalability.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's walk through the **KMP (Knuth-Morris-Pratt)** pattern searching algorithm and the Python code you provided, in detail.

## 🧠 **Overview of the Problem**

Given:
- A **text** string (e.g. `"AABAACAADAABAABA"`)
- A **pattern** string (e.g. `"AABA"`)

We want to find **all the starting indices** in the text where the pattern occurs.

---

## 🚀 Why Use KMP?

Naively checking every position of the text takes **O(n \* m)** in the worst case. KMP improves this by avoiding unnecessary
comparisons, and runs in **O(n + m)** time by precomputing a helper array called the **LPS** array.

---

## 🔧 `compute_lps(pattern)` – What It Does

This function builds the **LPS (Longest Prefix Suffix)** array.  
For a pattern of length `m`, `lps[i]` stores the **length of the longest proper prefix which is also a suffix** for
the substring `pattern[0...i]`.

### Example:

Pattern = `"AABA"`

Substrings and their longest prefix-suffix match:

| Index | Substring   | LPS value | Why?                      |
|-------|-------------|-----------|---------------------------|
| 0     | A           | 0         | No prefix/suffix          |
| 1     | AA          | 1         | Prefix = A, Suffix = A    |
| 2     | AAB         | 0         | No match                  |
| 3     | AABA        | 1         | A (prefix and suffix)     |

So `lps = [0, 1, 0, 1]`

### Code Explanation:

```
m = len(pattern)
lps = [0] * m
length = 0  # Length of the previous longest prefix suffix
i = 1       # Start from the second character

while i < m:
    if pattern[i] == pattern[length]:
        length += 1
        lps[i] = length
        i += 1
    else:
        if length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
```

---

## 🔍 `kmp_search(text, pattern)` – Main Function

This function:
1. Uses the LPS array to avoid unnecessary comparisons.
2. Finds **all** occurrences of the pattern in the text.

### Variables:

- `n = len(text)`
- `m = len(pattern)`
- `i` = index for **text**
- `j` = index for **pattern**

### How it Works:

```
while i < n:
    if pattern[j] == text[i]:
        i += 1
        j += 1

    if j == m:
        result.append(i - j)  # Match found!
        j = lps[j - 1]        # Reset j using LPS to allow overlap matches
    elif i < n and pattern[j] != text[i]:
        if j != 0:
            j = lps[j - 1]    # Use LPS to skip characters
        else:
            i += 1            # No match, move to next char in text
```

### Example Walkthrough:

Let's take:
- `text = "AABAACAADAABAABA"`
- `pattern = "AABA"`

#### Step-by-step match:

| i (text index) | j (pattern index) | Match?         | Action                    |
|----------------|-------------------|----------------|---------------------------|
| 0              | 0                 | A == A         | i++, j++                  |
| 1              | 1                 | A == A         | i++, j++                  |
| 2              | 2                 | B == B         | i++, j++                  |
| 3              | 3                 | A == A         | i++, j++ → j == 4         |
|                |                   | Match!         | Append 0, j = lps[3] = 1  |
| ...            | ...               | ...            | ...                       |

Eventually, `result = [0, 9, 12]`

---

## ✅ Final Output:

```
print("KMP:", kmp_search("AABAACAADAABAABA", "AABA"))
```

**Output:**
```
KMP: [0, 9, 12]
```

This means that the pattern `"AABA"` occurs at indices 0, 9, and 12 in the text.

---

## 📦 Time and Space Complexity

- **Time Complexity**:
  - Preprocessing LPS: O(m)
  - Searching: O(n)
  - **Total: O(n + m)**

- **Space Complexity**:
  - LPS array: O(m)
  - Result array: Depends on the number of matches

"""
