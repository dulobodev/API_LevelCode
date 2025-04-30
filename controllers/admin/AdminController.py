from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from schemas.UsuarioSchema import UserCreate, UserLogin
from schemas.RolesSchema import RolesCreate, PermissionCreate
from models.UsuarioModel import UsuarioModel
from models.RolesModel import RoleModel
from models.model import Usuario, Ranking, Role, Permission
from config.Database import db
from flask import jsonify, request
from dotenv import load_dotenv
import re


def senha_forte(senha):
    return (len(senha) >= 8 and
            re.search(r"[A-Z]", senha) and
            re.search(r"[a-z]", senha) and
            re.search(r"[0-9]", senha) and
            re.search(r"[@#$%^&*(),.?\":{}|<>]", senha))

load_dotenv()

class AdminController:
    
    @staticmethod
    def registrar_permissions(body: PermissionCreate):
        nova_permission = Permission(**body)
        if Permission.query.filter_by(nome=nova_permission.nome).first():
            return jsonify({"erro" : "Já existe uma permissão com este nome"}), 409
        try:
            db.session.add(nova_permission)
            db.session.commit()
            return jsonify({"message" : "Permission criada com sucesso."})
        except:
            return jsonify({"erro" : "Erro ao tentar criar permissao"}), 400

    @staticmethod
    def registrar_role():
        try:
            body = RolesCreate(**request.get_json())

            if RoleModel.busca_role_nome(body.nome):
                return jsonify({"error": "Role já existe"}), 422

            role = Role(nome=body.nome)
            db.session.add(role)

            for permission in body.permissions:
                existing_perm = Permission.query.filter_by(nome=permission.nome).first()
                if existing_perm:
                    role.permissions.append(existing_perm)
                else:
                    permission_obj = Permission(nome=permission.nome)
                    db.session.add(permission_obj)
                    role.permissions.append(permission_obj)

            db.session.commit()
            return jsonify({"message": "Role criada com sucesso", "role_id": role.id}), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar role", details=str(e)), 500

    @staticmethod
    def registrar_admin():
        try:
            body = UserCreate(**request.get_json())

            novo_admin = Usuario(
                nome = body.nome,
                email = body.email,
                senha = body.senha,
                roles_id = body.roles_id,
                ranking_id = body.ranking_id
            )

            if not senha_forte(novo_admin.senha):
                return jsonify(erro ="A senha deve conter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais."), 400
            if UsuarioModel.busca_email(novo_admin.email):
                return jsonify(error ="E-mail já cadastrado"), 422
            novo_admin.senha = generate_password_hash(novo_admin.senha)
            role = Role.query.get(novo_admin.roles_id)
        
            if not role:
                return jsonify(erro="Role não encontrada"), 404
            
            ranking = Ranking.query.get(novo_admin.ranking_id)
            if not ranking:
                return jsonify(erro="Ranking não encontrado"), 404
        
            db.session.add(novo_admin)
            db.session.commit()
            return jsonify({"message": "Admin criado com sucesso", "user_id": novo_admin.id}), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar um novo admin", details=str(e)), 500



    @staticmethod
    def login_admin():
        try:
            body = UserLogin(**request.get_json())

            validate = Usuario(
            nome = body.nome,
            senha= body.senha
            )

            usuario = UsuarioModel.busca_nome(validate.nome)
            if usuario and check_password_hash(usuario.senha, validate.senha):
                role = Role.query.get(usuario.roles_id)

                # Agora, extraia as permissões do role
                permissoes = [p.nome for p in role.permissions]

                token = create_access_token(identity=str(usuario.id),additional_claims={"role": role.nome,"permissions": permissoes})
                
                return jsonify({"access_token": token}), 200
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Nome do administrador ou senha invalidos", details=str(e)), 401

