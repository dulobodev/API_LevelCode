from schemas.CursosSchema import CourseResponse
from flask import jsonify
from config.Database import db, Curso

class CursoModel:
    @staticmethod
    def criar_curso(curso):
        try:
            db.session.add(curso)
            db.session.commit()

            response = CourseResponse.from_orm(curso)
            return jsonify(message ="Curso criado com sucesso", curso_response=response), 201
        except:
            return jsonify(erro = "Erro ao tentar criar um Curso,     FAÇA O L"), 400

    @staticmethod
    def busca_nome(titulo):
        curso = Curso.query.filter_by(titulo=titulo).first()

        if curso:
            return jsonify(message ="Curso:", dados =curso), 200
        else:
            return jsonify(message ="Curso nao encontrado"), 400
        
    @staticmethod
    def get_curso():
        curso = db.session.query(Curso).all()

        if curso:
            return jsonify(message ="Curso:", dados =curso), 200
        else:
            return jsonify(message ="Curso nao encontrado"), 400