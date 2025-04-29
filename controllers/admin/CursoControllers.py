from models.CursoModel import CursoModel
from config.Database import Modulo, Curso, db
from schemas.CursosSchema import CourseCreate
from flask import jsonify, request


class CursoController:

    @staticmethod
    def registrar_curso():
        body = CourseCreate(**request.get_json())

        curso = Curso(
            titulo=body.titulo,
            descricao=body.descricao,
            dificuldade=body.dificuldade,
            xp_total=body.xp_total
        )
            
        for modulo in body.modulos:
            existing_perm = Modulo.query.filter_by(nome=modulo.nome).first()
            if existing_perm:
                curso.modulos.append(existing_perm)
            else:
                modulo_obj = Modulo(nome=modulo.nome, curso=curso)
                db.session.add(modulo_obj)
                curso.modulos.append(existing_perm)

        if CursoModel.busca_nome(curso.titulo):
            return jsonify(erro ="Já existe um curso com esse titulo."), 422
        return CursoModel.criar_curso(curso)

    