from models.AulaModel import AulaModel
from schemas.AulaSchema import ClassCreate
from flask import jsonify


class AulaController:

    @staticmethod
    def registrar_aula(dados: ClassCreate):
        titulo = dados.titulo
        conteudo = dados.conteudo
        modulo_id = dados.modulo_id
        xp = dados.xp

        if AulaModel.busca_nome(titulo):
            return jsonify(erro ="Já existe uma aula com esse titulo."), 422
        AulaModel.criar_modulo(titulo, conteudo, modulo_id, xp)


