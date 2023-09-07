from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def api_hello():
    response = {'message': 'Hello from the API!'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
