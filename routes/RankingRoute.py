from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.RankingControllers import RankingControllers
from models.RankingModel import RankingModel

ranking_bp = Blueprint('ranking', __name__)

@ranking_bp.route('/register_ranking', endpoint='ranking1', methods=['POST'])
@jwt_required
@admin_required('PoderAdemiro')
def register_ranking():
    return RankingControllers.registrar_ranking(request.get_json())

@ranking_bp.route('/get_ranking', endpoint='ranking2', methods=['GET'])
@jwt_required
@admin_required
def get_ranking():
    return RankingModel.get_ranking()