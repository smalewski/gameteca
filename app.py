from flask import Flask
from database import db_session
from views import *

app = Flask(__name__)

@app.route('/')
def principal():
    return PrincipalView.inicio()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
