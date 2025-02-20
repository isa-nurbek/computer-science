# Asymptotic Notation: Conceptual

Asymptotic notation is a mathematical framework used to describe the efficiency of an algorithm in terms of time complexity and space complexity as the input size `n` grows. It provides a way to compare algorithms based on their performance without worrying about machine-specific details, such as processor speed or compiler optimizations.

## **Why Asymptotic Notation?**

1. **Focus on Growth Rate** – Instead of considering absolute execution time, we analyze how the runtime scales with increasing input size.
2. **Machine Independence** – It ignores constant factors and lower-order terms that do not significantly impact performance at large `n`.
3. **Comparative Analysis** – Helps determine which algorithm performs better for large inputs.

Cheetahs. Ferraris. Life. All are fast, but how do you know which one is the fastest? You can measure a cheetah’s and a Ferrari’s speed with a speedometer. You can measure life with years and months.

But what about computer programs? In fact, you can time a computer program, but different computers run at different speeds. For example, a program that takes 12 nanoseconds on one computer could take 45 milliseconds on another. Therefore, we need a more general way to gauge a program’s runtime. We do this with **Asymptotic Notation**.

Instead of timing a program, through asymptotic notation, we can calculate a program’s runtime by looking at how many instructions the computer has to perform based on the size of the program’s input: `n`.

For instance, a program that has input of size `n` may tell the computer to run `5n² + 3n + 2` instructions. (We will get into how we get this kind of expression in future exercises.) Nevertheless, this is still a fairly messy and large expression. For asymptotic notation, we drop all of our constants (the numbers) because as `n` becomes extremely large, the constants will make minute differences. After changing our constants, we have `n² + n`. If we take each of these terms in the expression and graph them, we see that the `n²` term grows faster than the `n` term.
![Common Runtimes](./image_of_an/runtimes%20compare.webp)

For example, when `n` is 1000:

- the `n²` term is 1,000,000
- the `n` term is 1,000
  
As you can see, the `n²` term is much more significant than the `n` term. When `n` is larger than 1000, the difference becomes even more significant. Because the difference is so enormous, we don’t even need to consider the `n` term when calculating the runtime. Thus, for this program, we would describe the runtime in terms of `n²`. There are three different ways we could describe the runtime of this program: Big Theta or `Θ(n²)`, Big O or `O(n²)`, Big Omega or `Ω(n²)`. The difference between the three and when to use which one will be detailed in the next exercises.

You may see the term **execution count** used in evaluating algorithms. Execution count is more precise than Big O notation. The following method, `addUpTo()`, depending on how we count the number of operations, can be as low as `2n` or as high as `5n + 2`.

```java
public class Main() { 
  void int addUpTo(int n) {
    int total = 0;
    for (int i = 1; i <= n; i++) {
      total += i;
    }
  return total;
  } 
}
```

Determining execution count can increase in difficulty as our algorithms become even more sophisticated!

But regardless of the execution count, the number of operations grows roughly proportionally with `n`. If `n` doubles, the number of operations will also roughly double.

Big O Notation is a way to formalize fuzzy counting. It allows us to talk formally about how the runtime of an algorithm grows as the inputs grow. As we will see, Big O doesn’t focus on the details, only the trends.

---

## **Types of Asymptotic Notation**

Asymptotic notations describe the upper, lower, and tight bounds of an algorithm’s time complexity.

### **1. Big-O Notation (O) – Upper Bound**

Big-O notation gives an upper bound on the growth rate of an algorithm. It describes the worst-case scenario, meaning it tells us the maximum time an algorithm could take.

#### **Mathematical Definition**

A function `f(n)` is said to be **O(g(n))** if there exist positive constants `c` and `n₀` such that:

```math
f(n) ≤ c ⋅ g(n),  ∀n ≥ n₀
```

### **What It Means**

- Big-O notation provides an **upper bound** on how fast an algorithm grows.
- It tells us that for sufficiently large values of `n`, the function `f(n)` will never grow faster than some constant multiple of `g(n)`.
- The constants `c` and `n₀` help define where the bound starts applying.

### **Breaking It Down**

- `f(n)`: The actual time complexity function of the algorithm.
- `g(n)`: A simpler function that acts as an upper bound.
- `c`: A constant multiplier that ensures `f(n)` is always below `c * g(n)`.
- `n₀`: The threshold beyond which this bound holds.

### **Example**

Suppose we have an algorithm with:

```text
f(n) = 3n² + 5n + 7
```

We claim that:

```text
f(n) = O(n²)
```

To prove this, we choose `c = 4` and `n₀ = 10`. For all `n ≥ 10`, we get:

```text
3n² + 5n + 7 ≤ 4n²
```

Thus, we say `f(n) = O(n²)`, meaning the algorithm **at most** grows like `n²`.

---

### **2. Omega Notation (Ω) – Lower Bound**

Omega notation provides a lower bound on the running time of an algorithm. It describes the best-case scenario, meaning it tells us the minimum time an algorithm will take.

#### **Mathematical Definition**

A function `f(n)` is said to be **Ω(g(n))** if there exist positive constants `c` and `n₀` such that:

```math
f(n) ≥ c ⋅ g(n),  ∀n ≥ n₀
```

