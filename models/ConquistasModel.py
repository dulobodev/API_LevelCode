from schemas.ConquistaSchema import ConquestBase, ConquestResponse
from flask import jsonify
from config.Database import db, Conquista

class ConquistaModel:
    @staticmethod
    def criar_conquista(body: ConquestBase, bodyresponse:ConquestResponse):
        nova_conquista = Conquista(**body.dict())

        db.session.add(nova_conquista)
        db.session.commit()

        return jsonify(message = 'Conquista criado com sucesso!', conquista = bodyresponse.dict()), 201

    @staticmethod
    def busca_nome(body: ConquestBase, nome):
        conquista = Conquista.query.filter_by(nome=nome).first()

        if conquista:
            return jsonify(message = "Conquista:", dados = conquista), 200
        else:
            return jsonify(message = "Conquista nao encontrado"), 400
        
    @staticmethod
    def busca_id(body: id):
        conquista = Conquista.query.get(id)

        if conquista:
            return jsonify(message = "Conquista:", dados = conquista), 200
        else:
            return jsonify(message = "Conquista nao encontrado"), 400