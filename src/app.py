import json
import csv
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# TODO: separate thread/file
# TODO: in memory db
current_dir = os.path.dirname(os.path.abspath(__file__))
datasrc_path = os.path.join(os.path.dirname(current_dir), 'players.csv')
with open(datasrc_path, 'r', encoding='utf-8') as csvfile:
   csv_reader = csv.reader(csvfile)
   for row in csv_reader:
      print(row)

# TODO: read csv, serve players instead
employees = [ { 'id': 1, 'name': 'Ashley' }, { 'id': 2, 'name': 'Kate' }, { 'id': 3, 'name': 'Joe' }]

@app.route('/api/players', methods=['GET'])
def get_players():
 return jsonify(employees)

if __name__ == '__main__':
    app.run(port=5000)