"""
This Python Flask blueprint defines routes for registering a course, concluding a lesson, and
retrieving course information, with authentication and role-based access control.
:return: The code provided defines a Flask Blueprint named `curso_bp` with three routes:
"""
from flask import Blueprint
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.CursoControllers import CursoController
from controllers.UserCursoController import UserCurso
from models.CursoModel import CursoModel

curso_bp = Blueprint('curso', __name__)

@curso_bp.route('/register', endpoint='curso1', methods=['POST'])
@jwt_required()
@admin_required('PoderAdemiro')
def register_curso():
    return CursoController.registrar_curso()

@curso_bp.route('/concluir', endpoint='cruso2', methods=['POST'])
@jwt_required()
@admin_required('PoderAdemiro')
@jwt_required()
@admin_required('PoderAdemiro')
def concluir():
    return UserCurso.concluir_aula()

@curso_bp.route('/get', endpoint='cruso3', methods=['GET'])
def get_c():
    return CursoModel.get_curso()