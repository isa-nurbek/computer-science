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
