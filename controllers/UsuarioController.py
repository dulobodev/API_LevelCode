import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models.UsuarioModel import UsuarioModel, UserCreate
from flask import jsonify

def senha_forte(senha):
    return (len(senha) >= 8 and
            re.search(r"[A-Z]", senha) and
            re.search(r"[a-z]", senha) and
            re.search(r"[0-9]", senha) and
            re.search(r"[@#$%^&*(),.?\":{}|<>]", senha))

def registrar_usuario(dados: UserCreate):
    nome = dados.nome
    email = dados.email
    senha_hash = dados.senha_hash

    if not senha_forte(senha_hash):
        return jsonify(erro ="A senha deve conter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais."), 400
    if UsuarioModel.busca_email(email):
        return {"error": "E-mail já cadastrado"}, 400
    
    senha_hash = generate_password_hash(senha_hash)
    UsuarioModel.criar_usuario(nome, senha_hash, email)

def login(dados: UserCreate):
    nome = dados.nome
    senha= dados.senha_hash

    usuario = UsuarioModel.busca_nome(nome)
    if usuario and check_password_hash(usuario['senha_hash'], senha):
        token = create_access_token(identity=str(usuario['id']))
        return {"access_token": token}, 200
    return {"error": "Nome de usuário ou senha inválidos"}, 401

