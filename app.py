# Input determines the symbol for player
player1 = input("Please pick a marker 'X' or 'O' :")

#Determines turn order
position = int(input('Please enter a number: '))

def display_board(board):
    print("\n"*100)

    print('___|___|___')
    print(' {} | {} | {} '.format(board[7],board[8],board[9]))
    print('___|___|___')
    print(' {} | {} | {} '.format(board[4],board[5],board[6]))
    print('___|___|___')
    print(' {} | {} | {} '.format(board[1],board[2],board[3]))

def winner(board):
    if board[1] == board[2] == board[3] or board[4] == board[5] == board[6] or board[7] == board[8] == board[9]:
        print('win')
    elif board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[3] == board[6] == board[9]:
        print('win')
    elif board[3] == board[5] == board[7] or board[1] == board[5] == board[9]:
        print('win')
    else:
        print('no one won, you suck')
    
    


