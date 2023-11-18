while True:
    players_amount = int(input("How many players? Enter 1 or 2. "))
    if players_amount in [1,2]:
        player_1 = input("Please enter the name for player 1. ").title()
        if players_amount == 1:
            player_2 = "Robot"
            break
        elif players_amount == 2:
            player_2 = input("Please enter the name for player 2. ").title()
        break
    else:
        print("Invalid number.")

def player_1_move():
    while True:
        input_player_1 = int(input("Please chose a number from 1 to 20 where to set your x! ")) - 1
        print(input_player_1)
        if input_player_1 in range(0,20):
            if game_board[input_player_1] == "-":
                game_board[input_player_1] = "x"
                return
            else: 
                print("Chose a free space.")
        else: 
            print("Enter a valid number!")

def evaluate():
    for i in range(18):
        if game_board[i] == game_board[i + 1] == game_board[i + 2] == "x": 
            print(game_board)
            print(player_1 + " won! Congratulations!")
            return False
        elif game_board[i] == game_board[i + 1] == game_board[i + 2] == "o": 
            print(game_board)
            print(player_2 + " won! Congratulations!")
            return False
    if "-" not in game_board:
        print(game_board)
        print ("It's a tie!")
        return False
    else: 
        print("Continue.")
        return True

print("Welcome to Ruth's TicTacToe game.\n")

print("\n" + player_1 + " is x.\n" + player_2 + " is o.\n")

game_board = list(20 * "-")

while True:
    print(game_board)
    player_1_move()
    if evaluate() == False:
        break



    


