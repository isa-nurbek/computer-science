# Implementation in Python:


def permutations(s):
    """
    Generate all possible permutations of the input string.

    Args:
        s: The input string to generate permutations for.

    Returns:
        A list containing all possible permutations of the input string.
    """

    # Base case: if the string has only one character,
    # the only permutation is the string itself
    if len(s) == 1:
        return [s]

    # This will store all permutations we generate
    result = []

    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Create a new string without the current character
        # by combining the part before and after it
        remaining = s[:i] + s[i + 1 :]

        # Recursively generate all permutations of the remaining string
        for perm in permutations(remaining):
            # Combine the current character with each permutation
            # of the remaining characters and add to result
            result.append(char + perm)

    return result


# Test Case:

print(permutations("abc"))
# Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### **Time Complexity:**

The function generates all permutations of a string `s`. The number of permutations of a string with `n` distinct characters
is `n!` (n factorial), since:
- The first character has `n` choices,
- The second has `n-1` choices, and so on.

**Recursive Breakdown:**
- At each level, the function iterates over each character (`n` iterations).
- For each character, it makes a recursive call on the remaining string of length `n-1`.
- This continues until the base case (`len(s) == 1`).

Thus, the recurrence relation is:

    T(n) = n * T(n-1) + O(n)
    
(where the O(n) term accounts for string slicing and concatenation).

Solving this recurrence:

    T(n) = n * (n-1) * (n-2) * ... * 1 = O(n!)

However, each permutation construction involves string concatenation, which takes O(n) time per permutation
(due to string immutability in Python). Thus, the total time complexity is: O(n * n!)

### **Space Complexity:**

The space complexity is determined by:
1. **Recursion Stack Depth**: The maximum depth is `n`, so this contributes O(n).
2. **Storage of Permutations**: There are `n!` permutations, each of length `n`, so storing them takes O(n * n!) space.

Thus, the total space complexity is: O(n * n!) 

### **Summary:**
- **Time Complexity**: O(n * n!)
- **Space Complexity**: O(n * n!)

### **Optimization Note:**
If we only need to **yield** permutations (instead of storing them all in memory), we could reduce the space complexity
to O(n) (due to recursion stack) using a generator-based approach. However, the given implementation stores all
permutations explicitly, leading to O(n * n!) space.

"""
