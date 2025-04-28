from schemas.RolesSchema import RolesCreate
from flask import jsonify
from config.Database import db, Role, Permission

class RoleModel:
    @staticmethod
    def criar_role(body: RolesCreate):
        novo_role = Role(**body.dict())
        
        try:
            db.session.add(novo_role)
            db.session.commit()

            return jsonify(message ='Ranking criado com sucesso!', ranking =novo_role), 201
        except:
            return jsonify(erro = "Erro ao tentar criar um Ranking,     FAÇA O L"), 400
    

    @staticmethod
    def busca_role_nome(nome):
        return Role.query.filter_by(nome=nome).first()
        
    @staticmethod
    def busca_permission_nome(nome):
        return Permission.query.filter_by(nome=nome).first()
        
    
    @staticmethod
    def busca_id(id):
        role = Role.query.get(id)

        if role:
            return jsonify(message ="Role:", dados =role), 200
        else:
            return jsonify(message ="Role nao encontrado"), 400
        
    @staticmethod
    def get():
        role = db.session.query(Role).all()

        if role:
            return jsonify(message ="role:", dados =role), 200
        else:
            return jsonify(message ="role nao encontrado"), 400