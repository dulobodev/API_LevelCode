import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from schemas.UsuarioSchema import UserCreate
from models.UsuarioModel import UsuarioModel
from config.Database import Role
from flask import jsonify

def senha_forte(senha):
    return (len(senha) >= 8 and
            re.search(r"[A-Z]", senha) and
            re.search(r"[a-z]", senha) and
            re.search(r"[0-9]", senha) and
            re.search(r"[@#$%^&*(),.?\":{}|<>]", senha))

class UsuarioControllers:

    @staticmethod
    def registrar_usuario(dados: UserCreate):
        nome = dados.nome
        email = dados.email
        senha = dados.senha

        if not senha_forte(senha):
            return jsonify(erro ="A senha deve conter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais."), 422
        if UsuarioModel.busca_email(email):
            return {"error": "E-mail já cadastrado"}, 400
        
        senha = generate_password_hash(senha)
        UsuarioModel.criar_usuario(nome, senha, email)

    @staticmethod
    def login(dados: UserCreate):
        nome = dados.nome
        senha= dados.senha

        usuario = UsuarioModel.busca_nome(nome)
        if usuario and check_password_hash(usuario['senha'], senha):
            role = Role.query.get(usuario['role_id'])

            identity = {"id": usuario['id'],"role": role.nome}

            token = create_access_token(identity=identity)
            return {"access_token": token}, 200
        return {"error": "Nome de usuário ou senha inválidos"}, 401

