from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.CursoControllers import CursoController
from models.CursoModel import CursoModel

curso_bp = Blueprint('curso', __name__)

@curso_bp.route('/register_curso', endpoint='curso1', methods=['POST'])
@jwt_required()
@admin_required('PoderAdemiro')
def register_curso():
    return CursoController.registrar_curso()

@curso_bp.route('/get_curso', endpoint='cruso2', methods=['GET'])
@jwt_required()
@admin_required('PoderAdemiro')
def get_c():
    return CursoModel.get_curso()