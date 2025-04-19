# Code Explanation: *N-Queens Problem*

## **N-Queens Problem function**

```python
def solve_n_queens(n):
    """
    Solves the N-Queens problem, which places N queens on an NxN chessboard
    such that no two queens threaten each other.
    Returns all distinct solutions as lists of board configurations.
    """

    def backtrack(row, cols, diags, anti_diags, board, res):
        """
        Recursive backtracking helper function.

        Args:
            row:    Current row being processed
            cols:   Set of occupied columns
            diags:  Set of occupied diagonals (row - col)
            anti_diags: Set of occupied anti-diagonals (row + col)
            board: Current board state
            res:   Result list to store valid solutions
        """
        # Base case: all rows processed, add solution
        if row == n:
            res.append(["".join(row) for row in board])
            return

        # Try placing queen in each column of current row
        for col in range(n):
            # Calculate diagonal and anti-diagonal identifiers
            diag = row - col  # Diagonal (top-left to bottom-right)
            anti_diag = row + col  # Anti-diagonal (top-right to bottom-left)

            # Skip if column or diagonals are already occupied
            if col in cols or diag in diags or anti_diag in anti_diags:
                continue

            # Place the queen
            cols.add(col)
            diags.add(diag)
            anti_diags.add(anti_diag)
            board[row][col] = "Q"

            # Recurse to next row
            backtrack(row + 1, cols, diags, anti_diags, board, res)

            # Backtrack (remove queen)
            board[row][col] = "."
            cols.remove(col)
            diags.remove(diag)
            anti_diags.remove(anti_diag)

    # Initialize result list and empty board
    res = []
    board = [["." for _ in range(n)] for _ in range(n)]

    # Start backtracking from first row with empty sets
    backtrack(0, set(), set(), set(), board, res)

    return res


# Test Case:

print(solve_n_queens(4))
# Output: [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
```

This Python function `solve_n_queens(n)` is an implementation of the **N-Queens problem** using **backtracking**. The problem is to place `n` queens on an `n x n` chessboard such that no two queens attack each other.

## **Understanding the Problem**

- Queens can attack **horizontally, vertically, and diagonally**.
- The goal is to place `n` queens such that **no two queens share the same row, column, or diagonal**.

## **Step-by-Step Code Explanation**

The function **`solve_n_queens(n)`** solves the problem by using **backtracking**.

### **1. Function Definition**

```python
def solve_n_queens(n):
```

- This is the main function that initializes the chessboard and calls the `backtrack` function to find all valid solutions.

### **2. Backtracking Helper Function**

```python
def backtrack(row, cols, diags, anti_diags, board, res):
```

- This is a recursive function that **places queens row by row**.
- It uses **sets** to keep track of **attacked columns and diagonals**.

---

### **3. Base Case - Stopping Condition**

```python
if row == n:
    res.append(["".join(row) for row in board])
    return
```

- If all `n` queens have been placed (`row == n`), we **add the current board configuration** to `res`.

---

### **4. Loop through each column**

```python
for col in range(n):
```

- We try to place a queen in every column of the current row.

---

### **5. Checking if the Position is Safe**

```python
diag = row - col
anti_diag = row + col
if col in cols or diag in diags or anti_diag in anti_diags:
    continue
```

- A queen **cannot be placed** in a column if:
  - Another queen is already in that **column** (`col in cols`).
  - Another queen is already in the **main diagonal** (`diag in diags`).
  - Another queen is already in the **anti-diagonal** (`anti_diag in anti_diags`).

If the column is unsafe, we skip it (`continue`).

---

### **6. Place the Queen**

```python
cols.add(col)
diags.add(diag)
anti_diags.add(anti_diag)
board[row][col] = 'Q'
```

- If the position is **safe**, we:
  - Mark the column as occupied.
  - Mark the diagonals as occupied.
  - Place the queen (`'Q'`) on the board.

---

### **7. Recursive Call**

```python
backtrack(row + 1, cols, diags, anti_diags, board, res)
```

- Move to the **next row** and try to place the next queen.

---

### **8. Backtracking (Undo the Move)**

```python
board[row][col] = '.'
cols.remove(col)
diags.remove(diag)
anti_diags.remove(anti_diag)
```

- If the recursive call **fails**, we **undo the move** and try the next column.

---

### **9. Initialize Board and Start Backtracking**

```python
res = []
board = [['.' for _ in range(n)] for _ in range(n)]
backtrack(0, set(), set(), set(), board, res)
return res
```

- Create an **empty chessboard**.
- Start the backtracking function from `row = 0`.
- Return all valid board configurations.

---

## **Example Walkthrough**

Let's run `solve_n_queens(4)`.

```plaintext
[
  [".Q..",  //  Q in column 1
   "...Q",  //  Q in column 4
   "Q...",  //  Q in column 0
   "..Q."], //  Q in column 2

  ["..Q.",  //  Q in column 2
   "Q...",  //  Q in column 0
   "...Q",  //  Q in column 4
   ".Q.."]  //  Q in column 1
]
```

These are the **two valid solutions** for `N = 4`.

## Let's visualize the **N-Queens (N=4)** step by step

### **Step 1: Start with an empty board**

