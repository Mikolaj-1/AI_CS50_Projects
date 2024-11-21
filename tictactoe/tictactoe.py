"""
Tic Tac Toe Player
"""

import math
from random import choice
from copy import deepcopy

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    if x_count > o_count:
        return O
    else:
        return X

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions=set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions



    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board=deepcopy(board)
    new_board[action[0]][action[1]]=player(board)
    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] != None and board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        return board[0][0]
    if board[1][0] != None and board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        return board[1][0]
    if board[2][0] != None and board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        return board[2][0]
    
    if board[0][0] != None and board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] != None and board[0][1] == board [1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] != None and board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    
    if board[0][0] != None and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != None and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    
    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for row in board:
        for cell in row:
            if cell==None:
                return False
        
    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)=="X":
        return 1
    
    if winner(board)=="O":
        return -1
    
    return 0
    
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board)==X:
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            move_value = min_value(new_board)
            if move_value > best_value:
                best_value = move_value
                best_action = action
        return best_action
    else:
        best_value= math.inf
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            move_value= max_value(new_board)
            if move_value < best_value:
                best_value = move_value
                best_action = action
        return best_action

def max_value(board):
    """
    Returns the maximum utility value for player X.
    """
    if terminal(board):
        return utility(board)

    value = -math.inf
    for action in actions(board):
        new_board = result(board, action)
        value = max(value, min_value(new_board))
    return value

def min_value(board):
    """
    Returns the minimum utility value for player O
    """
    if terminal(board):
        return utility(board)

    value = math.inf
    for action in actions(board):
        new_board = result(board, action)
        value = min(value, max_value(new_board))
    return value