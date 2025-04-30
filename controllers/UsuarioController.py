import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from schemas.UsuarioSchema import UserCreate, UserLogin
from models.UsuarioModel import UsuarioModel
from models.model import Usuario, Role, Ranking
from config.Database import db
from flask import jsonify, request
from datetime import datetime  

def senha_forte(senha):
    """
    Verifica se uma senha atende aos critérios de segurança:
    - Mínimo de 8 caracteres
    - Pelo menos uma letra maiúscula
    - Pelo menos uma letra minúscula
    - Pelo menos um número
    - Pelo menos um caractere especial
    """
    return (len(senha) >= 8 and
            re.search(r"[A-Z]", senha) and
            re.search(r"[a-z]", senha) and
            re.search(r"[0-9]", senha) and
            re.search(r"[@#$%^&*(),.?\":{}|<>]", senha))


class UsuarioControllers:
    """
    Controlador responsável pelas operações relacionadas aos usuários,
    como registro, login, progresso e sistema de XP/níveis.
    """

    @staticmethod
    def registrar_usuario():
        """
        Realiza o registro de um novo usuário, incluindo validação de senha,
        atribuição de ranking padrão e verificação de e-mail duplicado.
        """
        try:
            body = UserCreate(**request.get_json())

            novo_usuario = Usuario(
                nome=body.nome,
                email=body.email,
                senha=body.senha,
                roles_id=body.roles_id,
                ranking_id=body.ranking_id
            )

            # Ranking padrão: Noob
            ranking_noob = Ranking.query.filter_by(nome="Noob").first()
            novo_usuario.ranking_id = ranking_noob

            if UsuarioModel.busca_email(novo_usuario.email):
                return {"error": "E-mail já cadastrado"}, 400

            if not senha_forte(novo_usuario.senha):
                return jsonify(erro="A senha deve conter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais."), 422

            novo_usuario.senha = generate_password_hash(novo_usuario.senha)

            # Valida se Role e Ranking existem
            role = Role.query.get(novo_usuario.roles_id)
            if not role:
                return jsonify(erro="Role não encontrada"), 404

            ranking = Ranking.query.get(novo_usuario.ranking_id)
            if not ranking:
                return jsonify(erro="Ranking não encontrado"), 404

            db.session.add(novo_usuario)
            db.session.commit()

            return jsonify({"message": "Usuário criado com sucesso", "user_id": novo_usuario.id}), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar um novo usuário", details=str(e)), 500

    @staticmethod
    def login():
        """
        Realiza login do usuário a partir de nome e senha.
        Se autenticado com sucesso, retorna um token JWT com as credenciais.
        """
        try:
            body = UserLogin(**request.get_json())

            validate = Usuario(
                nome=body.nome,
                senha=body.senha
            )

            usuario = UsuarioModel.busca_nome(validate.nome)

            if usuario and check_password_hash(usuario['senha'], validate.senha):
                role = Role.query.get(usuario['role_id'])

                identity = {"id": usuario['id'], "role": role.nome}
                token = create_access_token(identity=identity)

                return jsonify({"access_token": token}), 200
            else:
                return jsonify(error="Nome de usuário ou senha inválidos"), 401

        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar fazer login", details=str(e)), 500

    @staticmethod
    def calcular_xp_necessario(nivel):
        """
        Calcula o XP necessário para atingir um determinado nível
        Fórmula: XP = a * nivel² + b * nivel + c
        """
        a = 10
        b = 50
        c = 0
        return a * (nivel ** 2) + b * nivel + c

    @staticmethod
    def concluir_aula():
        """
        Marca uma aula como concluída por um usuário.
        Atualiza o progresso, soma o XP ganho e recalcula o nível do usuário.
        Também verifica se o curso foi concluído.
        """
        try:
            body = AulaConclusaoRequest(**request.get_json())

            aula = Aula.query.get(body.aula_id)
            if not aula:
                return jsonify({"error": "Aula não encontrada"}), 404

            progresso = Progresso.query.filter_by(
                usuario_id=body.usuario_id,
                aula_id=body.aula_id
            ).first()

            if progresso and progresso.status == "concluído":
                return jsonify({"message": "Aula já foi concluída anteriormente"}), 200

            if not progresso:
                progresso = Progresso(
                    usuario_id=body.usuario_id,
                    aula_id=body.aula_id,
                    modulo_id=aula.modulo_id,
                    status="concluído",
                    data_conclusao=datetime.now().strftime("%Y-%m-%d")
                )
                db.session.add(progresso)
            else:
                progresso.status = "concluído"
                progresso.data_conclusao = datetime.now().strftime("%Y-%m-%d")

            # Atualiza XP e nível do usuário
            usuario = Usuario.query.get(body.usuario_id)
            usuario.xp_total += aula.xp

            nivel_atual = usuario.xp_total // 100
            xp_necessario = UsuarioControllers.calcular_xp_necessario(nivel_atual + 1)

            if usuario.xp_total >= xp_necessario:
                usuario.nivel = nivel_atual + 1
            else:
                usuario.nivel = nivel_atual

            db.session.commit()

            # Verifica se o curso foi concluído
            verificar_conclusao_curso(usuario.id, aula.modulo.cursos[0].id)

            return jsonify({
                "message": "Aula concluída com sucesso",
                "xp_ganho": aula.xp,
                "xp_total": usuario.xp_total,
                "nivel": usuario.nivel
            }), 200

        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao concluir aula", details=str(e)), 500
