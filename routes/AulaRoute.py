"""
This Python Flask blueprint defines routes for registering and retrieving Aula objects, with
authentication and admin role validation.
:return: The code snippet provided defines a Flask Blueprint named `aula_bp` with two routes.
"""
from flask import Blueprint
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.admin.AulaControllers import AulaController
from models.AulaModel import AulaModel

aula_bp = Blueprint('aula', __name__)

@aula_bp.route('/register', endpoint='aula1',methods=['POST'])
@jwt_required()
@admin_required('PoderAdemiro')
def register_aula():
    return AulaController.registrar_aula()

@aula_bp.route('/get', endpoint='aula2',methods=['GET'])
@jwt_required()
@admin_required('PoderAdemiro')
def get():
    return AulaModel.get_aula()