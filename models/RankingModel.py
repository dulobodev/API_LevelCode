from config.Database import db
from models.model import Ranking

class RankingModel:
    @staticmethod
    def busca_nome(nome):
        return Ranking.query.filter_by(nome=nome).first()

        
    @staticmethod
    def get_ranking():
        return db.session.query(Ranking).all()