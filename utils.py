def print_board(current_board):
    print("   a |b |c |d |e |f |g |h ")
    print("  -------------------------")
    for i in range(8,0,-1):
        board_row_string = str(i) + " |"
        for j in range(8):
            board_row_string += current_board[8-i][j] + "|"
        print(board_row_string)
        print("  -------------------------")

    
def parse_input_coords(input_move):
    # This function should return the a 2-element list which contains the
    # row and column index of the chess piece or the square the player wants
    # to move it to.
    column_letters = "abcdefgh"
    if input_move[0] not in column_letters:
        print("Error: First character must be a letter")
        return [-1,-1]
    if not input_move[1].isnumeric():
        print("Error: Second character must be a number/integer")
        return [-1,-1]
    row = int(input_move[1])
    if row > 8 or row < 1:
        print("Error: Row index must be between 1 and 8")
        return [-1, -1]

    output_move = [0, 0]
    # Row index in the board display goes in reverse order compared to the
    # row index for the board array
    output_move[0] = 8 - row
    output_move[1] = column_letters.index(input_move[0])
    return output_move
