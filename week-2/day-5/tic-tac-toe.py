currentBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]
def display_board():
    board = f"        **************************\n\
        *  {currentBoard[0][0]}    |    {currentBoard[0][1]}   |    {currentBoard[0][2]}  *\n\
        *-------|--------|-------*\n\
        *   {currentBoard[1][0]}   |   {currentBoard[1][1]}    |   {currentBoard[1][2]}   *\n\
        *-------|--------|-------*\n\
        *   {currentBoard[2][0]}   |    {currentBoard[2][1]}   |    {currentBoard[2][2]}  *\n\
        **************************"
    print(board)

def checkForWin():
    for row in currentBoard:
        if row[0] == row [1] == row[2] and row[0] != " ":
            display_board()
            print(f"{row[0]} wins")
            return True

    for i in range(3):
        if currentBoard[0][i] == currentBoard[1][i] == currentBoard[2][i] and currentBoard[0][i] != " ":
            display_board()
            print(f"{currentBoard[0][i]} wins")
            return True
    
    if (currentBoard[0][0] == currentBoard[1][1] == currentBoard[2][2] or currentBoard[0][2] == currentBoard[1][1] == currentBoard[2][0]) and currentBoard[1][1] != " ":
        display_board()
        print(f"{currentBoard[1][1]} wins")
        return True
    
    return False

def takeTurn(player: str):
    try:
        rowNumber = int(input(f"Player {player} enter a row number: "))
        columnNumber = int(input(f"Player {player} enter a column number: "))
        if currentBoard[rowNumber][columnNumber] == " ":
            currentBoard[rowNumber][columnNumber] = player
        else: 
            print("Invalid move, try again")
            takeTurn(player)
            return
    except:
        print("Error try again ")
        takeTurn(player)

def play():
    gameOver = False
    while not gameOver:
        display_board()
        if checkForWin():
            break
        takeTurn("X")
        if checkForWin():
            break
        display_board()
        takeTurn("O")

play()

    