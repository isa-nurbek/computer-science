# Code Explanation: Subsets (Power Set) Implementing in Python

## **Subsets function**

```python
def subsets(nums):
    """
    Generates all possible subsets (the power set) of a given list of unique numbers.
    Uses a recursive approach to build subsets by including/excluding each element.

    Args:
        nums: List of unique integers

    Returns:
        List of lists containing all possible subsets
    """

    # Base case: if input list is empty, return list containing only the empty subset
    if not nums:
        return [[]]

    # Recursive case:
    # 1. Get all subsets without the first element (recursive call on nums[1:])
    without_first = subsets(nums[1:])

    # 2. Generate all subsets that include the first element:
    #    - Take each subset from the 'without_first' result
    #    - Add the first element to it
    with_first = [[nums[0]] + subset for subset in without_first]

    # Combine subsets that include first element with those that don't
    return with_first + without_first


# Test Case:

print(subsets([1, 2, 3]))
# Output: [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
```

This code generates all possible subsets of a given list of numbers using recursion. Let's break it down step by step:

## **Understanding the function:**

```python
def subsets(nums):
```

- This function takes a list of numbers `nums` as input and returns a list of all possible subsets.

---

### **Base Case (Stopping Condition):**

```python
if not nums:
    return [[]]
```

- If `nums` is empty (`nums == []`), it means we've reached the end of the recursion.
- In this case, the only subset is the empty subset `[[]]`, so we return that.

---

### **Recursive Case:**

```python
without_first = subsets(nums[1:])
```

- Here, we call `subsets` recursively on the rest of the list (`nums[1:]`), which means we are generating subsets **without including the first element**.
- This step keeps reducing the size of the list until it eventually reaches the base case.

---

```python
with_first = [[nums[0]] + subset for subset in without_first]
```

- This creates new subsets by **including the first element** (`nums[0]`) in each subset of `without_first`.
- It goes through each subset in `without_first` and adds `nums[0]` to it.

---

### **Combining Both Cases:**

```python
return with_first + without_first
```

- We return both groups of subsets:
  - `with_first`: subsets that include `nums[0]`
  - `without_first`: subsets that exclude `nums[0]`

---

## **Step-by-step Execution for [1, 2, 3]**

### **Recursive Breakdown**

1. `subsets([1, 2, 3])`
   - First element: `1`
   - Compute `subsets([2, 3])`

2. `subsets([2, 3])`
   - First element: `2`
   - Compute `subsets([3])`

3. `subsets([3])`
   - First element: `3`
   - Compute `subsets([])`

4. `subsets([])  → returns [[]]` (base case reached)

---

### **Building Subsets Bottom-Up**

- `subsets([3])`:

  ```python
  without_first = [[]]
  with_first = [[3]]
  return [[3], []]
  ```
  
- `subsets([2, 3])`:

  ```python
  without_first = [[3], []]
  with_first = [[2, 3], [2]]
  return [[2, 3], [2], [3], []]
  ```

- `subsets([1, 2, 3])`:

  ```python
  without_first = [[2, 3], [2], [3], []]
  with_first = [[1, 2, 3], [1, 2], [1, 3], [1]]
  return [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
  ```

---

## **Final Output**

```plaintext
[[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
```

This is the **power set**, which contains all possible subsets of `[1, 2, 3]`.

---

## **Key Takeaways**

1. **Recursive approach**: We break the problem into smaller subproblems.
2. **Base case**: If the list is empty, return `[[]]`.
3. **Subset formation**:
   - Find subsets **without** the first element.
   - Create new subsets **with** the first element.
4. **Combine** both cases to form the full list of subsets.

---

## Big O Analysis

## Time and Space Complexity Analysis

### **Time Complexity:**

The function is recursive and generates all subsets by including or excluding each element in the list.

1. **Recurrence Relation:**
   - For each recursive call, the problem size reduces by 1 (`nums[1:]`).
   - The work done at each step involves:
     - Creating `with_first` by prepending `nums[0]` to every subset in `without_first` (this takes `O(2ⁿ⁻¹)` time, since there are `2ⁿ⁻¹` subsets).
     - Concatenating `with_first` and `without_first` (this takes `O(2ⁿ)` time since the total number of subsets doubles at each step).

2. **Total Work:**
   - The recurrence relation is:

    ```plaintext
    T(n) = T(n-1) + O(2ⁿ)
    ```

   - Solving this recurrence (unrolling it):

    ```plaintext
    T(n) = 2ⁿ + 2ⁿ⁻¹ + 2ⁿ⁻² + ... + 2⁰ = O(2ⁿ⁺¹) = O(2ⁿ)
    ```

   - Thus, the time complexity is `O(2ⁿ)`.

### **Space Complexity:**

The space complexity is determined by the maximum memory used during execution.

1. **Recursive Call Stack:**
   - The recursion depth is `O(n)` (since we reduce the problem size by 1 at each step).

2. **Output Space:**
   - The total number of subsets is `2ⁿ`, and each subset can be up to size `n`.
   - Thus, the output space is `O(n ⋅ 2ⁿ)`.

3. **Total Space Complexity:**
   - The space is dominated by the output, so the space complexity is `O(n ⋅ 2ⁿ)`.

### **Summary:**

- **Time Complexity:** `O(2ⁿ)`
- **Space Complexity:** `O(n ⋅ 2ⁿ)` (due to the output storage)

### **Intuition:**

- The function generates all subsets by deciding for each element whether to include it or not (binary choice per element), leading to `2ⁿ` subsets.
- Each subset can be up to size `n`, so the total space required is `O(n ⋅ 2ⁿ)`.

This is optimal for generating all subsets, as the output itself is of size `O(n ⋅ 2ⁿ)`.
