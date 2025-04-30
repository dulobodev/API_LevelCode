from config.Database import db
from models.model import Curso

class CursoModel:
    """
    Classe responsável por realizar operações de acesso ao banco de dados relacionadas ao modelo 'Curso'.
    """

    @staticmethod
    def busca_nome(titulo):
        """
        Busca um curso pelo título fornecido.

        Args:
            titulo (str): O título do curso a ser buscado.

        Returns:
            Curso: Objeto Curso correspondente ao título, ou None se não encontrado.
        """
        return Curso.query.filter_by(titulo=titulo).first()
        
    @staticmethod
    def get_curso():
        """
        Retorna todos os cursos cadastrados no banco de dados.

        Returns:
            list[Curso]: Lista com todos os objetos Curso encontrados.
        """
        return db.session.query(Curso).all()
