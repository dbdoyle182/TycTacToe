# Input determines the order of the game as well as the symbol for player
player1 = input("Please pick a marker 'X' or 'O' :")
player2 = ""

def turnOrder(playerchoice):
    if(playerchoice) == 'x' or(playerchoice) == 'X':
        print("Player one has chosen X, please go first")
        player2 = "O"
    elif(playerchoice) =='o' or(playerchoice) == 'O':
        print("Player one has chosen O, please go second")
        player2 = "X"
    else:
        

print(player1)
print(player2)

