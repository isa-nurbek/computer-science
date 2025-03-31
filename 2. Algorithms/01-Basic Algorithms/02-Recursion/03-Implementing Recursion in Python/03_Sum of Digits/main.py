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

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the Code**

The function `sum_digits(n)` calculates the sum of the digits of a given integer `n` recursively. 
Let's break down how it works step by step.

### **Code Breakdown**
```python
def sum_digits(n):
```
- This defines a function named `sum_digits` that takes a single argument `n`, which is expected to be an integer.

```
if n == 0:
    return 0
```
- This is the **base case** of the recursion. If `n` is `0`, we return `0` because the sum of digits in `0` is `0`.
This stops further recursive calls.

```
else:
    return (n % 10) + sum_digits(n // 10)
```
- The function recursively breaks down the number:
  - `(n % 10)` extracts the last digit of `n`. 
  - `sum_digits(n // 10)` is a recursive call that removes the last digit and continues summing the remaining digits.

---

### **Step-by-Step Execution for `sum_digits(1234)`**

Let's trace the execution:

#### **First Call:**
```
sum_digits(1234)
```
- `n % 10` → `1234 % 10 = 4` (Extracts last digit)
- `n // 10` → `1234 // 10 = 123` (Removes last digit)
- Returns: `4 + sum_digits(123)`

#### **Second Call:**
```
sum_digits(123)
```
- `n % 10` → `123 % 10 = 3`
- `n // 10` → `123 // 10 = 12`
- Returns: `3 + sum_digits(12)`

#### **Third Call:**
```
sum_digits(12)
```
- `n % 10` → `12 % 10 = 2`
- `n // 10` → `12 // 10 = 1`
- Returns: `2 + sum_digits(1)`

#### **Fourth Call:**
```
sum_digits(1)
```
- `n % 10` → `1 % 10 = 1`
- `n // 10` → `1 // 10 = 0`
- Returns: `1 + sum_digits(0)`

#### **Base Case Reached:**
```
sum_digits(0)
```
- Since `n == 0`, the function returns `0`.

---

### **Final Calculation (Returning the Values)**

Now, we sum up the returned values from each recursive call:

```
sum_digits(1)  →  1 + 0  = 1
sum_digits(12) →  2 + 1  = 3
sum_digits(123) → 3 + 3  = 6
sum_digits(1234) → 4 + 6  = 10
```

### **Final Output:**
```
print(sum_digits(1234))  # Output: 10
```

---

### **Key Takeaways**

1. **Recursive Approach**  
   - The function reduces `n` by one digit in each recursive call (`n // 10`).
   - It adds the last digit (`n % 10`) to the sum of digits of the remaining number.

2. **Base Case**  
   - Stops recursion when `n == 0`, returning `0`.

"""
