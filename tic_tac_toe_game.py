def display_board(board):
    """
    display the board
    """
    print('\n'*10)
    print('    |   |')
    print('  '  + board[7] +' | '   + board[8]+' | '   + board[9])
    print('    |   |')
    print(' -----------')
    print('    |   |')
    print('  '  + board[4] +' | '   + board[5]+' | '   + board[6])
    print('    |   |')
    print(' -----------')
    print('    |   |')
    print('  '  + board[1] +' | '   + board[2]+' | '   + board[3])
    print('    |   |')



def player_input():                        #asking for player input
    playerinput=''
    while playerinput not in ['X','O']:
        playerinput=input("Player 1:Please pick a marker 'X' or 'O' \n").upper()
    if playerinput=='X':
        return ('X','O')
    return ('O','X')



def place_marker(board, marker, position):#placing the marker at the position prvided by the player
        board[position]=marker



def win_check(board, mark):  #checking for the win
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))




import random

def choose_first():
    toss=random.randint(1,2)
    if (toss==1):
        return 'Player1'
    return 'Player2'

def space_check(board, position):#checking whether the position entered by the player is available or not
    return board[position]==' '


def full_board_check(board):  #checking for full board situation
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(turn,board):   #asking continuously for player input
    position = 0
    while position not in range(1,10):
        print(f"{turn} turn")
        position = int(input('Please enter a number between 1-9 \n'))
        if space_check(board, position):
            return position




def replay():
    return input('do you want to play again : Yes or No? \n').lower().startswith('y')



#MAIN BODY OF THE CODE

print('Welcome to Tic Tac Toe!')
while True:
    board=[' ']*10
    P1,P2=player_input()
    turn=choose_first()
    if turn == 'Player1':
        print(turn + ' will go first and your marker is '+P1 +'\n')
    else:
        print(turn + ' will go first and your marker is '+P2 + '\n')

    play_game=input('Do you want to play the game? yes or no \n')
    if play_game[0].lower()=='y':
        game_on=True
    else:
        game_on=False




    while game_on:   #game on logic here
        if turn=='Player1':
            display_board(board)
            position=player_choice(turn,board)   #returns position where marker will be placed
            place_marker(board, P1, position)  #places the marker for the appr0priate user

            if win_check(board,P1):   #checking for win
                display_board(board)
                print('\ncongratulation'+turn+'you have won the game')
                game_on=False
            else:
                if full_board_check(board):   #if draw
                    display_board(board)
                    print('\nthe game is a draw')
                    break

                else:
                    turn='Player2'    #else player 2s turn



        else:
            display_board(board)
            position=player_choice(turn,board)
            place_marker(board, P2, position)

            if win_check(board,P2):
                display_board(board)
                print('\ncongratulation'+turn+'you have won the game')
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('\nthe game is a draw')
                    break

                else:
                    turn='Player1'

    if not replay():
        break
