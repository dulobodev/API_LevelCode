from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.DesafiosControllers import DesafioController
from models.DesafiosModel import DesafioModel

desafio_bp = Blueprint('desafio', __name__)

@desafio_bp.route('/register', endpoint='desafio1', methods=['POST'])
def register_desafio():
    return DesafioController.registrar_desafio()

@desafio_bp.route('/get', endpoint='desafio2', methods=['GET'])
def get_def():
    return DesafioModel.get_desafio()