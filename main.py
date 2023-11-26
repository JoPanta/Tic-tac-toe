import random

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def reset_board():
    global board
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

def print_board():
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("_________")

def replay():
    global board
    play_again = input("Do you want to play again? Y or N: ").upper()
    if play_again == "Y":
        reset_board()
        main()
    elif play_again == "N":
        exit()
    else:
        print("Invalid input. Please enter Y for Yes or N for No.")
        return replay()


def ai_move():
    ai_played = False
    while not ai_played:
        #checkinf for diagonal win:
        if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == " ":
            board[2][2] = "O"
            ai_played = True
            return ai_played
        elif board[1][1] == "O" and board[2][2] == "O" and board[0][0] == " ":
            board[0][0] = "O"
            ai_played = True
            return ai_played
        elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == " ":
            board[2][0] = "O"
            ai_played = True
            return ai_played
        elif board[1][1] == "O" and board[2][0] == "O" and board[0][2] == " ":
            board[0][2] = "O"
            ai_played = True
            return ai_played
        #checking for horizontal win
        for i in range(len(board)):
            if board[i].count("O") == 2 and " " in board[i]:
                f = board[i].index(" ")
                board[i][f] = "O"
                ai_played = True
                return ai_played
        #checking for vertical win:
        for column in range(3):
            if ((board[0][column], board[1][column], board[2][column]).count("O") == 2
                    and " " in (board[0][column], board[1][column], board[2][column])):
                index_of_space = (board[0][column], board[1][column], board[2][column]).index(" ")
                board[index_of_space][column] = "O"
                ai_played = True
                return ai_played
        # blocking diagonal loss
        if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == " ":
            board[2][2] = "O"
            ai_played = True
            return ai_played
        elif board[1][1] == "X" and board[2][2] == "X" and board[0][0] == " ":
            board[0][0] = "O"
            ai_played = True
            return ai_played
        elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == " ":
            board[2][0] = "O"
            ai_played = True
            return ai_played
        elif board[1][1] == "X" and board[2][0] == "X" and board[0][2] == " ":
            board[0][2] = "O"
            ai_played = True
            return ai_played
        # blocking horizontal loss
        for i in range(len(board)):
            if board[i].count("X") == 2 and " " in board[i]:
                f = board[i].index(" ")
                board[i][f] = "O"
                ai_played = True
                return ai_played
        # blocking vertical loss

        for column in range(3):
            if ((board[0][column], board[1][column], board[2][column]).count("X") == 2
                    and " " in (board[0][column], board[1][column], board[2][column])):
                index_of_space = (board[0][column], board[1][column], board[2][column]).index(" ")
                board[index_of_space][column] = "O"
                ai_played = True
                return ai_played

        # checking for center spot
        if board[1][1] == " ":
            board[1][1] = "O"
            ai_played = True
            return ai_played

        # random move
        random_row = random.choice(board)
        random_col = random.choice(range(3))
        if random_row[random_col] == " ":
            random_row[random_col] = "O"
            ai_played = True
            return ai_played
        elif all(cell != " " for row in board for cell in row):
            ai_played = True
            return ai_played
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


def main():

    round = 1
    global board
    while True:
        print_board()

        if round == 1:
            first = input("Do you want to play first? Y or N: ").upper()
            if first == "N":
                ai_move()

                print_board()
            else:
                pass

        player_move()
        #checking if player wins
        #diagonal:
        if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X"
                or board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
            print_board()
            print("YOU WIN!")
            replay()
        #horizontal
        for i in range(len(board)):
            if board[i].count("X") == 3:
                print_board()
                print("YOU WIN!")
                replay()
        #vertical
        for column in range(3):
            if (board[0][column], board[1][column], board[2][column]).count("X") == 3:
                print_board()
                print("YOU WIN!")
                replay()
        #checking for a draw
        if board[0].count(" ") == 0 and board[1].count(" ") == 0 and board[2].count(" ") == 0:
            print_board()
            print("IT'S A DRAW!")
            replay()


        ai_move()
        #checking if ai wins
        #diagonal:
        if (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"
                or board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
            print_board()
            print("PC WINS!")
            replay()
        #horizontal
        for i in range(len(board)):
            if board[i].count("O") == 3:
                print_board()
                print("PC WINS!")
                replay()
        #vertical
        for column in range(3):
            if (board[0][column], board[1][column], board[2][column]).count("O") == 3:
                print_board()
                print("PC WINS!")
                replay()
        # checking for a draw
        if board[0].count(" ") == 0 and board[1].count(" ") == 0 and board[2].count(" ") == 0:
            print_board()
            print("IT'S A DRAW!")
            replay()

        round += 1


main()