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
