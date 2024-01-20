from random import randrange

def evaluate(board, mark):
    print(board)
    for i in range(0,20):
        #if board[i] == board[i +1] == board[i +2] == mark:
        if 3*mark in board:
            return mark
        elif "-" not in board:
            return "!"
        else:
            return "-"


def move(board, mark, position: int):
    if position == 0 or position > 20:
        return False
    else:
        updated_board = board[:position - 1] + mark + board[position:]
        return updated_board

def player_move(board):
    while True:
        player_position = int(input("Which position do you want to play? Write a number from 1 to 20. "))
        if player_position in range(1,21):
            if board[player_position -1] == "-":
                updated_board = board[:player_position - 1] + "x" + board[player_position:]
                return updated_board
            else:
                print("Space already taken.")
                continue
        else:
            print("Number incorrect.")
            continue

'''def pc_move(board, mark):
    while True:
        pc_position = randrange(0,20)
        if board[pc_position] == "-":
                print("Pc_move is " + str(pc_position + 1) + ".")
                updated_board = board[:pc_position] + mark + board[pc_position + 1:]
                return updated_board
        else:
            print("Pc tried " + str(pc_position + 1) + ".")
            continue'''

def pc_move(board):
    while True:
        pc_position = randrange(1,21)
        if board[pc_position - 1] == "-":
                #print("Pc_move is " + str(pc_position) + ".")
                updated_board = board[:pc_position - 1] + "o" + board[pc_position:]
                return updated_board
        else:
            #print("Pc tried " + str(pc_position) + ".")
            continue

def tictactoe_1d():
    board = 20*"-"
    print(board)
    while True:
        board = player_move(board)
        result = evaluate(board, "x")
        if result != "-":
            print("Game over! - " + str(result))
            break
        board = pc_move(board)
        result = evaluate(board, "o")
        if result != "-":
            print("Game over! - " + str(result))
            break


board = move("-"*20, "x", 0)
print(board)