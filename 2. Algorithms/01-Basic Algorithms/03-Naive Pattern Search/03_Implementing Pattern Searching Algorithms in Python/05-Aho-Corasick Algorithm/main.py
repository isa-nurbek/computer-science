# Implementation in Python:

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

"""
Pattern 'she' found at index 1
Pattern 'he' found at index 2
Pattern 'hers' found at index 2

"""

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the **time and space complexity** of the **Aho-Corasick algorithm**, which is particularly efficient for
**multi-pattern string matching**.

---

### ✅ **Let’s define some variables:**
- `n` = length of the **text**.
- `m` = total length of all **patterns** combined.
- `k` = number of **patterns**.
- `σ` = size of the **alphabet** (e.g., 26 for lowercase English letters).

---

## 🔧 Build Phase

### 1. `build_trie(patterns)`
- Every character in every pattern is inserted once into the trie.
- **Time complexity:** `O(m)` (each character in the patterns is processed once).
- **Space complexity:** `O(m)` (in worst-case, each character creates a new node).

---

### 2. `build_failure_links()`
- BFS traversal of the trie, setting fail links.
- Each node has at most `σ` children.
- For each node and each child, the failure link is found by traversing up at most `log(m)` times in practice,
but amortized constant time using efficient fail links.

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

| Phase                 | Time Complexity  | Space Complexity  |
|-----------------------|------------------|-------------------|
| `build_trie`          | O(m)             | O(m)              |
| `build_failure_links` | O(m)             | O(m)              |
| `search`              | O(n + z)         | O(z)              |
| **Total**             | **O(m + n + z)** | **O(m + z)**      |

"""
