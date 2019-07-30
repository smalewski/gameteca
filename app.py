from flask import Flask
from gameteca.database import db_session
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return "Hello World!"

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
