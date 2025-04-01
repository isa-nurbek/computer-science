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
