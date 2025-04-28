from models.ModuloModel import ModuloModel
from schemas.ModuloSchema import ModuleCreate
from flask import jsonify


class ModuloControllers:

    @staticmethod
    def registrar_modulo(dados: ModuleCreate):
        nome = dados.nome
        curso_id = dados.curso_id

        if ModuloModel.busca_nome(nome):
            return jsonify(erro ="Já existe um módulo com esse nome."), 422
        ModuloModel.criar_modulo(nome, curso_id)