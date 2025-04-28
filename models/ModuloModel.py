from schemas.ModuloSchema import ModuleCreate, ModuleResponse
from flask import jsonify
from config.Database import db, Modulo

class ModuloModel:
    @staticmethod
    def criar_modulo(body: ModuleCreate):
        novo_modulo = Modulo(**body.dict())
        
        try:
            db.session.add(novo_modulo)
            db.session.commit()

            response = ModuleResponse.from_orm(novo_modulo)
            return jsonify(message ='Modulo criado com sucesso!', modulo =response.dict()), 201
        except:
            return jsonify(erro = "Erro ao tentar criar um Modulo,     FAÇA O L"), 400

    @staticmethod
    def busca_nome(nome):
        modulo = Modulo.query.filter_by(nome=nome).first()
        
        if modulo:
            return jsonify(message ="Modulo", dados =modulo), 200
        else:
            return jsonify(message ="Modulo nao encontrado"), 400
        
    @staticmethod
    def get_modulo():
        modulo = db.session.query(Modulo).all()

        if modulo:
            return jsonify(message ="Modulo:", dados =modulo), 200
        else:
            return jsonify(message ="Modulo nao encontrado"), 400