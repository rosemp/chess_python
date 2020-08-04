
"""
Queen - Can move vertically, horizontally, or diagonally/anti-diagonally

Bishop - Can only move diagonally

Pawn - Can only move up to two spaces vertically at start, but afterwards it can only move 1 space vertically. It can
also move diagonally for attacking.

King - Can move just one space in every direction. If the king is in check, it has to move out of it. When it finally
can’t move out of check, the opposing player has officially put the king in checkmate, therefore winning the game.

Rook - Can move vertically or horizontally

Knight - The only piece that can jump over other pieces, having 8 move options that consist of the knight moving in an
L shape.

"""


"""     Chess board

   a |b |c |d |e |f |g |h 
  -------------------------
8 |br|bn|bb|bq|bk|bb|bn|br|
  -------------------------
7 |bp|bp|bp|bp|bp|bp|bp|bp|
  -------------------------
6 |  |  |  |  |  |  |  |  |
  -------------------------
5 |  |  |  |  |  |  |  |  |
  -------------------------
4 |  |  |  |  |  |  |  |  |
  -------------------------
3 |  |  |  |  |  |  |  |  |
  -------------------------
2 |wp|wp|wp|wp|wp|wp|wp|wp|
  -------------------------
1 |wr|wn|wb|wq|wk|wb|wn|wr|
  -------------------------  
"""
