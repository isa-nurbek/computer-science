# Big Theta (Θ) Notation – Detailed Explanation

Big Theta (Θ) notation is used in asymptotic analysis to describe an algorithm’s running time in a **tight bound**—meaning it provides both an upper and lower bound for the function's growth rate.

In the analysis of algorithms, asymptotic notations are used to evaluate the performance of an algorithm by providing an exact order of growth. This article will discuss Big – Theta notations represented by a Greek letter `(Θ)`.

**Definition:** Let `g` and `f` be the function from the set of natural numbers to itself. The function `f` is said to be `Θ(g)`, if there are constants `c1`, `c2 > 0` and a natural number `n₀` such that: `c1 * g(n) ≤ f(n) ≤ c2 * g(n) for all n ≥ n0`

Mathematical Representation:

```text
Θ (g(n)) = {f(n): there exist positive constants c1, c2 and n₀ such that 0 ≤ c1 * g(n) ≤ f(n) ≤ c2 * g(n) for all n ≥ n₀}
Note: `Θ(g)` is a set
```

The above definition means, if `f(n)` is theta of `g(n)`, then the value `f(n)` is always between `c1 * g(n) and c2 * g(n)` for large values of `n (n ≥ n0)`. The definition of theta also requires that `f(n)` must be non-negative for values of `n` greater than `n₀`.

Graphical Representation:

![Big Theta (Θ)](./images_of_bt/big_theta.webp)

## **Interpretation**

- **Upper bound:** \( f(n) \) does not grow faster than \( c_2 \cdot g(n) \) after some \( n_0 \).
- **Lower bound:** \( f(n) \) does not grow slower than \( c_1 \cdot g(n) \) after some \( n_0 \).
- **Tight bound:** The function is "sandwiched" between two multiples of \( g(n) \).

### **Big Theta Example Cases**

1. **Θ(n)**: Linear time algorithms, e.g., iterating through an array.
2. **Θ(n²)**: Quadratic time algorithms, e.g., nested loops.
3. **Θ(log n)**: Logarithmic time algorithms, e.g., binary search.
4. **Θ(1)**: Constant time operations.

---

## **Python Examples of Big Theta (Θ) Complexity**

### **Example 1: Θ(n) – Linear Complexity**

A single loop iterating over `n` elements leads to a **Θ(n)** complexity.

```python
def linear_function(arr):
    for item in arr:  # Runs n times
        print(item)    

# Example usage
arr = [1, 2, 3, 4, 5]
linear_function(arr)  # Θ(n), as it runs a single loop over n elements.
```

### **Example 2: Θ(n²) – Quadratic Complexity**

A nested loop where each iteration runs another full iteration.

```python
def quadratic_function(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):  # Nested loop runs n * n times
            print(arr[i], arr[j])

# Example usage
arr = [1, 2, 3]
quadratic_function(arr)  # Θ(n²)
```

### **Example 3: Θ(log n) – Logarithmic Complexity**

Binary search runs in **Θ(log n)** time since the search space is halved at each step.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found

# Example usage
arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 5))  # Output: 2, Θ(log n)
```

### **Example 4: Θ(1) – Constant Complexity**

Accessing an array index is always **Θ(1)** because it doesn't depend on `n`.

```python
def constant_function(arr, index):
    return arr[index]  # Direct access

# Example usage
arr = [10, 20, 30, 40]
print(constant_function(arr, 2))  # Output: 30, Θ(1)
```

---

## **Key Takeaways**

- **Θ(g(n)) gives a tight bound**, meaning it provides both the upper and lower limits for an algorithm's growth rate.
- It is useful in cases where we need a **precise classification** of an algorithm’s time complexity.
- **Different algorithms** have different growth rates, but Big Theta helps **categorize them efficiently**.
- **In Python**, understanding Big Theta helps optimize code and choose the best algorithm for a given problem.
