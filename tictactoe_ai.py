import random

def print_board(board):
    # Print reference board
    print("\nReference board for moves:")
    ref_board = [[str(i*3 + j + 1) for j in range(3)] for i in range(3)]
    for row in ref_board:
        print(" | ".join(row))
        print("-" * 9)
    
    # Print game board
    print("Current game board:")
    for row in board:
        print(" | ".join(cell if cell != " " else "." for cell in row))
        print("-" * 9)

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    if is_winner(board, "X"):
        return -1
    if is_winner(board, "O"):
        return 1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -float("inf")
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def play_game():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
        print("Enter a number (1-9) to place your X, using the reference board.")
        
        while True:
            # Human move
            print_board(board)
            try:
                move = int(input("Your move (1-9): ")) - 1
                if 0 <= move <= 8:
                    row, col = divmod(move, 3)
                    if board[row][col] == " ":
                        board[row][col] = "X"
                    else:
                        print("Invalid move! That position is already taken.")
                        continue
                else:
                    print("Invalid move! Enter a number between 1 and 9.")
                    continue
            except ValueError:
                print("Invalid input! Enter a number between 1 and 9.")
                continue

            if is_winner(board, "X"):
                print_board(board)
                print("You win!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            # AI move
            move = ai_move(board)
            if move:
                board[move[0]][move[1]] = "O"
                print("AI's move:")
            if is_winner(board, "O"):
                print_board(board)
                print("AI wins!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

        # Ask to play again
        while True:
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again in ['y', 'n']:
                break
            print("Please enter 'y' for yes or 'n' for no.")
        if play_again == 'n':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()