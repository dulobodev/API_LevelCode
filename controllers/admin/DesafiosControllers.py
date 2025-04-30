from models.DesafiosModel import DesafioModel
from models.model import Desafio
from schemas.DesafiosSchema import ChallengeCreate
from flask import jsonify, request
from config.Database import db

class DesafioController:
    """
    Controlador responsável pelas operações relacionadas aos Desafios.
    """

    @staticmethod
    def registrar_desafio():
        """
        Registra um novo desafio no sistema.

        Valida se já existe um desafio com o mesmo nome.
        Se não existir, cria um novo desafio com os dados fornecidos
        e o armazena no banco de dados.

        Returns:
            JSON: Mensagem de sucesso com o ID do desafio ou mensagem de erro apropriada.
        """
        try:
            # Valida os dados recebidos com o schema
            body = ChallengeCreate(**request.get_json())

            # Verifica se o desafio já existe pelo nome
            if DesafioModel.busca_nome(body.nome):
                return jsonify({"error": "Esse desafio já existe"}), 422

            # Criação do novo desafio
            desafio = Desafio(
                nome=body.nome,
                descricao=body.descricao,
                requisitos=body.requisitos,
                resultado=body.resultado,
                xp=body.xp
            )

            # Persistência no banco de dados
            db.session.add(desafio)
            db.session.commit()

            return jsonify({
                "message": "Desafio criado com sucesso",
                "desafio_id": desafio.id
            }), 201

        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(
                error="Erro ao tentar criar desafio",
                details=str(e)
            ), 500
