from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from schemas.UsuarioSchema import UserCreate
from schemas.RolesSchema import RolesCreate, PermissionCreate
from models.UsuarioModel import UsuarioModel
from models.RolesModel import RoleModel
from config.Database import Role, Permission, db
from flask import jsonify, request
from dotenv import load_dotenv
import os

load_dotenv()

def registrar_permissions_superadmin(body: dict):  
    try:
        permission_data = PermissionCreate.parse_obj(body)  # Parse da entrada de dados

        # Verifica se a permissão já existe
        if Permission.query.filter_by(nome=permission_data.nome).first():
            return jsonify({"erro": "Permissao ja existente"}), 422

        nova_permission = Permission(**permission_data.dict())  # Cria o objeto de permissão
        db.session.add(nova_permission)
        db.session.commit()

        # Serializa a permissão para garantir que seja JSON serializable
        permission_serialized = {
            "id": nova_permission.id,
            "nome": nova_permission.nome
        }

        return jsonify({"message": "Permissão criada com sucesso", "permission": permission_serialized}), 201
        
    except Exception as e:
        print(f"Erro ao tentar criar permissão superadmin: {e}")
        return jsonify({"erro": "Erro ao criar permissão"}), 422


def registrar_role_superadmin(dados: dict):  
    try:
        body = RolesCreate.parse_obj(dados)  # Parse da entrada de dados

        # Verificando se a role já existe
        if RoleModel.busca_role_nome(body.nome):
            print(f"Role '{body.nome}' já existe no banco.")  # Log para verificação
            return jsonify(erro="Já existe a role superadmin.")
        
        role = Role(nome=body.nome)  # Cria a role
        db.session.add(role)
        db.session.commit()  # Commit após criar a role para garantir que seja persistida

        # Agora, associa as permissões à role
        for permission in body.permissions:
            # Verificar se a permissão já existe
            permission_obj = Permission.query.filter_by(nome=permission.nome).first()
            
            if not permission_obj:
                permission_obj = Permission(nome=permission.nome)
                db.session.add(permission_obj)

            role.permissions.append(permission_obj)

        db.session.commit()  # Commit após associar as permissões
        print(f"Role '{body.nome}' criada com sucesso!")  # Log de sucesso

        # Serializa as permissões associadas à role
        role_permissions_serialized = [
            {"id": p.id, "nome": p.nome} for p in role.permissions
        ]

        return jsonify({
            "message": "Role criada com sucesso",
            "role": body.nome,
            "permissions": role_permissions_serialized
        }), 201

    except Exception as e:
        print(f"Erro ao tentar criar role superadmin: {e}")
        return jsonify({"erro": "Erro ao criar role"}), 500



def login_superadmin(dados: dict):
    try:
        body = UserCreate.parse_obj(dados)  # Cria o objeto UserCreate
        nome = body.nome
        senha = body.senha

        usuario = UsuarioModel.busca_nome(nome)  # Busca o usuário pelo nome
        if usuario and check_password_hash(usuario.senha, senha):  # Verifica a senha
            role = Role.query.get(usuario.role_id)

            # Cria o token de acesso
            identity = {"id": usuario.id, "role": role.nome}
            token = create_access_token(identity=identity)
            return jsonify(acesstoken=token), 200
        return jsonify(erro="Nome do usuario ou senha invalidos."), 401
    except Exception as e:
        print(f"Erro no login: {e}")
        return jsonify({"erro": "Erro ao fazer login"}), 500


def criar_tudo():
    try:
        # Registrar permissões e roles
        registrar_permissions_superadmin({
            "nome": "PoderAdemiro"
        })
        
        registrar_role_superadmin({
            "nome": "superadmin",
            "permissions": [
                {"nome": "PoderAdemiro"}
            ]
        })
    except Exception as e:
        print(f"Erro ao tentar criar tudo: {e}")

