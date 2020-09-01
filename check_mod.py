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
    
    Note: When checking for check, you need to check for all of the opponent's 
    pieces, because any of those pieces can put the king in check.
    

    More planning----(google docs)

    """
    
    if player == "w":
        other_player = "b"
    else:
        other_player = "w"

    # PAWN CHECK: Check the two spots in front of the king from which the
    # opponent's pawns could threaten him.
    if player == "w":
        # Check upper right square for attacking pawn
        in_bounds_list = [square[0] - 1, square[1] + 1]
        if in_bounds(in_bounds_list):
            if board[square[0] - 1][square[1] + 1] == "bp":
                return True

        in_bounds_list = [square[0] - 1, square[1] - 1]
        if in_bounds(in_bounds_list):
            if board[square[0] - 1][square[1] - 1] == "bp":
                return True

    elif player == "b":
        in_bounds_list = [square[0] + 1, square[1] + 1]
        if in_bounds(in_bounds_list):
            if board[square[0] + 1][square[1] + 1] == "wp":
                return True

        in_bounds_list = [square[0] + 1, square[1] - 1]
        if in_bounds(in_bounds_list):
            if board[square[0] + 1][square[1] - 1] == "wp":
                return True
    
    # KNIGHT CHECK: Check the eight spots around the king that a knight could
    # possibly attack from.
    attack_square = []
    attack_square.append([square[0] - 1, square[1] + 2])
    attack_square.append([square[0] - 2, square[1] + 1])
    attack_square.append([square[0] - 2, square[1] - 1])
    attack_square.append([square[0] - 1, square[1] - 2])
    attack_square.append([square[0] + 1, square[1] - 2])
    attack_square.append([square[0] + 2, square[1] - 1])
    attack_square.append([square[0] + 2, square[1] + 1])
    attack_square.append([square[0] + 1, square[1] + 2])
    
    for asquare in attack_square:
        if in_bounds(asquare):
            if board[asquare[0]][asquare[1]] == other_player + "n":
                return True
    
    # Note: King cannot put the other king in check
    
    # BISHOP

    # ROOK
    blocked = False
    # Check to the right of the king
    for i in range(square[1], 8):
        if board[square[0]][i] == other_player + "r":
            if not blocked:
                return True
        # Check for any piece that is in the way of a possible opponents rook
        elif board[square[0]][i] != "  ":
            blocked = True
            break

    blocked = False
    # Check above the king
    for i in range(square[0], -1, -1):
        if board[i][square[1]] == other_player + "r":
            if not blocked:
                return True
        # Check for any piece that is in the way of a possible opponents rook
        elif board[i][square[1]] != "  ":
            blocked = True
            break

    blocked = False
    # Check to the left of the king
    for i in range(square[1], -1, -1):
        if board[square[0]][i] == other_player + "r":
            if not blocked:
                return True
        # Check for any piece that is in the way of a possible opponents rook
        elif board[square[0]][i] != "  ":
            blocked = True
            break

    blocked = False
    # Check below the king
    for i in range(square[0], +8):
        if board[i][square[1]] == other_player + "r":
            if not blocked:
                return True
        # Check for any piece that is in the way of a possible opponents rook
        elif board[i][square[1]] != "  ":
            blocked = True
            break

    # QUEEN
    # For hw

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
