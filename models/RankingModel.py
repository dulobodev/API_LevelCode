from schemas.RankingSchema import RankingCreate, RankingResponse
from flask import jsonify
from config.Database import db, Ranking

class RankingModel:
    @staticmethod
    def criar_ranking(body: RankingCreate):
        novo_ranking = Ranking(**body.dict())

        db.session.add(novo_ranking)
        db.session.commit()

        response = RankingResponse.from_orm(novo_ranking)
        return jsonify(message ='Ranking criado com sucesso!', ranking =response.dict()), 201

    @staticmethod
    def busca_nome(nome):
        ranking = Ranking.query.filter_by(nome=nome).first()
        
        if ranking:
            return jsonify(message ="Ranking:", dados =ranking), 200
        else:
            return jsonify(message ="Ranking nao encontrado"), 400
        
    @staticmethod
    def busca_id(id):
        ranking = Ranking.query.get(id)

        if ranking:
            return jsonify(message ="Ranking:", dados =ranking), 200
        else:
            return jsonify(message ="Ranking nao encontrado"), 400