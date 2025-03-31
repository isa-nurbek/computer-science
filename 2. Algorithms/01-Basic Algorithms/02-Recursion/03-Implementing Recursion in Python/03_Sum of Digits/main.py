# Implementation in Python:


def sum_digits(n):
    # Base case: if n is 0, return 0 (no digits left to sum)
    if n == 0:
        return 0
    else:
        # Recursive case:
        # 1. Get the last digit (n % 10)
        # 2. Add it to the sum of the remaining digits (sum_digits(n // 10))
        # n // 10 effectively removes the last digit from the number
        return (n % 10) + sum_digits(n // 10)


print(sum_digits(1234))  # Output: 10

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

The time complexity is determined by the number of recursive calls the function makes. 

1. In each recursive call, the function processes one digit of `n` (by taking `n % 10`) and then reduces `n` by removing
the last digit (using `n // 10`).
2. The recursion continues until `n` becomes `0`, at which point the function stops.
3. The number of digits in `n` is given by `d = floor(log10(n)) + 1` (for `n > 0`).
For example:
   - If `n = 123`, the number of digits is `3`.
   - If `n = 10`, the number of digits is `2`.
4. Thus, the function makes `d` recursive calls, where `d` is the number of digits in `n`.

The time complexity is therefore **O(d)**, where `d` is the number of digits in `n`. Since `d = floor(log10(n)) + 1`,
the time complexity can also be expressed as **O(log n)** (logarithmic in `n`).

---

### Space Complexity:

The space complexity is determined by the maximum depth of the recursion stack.

1. Each recursive call adds a new frame to the call stack.
2. The maximum depth of the recursion is equal to the number of digits in `n`, which is `d = floor(log10(n)) + 1`.
3. Thus, the space complexity is also **O(d)** or **O(log n)** (logarithmic in `n`).

---

### Summary:

- Time Complexity: **O(log n)** (or more precisely, O(d), where d is the number of digits in `n`).
- Space Complexity: **O(log n)** (due to the recursion stack, where the depth is the number of digits in `n`).

"""
