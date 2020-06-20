""" This docstring probably should be here.

Describe the module."""

from game_state import *

def move_pawn(player,piece_pos,move_to):
    # Check that the user enters a valid pawn move
        
    # Determine what type of move the player is attempting
    # Remember, an increase in the row index means moving down
    vertical_move = move_to[0] - piece_pos[0]
    horizontal_move = move_to[1] - piece_pos[1]
    # Forward move
    if horizontal_move == 0:
        # Move the pawn one space
        if (vertical_move == 1 and player == 'b') or \
            (vertical_move == -1 and player == 'w'):
            pass
        # Move the pawn two spaces if it has not yet moved.
        elif (vertical_move == 2 and player == 'b') or \
            (vertical_move == -2 and player == 'w'):
            # Check whether pawn has already been moved once
            if (player == "w" and piece_pos[0] != 6) or \
                (player == "b" and piece_pos[0] != 1):
                msg = "\nThis pawn has already been moved, so you can" \
                      " only move it by one space."
                print(msg)
                return False
            # Check whether pawn is blocked
            if player == "w":
                if board[piece_pos[0] - 1][piece_pos[1]] != "  ":
                    print("Your pawn is blocked!")
                    return False
                elif board[piece_pos[0] - 2][piece_pos[1]] != "  ":
                    print("\nThere is already another piece in your selected \
                           spot.")
                    return False
            else:
                if board[piece_pos[0] + 1][piece_pos[1]] != "  ":
                    print("Your pawn is blocked!")
                    return False
                elif board[piece_pos[0] + 2][piece_pos[1]] != "  ":
                    print("\nThere is already another piece in your selected \
                           spot.")
                    return False
        # Non-valid move
        else:
            print("\nA pawn must move forward 1 or 2 spaces.")
            return False
    # Attack move
    elif horizontal_move == -1 or horizontal_move == 1:
        if (vertical_move == 1 and player == 'b') or \
            (vertical_move == -1 and player == 'w'):
            if player == "w":
                if board[move_to[0]][move_to[1]][0] != "b":
                    print("Error: You can only attack a black piece")
                    return False
            else:
                if board[move_to[0]][move_to[1]][0] != "w":
                    print("Error: You can only attack a white piece")
                    return False
        # Non-valid move
        else:
            print("\nA pawn can move forward by only one space when \
                  attacking.")
            return False
    # Non-valid move
    else:
        print("\nA pawn cannot move more than 1 space to the left or right.")
        return False
    
    # This function returns True if no errors are detected.
    return True
    


