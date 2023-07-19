print("\t\t\tTIC TAC TOE")

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def tic_tac():
    print(f"{board[0]}  |  {board[1]}  |  {board[2]}")
    print("---- --- ----")
    print(f"{board[3]}  |  {board[4]}  |  {board[5]}")
    print("---- --- ----")
    print(f"{board[6]}  |  {board[7]}  |  {board[8]}", "\n")


def player1():
    print("Player 1")
    while (True):
        p1 = int(input("Enter the Grid Number Where you want to mark: "))
        if (p1 not in values):
            print("\nGrid Already Occupied!! Place SomeWhere Else\n")
        else:
            break
    board[p1-1] = 'O'
    values.remove(p1)


def player2():
    print("Player 2")
    while (True):
        p2 = int(input("Enter the Grid Number where you want to mark: "))
        if (p2 not in values):
            print("\nGrid Already Occupied!! Place SomeWhere Else\n")
        else:
            break
    board[p2-1] = 'X'
    values.remove(p2)


def row_win():
    for i in range(0, 9, 3):
        if (board[i] == board[i+1] and board[i+1] == board[i+2]):
            print(board[i]+" Won ")
            exit(0)


def column_win():
    for i in range(3):
        if (board[i] == board[i+3] and board[i+3] == board[i+6]):
            print(board[i]+" Won")
            exit(0)


def daigonal_win():
    if (board[0] == board[4] and board[4] == board[8]):
        print(board[0]+" Won")
        exit(0)
    elif (board[2] == board[4] and board[4] == board[6]):
        print(board[2]+" Won")
        exit(0)


tic_tac()
for i in range(5):
    player1()
    tic_tac()
    row_win()
    column_win()
    daigonal_win()
    if i == 4:
        continue
    player2()
    tic_tac()
    row_win()
    column_win()
    daigonal_win()
print("Draw")