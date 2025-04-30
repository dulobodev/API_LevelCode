"""
This Python code defines Flask routes for registering and retrieving rankings, with authentication
and admin role validation.
:return: The code snippet provided defines a Flask Blueprint named `ranking_bp` with two routes.
"""
from flask import Blueprint
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.RankingControllers import RankingControllers
from models.RankingModel import RankingModel

ranking_bp = Blueprint('ranking', __name__)

@ranking_bp.route('/register', endpoint='ranking1', methods=['POST'])
@jwt_required()
@admin_required('PoderAdemiro')
def register_ranking():
    return RankingControllers.registrar_ranking()

@ranking_bp.route('/get', endpoint='ranking2', methods=['GET'])
@jwt_required()
@admin_required('PoderAdemiro')
def get_ranking():
    return RankingModel.get_ranking()