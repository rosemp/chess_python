""" This docstring probably should be here.

Describe the module."""

from game_state import *

def move_knight(player,piece_pos,move_to):
    # Check that the user enters a valid knight move
    possible_moves = []
    possible_moves.append([piece_pos[0] - 1, piece_pos[1] + 2])
    possible_moves.append([piece_pos[0] - 2, piece_pos[1] + 1])
    possible_moves.append([piece_pos[0] - 2, piece_pos[1] - 1])
    possible_moves.append([piece_pos[0] - 1, piece_pos[1] - 2])
    possible_moves.append([piece_pos[0] + 1, piece_pos[1] - 2])
    possible_moves.append([piece_pos[0] + 2, piece_pos[1] - 1])
    possible_moves.append([piece_pos[0] + 2, piece_pos[1] + 1])
    possible_moves.append([piece_pos[0] + 1, piece_pos[1] + 2])
    # This function returns True if no errors are detected.
    # Check if move_to is one of these possible moves
    return True
    









