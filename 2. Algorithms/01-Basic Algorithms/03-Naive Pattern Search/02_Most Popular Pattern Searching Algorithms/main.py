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
            if text[i : i + len(pattern)] == pattern:
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
            if p == t and text[s : s + m] == pattern:
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


pm = PatternMatcher("aba")
text = "abacababcaba"
print("Naive:", pm.naive_search(text))
print("KMP:", pm.kmp_search(text))
print("Rabin-Karp:", pm.rabin_karp(text))
print("Boyer-Moore:", pm.boyer_moore(text))


pm_multi = PatternMatcher(["he", "she", "his", "hers"])
text = "ushers"
print("Aho-Corasick:", pm_multi.aho_corasick(text))
