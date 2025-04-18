# 🔍 Naive Pattern Search: Conceptual Overview

The **Naive Pattern Search** algorithm is a simple string-searching technique used to find occurrences of a *pattern* within a *text*. It’s called *naive* because it doesn’t use any advanced preprocessing or optimization—it just checks every possible position in the text.

---

## 🎯 What Is It?

Have you ever scanned a dictionary page or a website, checking word after word until you found the one you were looking for? That’s a **naive form of pattern searching**!

This approach is straightforward: slide the pattern across the text one character at a time, checking for a match at each position.

---

## 🧱 Components

To perform pattern searching, you need:

- A **text** to scan (e.g., a sentence or paragraph)
- A **pattern** to search for (e.g., a word or substring)

We treat the text as a long string and slide the shorter pattern along it, one character at a time. At each position, we check if the pattern matches the corresponding substring of the text.

---

## 🔁 How It Works

Let:

- `n` = length of the text  
- `m` = length of the pattern

### 🧠 Algorithm Steps

1. Start from the beginning of the text.
2. For each index `i` from `0` to `n - m`:
   - Compare the substring `text[i...i+m-1]` with the pattern.
   - If they match, record the index.
3. Repeat until the end of the text is reached.

---

## 💡 Example

**Text**: `"ABABDABACDABABCABAB"`  
**Pattern**: `"ABAB"`

We slide the pattern over the text one character at a time:

```plaintext
ABABDABACDABABCABAB
↑↑↑↑
ABAB   ✅ Match at index 0

        ↑↑↑↑
        ABAB ❌ Not a match

                  ↑↑↑↑
                  ABAB ✅ Match at index 15
```

---

## ⏱️ Time Complexity

| Case        | Time Complexity             | Description                                 |
|-------------|-----------------------------|---------------------------------------------|
| Best Case   | O(n)                        | When mismatches occur early                 |
| Worst Case  | O((n - m + 1) × m) ≈ O(nm)  | For repetitive text and pattern combinations|

In the worst case, each character in the text can trigger a full pattern comparison, leading to slower performance.

---

## ✅ Pros

- Very simple and intuitive
- Easy to implement
- No preprocessing required

## ❌ Cons

- Not efficient for large texts or long patterns
- Poor performance with repetitive inputs
- Doesn’t scale well

---

## 🧪 Sample Python Code

```python
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    result = []

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            result.append(i)
    
    return result

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABAB"
print(naive_search(text, pattern))  # Output: [0, 15]
```

---

## 📌 Summary

The **Naive Pattern Search** algorithm is great for learning how pattern matching works, but not suitable for high-performance applications. More advanced algorithms like **Knuth–Morris–Pratt (KMP)** or **Boyer-Moore** offer better time complexity and efficiency for real-world tasks.
