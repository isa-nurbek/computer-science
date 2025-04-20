# Code Explanation: *Aho-Corasick Algorithm*

## 1. **AhoCorasick Class**

```python
from collections import deque, defaultdict


class TrieNode:
    """
    Represents a node in the trie (prefix tree) used by the Aho-Corasick algorithm.
    Each node contains:
    - children: a dictionary mapping characters to child nodes
    - fail: a pointer to the failure node (similar to KMP's failure function)
    - output: list of patterns that end at this node
    """

    def __init__(self):
        self.children = {}
        self.fail = None  # Failure link (similar to KMP's failure function)
        self.output = []  # Patterns that end at this node


class AhoCorasick:
    """
    Aho-Corasick string matching algorithm implementation.
    This algorithm efficiently searches for multiple patterns in a text with O(n + m + z) time complexity,
    where n is text length, m is total pattern lengths, and z is number of matches.
    """

    def __init__(self, patterns):
        self.root = TrieNode()
        self.build_trie(patterns)  # First step: build the trie
        self.build_failure_links()  # Second step: add failure links

    def build_trie(self, patterns):
        """Build the initial trie structure from the patterns."""
        for pattern in patterns:
            node = self.root
            for char in pattern:
                # Traverse the trie, creating nodes as needed
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            # Mark the end node with the complete pattern
            node.output.append(pattern)

    def build_failure_links(self):
        """Build the failure links using BFS (similar to KMP failure function but for trie)."""
        queue = deque()
        # Initialize failure links for root's children to root
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)

        while queue:
            current = queue.popleft()

            for char, child in current.children.items():
                queue.append(child)

                # Find the failure node for this child
                f = current.fail
                # Traverse failure links until we find a node with matching child or reach root
                while f and char not in f.children:
                    f = f.fail

                # Set child's failure link
                child.fail = f.children[char] if f and char in f.children else self.root

                # Merge outputs from failure node (all patterns found in failure node are also found here)
                child.output += child.fail.output

    def search(self, text):
        """
        Search for all patterns in the given text.
        Returns a list of tuples (start_index, matched_pattern).
        """
        node = self.root
        matches = []

        for i, char in enumerate(text):
            # Follow failure links until we find a node with matching child or reach root
            while node and char not in node.children:
                node = node.fail

            if node:
                # Move to the matching child node
                node = node.children[char]
                # Record any patterns found at this node
                for pattern in node.output:
                    matches.append((i - len(pattern) + 1, pattern))
            else:
                # No match found, reset to root
                node = self.root

        return matches


# Example usage:

patterns = ["he", "she", "his", "hers"]
text = "ushers"

ac = AhoCorasick(patterns)
matches = ac.search(text)

for index, pattern in matches:
    print(f"Pattern '{pattern}' found at index {index}")

# Output:

Pattern 'she' found at index 1
Pattern 'he' found at index 2
Pattern 'hers' found at index 2
```

---

## 🧠 **Overview of the Problem**

The provided code implements the **Aho-Corasick algorithm**, which is a powerful pattern matching algorithm used to efficiently search for **multiple patterns** in a single pass through the text. It builds an automaton (a finite state machine with failure links) based on the patterns and then uses it to scan the text.

## ✅ Core Components and Explanation

### 📦 `TrieNode` Class

Each `TrieNode` represents a node in the trie (prefix tree).

