import math

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def is_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    return [player, player, player] in win_conditions

def minimax(board, depth, alpha, beta, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    elif is_winner(board, 'X'):
        return -1
    elif ' ' not in board:
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in available_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in available_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    best_score = -math.inf
    move = None
    for m in available_moves(board):
        board[m] = 'O'
        score = minimax(board, 0, -math.inf, math.inf, False)
        board[m] = ' '
        if score > best_score:
            best_score = score
            move = m
    return move

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    print_board(board)

    while ' ' in board and not is_winner(board, 'X') and not is_winner(board, 'O'):
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] == ' ':
            board[human_move] = 'X'
            if ' ' not in board or is_winner(board, 'X'):
                break
            ai_move = best_move(board)
            board[ai_move] = 'O' # type: ignore
            print_board(board)
        else:
            print("Invalid move. Try again.")

    if is_winner(board, 'X'):
        print("Congratulations! You win!")
    elif is_winner(board, 'O'):
        print("You lose. AI wins!")
    else:
        print("It's a tie!")



if __name__ == "__main__":
    tic_tac_toe()
