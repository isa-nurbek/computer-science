# Most Popular Pattern Searching Algorithms

## 🔍 1. **Naive Pattern Searching Algorithm**

**💡 Idea:**

Slide the pattern over the text one by one and check for a match at every position.

### 🔧 Python Code

```python
def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    positions = []
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i)
    return positions
```

### ⏱ Time Complexity

- Worst case: **`O((n - m + 1) * m)`**  
- Best case: **`O(n)`** (if first character mismatch occurs frequently)

### 📦 Space Complexity: **`O(1)`**

---

## ⚡ 2. **Knuth-Morris-Pratt (KMP) Algorithm**

**💡 Idea:**

Use a **prefix table (LPS - longest prefix suffix)** to skip characters after mismatches.

**🔧 Python Code:**

```python
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
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
    return lps

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    positions = []
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            positions.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return positions
```

**⏱ Time Complexity:**

- Preprocessing: **`O(m)`**
- Search: **`O(n)`**  
- Total: **`O(n + m)`**

### 📦 Space Complexity: **`O(m)`**

---

## 🧮 3. **Rabin-Karp Algorithm**

### 💡 Idea

Use hashing to compare pattern and text substrings efficiently.

**🔧 Python Code:**

```python
def rabin_karp(text, pattern, prime=101):
    n, m = len(text), len(pattern)
    d = 256
    h = pow(d, m-1) % prime
    p = t = 0
    results = []

    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                results.append(s)
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % prime
            if t < 0:
                t += prime
    return results
```

**⏱ Time Complexity:**

- Average: **`O(n + m)`**
- Worst case (hash collisions): **`O(nm)`**

**📦 Space Complexity: **`O(1)`****

---

## 🎯 4. **Boyer-Moore Algorithm**

**💡 Idea:**

Starts matching from the **rightmost character**. Uses **bad character rule** and optionally **good suffix rule** to skip ahead.

### 🔧 Python Code (Bad Character Heuristic Only)

```python
def bad_char_table(pattern):
    bad_char = [-1] * 256
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    return bad_char

def boyer_moore(text, pattern):
    n, m = len(text), len(pattern)
    bad_char = bad_char_table(pattern)
    s = 0
    positions = []
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            positions.append(s)
            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(text[s + j])])
    return positions
```

**⏱ Time Complexity:**

- Best case: **`O(n/m)`**
- Worst case: **`O(n * m)`** (rare)
- Average: **sub-linear** in practice

### 📦 Space Complexity: **`O(256)`** for the bad character table

---

## 📘 5. **Aho-Corasick Algorithm (for Multiple Patterns)**

1. Building the **trie**
2. Creating **failure links**
3. Performing the **search**

```python
from collections import deque, defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = []

class AhoCorasick:
    def __init__(self, patterns):
        self.root = TrieNode()
        self.build_trie(patterns)
        self.build_failure_links()

    def build_trie(self, patterns):
        for pattern in patterns:
            node = self.root
            for char in pattern:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.output.append(pattern)

    def build_failure_links(self):
        queue = deque()
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)

        while queue:
            current = queue.popleft()
            for char, child in current.children.items():
                queue.append(child)

                # Set the failure link
                f = current.fail
                while f and char not in f.children:
                    f = f.fail
                child.fail = f.children[char] if f and char in f.children else self.root

                # Merge output from failure node
                child.output += child.fail.output

    def search(self, text):
        node = self.root
        matches = []

        for i, char in enumerate(text):
            while node and char not in node.children:
                node = node.fail
            if node:
                node = node.children[char]
                for pattern in node.output:
                    matches.append((i - len(pattern) + 1, pattern))
            else:
                node = self.root

        return matches
```

## 🚀 Example Usage

```python
patterns = ["he", "she", "his", "hers"]
text = "ushers"

ac = AhoCorasick(patterns)
matches = ac.search(text)

for index, pattern in matches:
    print(f"Pattern '{pattern}' found at index {index}")
```

### ✅ Output

```plaintext
Pattern 'she' found at index 1
Pattern 'he' found at index 2
Pattern 'hers' found at index 2
```

## 📊 Time & Space Complexity

**⏱ Time Complexity:**

- **Preprocessing:** `O(∑m)` where m is the length of each pattern.
- **Search:** `O(n + z)`, where:
  - `n` = length of the text
  - `z` = number of matches

### 📦 Space Complexity

- O(total characters in all patterns + total trie nodes + failure links)

---

## Summary Table

| Algorithm         | Time Complexity               | Space Complexity   | Best For                         |
|-------------------|-------------------------------|--------------------|----------------------------------|
| Naive             | `O(n * m)`                    | `O(1)`             | Simplicity, small patterns       |
| KMP               | `O(n + m)`                    | `O(m)`             | Large patterns, efficient search |
| Rabin-Karp        | Avg `O(n + m)`, Worst `O(nm)` | `O(1)`             | Multiple pattern matching        |
| Boyer-Moore       | Sublinear avg, Worst `O(nm)`  | `O(1)–O(256)`      | Efficient for long texts         |
| Aho-Corasick      | `O(n + total matches)`        | `O(trie size)`     | Multiple pattern matching        |

