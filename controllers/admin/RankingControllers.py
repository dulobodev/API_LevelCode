from models.RankingModel import RankingModel
from schemas.RankingSchema import RankingCreate
from flask import jsonify


class RankingControllers:

    @staticmethod
    def registrar_ranking(dados: RankingCreate):
        nome = dados.nome
        privilegios = dados.privilegios
        requisitos = dados.requisitos
        created_date = dados.created_date

        if RankingModel.busca_nome(nome):
            return jsonify(erro ="Já existe um Rank com esse nome."), 422
        RankingModel.criar_modulo(nome, privilegios, requisitos, created_date)


