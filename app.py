from flask import Flask
from flask_jwt_extended import JWTManager
from config.Database import db
from routes.Blueprints.blueprints import register_blueprints
from middleware.CreateSuperadmin import criar_tudo

# Execute esse comando no terminal para aplicar as migrations:
# flask db upgrade

app = Flask(__name__)

app.config.from_pyfile('config/.env')

jwt = JWTManager(app)

db.init_app(app)

with app.app_context():
    db.create_all()
    
register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)