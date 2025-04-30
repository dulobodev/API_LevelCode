from models.CursoModel import CursoModel
from models.model import Curso, Modulo
from schemas.CursosSchema import CourseCreate
from flask import jsonify, request
from config.Database import db

class CursoController:

    @staticmethod
    def registrar_curso():
        try:
            body = CourseCreate(**request.get_json())
        
            curso = Curso(
                titulo=body.titulo,
                descricao=body.descricao,
                dificuldade=body.dificuldade,
                xp_total=body.xp_total
            )

            if CursoModel.busca_nome(curso.titulo):
                    return jsonify(erro ="Já existe um curso com esse titulo."), 422

            db.session.add(curso)
        
            for modulo in body.modulos:
                existing_perm = Modulo.query.filter_by(nome=modulo.nome).first()
                if existing_perm:
                    curso.modulos.append(existing_perm)
                else:
                    novo_modulo = Modulo(nome=modulo.nome)
                    db.session.add(novo_modulo)
                    curso.modulos.append(novo_modulo)
            db.session.commit()
            return jsonify(message="Curso criado com sucesso", curso =curso.id), 201
                
        except Exception as e:
            db.session.rollback()
            print("Erro:", e)
            return jsonify(erro="Erro ao tentar criar um Curso"), 400

    