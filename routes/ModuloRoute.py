from flask import Blueprint
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.ModuloControllers import ModuloControllers
from models.ModuloModel import ModuloModel

modulo_bp = Blueprint('modulo', __name__)

@modulo_bp.route('/register', endpoint='modulo1', methods=['POST'])
@jwt_required()
@admin_required('PoderAdemiro')
def register_modulo():
    return ModuloControllers.registrar_modulo()

@modulo_bp.route('/get', endpoint='modulo2', methods=['GET'])
def get_mod():
    return ModuloModel.get_modulo()