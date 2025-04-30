from models.CursoModel import CursoModel
from models.model import Curso, Modulo
from schemas.CursosSchema import CourseCreate
from flask import jsonify, request
from config.Database import db

class CursoController:
    """
    Controlador responsável pelas operações relacionadas ao curso.
    """

    @staticmethod
    def registrar_curso():
        """
        Registra um novo curso no sistema.

        Passos:
        - Valida os dados de entrada via schema `CourseCreate`.
        - Verifica se já existe um curso com o mesmo título.
        - Cria o curso e associa os módulos (existentes ou novos).
        - Persiste no banco de dados.

        Returns:
            JSON: Mensagem de sucesso ou erro detalhado.
        """
        try:
            # Valida os dados recebidos no corpo da requisição
            body = CourseCreate(**request.get_json())

            # Cria uma instância do curso com os dados recebidos
            curso = Curso(
                titulo=body.titulo,
                descricao=body.descricao,
                dificuldade=body.dificuldade,
                xp_total=body.xp_total
            )

            # Verifica se já existe um curso com o mesmo título
            if CursoModel.busca_nome(curso.titulo):
                return jsonify(erro="Já existe um curso com esse título."), 422

            # Adiciona o curso ao banco de dados
            db.session.add(curso)

            # Para cada módulo recebido, verifica se já existe ou cria um novo
            for modulo in body.modulos:
                existing_modulo = Modulo.query.filter_by(nome=modulo.nome).first()
                if existing_modulo:
                    curso.modulos.append(existing_modulo)
                else:
                    novo_modulo = Modulo(nome=modulo.nome)
                    db.session.add(novo_modulo)
                    curso.modulos.append(novo_modulo)

            # Confirma as alterações no banco
            db.session.commit()

            return jsonify(message="Curso criado com sucesso", curso=curso.id), 201

        except Exception as e:
            db.session.rollback()  # Reverte alterações no banco em caso de erro
            print("Erro:", e)
            return jsonify(erro="Erro ao tentar criar um Curso", details=str(e)), 400
