from flask import Flask, request, jsonify

app = Flask(__name__)


# Define the chessboard dimensions
ROWS = 8
COLS = 8

# Function to get moves in a specific direction
def get_direction_moves(row, col, dr, dc):
    moves = []
    while True:
        row += dr
        col += dc
        if 0 <= row < ROWS and 0 <= col < COLS:
            moves.append(chr(col + ord('A')) + str(row + 1))
        else:
            break
    return moves

def calculate_bishop_moves(position):
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []

    # Diagonal moves
    for dr, dc in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
        moves.extend(get_direction_moves(row, col, dr, dc))

    return moves

def calculate_rook_moves(position):
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []

    # Horizontal and vertical moves
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        moves.extend(get_direction_moves(row, col, dr, dc))

    return moves

def calculate_queen_moves(position):
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []

    # Horizontal, vertical, and diagonal moves
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
        moves.extend(get_direction_moves(row, col, dr, dc))

    return moves

# Function to get valid moves for a knight
def calculate_knight_moves(position):
    print("position",position)
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    print(row,col)
    moves = []
    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    for dr, dc in knight_moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < ROWS and 0 <= new_col < COLS:
            moves.append(chr(new_col + ord('A')) + str(new_row + 1))

    return moves


def calculate_valid_moves(positions,slug):
    print("slug",slug,"positions",positions)

    valid_moves = []
    if slug == "Rook":
        valid_moves = calculate_rook_moves(positions)
    elif slug == "Queen":
        valid_moves = calculate_queen_moves(positions)
    elif slug == "Bishop":
        valid_moves = calculate_bishop_moves(positions)
    elif slug == "Knight":
        valid_moves = calculate_knight_moves(positions)

    return valid_moves

def remove_common_moves(list1, list2):
    print(list1, list2)
    return [move for move in list1 if move not in list2]

@app.route('/chess/<slug>', methods=['POST'])
def get_valid_moves(slug):
    valid_moves = {}
    slug = slug.capitalize()
    data = request.get_json()
    positions = data.get("Positions")
    print("positions",positions)

    for piece, position in positions.items():

        if piece == slug:

            valid_moves[slug] = calculate_valid_moves(position, slug)
            print(f"valid{piece}", valid_moves[slug])
        else:

            valid_moves[piece] = calculate_valid_moves(position, piece)
            print(f"valid{piece}", valid_moves[piece])

    # Remove common moves between the selected piece's valid moves and other pieces' valid moves
    for piece, position in positions.items():
        if piece != slug:
            valid_moves[slug] = remove_common_moves(valid_moves[slug],
                                                                  valid_moves[piece])
    return jsonify({"valid_moves": valid_moves[slug]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
