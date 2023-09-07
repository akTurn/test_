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
        valid_moves = calculate_valid_moves(slug, positions, current_position)
        return jsonify({"valid_moves": valid_moves})
    else:
        return jsonify({"error": f"Slug '{slug}' not found in positions dictionary"})


def calculate_valid_moves(slug, positions, current_position):
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
    valid_moves += calculate_rook_moves(current_position, positions)
    valid_moves += calculate_bishop_moves(current_position, positions)
    for piece_slug, piece_position in positions.items():
        if piece_slug != "Queen":
            valid_moves = filter_moves_for_obstacles(valid_moves, piece_position, current_position)
    return valid_moves


def calculate_knight_moves(current_position, positions):
    valid_moves = []
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
    for piece_slug, piece_position in positions.items():
        if piece_slug != "Knight":
            valid_moves = filter_moves_for_obstacles(valid_moves, piece_position, current_position)
    return valid_moves


def calculate_rook_moves(current_position, positions):
    valid_moves = []
    for row in 'abcdefgh':
        move = row + current_position[1]
        if move != current_position:
            valid_moves.append(move)
    for col in '12345678':
        move = current_position[0] + col
        if move != current_position:
            valid_moves.append(move)
    for piece_slug, piece_position in positions.items():
        if piece_slug != "Rook":
            valid_moves = filter_moves_for_obstacles(valid_moves, piece_position, current_position)
    return valid_moves


def calculate_bishop_moves(current_position, positions):
    valid_moves = []
    for row in 'abcdefgh':
        for col in '12345678':
            move = row + col
            if is_diagonal(current_position, move) and move != current_position:
                valid_moves.append(move)
    for piece_slug, piece_position in positions.items():
        if piece_slug != "Bishop":
            valid_moves = filter_moves_for_obstacles(valid_moves, piece_position, current_position)
    return valid_moves


def filter_moves_for_obstacles(valid_moves, obstacle_position, current_position):
    obstacle_position = obstacle_position.lower()
    if is_diagonal(current_position, obstacle_position):
        valid_moves = [move for move in valid_moves if not is_diagonal(current_position, move)]
    elif current_position[0] == obstacle_position[0]:
        valid_moves = [move for move in valid_moves if current_position[0] != move[0]]
    elif current_position[1] == obstacle_position[1]:
        valid_moves = [move for move in valid_moves if current_position[1] != move[1]]
    return valid_moves


def is_diagonal(position1, position2):
    return abs(ord(position1[0]) - ord(position2[0])) == abs(int(position1[1]) - int(position2[1]))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
