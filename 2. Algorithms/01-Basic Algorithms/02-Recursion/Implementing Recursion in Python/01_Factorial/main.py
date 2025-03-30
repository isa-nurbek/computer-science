# Implementation in Python:


def factorial(n):
    # Base case:
    # If n is 0, return 1 because 0! is defined as 1
    # This also serves as the stopping condition for the recursion
    if n == 0:
        return 1
    else:
        # Recursive case:
        # For n > 0, return n multiplied by factorial of (n-1)
        # This recursively breaks down the problem into smaller subproblems
        # until it reaches the base case
        return n * factorial(n - 1)


# Test Case:
print(factorial(5))  # Output: 120

# =========================================================================================================================== #
