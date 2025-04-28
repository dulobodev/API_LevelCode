from models.ConquistasModel import ConquistaModel
from schemas.ConquistaSchema import ConquestCreate, UserConquestBase
from flask import jsonify


class ConquistaController:

    @staticmethod
    def registrar_conquista(dados: ConquestCreate):
        nome = dados.nome
        criterio = dados.criterio

        if ConquistaModel.busca_nome(nome):
            return jsonify(erro ="Já existe uma conquista com esse nome."), 422
        ConquistaModel.criar_modulo(nome, criterio)




