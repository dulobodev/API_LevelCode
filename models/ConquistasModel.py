from config.Database import db
from models.model import Conquista, UsuarioConquista


class ConquistaModel:
    @staticmethod
    def busca_nome(nome):
        return Conquista.query.filter_by(nome=nome).first()
    
    def verifica_conquista(usuario_id):
        return UsuarioConquista.query.filter_by(usuario_id=usuario_id).first()

    @staticmethod
    def get_conquista():
        return db.session.query(Conquista).all()
    