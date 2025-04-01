# Code Explanation: Greatest Common Divisor (Euclidean Algorithm) Implementing in Python

## **Greatest Common Divisor function**

```python
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
```

This function calculates the **Greatest Common Divisor (GCD)** of two numbers using **Euclid’s Algorithm**. Let's go through the function step by step.

---

### **Understanding the Function:**

1. **Base Case:**
   - If `b == 0`, the function returns `a`. This is the stopping condition.
   - The GCD of any number and `0` is the number itself (`GCD(a, 0) = a`).

2. **Recursive Case:**
   - Otherwise, the function calls itself with new arguments: `gcd(b, a % b)`.
   - This follows the rule:  

    ```plaintext
    GCD(a, b) = GCD(b, a % b)
    ```

   - This step keeps reducing `a` and `b` until `b` becomes `0`, at which point `a` is the GCD.

---

### **Example Execution:**

Let's trace `gcd(48, 18)` step by step.

#### **Step 1:**

```python
gcd(48, 18)
```

- `b` is not `0`, so we compute:
  - `a % b = 48 % 18 = 12`
  - Call `gcd(18, 12)`

#### **Step 2:**

```python
gcd(18, 12)
```

- `b` is not `0`, so we compute:
  - `a % b = 18 % 12 = 6`
  - Call `gcd(12, 6)`

#### **Step 3:**

```python
gcd(12, 6)
```

- `b` is not `0`, so we compute:
  - `a % b = 12 % 6 = 0`
  - Call `gcd(6, 0)`

#### **Step 4:**

```python
gcd(6, 0)
```

- Now `b == 0`, so return `6`.

**Final Output:** `6`

---

### **Key Takeaways:**

- Uses **recursion** based on **Euclidean Algorithm**.
- Reduces the problem size significantly at each step.
- Stops when `b == 0`, returning the greatest common divisor.

---

## Big O Analysis

### Time and Space Complexity Analysis

### Time Complexity

The time complexity of the Euclidean algorithm is **O(log(min(a, b)))** in the worst case. Here's why:

1. The algorithm works by repeatedly taking the remainder of `a` divided by `b` (`a % b`) until `b` becomes 0. The key observation is that `a % b` is at most `a / 2` when `b` is greater than `a / 2`, and less than `a / 2` otherwise. This means the numbers reduce very quickly.
2. Specifically, in every two recursive calls, the larger number is at least halved. This logarithmic behavior leads to the time complexity being proportional to the number of digits in the smaller of the two numbers, hence **O(log(min(a, b)))**.

### Space Complexity

The space complexity is **O(log(min(a, b)))** for the recursive version due to the recursion stack. Here's why:

1. Each recursive call adds a new layer to the call stack. The depth of the recursion is the same as the number of steps required to compute the GCD, which is **O(log(min(a, b)))**.
2. If you were to implement this iteratively, the space complexity would be **O(1)** (constant space), as you wouldn't need the call stack.

### Summary

- Time Complexity: **`O(log(min(a, b)))`**
- Space Complexity (recursive): **`O(log(min(a, b)))`**
- Space Complexity (iterative): **`O(1)`** (if implemented without recursion)
