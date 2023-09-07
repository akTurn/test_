from flask import Flask, request, render_template
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

def get_bishop_moves(position):
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []

    # Diagonal moves
    for dr, dc in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
        moves.extend(get_direction_moves(row, col, dr, dc))

    return moves

def get_rook_moves(position):
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []

    # Horizontal and vertical moves
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        moves.extend(get_direction_moves(row, col, dr, dc))

    return moves

def get_queen_moves(position):
    row, col = int(position[1]) - 1, ord(position[0]) - ord('A')
    moves = []

    # Horizontal, vertical, and diagonal moves
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
        moves.extend(get_direction_moves(row, col, dr, dc))

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

        for piece, position in piece_positions.items():
            if piece == 'Queen':
                valid_moves['Queen'] = get_queen_moves(position)
            elif piece == 'Bishop':
                valid_moves['Bishop'] = get_bishop_moves(position)
            elif piece == 'Rook':
                valid_moves['Rook'] = get_rook_moves(position)
            elif piece == 'Knight':
                valid_moves['Knight'] = get_knight_moves(position)

    return render_template('index.html', valid_moves=valid_moves)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
