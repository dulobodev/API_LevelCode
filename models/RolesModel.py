from config.Database import db
from models.model import Role, Permission

class RoleModel:
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