### **What It Means**

- Omega notation provides a **lower bound** on the algorithm's growth.
- It tells us that for sufficiently large `n`, the function `f(n)` will **at least** grow as fast as `g(n)`.
- This helps determine the **best-case** performance of an algorithm.

### **Breaking It Down**

- `f(n)`: The actual complexity function.
- `g(n)`: A simpler function that acts as a lower bound.
- `c`: A constant that ensures `f(n)` is always at least `c * g(n)`.
- `n₀`: The threshold beyond which this bound holds.

### **Example**

For the same function:

```text
f(n) = 3n² + 5n + 7
```

We claim:

```text
f(n) = Ω(n²)
```

By picking `c = 2` and `n₀ = 10`, we see that for all `n ≥ 10`:

```text
3n² + 5n + 7 ≥ 2n²
```

Thus, `f(n) = Ω(n²)`, meaning the algorithm **at least** grows like `n²`.

---

### **3. Theta Notation (Θ) – Tight Bound**

Theta notation describes the exact bound of an algorithm, meaning it provides both an upper and a lower bound. It shows the precise order of growth.

#### **Mathematical Definition**

A function `f(n)` is said to be **Θ(g(n))** if there exist positive constants `c₁`, `c₂`, and `n₀` such that:

```math
c₁ ⋅ g(n) ≤ f(n) ≤ c₂ ⋅ g(n),  ∀n ≥ n₀
```

### **What It Means**

- Theta notation provides a **tight bound**, meaning the algorithm **exactly** follows the growth rate of `g(n)`.
- This notation is used when both the upper and lower bounds are the same.

### **Breaking It Down**

- `c₁` and `c₂`: Two constants that sandwich `f(n)`.
- `f(n)`: The actual complexity function.
- `g(n)`: The function that defines the growth rate.
- `n₀`: The threshold beyond which this bound holds.

### **Example**

For the same function:

```text
f(n) = 3n² + 5n + 7
```

Since it is both `O(n²)` and `Ω(n²)`, it follows that:

```text
f(n) = Ω(n²)
```

For `c₁ = 2` and `c₂ = 4`, we get:

```math
2n² ≤ 3n² + 5n + 7 ≤ 4n²,  ∀n ≥ 10
```

Thus, `f(n) = Θ(n²)`, meaning the algorithm **grows exactly** like `n²`.

---

## **Summary**

| Notation | Formula | Meaning |
|----------|---------|---------|
| **Big-O** (`O(g(n))`) | `f(n) ≤ c * g(n)` | **Upper bound (worst case)** |
| **Omega** (`Ω(g(n))`) | `f(n) ≥ c * g(n)` | **Lower bound (best case)** |
| **Theta** (`Θ(g(n))`) | `c₁ * g(n) ≤ f(n) ≤ c₂ * g(n)` | **Exact bound (tight case)** |

---

## **How Asymptotic Notation Works**

To analyze an algorithm, follow these steps:

1. **Identify the Most Significant Term**  
   - Ignore constants and lower-order terms.
   - Example: `4n³ + 3n² + 2n + 1` simplifies to `O(n³)`.

2. **Classify the Complexity Using Notations**  
   - Worst-case: `O(n³)`
   - Best-case: `Ω(n³)`
   - Tight bound: `Θ(n³)`

3. **Compare Algorithms Using Growth Rate**  
   - `O(1)`         (constant) → Best  
   - `O(log n)`     (logarithmic)  
   - `O(n)`         (linear)  
   - `O(n log n)`   (Log-linear)
   - `O(n²)`        (quadratic)  
   - `O(n³)`        (cubic)  
   - `O(2ⁿ)`        (exponential) → Worst  

---

## **Common Time Complexities and Examples**

| Complexity | Name | Example Algorithm |
|------------|---------|--------------------|
| `O(1)` | Constant | Accessing an array index |
| `O(log n)` | Logarithmic | Binary search |
| `O(n)` | Linear | Linear search |
| `O(n log n)` | Log-linear | Merge sort, Quick sort (average case) |
| `O(n²)` | Quadratic | Bubble sort, Selection sort |
| `O(n³)` | Cubic | Matrix multiplication |
| `O(2ⁿ)` | Exponential | Recursive Fibonacci |
| `O(n!)` | Factorial | Traveling Salesman Problem |

---

## **Real-World Example**

Consider **binary search**:

- It repeatedly divides the problem size by 2.
- At each step, it eliminates half the remaining elements.
- The recurrence relation is: `T(n) = T(n/2) + O(1)`.
- This simplifies to **O(log n)** complexity.

Whereas **linear search**:

- Scans each element one by one.
- Worst case: searches through all `n` elements.
- Thus, its time complexity is **O(n)**.

Since **O(log n) < O(n)**, binary search is faster than linear search for large `n`.

---

## **Key Takeaways**

✅ **Big-O** provides an upper bound (worst-case scenario).  
✅ **Omega (Ω)** provides a lower bound (best-case scenario).  
✅ **Theta (Θ)** provides a tight bound (exact growth rate).  
✅ **Higher-order terms dominate complexity** (e.g., `O(n²)` dominates `O(n)`).  
✅ **Ignoring constants simplifies analysis**.
