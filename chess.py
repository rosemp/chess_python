from game_state import *
from utils import *
from move_piece_mod import *

print_board(board)

# Loop for the main game (only running 5 moves at this time).
player = "w"
for i in range(10):
    if player == "w":
        print("\nIt is the white player's turn.")
    else:
        print("\nIt is the black player's turn.")
    
    # Prompt player for their move and then make the move.    
    move_piece(player)

    # Print board after move has been made.
    print("\n")
    print_board(board)

    # This "if block" switches the turn between players
    if player == "w":
        player = "b"
    else:
        player = "w"

