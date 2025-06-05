from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/api')
def get_data():
    try:
        f= open('data.json', 'r')
        filedata = json.load(f)
        return jsonify(filedata)
    except FileNotFoundError:
        return jsonify({"error": "data.json not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
