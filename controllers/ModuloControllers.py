from models.ModuloModel import ModuloModel, ModuleCreate
from flask import jsonify

def registrar_usuario(dados: ModuleCreate):
    nome = dados.nome
    curso_id = dados.curso_id

    if ModuloModel.busca_nome(nome):
        return jsonify(erro ="Já existe um módulo com esse nome.")
    ModuloModel.criar_modulo(nome, curso_id)