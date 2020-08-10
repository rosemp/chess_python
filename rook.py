""" This docstring probably should be here.

Describe the module."""

import numpy as np
from game_state import *


def move_rook(player, piece_pos, move_to):
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

    if player == board[move_to[0]][move_to[1]][0]:
        print("Error: You can't attack your own piece")
        return False

    vertical_dist = move_to[0] - piece_pos[0]
    horizontal_dist = move_to[1] - piece_pos[1]
    vertical_move = False
    horizontal_move = False
    if vertical_dist != 0:
        vertical_move = True
    elif horizontal_dist != 0:
        horizontal_move = True
    
    # Check if rook is blocked horizontally or vertically
    # Vertical move
    # move_direct is either -1 or +1
    move_direct = np.sign(vertical_dist)
    for i in range(piece_pos[0] + move_direct, move_to[0], move_direct):
        if board[i][piece_pos[1]] != "  ":
           print("Error: Your piece is blocked!")
           return False
    # Horizontal move
    # move_direct is either -1 or +1
    move_direct = np.sign(horizontal_dist)
    for j in range(piece_pos[1] + move_direct, move_to[1], move_direct):
        if board[piece_pos[0]][j] != "  ":
           print("Error: Your piece is blocked!")
           return False
        
    # This function returns True if no errors are detected.
    return True
    


