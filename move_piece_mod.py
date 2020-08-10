from game_state import *
from pawn import *
from bishop import *
from knight import *
from rook import *
from queen import *
from king import *
from utils import *


def which_piece(player):
    piece_pos = [0, 0]
    # Check that user enters the proper piece
    while True:
        inp_string = input("\nWhich piece do you want to move?  ")
        piece_pos = parse_input_coords(inp_string)
        if piece_pos[0] == -1:
            continue
        # Makes sure player doesn't pick a blank space or the
        # other player's piece.
        if player != board[piece_pos[0]][piece_pos[1]][0]:
            print("\nYou must pick one of your pieces.")
            continue
        return piece_pos


def move_piece(player, piece_pos):
    piece_type = board[piece_pos[0]][piece_pos[1]][1]
    valid_move = False

    while True:
        move_to = [0, 0]
        inp_string = input("\nWhich square do you want to move it to?  ")
        if inp_string == "abort" or inp_string == "new piece":
            break
        move_to = parse_input_coords(inp_string)
        if move_to[0] == -1:
            continue
        
        if piece_type == "p":
            valid_move = move_pawn(player, piece_pos, move_to)
        elif piece_type == "b":
            valid_move = move_bishop(player, piece_pos, move_to)
        elif piece_type == "n":
            valid_move = move_knight(player, piece_pos, move_to)
        elif piece_type == "r":
            valid_move = move_rook(player, piece_pos, move_to)
        elif piece_type == "q":
            valid_move = move_queen(player, piece_pos, move_to)
        elif piece_type == "k":
            valid_move = move_king(player, piece_pos, move_to)
        
        if valid_move:
            break
    
    # If player enters a valid move, then move the piece
    if valid_move:
        piece = player + piece_type
        board[piece_pos[0]][piece_pos[1]] = "  "
        board[move_to[0]][move_to[1]] = piece
    
    return valid_move
