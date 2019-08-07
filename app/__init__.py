from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from functools import wraps
from os import environ

app = Flask(__name__)
app.secret_key = environ.get('CLAVE_SECRETA') or "clave"

# Configuración
app.config.from_object(Config)

# Base de datos
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Sesiones
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'crearCuenta'

@login_manager.user_loader
def load_user(user_id):
    return models.Usuario.query.get(user_id)

from app import models

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
              return login_manager.unauthorized()
            if ((current_user.urole() != role) and (role != "ANY")):
                return login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


from app import routes
