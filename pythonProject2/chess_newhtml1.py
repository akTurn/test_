from flask import Flask, request, render_template

app = Flask(__name__)

# Define the chessboard dimensions
ROWS = 8
COLS = 8


def get_bishop_moves(position, occupied_positions):
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []

    # Diagonal moves
    for i in range(1, ROWS):
        if add_move(moves, row + i, col + i, occupied_positions):
            break
    for i in range(1, ROWS):
        if add_move(moves, row - i, col + i, occupied_positions):
            break
    for i in range(1, ROWS):
        if add_move(moves, row + i, col - i, occupied_positions):
            break
    for i in range(1, ROWS):
        if add_move(moves, row - i, col - i, occupied_positions):
            break

    return moves


# Function to get valid moves for a rook
def get_rook_moves(position, occupied_positions):
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []

    # Horizontal moves
    for i in range(ROWS):
        if add_move(moves, i, col, occupied_positions):
            break

    # Vertical moves
    for i in range(COLS):
        if add_move(moves, row, i, occupied_positions):
            break

    return moves


# Function to get valid moves for a knight
def get_knight_moves(position, occupied_positions):
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []
    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    for dr, dc in knight_moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < ROWS and 0 <= new_col < COLS:
            move = chr(new_col + ord('A')) + str(new_row + 1)
            if not any(move in occupied_position for occupied_position in occupied_positions):
                moves.append(move)

    return moves


def get_queen_moves(position, occupied_positions):
    print("run", position, occupied_positions)

    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []
    print("run", row, col)
    # Diagonal moves (similar to Bishop)
    for i in range(1, ROWS):
        if add_move(moves, row + i, col + i, occupied_positions):
            break
    for i in range(1, ROWS):
        if add_move(moves, row - i, col + i, occupied_positions):
            break
    for i in range(1, ROWS):
        if add_move(moves, row + i, col - i, occupied_positions):
            break
    for i in range(1, ROWS):
        if add_move(moves, row - i, col - i, occupied_positions):
            break

    # Horizontal and vertical moves (similar to Rook)
    for i in range(ROWS):
        if i != row and add_move(moves, i, col, occupied_positions):
            break
    for i in range(COLS):
        if i != col and add_move(moves, row, i, occupied_positions):
            break

    return moves


def add_move(moves, row, col, occupied_positions):
    if 0 <= row < ROWS and 0 <= col < COLS:
        move = chr(col + ord('A')) + str(row + 1)
        if not any(move in occupied_position for occupied_position in occupied_positions):
            moves.append(move)
            return True
    return False


"""
# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    valid_moves = {}

    if request.method == 'POST':
        piece_names = ['Queen', 'Bishop', 'Rook', 'Knight']
        piece_positions = {}

        for piece in piece_names:
            position = request.form.get(f'piece_position[{piece}]')
            if position:
                piece_positions[piece] = position

        occupied_positions = [position for piece, position in piece_positions.items() if position]

        for piece, position in piece_positions.items():
            if piece == 'Queen':
                valid_moves['Queen'] = get_queen_moves(position, occupied_positions)
            elif piece == 'Bishop':
                valid_moves['Bishop'] = get_bishop_moves(position, occupied_positions)
            elif piece == 'Rook':
                valid_moves['Rook'] = get_rook_moves(position, occupied_positions)
            elif piece == 'Knight':
                valid_moves['Knight'] = get_knight_moves(position, occupied_positions)

    return render_template('index2.html', valid_moves=valid_moves)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
"""


def get_valid_moves(position, occupied_positions, piece_to_calculate):
    if piece_to_calculate == 'Queen':
        return get_queen_moves(position, occupied_positions)
    elif piece_to_calculate == 'Bishop':
        return get_bishop_moves(position, occupied_positions)
    elif piece_to_calculate == 'Rook':
        return get_rook_moves(position, occupied_positions)
    elif piece_to_calculate == 'Knight':
        return get_knight_moves(position, occupied_positions)

    else:
        return []

"""

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    valid_moves = {}

    if request.method == 'POST':
        piece_names = ['Queen', 'Rook', 'Bishop', 'Knight']
        all_piece_positions = {}

        for piece in piece_names:
            position = request.form.get(f'piece_position[{piece}]')
            all_piece_positions[piece] = position

        for piece_name, piece_position in all_piece_positions.items():
            other_piece_positions = {other_piece_name: all_piece_positions[other_piece_name] for other_piece_name in piece_names if other_piece_name != piece_name}
            occupied_positions = [position for position in other_piece_positions.values() if position]
            valid_moves[piece_name] = get_valid_moves(piece_name, piece_position, occupied_positions)

        # Check for overlapping moves between pieces
        for piece_name in piece_names:
            other_piece_names = [other_piece for other_piece in piece_names if other_piece != piece_name]
            for other_piece_name in other_piece_names:
                valid_moves[piece_name] = [move for move in valid_moves[piece_name] if move not in valid_moves[other_piece_name]]

    return render_template('index4.html', valid_moves=valid_moves)
"""
# Function to remove common moves between two lists of moves
def remove_common_moves(list1, list2):
    print(list1,list2)
    return [move for move in list1 if move not in list2]

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    valid_moves = {}

    if request.method == 'POST':
        piece_names = ['Queen', 'Bishop', 'Rook', 'Knight']
        piece_to_calculate = request.form.get('piece_to_calculate')
        piece_positions = {}

        for piece in piece_names:
            position = request.form.get(f'piece_position[{piece}]')
            if position:
                piece_positions[piece] = position
        #Remove the selected piece's position from occupied_positions
        occupied_positions = [position for piece, position in piece_positions.items() if
                              position and piece != piece_to_calculate]

        #occupied_positions = [position for piece, position in piece_positions.items() if position]

        for piece, position in piece_positions.items():
            if piece == piece_to_calculate:
                  valid_moves[piece] = get_valid_moves(position, occupied_positions, piece_to_calculate)
                  print(f"valid{piece}",valid_moves[piece])
        # Remove common moves between the selected piece's valid moves and other pieces' valid moves
        for piece, position in piece_positions.items():
            if piece != piece_to_calculate:
                print(f"!!!!!!!{piece}")
                valid_moves[piece_to_calculate] = remove_common_moves(valid_moves[piece_to_calculate], valid_moves[piece])

    return render_template('index_final.html', valid_moves=valid_moves)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
