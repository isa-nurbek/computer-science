# Code Explanation: Permutations of a String Implementing in Python

## **Permutations of a String function**

```python
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
```

This function generates all possible permutations of a given string using recursion.

Let's break it down step by step.

## **Understanding the Code**

### **1. Base Case (Stopping Condition)**

```python
if len(s) == 1:
    return [s]
```

- If the input string `s` has only one character, return a list containing just that character (a permutation of itself).
- This is the base case of the recursion, which prevents infinite recursive calls.

### **2. Recursive Case**

```python
result = []
for i, char in enumerate(s):
```

- `result` is an empty list that will store all permutations.
- The `for` loop iterates over the string, treating each character as the first character in a permutation.

### **3. Generating Substrings**

```python
remaining = s[:i] + s[i+1:]
```

- `remaining` is the substring that excludes the character at index `i`.
- Example:
  - If `s = "abc"` and `i = 0`, then:
    - `char = 'a'`
    - `remaining = "bc"`

### **4. Recursive Call**

```python
for perm in permutations(remaining):
```

- The function calls itself recursively on the `remaining` substring.
- This recursion continues until it reaches the base case where `len(s) == 1`.

### **5. Constructing Permutations**

```python
result.append(char + perm)
```

- Each recursive call returns a list of permutations.
- `char + perm` adds the removed character to the front of each returned permutation.

---

## **Example Execution for `"abc"`**

### **Step 1: Initial Call**

```python
permutations("abc")
```

- First loop (`i = 0`):
  - `char = 'a'`
  - `remaining = "bc"`
  - Calls `permutations("bc")`

### **Step 2: Recursive Call on `"bc"`**

```python
permutations("bc")
```

- First loop (`i = 0`):
  - `char = 'b'`
  - `remaining = "c"`
  - Calls `permutations("c")`
- Second loop (`i = 1`):
  - `char = 'c'`
  - `remaining = "b"`
  - Calls `permutations("b")`

### **Step 3: Base Case on `"c"` and `"b"`**

```python
permutations("c")  # Returns ["c"]
permutations("b")  # Returns ["b"]
```

### **Step 4: Construct `"bc"` and `"cb"`**

- The recursive call `permutations("bc")` gets the results `["c"]` and `["b"]`.
- Adding `b` and `c` back:
  - `"b" + "c" = "bc"`
  - `"c" + "b" = "cb"`
- So, `permutations("bc")` returns `["bc", "cb"]`.

### **Step 5: Construct `"abc", "acb"`**

- Back to `permutations("abc")` where `char = "a"`, and `remaining = "bc"`:
- From `permutations("bc") = ["bc", "cb"]`
  - `"a" + "bc" = "abc"`
  - `"a" + "cb" = "acb"`

### **Step 6: Repeat for Other Characters**

- The function continues for `i = 1` (`char = 'b', remaining = "ac"`) and `i = 2` (`char = 'c', remaining = "ab"`).
- Eventually, it collects all permutations:

  ```python
  ["abc", "acb", "bac", "bca", "cab", "cba"]
  ```

### **Final Output**

```python
print(permutations("abc"))
```

**Output:**

```python
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```

This is a **brute-force approach** to generating permutations, using recursion and string slicing.

---

## Big O Analysis

## Time and Space Complexity Analysis

Let's analyze the time and space complexity of the given `permutations` function.

### **Time Complexity:**

The function generates all permutations of a string `s`. The number of permutations of a string with `n` distinct characters is `n!` (n factorial), since:

- The first character has `n` choices,
- The second has `n-1` choices, and so on.

**Recursive Breakdown:**

- At each level, the function iterates over each character (`n` iterations).
- For each character, it makes a recursive call on the remaining string of length `n-1`.
- This continues until the base case (`len(s) == 1`).

Thus, the recurrence relation is:

```plaintext
T(n) = n * T(n-1) + O(n)
```

(where the `O(n)` term accounts for string slicing and concatenation).

Solving this recurrence:

```plaintext
T(n) = n * (n-1) * (n-2) * ... * 1 = O(n!)
```

However, each permutation construction involves string concatenation, which takes `O(n)` time per permutation (due to string immutability in Python).

Thus, the total time complexity is: `O(n * n!)`

### **Space Complexity:**

The space complexity is determined by:

1. **Recursion Stack Depth**: The maximum depth is `n`, so this contributes `O(n)`.
2. **Storage of Permutations**: There are `n!` permutations, each of length `n`, so storing them takes `O(n * n!)` space.

Thus, the total space complexity is: `O(n * n!)`

### **Summary:**

- **Time Complexity**: `O(n * n!)`
- **Space Complexity**: `O(n * n!)`

### **Optimization Note:**

If we only need to **yield** permutations (instead of storing them all in memory), we could reduce the space complexity to `O(n)` (due to recursion stack) using a generator-based approach. However, the given implementation stores all permutations explicitly, leading to `O(n * n!)` space.
