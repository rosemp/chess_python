
def print_board(current_board):
    print("Current chess board:")
    for i in range(len(current_board)):
        print(current_board[i])


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

    # Check that user enters the proper piece
    while True:
        inp_string = input("\nWhich pawn do you want to move?\n")
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
        # Makes sure player doesn't pick a blank space or the
        # other player's piece.
        if player != board[pawn_pos[0]][pawn_pos[1]][0]:
            print("\nYou must pick one of your pieces.")
            continue
        # Makes sure player doesn't pick a piece other than a
        # pawn.
        if board[pawn_pos[0]][pawn_pos[1]][1] != "p":
            print("\nYou must pick a pawn.")
            continue
        
        # Leave loop if there are no errors.
        break
    
    # Check that the user enters a valid pawn move
    while True:
        print("\nEnter the move you would like to do:")
        inp_string = input("\n'forward 1', 'forward 2','attack left','attack right'\n")
        # Input error checking
        split_input = inp_string.split()
        move_type = split_input[0].lower()
        if move_type == "forward":
            if not split_input[1].isnumeric():
                print("\nError: Please enter a move distance of 1 or 2.")
                continue
            
            move_dist = int(split_input[1])
            if move_dist < 1 or move_dist > 2:
                print("\nError: Invalid number. Move distance must be 1 or 2.")
                continue
            
            # If the player wants to move the pawn two spaces, check 
            # whether the pawn has been moved yet.
            if move_dist == 2:
                # White player
                if player == "w":
                    if pawn_pos[0] != 1:
                        print("\nThis pawn has already been moved, so you can only move it by one space.")
                        move_dist = 1
                        continue
                # Black player
                else:
                    if pawn_pos[0] != 6:
                        print("\nThis pawn has already been moved, so you can only move it by one space.")
                        move_dist = 1
                        continue
                    
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
        
        # Check to make sure pawn can attack
        elif move_type == "attack":
            attack_direction = split_input[1].lower()
            # attack_direction 'left' means pawn moves pawn_pos[1] -= 1
            # attack_direction 'right' means pawn moves pawn_pos[1] += 1
            attack_pos = [0, 0]
            if attack_direction == 'left':
                attack_pos[1] = pawn_pos[1] - 1
                if attack_pos[1] < 0:
                    print("\nError: Piece will go off the board")
                    continue

            elif attack_direction == 'right':
                attack_pos[1] = pawn_pos[1] + 1
                # Check to make sure piece doesn't go off the board
                if attack_pos[1] > 7:
                    print("/nError: Piece will go off the board")
                    continue
            # Make sure player enters valid direction (left or right?)
            else:
                print("\nError: Please enter an attack direction of 'left' or 'right'")
                continue
            if player == "w":
                attack_pos[0] = pawn_pos[0] + 1
                if board[attack_pos[0]][attack_pos[1]][0] != "b":
                    print("Error: You can only attack a black piece")
                    continue

            else:
                attack_pos[0] = pawn_pos[0] - 1
                if board[attack_pos[0]][attack_pos[1]][0] != "w":
                    print("Error: You can only attack a white piece")
                    continue

        else:
            print("\nError: You must enter 'forward' or 'attack'.")
            continue

        # If there are no errors, we want to exit the while loop.
        break

    # Now that the program has done all of the checks for the pawn,
    # it will move the pawn to its new spot.
    board[pawn_pos[0]][pawn_pos[1]] = "  "
    if move_type == "forward":
        if player == "w":
            pawn_pos[0] += move_dist
            board[pawn_pos[0]][pawn_pos[1]] = "wp"
        else:
            pawn_pos[0] -= move_dist
            board[pawn_pos[0]][pawn_pos[1]] = "bp"
    elif move_type == "attack":
        if player == "w":
            board[attack_pos[0]][attack_pos[1]] = "wp"
        else:
            board[attack_pos[0]][attack_pos[1]] = "bp"

    # Print board after move has been made.
    print("\n")
    print_board(board)

    if player == "w":
        player = "b"
    else:
        player = "w"

