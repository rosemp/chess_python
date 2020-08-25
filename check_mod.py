from game_state import *


# Find where the king is located
def find_king(player):
    """
    :argument player: This is the string (w or b) that indicates the team whose 
                      king we are checking
    :return A list of two integers which specify the row and column indices of 
            the king
    """
    
    king_name = player + "k"
    for row in range(8):
        for col in range(8):
            if board[row][col] == king_name:
                return [row, col]
    
def in_bounds(square):
    if square[0] < 0 or square[0] > 7:
        return False
    elif square[1] < 0 or square[1] > 7:
        return False
    else:
        return True

# For check
def check(player, square):
    """
    This function checks whether king is in check
    :argument player: This is the string (w or b) that indicates the team whose 
                      king we are checking
    :argument square: This is the list of two integers that says where the king
                      is or where the king wants to move
    :return True if player is in check, false if player is not in check.
    
    Note: When checking for check, you need to check for all of the opponents pieces, because any of those pieces can
    put the king in check.
    

    More planning----(google docs)

    """

    # PAWN CHECK: Check the two spots in front of the king from which the
    # opponent's pawns could threaten him.
    if player == "w":
        # Check upper right square for attacking pawn
        in_bounds_list = [square[0] - 1, square[1] + 1]
        if in_bounds(in_bounds_list):
            if board[square[0] - 1][square[1] + 1] == "bp":
                white_player_check = True
                return True

        in_bounds_list = [square[0] - 1, square[1] - 1]
        if in_bounds(in_bounds_list):
            if board[square[0] - 1][square[1] - 1] == "bp":
                white_player_check = True
                return True

    elif player == "b":
        in_bounds_list = [square[0] + 1, square[1] + 1]
        if in_bounds(in_bounds_list):
            if board[square[0] + 1][square[1] + 1] == "wp":
                black_player_check = True
                return True

        in_bounds_list = [square[0] + 1, square[1] - 1]
        if in_bounds(in_bounds_list):
            if board[square[0] + 1][square[1] - 1] == "wp":
                black_player_check = True
                return True
    
    # KNIGHT CHECK: Check the eight spots around the king that a knight could
    # possibly attack from.
    
    # KING CHECK: Check the eight adjacent spots to king that the opponent
    # king could possibly attack from.
    # Hw here
    
    # BISHOP
    # ROOK
    # QUEEN

    # Loop over 8 directions radially from
    # :square (right, upper right, up, etc.). Check for attacking rooks and
    # queens in vertical and horizontal directions, and attacking bishops and
    # queens in diagonal direction. Also, in each direction, check each square
    # in succession to make sure they're empty so that the attacking piece is 
    # actually putting the king in check.


# For checkmate
def check_mate(player):
    """
    This function checks whether king is in checkmate
    :argument player: This is the string (w or b) that indicates the team whose
    king we are checking.
    Note: If the code loops over the usual moves and finds that the king cannot
    move out of check safely, it is declared checkmate, and the opponent wins.

    """
    pass
