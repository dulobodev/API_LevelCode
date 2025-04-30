from models.ModuloModel import ModuloModel
from models.model import Modulo
from schemas.ModuloSchema import ModuleCreate
from config.Database import db
from flask import jsonify, request

class ModuloControllers:
    """
    Controlador responsável pelas operações relacionadas ao modelo de Módulo.
    """

    @staticmethod
    def registrar_modulo():
        """
        Registra um novo módulo no sistema.

        Valida se já existe um módulo com o mesmo nome.
        Se não existir, cria um novo módulo e o salva no banco de dados.

        Returns:
            JSON: Mensagem de sucesso com o ID do módulo ou erro com status apropriado.
        """
        try:
            # Valida os dados recebidos com o schema
            body = ModuleCreate(**request.get_json())

            # Verifica se já existe um módulo com esse nome
            if ModuloModel.busca_nome(body.nome):
                return jsonify(erro="Já existe um módulo com esse nome."), 422

            # Criação do novo módulo
            modulo = Modulo(nome=body.nome)

            # Adiciona e confirma no banco de dados
            db.session.add(modulo)
            db.session.commit()

            return jsonify({
                "message": "Módulo criado com sucesso",
                "modulo": modulo.id
            }), 201

        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar módulo", details=str(e)), 500
