""" This docstring probably should be here.

Describe the module."""

from game_state import *

def move_bishop(player,piece_pos,move_to):
    # Check that the user enters a valid bishop move
    if move_to == piece_pos:
        print("Error: Bishop must move.")
        return False

    move_in_diagonal = False
    direction = 'Unknown'
    i = piece_pos[0]
    j = piece_pos[1]

    # First, check upper right diagonal
    while not move_in_diagonal:
        i -= 1
        j += 1
        if i < 0 or j > 7:
            break
        elif move_to == [i,j]:
            direction == 'Upper right'
            move_in_diagonal = True

    # Second, check upper left diagonal
    while not move_in_diagonal:
        i -= 1
        j -= 1
        if i < 0 or j < 0:
            break
        elif move_to == [i, j]:
            direction == 'Upper left'
            move_in_diagonal = True

    # Third, check lower left diagonal
    while not move_in_diagonal:
        i += 1
        j -= 1
        if i > 7 or j < 0:
            break
        elif move_to == [i, j]:
            direction == 'Lower left'
            move_in_diagonal = True

    # Fourth, check lower right diagonal
    while not move_in_diagonal:
        i += 1
        j += 1
        if i > 7 or j > 7:
            break
        elif move_to == [i, j]:
            direction == 'Lower right'
            move_in_diagonal = True

    if not move_in_diagonal:
        print("Error: Bishop must move diagonally")
        return False

    if player == board[move_to[0]][move_to[1]][0]:
        print("Error: You can't attack your own piece")
        return False

# loop over all squares between piece_pos and move_to
# increment row and column index based on 'direction' variable
# also add code to check if bishop is blocked
    # This function returns True if no errors are detected.
    return True
    


