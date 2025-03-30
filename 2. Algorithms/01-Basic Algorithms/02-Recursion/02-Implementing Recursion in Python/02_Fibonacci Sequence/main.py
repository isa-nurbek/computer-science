def fibonacci(n):
    # Base case: if n is 0 or 1, return n directly
    # This is because Fibonacci(0) = 0 and Fibonacci(1) = 1
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)
    # Recursive case: for n > 1, return the sum of the two previous Fibonacci numbers
    # This implements the mathematical definition F(n) = F(n-1) + F(n-2)


# Test Case:
print(fibonacci(6))  # Output: 8
