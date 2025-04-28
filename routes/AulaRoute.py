from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.AulaControllers import AulaController
from models.AulaModel import AulaModel

aula_bp = Blueprint('aula', __name__)

@aula_bp.route('/register_aula', endpoint='aula1',methods=['POST'])
@jwt_required
@admin_required('PoderAdemiro')
def register_aula():
    return AulaController.registrar_aula(request.get_json())

@aula_bp.route('/get_aula', endpoint='aula2',methods=['GET'])
@jwt_required
@admin_required('PoderAdemiro')
def get():
    return AulaModel.get_aula()