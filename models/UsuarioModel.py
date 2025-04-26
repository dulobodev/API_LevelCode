from schemas.UsuarioSchema import UserCreate, UserResponse
from flask import jsonify
from config.Database import db, Usuario

class UsuarioModel:
    @staticmethod
    def criar_usuario(body: UserCreate):
        novo_usuario = Usuario(**body.dict())
        try:
            db.session.add(novo_usuario)
            db.session.commit()

            response = UserResponse.from_orm(novo_usuario)
            return jsonify(message ='Usuario criado com sucesso!', usuario =response.dict()), 201
        except:
            return jsonify(erro = "Erro ao tentar criar um Usuario,     FAÇA O L"), 400

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
        
    @staticmethod
    def busca_email(email):
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario:
            return jsonify(message ="Usuario:", dados =usuario), 200
        else:
            return jsonify(message ="Usuario nao encontrado"), 400