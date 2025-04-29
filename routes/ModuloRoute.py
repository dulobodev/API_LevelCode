from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.ModuloControllers import ModuloControllers
from models.ModuloModel import ModuloModel

modulo_bp = Blueprint('modulo', __name__)

@modulo_bp.route('/register_modulo', endpoint='modulo1', methods=['POST'])
@jwt_required()
@admin_required('PoderAdemiro')
def register_modulo():
    return ModuloControllers.registrar_modulo(request.get_json())

@modulo_bp.route('/get_modulo', endpoint='modulo2', methods=['GET'])
@jwt_required()
@admin_required
def get_mod():
    return ModuloModel.get_modulo()