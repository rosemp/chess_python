def print_board(board):
    print("Current chess board:")
    for i in range(len(board)):
        print(board[i])


board = [["wr", "wn", "wb", "wk", "wq", "wb", "wn", "wr"],
         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
         ["br", "bn", "bb", "bk", "bq", "bb", "bn", "br"]]
player = "w"

print_board(board)

# Loop for the main game (only running 5 moves at this time).
for i in range(5):
    pawn_pos = [0, 0]
    if player == "w":
        print("\nIt is the white player's turn.")
    else:
        print("\nIt is the black player's turn.")
    
    #Check that user enters the proper piece
    while True:
        inp_string = input("\nWhich pawn do you want to move?")
        split_string = inp_string.split()
        for element in split_string:
            check_numeric = element.isnumeric()
            if not check_numeric:
                print("\nYou have to enter integers.")
                break
        if not check_numeric:
            continue
        pawn_pos[0] = int(split_string[0])
        pawn_pos[1] = int(split_string[1])
        # Makes sure player doesn't pick a black space or the
        # other player's piece.
        if player != board[pawn_pos[0]][pawn_pos[1]][0]:
            print("\nYou picked an invalid position.")
            continue
        # Makes sure player doesn't pick a piece other than a
        # pawn.
        if board[pawn_pos[0]][pawn_pos[1]][1] != "p":
            print("\nYou picked the other player's piece.")
            continue
    
        # Make sure that the user only moves a pawn 1 or 2 spaces
        while True:
            inp_string = input("\nHow many spaces would you like to move?")
            # Move distance
            move_dist = int(inp_string)
            if move_dist < 1 or move_dist > 2:
                print("\nInvalid number. Move distance must be 1 or 2.")
                continue
            # Need to leave this loop if there is no error.
            break
        
        # If the player wants to move the pawn two spaces, check whether the 
        # pawn has been moved yet.
        if move_dist == 2:
            # White player
            if player == "w":
                if pawn_pos[0] != 1:
                    print("\nThis pawn has already been moved, so you can \
                           only move it by one space.")
                    move_dist = 1
            # Black player
            else:
                if pawn_pos[0] != 6:
                    print("\nThis pawn has already been moved, so you can \
                           only move it by one space.")
                    move_dist = 1
        
        # Check whether the space is empty
        new_pawn_row = pawn_pos[0]
        if player == "w":
            new_pawn_row += move_dist
        else:
            new_pawn_row -= move_dist
        if board[new_pawn_row][pawn_pos[1]] != "  ":
            print("\nThere is already another piece in your selected spot.")
            continue
        
        # For a pawn moving two places, make sure it's not blocked
        if move_dist == 2:
            if player == "w":
                if board[pawn_pos[0] + 1][pawn_pos[1]] != "  ":
                    print("Your pawn is blocked!")
                    continue
            else:
                if board[pawn_pos[0] - 1][pawn_pos[1]] != "  ":
                    print("Your pawn is blocked!")
                    continue
        
        # If there are no errors, we want to exit the while loop.
        break
    
    # Now that the program has done all of the checks for the pawn,
    # it will move the pawn to its new spot.
    board[pawn_pos[0]][pawn_pos[1]] = "  "
    if player == "w":
        pawn_pos[0] += move_dist
        board[pawn_pos[0]][pawn_pos[1]] = "wp"
    else:
        pawn_pos[0] -= move_dist
        board[pawn_pos[0]][pawn_pos[1]] = "bp"

    print("\n")
    print_board(board)

    if player == "w":
        player = "b"
    else:
        player = "w"