from config.Database import db
from models.model import Curso

class CursoModel:
    @staticmethod
    def busca_nome(titulo):
        return Curso.query.filter_by(titulo=titulo).first()
        
    @staticmethod
    def get_curso():
        return db.session.query(Curso).all()