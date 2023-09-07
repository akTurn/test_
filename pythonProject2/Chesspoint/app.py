import json
def get_position(row, col):
  position = chr(ord('a') + col) + str(row + 1)
  return position
def get_alphanumeric_positions(valid_moves):
  alphanumeric_positions = []

  for row, col in valid_moves:
    alphanumeric_positions.append(get_position(row, col))

  return alphanumeric_positions


def get_valid_moves(piece_name, position):

  if piece_name == "Queen":
   valid_moves = get_queen_moves(position)
  elif piece_name == "Rook":
   valid_moves = get_rook_moves(position)
  elif piece_name == "Bishop":
   valid_moves = get_bishop_moves(position)
  elif piece_name == "Knight":
   valid_moves = get_knight_moves(position)
   #valid_moves = get_valid_knight_moves(position)
  else:
   valid_moves = []

  return valid_moves
"""
def get_bishop_moves(position):
  row, col = position
  valid_moves = []
  # Check for moves diagonally up and to the right.
  for i in range(1, 8):
    new_row = row + i
    new_col = col + i
    if new_row >= 0 and new_row < 8 and new_col >= 0 and new_col < 8:
      valid_moves.append((new_row, new_col))

    if new_row == 8 or new_col == 8:
      break

  # Check for moves diagonally up and to the left.

  for i in range(1, 8):
    new_row = row + i
    new_col = col - i
    if new_row >= 0 and new_row < 8 and new_col >= 0 and new_col < 8:
      valid_moves.append((new_row, new_col))

    if new_row == 8 or new_col == -1:
      break

  # Check for moves diagonally down and to the right.

  for i in range(1, 8):
    new_row = row - i
    new_col = col + i
    if new_row >= 0 and new_row < 8 and new_col >= 0 and new_col < 8:
      valid_moves.append((new_row, new_col))

    if new_row == -1 or new_col == 8:
      break

  # Check for moves diagonally down and to the left.

  for i in range(1, 8):
    new_row = row - i
    new_col = col - i
    if new_row >= 0 and new_row < 8 and new_col >= 0 and new_col < 8:
      valid_moves.append((new_row, new_col))

    if new_row == -1 or new_col == -1:
      break
  valid_moves=get_position(valid_moves)
  return valid_moves

def get_queen_moves(position):
  row, col = position
  valid_moves = []
  # Check for moves any number of squares horizontally, vertically, or diagonally.

  for i in range(-8, 9):
    for j in range(-8, 9):
      if i == 0 and j == 0:
        continue
      new_row = row + i
      new_col = col + j
      if new_row >= 0 and new_row < 8 and new_col >= 0 and new_col < 8:
        valid_moves.append((new_row, new_col))

  return valid_moves

def get_rook_moves(position):
  print("position",position)

  row, col = position
  valid_moves = []

  # Check for moves any number of squares horizontally or vertically.

  for i in range(-8, 9):
    if i == 0:
      continue
    new_row = row + i
    new_col = col
    while new_row >= 0 and new_row < 8:
      valid_moves.append((new_row, new_col))
      new_row += i

  for i in range(-8, 9):
    if i == 0:
      continue
    new_row = row
    new_col = col + i
    while new_col >= 0 and new_col < 8:
      valid_moves.append((new_row, new_col))
      new_col += i

  return valid_moves """

def get_knight_moves(position):
  row, col = position
  valid_moves = []
  # Check for moves two squares up and one square to the left or right.
  for i in [-2, 2]:
    for j in [-1, 1]:
      new_row = row + i
      new_col = col + j
      if new_row >= 0 and new_row < 8 and new_col >= 0 and new_col < 8:
        valid_moves.append((new_row, new_col))

  # Check for moves two squares to the left or right and one square up or down.
  for i in [-1, 1]:
    for j in [-2, 2]:
      new_row = row + i
      new_col = col + j
      if new_row >= 0 and new_row < 8 and new_col >= 0 and new_col < 8:
        valid_moves.append((new_row, new_col))

  return valid_moves

def get_valid_knight_moves(position):
  x, y = position
  possible_moves = []

  moves = [
    (x + 2, y + 1), (x + 2, y - 1),
    (x - 2, y + 1), (x - 2, y - 1),
    (x + 1, y + 2), (x + 1, y - 2),
    (x - 1, y + 2), (x - 1, y - 2)
  ]

  for move in moves:
    if 1 <= move[0] <= 8 and 1 <= move[1] <= 8:
      possible_moves.append(move)

  return possible_moves


def main():
  """
  Main function.

  Reads the input JSON and prints the valid moves for the knight.


  input_json = {
    "Positions": {
      "Queen": "E7",
      "Bishop":"B7",
      "Rook": G5"",
      "Knight": "C3"}}

  piece_name = "Knight"
  position = "C3"
"""
  Chess_piece = {}
  max_length = 1

  while len(Chess_piece) < max_length:
    piece_name = input("Enter Piece name (Rook, Queen, Bishop, or Knight): ")
    if piece_name not in Chess_piece and piece_name in ['Rook', 'Queen', 'Bishop', 'Knight']:
      position = input("Enter Position in Alphanumeric eg( A4,H6): ")
      Chess_piece[piece_name] = position
    else:
      print("Invalid piece name. Please enter one of Rook, Queen, Bishop, or Knight")
      pass

  def convert_to_coordinates(alpn_position):
    letter = alpn_position[0]
    x = ord(letter) - ord('A') + 1
    y = int(alpn_position[1])
    return x,y

  for piece_name in Chess_piece:
    position=convert_to_coordinates(position)
    print("Main",position,piece_name)
    valid_moves = get_valid_moves(piece_name, position)
    print(json.dumps({"valid_moves": get_alphanumeric_positions(valid_moves)}))


if __name__ == "__main__":
  main()
