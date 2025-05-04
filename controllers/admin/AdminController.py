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

# Função que valida a força da senha
def senha_forte(senha):
    """'
    Verifica se a senha possui pelo menos 8 caracteres, 
    incluindo letras maiúsculas, minúsculas, números e caracteres especiais.
    
    Args:
        senha (str): A senha a ser verificada.

    Returns:
        bool: True se a senha for forte, caso contrário False.
    """
    return (len(senha) >= 8 and
            re.search(r"[A-Z]", senha) and
            re.search(r"[a-z]", senha) and
            re.search(r"[0-9]", senha) and
            re.search(r"[@#$%^&*(),.?\":{}|<>]", senha))

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class AdminController:
    """
    Controlador responsável pelas operações administrativas, incluindo criação de permissões, 
    roles (funções), administração de usuários (administradores) e login.
    """

    @staticmethod
    def registrar_permissions(body: PermissionCreate):
        """
        Registra uma nova permissão no sistema.
        
        Args:
            body (PermissionCreate): Dados da permissão a ser criada.

        Returns:
            JSON: Resposta de sucesso ou erro.
        """
        # Verifica se já existe uma permissão com o mesmo nome
        nova_permission = Permission(**body)
        if Permission.query.filter_by(nome=nova_permission.nome).first():
            return jsonify({"erro" : "Já existe uma permissão com este nome"}), 409

        try:
            # Adiciona a nova permissão ao banco de dados
            db.session.add(nova_permission)
            db.session.commit()
            return jsonify({"message" : "Permissão criada com sucesso."})
        except:
            return jsonify({"erro" : "Erro ao tentar criar permissão"}), 400

    @staticmethod
    def registrar_role():
        """
        Registra uma nova role (função) no sistema, incluindo a atribuição de permissões a ela.
        
        Returns:
            JSON: Resposta de sucesso ou erro.
        """
        try:
            # Recebe e valida os dados de entrada
            body = RolesCreate(**request.get_json())

            # Verifica se já existe uma role com o mesmo nome
            if RoleModel.busca_role_nome(body.nome):
                return jsonify({"error": "Role já existe"}), 422

            # Cria uma nova role
            role = Role(nome=body.nome)
            db.session.add(role)

            # Associa as permissões à role
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
        """
        Registra um novo administrador no sistema, incluindo validação de senha e associação com roles e rankings.
        
        Returns:
            JSON: Resposta de sucesso ou erro.
        """
        try:
            # Recebe e valida os dados de entrada
            body = UserCreate(**request.get_json())

            # Cria um novo usuário (administrador)
            novo_admin = Usuario(
                nome = body.nome,
                email = body.email,
                senha = body.senha,
                roles_id = body.roles_id,
                ranking_id = body.ranking_id
            )

            # Valida a força da senha
            if not senha_forte(novo_admin.senha):
                return jsonify(erro ="A senha deve conter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais."), 400

            # Verifica se o email já está registrado
            if UsuarioModel.busca_email(novo_admin.email):
                return jsonify(error ="E-mail já cadastrado"), 422

            # Gera o hash da senha
            novo_admin.senha = generate_password_hash(novo_admin.senha)

            # Verifica a existência da role e do ranking
            role = Role.query.get(novo_admin.roles_id)
            if not role:
                return jsonify(erro="Role não encontrada"), 404
            
            ranking = Ranking.query.get(novo_admin.ranking_id)
            if not ranking:
                return jsonify(erro="Ranking não encontrado"), 404
        
            # Adiciona o novo administrador ao banco de dados
            db.session.add(novo_admin)
            db.session.commit()
            return jsonify({"message": "Admin criado com sucesso", "user_id": novo_admin.id}), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar um novo admin", details=str(e)), 500

    @staticmethod
    def login_admin():
        """
        Realiza o login do administrador no sistema, retornando um token JWT para autenticação.
        
        Returns:
            JSON: Token de acesso ou erro.
        """
        try:
            # Recebe e valida os dados de entrada
            body = UserLogin(**request.get_json())

            validate = Usuario(
                nome = body.nome,
                senha= body.senha
            )

            # Verifica se o nome e a senha estão corretos
            usuario = UsuarioModel.busca_nome(validate.nome)
            if usuario and check_password_hash(usuario.senha, validate.senha):
                role = Role.query.get(usuario.roles_id)

                # Agora, extrai as permissões do role
                permissoes = [p.nome for p in role.permissions]

                # Cria o token de acesso com as permissões do usuário
                token = create_access_token(identity=str(usuario.id),additional_claims={"role": role.nome,"permissions": permissoes})
                
                return jsonify({"access_token": token}), 200
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Nome do administrador ou senha inválidos", details=str(e)), 401
