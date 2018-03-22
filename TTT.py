import os

def start(): 
    os.system('clear')
    board = [ '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    end = False
    win_commbinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    def startBoard():
        print("That are the places where you can put X or O:")
        print()
        print('     7 | 8 | 9')
        print('    ---|---|---')
        print('     4 | 5 | 6')
        print('    ---|---|---')
        print('     1 | 2 | 3')

    def drawBoard(board):
        print()
        print('     '  + board[7] + ' | '  + board[8] + ' | '  + board[9])
        print('    ---|---|---')
        print('     '  + board[4] + ' | '  + board[5] + ' | '  + board[6])
        print('    ---|---|---')
        print('     '  + board[1] + ' | '  + board[2] + ' | '  + board[3])
        print()

    def player1():
        n=chooseplace()
        if board[n]=="O" or board[n]=="X":
            print("That place has been already choosen. Choose another one!")
            player1()
        else:
            board[n]= "X"

    def player2():
        n=chooseplace()
        if board[n]=="O" or board[n]=="X":
            print("That place has been already choosen. Choose another one!")
            player2()
        else:
            board[n]= "O"

    def chooseplace():
        while True:
            choosenplace=input('Choose place (1-9): ')
            try:
                if int(choosenplace) in range(1,10):
                    return choosenplace
            except ValueError:
                print("\nThat's not on the board. Choose number between 1 and 9!")

    def checking():
        insertedXO = 0
        for a in (win_commbinations):
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True
            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":

                insertedXO += 1
            if insertedXO == 8:
                print("The game ends in a Tie\n")
                return True

   #main function
    while not end:
        startBoard()
        drawBoard(board)
        end = checking()
        if end == True:
            break
        print("\nplayer 1")    
        player1()
        os.system('clear')
        startBoard()
        drawBoard(board)
        end = checking()
        if end == True:
            break
        print("\nplayer 2")
        player2()
        os.system('clear')
    if input('Wanna play again? (y/n)') == "y":
        os.system('clear')
        start()
    else:
        print('See you')
        os.system('clear')
        
start()