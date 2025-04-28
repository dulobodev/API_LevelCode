from models.DesafiosModel import DesafioModel
from schemas.DesafiosSchema import ChallengeCreate
from flask import jsonify


class DesafioController:

    @staticmethod
    def registrar_desafio(dados: ChallengeCreate):
        nome = dados.nome
        desafio = dados.desafio
        requisitos = dados.requisitos
        resultado = dados.resultado
        xp = dados.xp

        if DesafioModel.busca_nome(nome):
            return jsonify(erro ="Já existe um Desafio com esse nome."), 422
        DesafioModel.criar_modulo(nome, desafio, requisitos, resultado, xp)



