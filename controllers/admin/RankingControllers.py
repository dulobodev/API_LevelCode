from models.RankingModel import RankingModel
from models.model import Ranking
from schemas.RankingSchema import RankingCreate
from flask import jsonify, request
from config.Database import db


class RankingControllers:

    @staticmethod
    def registrar_ranking():
        try:
            body = RankingCreate(**request.get_json())

            if RankingModel.busca_nome(body.nome):
                return jsonify({"error": "Esse Ranking já existe"}), 422

            ranking = Ranking(
            nome = body.nome,
            privilegios = body.privilegios,
            requisitos = body.requisitos,
            )

            db.session.add(ranking)
            db.session.commit()
            return jsonify({"message": "Ranking criada com sucesso", "ranking_id": ranking.id}), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar ranking", details=str(e)), 500


