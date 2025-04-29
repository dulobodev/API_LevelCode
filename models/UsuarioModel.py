from schemas.UsuarioSchema import UserCreate, UserResponse
from flask import jsonify
from config.Database import db, Usuario

class UsuarioModel:
    @staticmethod
    def criar_usuario(novo_usuario):
        try:
            db.session.add(novo_usuario)
            db.session.commit()

            response = UserResponse.from_orm(novo_usuario)
            return jsonify(message='Usuário criado com sucesso!', usuario=response.dict()), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(erro="Erro ao tentar criar um usuário"), 400

    @staticmethod
    def busca_nome(nome):
        return Usuario.query.filter_by(nome=nome).first()

        
    @staticmethod
    def busca_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def busca_email(email):
        return Usuario.query.filter_by(email=email).first()
