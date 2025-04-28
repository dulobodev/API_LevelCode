from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.ConquistaControllers import ConquistaController
from models.ConquistasModel import ConquistaModel

conquista_bp = Blueprint('conquista', __name__)

@conquista_bp.route('/register_conquista', endpoint='conquista1', methods=['POST'])
@jwt_required
@admin_required('PoderAdemiro')
def register_conquista():
    return ConquistaController.registrar_conquista(request.get_json())

@conquista_bp.route('/get_conquista', endpoint='conquista2', methods=['GET'])
@jwt_required
@admin_required('PoderAdemiro')
def get_conq():
    return ConquistaModel.get_conquista()