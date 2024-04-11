from flask import Blueprint, jsonify, abort
from .models import Player

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/players', methods=['GET'])
def get_players():
 players = Player.query.all()
 if players:
    response = [player.as_dict() for player in players]
    return jsonify(response)
 else:
   return jsonify([])

@api_bp.route('/api/players/<playerId>', methods=['GET'])
def get_player_by_id(playerId):
   player = Player.get_by_playerId(playerId)
   if player:
     return jsonify(player.as_dict())
   else:
    #  abort(404, "Could not find a player by the id {}".format(playerId))
    jsonify({'error', "Could not find a player by the id {}".format(playerId)}), 404
