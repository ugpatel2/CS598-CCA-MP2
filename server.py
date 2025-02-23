from flask import Flask, request, jsonify

app = Flask(__name__)
num = 0  # Variable to store the number

@app.route('/', methods=['POST'])
def save_number():
    global num
    data = request.get_json()
    if 'num' in data:
        num = data['num']
        return jsonify({'message': 'Number saved successfully'}), 200
    return jsonify({'error': 'Missing num in request'}), 400

@app.route('/', methods=['GET'])
def get_number():
    if num is not None:
        return str(num), 200
    return jsonify({'error': 'No number saved'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
