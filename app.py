import random

theBoard = [' ']
available = [str(num) for num in range(0, 10)]
players = [0, 'X', 'O']



def display_board(a,b):
    print(f'Available   TIC-TAC-TOE\n  moves\n\n  {a[7]}|{a[8]}|{a[9]}        {b[7]}|{b[8]}|{b[9]}\n  -----        -----\n  {a[4]}|{a[5]}|{a[6]}        {b[4]}|{b[5]}|{b[6]}\n  -----        -----\n  {a[1]}|{a[2]}|{a[3]}        {b[1]}|{b[2]}|{b[3]}\n')


display_board(available,theBoard)

def place_marker(avail,board,marker,position):
    board[position] = marker
    avail[position] = ' '


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def random_player():
    return random.choice((-1, 1))
    
def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board[1:]

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def player_choice(board,player):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
            position = int(input('Player %s, choose your next position: (1-9) '%(player)))
        except:
            print("I'm sorry, please try again.")
        
    return position

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
    
print('Welcome to Tyc Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            # Player One's turn

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else: 
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

# def winner(board):
#     if board[1] == board[2] == board[3] or board[4] == board[5] == board[6] or board[7] == board[8] == board[9]:
#         print('win')
#     elif board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[3] == board[6] == board[9]:
#         print('win')
#     elif board[3] == board[5] == board[7] or board[1] == board[5] == board[9]:
#         print('win')
#     else:
#         print('no one won, you suck')
    



