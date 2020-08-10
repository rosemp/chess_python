""" This docstring probably should be here.

Describe the module."""

from game_state import *


def move_bishop(player, piece_pos, move_to):
    # Check that the user enters a valid bishop move
    if move_to == piece_pos:
        print("Error: Bishop must move.")
        return False

    move_in_diagonal = False
    direction = 'Unknown'

    # First, check upper right diagonal
    i = piece_pos[0]
    j = piece_pos[1]
    while not move_in_diagonal:
        i -= 1
        j += 1
        if i < 0 or j > 7:
            break
        elif move_to == [i, j]:
            direction = 'upper right'
            move_in_diagonal = True

    # Second, check upper left diagonal
    i = piece_pos[0]
    j = piece_pos[1]
    while not move_in_diagonal:
        i -= 1
        j -= 1
        if i < 0 or j < 0:
            break
        elif move_to == [i, j]:
            direction = 'upper left'
            move_in_diagonal = True

    # Third, check lower left diagonal
    i = piece_pos[0]
    j = piece_pos[1]
    while not move_in_diagonal:
        i += 1
        j -= 1
        if i > 7 or j < 0:
            break
        elif move_to == [i, j]:
            direction = 'lower left'
            move_in_diagonal = True

    # Fourth, check lower right diagonal
    i = piece_pos[0]
    j = piece_pos[1]
    while not move_in_diagonal:
        i += 1
        j += 1
        if i > 7 or j > 7:
            break
        elif move_to == [i, j]:
            direction = 'lower right'
            move_in_diagonal = True

    if not move_in_diagonal:
        print("Error: Bishop must move diagonally")
        return False

    if player == board[move_to[0]][move_to[1]][0]:
        print("Error: You can't attack your own piece")
        return False


# loop over all squares between piece_pos and move_to
# increment row and column index based on 'direction' variable

    # Check whether bishop is blocked by another piece
    i = piece_pos[0]
    j = piece_pos[1]
    split_dir = direction.split()
    vert_dir = split_dir[0]
    horiz_dir = split_dir[1]
    while True:
        # Increment square which program is checking
        if vert_dir == 'upper':
            i -= 1
        else:
            i += 1
            
        if horiz_dir == 'right':
            j += 1
        else:
            j -= 1
            
        # Terminate loop if at move_to
        if move_to == [i, j]:
            break
        
        # Check square if between piece_pos and move_to
        if board[i][j] != "  ":
            print("Error: your bishop is blocked!")
            return False

    # This function returns True if no errors are detected.
    return True
    


