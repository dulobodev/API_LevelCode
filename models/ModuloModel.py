from schemas.ModuloSchema import ModuleCreate, ModuleResponse
from flask import jsonify
from config.Database import db, Modulo

class RankingModel:
    @staticmethod
    def criar_ranking(body: ModuleCreate):
        novo_modulo = Modulo(**body.dict())

        db.session.add(novo_modulo)
        db.session.commit()

        response = ModuleResponse.from_orm(novo_modulo)
        return jsonify(message ='Ranking criado com sucesso!', ranking =response.dict()), 201

    @staticmethod
    def busca_nome(nome):
        modulo = Modulo.query.filter_by(nome=nome).first()
        
        if modulo:
            return jsonify(message ="Ranking:", dados =modulo), 200
        else:
            return jsonify(message ="Ranking nao encontrado"), 400
        
    @staticmethod
    def busca_id(id):
        modulo = Modulo.query.get(id)

        if modulo:
            return jsonify(message ="Ranking:", dados =modulo), 200
        else:
            return jsonify(message ="Ranking nao encontrado"), 400