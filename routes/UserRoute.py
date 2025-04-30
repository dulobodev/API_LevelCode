"""
The code defines Flask routes for user registration and login using a Blueprint.
:return: The `register_user()` function returns the result of the
`UsuarioControllers.registrar_usuario()` method, and the `login_user()` function returns the result
of the `UsuarioControllers.login()` method.
"""
from flask import Blueprint
from controllers.UsuarioController import UsuarioControllers

user_bp = Blueprint('users', __name__)

@user_bp.route('/register', endpoint='user1', methods=['POST'])
def register_user():
    return UsuarioControllers.registrar_usuario()

@user_bp.route('/login', endpoint='user2', methods=['POST'])
def login_user():
    return UsuarioControllers.login()