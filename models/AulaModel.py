from schemas.AulaSchema import ClassCreate, ClassResponse
from flask import jsonify
from config.Database import db, Aula

class AulaModel:
    @staticmethod
    def criar_aula(body: ClassCreate):
        try:
            nova_aula = Aula(**body.dict())

            db.session.add(nova_aula)
            db.session.commit()

            response = ClassResponse.from_orm(nova_aula)
            return jsonify(message ='Aula criada com sucesso!', aula =response.dict()), 201
        except:
            return jsonify(erro = "Erro ao tentar criar uma Conquista,     FAÇA O L"), 400

    @staticmethod
    def busca_nome(titulo):
        aula = Aula.query.filter_by(titulo=titulo).first()
        
        if aula:
            return jsonify(message ="Aula:", dados =aula), 200
        else:
            return jsonify(message ="Aula nao encontrado"), 400
        
    @staticmethod
    def busca_id(id):
        aula = Aula.query.get(id)

        if aula:
            return jsonify(message ="Aula:", dados =aula), 200
        else:
            return jsonify(message ="Aula nao encontrado"), 400