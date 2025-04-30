from config.Database import db
from models.model import Aula

class AulaModel:
    """
    Classe responsável por realizar operações de acesso ao banco de dados relacionadas ao modelo 'Aula'.
    """

    @staticmethod
    def busca_nome(titulo):
        """
        Busca uma instância de Aula com base no título fornecido.

        Args:
            titulo (str): O título da aula a ser buscada.

        Returns:
            Aula: Objeto Aula correspondente ao título, ou None se não encontrado.
        """
        return Aula.query.filter_by(titulo=titulo).first()
        
    @staticmethod
    def get_aula():
        """
        Retorna todas as instâncias de Aula cadastradas no banco de dados.

        Returns:
            list[Aula]: Lista de objetos Aula encontrados.
        """
        return db.session.query(Aula).all()
