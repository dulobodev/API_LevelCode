from config.Database import db
from  models.model import Desafio

class DesafioModel:
    @staticmethod
    def busca_nome(nome):
        return Desafio.query.filter_by(nome=nome).first()
        
    @staticmethod
    def get_desafio():
        return db.session.query(Desafio).all()