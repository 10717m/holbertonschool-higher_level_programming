#!/usr/bin/python3
"""
Solves the N-Queens problem:
- Places N non-attacking queens on an N×N chessboard
- Usage: ./101-nqueens.py N
"""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col] safely."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Solves the N-Queens puzzle and prints all solutions."""
    def backtrack(row):
        if row == n:
            solution = [[i, board[i]] for i in range(n)]
            print(solution)
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)

    board = [-1 for _ in range(n)]
    backtrack(0)


def main():
    """Main entry point of the script."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
