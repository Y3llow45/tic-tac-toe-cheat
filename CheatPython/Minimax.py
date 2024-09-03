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

