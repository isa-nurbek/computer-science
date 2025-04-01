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
