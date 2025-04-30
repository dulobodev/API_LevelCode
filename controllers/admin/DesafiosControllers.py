from models.DesafiosModel import DesafioModel
from models.model import Desafio
from schemas.DesafiosSchema import ChallengeCreate
from flask import jsonify, request
from config.Database import db


class DesafioController:

    @staticmethod
    def registrar_desafio():
        try:
            body = ChallengeCreate(**request.get_json())

            if DesafioModel.busca_nome(body.nome):
                return jsonify({"error": "Esse desafio já existe"}), 422

            desafio = Desafio(
            nome = body.nome,
            descricao = body.descricao,
            requisitos = body.requisitos,
            resultado = body.resultado,
            xp = body.xp
            )

            db.session.add(desafio)
            db.session.commit()
            return jsonify({"message": "Desafio criado com sucesso", "desafio_id": desafio.id}), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar desafio", details=str(e)), 500
        



