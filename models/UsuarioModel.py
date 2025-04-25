from schemas.UsuarioSchema import UserCreate, UserResponse
from flask import jsonify
from config.Database import db, Usuario

class UsuarioModel:
    @staticmethod
    def criar_usuario(body: UserCreate, bodyresponse:UserResponse):
        novo_usuario = Usuario(**body.dict())

        db.session.add(novo_usuario)
        db.session.commit()

        return jsonify(message = 'Usuario criado com sucesso!', usuario = bodyresponse.dict()), 201

    @staticmethod
    def busca_nome(body: UserCreate, nome):
        usuario = Usuario.query.get(nome)

        if usuario:
            return jsonify(message = "Usuario:", dados = body.dict()), 200
        else:
            return jsonify(message = "Usuario nao encontrado"), 400
        
    @staticmethod
    def busca_id(body: UserCreate, id):
        usuario = Usuario.query.get(id)

        if usuario:
            return jsonify(message = "Usuario:", dados = body.dict()), 200
        else:
            return jsonify(message = "Usuario nao encontrado"), 400