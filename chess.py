from game_state import *
from utils import *
from move_piece_mod import *


print_board(board)
# White player moves first
player = "w"
# Game will run indefinitely in current form
while True:
    if player == "w":
        print("\nIt is the white player's turn.")
    else:
        print("\nIt is the black player's turn.")
    
    king_location = find_king(player)
    if check(player, king_location):
        if check_mate(player):
            if player == "w":
                print("\nGame declared checkmate. Black team wins.")
            else:
                print("\nGame declared checkmate. White team wins.")
        else:
            print("\nYour king is in check!")
        
    # Prompt player for their move and then make the move.
    while True:
        piece_pos = which_piece(player)
        valid = move_piece(player, piece_pos)
        if valid:
            break

    # Print board after move has been made.
    print("\n")
    print_board(board)

    # This "if block" switches the turn between players
    if player == "w":
        player = "b"
    else:
        player = "w"
