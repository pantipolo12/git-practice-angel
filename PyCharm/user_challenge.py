def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    for row_index in range(3):
        if (all(board[row_index][col_index] == player for col_index in range(3)) or
            all(board[col_index][row_index] == player for col_index in range(3))):
            return True
    if (all(board[diagonal_index][diagonal_index] == player for diagonal_index in range(3)) or
        all(board[diagonal_index][2 - diagonal_index] == player for diagonal_index in range(3))):
        return True
    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def start_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = ["X", "O"]
    print("Tic-Tac-Toe Game")
    player(board)

    for turn_number in range(9):
        current_player = player[turn_number % 2]
        while 1:
            try:
                row, col = map(int, input(f"P {current_player}, row col (0-2): ").split())
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("spot already taken, try again.")
            except ValueError:
                print("Invalid input. Please enter two integers seperated by a space.")

        player(board)
        if check_winner(board, current_player):
            print(f"P {current_player} wins!")
            return
        if is_board_full(board):
            print("Draw!")
            return
    print("Draw!")


start_game()