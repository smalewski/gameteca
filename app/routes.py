from flask import request
from app.views import *

from app import app

@app.route('/')
def principal():
    return PrincipalView.inicio()

@app.route('/videojuegos')
def videojuegos():
    pass

#
# Busquedas
#
@app.route('/videojuego/<nombre>')
def buscarVideojuego(nombre):
    return BuscarVideojuegoView.buscarVideojuego(nombre)

@app.route('/usuario/<username>')
def buscarUsuario(username):
    return BuscarUsuarioView.buscarUsuario(username)


#
# Gestión usuarios
#

@app.route('/nueva-cuenta', methods=['GET', 'POST'])
def crearCuenta():
    if request.method == 'GET':
        return RegistrarCuentaView.inicio()
    else:
        return RegistrarCuentaView.registrar(request)

@app.route('/usuario/<username>')
def verUsuario(username):
    return BuscarUsuarioView.buscarUsuario(username)


#
# Tablas básicas
#


#
# Videojuegos
#
@app.route('/admin/videojuego')
def adminVideojuego():
    return GestionarVideojuegoView.inicio()

@app.route('/admin/videojuego', methods=['POST'])
def adminRegistrarVideojuego():
    action = request.form.get('action', '')
    if action == "Agregar":
        return GestionarVideojuegoView.registrar(request)
    elif action == "Editar":
        return GestionarVideojuegoView.editar(request)
    elif action == "Dar de baja":
        return GestionarVideojuegoView.eliminar(request)
    else:
        return GestionarVideojuegoView.inicio()


#
# Generos
#
@app.route('/admin/genero')
def adminGenero():
    return GestionarGeneroView.inicio()

@app.route('/admin/genero', methods=['POST'])
def adminRegistrarGenero():
    action = request.form.get('action', '')
    if action == "Agregar":
        return GestionarGeneroView.registrar(request)
    elif action == "Editar":
        return GestionarGeneroView.editar(request)
    elif action == "Dar de baja":
        return GestionarGeneroView.eliminar(request)
    else:
        return GestionarGeneroView.inicio()

@app.route('/admin/genero', methods=['POST'])
def adminEditarGenero():
    return GestionarGeneroView.editar(request)

@app.route('/admin/genero', methods=['POST'])
def adminEliminarGenero():
    return GestionarGeneroView.eliminar(request)
    return GestionarGeneroView.registrar(request)


#
# Plataformas
#
@app.route('/admin/plataforma')
def adminPlataforma():
    return GestionarPlataformaView.inicio()

@app.route('/admin/plataforma', methods=['POST'])
def adminRegistrarPlataforma():
    return GestionarPlataformaView.registrar(request)

@app.route('/admin/plataforma', methods=['POST'])
def adminEditarPlataforma():
    return GestionarPlataformaView.editar(request)

@app.route('/admin/plataforma', methods=['POST'])
def adminEliminarPlataforma():
    return GestionarPlataformaView.eliminar(request)
