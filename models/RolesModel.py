from schemas.RolesSchema import RolesCreate
from flask import jsonify, request
from config.Database import db, Role, Permission

class RoleModel:
    @staticmethod
    def criar_role():
        try:
            body = RolesCreate(**request.get_json())

            if RoleModel.busca_role_nome(body.nome):
                return jsonify({"error": "Role já existe"}), 422

            role = Role(nome=body.nome)
            db.session.add(role)

            for permission in body.permissions:
                existing_perm = Permission.query.filter_by(nome=permission.nome).first()
                if existing_perm:
                    role.permissions.append(existing_perm)
                else:
                    permission_obj = Permission(nome=permission.nome)
                    db.session.add(permission_obj)
                    role.permissions.append(permission_obj)

            db.session.commit()
            return jsonify({"message": "Role criada com sucesso", "role_id": role.id}), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar role", details=str(e)), 500
    

    @staticmethod
    def busca_role_nome(nome):
        return Role.query.filter_by(nome=nome).first()
        
    @staticmethod
    def busca_permission_nome(nome):
        return Permission.query.filter_by(nome=nome).first()
        
    
    @staticmethod
    def busca_id(id):
      return Role.query.get(id)

        
    @staticmethod
    def get():
        return db.session.query(Role).all()
