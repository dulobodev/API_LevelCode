from models.AulaModel import ClassCreate, AulaModel
from flask import jsonify

def registrar_usuario(dados: ClassCreate):
    titulo = dados.titulo
    conteudo = dados.conteudo
    modulo_id = dados.modulo_id
    xp = dados.xp

    if AulaModel.busca_nome(titulo):
        return jsonify(erro ="Já existe uma aula com esse titulo.")
    AulaModel.criar_modulo(titulo, conteudo, modulo_id, xp)


