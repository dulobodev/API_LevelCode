from config.Database import db
from models.model import Aula

class AulaModel:

    @staticmethod
    def busca_nome(titulo):
        return Aula.query.filter_by(titulo=titulo).first()
        
        
    @staticmethod
    def get_aula():
        return db.session.query(Aula).all()