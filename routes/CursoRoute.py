from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.CursoControllers import CursoController
from controllers.UserCursoController import UserCurso
from models.CursoModel import CursoModel

curso_bp = Blueprint('curso', __name__)

@curso_bp.route('/register', endpoint='curso1', methods=['POST'])
def register_curso():
    return CursoController.registrar_curso()

@curso_bp.route('/concluir', endpoint='cruso2', methods=['POST'])
@jwt_required()
@admin_required('PoderAdemiro')
def concluir():
    return UserCurso.concluir_aula()

@curso_bp.route('/get', endpoint='cruso3', methods=['GET'])
def get_c():
    return CursoModel.get_curso()