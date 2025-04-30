from models.model import Progresso


class UsuarioModel:
    @staticmethod
    def consulta_progresso(id):
        return Progresso.query.get(id)
