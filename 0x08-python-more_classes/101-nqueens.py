#!/usr/bin/python3
"""The N queens puzzle
Class to solve the N puzzle challenge

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
"""
import sys


def init_board(n):
    """Initialize chessboard with empty spaces."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def sol_board(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution

def is_safe(board, row, col):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    # If all queens are placed then return true
    if col >= len(board):
        return True

    # Place this queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, then remove queen from board[i][col]
            board[i][col] = 0

    return False


if __name__ == "__main__":
    """
    Check if the correct number of arguments is provided
    """
    N = 4
    board = [[0]*N for _ in range(N)]
    if not solve_n_queens(board, 0):
        print("Solution does not exist")
    else:
        for row in board:
	print(row)

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = r_sol(board, 0, 0, [])
    for sol in solutions:
        print(sol)
