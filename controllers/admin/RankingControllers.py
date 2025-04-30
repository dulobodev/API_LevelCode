from models.RankingModel import RankingModel
from models.model import Ranking
from schemas.RankingSchema import RankingCreate
from flask import jsonify, request
from config.Database import db

class RankingControllers:
    """
    Controlador responsável pelas operações relacionadas ao modelo de Ranking,
    como criação e verificação de rankings existentes.
    """

    @staticmethod
    def registrar_ranking():
        """
        Registra um novo ranking no sistema.
        
        Valida se já existe um ranking com o mesmo nome.
        Se não existir, cria um novo com os dados fornecidos (nome, privilégios, requisitos)
        e salva no banco de dados.

        Returns:
            JSON: Mensagem de sucesso com o ID do ranking ou erro com status apropriado.
        """
        try:
            # Valida os dados recebidos com o schema
            body = RankingCreate(**request.get_json())

            # Verifica se já existe um ranking com o mesmo nome
            if RankingModel.busca_nome(body.nome):
                return jsonify({"error": "Esse Ranking já existe"}), 422

            # Criação do novo ranking
            ranking = Ranking(
                nome=body.nome,
                privilegios=body.privilegios,
                requisitos=body.requisitos,
            )

            # Adiciona e confirma no banco de dados
            db.session.add(ranking)
            db.session.commit()

            return jsonify({
                "message": "Ranking criado com sucesso",
                "ranking_id": ranking.id
            }), 201

        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar ranking", details=str(e)), 500
