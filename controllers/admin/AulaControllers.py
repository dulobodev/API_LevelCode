from models.AulaModel import AulaModel
from models.model import Aula
from schemas.AulaSchema import ClassCreate
from flask import jsonify, request
from config.Database import db


class AulaController:

    @staticmethod
    def registrar_aula():
        try:
            body = ClassCreate(**request.get_json())

            if AulaModel.busca_nome(body.titulo):
                return jsonify({"error": "Essa aula já existe"}), 422

            aula = Aula(
                titulo = body.titulo,
                conteudo = body.conteudo,
                modulo_id = body.modulo_id,
                xp = body.xp

                )
            
            db.session.add(aula)
            db.session.commit()
            return jsonify({"message": "Aula criada com sucesso", "aula_id": aula.id}), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar aula", details=str(e)), 500


