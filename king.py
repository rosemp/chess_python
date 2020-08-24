"""This module does all the checks for the king.
   The king is pretty simple, as the only things
   we need to check for is making sure that the
   king actually moves, that it only is able to
   move one space in every direction, and also
   to make sure it doesn't attack it's own piece."""


from game_state import *
from check_mod import *


def move_king(player, piece_pos, move_to):
    # Check that the user enters a valid king move

    # This variables store the vertical and horizontal move so the code can simpler
    vertical_move = move_to[0] - piece_pos[0]
    horizontal_move = move_to[1] - piece_pos[1]
    if piece_pos == move_to:
        print("\nError: King must move")
        return False

    # Make sure the king doesn't attack it's own piece. The king can't be blocked
    if player == board[move_to[0]][move_to[1]][0]:
        print("\nError: You can't attack your own piece")
        return False

    # Make sure the king is only able to move by one space in each direction
    if vertical_move < -1 or vertical_move > 1:
        print("\nError: King can only move one space vertically")
        return False

    elif horizontal_move < -1 or horizontal_move > 1:
        print("\nError: King can only move one space horizontally")
        return False

    # This function returns True if no errors are detected.
    return True
