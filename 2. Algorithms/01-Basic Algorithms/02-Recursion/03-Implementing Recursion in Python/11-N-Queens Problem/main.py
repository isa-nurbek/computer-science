# Implementation in Python:


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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

The time complexity is determined by the number of recursive calls and the work done in each call.

1. **Recursive Tree**: At each row `row`, the algorithm tries to place a queen in each of the `n` columns (unless blocked by
the `cols`, `diags`, or `anti_diags` sets). In the worst case, this leads to a tree with a branching factor of `n` and a
depth of `n` (since there are `n` rows).

2. **Pruning**: The backtracking prunes invalid paths early (when `col`, `diag`, or `anti_diag` is already occupied), but
in the worst case, the number of recursive calls is still exponential.

3. **Worst-Case Time Complexity**: The exact number of valid N-Queens solutions is not straightforward (it grows roughly as
`O(n!)` for large `n`), but the upper bound is `O(nⁿ)` because at each of the `n` rows, there are up to `n` choices (columns)
to place the queen. This is a loose upper bound because pruning reduces this significantly in practice.

4. **Tighter Bound**: The actual number of solutions is much smaller than `n^n`. The time complexity is often approximated as
O(n!) because the backtracking avoids placing queens in the same column or diagonal, reducing the choices as we go down the rows.


### Space Complexity:

The space complexity is determined by the storage required for the recursion stack and the auxiliary data structures.

1. **Recursion Stack**: The recursion goes up to `n` levels deep (one level per row), so the stack space is `O(n)`.

2. **Auxiliary Sets**: The `cols`, `diags`, and `anti_diags` sets each can grow up to `O(n)` size (since there are `n` columns,
`2n-1` diagonals, and `2n-1` anti-diagonals).

3. **Board Storage**: The `board` is `O(n²)` in size, but this is part of the output and not auxiliary space. However, during
recursion, we modify the board in place, so no additional space is used per recursive call for the board.

4. **Output Storage**: The `res` list stores all valid solutions, and each solution is a board of size `O(n^2)`. If there
are `S` solutions, this contributes `O(S * n²)` to the space complexity. However, this is often considered separate from
the auxiliary space complexity.

5. **Total Auxiliary Space Complexity**: `O(n)` (recursion stack) + `O(n)` (sets) = `O(n)`.


### Summary:
- **Time Complexity**: `O(n!)` (tight bound, due to pruning) or `O(nⁿ)` (loose bound).
- **Space Complexity**: `O(n)` (auxiliary space for recursion and sets), excluding the output storage (`res`).

This is a classic backtracking problem where the time complexity is exponential but significantly better than the naive
approach due to pruning. The space complexity is linear in terms of auxiliary space.

"""
