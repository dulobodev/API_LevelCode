from config.Database import db
from models.model import Ranking

class RankingModel:
    """
    Classe responsável pelas operações relacionadas ao modelo 'Ranking' no banco de dados.
    Oferece métodos para buscar rankings pelo nome e para recuperar todos os rankings cadastrados.
    """
    
    @staticmethod
    def busca_nome(nome):
        """
        Busca um ranking pelo nome.

        Este método faz uma consulta ao banco de dados e retorna o primeiro ranking que corresponde ao nome fornecido.

        Args:
            nome (str): O nome do ranking a ser buscado.

        Returns:
            Ranking | None: Retorna o primeiro ranking encontrado com o nome fornecido, 
            ou None se nenhum ranking com esse nome for encontrado.
        """
        return Ranking.query.filter_by(nome=nome).first()

    @staticmethod
    def get_ranking():
        """
        Recupera todos os rankings cadastrados no banco de dados.

        Este método faz uma consulta ao banco de dados e retorna todos os rankings existentes.

        Returns:
            list: Lista de objetos 'Ranking', contendo todos os rankings cadastrados.
        """
        return db.session.query(Ranking).all()
