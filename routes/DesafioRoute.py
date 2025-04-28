from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.DesafiosControllers import DesafioController
from models.DesafiosModel import DesafioModel

desafio_bp = Blueprint('desafio', __name__)

@desafio_bp.route('/register_desafio', endpoint='desafio1', methods=['POST'])
@jwt_required
@admin_required('PoderAdemiro')
def register_desafio():
    return DesafioController.registrar_desafio(request.get_json())

@desafio_bp.route('/get_desafio', endpoint='desafio2', methods=['GET'])
@jwt_required
@admin_required('PoderAdemiro')
def get_def():
    return DesafioModel.get_desafio()