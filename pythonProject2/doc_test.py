from flask import Flask, request, jsonify

app = Flask(__name__)

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

@app.route('/valid_knight_moves', methods=['GET', 'POST'])
def valid_knight_moves():
    if request.method == 'POST':
        data = request.json
        position = data.get('position')

        if position is None or len(position) != 2:
            return jsonify({'message': 'Invalid position'}), 400

        valid_moves = get_valid_knight_moves(position)

        return jsonify({'valid_moves': valid_moves}), 200
    else:
        return jsonify({'message': 'Method Not Allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
