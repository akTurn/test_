from flask import Flask, request
from chess import Board

app = Flask(__name__)

def get_valid_moves(piece_name, piece_position, board):
  """
  Returns a list of valid moves for a given chess piece.

  Args:
    piece_name: The name of the chess piece.
    piece_position: The position of the chess piece on the board.
    board: The current state of the chessboard.

  Returns:
    A list of valid moves for the chess piece.
  """

  valid_moves = []

  if piece_name == "Rook":
    valid_moves = board.get_all_possible_moves(piece_position)
  elif piece_name == "Queen":
    valid_moves = board.get_all_possible_moves(piece_position)
  elif piece_name == "Bishop":
    valid_moves = board.get_all_possible_moves_by_direction(piece_position, "diagonal")
  elif piece_name == "Knight":
    valid_moves = board.get_all_possible_moves_by_direction(piece_position, "knight")
  else:
    raise ValueError("Invalid piece name: " + piece_name)

  return valid_moves

@app.route("/chess/<piece_name>", methods=["POST"])
def get_chess_moves(piece_name):
  """
  Returns a list of valid moves for a given chess piece.

  Args:
    piece_name: The name of the chess piece.

  Returns:
    A list of valid moves for the chess piece.
  """
  data = request.get_json()
  pieces = data["pieces"]

  board = Board()
  for piece_name, piece_position in pieces.items():
    board.set_piece_at(piece_position, piece_name)

  valid_moves = get_valid_moves(piece_name, piece_position, board)
  return {"valid_moves": valid_moves}

if __name__ == "__main__":
  app.run(debug=True)
