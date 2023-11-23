import random

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("_________")


def ai_move(board):
    # blockin diagonal loss
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == " ":
        board[2][2] = "O"
        return
    elif board[1][1] == "X" and board[2][2] == "X" and board[0][0] == " ":
        board[0][0] = "O"
        return
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == " ":
        board[2][0] = "O"
        return
    elif board[1][1] == "X" and board[2][0] == "X" and board[0][2] == " ":
        board[0][2] = "O"
        return
    # checking for horizontal loss
    for i in range(len(board)):
        if board[i].count("X") == 2 and " " in board[i]:
            f = board[i].index(" ")
            board[i][f] = "O"
            return
    # checking for vertical loss

    for column in range(3):
        if (board[0][column], board[1][column], board[2][column]).count("X") == 2 and " " in (
        board[0][column], board[1][column], board[2][column]):
            index_of_space = (board[0][column], board[1][column], board[2][column]).index(" ")
            board[index_of_space][column] = "O"
    # checking for center spot
    if board[1][1] == " ":
        board[1][1] = "O"
        return
    # random move
    random_row = random.choice(board)
    random_col = random.randint(0, 2)
    if random_row[random_col] == " ":
        random_row[random_col] = "O"
        return
    else:
        ai_move(board)


def player_move(board):
    print_board(board)
    try:
        row = int(input("Chose the row:"))
    except ValueError:
        print("Invalid input")
        player_move(board)
        return

    if row > 3 or row < 1:
        print("Invalid Move, pick 1, 2 or 3")
        player_move(board)
    try:
        column = int(input("Chose the column:"))
    except ValueError:
        print("Invalid input")
        player_move(board)
        return
    if column > 3 or column < 1:
        print("Invalid Move, pick 1, 2 or 3")
        player_move(board)


    elif board[row - 1][column - 1] == " ":
        board[row - 1][column - 1] = "X"
    else:
        print("This spot is already taken")
        player_move(board)
    ai_move(board)
    player_move(board)


player_move(board)
