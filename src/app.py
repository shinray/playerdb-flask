import json
import csv
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

players = []

# TODO: separate thread/file
# TODO: in memory db
current_dir = os.path.dirname(os.path.abspath(__file__))
datasrc_path = os.path.join(os.path.dirname(current_dir), 'lahman_1871-2023_csv', 'People.csv')
with open(datasrc_path, 'rU', encoding='utf-8') as csvfile:
   csv_reader = csv.DictReader(csvfile)
   for row in csv_reader:
      players.append(row)

@app.route('/api/players', methods=['GET'])
def get_players():
 return jsonify(players)

if __name__ == '__main__':
    app.run(port=5000)