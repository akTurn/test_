from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)
"""
def get_valid_moves(piece_names, piece_positions,other_positions):

  valid_moves = []
  for piece_name in piece_names:
    valid_moves.extend(get_valid_moves(piece_name, piece_positions,other_positions))

  return valid_moves
"""
def get_valid_moves(piece_name, piece_position, other_positions):

  valid_moves = []

  if piece_name == "Rook":
    valid_moves = get_rook_moves(piece_position, other_positions)
  elif piece_name == "Queen":
    valid_moves = get_queen_moves(piece_position, other_positions)
  elif piece_name == "Bishop":
    valid_moves = get_bishop_moves(piece_position, other_positions)
  elif piece_name == "Knight":
    valid_moves = get_knight_moves(piece_position, other_positions)

  return valid_moves

def get_knight_moves(piece_position, other_positions):

  valid_moves = []

  row, col = piece_position

  # Check valid moves diagonally upwards.
  for i in range(-2, 3):
    for j in range(-2, 3):
      if abs(i) == 2 and abs(j) == 1:
        new_row = row + i
        new_col = col + j
        if (new_row, new_col) not in other_positions:
          valid_moves.append((new_row, new_col))

  return valid_moves


def get_rook_moves(piece_position, other_positions):
  valid_moves = []

  row, col = piece_position

  # Check valid moves horizontally.
  for i in range(1, 8):
    if 0 <= row + i < 8:
      if (row + i, col) not in other_positions:
        valid_moves.append((row + i, col))
      else:
        break

  for i in range(1, 8):
    if 0 <= col + i < 8:
      if (row, col + i) not in other_positions:
        valid_moves.append((row, col + i))
      else:
        break

  # Check valid moves vertically.
  for i in range(1, 8):
    if 0 <= row - i < 8:
      if (row - i, col) not in other_positions:
        valid_moves.append((row - i, col))
      else:
        break

  for i in range(1, 8):
    if 0 <= col - i < 8:
      if (row, col - i) not in other_positions:
        valid_moves.append((row, col - i))
      else:
        break

  return valid_moves

def get_queen_moves(piece_position, other_positions):
    return get_rook_moves(piece_position, other_positions) + get_bishop_moves(piece_position, other_positions)
def get_bishop_moves(piece_position, other_positions):

  valid_moves = []

  row, col = piece_position

  # Check valid moves diagonally upwards.
  for i in range(1, 8):
    if 0 <= row + i < 8 and 0 <= col + i < 8:
      if (row + i, col + i) not in other_positions:
        valid_moves.append((row + i, col + i))
      else:
        break

  for i in range(1, 8):
    if 0 <= row - i < 8 and 0 <= col - i < 8:
      if (row - i, col - i) not in other_positions:
        valid_moves.append((row - i, col - i))
      else:
        break

  # Check valid moves diagonally downwards.
  for i in range(1, 8):
    if 0 <= row + i < 8 and 0 <= col - i < 8:
      if (row + i, col - i) not in other_positions:
        valid_moves.append((row + i, col - i))
      else:
        break

  for i in range(1, 8):
    if 0 <= row - i < 8 and 0 <= col + i < 8:
      if (row - i, col + i) not in other_positions:
        valid_moves.append((row - i, col + i))
      else:
        break

  return valid_moves
@app.route("/chess/<slug>", methods=["POST"])
def get_valid_moves_endpoint(slug):

  # Get the chess piece name from the slug.
  piece_name = slug.lower()

  # Get the chess piece positions from the request body.
  piece_positions = json.loads(request.data)

  # Get the valid moves for the given chess piece.
  valid_moves = get_valid_moves([piece_name], piece_positions)

  # Return a JSON response containing the valid moves.
  response = {"valid_moves": valid_moves}
  return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)