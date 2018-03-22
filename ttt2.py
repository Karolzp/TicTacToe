
import os
import sys
os.system('clear')
board = ['-'] * 10
char={}
character = ['X',"O"]
end = False
win_commbinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
krok=1
yn=""

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

def chooseCharacter():
    choosencharacter=''
    while choosencharacter.upper() not in character:
        choosencharacter=str(input('Player 1 Choose X or O: '))
        if choosencharacter.upper() == "X":
            return {1:'X',2:'O'}
        elif choosencharacter.upper() == "O":
            return {1:'O',2:'X'}

def playerchoseplace(number):
    n=chooseplace(number)
    if board[n] in character:
        print("\nThat place has been already choosen. Choose another one!")
        playerchoseplace(number)
    else:       
        board[n]= char.get(number)
        refresh()

def chooseplace(number):
    choosenplace=0
    while choosenplace not in list(range(1,10)):       
        choosenplace=input('Player {}({}) Choose place (1-9): '.format(number ,char.get(number)))
        try:
            if int(choosenplace) in list(range(1,10)):
                return int(choosenplace)
            else:
                print("That's not on the board. Choose number between 1 and 9!\n")
        except ValueError:
            print("That's not on the board. Choose number between 1 and 9!\n")       
           
def checking():
    insertedXO = 0
    for a in (win_commbinations):
        if board[a[0]] == board[a[1]] == board[a[2]] == char.get(1):
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[a[0]] == board[a[1]] == board[a[2]] == char.get(2):
            print("Player 2 Wins!\n")
            print("Congratulations!\n")
            return True
    for a in range(9):
        if board[a] == "X" or board[a] == "O":
            insertedXO += 1
        if insertedXO == 8:
            print("The game ends in a Tie\n")
            return True

def one_or_two(step):
    if step % 2:
        return 1
    else:
        return 2
    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def refresh():
    os.system('clear')
    startBoard()
    drawBoard(board)
  
   #main function
char = chooseCharacter()
refresh()
while end != True:
    refresh()
    playerchoseplace(one_or_two(krok))
    krok+=1
    end = checking()
 
while yn != "n":
    yn=input('Wanna play again? (y/n)')
    if yn =="y":
        restart_program()
        