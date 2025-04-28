from schemas.DesafiosSchema import ChallengeCreate, ChallengeResponse
from flask import jsonify
from config.Database import db, Desafio

class DesafioModel:
    @staticmethod
    def criar_desafio(body: ChallengeCreate):
        novo_desafio = Desafio(**body.dict())
        try:
            db.session.add(novo_desafio)
            db.session.commit()

            response = ChallengeResponse.from_orm(novo_desafio)
            return jsonify(message ='Desafio criado com sucesso!', desafio =response.dict()), 201
        except:
            return jsonify(erro = "Erro ao tentar criar um Desafio,     FAÇA O L"), 400

    @staticmethod
    def busca_nome(nome):
        desafio = Desafio.query.filter_by(nome=nome).first()
        
        if desafio:
            return jsonify(message ="desafio:", dados =desafio), 200
        else:
            return jsonify(message ="desafio nao encontrado"), 400
        
    @staticmethod
    def get_desafio():
        desafio = db.session.query(Desafio).all()

        if desafio:
            return jsonify(message ="desafio:", dados =desafio), 200
        else:
            return jsonify(message ="desafio nao encontrado"), 400