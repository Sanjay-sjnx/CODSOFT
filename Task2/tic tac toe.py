from tkinter import *

root = Tk()
root.geometry("300x400")
root.title("Tic Tac Toe")

root.resizable(0, 0)

frame1 = Frame(root)
frame1.pack(pady=5)
titleLabel = Label(frame1, text="Tic Tac Toe", font=("Helvetica", 18, 'bold'), bg="black", fg="red", width=20)
titleLabel.grid(row=0, column=0)

optionFrame = Frame(root, bg="black")
optionFrame.pack(pady=5)

frame2 = Frame(root, bg="black")
frame2.pack(pady=5)

board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

turn = "x"
game_end = False
mode = "singlePlayer"


def changeModeToSinglePlayer():
    global mode
    mode = "singlePlayer"
    singlePlayerButton["bg"] = "red"
    multiPlayerButton["bg"] = "black"


def changeModeToMultiplayer():
    global mode
    mode = "multiPlayer"
    multiPlayerButton["bg"] = "red"
    singlePlayerButton["bg"] = "black"


def updateBoard():
    for key in board.keys():
        buttons[key - 1]["text"] = board[key]


def checkForWin(player):
    # rows
    if board[1] == board[2] and board[2] == board[3] and board[3] == player:
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[6] == player:
        return True
    elif board[7] == board[8] and board[8] == board[9] and board[9] == player:
        return True

    # columns
    elif board[1] == board[4] and board[4] == board[7] and board[7] == player:
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[8] == player:
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[9] == player:
        return True

    # diagonals
    elif board[1] == board[5] and board[5] == board[9] and board[9] == player:
        return True
    elif board[3] == board[5] and board[5] == board[7] and board[7] == player:
        return True

    return False


def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False

    return True


def restartGame():
    global game_end
    game_end = False
    for button in buttons:
        button["text"] = " "

    for i in board.keys():
        board[i] = " "

    titleLabel.config(text="Tic Tac Toe")


def minimax(board, isMaximizing):
    if checkForWin("o"):
        return 1

    if checkForWin("x"):
        return -1

    if checkForDraw():
        return 0

    if isMaximizing:
        bestScore = -100
        for key in board.keys():
            if board[key] == " ":
                board[key] = "o"
                score = minimax(board, False)
                board[key] = " "
                if score > bestScore:
                    bestScore = score

        return bestScore

    else:
        bestScore = 100
        for key in board.keys():
            if board[key] == " ":
                board[key] = "x"
                score = minimax(board, True)
                board[key] = " "
                if score < bestScore:
                    bestScore = score

        return bestScore


def playComputer():
    bestScore = -100
    bestMove = 0

    for key in board.keys():
        if board[key] == " ":
            board[key] = "o"
            score = minimax(board, False)
            board[key] = " "
            if score > bestScore:
                bestScore = score
                bestMove = key

    board[bestMove] = "o"


# Function to play
def play(event):
    global turn, game_end
    if game_end:
        return

    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]
    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)

    if button["text"] == " ":
        if turn == "x":
            board[clicked] = turn
            if checkForWin(turn):
                winningLabel = Label(frame1, text=f"{turn} wins the game", bg="black", fg="red", font=("Helvetica", 18, 'bold'), width=20)
                winningLabel.grid(row=0, column=0, columnspan=3)
                game_end = True

            turn = "o"
            updateBoard()

            if mode == "singlePlayer":
                playComputer()

                if checkForWin(turn):
                    winningLabel = Label(frame1, text=f"{turn} wins the game", bg="black", fg="red", font=("Helvetica", 18, 'bold'), width=20)
                    winningLabel.grid(row=0, column=0, columnspan=3)
                    game_end = True

                turn = "x"
                updateBoard()

        else:
            board[clicked] = turn
            updateBoard()
            if checkForWin(turn):
                winningLabel = Label(frame1, text=f"{turn} wins the game", bg="black", fg="red", font=("Helvetica", 18, 'bold'), width=20)
                winningLabel.grid(row=0, column=0, columnspan=3)
                game_end = True
            turn = "x"

        if checkForDraw():
            drawLabel = Label(frame1, text=f"Game Draw", bg="black", fg="red", font=("Helvetica", 18, 'bold'), width=20)
            drawLabel.grid(row=0, column=0, columnspan=3)


# ------ UI --------

# Change Mode options
singlePlayerButton = Button(optionFrame, text="SinglePlayer", width=10, height=1, font=("Helvetica", 10, 'bold'), bg="black", fg="red", relief=RAISED, borderwidth=3, command=changeModeToSinglePlayer)
singlePlayerButton.grid(row=0, column=0, columnspan=1, sticky=NW, padx=5, pady=5)

multiPlayerButton = Button(optionFrame, text="Multiplayer", width=10, height=1, font=("Helvetica", 10, 'bold'), bg="black", fg="red", relief=RAISED, borderwidth=3, command=changeModeToMultiplayer)
multiPlayerButton.grid(row=0, column=1, columnspan=1, sticky=NW, padx=5, pady=5)

# Tic Tac Toe Board
buttons = []
for i in range(3):
    for j in range(3):
        button = Button(frame2, text=" ", width=4, height=2, font=("Helvetica", 18, 'bold'), bg="black", fg="white", relief=RAISED, borderwidth=3)
        button.grid(row=i, column=j, padx=5, pady=5)
        button.bind("<Button-1>", play)
        buttons.append(button)

restartButton = Button(frame2, text="Restart Game", width=15, height=1, font=("Helvetica", 12, 'bold'), bg="black", fg="red", relief=RAISED, borderwidth=3, command=restartGame)
restartButton.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
