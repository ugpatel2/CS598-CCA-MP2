from flask import Flask, jsonify

import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST'])
def load_server():
    subprocess.Popen(["python3", "stress_cpu.py"])
    return jsonify({'message': 'Ran the subprocess successfully'}), 200


@app.route('/', methods=['GET'])
def get_private_ip():
    hname = socket.gethostname()
    return hname, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
