from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.RankingControllers import RankingControllers
from models.RankingModel import RankingModel

ranking_bp = Blueprint('ranking', __name__)

@ranking_bp.route('/register', endpoint='ranking1', methods=['POST'])
def register_ranking():
    return RankingControllers.registrar_ranking()

@ranking_bp.route('/get', endpoint='ranking2', methods=['GET'])
def get_ranking():
    return RankingModel.get_ranking()