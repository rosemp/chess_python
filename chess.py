from game_state import *
from utils import *
from move_piece_mod import *


print_board(board)
# Loop for the main game (only running 20 moves at this time).
# Turn this into an unbounded loop once checkmate functionality
# has been implemented.
player = "w"
for i in range(20):
    if player == "w":
        print("\nIt is the white player's turn.")
    else:
        print("\nIt is the black player's turn.")
    
    king_location = find_king(player)
    if check(player, king_location):
        print("Your king is in check!")
        if player == "w":
            white_player_check = True
        else:
            black_player_check = True
        
    # Prompt player for their move and then make the move.
    while True:
        piece_pos = which_piece(player)
        valid = move_piece(player,piece_pos)
        king_location = find_king(player)
        if check(player, king_location):
            print("You can't put yourself in check, please pick another move!")
            valid = False
            if player == "w":
                white_player_check = True
            else:
                black_player_check = True
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

