from routes.AdminRoute import admin_bp
from routes.AulaRoute import aula_bp
from routes.ConquistaRoute import conquista_bp
from routes.CursoRoute import curso_bp
from routes.DesafioRoute import desafio_bp
from routes.ModuloRoute import modulo_bp
from routes.RankingRoute import ranking_bp
from routes.UserRoute import user_bp

def register_blueprints(app):
    app.register_blueprint(admin_bp, url_prefix='/admin', endpoint='admin_bp')
    app.register_blueprint(aula_bp, url_prefix='/aula', endpoint='aula_bp')
    app.register_blueprint(conquista_bp, url_prefix='/conquista', endpoint='conquista_bp')
    app.register_blueprint(curso_bp, url_prefix='/curso', endpoint='curso_bp')
    app.register_blueprint(desafio_bp, url_prefix='/desafio', endpoint='desafio_bp')
    app.register_blueprint(modulo_bp, url_prefix='/modulo', endpoint='modulo_bp')
    app.register_blueprint(ranking_bp, url_prefix='/ranking', endpoint='ranking_bp')
    app.register_blueprint(user_bp, url_prefix='/users', endpoint='user_bp')
