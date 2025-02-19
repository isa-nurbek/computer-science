# Asymptotic Notation: Conceptual

Asymptotic notation is a mathematical framework used to describe the efficiency of an algorithm in terms of time complexity and space complexity as the input size `( n )` grows. It provides a way to compare algorithms based on their performance without worrying about machine-specific details, such as processor speed or compiler optimizations.

## **Why Asymptotic Notation?**

1. **Focus on Growth Rate** – Instead of considering absolute execution time, we analyze how the runtime scales with increasing input size.
2. **Machine Independence** – It ignores constant factors and lower-order terms that do not significantly impact performance at large `n`.
3. **Comparative Analysis** – Helps determine which algorithm performs better for large inputs.

Cheetahs. Ferrari's. Life. All are fast, but how do you know which one is the fastest? You can measure a cheetah’s and a Ferrari’s speed with a speedometer. You can measure life with years and months.

But what about computer programs? In fact, you can time a computer program, but different computers run at different speeds. For example, a program that takes 12 nanoseconds on one computer could take 45 milliseconds on another. Therefore, we need a more general way to gauge a program’s runtime. We do this with **Asymptotic Notation**.

Instead of timing a program, through asymptotic notation, we can calculate a program’s runtime by looking at how many instructions the computer has to perform based on the size of the program’s input: `N`.

For instance, a program that has input of size `N` may tell the computer to run `5N2 + 3N + 2` instructions. (We will get into how we get this kind of expression in future exercises.) Nevertheless, this is still a fairly messy and large expression. For asymptotic notation, we drop all of our constants (the numbers) because as `N` becomes extremely large, the constants will make minute differences. After changing our constants, we have `N2 + N`. If we take each of these terms in the expression and graph them, we see that the `N2` term grows faster than the `N` term.

![Common Runtimes](../01_What%20is%20Asymptotic%20Notation/image_of_an/runtimes%20compare.webp)

For example, when `N` is 1000:

- the `N2` term is 1,000,000
- the `N` term is 1,000
  
As you can see, the `N2` term is much more significant than the `N` term. When `N` is larger than 1000, the difference becomes even more significant. Because the difference is so enormous, we don’t even need to consider the `N` term when calculating the runtime. Thus, for this program, we would describe the runtime in terms of `N2`. There are three different ways we could describe the runtime of this program: Big Theta or `Θ(N2)`, Big O or `O(N2)`, Big Omega or `Ω(N2)`. The difference between the three and when to use which one will be detailed in the next exercises.

You may see the term **execution count** used in evaluating algorithms. Execution count is more precise than Big O notation. The following method, `addUpTo()`, depending on how we count the number of operations, can be as low as `2N` or as high as `5N + 2`.

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
f(n) ≤ c * g(n)  for all n ≥ n₀
```

#### **Example**

If an algorithm takes `3n² + 5n + 7` operations, we approximate its time complexity as:

```math
O(n²)
```

**Why?** Because as `n` grows large, the `n²` term dominates, and constants are ignored.

---

### **2. Omega Notation (Ω) – Lower Bound**

Omega notation provides a lower bound on the running time of an algorithm. It describes the best-case scenario, meaning it tells us the minimum time an algorithm will take.

#### **Mathematical Definition**

A function `f(n)` is said to be **Ω(g(n))** if there exist positive constants `c` and `n₀` such that:

```math
f(n) ≥ c * g(n)  for all n ≥ n₀
```

#### **Example**

For the function `f(n) = 3n² + 5n + 7`, we can say:

```math
`Ω(n²)`
```

because, in the best case, it still behaves at least as `n²` for large `n`.

---

### **3. Theta Notation (Θ) – Tight Bound**

Theta notation describes the exact bound of an algorithm, meaning it provides both an upper and a lower bound. It shows the precise order of growth.

#### **Mathematical Definition**

A function `f(n)` is said to be **Θ(g(n))** if there exist positive constants `c₁`, `c₂`, and `n₀` such that:

```math
c₁ * g(n) ≤ f(n) ≤ c₂ * g(n)  for all n ≥ n₀`
```

#### **Example**

For the function `f(n) = 3n² + 5n + 7`, since its growth rate is bounded both from above and below by `n²`, we write:

```math
Θ(n²)
```

Thus, `f(n)` is neither faster nor slower than `n²` in terms of growth rate.

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
