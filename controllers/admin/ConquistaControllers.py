from models.ConquistasModel import ConquistaModel
from models.model import Conquista
from models.model import UsuarioConquista
from schemas.ConquistaSchema import ConquestCreate, UserConquestBase
from flask import jsonify, request
from config.Database import db


class ConquistaController:

    @staticmethod
    def registrar_conquista():
        try:
            body = ConquestCreate(**request.get_json())
            
            if ConquistaModel.busca_nome(body.nome):
                return jsonify({"error": "Conquista já existente"}), 422

            conquista = Conquista(
            nome = body.nome,
            criterios = body.criterios
            )

            db.session.add(conquista)
            db.session.commit()
            return jsonify({"message": "Conquista criada com sucesso", "conquista_id": conquista.id}), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar conquista", details=str(e)), 500
    
    @staticmethod
    def adicionar_conquista():
        try:
            body = UserConquestBase(**request.get_json())

            if ConquistaModel.verifica_conquista(body.usuario_id):
                return jsonify({"error": "Essa conquista ja pertence a esse usuario"}), 422
            
            add_conquista = UsuarioConquista(
                usuario_id = body.usuario_id,
                conquista_id = body.conquista_id
            )
            
            user_conquista = ConquistaModel.verifica_conquista(body.usuario_id)

            db.session.add(add_conquista)
            db.session.commit()
            return jsonify({"message": "Esse usuario ja possui essa conquista", "user_conquista": user_conquista}), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar conquista", details=str(e)), 500



