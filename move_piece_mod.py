from game_state import *
from pawn import *
from bishop import *
from knight import *
from rook import *
from queen import *
from king import *

def move_piece(player):
    piece = board[piece_loc[0]][piece_loc[1]][1]
    piece = "p"
    valid_move = False
    if piece == "p":
        valid_move = move_pawn(player)
    elif piece == "b":
        valid_move = move_bishop(player)
    elif piece == "n":
        valid_move = move_knight(player)
    elif piece == "r":
        valid_move = move_rook(player)
    elif piece == "q":
        valid_move = move_queen(player)
    elif piece == "k":
        valid_move = move_king(player)
    
    # If player enters a valid move, then move the piece
    if valid_move:
        pass
    