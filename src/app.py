import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# TODO: read csv, serve players instead
employees = [ { 'id': 1, 'name': 'Ashley' }, { 'id': 2, 'name': 'Kate' }, { 'id': 3, 'name': 'Joe' }]

@app.route('/api/players', methods=['GET'])
def get_players():
 return jsonify(employees)

if __name__ == '__main__':
    app.run(port=5000)