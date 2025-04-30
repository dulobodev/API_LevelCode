from models.ConquistasModel import ConquistaModel
from models.model import Conquista
from models.model import UsuarioConquista
from schemas.ConquistaSchema import ConquestCreate, UserConquestBase
from flask import jsonify, request
from config.Database import db

class ConquistaController:
    """
    Controlador responsável pelas operações relacionadas às conquistas.
    """

    @staticmethod
    def registrar_conquista():
        """
        Registra uma nova conquista no sistema.

        Passos:
        - Valida os dados de entrada via schema `ConquestCreate`.
        - Verifica se já existe uma conquista com o mesmo nome.
        - Cria a nova conquista e persiste no banco de dados.

        Returns:
            JSON: Mensagem de sucesso ou erro detalhado.
        """
        try:
            # Valida os dados recebidos no corpo da requisição
            body = ConquestCreate(**request.get_json())

            # Verifica se já existe uma conquista com o mesmo nome
            if ConquistaModel.busca_nome(body.nome):
                return jsonify({"error": "Conquista já existente"}), 422

            # Cria uma instância de conquista com os dados recebidos
            conquista = Conquista(
                nome=body.nome,
                criterios=body.criterios
            )

            # Adiciona a conquista ao banco de dados
            db.session.add(conquista)
            db.session.commit()

            return jsonify({"message": "Conquista criada com sucesso", "conquista_id": conquista.id}), 201

        except Exception as e:
            # Em caso de erro, imprime o erro e retorna uma resposta de erro
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar conquista", details=str(e)), 500
    
    @staticmethod
    def adicionar_conquista():
        """
        Adiciona uma conquista a um usuário.

        Passos:
        - Valida os dados de entrada via schema `UserConquestBase`.
        - Verifica se o usuário já possui essa conquista.
        - Associa a conquista ao usuário e persiste no banco de dados.

        Returns:
            JSON: Mensagem de sucesso ou erro detalhado.
        """
        try:
            # Valida os dados recebidos no corpo da requisição
            body = UserConquestBase(**request.get_json())

            # Verifica se o usuário já possui a conquista
            if ConquistaModel.verifica_conquista(body.usuario_id):
                return jsonify({"error": "Essa conquista já pertence a esse usuário"}), 422
            
            # Cria a associação entre o usuário e a conquista
            add_conquista = UsuarioConquista(
                usuario_id=body.usuario_id,
                conquista_id=body.conquista_id
            )

            # Adiciona a associação ao banco de dados
            db.session.add(add_conquista)
            db.session.commit()

            # Retorna a resposta de sucesso
            return jsonify({"message": "Esse usuário já possui essa conquista", "user_conquista": add_conquista}), 201

        except Exception as e:
            # Em caso de erro, imprime o erro e retorna uma resposta de erro
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar adicionar conquista", details=str(e)), 500
