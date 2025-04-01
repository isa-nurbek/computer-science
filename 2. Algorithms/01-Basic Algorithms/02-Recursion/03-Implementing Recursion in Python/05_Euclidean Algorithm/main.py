# Implementation in Python:


def gcd(a, b):
    # Base case: when b becomes 0, a contains the GCD
    # This is because GCD(a, 0) = a
    if b == 0:
        return a
    else:
        # Recursive case: apply Euclid's algorithm
        # The GCD of a and b is the same as the GCD of b and the remainder of a divided by b (a % b)
        return gcd(b, a % b)


# Test Case:
print(gcd(48, 18))  # Output: 6
