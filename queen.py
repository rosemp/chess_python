""" This docstring probably should be here.

Describe the module."""

from game_state import *


def move_queen(player, piece_pos, move_to):
    # Check that the user enters a valid queen move
    if move_to == piece_pos:
        print("Error: Queen must move.")
        return False

    valid_move = False
    direction = 'unknown'

    # Check for right horizontal
    if piece_pos[0] == move_to[0] and piece_pos[1] < move_to[1]:
        direction = "horizontal right"
        valid_move = True

    # Check upper right diagonal
    i = piece_pos[0]
    j = piece_pos[1]
    while not valid_move:
        i -= 1
        j += 1
        if i < 0 or j > 7:
            break
        elif move_to == [i, j]:
            direction = 'upper right'
            valid_move = True

    # Check for upper vertical
    if piece_pos[1] == move_to[1] and piece_pos[0] > move_to[0]:
        direction = "upper vertical"
        valid_move = True

    # Check upper left diagonal
    i = piece_pos[0]
    j = piece_pos[1]
    while not valid_move:
        i -= 1
        j -= 1
        if i < 0 or j < 0:
            break
        elif move_to == [i, j]:
            direction = 'upper left'
            valid_move = True

    # Check for left horizontal
    if piece_pos[0] == move_to[0] and piece_pos[1] > move_to[1]:
        direction = "horizontal left"
        valid_move = True

    # Check lower left diagonal
    i = piece_pos[0]
    j = piece_pos[1]
    while not valid_move:
        i += 1
        j -= 1
        if i > 7 or j < 0:
            break
        elif move_to == [i, j]:
            direction = 'lower left'
            valid_move = True

    # Check for lower vertical
    if piece_pos[1] == move_to[1] and piece_pos[0] < move_to[0]:
        direction = "lower vertical"
        valid_move = True

    # Check lower right diagonal
    i = piece_pos[0]
    j = piece_pos[1]
    while not valid_move:
        i += 1
        j += 1
        if i > 7 or j > 7:
            break
        elif move_to == [i, j]:
            direction = 'lower right'
            valid_move = True

    if not valid_move:
        print("Error: Queen must move diagonally")
        return False

    if player == board[move_to[0]][move_to[1]][0]:
        print("Error: You can't attack your own piece")
        return False

    # loop over all squares between piece_pos and move_to
    # increment row and column index based on 'direction' variable

    # Check whether queen is blocked by another piece
    i = piece_pos[0]
    j = piece_pos[1]
    split_dir = direction.split()
    vert_dir = split_dir[0]
    horiz_dir = split_dir[1]
    while True:
        # Increment square which program is checking
        if vert_dir == 'upper':
            i -= 1
        elif vert_dir == 'lower':
            i += 1

        if horiz_dir == 'right':
            j += 1
        elif horiz_dir == 'left':
            j -= 1

        # Terminate loop if at move_to
        if move_to == [i, j]:
            break

        # Check square if between piece_pos and move_to
        if board[i][j] != "  ":
            print("Error: Your queen is blocked!")
            return False
    # This function returns True if no errors are detected.
    return True
