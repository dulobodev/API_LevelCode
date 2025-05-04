from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.RolesValidate import superadmin_required
from controllers.admin.AdminController import AdminController
from models.RolesModel import RoleModel

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/permissions', endpoint='admin1',methods=['POST'])
@jwt_required()
@superadmin_required
def register_permissions():
    return AdminController.registrar_permissions(request.get_json())

@admin_bp.route('/roles', endpoint='admin2',methods=['POST'])
@jwt_required()
@superadmin_required
def register_role():
    return AdminController.registrar_role()

@admin_bp.route('/roles_get', endpoint='admin5',methods=['GET'])
@jwt_required()
@superadmin_required
def register_role():
    return RoleModel.get()


@admin_bp.route('/register', endpoint='admin3',methods=['POST'])
@jwt_required()
@superadmin_required
def register_admin():
    return AdminController.registrar_admin()

@admin_bp.route('/login', endpoint='admin4',methods=['POST'])
@jwt_required()
@superadmin_required
def login():
    return AdminController.login_admin()