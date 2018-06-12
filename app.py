# Input determines the order of the game as well as the symbol for player
player1 = input("Please pick a marker 'X' or 'O' :")

def turnOrder(playerchoice):
    if(playerchoice) == 'x' or(playerchoice) == 'X':
        print("Player one has chosen X, please go first")
        player2 = "O"
    elif(playerchoice) =='o' or(playerchoice) == 'O':
        print("Player one has chosen O, please go second")
        player2 = "X"

turnOrder(player1)

print(player1)
print(player2)

