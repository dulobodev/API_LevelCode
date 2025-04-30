from config.Database import db
from models.model import Role, Permission

class RoleModel:
    """
    Classe responsável pelas operações relacionadas ao modelo 'Role' e 'Permission' no banco de dados.
    Oferece métodos para buscar roles e permissões pelo nome, ID e para recuperar todas as roles cadastradas.
    """
    
    @staticmethod
    def busca_role_nome(nome):
        """
        Busca uma role pelo seu nome.

        Este método realiza uma consulta no banco de dados para encontrar a role com o nome fornecido.

        Args:
            nome (str): Nome da role a ser buscada.

        Returns:
            Role | None: Retorna o primeiro objeto 'Role' encontrado com o nome fornecido,
            ou None se não for encontrado.
        """
        return Role.query.filter_by(nome=nome).first()

    @staticmethod
    def busca_permission_nome(nome):
        """
        Busca uma permissão pelo seu nome.

        Este método realiza uma consulta no banco de dados para encontrar a permissão com o nome fornecido.

        Args:
            nome (str): Nome da permissão a ser buscada.

        Returns:
            Permission | None: Retorna o primeiro objeto 'Permission' encontrado com o nome fornecido,
            ou None se não for encontrado.
        """
        return Permission.query.filter_by(nome=nome).first()
        
    @staticmethod
    def busca_id(id):
        """
        Busca uma role pelo seu ID.

        Este método faz uma consulta no banco de dados e retorna a role correspondente ao ID fornecido.

        Args:
            id (int): ID da role a ser buscada.

        Returns:
            Role | None: Retorna o objeto 'Role' correspondente ao ID fornecido,
            ou None se não for encontrado.
        """
        return Role.query.get(id)

    @staticmethod
    def get():
        """
        Recupera todas as roles cadastradas no banco de dados.

        Este método retorna uma lista de todas as roles disponíveis no banco de dados.

        Returns:
            list: Lista de objetos 'Role', contendo todas as roles cadastradas.
        """
        return db.session.query(Role).all()
