
"""
HW 2
Problem 4
Author : Kalla Naga Suresh

"""
# Define a function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))  # Print each row with separator "|"
        print("-" * 9)  # Print a horizontal line to separate rows

# Define a function to check if a player has won
def checkforplayerwin(board, player):
    # Check rows and columns for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Define a function to check if the game is a draw
def drawed(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# Define the main game function
if __name__ == "__main__":
    # Initialize an empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"  # Start with player X
    game_over = False  # Flag to track if the game is over


    while not game_over:
        print_board(board)  # Display the current state of the board
        row = int(input(f"Enter a row (0, 1, or 2) for player {player}: "))  # Player input for row
        col = int(input(f"Enter a column (0, 1, or 2) for player {player}: "))  # Player input for column

        # Check if the move is valid
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        # Update the board with the player's move
        board[row][col] = player

        # Check if the current player has won
        if checkforplayerwin(board, player):
            print_board(board)
            print(f"{player} player won")
            game_over = True
        # Check if the game is a draw
        elif drawed(board):
            print_board(board)
            print("It's a draw! The game is over.")
            game_over = True
        else:
            # Switch to the other player's turn
            player = "O" if player == "X" else "X"