---

## `PatternMatcher` unified utility class for all algorithms

Here's a unified Python module called `PatternMatcher`, which integrates the following algorithms into a single utility class:

- Naive
- KMP
- Rabin-Karp
- Boyer-Moore
- Aho-Corasick (for multiple patterns)

---

## 🔧 `PatternMatcher` Class

```python
from collections import deque

class PatternMatcher:
    def __init__(self, patterns):
        if isinstance(patterns, str):
            patterns = [patterns]
        self.patterns = patterns
        self.single_pattern = patterns[0] if len(patterns) == 1 else None
        self.ac = None
        if len(patterns) > 1:
            self.ac = self._build_aho_corasick()

    # 1. Naive Search
    def naive_search(self, text):
        results = []
        pattern = self.single_pattern
        for i in range(len(text) - len(pattern) + 1):
            if text[i:i + len(pattern)] == pattern:
                results.append(i)
        return results

    # 2. KMP Search
    def _compute_lps(self, pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    i += 1
        return lps

    def kmp_search(self, text):
        results = []
        pattern = self.single_pattern
        lps = self._compute_lps(pattern)
        i = j = 0
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            if j == len(pattern):
                results.append(i - j)
                j = lps[j - 1]
            elif i < len(text) and text[i] != pattern[j]:
                j = lps[j - 1] if j != 0 else 0
                if j == 0:
                    i += 1
        return results

    # 3. Rabin-Karp
    def rabin_karp(self, text, prime=101):
        results = []
        pattern = self.single_pattern
        n, m = len(text), len(pattern)
        d = 256
        h = pow(d, m - 1) % prime
        p = t = 0
        for i in range(m):
            p = (d * p + ord(pattern[i])) % prime
            t = (d * t + ord(text[i])) % prime
        for s in range(n - m + 1):
            if p == t and text[s:s + m] == pattern:
                results.append(s)
            if s < n - m:
                t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % prime
                if t < 0:
                    t += prime
        return results

    # 4. Boyer-Moore (Bad Character Heuristic)
    def _bad_char_table(self, pattern):
        bad_char = [-1] * 256
        for i in range(len(pattern)):
            bad_char[ord(pattern[i])] = i
        return bad_char

    def boyer_moore(self, text):
        results = []
        pattern = self.single_pattern
        n, m = len(text), len(pattern)
        bad_char = self._bad_char_table(pattern)
        s = 0
        while s <= n - m:
            j = m - 1
            while j >= 0 and pattern[j] == text[s + j]:
                j -= 1
            if j < 0:
                results.append(s)
                s += m - bad_char[ord(text[s + m])] if s + m < n else 1
            else:
                s += max(1, j - bad_char[ord(text[s + j])])
        return results

    # 5. Aho-Corasick (Multi-pattern)
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.fail = None
            self.output = []

    def _build_aho_corasick(self):
        root = self.TrieNode()
        for pattern in self.patterns:
            node = root
            for char in pattern:
                if char not in node.children:
                    node.children[char] = self.TrieNode()
                node = node.children[char]
            node.output.append(pattern)
        queue = deque()
        for child in root.children.values():
            child.fail = root
            queue.append(child)
        while queue:
            current = queue.popleft()
            for char, child in current.children.items():
                queue.append(child)
                f = current.fail
                while f and char not in f.children:
                    f = f.fail
                child.fail = f.children[char] if f and char in f.children else root
                child.output += child.fail.output
        return root

    def aho_corasick(self, text):
        if not self.ac:
            raise ValueError("Aho-Corasick requires multiple patterns.")
        results = []
        node = self.ac
        for i, char in enumerate(text):
            while node and char not in node.children:
                node = node.fail
            if node:
                node = node.children[char]
                for pattern in node.output:
                    results.append((i - len(pattern) + 1, pattern))
            else:
                node = self.ac
        return results
```

## 🧪 Example Usage

### 🔍 For Single Pattern

```python
pm = PatternMatcher("aba")
text = "abacababcaba"
print("Naive:", pm.naive_search(text))
print("KMP:", pm.kmp_search(text))
print("Rabin-Karp:", pm.rabin_karp(text))
print("Boyer-Moore:", pm.boyer_moore(text))
```

### 🔍 For Multiple Patterns

```python
pm_multi = PatternMatcher(["he", "she", "his", "hers"])
text = "ushers"
print("Aho-Corasick:", pm_multi.aho_corasick(text))
```

**Output:**

```plaintext
Naive: [0, 4, 9]
KMP: [0, 4, 9]
Rabin-Karp: [0, 4, 9]
Boyer-Moore: [0, 4, 9]
Aho-Corasick: [(1, 'she'), (2, 'he'), (2, 'hers')]
```
