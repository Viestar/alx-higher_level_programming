#!/usr/bin/python3
"""Solves the N-qs puzzle."""
import sys


def board_init(n):
    """Initialize chessboard"""
    chess_board = []
    [chess_board.append([]) for index in range(n)]
    [row.append(' ') for index in range(n) for row in chess_board]
    return (chess_board)


def board_copier(chess_board):
    """Returns chessboard copy."""
    if isinstance(chess_board, list):
        return list(map(board_copier, chess_board))
    return (chess_board)


def board_solution(chess_board):
    """Returns a solved chessboard."""
    chess_solutions = []
    for row in range(len(chess_board)):
        for column in range(len(chess_board)):
            if chess_board[row][column] == "Q":
                chess_solutions.append([row, column])
                break
    return (chess_solutions)


def board_play(chess_board, row, col):
    """ Game Play.
    Args:
    chess_board (list): The currentchessboard.
    row (int): The row last played.
    col (int): The column last played.
    """
    for column in range(col + 1, len(chess_board)):
        chess_board[row][column] = "Q"

    for column in range(col - 1, -1, -1):
        chess_board[row][column] = "Q"

    for row in range(row + 1, len(chess_board)):
        chess_board[row][col] = "Q"

    for row in range(row - 1, -1, -1):
        chess_board[row][col] = "Q"

    column = col + 1
    for row in range(row + 1, len(chess_board)):
        if column >= len(chess_board):
            break
        chess_board[row][column] = "Q"
        column += 1

    column = col - 1
    for row in range(row - 1, -1, -1):
        if column < 0:
            break
        chess_board[row][column]
        column -= 1

    column = col + 1
    for row in range(row - 1, -1, -1):
        if column >= len(chess_board):
            break
        chess_board[row][column] = "Q"
        column += 1

    column = col - 1
    for row in range(row + 1, len(chess_board)):
        if column < 0:
            break
        chess_board[row][column] = "Q"
        column -= 1


def board_repeat(chess_board, row, qs, board_solutions):
    """Solution
    Args:
    chess_board (list): The current working chessboard.
    row (int): The current working row.
    qs (int): The current number of placed qs.
    board_solutions (list): A list of lists of board_solutions.
    """
    if qs == len(chess_board):
        board_solutions.append(board_solution(chess_board))
        return (board_solutions)

    for column in range(len(chess_board)):
        if chess_board[row][column] == " ":
            tmp_board = board_copier(chess_board)
            tmp_board[row][column] = "Q"
            board_play(tmp_board, row, column)
            board_solutions = board_repeat(tmp_board, row + 1,
                                           qs + 1, board_solutions)

    return (board_solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess_board = board_init(int(sys.argv[1]))
    board_solutions = board_repeat(chess_board, 0, 0, [])
    for solution in board_solutions:
        print(solution)
