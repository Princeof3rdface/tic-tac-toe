import math

# Define players
HUMAN = 'O'
AI = 'X'
EMPTY = ' '

def print_board(board):
    """Renders the game board cleanly in the terminal."""
    print("\n")
    for i, row in enumerate(board):
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def check_winner(board):
    """Checks if there's a winner or a tie."""
    # Rows and Columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
            
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
        
    # Check for Tie / Available spaces
    for row in board:
        if EMPTY in row:
            return None # Game still ongoing
            
    return 'Tie'

def minimax(board, depth, is_maximizing):
    """The Minimax algorithm recursive engine."""
    score = check_winner(board)
    
    # Base cases: Return terminal score if game over
    if score == AI:
        return 10 - depth
    if score == HUMAN:
        return depth - 10
    if score == 'Tie':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == EMPTY:
                    board[r][c] = AI
                    score_eval = minimax(board, depth + 1, False)
                    board[r][c] = EMPTY # Undo move
                    best_score = max(score_eval, best_score)
        return best_score
    else:
        best_score = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == EMPTY:
                    board[r][c] = HUMAN
                    score_eval = minimax(board, depth + 1, True)
                    board[r][c] = EMPTY # Undo move
                    best_score = min(score_eval, best_score)
        return best_score

def find_best_move(board):
    """Calculates the ultimate move for the AI."""
    best_score = -math.inf
    move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                board[r][c] = AI
                move_score = minimax(board, 0, False)
                board[r][c] = EMPTY
                if move_score > best_score:
                    best_score = move_score
                    move = (r, c)
    return move

def play_game():
    """Main game loop handling turns."""
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to Codmetric AI Tic-Tac-Toe!")
    print("You play as 'O' and the Unbeatable AI is 'X'.")
    print("Positions are chosen using grid coordinates (Row and Column: 0, 1, or 2).")
    
    print_board(board)
    
    while True:
        # --- HUMAN TURN ---
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if board[row][col] == EMPTY:
                    board[row][col] = HUMAN
                    break
                else:
                    print("That spot is already taken!")
            except (ValueError, IndexError):
                print("Invalid input. Please type numbers between 0 and 2.")
                
        print_board(board)
        if check_winner(board):
            break
            
        # --- AI TURN ---
        print("AI is thinking...")
        ai_move = find_best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = AI
            
        print_board(board)
        if check_winner(board):
            break

    # Determine final result
    result = check_winner(board)
    if result == 'Tie':
        print("It's a tie! Well played.")
    elif result == HUMAN:
        print("Wow! You actually beat the AI!")
    else:
        print("The AI wins! Better luck next time.")

if __name__ == "__main__":
    play_game()