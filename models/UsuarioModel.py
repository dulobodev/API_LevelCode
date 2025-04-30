from config.Database import db
from models.model import Usuario

class UsuarioModel:
    """
    Classe responsável pelas operações relacionadas ao modelo 'Usuario' no banco de dados.
    Oferece métodos para buscar usuários pelo nome, ID, e e-mail, além de recuperar todos os usuários cadastrados.
    """
    
    @staticmethod
    def busca_nome(nome):
        """
        Busca um usuário pelo seu nome.

        Este método realiza uma consulta no banco de dados para encontrar o primeiro usuário com o nome fornecido.

        Args:
            nome (str): Nome do usuário a ser buscado.

        Returns:
            Usuario | None: Retorna o primeiro objeto 'Usuario' encontrado com o nome fornecido,
            ou None se não for encontrado.
        """
        return Usuario.query.filter_by(nome=nome).first()

    @staticmethod
    def busca_id(id):
        """
        Busca um usuário pelo seu ID.

        Este método faz uma consulta no banco de dados e retorna o usuário correspondente ao ID fornecido.

        Args:
            id (int): ID do usuário a ser buscado.

        Returns:
            Usuario | None: Retorna o objeto 'Usuario' correspondente ao ID fornecido,
            ou None se não for encontrado.
        """
        return Usuario.query.get(id)

    @staticmethod
    def busca_email(email):
        """
        Busca um usuário pelo seu e-mail.

        Este método realiza uma consulta no banco de dados para encontrar o primeiro usuário com o e-mail fornecido.

        Args:
            email (str): E-mail do usuário a ser buscado.

        Returns:
            Usuario | None: Retorna o primeiro objeto 'Usuario' encontrado com o e-mail fornecido,
            ou None se não for encontrado.
        """
        return Usuario.query.filter_by(email=email).first()
    
    @staticmethod
    def get():
        """
        Recupera todos os usuários cadastrados no banco de dados.

        Este método retorna uma lista de todos os usuários disponíveis no banco de dados.

        Returns:
            list: Lista de objetos 'Usuario', contendo todos os usuários cadastrados.
        """
        return db.session.query(Usuario).all()
