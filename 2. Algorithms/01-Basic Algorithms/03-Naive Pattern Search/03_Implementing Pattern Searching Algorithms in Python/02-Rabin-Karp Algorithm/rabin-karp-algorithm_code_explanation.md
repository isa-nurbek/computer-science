# Code Explanation: Rabin-Karp Algorithm Implementation in Python

## 1. **rabin_karp_search() Function**

```python
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

Rabin-Karp: [0, 9, 12]

```

---

### 🔍 **Purpose of the Code**

Find all **starting indices** in the `text` where the `pattern` appears.

---

### 🔧 **Parameters**

```python
def rabin_karp_search(text, pattern, prime=101):
```

- `text`: The string we want to search in.
- `pattern`: The substring we want to find.
- `prime`: A large prime number used for hashing to reduce collisions.

---

### 📌 **Variables and Setup**

```python
n = len(text)        # Length of the text
m = len(pattern)     # Length of the pattern
d = 256              # Size of the alphabet (extended ASCII)
```

#### Rolling Hash

```python
h = pow(d, m - 1) % prime
```

- `h` is used to remove the leading character when sliding the window.
- `pow(d, m - 1)` calculates `d^m-1`, which helps in removing the contribution of the first character of the current window.

```python
p = 0  # Hash value for the pattern
t = 0  # Hash value for the text window
result = []  # List to store the result (starting indices)
```

---

### 🔢 **Initial Hash Computation**

```python
for i in range(m):
    p = (d * p + ord(pattern[i])) % prime
    t = (d * t + ord(text[i])) % prime
```

This loop computes:

- `p`: Hash of the pattern
- `t`: Hash of the first `m` characters (first window) of the text

Both use the **same rolling hash formula**, similar to calculating a number in base-256.

---

### 🔄 **Main Loop**

```python
for i in range(n - m + 1):
```

This loop slides the pattern over the text.

#### ✅ **Hash Match**

```python
    if p == t:
        if text[i:i + m] == pattern:
            result.append(i)
```

- If the hash values match, it's a **potential match**.
- To confirm (due to possibility of hash collisions), check the actual substring: `text[i:i + m]`.

---

### 📦 **Update Hash (Sliding Window)**

```python
    if i < n - m:
        t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % prime
        if t < 0:
            t += prime
```

#### What’s happening here?

Let’s break this down:

- Remove the contribution of `text[i]` (leftmost character of the current window).
- Add `text[i + m]` (next character in text).
- The hash is updated efficiently in constant time.

The modulo `prime` ensures the hash value stays within integer bounds.

---

### ✅ **Return Results**

```python
return result
```

---

### 🧪 **Example**

```python
text = "AABAACAADAABAABA"
pattern = "AABA"
```

**Output:**

```python
Rabin-Karp: [0, 9, 12]
```

Which means `"AABA"` occurs at indices 0, 9, and 12 in the text.

---

### 📈 **Time Complexity**

- **Best/Average Case**: `O(n + m)`
  - Hash comparisons are fast, and very few actual substring comparisons.
- **Worst Case**: `O(nm)`
  - Happens when lots of hash collisions occur.

---

### 🧠 Summary

The Rabin-Karp algorithm:

- Uses hashing to **quickly eliminate non-matches**.
- Only does **character-by-character comparison** when hashes match.
- Efficient for **multiple pattern search** (with slight modifications).

---

## **Big O Analysis:**

### Time and Space Complexity Analysis

### **Rabin-Karp Algorithm: Time and Space Complexity Analysis**

#### **Time Complexity:**

1. **Preprocessing (Hash Calculation for Pattern and First Window):**
   - The loop runs **`m`** times (where `m` is the length of the pattern).
   - Each iteration involves constant-time operations (arithmetic and modulus).
   - **Time Complexity:** **`O(m)`**

2. **Main Loop (Sliding Window over Text):**
   - The loop runs **`n - m + 1`** times (where `n` is the length of the text).
   - Each iteration involves:
     - **Hash Comparison (`p == t`)** → `O(1)`
     - **Potential Full String Comparison (`text[i:i+m] == pattern`)** → `O(m)` in the worst case (when hash matches but strings differ).
     - **Rolling Hash Update** → `O(1)`
   - **Time Complexity:**
     - **Best/Average Case:** `O(n + m)` (if few spurious hash matches occur).
     - **Worst Case:** `O(nm)` (if hash matches every time but strings differ, e.g., `text = "AAAAA"`, `pattern = "AAAB"`).

3. **Overall Time Complexity:**
   - **Best/Average Case:** `O(n + m)`
   - **Worst Case:** `O(nm)`

#### **Space Complexity:**

- The algorithm uses **constant extra space**:
  - Variables (`p`, `t`, `h`, `d`, `i`, etc.) take `O(1)` space.
  - The `result` list stores indices of matches, which could be up to `O(n)` in the worst case (e.g., `text = "AAAAA"`, `pattern = "A"`).
- **Overall Space Complexity:** `O(1)` (excluding output storage) or `O(n)` (if considering worst-case output).

### **Summary:**

| Scenario          | Time Complexity | Space Complexity |
|-------------------|-----------------|------------------|
| Best/Average Case | `O(n + m)`      | `O(1)` (or `O(n)` with output) |
| Worst Case        | `O(nm)`         | `O(1)` (or `O(n)` with output) |

The **average case** is efficient (`O(n + m)`) due to the rolling hash, but the **worst case** degrades to `O(nm)` due to spurious hash matches. The space complexity is **constant** if we ignore the output storage.

Would you like further clarification on any part? 😊
