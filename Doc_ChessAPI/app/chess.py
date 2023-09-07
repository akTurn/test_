from flask import Flask, request, jsonify

app = Flask(__name__)
chess_positions = {}

board = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
         'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
         'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
         'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
         'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
         'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
         'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
         'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']


@app.route('/chess/<slug>', methods=['POST'])
def get_valid_moves(slug):
    slug = slug.capitalize()
    data = request.get_json()
    positions = data.get("Positions")

    if slug in positions:

        current_position = positions[slug].lower()
        print(f" {slug,current_position} ,{positions}")
        valid_moves = calculate_valid_moves(slug, positions,current_position)

        # Return the valid moves as JSON response
        return jsonify({"valid_moves": valid_moves})
    else:
        # Handle the case when the slug is not found in positions
        return jsonify({"error": f"Slug '{slug}' not found in positions dictionary"})

"""  # Implement logic to calculate valid moves based on the piece type (slug)
    valid_moves = calculate_valid_moves(slug, positions)

    # Return the valid moves as JSON response
    return jsonify({"valid_moves": valid_moves})
"""

def calculate_valid_moves(slug, positions,current_position):
    valid_moves = []
    if slug == "Rook":
        valid_moves = calculate_rook_moves(current_position, positions)
    elif slug == "Queen":
        valid_moves = calculate_queen_moves(current_position, positions)
    elif slug == "Bishop":
        valid_moves = calculate_bishop_moves(current_position, positions)
    elif slug == "Knight":
        valid_moves = calculate_knight_moves(current_position, positions)

    return valid_moves


def calculate_queen_moves(current_position, positions):
    valid_moves = []

    # Queen can move horizontally, vertically, and diagonally
    # Horizontal and vertical moves
    valid_moves += calculate_rook_moves(current_position, positions)

    # Diagonal moves
    valid_moves += calculate_bishop_moves(current_position, positions)

    # Consider other piece positions
    for piece_slug, piece_position in positions.items():
        if piece_slug != "Queen":
            valid_moves = filter_moves_for_obstacles(valid_moves, piece_position, current_position)

    return valid_moves


def calculate_knight_moves(current_position, positions):
    valid_moves = []

    # Knight can move in an L-shape pattern
    # Calculate all possible knight moves
    possible_moves = [
        (2, 1), (1, 2),
        (-2, 1), (-1, 2),
        (2, -1), (1, -2),
        (-2, -1), (-1, -2)
    ]

    row, col = current_position[0], int(current_position[1])


    for move in possible_moves:
        new_row = chr(ord(row) + move[0])
        new_col = col + move[1]
        new_position = new_row + str(new_col)

        if new_position in board:
            valid_moves.append(new_position)

    # Filter valid moves to avoid obstacles (pieces)
    for piece_slug, piece_position in positions.items():

        if piece_slug != "Knight":
            valid_moves = filter_moves_for_obstacles(valid_moves, piece_position, current_position)

    return valid_moves


def calculate_rook_moves(current_position, positions):
    valid_moves = []

    # Rook can move horizontally and vertically
    # Check horizontal moves
    for row in 'abcdefgh':
        move = row + current_position[1]
        if move != current_position:
            valid_moves.append(move)

    # Check vertical moves
    for col in '12345678':
        move = current_position[0] + col
        if move != current_position:
            valid_moves.append(move)

    # Filter valid moves to avoid obstacles (pieces)
    for piece_slug, piece_position in positions.items():
        if piece_slug != "Rook":
            valid_moves = filter_moves_for_obstacles(valid_moves, piece_position, current_position)

    return valid_moves


def calculate_bishop_moves(current_position, positions):
    valid_moves = []

    # Bishop can move diagonally
    for row in 'abcdefgh':
        for col in '12345678':
            move = row + col
            if is_diagonal(current_position, move) and move != current_position:
                valid_moves.append(move)

    # Filter valid moves to avoid obstacles (pieces)
    for piece_slug, piece_position in positions.items():
        if piece_slug != "Bishop":
            valid_moves = filter_moves_for_obstacles(valid_moves, piece_position, current_position)

    return valid_moves


def filter_moves_for_obstacles(valid_moves, obstacle_position, current_position):
    obstacle_position =obstacle_position.lower()
    print("valid_moves", valid_moves)
    print("obstacle_position", obstacle_position)
    print("current_position",current_position)
    # Filter valid moves to avoid obstacles (pieces)
    if is_diagonal(current_position, obstacle_position):
        # Filter diagonal moves
        valid_moves = [move for move in valid_moves if not is_diagonal(current_position, move)]
    elif current_position[0] == obstacle_position[0]:
        # Filter horizontal moves
        valid_moves = [move for move in valid_moves if current_position[0] != move[0]]
    elif current_position[1] == obstacle_position[1]:
        # Filter vertical moves
        valid_moves = [move for move in valid_moves if current_position[1] != move[1]]

    return valid_moves


def is_diagonal(position1, position2):
    return abs(ord(position1[0]) - ord(position2[0])) == abs(int(position1[1]) - int(position2[1]))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
