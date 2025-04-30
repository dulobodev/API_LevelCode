from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.AulaControllers import AulaController
from models.AulaModel import AulaModel

aula_bp = Blueprint('aula', __name__)

@aula_bp.route('/register', endpoint='aula1',methods=['POST'])
def register_aula():
    return AulaController.registrar_aula()

@aula_bp.route('/get', endpoint='aula2',methods=['GET'])
def get():
    return AulaModel.get_aula()