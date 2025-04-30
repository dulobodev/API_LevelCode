from flask import Flask
from flask_jwt_extended import JWTManager
from config.Database import db
from routes.Blueprints.blueprints import register_blueprints

# Criação da instância da aplicação Flask
app = Flask(__name__)

# Carregamento das configurações do arquivo '.env' para a aplicação
app.config.from_pyfile('config/.env')

# Inicialização do JWTManager para autenticação baseada em JWT
jwt = JWTManager(app)

# Inicialização do banco de dados com a aplicação Flask
db.init_app(app)

# Criação das tabelas no banco de dados com base nos modelos definidos
with app.app_context():
    db.create_all()
    
# Registro de todos os blueprints (módulos de rotas) na aplicação
register_blueprints(app)

# Inicia a aplicação em modo de desenvolvimento (debug)
if __name__ == '__main__':
    app.run(debug=True)
