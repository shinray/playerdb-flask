from flask import Blueprint, jsonify, abort
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
  if True:
    return jsonify({"error": "This route is not yet implemented"}), 501
  return jsonify({"message": "Processing source file..."}), 202
