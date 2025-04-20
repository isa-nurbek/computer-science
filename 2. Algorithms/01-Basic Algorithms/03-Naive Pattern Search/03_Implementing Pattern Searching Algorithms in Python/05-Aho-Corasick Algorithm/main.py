# Implementation in Python:

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
