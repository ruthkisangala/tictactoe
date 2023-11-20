def player_move(player):
    while True:
        input_player = int(input(f"{player}, please chose a number from 1 to 20 where to set your x!\n{player} = ")) - 1
        if input_player in range(0,20):
            return input_player
        else: 
            print(f"{player}, enter a valid number!")

def move(position, mark, player):
    if game_board[position] == "-":
        game_board[position] = mark
    else: 
        print(f"{player}, chose a free space.")

def robot_move():
    while True:
        from random import randrange
        input_robot = randrange(0,20)
        print("Robot = " + str(input_robot + 1))
        if game_board[input_robot] == "-":
            game_board[input_robot] = "o"
            return
        else:
            print("Same number. Try again, Robot.")

def terminator_move(position):
    for i in range (18):
        # for o-o situation
        if game_board[i] == game_board[i+2] == "o":
            if game_board[i+1] == "-":
                game_board[i+1] = "o"
                return True
        # for oo- situation
        elif game_board[i] == game_board[i+1] == "o":
            if game_board[i+2] == "-":
                game_board[i+2] = "o"
                return True 
    # for -oo situation
    for i in range (2,19):
        if game_board[i] == game_board[i+1] == "o":
            if game_board[i-1] == "-":
                game_board[i+2] = "o"
                return True
            
    if position <= 18:
        position_robot = position + 1
        if game_board[position_robot] == "-":
            print("Robot =",position_robot + 1)
            game_board[position_robot] = "o"
            return True
    
    for i in range(1, position + 1):
        position_robot = position - i 
        print("Robot = ",position_robot + 1)
        if game_board[position_robot] == "-":
            game_board[position_robot] = "o"
            return True

def evaluate(player, mark):
    for i in range(18):
        if game_board[i] == game_board[i + 1] == game_board[i + 2] == mark: 
            print("\n" + "".join(game_board))
            print(player + " won! Congratulations!\n")
            return False
    if "-" not in game_board:
        print("\n" + "".join(game_board))
        print ("It's a tie!")
        return False
    print("".join(game_board) + "\n")

# Checking how many players and names
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

#Greeting
print("\nWelcome to Ruth's TicTacToe game, " + str(player_1) + " and " + str(player_2) + ".\n")

print("\n" + player_1 + " is x.\n" + player_2 + " is o.\n")

game_board = list(20 * "-")
print("".join(game_board) + "\n")

#Actual game
while True:
    # move player 1
    position = player_move(player_1)
    move(position, "x", player_1)
    if evaluate(player_1, "x") == False:
        break

    # move player 2
    elif players_amount == 2:
        position = player_move(player_2)
        move(position, "o", player_2)
        if evaluate(player_2, "o") == False:
            break

    # move computer if no player 2
    elif players_amount == 1:
        #robot_move()
        terminator_move(position)
        if evaluate(player_2, "o") == False:
            break
