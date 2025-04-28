from schemas.ProgressoSchema import ProgressBase
from flask import jsonify
from config.Database import db, Progresso

class UsuarioModel:
    @staticmethod
    def consulta_progresso(id):
        progresso = Progresso.query.get(id)

        if progresso:
            return jsonify(message ="Seu progresso atualmente e esse:", dados =progresso), 200
        else:
            return jsonify(message ="Usuario nao encontrado"), 400