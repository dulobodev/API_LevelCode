from config.Database import db
from models.model import Desafio

class DesafioModel:
    """
    Classe responsável por realizar operações de acesso ao banco de dados relacionadas ao modelo 'Desafio'.
    """

    @staticmethod
    def busca_nome(nome):
        """
        Busca um desafio pelo nome fornecido.

        Args:
            nome (str): O nome do desafio a ser buscado.

        Returns:
            Desafio: Objeto Desafio correspondente ao nome, ou None se não encontrado.
        """
        return Desafio.query.filter_by(nome=nome).first()
        
    @staticmethod
    def get_desafio():
        """
        Retorna todos os desafios cadastrados no banco de dados.

        Returns:
            list[Desafio]: Lista com todos os objetos Desafio encontrados.
        """
        return db.session.query(Desafio).all()
