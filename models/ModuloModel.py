from config.Database import db
from models.model import Modulo

class ModuloModel:
    @staticmethod
    def busca_nome(nome):
        return Modulo.query.filter_by(nome=nome).first()
        
        
    @staticmethod
    def get_modulo():
        return db.session.query(Modulo).all()