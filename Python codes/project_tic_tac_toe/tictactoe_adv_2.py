def display_board(board):
    print(board[1] + '|' + board[2] + '|'+ board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|'+ board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|'+ board[9])

def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input("player1 choose x or o: ").upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,position,marker):
    board[position]=marker

def win_check(board,marker):
    return ((board[1]==board[2]==board[3]==marker) or
    (board[4]==board[5]==board[6]==marker) or
    (board[7]==board[8]==board[9]==marker) or
    (board[1]==board[4]==board[7]==marker) or
    (board[2]==board[5]==board[8]==marker) or
    (board[3]==board[6]==board[9]==marker) or
    (board[1]==board[5]==board[9]==marker) or 
    (board[3]==board[5]==board[7]==marker))


import random
def first_choose():
    flip=random.randint(0,1)
    if flip==1:
        return 'player1'
    else:
        return 'player2'

def space_check():
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False

def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input('choose position in (1-9): '))
    return position
    

def replay():
    choice=input("do you wanna play again, yes or no: ")
    return choice=='yes'

print("Welcome to play TIC TAC TOE")
print(":- by AYUSH GUPTA")
while True:
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=first_choose()
    print(turn + "will choose first")
    play_game=input("ready to play? choose y or n: ")
    if play_game=='y':
        game_on=True
    else:
        game_on= False

    while game_on:
        if turn=='player 1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player1 has won!!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("tie game")
                    game_on=False
                else:
                    turn="player 2"
        else:
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player2 has won!!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("tie game")
                    game_on=False
                else:
                    turn="player 1"



    if not replay():
        break




