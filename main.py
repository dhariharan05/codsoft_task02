#TIC-TAC-TOE AI
import math
PLAYER_X = 'X'
PLAYER_O = 'O'
def scan_winner(board):
    # Row Condition Check
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0]

    # Column Condition Check
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Diagonal Condition Check
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # Draw Condition Check
    if is_board_full(board):
        return 'Draw'

    return None

def assess_position(board):
    winner = scan_winner(board)

    if winner == PLAYER_X:
        return -1  # Score for 'X' win
    elif winner == PLAYER_O:
        return 1  # Score for 'O' win
    elif winner == 'Draw':
        return 0  # Score for a draw
    else:
        return None

def display_board(board):
    print("    0   1   2  ")
    print("  -------------")
    count = 0
    for row in board:
        print(count,"'", row[0], "'", row[1], "'", row[2], "'")
        print("  -------------")
        count=count+1
    print()



def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

#Minimax with alpha beta pruning algorithm
def minimax(board, depth, isMaximizingPlayer, alpha, beta):

    score = assess_position(board)

    if score is not None:
        return score

    if isMaximizingPlayer:
        maxScore = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    maxScore = max(maxScore, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = ' '
                    alpha = max(alpha, maxScore)
                    if beta <= alpha:
                        break
        return maxScore
    else:
        minScore = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    minScore = min(minScore, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = ' '
                    beta = min(beta, minScore)
                    if beta <= alpha:
                        break
        return minScore

def get_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def main():
    flag = False
    count = 0
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True  # True for 'X', False for 'O'

    while True:

        if flag == False:
            print("Displaying board(Human Player turn ...)")
        else:
            print("Displaying board(AI Player turn..)")
        display_board(board)
        if player_turn:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            flag = False
        else:
            flag = True
            row, col = get_best_move(board)

        if board[row][col] == ' ':
            board[row][col] = 'X' if player_turn else 'O'
            player_turn = not player_turn

        if assess_position(board) is not None:
            print("AI Player turn..")
            display_board(board)
            if(assess_position(board)) == 1:
                print("AI Wins!")
            elif(assess_position(board)) == -1:
                print("Human Wins!")
            else:
                print("Draw!")
            print("Game Over")
            break

        if is_board_full(board):
            print("AI Player turn..")
            display_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
