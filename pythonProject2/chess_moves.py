from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the chessboard dimensions
ROWS = 8
COLS = 8
def get_bishop_moves(position):
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []

    # Diagonal moves
    for i in range(1, ROWS):
        if 0 <= row + i < ROWS and 0 <= col + i < COLS:
            moves.append(chr(col + i + ord('A')) + str(row + i + 1))
        if 0 <= row - i < ROWS and 0 <= col + i < COLS:
            moves.append(chr(col + i + ord('A')) + str(row - i + 1))
        if 0 <= row + i < ROWS and 0 <= col - i < COLS:
            moves.append(chr(col - i + ord('A')) + str(row + i + 1))
        if 0 <= row - i < ROWS and 0 <= col - i < COLS:
            moves.append(chr(col - i + ord('A')) + str(row - i + 1))

    return moves
def get_rook_moves(position):
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []

    # Horizontal and vertical moves
    for i in range(ROWS):
        if i != row:
            moves.append(chr(col + ord('A')) + str(i + 1))
        if i != col:
            moves.append(chr(i + ord('A')) + str(row + 1))

    return moves

def get_queen_moves(position):
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []

    # Horizontal and vertical moves
    for i in range(ROWS):
        if i != row:
            moves.append(chr(col + ord('A')) + str(i + 1))
        if i != col:
            moves.append(chr(i + ord('A')) + str(row + 1))

    # Diagonal moves
    for i in range(1, ROWS):
        if 0 <= row + i < ROWS and 0 <= col + i < COLS:
            moves.append(chr(col + i + ord('A')) + str(row + i + 1))
        if 0 <= row - i < ROWS and 0 <= col + i < COLS:
            moves.append(chr(col + i + ord('A')) + str(row - i + 1))
        if 0 <= row + i < ROWS and 0 <= col - i < COLS:
            moves.append(chr(col - i + ord('A')) + str(row + i + 1))
        if 0 <= row - i < ROWS and 0 <= col - i < COLS:
            moves.append(chr(col - i + ord('A')) + str(row - i + 1))

    return moves



# Function to get valid moves for a knight
def get_knight_moves(position):
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []
    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    for dr, dc in knight_moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < ROWS and 0 <= new_col < COLS:
            moves.append(chr(new_col + ord('A')) + str(new_row + 1))

    return moves


# API endpoint for getting valid moves of a chess piece
@app.route('/chess/<slug>', methods=['POST'])
def get_valid_moves(slug):
    data = request.json
    piece_positions = data.get("Positions", {})

    if slug == 'knight':
        knight_position = piece_positions.get("Knight")
        if knight_position:
            valid_moves = get_knight_moves(knight_position)
            return jsonify({"valid_moves": valid_moves})
        else:
            return jsonify({"error": "Knight position not provided"}), 400
    else:
        return jsonify({"error": "Invalid chess piece"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
