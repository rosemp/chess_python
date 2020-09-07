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

    # Note: A king cannot put another king in check

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
    
    # BISHOP
    # Check to the upper right of the king
    blocked = False
    row = square[0]
    col = square[1]
    while True:
        row -= 1
        col += 1
        if row < 0 or col > 7:
            break
        if board[row][col] == other_player + "b":
            return True
        # Check for any piece that is in the way of a possible opponent's bishop
        elif board[row][col] != "  ":
            break
    # Check to the upper left of the king
    blocked = False
    row = square[0]
    col = square[1]
    while True:
        row -= 1
        col -= 1
        if row < 0 or col < 0:
            break
        if board[row][col] == other_player + "b":
            return True
        elif board[row][col] != "  ":
            break
    # Check to the lower left of the king
    blocked = False
    row = square[0]
    col = square[1]
    while True:
        row += 1
        col -= 1
        if row > 7 or col < 0:
            break
        if board[row][col] == other_player + "b":
            return True
        elif board[row][col] != "  ":
            break
    # Check to the lower right of the king
    blocked = False
    row = square[0]
    col = square[1]
    while True:
        row += 1
        col += 1
        if row > 7 or col > 7:
            break
        if board[row][col] == other_player + "b":
            return True
        elif board[row][col] != "  ":
            break

    # ROOK
    blocked = False
    # Check to the right of the king
    for i in range(square[1] + 1, 8):
        # Check for any piece that is in the way of a possible opponent's rook
        if board[square[0]][i] == other_player + "r":
            return True
        elif board[square[0]][i] != "  ":
            break
    blocked = False
    # Check above the king
    for i in range(square[0] - 1, -1, -1):
        if board[i][square[1]] == other_player + "r":
            return True
        elif board[i][square[1]] != "  ":
            break
    blocked = False
    # Check to the left of the king
    for i in range(square[1] - 1, -1, -1):
        if board[square[0]][i] == other_player + "r":
            return True
        elif board[square[0]][i] != "  ":
            break
    blocked = False
    # Check below the king
    for i in range(square[0] + 1, 8):
        if board[i][square[1]] == other_player + "r":
            return True
        elif board[i][square[1]] != "  ":
            break

    # QUEEN
    # First lets check all four horizontal/vertical paths around the king
    blocked = False
    # Check to the right of the king
    for i in range(square[1] + 1, 8):
        # Check for any piece that is in the way of a possible opponent's queen
        if board[square[0]][i] == other_player + "q":
            return True
        elif board[square[0]][i] != "  ":
            break
    blocked = False
    # Check above the king
    for i in range(square[0] - 1, -1, -1):
        if board[i][square[1]] == other_player + "q":
            return True
        elif board[i][square[1]] != "  ":
            break
    blocked = False
    # Check to the left of the king
    for i in range(square[1] - 1, -1, -1):
        if board[square[0]][i] == other_player + "q":
            return True
        elif board[square[0]][i] != "  ":
            break
    blocked = False
    # Check below the king
    for i in range(square[0] + 1, 8):
        if board[i][square[1]] == other_player + "q":
            return True
        elif board[i][square[1]] != "  ":
            break
    # Now we check the four corners surrounding the king
    row = square[0]
    col = square[1]
    while True:
        row -= 1
        col += 1
        if row < 0 or col > 7:
            break
        if board[row][col] == other_player + "q":
            return True
        # Check for any piece that is in the way of a possible opponent's queen
        elif board[row][col] != "  ":
            break
    # Check to the upper left of the king
    blocked = False
    row = square[0]
    col = square[1]
    while True:
        row -= 1
        col -= 1
        if row < 0 or col < 0:
            break
        if board[row][col] == other_player + "q":
            return True
        elif board[row][col] != "  ":
            break
    # Check to the lower left of the king
    blocked = False
    row = square[0]
    col = square[1]
    while True:
        row += 1
        col -= 1
        if row > 7 or col < 0:
            break
        if board[row][col] == other_player + "q":
            return True
        elif board[row][col] != "  ":
            break
    # Check to the lower right of the king
    blocked = False
    row = square[0]
    col = square[1]
    while True:
        row += 1
        col += 1
        if row > 7 or col > 7:
            break
        if board[row][col] == other_player + "q":
            return True
        elif board[row][col] != "  ":
            break

    # If no attacking pieces are putting the king in check, return False
    return False


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