- `children`: a dictionary mapping each character to its child node.
- `fail`: a pointer to the longest proper suffix which is also a prefix (used when the current character doesn't match).
- `output`: list of patterns that end at this node (used to collect matches).

---

### 🔧 `AhoCorasick` Class

The main class that constructs the automaton and performs the search.

### 1. `build_trie(patterns)`

Builds a **trie (prefix tree)** from the given list of patterns.

#### Example: patterns = `["he", "she", "his", "hers"]`

It will create a tree like:

```plaintext
(root)
  ├─ h ─ e*  [he]
  │   └─ r ─ s*  [hers]
  └─ s ─ h ─ e*  [she]
      └─ i ─ s*  [his]
```

> Asterisks (*) indicate terminal nodes with `output` values (i.e., patterns ending here).

---

### 2. `build_failure_links()`

Adds **failure links** to each node in the trie. These links help the automaton **fall back** to a proper node when a mismatch occurs during the search.

- Starts from the root node’s children, whose failure link is the root itself.
- For each node, it tries to find the longest possible suffix that is also a prefix.
- If it can’t find one, it defaults to the root.
- It also merges the output of the fail node, so the search can detect multiple overlapping patterns.

#### Example

If you're at `'hers'` and the next char doesn’t match, you follow the `fail` link. If that node has an output (like `he`), it’ll still be detected.

---

### 3. `search(text)`

Scans through the given text using the constructed automaton.

#### Workflow

- Start at the root.
- For each character in the text:
  - Follow the character down the trie.
  - If no edge exists, follow the failure link until you find one (or hit the root).
  - If you land on a node with an output, it means **a pattern ends here**, so store the match.
- Continues scanning the text.

#### Output

A list of `(start_index, pattern)` tuples indicating where each pattern was found in the text.

---

## 🧪 Example: Searching "ushers"

Patterns: `["he", "she", "his", "hers"]`  
Text: `"ushers"`

During the search:

| i | char | matched patterns |
|---|------|------------------|
| 0 | u    | none             |
| 1 | s    | "she"            |
| 2 | h    |                  |
| 3 | e    | "he"             |
| 4 | r    |                  |
| 5 | s    | "hers"           |

So the output is:

```plaintext
Pattern 'she' found at index 1
Pattern 'he' found at index 2
Pattern 'hers' found at index 2
```

---

## 💡 Summary

- **Trie** helps organize the patterns by common prefixes.
- **Failure links** allow the algorithm to backtrack efficiently without re-checking the input.
- **Output links** ensure we don't miss matches from fallback paths.
- Time complexity:
  - Preprocessing: O(total length of all patterns)
  - Search: O(length of text + number of matches)

---

## ASCII visualization of the Aho-Corasick trie

Here's an **ASCII visualization** of the **Aho-Corasick trie** structure for the patterns:

- `"he"`
- `"she"`
- `"his"`
- `"hers"`

---

### 📦 Trie with Output Labels (Terminal Nodes)

We'll build the trie step by step and mark:

- Terminal nodes with `[pattern]`
- Failure links (will be shown below separately)

```plaintext
(root)
  |
  |-- h
  |    |
  |    |-- e [he]
  |         |
  |         |-- r
  |              |
  |              |-- s [hers]
  |
  |-- s
       |
       |-- h
            |
            |-- e [she]
       |
       |-- i
            |
            |-- s [his]
```

---

### 🔄 Failure Links (Dashed arrows, logical view)

Failure links are set up during the `build_failure_links()` phase.

Let’s represent them like this: `node --fail--> fallback_node`

#### Key failure links (simplified)

```plaintext
h          --fail--> (root)
s          --fail--> (root)
e (under h)--fail--> e (under s->h)
r (under he)--fail--> (root)
s (under her)--fail--> s (under root->s)
h (under s) --fail--> h (under root)
e (under sh)--fail--> e (under h)
i (under s) --fail--> (root)
s (under si)--fail--> s (under h)
```

Failure links are designed to:

- Redirect search to the **next best node** when a mismatch happens.
- Carry over any matching patterns from those fallback nodes.

---

### 🧠 How it helps during search

Example: Searching "ushers"

- At `'s'` → matches `s`
- Then `'h'` → matches `sh`
- Then `'e'` → hits terminal node → matches `she`
- Then `'r'` → fallback to `'r'` under `'he'`
- Then `'s'` → hits `'hers'`

---

This ASCII view helps understand how:

- The trie stores pattern structure.
- The failure links let the search bounce efficiently between branches.

---

## **Big O Analysis:**

### Time and Space Complexity Analysis

Let's analyze the **time and space complexity** of the **Aho-Corasick algorithm**, which is particularly efficient for **multi-pattern string matching**.

### ✅ **Let’s define some variables:**

- `n` = length of the **text**.
- `m` = total length of all **patterns** combined.
- `k` = number of **patterns**.
- `σ` = size of the **alphabet** (e.g., 26 for lowercase English letters).

---

## 🔧 Build Phase

**1. `build_trie(patterns)`:**

- Every character in every pattern is inserted once into the trie.
- **Time complexity:** `O(m)` (each character in the patterns is processed once).
- **Space complexity:** `O(m)` (in worst-case, each character creates a new node).

**2. `build_failure_links()`:**

- BFS traversal of the trie, setting fail links.
- Each node has at most `σ` children.
- For each node and each child, the failure link is found by traversing up at most `log(m)` times in practice, but amortized constant time using efficient fail links.
- **Time complexity:** `O(m)` (since each node and edge is visited once).
- **Space complexity:** `O(m)` (queue size and failure links).

---

## 🔍 Search Phase: `search(text)`

- Traverse the text once, following trie edges and fail links.
- For each character in the text:
  - In the worst case, we might follow several fail links (though amortized time per character is **O(1)**).
- When we land on a node with output, we collect matches (which may be many).
- **Time complexity:** `O(n + z)`  
  - `n` for scanning the text,  
  - `z` for total number of matches found.
- **Space complexity:** `O(z)` for storing matches.

---

## ✅ Summary

| Phase                 | Time Complexity    | Space Complexity |
|-----------------------|--------------------|------------------|
| `build_trie`          | `O(m)`             | `O(m)`           |
| `build_failure_links` | `O(m)`             | `O(m)`           |
| `search`              | `O(n + z)`         | `O(z)`           |
| **Total**             | **`O(m + n + z)`** | **`O(m + z)`**   |
