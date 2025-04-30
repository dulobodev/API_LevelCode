from config.Database import db
from models.model import Conquista, UsuarioConquista


class ConquistaModel:
    """
    Classe responsável por operações relacionadas ao modelo 'Conquista'
    e à associação entre usuários e conquistas (UsuarioConquista).
    """

    @staticmethod
    def busca_nome(nome):
        """
        Busca uma conquista pelo nome.

        Args:
            nome (str): Nome da conquista a ser buscada.

        Returns:
            Conquista: Objeto Conquista correspondente, ou None se não encontrado.
        """
        return Conquista.query.filter_by(nome=nome).first()
    
    @staticmethod
    def verifica_conquista(usuario_id):
        """
        Verifica se um usuário possui alguma conquista.

        Args:
            usuario_id (int): ID do usuário.

        Returns:
            UsuarioConquista: Objeto representando a conquista do usuário, ou None se não houver.
        """
        return UsuarioConquista.query.filter_by(usuario_id=usuario_id).first()

    @staticmethod
    def get_conquista():
        """
        Retorna todas as conquistas cadastradas no banco de dados.

        Returns:
            list[Conquista]: Lista com todas as conquistas encontradas.
        """
        return db.session.query(Conquista).all()
