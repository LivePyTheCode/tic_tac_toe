import random
# ------------- TIC TAC TOE --------- #
# ---- BUILD BOARD
# ---- SET GAME LOGIC
# ---- MAKE IT 2 PLAYER OR VS COMPUTER
# ---- WINNING COMBINATIONS
# ----  RESTARTING THE GAME

computer_options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_game_board():
    print('-------------')
    print(f'| {game_board[0][0]} | {game_board[0][1]} | {game_board[0][2]} |')
    print('-------------')
    print(f'| {game_board[1][0]} | {game_board[1][1]} | {game_board[1][2]} |')
    print('-------------')
    print(f'| {game_board[2][0]} | {game_board[2][1]} | {game_board[2][2]} |')
    print('-------------')


def player_move(player_selection, move):
    row = (move - 1) // 3
    col = (move - 1) % 3
    if game_board[row][col] == " ":
        game_board[row][col] = player_selection
        return True
    else:
        print("Invalid move! That cell is already taken.")
        return False

def computer_move():
    available_moves = [i for i in range(1, 10) if game_board[(i - 1) // 3][(i - 1) % 3] == " "]
    if available_moves:
        return random.choice(available_moves)
    else:
        return None

def check_winner(player_selection):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(game_board[i][j] == player_selection for j in range(3)):  # Rows
            return True
        if all(game_board[j][i] == player_selection for j in range(3)):  # Columns
            return True
    if all(game_board[i][i] == player_selection for i in range(3)):  # Main diagonal
        return True
    if all(game_board[i][2 - i] == player_selection for i in range(3)):  # Anti-diagonal
        return True
    return False


def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    player_selection = input("Do you want to be X or O? ").upper()
    print_game_board()

    while True:
        # Player's move
        while True:
            move = int(input("Enter your move (1-9): "))
            if player_move(player_selection, move):
                break
            else:
                continue

        print_game_board()

        # Check if the player has won
        if check_winner(player_selection):
            print("Congratulations! You win!")
            break

        # Computer's move
        computer_selection = "X" if player_selection == "O" else "O"
        move = computer_move()
        if move:
            print(f"Computer moves to {move}.")
            player_move(computer_selection, move)
        else:
            print("It's a draw!")
            break

        print_game_board()

        # Check if the computer has won
        if check_winner(computer_selection):
            print("Sorry, you lose!")
            break


tic_tac_toe()
