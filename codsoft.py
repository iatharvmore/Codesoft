import random

# Define the board
board = [' ' for _ in range(9)]

# Define the winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

# Function to print the board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the board is full
def isboardfull(board):
    return ' ' not in board

# Function to check if a player has won
def check_winner(board, player):
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to get a list of available moves
def availablemoves(board):
    return [i for i in range(9) if board[i] == ' ']

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return -1
    elif check_winner(board, 'X'):
        return 1
    elif isboardfull(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for move in availablemoves(board):
            board[move] = 'X'
            eval = minimax(board, depth+1, False)
            board[move] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in availablemoves(board):
            board[move] = 'O'
            eval = minimax(board, depth+1, True)
            board[move] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move using minimax
def bestmove(board):
    best_move = -1
    best_eval = float('-inf')
    for move in availablemoves(board):
        board[move] = 'X'
        move_eval = minimax(board, 0, False)
        board[move] = ' '
        if move_eval > best_eval:
            best_eval = move_eval
            bestmove = move
    return best_move

print("Welcom to the TIC-TAC-TOE")
print("-------------------------")
# Main game loop
while True:
    print_board(board)
    if isboardfull(board):
        print("It's a draw!")
        break

    player_move = int(input("Enter your move (1-9): ")) - 1
    if board[player_move] != ' ' or player_move < 0 or player_move > 8:
        print("Invalid move! Try again.")
        continue

    board[player_move] = 'O'
    
    if check_winner(board, 'O'):
        print_board(board)
        print("You win!")
        break

    if isboardfull(board):
        print_board(board)
        print("It's a draw!")
        break

    computer_move = bestmove(board)
    board[computer_move] = 'X'

    if check_winner(board, 'X'):
        print_board(board)
        print("Computer wins!")
        break
