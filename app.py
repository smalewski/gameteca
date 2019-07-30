from flask import Flask
from database import db_session
from views import *

app = Flask(__name__)

@app.route('/')
def principal():
    return PrincipalView.inicio()

@app.route('/videojuegos')
def videojuegos():
    pass

#
# Tablas básicas
#


#
# Videojuegos
#
@app.route('/admin/videojuego')
def adminVideojuego():
    return GestionarVideojuegoView.inicio()

@app.route('/admin/videojuego/agregar')
def adminVideojuego():
    return RegistrarVideojuegoView.inicio()

@app.route('/admin/videojuego/editar')
def adminVideojuego():
    return EditarVideojuegoView.inicio()

@app.route('/admin/videojuego/eliminar')
def adminVideojuego():
    return EliminarVideojuegoView.inicio()


#
# Generos
#
@app.route('/admin/genero')
def adminGenero():
    return GestionarGeneroView.inicio()

@app.route('/admin/genero/agregar')
def adminGenero():
    return RegistrarGeneroView.inicio()

@app.route('/admin/genero/editar')
def adminGenero():
    return EditarGeneroView.inicio()

@app.route('/admin/genero/eliminar')
def adminGenero():
    return EliminarGeneroView.inicio()


#
# Plataformas
#
@app.route('/admin/plataforma')
def adminPlataforma():
    return GestionarPlataformaView.inicio()

@app.route('/admin/plataforma/agregar')
def adminPlataforma():
    return RegistrarPlataformaView.inicio()

@app.route('/admin/plataforma/editar')
def adminPlataforma():
    return EditarPlataformaView.inicio()

@app.route('/admin/plataforma/eliminar')
def adminPlataforma():
    return EliminarPlataformaView.inicio()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
