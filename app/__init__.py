from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from os import environ

app = Flask(__name__)
app.secret_key = environ.get('CLAVE_SECRETA') or "clave"

# Configuración
app.config.from_object(Config)

# Base de datos
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

# Sesiones
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'crearCuenta'

@login_manager.user_loader
def load_user(user_id):
    return models.Usuario.query.get(user_id)
