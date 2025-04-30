from config.Database import db
from models.model import Usuario

class UsuarioModel:
    @staticmethod
    def busca_nome(nome):
        return Usuario.query.filter_by(nome=nome).first()

        
    @staticmethod
    def busca_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def busca_email(email):
        return Usuario.query.filter_by(email=email).first()
    
    @staticmethod
    def get():
        return db.session.query(Usuario).all()
