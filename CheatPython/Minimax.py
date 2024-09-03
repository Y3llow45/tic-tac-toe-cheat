import math

X = 'X'
O = 'O'
EMPTY = ' '

def check_winner(board):
  for row in board:
    if row[0] == row[1] == row[2] != EMPTY:
      return row[0]

  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] != EMPTY:
      return board[0][col]

  if board[0][0] == board[1][1] == board[2][2] != EMPTY:
      return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] != EMPTY:
      return board[0][2]
  
  return None

def is_full(board):
  return all(cell != EMPTY for row in board for cell in row)

def minimax(board, depth, is_maximizing):
  winner = check_winner(board)
  if winner == X:
    return 10 - depth
  if winner == O:
    return depth - 10
  if is_full(board):
    return 0

  if is_maximizing:
    best_score = -math.inf
    for i in range(3):
      for j in range(3):
        if board[i][j] == EMPTY:
          board[i][j] = X
          score = minimax(board, depth + 1, False)
          board[i][j] = EMPTY
          best_score = max(score, best_score)
    return best_score
  else:
    best_score = math.inf
    for i in range(3):
      for j in range(3):
        if board[i][j] == EMPTY:
          board[i][j] = O
          score = minimax(board, depth + 1, True)
          board[i][j] = EMPTY
          best_score = min(score, best_score)
    return best_score

