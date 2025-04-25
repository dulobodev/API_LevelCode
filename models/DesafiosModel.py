from schemas.DesafiosSchema import ChallengeCreate, ChallengeResponse
from flask import jsonify
from config.Database import db, Desafio

class UsuarioModel:
    @staticmethod
    def criar_usuario(body: ChallengeCreate):
        novo_desafio = Desafio(**body.dict())

        db.session.add(novo_desafio)
        db.session.commit()

        response = ChallengeResponse.from_orm(novo_desafio)
        return jsonify(message ='Desafio criado com sucesso!', desafio =response.dict()), 201

    @staticmethod
    def busca_nome(nome):
        desafio = Desafio.query.filter_by(nome=nome).first()
        
        if desafio:
            return jsonify(message ="desafio:", dados =desafio), 200
        else:
            return jsonify(message ="desafio nao encontrado"), 400
        
    @staticmethod
    def busca_id(id):
        desafio = Desafio.query.get(id)

        if desafio:
            return jsonify(message ="desafio:", dados =desafio), 200
        else:
            return jsonify(message ="desafio nao encontrado"), 400