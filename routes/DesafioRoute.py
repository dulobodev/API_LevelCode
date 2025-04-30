"""
The code defines Flask routes for registering and retrieving challenges, requiring JWT
authentication and admin role validation.
:return: The code snippet provided defines a Flask Blueprint named `desafio_bp` with two routes.
"""
from flask import Blueprint
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.DesafiosControllers import DesafioController
from models.DesafiosModel import DesafioModel

desafio_bp = Blueprint('desafio', __name__)

@desafio_bp.route('/register', endpoint='desafio1', methods=['POST'])
@jwt_required()
@admin_required('PoderAdemiro')
def register_desafio():
    return DesafioController.registrar_desafio()

@desafio_bp.route('/get', endpoint='desafio2', methods=['GET'])
@jwt_required()
@admin_required('PoderAdemiro')
def get_def():
    return DesafioModel.get_desafio()