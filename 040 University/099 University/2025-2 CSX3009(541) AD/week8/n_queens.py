# Puran Paodensakul
# 6611140
# 541


def nqueens(n):
    results = []
    board = [["." for _ in range(n)] for _ in range(n)]

    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            results.append(["".join(r) for r in board])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return results
