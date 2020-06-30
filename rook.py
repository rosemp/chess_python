""" This docstring probably should be here.

Describe the module."""

from game_state import *

def move_rook(player,piece_pos,move_to):
    """ This docstring probably should be here.

    Describe the function."""
    # Check that the user enters a valid rook move
    # Makes sure rook stays in the same row or the same column
    if piece_pos[0] != move_to[0] and piece_pos[1] != move_to[1]:
        print("Error: Rook must move vertically or horizontally from its position.")
        return False
    elif move_to == piece_pos:
        print("Error: Rook must move.")
        return False

    if board[move_to[0]][move_to[1]][0] == player:
        print("Error: You can't attack your own piece")
        return False

    vertical_move = move_to[0] - piece_pos[0]
    horizontal_move = move_to[1] - piece_pos[1]
    # Bookmark: Check if rook is blocked horizontally or vertically
    # This function returns True if no errors are detected.
    return True
    


