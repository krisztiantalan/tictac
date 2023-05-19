import os

board = dict()


def create_board():
    for i in range(1, 10):
        board[i] = '_'


def show_board():
    print(board[1] + ' ' + board[2] + ' ' + board[3])
    print(board[4] + ' ' + board[5] + ' ' + board[6])
    print(board[7] + ' ' + board[8] + ' ' + board[9])


def invalid(msg):
    os.system('cls')
    print('\n{}\n'.format(msg))
    show_board()


def move(char):
    field = input("\n{}'s move: ".format(char))
    if not field.isnumeric() or int(field) not in range(1, 10):
        invalid('Enter a number between 1-9: ')
        return move(char)
    elif board[int(field)] == '_':
        board[int(field)] = str(char)
        os.system('cls')
        show_board()
        check_score(char)
    else:
        invalid('Invalid move.')
        return move(char)


def play_again():
    global game
    print('Play again? Press y/n to play/quit.')
    choice = input()
    if choice == 'n':
        game = False
    elif choice == 'y':
        create_board()
        os.system('cls')
        show_board()
    else:
        return play_again()


def check_score(char):
    if (board[1] == board[2] == board[3] != '_')\
            or (board[1] == board[2] == board[3] != '_')\
            or (board[1] == board[4] == board[7] != '_')\
            or (board[1] == board[5] == board[9] != '_')\
            or (board[2] == board[5] == board[8] != '_')\
            or (board[3] == board[6] == board[9] != '_')\
            or (board[3] == board[5] == board[7] != '_')\
            or (board[1] == board[2] == board[3] != '_')\
            or (board[4] == board[5] == board[6] != '_')\
            or (board[7] == board[8] == board[9] != '_'):
        os.system('cls')
        print('{} won the game!'.format(char))
        play_again()
    elif '_' not in board.values():
        os.system('cls')
        print('Game tied.')
        play_again()


create_board()
game = True

while game:
    os.system('cls')
    show_board()
    if game:
        move('x')
    if game:
        move('o')
