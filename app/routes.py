from flask import request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app.views import *
from app.models import Usuario
from app import app, db, login_required

#
# Sesiones
#

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        user = Usuario.query.filter(Usuario.username == username).first()

        if user is not None and password == user.password:
            user.conectado = True
            db.session.commit()
            login_user(user, remember=True)
    if current_user is None:
        return redirect(url_for('principal'))
    else:
        return redirect(url_for('buscarUsuario', username=current_user.username))


@app.route('/logout')
@login_required()
def logout():
    user = current_user
    user.conectado = False
    db.session.commit()
    logout_user()
    return redirect(url_for('principal'))


#
# Principal
#

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

@app.route('/editar-cuenta', methods=['POST', 'GET'])
@login_required()
def editarCuenta():
    usuario = current_user
    if request.method == 'GET':
        return EditarCuentaView.inicio(usuario)
    else:
        return EditarCuentaView.editar(usuario, request)

@app.route('/eliminar-cuenta', methods=['POST', 'GET'])
@login_required()
def eliminarCuenta():
    usuario = current_user
    if request.method == 'GET':
        return EliminarCuentaView.inicio(usuario)
    else:
        return EliminarCuentaView.eliminar(usuario, request)


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
# Valoraciones
#

@app.route('/videojuego/<nombre>/crear-reseña', methods=['GET', 'POST'])
@login_required()
def crearReseña(nombre):
    if request.method == 'POST':
        return AnadirListadoView.anadir(nombre, request)
    else:
        return AnadirListadoView.inicio(nombre)

@app.route('/videojuego/<nombre>/editar-reseña', methods=['GET', 'POST'])
@login_required()
def editarReseña(nombre):
    if request.method == 'POST':
        return EditarListadoView.editar(nombre, request)
    else:
        return EditarListadoView.inicio(nombre)

@app.route('/videojuego/<nombre>/eliminar-reseña')
@login_required()
def eliminarReseña(nombre):
    username = current_user
    return EliminarListadoView.eliminar(user, nombre)


#
# Tablas básicas
#


#
# Videojuegos
#
@app.route('/admin/videojuego')
@login_required("ADMIN")
def adminVideojuego():
    return GestionarVideojuegoView.inicio()

@app.route('/admin/videojuego', methods=['POST'])
@login_required("ADMIN")
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
@login_required("ADMIN")
def adminGenero():
    return GestionarGeneroView.inicio()

@app.route('/admin/genero', methods=['POST'])
@login_required("ADMIN")
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
@login_required("ADMIN")
def adminEditarGenero():
    return GestionarGeneroView.editar(request)

@app.route('/admin/genero', methods=['POST'])
@login_required("ADMIN")
def adminEliminarGenero():
    return GestionarGeneroView.eliminar(request)
    return GestionarGeneroView.registrar(request)


#
# Plataformas
#
@app.route('/admin/plataforma')
@login_required("ADMIN")
def adminPlataforma():
    return GestionarPlataformaView.inicio()

@app.route('/admin/plataforma', methods=['POST'])
@login_required("ADMIN")
def adminRegistrarPlataforma():
    return GestionarPlataformaView.registrar(request)

@app.route('/admin/plataforma', methods=['POST'])
@login_required("ADMIN")
def adminEditarPlataforma():
    return GestionarPlataformaView.editar(request)

@app.route('/admin/plataforma', methods=['POST'])
@login_required("ADMIN")
def adminEliminarPlataforma():
    return GestionarPlataformaView.eliminar(request)
