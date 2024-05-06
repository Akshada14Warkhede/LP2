class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
                    self.board[i] - i == col - row or \
                    self.board[i] + i == col + row:
                return False
        return True

    def solve(self, row=0):
        if row == self.n:
            return True

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                if self.solve(row + 1):
                    return True
                self.board[row] = -1

        return False

    def print_solution(self):
        for row in range(self.n):
            line = ["Q" if self.board[row] == col else "." for col in range(self.n)]
            print(" ".join(line))


# Example usage:
n_queens = NQueens(8)  # Change the number to solve for different board sizes
if n_queens.solve():
    n_queens.print_solution()
else:
    print("No solution exists.")
