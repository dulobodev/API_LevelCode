"""
This Flask blueprint defines routes for registering permissions, roles, admins, and logging in with
JWT authentication and superadmin role validation.
:return: The code defines a Flask Blueprint named `admin_bp` with several routes for handling
admin-related functionalities. Each route is decorated with `jwt_required()` and
`superadmin_required()` decorators to ensure authentication and authorization.
"""
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import superadmin_required
from controllers.admin.AdminController import AdminController
from models.RolesModel import RoleModel

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/permissions', endpoint='admin1',methods=['POST'])
@jwt_required()
@superadmin_required()
def register_permissions():
    return AdminController.registrar_permissions(request.get_json())

@admin_bp.route('/roles', endpoint='admin2',methods=['POST'])
@jwt_required()
@superadmin_required()
def register_role():
    return AdminController.registrar_role()

@admin_bp.route('/roles_get', endpoint='admin5',methods=['GET'])
@jwt_required()
@superadmin_required()
def register_role():
    return RoleModel.get()


@admin_bp.route('/register', endpoint='admin3',methods=['POST'])
@jwt_required()
@superadmin_required()
def register_admin():
    return AdminController.registrar_admin()

@admin_bp.route('/login', endpoint='admin4',methods=['POST'])
@jwt_required()
@superadmin_required()
def login():
    return AdminController.login_admin()