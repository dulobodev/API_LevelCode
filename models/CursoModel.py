from schemas.CursosSchema import CourseCreate, CourseResponse
from flask import jsonify, request
from config.Database import db, Curso, Modulo

class CursoModel:
    @staticmethod
    def criar_curso():
        try:
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
    def busca_id(id):
        curso = Curso.query.get(id)

        if curso:
            return jsonify(message ="Curso:", dados =curso), 200
        else:
            return jsonify(message ="Curso nao encontrado"), 400