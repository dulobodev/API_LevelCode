from models.AulaModel import AulaModel
from models.model import Aula
from schemas.AulaSchema import ClassCreate
from flask import jsonify, request
from config.Database import db

class AulaController:
    """
    Controlador responsável pelas operações relacionadas às aulas.
    """

    @staticmethod
    def registrar_aula():
        """
        Registra uma nova aula no sistema.

        Passos:
        - Valida os dados de entrada via schema `ClassCreate`.
        - Verifica se já existe uma aula com o mesmo título.
        - Cria a nova aula e persiste no banco de dados.

        Returns:
            JSON: Mensagem de sucesso ou erro detalhado.
        """
        try:
            # Valida os dados recebidos no corpo da requisição
            body = ClassCreate(**request.get_json())

            # Verifica se já existe uma aula com o mesmo título
            if AulaModel.busca_nome(body.titulo):
                return jsonify({"error": "Essa aula já existe"}), 422

            # Cria uma instância de aula com os dados recebidos
            aula = Aula(
                titulo=body.titulo,
                conteudo=body.conteudo,
                modulo_id=body.modulo_id,
                xp=body.xp
            )

            # Adiciona a aula ao banco de dados
            db.session.add(aula)
            db.session.commit()

            return jsonify({"message": "Aula criada com sucesso", "aula_id": aula.id}), 201

        except Exception as e:
            # Em caso de erro, imprime o erro e retorna uma resposta de erro
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar aula", details=str(e)), 500
