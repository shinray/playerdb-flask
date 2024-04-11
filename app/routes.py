import threading
from flask import Blueprint, jsonify, current_app
from .utils import reset_database
from .models import Player

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/players', methods=['GET'])
def get_players():
 players = Player.get_players()
 if players:
    response = [player.as_dict() for player in players]
    return response
 else:
    return []

@api_bp.route('/api/players/<playerId>', methods=['GET'])
def get_player_by_id(playerId):
   player = Player.get_by_playerId(playerId)
   if player:
    return player.as_dict()
   else:
    return jsonify({'error': "Could not find a player by the id {}".format(playerId)}), 404

@api_bp.route('/api/admin/loadfile', methods=['GET'])
def loadfile():
    path = current_app.config['CSV_FILE_PATH']
    def reset_db_thread(context, path):
        with context:
           reset_database(path)
    app_context = current_app.app_context()       
    
    with current_app.app_context():
        thread = threading.Thread(target=reset_db_thread, args=(app_context, path))
        thread.start()

    return jsonify({"message": "Processing source file..."}), 202
