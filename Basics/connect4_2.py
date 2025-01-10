def print_board():
    # Print the game board
    for row in reversed(range(6)):
        for col in range(7):
            print(column[col][row], end="")
        print()

def check_connect_four(symbol):
    # Check for Connect Four lines in rows, columns, and diagonals
    for col in range(4):
        for row in range(6):
            if all(column[col + i][row] == symbol for i in range(4)):  # Horizontal
                return True
        for row in range(3):
            if all(column[col][row + i] == symbol for i in range(4)):  # Vertical
                return True
            if all(column[col + i][row + i] == symbol for i in range(4)):  # Main Diagonal
                return True
            if all(column[col + i][row - i + 3] == symbol for i in range(4)):  # Off-Diagonal
                return True
    return False

def main():
    global column
    
    print("Player 1 counter will be X and Player 2 counter will be 0\n")
    
    # Initialize the game board
    column = [[" # "] * 6 for _ in range(7)]

    print_board()

    players = ["X", "0"]
    current_player = 0

    while True:
        player_symbol = players[current_player]
        player_name = f"Player {current_player + 1}"

        while True:
            try:
                col_choice = int(input(f"\n{player_name}, choose a column (1-7): ")) - 1
                if 0 <= col_choice < 7 and column[col_choice][0] == " # ":
                    break
                else:
                    print("Invalid column choice. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

        # Place the counter in the chosen column
        for row in reversed(range(6)):
            if column[col_choice][row] == " # ":
                column[col_choice][row] = f" {player_symbol} "
                break
        
        print_board()

        # Check for a win
        if check_connect_four(f" {player_symbol} "):
            print(f"\n{player_name} wins!")
            break
        
        # Check for a draw
        if all(cell != " # " for col in column for cell in col):
            print("\nIt's a draw!")
            break
        
        # Switch to the other player
        current_player = 1 - current_player

if __name__ == "__main__":
    main()
