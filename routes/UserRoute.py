from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import admin_required
from controllers.UsuarioController import UsuarioControllers

user_bp = Blueprint('users', __name__)

@user_bp.route('/register', endpoint='user1', methods=['POST'])
def register_user():
    return UsuarioControllers.registrar_usuario()

@user_bp.route('/login', endpoint='user2', methods=['POST'])
def login_user():
    return UsuarioControllers.login()