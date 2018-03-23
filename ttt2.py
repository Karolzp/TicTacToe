import os
import sys
import random
duration = 0.1  # second
freq = 500  # Hz
os.system('clear')
board = ['-'] * 10
char_dict = {}
character = ['X', "O"]
end = False
win_commbinations = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9], 
    [1, 4, 7], 
    [2, 5, 8], 
    [3, 6, 9],
    [1, 5, 9], 
    [3, 5, 7]]
krok = 1
yn = ""
click = ""


def firstboard():
    print("               ,,                                                                ")
    print("MMP^^MM^^YMM   db               MMP^^MM^^YMM                       MMP^^MM^^YMM   ")
    print("P'   MM   `7                    P'   MM   `7                       P'   MM   `7    ")
    print("     MM        MM   ,p6^bo           MM       ,6^Yb.   ,p6^bo           MM       ,pW^Wq.   .gP6Ya  ")
    print("     MM        MM  6M'  OO           MM      8)   MM  6M'  OO           MM      6W'   `Wb ,M'   Yb")
    print("     MM        MM  8M                MM       ,pm9MM  8M                MM      8M     M8 Codecool")
    print("     MM        MM  YM.    ,          MM      8M   MM  YM.    ,          MM      YA.   ,A9 YM.    , ")
    print("   .JMML.    .JMML. YMbmd'         .JMML.    `Moo9^Yo. YMbmd'         .JMML.     `Ybmd9'   `Mbmmd' ")
    print("\n                                       Enter p to play :)")


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
    print('     ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('    ---|---|---')
    print('     ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('    ---|---|---')
    print('     ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print()


def choosegamemode():
    print("1.Muliplayer")
    print('2.Single player')
    x = 0
    while x not in [1, 2]:

        try:
            x = int(input('Choose game mode: '))
            if x in [1, 2]:
                return x
        except ValueError:
            continue


def chooseCharacter():
    choosencharacter = ''
    while choosencharacter.upper() not in character:
        choosencharacter = str(input('Player 1 Choose X or O: '))
        if choosencharacter.upper() == "X":
            return {1: 'X', 2: 'O'}
        elif choosencharacter.upper() == "O":
            return {1: 'O', 2: 'X'}


def playerchoseplace(number):
    n = chooseplace(number)
    if board[n] in character:
        print("\nThat place has been already choosen. Choose another one!")
        playerchoseplace(number)
    else:
        board[n] = char_dict.get(number)
        os.system(
            'play --no-show-progress --null --channels 1 synth %s sine %f' %
            (duration, freq))
        refresh()


def computerchoseplace():
    n = random.randint(1, 9)
    if board[n] in character:
        computerchoseplace()
    else:
        board[n] = char_dict.get(2)
        os.system(
            'play --no-show-progress --null --channels 1 synth %s sine %f' %
            (duration, freq))
        refresh()


def chooseplace(number):
    place = 0
    while place not in list(range(1, 10)):
        place = input(
            'Player {}({}) Choose place (1-9): '.format(number, char_dict.get(number)))
        try:
            if int(place) in list(range(1, 10)):
                return int(place)
            else:
                print("That's not on the board. Choose number between 1 and 9!\n")
        except ValueError:
            print("That's not on the board. Choose number between 1 and 9!\n")


def checking(modegame):
    insertedXO = 0
    for a in (win_commbinations):
        if board[a[0]] == board[a[1]] == board[a[2]] == char_dict.get(1):
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[a[0]] == board[a[1]] == board[a[2]] == char_dict.get(2):
            if modegame == 2:
                print("Computer win!\n")
            else:
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
            return True
    for a in range(9):
        if board[a] == "X" or board[a] == "O":
            insertedXO += 1
        if insertedXO == 8:           
            print("The game ends in a Tie\n")
            os.system(
                'play --no-show-progress --null --channels 1 synth %s sine %f' %
                (1.5, 700))
            os.system('spd-say "haha! loosers"')
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


def startscreen(click):
    firstboard()
    os.system('spd-say "Welcome! To Tic Tac Toe game! Enter p to play"')
    while click.lower() != "p":
        click = input()
        os.system('clear')
        firstboard()
    os.system('clear')


def endgame(yn2):
    yn2 = ""
    while yn2 != "n":
        yn2 = input('Wanna play again? (y/n)')
        if yn2 == "y":
            restart_program()
        refresh()


#          main function         #
startscreen(click)
game = choosegamemode()
os.system('clear')
if game == 1:
    char_dict = chooseCharacter()
    refresh()
    while end != True:
        refresh()
        playerchoseplace(one_or_two(krok))
        krok += 1
        end = checking(game)
        if end:
            endgame(yn)
if game == 2:
    char_dict = chooseCharacter()
    refresh()
    while end != True:
        refresh()
        playerchoseplace(1)
        end = checking(game)
        if end:
            endgame(yn)
        refresh()
        computerchoseplace()
        end = checking(game)
        if end:
            endgame(yn)
