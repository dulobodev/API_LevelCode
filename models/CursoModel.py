from schemas.CursosSchema import CourseCreate, CourseResponse
from flask import jsonify, request
from config.Database import db, Curso, Modulo

class CursoModel:
    @staticmethod
    def criar_curso(bodyresponse: CourseResponse):
        body = CourseCreate.parse_obj(request.json)

        # Cria o curso
        curso = Curso(
            titulo=body.titulo,
            descricao=body.descricao,
            dificuldade=body.dificuldade,
            xp_total=body.xp_total
        )

        # Cria os módulos e os associa ao curso
        for modulo in body.modulos:
            modulo_obj = Modulo(nome=modulo.nome, curso=curso)
            db.session.add(modulo_obj)

        db.session.add(curso)
        db.session.commit()

        return jsonify(message = "Curso criado com sucesso", curso_id = bodyresponse.dict()), 201

    @staticmethod
    def busca_nome(body: CourseCreate, nome):
        curso = Curso.query.get(nome)

        if curso:
            return jsonify(message = "Curso:", dados = body.dict()), 200
        else:
            return jsonify(message = "Curso nao encontrado"), 400
        
    @staticmethod
    def busca_id(body: CourseCreate, id):
        curso = Curso.query.get(id)

        if curso:
            return jsonify(message = "Curso:", dados = body.dict()), 200
        else:
            return jsonify(message = "Curso nao encontrado"), 400