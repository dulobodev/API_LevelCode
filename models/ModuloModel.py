from config.Database import db
from models.model import Modulo

class ModuloModel:
    """
    Classe que gerencia as operações relacionadas ao modelo 'Modulo' no banco de dados.
    Contém métodos para buscar módulos por nome e para obter todos os módulos cadastrados.
    """
    
    @staticmethod
    def busca_nome(nome):
        """
        Busca um módulo pelo seu nome.

        Args:
            nome (str): Nome do módulo a ser buscado.

        Returns:
            Modulo | None: Retorna o primeiro módulo encontrado com o nome fornecido ou None se não encontrado.
        """
        return Modulo.query.filter_by(nome=nome).first()

    @staticmethod
    def get_modulo():
        """
        Obtém todos os módulos cadastrados no banco de dados.

        Returns:
            list: Lista de objetos 'Modulo', contendo todos os módulos disponíveis.
        """
        return db.session.query(Modulo).all()
