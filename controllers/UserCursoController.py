from models.model import UsuarioCurso, Usuario, Progresso, Aula
from schemas.CursosSchema import UsuarioCursoCreate
from schemas.ProgressoSchema import ProgressCreate
from config.Database import db
from flask import jsonify, request
from datetime import datetime


class UserCurso:
    """Classe responsável pelas ações de usuário relacionadas a cursos, como inscrição, conclusão de aula e verificação de progresso."""

    @staticmethod
    def inscrever_usuario():
        """
        Inscreve um usuário em um curso, se ainda não estiver inscrito.

        Returns:
            JSON: Mensagem de sucesso com ID da inscrição ou erro com detalhes.
        """
        try:
            body = UsuarioCursoCreate(**request.get_json())

            if UsuarioCurso.query.filter_by(usuario_id=body.usuario_id, curso_id=body.curso_id).first():
                return jsonify({"error": "Usuário já está inscrito neste curso"}), 422

            nova_inscricao = UsuarioCurso(
                usuario_id=body.usuario_id,
                curso_id=body.curso_id,
                status="em progresso"
            )

            db.session.add(nova_inscricao)
            db.session.commit()

            return jsonify({"message": "Inscrição realizada com sucesso", "inscricao_id": nova_inscricao.id}), 201

        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar inscrever usuário", details=str(e)), 500

    @staticmethod
    def verificar_conclusao_curso(usuario_id, curso_id):
        """
        Verifica se o usuário concluiu todas as aulas do curso e atualiza o status do curso para 'concluído' se for o caso.

        Args:
            usuario_id (int): ID do usuário.
            curso_id (int): ID do curso.
        """
        try:
            aulas_concluidas = db.session.query(Progresso).filter_by(
                usuario_id=usuario_id,
                status="concluído"
            ).join(Aula, Progresso.aula_id == Aula.id).filter(Aula.curso_id == curso_id).all()

            todas_aulas = Aula.query.filter_by(curso_id=curso_id).all()

            if len(aulas_concluidas) == len(todas_aulas):
                progresso_curso = UsuarioCurso.query.filter_by(usuario_id=usuario_id, curso_id=curso_id).first()

                if progresso_curso:
                    progresso_curso.status = "concluído"
                else:
                    progresso_curso = UsuarioCurso(usuario_id=usuario_id, curso_id=curso_id, status="concluído")
                    db.session.add(progresso_curso)

                db.session.commit()
                print(f"Curso {curso_id} concluído pelo usuário {usuario_id}")
            else:
                print(f"O curso {curso_id} ainda não foi concluído.")
        except Exception as e:
            print(f"Erro ao verificar conclusão do curso: {e}")

    @staticmethod
    def calcular_xp_necessario(nivel):
        """
        Calcula o XP necessário para o próximo nível, baseado em uma fórmula quadrática.

        Args:
            nivel (int): Nível atual.

        Returns:
            int: Quantidade de XP necessária.
        """
        a = 10
        b = 50
        c = 0
        return a * (nivel ** 2) + b * nivel + c

    @staticmethod
    def concluir_aula():
        """
        Marca uma aula como concluída para o usuário, atualiza o XP total, verifica o nível,
        e verifica a conclusão do curso correspondente.

        Returns:
            JSON: Mensagem de sucesso com informações de XP e nível, ou erro com detalhes.
        """
        try:
            body = ProgressCreate(**request.get_json())

            aula = Aula.query.get(body.aula_id)
            if not aula:
                return jsonify({"error": "Aula não encontrada"}), 404

            progresso = Progresso.query.filter_by(usuario_id=body.usuario_id, aula_id=body.aula_id).first()

            if progresso and progresso.status == "concluído":
                return jsonify({"message": "Aula já foi concluída anteriormente"}), 200

            if not progresso:
                progresso = Progresso(
                    usuario_id=body.usuario_id,
                    aula_id=body.aula_id,
                    modulo_id=aula.modulo_id,
                    status="concluído",
                    data_conclusao=datetime.now()
                )
                db.session.add(progresso)
            else:
                progresso.status = "concluído"
                progresso.data_conclusao = datetime.now()

            usuario = Usuario.query.get(body.usuario_id)
            usuario.xp_total += aula.xp

            nivel_atual = usuario.xp_total // 100

            while usuario.xp_total >= UserCurso.calcular_xp_necessario(nivel_atual + 1):
                nivel_atual += 1

            usuario.nivel = nivel_atual

            db.session.commit()

            UserCurso.verificar_conclusao_curso(usuario.id, aula.modulo.cursos[0].id)

            return jsonify({
                "message": "Aula concluída com sucesso",
                "xp_ganho": aula.xp,
                "xp_total": usuario.xp_total,
                "nivel": usuario.nivel
            }), 200

        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao concluir aula", details=str(e)), 500
