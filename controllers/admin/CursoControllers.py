from models.CursoModel import CursoModel
from config.Database import Modulo, Curso, db
from schemas.CursosSchema import CourseCreate
from flask import jsonify, request


class CursoController:

    @staticmethod
    def registrar_curso():
        body = CourseCreate.parse_obj(request.json)

        curso = Curso(
            titulo=body.titulo,
            descricao=body.descricao,
            dificuldade=body.dificuldade,
            xp_total=body.xp_total
        )

        for modulo in body.modulos:
            modulo_obj = Modulo(nome=modulo.nome, curso=curso)
            db.session.add(modulo_obj)

        if CursoModel.busca_nome(curso.titulo):
            return jsonify(erro ="Já existe um curso com esse titulo."), 422
        CursoModel.criar_curso(curso)
