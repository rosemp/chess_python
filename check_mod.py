
from game_state import *


# For check
def check(player, square):
    """
    This function checks whether king is in check
    :argument player: This is the string (w or b) that indicates the team whose king we are checking
    :argument square: This is the list of two integers that says where the king is or where the king wants to move
    Note 1: When checking for check, you need to check for all of the opponents pieces, because any of those pieces can
    put the king in check.
    Note 2: If king is in check because of it's opponents piece, it must move to a safe location. To find that safe
    location, the code needs to loop over the area the king can usually move, and check if there are any pieces in that
    area. The king cannot move out of check to an area where there are opponent pieces.

    More planning----(google docs)

    """
    pass


# For checkmate
def check_mate(player):
    """
    This function checks whether king is in checkmate
    :argument player: This is the string (w or b) that indicates the team whose king we are checking
    Note 3: If the code loops over the usual moves and finds that the king cannot move out of check safely, it is
    declared checkmate, and the opponent wins.

    """
    pass
