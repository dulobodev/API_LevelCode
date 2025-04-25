from schemas.UsuarioSchema import UserCreate, UserResponse
from flask import jsonify
from config.Database import db, Usuario

class UsuarioModel:
    @staticmethod
    def criar_usuario(body: UserCreate):
        novo_usuario = Usuario(**body.dict())

        db.session.add(novo_usuario)
        db.session.commit()

        response = UserResponse.from_orm(novo_usuario)
        return jsonify(message ='Usuario criado com sucesso!', usuario =response.dict()), 201

    @staticmethod
    def busca_nome(nome):
        usuario = Usuario.query.filter_by(nome=nome).first()
        
        if usuario:
            return jsonify(message ="Usuario:", dados =usuario), 200
        else:
            return jsonify(message ="Usuario nao encontrado"), 400
        
    @staticmethod
    def busca_id(id):
        usuario = Usuario.query.get(id)

        if usuario:
            return jsonify(message ="Usuario:", dados =usuario), 200
        else:
            return jsonify(message ="Usuario nao encontrado"), 400