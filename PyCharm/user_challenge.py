def print_board(board):
    """
    Displays the current state of the Tic-Tac-Toe board.

    Args:
        board (list of list of str): A 3x3 matrix representing the Tic-Tac-Toe grid.
    """
    for row in board:
        print(" | ".join(row))
        print("---" * 3)


def check_winner(board, player):
    """
    Checks if the given player has won the Tic-Tac-Toe game.

    Args:
        board (list of list of str): A 3x3 matrix representing the Tic-Tac-Toe grid.
        player (str): The current player's symbol ("X" or "O").

    Returns:
        bool: True if the player has a winning combination, False otherwise.
    """
    for row_index in range(3):
        if (all(board[row_index][col_index] == player for col_index in range(3)) or
                all(board[col_index][row_index] == player for col_index in range(3))):
            return True
    if (all(board[diagonal_index][diagonal_index] == player for diagonal_index in range(3)) or
            all(board[diagonal_index][2 - diagonal_index] == player for diagonal_index in range(3))):
        return True
    return False


def is_board_full(board):
    """
    Checks if the Tic-Tac-Toe board is completely filled.

    Args:
        board (list of list of str): A 3x3 matrix representing the Tic-Tac-Toe grid.

    Returns:
        bool: True if all cells on the board are filled, False otherwise.
    """
    return all(cell != " " for row in board for cell in row)


def start_game():
    """
    Starts the Tic-Tac-Toe game, alternates turns between two players (X and O),
    and determines the outcome (win, draw, or ongoing).

    The function manages player inputs, validates moves, calls helper functions
    to check for a winner or a full board, and displays the game state at each step.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_board(board)

    for turn_number in range(9):
        current_player = player[turn_number % 2]
        while 1:
            try:
                row, col = map(int, input(f"Player {current_player}, please enter (row-col) (0-2): ").split())
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("spot already taken, try again.")
            except ValueError:
                print("Invalid input. Please enter two integers seperated by a space.")

        print_board(board)
        if check_winner(board, current_player):
            print(f"P {current_player} wins!")
            return
        if is_board_full(board):
            print("Draw!")
            return
    print("Draw!")


def play_game():
    """
    Entry point for playing the Tic-Tac-Toe game.

    This function initiates the game by calling the start_game() function.
    """
    start_game()


play_game()