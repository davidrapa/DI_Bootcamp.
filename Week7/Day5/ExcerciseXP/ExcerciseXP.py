
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")


def player_input(player):
    while True:
        row = input(f"Player {player}, row (1-3): ")
        col = input(f"PLayer {player}, column (1-3): ")

        if row.isdigit() and col.isdigit():
            row = int(row)
            col = int(col)
            if 1 <= row <= 3 and 1 <= col <= 3:
                position = (row - 1) * 3 + (col - 1)
                return position
        print("Invalid entry, introduce row and column from 1 al 3.")

def check_win(board):
    win_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != "-":
            return board[pattern[0]]
    if "-" not in board:
        return "tie"
    return None

def play():
    board = ["-" for _ in range(9)]
    current_player = "X"
    while True:
        display_board(board)
        position = player_input(current_player)
        board[position] = current_player
        winner = check_win(board)
        if winner:
            display_board(board)
            if winner == "tie":
                print("The game ended in a tie.")
            else:
                print(f"Congratulations! Player {winner} won!")
            break
        current_player = "O" if current_player == "X" else "X"

play()