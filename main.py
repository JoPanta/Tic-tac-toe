import random

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

game_on = True

def print_board():
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("_________")


def ai_move():
    ai_played = False
    while not ai_played:
        # blocking diagonal loss
        if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == " ":
            board[2][2] = "O"
            ai_played = True
        elif board[1][1] == "X" and board[2][2] == "X" and board[0][0] == " ":
            board[0][0] = "O"
            ai_played = True
        elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == " ":
            board[2][0] = "O"
            ai_played = True
        elif board[1][1] == "X" and board[2][0] == "X" and board[0][2] == " ":
            board[0][2] = "O"
            ai_played = True
        # blocking horizontal loss
        for i in range(len(board)):
            if board[i].count("X") == 2 and " " in board[i]:
                f = board[i].index(" ")
                board[i][f] = "O"
                ai_played = True
        # blocking vertical loss

        for column in range(3):
            if ((board[0][column], board[1][column], board[2][column]).count("X") == 2
                    and " " in (board[0][column], board[1][column], board[2][column])):
                index_of_space = (board[0][column], board[1][column], board[2][column]).index(" ")
                board[index_of_space][column] = "O"
                ai_played = True

        # checking for center spot
        if board[1][1] == " ":
            board[1][1] = "O"
            ai_played = True

        # random move
        random_row = random.choice(board)
        random_col = random.randint(0, 2)
        if random_row[random_col] == " ":
            random_row[random_col] = "O"
            ai_played = True
        elif all(cell != " " for row in board for cell in row):
            ai_played = True
    return board


def player_move():
    try:
        row = int(input("Chose the row:"))
    except ValueError:
        print("Invalid input")
        player_move()
        return
    if row > 3 or row < 1:
        print("Invalid Move, pick 1, 2 or 3")
        player_move()

    try:
        column = int(input("Chose the column:"))
    except ValueError:
        print("Invalid input")
        player_move()
        return
    if column > 3 or column < 1:
        print("Invalid Move, pick 1, 2 or 3")
        player_move()

    elif board[row - 1][column - 1] == " ":
        board[row - 1][column - 1] = "X"
    else:
        print("This spot is already taken")
        player_move()


while game_on:
    print_board()
    player_move()
    #checking if player wins
    #diagonal:
    if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X"
            or board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        print("YOU WIN!")
        game_on = False
    #horizontal
    for i in range(len(board)):
        if board[i].count("X") == 3:
            print("YOU WIN!")
            game_on = False
    #vertical
    for column in range(3):
        if (board[0][column], board[1][column], board[2][column]).count("X") == 3:
            print_board()
            print("YOU WIN!")
            game_on = False
    #checking for a draw
    if board[0].count(" ") == 0 and board[1].count(" ") == 0 and board.count(" ") == 0:
        print_board()
        print("IT'S A DRAW")
        game_on = False
    ai_move()
    #checking if ai wins
    #diagonal:
    if (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"
            or board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        print_board()
        print("PC WINS!")
        game_on = False
    #horizontal
    for i in range(len(board)):
        if board[i].count("O") == 3:
            print_board()
            print("PC WINS!")
            game_on = False
    #vertical
    for column in range(3):
        if (board[0][column], board[1][column], board[2][column]).count("O") == 3:
            print_board()
            print("PC WINS!")
            game_on = False
    # checking for a draw
    if board[0].count(" ") == 0 and board[1].count(" ") == 0 and board.count(" ") == 0:
        print_board()
        print("IT'S A DRAW")
        game_on = False

