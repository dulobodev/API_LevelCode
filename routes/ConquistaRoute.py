from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.ConquistaControllers import ConquistaController
from models.ConquistasModel import ConquistaModel

conquista_bp = Blueprint('conquista', __name__)

@conquista_bp.route('/register', endpoint='conquista1', methods=['POST'])
def register_conquista():
    return ConquistaController.registrar_conquista()

@conquista_bp.route('/adicionar', endpoint='conquista2', methods=['POST'])
def add_conquista():
    return ConquistaController.adicionar_conquista()

@conquista_bp.route('/get', endpoint='conquista3', methods=['GET'])
def get_conq():
    return ConquistaModel.get_conquista()