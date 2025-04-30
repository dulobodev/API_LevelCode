import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from schemas.UsuarioSchema import UserCreate, UserLogin
from models.UsuarioModel import UsuarioModel
from models.model import Usuario, Role, Ranking
from config.Database import db
from flask import jsonify, request

def senha_forte(senha):
    return (len(senha) >= 8 and
            re.search(r"[A-Z]", senha) and
            re.search(r"[a-z]", senha) and
            re.search(r"[0-9]", senha) and
            re.search(r"[@#$%^&*(),.?\":{}|<>]", senha))

class UsuarioControllers:

    @staticmethod
    def registrar_usuario():
        try:
            body = UserCreate(**request.get_json())
            
            novo_usuario = Usuario(
                nome = body.nome,
                email = body.email,
                senha = body.senha,
                roles_id = body.roles_id,
                ranking_id = body.ranking_id

            )
            
            ranking_noob = Ranking.query.filter_by(nome="Noob").first()

            novo_usuario.ranking_id = ranking_noob

            if UsuarioModel.busca_email(novo_usuario.email):
                return {"error": "E-mail já cadastrado"}, 400
            if not senha_forte(novo_usuario.senha):
                return jsonify(erro ="A senha deve conter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais."), 422
            
            novo_usuario.senha = generate_password_hash(novo_usuario.senha)

            role = Role.query.get(novo_usuario.roles_id)
            if not role:
                return jsonify(erro="Role não encontrada"), 404
            
            ranking = Ranking.query.get(novo_usuario.ranking_id)
            if not ranking:
                return jsonify(erro="Ranking não encontrado"), 404
            
            db.session.add(novo_usuario)
            db.session.commit()
            return jsonify({"message": "Usuario criadu com sucesso", "user_id": novo_usuario.id}), 201
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Erro ao tentar criar um novo usuario", details=str(e)), 500

            

    @staticmethod
    def login():
        try:
            body = UserLogin(**request.get_json())

            validate = Usuario(
            nome = body.nome,
            senha= body.senha
            )

            usuario = UsuarioModel.busca_nome(validate.nome)
            if usuario and check_password_hash(usuario['senha'], validate.senha):
                role = Role.query.get(usuario['role_id'])

                identity = {"id": usuario['id'],"role": role.nome}

                token = create_access_token(identity=identity)
                return jsonify({"access_token": token}), 200
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify(error="Nome de usuario ou senha invalidos", details=str(e)), 401

        
    def calcular_xp_necessario(nivel):
        a = 10  # Exemplo: valor de a
        b = 50  # Exemplo: valor de b
        c = 0   # Exemplo: valor de c
        return a * (nivel ** 2) + b * nivel + c

    @staticmethod
    def concluir_aula():
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

            # Atualiza XP do usuário
            usuario = Usuario.query.get(body.usuario_id)
            usuario.xp_total += aula.xp

            # Calcula o nível atual
            nivel_atual = usuario.xp_total // 100

            # Verifica se o XP é suficiente para alcançar o próximo nível
            xp_necessario_para_proximo_nivel = calcular_xp_necessario(nivel_atual + 1)
            
            # Verifica se o usuário já alcançou o próximo nível
            if usuario.xp_total >= xp_necessario_para_proximo_nivel:
                usuario.nivel = nivel_atual + 1  # Aumenta o nível
            else:
                usuario.nivel = nivel_atual  # Mantém o nível atual

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