```plaintext
. . . .   (row 0)
. . . .   (row 1)
. . . .   (row 2)
. . . .   (row 3)
```

Now, we try placing the first queen in **row 0**.

---

### **Step 2: Place the first queen (Q)**

We place **Q** in **row 0, column 0**.

```plaintext
Q . . .   (row 0)
. . . .   (row 1)
. . . .   (row 2)
. . . .   (row 3)
```

- `Q` attacks the entire **column 0** and **both diagonals**.

Now, move to **row 1**.

---

### **Step 3: Place the second queen**

- We **skip column 0** (attacked).
- We place **Q** in **row 1, column 2**.

```plaintext
Q . . .   (row 0)
. . Q .   (row 1)
. . . .   (row 2)
. . . .   (row 3)
```

- `Q` attacks **column 2** and both diagonals.

Move to **row 2**.

---

### **Step 4: Place the third queen**

- We **skip columns 0 and 2** (attacked).
- We place **Q** in **row 2, column 3**.

```plaintext
Q . . .   (row 0)
. . Q .   (row 1)
. . . Q   (row 2)
. . . .   (row 3)
```

- `Q` attacks **column 3** and both diagonals.

Move to **row 3**.

---

### **Step 5: Cannot Place Fourth Queen**

- No safe columns in **row 3**.
- **Backtrack!** Remove last placed **Q**.

---

### **Step 6: Try a different position in row 2**

We try **row 2, column 1** instead.

```plaintext
Q . . .   (row 0)
. . Q .   (row 1)
. Q . .   (row 2)
. . . .   (row 3)
```

Move to **row 3**.

---

### **Step 7: Place the fourth queen**

- The only safe spot is **row 3, column 3**.

```plaintext
Q . . .   (row 0)
. . Q .   (row 1)
. Q . .   (row 2)
. . . Q   (row 3)
```

✅ **Valid solution found!**

---

### **Step 8: Backtrack to find another solution**

After backtracking, we find the second solution:

```plaintext
. Q . .   (row 0)
. . . Q   (row 1)
Q . . .   (row 2)
. . Q .   (row 3)
```

✅ **Second valid solution found!**

---

## **Final Output**

```plaintext
[
  [".Q..",  // Solution 1
   "...Q",
   "Q...",
   "..Q."],

  ["..Q.",  // Solution 2
   "Q...",
   "...Q",
   ".Q.."]
]
```

This shows **all unique ways** to place **4 queens** safely!

## **Summary**

- The algorithm **explores all possibilities** using recursion.
- It **prunes invalid paths** using sets (`cols`, `diags`, `anti_diags`).
- The **backtracking step removes** the queen when needed.
- This ensures **only valid configurations** are stored in `res`.

---

## Big O Analysis

## Time and Space Complexity Analysis

### Time Complexity

The time complexity is determined by the number of recursive calls and the work done in each call.

1. **Recursive Tree**: At each row `row`, the algorithm tries to place a queen in each of the `n` columns (unless blocked by the `cols`, `diags`, or `anti_diags` sets). In the worst case, this leads to a tree with a branching factor of `n` and a depth of `n` (since there are `n` rows).

2. **Pruning**: The backtracking prunes invalid paths early (when `col`, `diag`, or `anti_diag` is already occupied), but in the worst case, the number of recursive calls is still exponential.

3. **Worst-Case Time Complexity**: The exact number of valid N-Queens solutions is not straightforward (it grows roughly as `O(n!)` for large `n`), but the upper bound is `O(nⁿ)` because at each of the `n` rows, there are up to `n` choices (columns) to place the queen. This is a loose upper bound because pruning reduces this significantly in practice.

4. **Tighter Bound**: The actual number of solutions is much smaller than `nⁿ`. The time complexity is often approximated as `O(n!)` because the backtracking avoids placing queens in the same column or diagonal, reducing the choices as we go down the rows.

### Space Complexity

The space complexity is determined by the storage required for the recursion stack and the auxiliary data structures.

1. **Recursion Stack**: The recursion goes up to `n` levels deep (one level per row), so the stack space is `O(n)`.

2. **Auxiliary Sets**: The `cols`, `diags`, and `anti_diags` sets each can grow up to `O(n)` size (since there are `n` columns, `2n-1` diagonals, and `2n-1` anti-diagonals).

3. **Board Storage**: The `board` is `O(n²)` in size, but this is part of the output and not auxiliary space. However, during recursion, we modify the board in place, so no additional space is used per recursive call for the board.

4. **Output Storage**: The `res` list stores all valid solutions, and each solution is a board of size `O(n²)`. If there are `S` solutions, this contributes `O(S * n²)` to the space complexity. However, this is often considered separate from the auxiliary space complexity.

5. **Total Auxiliary Space Complexity**: `O(n)` (recursion stack) + `O(n)` (sets) = `O(n)`.

### Summary

- **Time Complexity**: `O(n!)` (tight bound, due to pruning) or `O(nⁿ)` (loose bound).
- **Space Complexity**: `O(n)` (auxiliary space for recursion and sets), excluding the output storage (`res`).

This is a classic backtracking problem where the time complexity is exponential but significantly better than the naive approach due to pruning. The space complexity is linear in terms of auxiliary space.
