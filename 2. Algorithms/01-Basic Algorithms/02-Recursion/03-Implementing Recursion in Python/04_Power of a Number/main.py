# Implementation in Python:


def power(base, exp):
    # Base case: any number raised to power 0 is 1
    if exp == 0:
        return 1
    # Recursive case: multiply base by power(base, exp-1)
    # This effectively breaks down the problem into smaller subproblems
    else:
        return base * power(base, exp - 1)


# Test Case:
print(power(2, 3))  # Output: 8

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:
- The function makes one recursive call each time until `exp` reaches 0.
- The number of recursive calls is equal to the value of `exp`.
- Each recursive call performs a constant amount of work (multiplication and subtraction).
- Thus, the time complexity is **O(exp)** (linear in the value of `exp`).

### Space Complexity:
- Each recursive call adds a new stack frame to the call stack.
- The maximum depth of the call stack is equal to the value of `exp`.
- Thus, the space complexity is **O(exp)** (linear in the value of `exp`).

### Summary:
- **Time Complexity:** O(exp)
- **Space Complexity:** O(exp)

### Note:
This is a straightforward recursive implementation. There are more efficient ways to compute powers (e.g., using exponentiation 
by squaring, which reduces the time complexity to O(log exp)), but this implementation serves as a simple example of recursion.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the Code**

The function `power(base, exp)` calculates the exponentiation of `base` raised to `exp` using **recursion**.
Here's a step-by-step breakdown:

#### **1. Base Case**
```
if exp == 0:
    return 1
```
- When `exp` is **0**, the function returns `1` because any number raised to the power of `0` is **1**.
- This serves as the base case, preventing infinite recursion.

#### **2. Recursive Case**
```
else:
    return base * power(base, exp - 1)
```
- The function recursively calls itself, reducing `exp` by `1` in each call.
- This continues until `exp` reaches `0`, at which point the recursion stops.

---

### **Step-by-Step Execution for `power(2, 3)`**

#### **First Call: `power(2, 3)`**
- `exp` is not `0`, so it returns:

```
2 * power(2, 2)
```

#### **Second Call: `power(2, 2)`**
- `exp` is not `0`, so it returns:

```
2 * power(2, 1)
```

#### **Third Call: `power(2, 1)`**
- `exp` is not `0`, so it returns:

```
2 * power(2, 0)
```

#### **Fourth Call: `power(2, 0)` (Base Case)**
- Since `exp == 0`, it returns **1**.

---

### **Now, Let's Resolve the Recursion**

Each function call now returns its result to the previous call:

1. `power(2, 0) → 1`
2. `power(2, 1) → 2 × 1 = 2`
3. `power(2, 2) → 2 × 2 = 4`
4. `power(2, 3) → 2 × 4 = 8`

Thus, `power(2, 3) → 8`, which is the expected output.

"""
