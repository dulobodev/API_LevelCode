from models.model import Progresso

class UsuarioModel:
    """
    Classe que gerencia as operações relacionadas ao modelo 'Progresso' no banco de dados.
    Contém métodos para consultar o progresso de um usuário específico.
    """
    
    @staticmethod
    def consulta_progresso(id):
        """
        Consulta o progresso de um usuário pelo seu ID.

        Args:
            id (int): ID do usuário cujo progresso deve ser consultado.

        Returns:
            Progresso | None: Retorna o objeto 'Progresso' do usuário com o ID fornecido, ou None se não encontrado.
        """
        return Progresso.query.get(id)
