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
    # checking for center spot
    if board[1][1] == " ":
        board[1][1] = "O"
        return

    random_row = random.choice(board)
    random_col = random.randint(0, 2)
    if random_row[random_col] == " ":
        random_row[random_col] = "O"
        return
    else:
        ai_move(board)


def player_move(board):
    print_board(board)
    row = input("Chose the row:")
    column = input("Chose the column:")
    if board[int(row) - 1][int(column) - 1] == " ":
        board[int(row) - 1][int(column) - 1] = "X"
    else:
        print("This spot is already taken")
        player_move(board)
    ai_move(board)
    player_move(board)


player_move(board)
