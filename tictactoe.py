"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for column in row:
            if column == 'X':
                x_count += 1
            elif column == 'O':
                o_count += 1
    if x_count + o_count == 9: return None
    elif x_count <= o_count: return 'X'
    else: return 'O'
            

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_moves = set()
    for x, row in enumerate(board):
        for y, column in enumerate(row):
            if column is None:
                available_moves.add((x, y))
    return available_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    copy_board = copy.deepcopy(board)
    if (not 0 <= i <= 2) or (not 0 <= j <= 2) or copy_board[i][j] is not None:
        raise Exception('Invalid Command')
    
    copy_board[i][j] = player(copy_board)
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board:
        if i[0] !=  None:
            if i[0] == i[1] == i[2]:
                return i[0]
    for i in range(3):
        if board[0][i] != None:
            if board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != None:
        return board[0][0]
    if board[0][2] == board[1][1] and board[2][0] == board[1][1]and board[0][2] != None:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None: return True
    else:
        for i in board:
            for j in i:
                if j is None: return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) and winner(board) == 'X': return 1
    elif terminal(board) and winner(board) == 'O': return -1
    else: return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == initial_state: return (1, 1)
    if terminal(board): return None

    if player(board) == 'X':
        best_move = None
        current_max = -math.inf
        for moves in actions(board):
            temp = copy.deepcopy(board)
            max_val = min_value(result(temp, moves))
            if max_val > current_max: 
                current_max = max_val
                best_move = moves
        return best_move
    
    if player(board) == 'O':
        best_move = None
        current_min = math.inf
        for moves in actions(board):
            temp = copy.deepcopy(board)
            min_val = max_value(result(temp, moves))
            if min_val < current_min: 
                current_min = min_val
                best_move = moves
        return best_move
        


def min_value(board):
    min_val = math.inf
    if terminal(board) is True:
        return utility(board)
    for moves in actions(board):
        min_val = min(min_val, max_value(result(board, moves)))

    return min_val

def max_value(board):
    max_val = -math.inf
    if terminal(board) is True:
        return utility(board)
    for moves in actions(board):
        max_val = max(max_val, min_value(result(board, moves)))

    return max_val