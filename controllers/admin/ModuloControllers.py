from models.ModuloModel import ModuloModel
from schemas.ModuloSchema import ModuleCreate
from config.Database import Modulo, db
from flask import jsonify, request


class ModuloControllers:

    @staticmethod
    def registrar_modulo(dados: ModuleCreate):
        try:
            body = Modulo(**request.get_json())
            if ModuloModel.busca_nome(body.nome):
                return jsonify(erro ="Já existe um módulo com esse nome."), 422
            
            modulo = Modulo(nome=body.nome)
            db.session.add(modulo)
            db.session.commit()

            db.session.commit()
            return jsonify({"message": "Modulo criada com sucesso", "modulo": modulo.id}), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar modulo", details=str(e)), 500