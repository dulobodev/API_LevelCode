from schemas.ModuloSchema import ModuleCreate, ModuleResponse
from flask import jsonify, request
from config.Database import db, Modulo

class ModuloModel:
    @staticmethod
    def criar_modulo():
        try:
            body = Modulo(**request.get_json())
            
            modulo = Modulo(nome=body.nome)
            db.session.add(modulo)
            db.session.commit()

            db.session.commit()
            return jsonify({"message": "Modulo criada com sucesso", "modulo": modulo.id}), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar modulo", details=str(e)), 500

    @staticmethod
    def busca_nome(nome):
        return Modulo.query.filter_by(nome=nome).first()
        
        
    @staticmethod
    def get_modulo():
        modulo = db.session.query(Modulo).all()

        if modulo:
            return jsonify(message ="Modulo:", dados =modulo), 200
        else:
            return jsonify(message ="Modulo nao encontrado"), 400