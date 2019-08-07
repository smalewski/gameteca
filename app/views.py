from flask import render_template, redirect, url_for
from app.controllers import *
from app.utils import *


class BuscarVideojuegoView():

    @staticmethod
    def buscarVideojuego(nombre):
        if verificarNombre(nombre):
            juego = BuscarVideojuegoController.buscarVideojuego(nombre)
            if juego is None:
                return PrincipalView.inicio()
            return render_template('verVideojuego.html', videojuego=juego)

        return PrincipalView.inicio()


class BuscarUsuarioView():

    @staticmethod
    def inicio():
        return render_template('buscarUsuario.html')

    @staticmethod
    def buscarUsuario(nombre):
        if verificarNombre(nombre):
            usuario = BuscarUsuarioController.buscarUsuario(nombre)
            if usuario is None:
                return render_template('verUsuario.html')
            return render_template('verUsuario.html', usuario=usuario)
        return render_template('verUsuario.html')

    @staticmethod
    def verListado(usuario):
        return BuscarUsuarioController.verListado(usuario)


class VerListadoView():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def mostrarListado(listado):
        return render_template('usuario/listado.html', listado=listado)

class AnadirListadoView():

    @staticmethod
    def inicio():
        juegos = AnadirListadoController.obtenerJuegos()
        return render_template('listado/anadir.html', juegos)

    @staticmethod
    def anadeVideojuego(request):
        idn = request.form.get('idn, ''')
        if verificarID(idn) and \
           AnadirVideojuegoListadoController.anadeVideojuego(juego):
            return render_template('listado/anadir.html', ok=True)
        return render_template('listado/anadir.html', ok=False)


class EditarListadoView():

    @staticmethod
    def inicio():
        juegos = EditarListadoView.obtenerJuegos()
        return render_template('listado/editar.html', juegos=juegos)

    @staticmethod
    def editar(request):
        idn = request.form.get('idn', -1)
        valoracion = request.form.get('valoracion', 0)
        horas = request.form.get('horas', 0)
        if verificarJuego(idn) and \
           verificarHoras(horas) and \
           verificarValoracion(valoracion):
            EditarListadoController.editar(idn, valoracion, horas)
            return render_template('listado/editar', ok=True)
        return render_template('listado/editar', ok=False)

class EliminarListadoView():

    @staticmethod
    def inicio():
        juegos = EliminarListadoView.obtenerJuegos()
        return render_template('listado/eliminar.html', juegos=juegos)

    @staticmethod
    def eliminar(request):
        idn = request.form.get('idn', -1)
        if verificarJuego(idn):
            EliminarListadoController.eliminar(idn)
            return render_template('listado/eliminar', ok=True)
        return render_template('listado/eliminar', ok=False)

class GestionarListadoView():

    @staticmethod
    def inicio():
        return render_template('listado/index.html')

    @staticmethod
    def anadir():
        return AnadirListadoView.inicio()

    @staticmethod
    def editar():
        return EditarListadoView.inicio()

    @staticmethod
    def eliminar():
        return EliminarListadoView.inicio()


class RegistrarCuentaView():

    @staticmethod
    def inicio():
        return render_template('crearuser.html')

    @staticmethod
    def registrar(request):
        username = request.form.get('username', '')
        imagen = request.form.get('imagen', '')
        nombre = request.form.get('nombre', '')
        apellido = request.form.get('apellido', '')
        correo = request.form.get('correo', '')
        password = request.form.get('password', '')
        if verificarNombre(username) and \
           verificarPassword(password) and \
           verificarCorreo(correo):
            RegistrarCuentaController.registrar(username, nombre, apellido, correo, password, imagen)
        return PrincipalView.inicio()


class EditarCuentaView():

    @staticmethod
    def inicio(cuenta):
        return render_template('editaruser.html', usuario=cuenta)

    @staticmethod
    def editar(cuenta, request):
        imagen = request.form.get('imagen', '')
        nombre = request.form.get('nombre', '')
        apellido = request.form.get('apellido', '')
        correo = request.form.get('correo', '')
        passwordNueva = request.form.get('passwordNueva', '')
        passwordActual = request.form.get('passwordActual', '')
        if verificarPassword(passwordNueva) and \
           verificarPassword(passwordActual) and \
           verificarCorreo(correo):
            EditarCuentaController.editar(cuenta, nombre, apellido, passwordNueva, passwordActual, correo, imagen)
        return redirect(url_for('login'))

class EliminarCuentaView():

    @staticmethod
    def inicio(cuenta):
        return render_template('eliminaruser.html', usuario=cuenta)

    @staticmethod
    def eliminar(cuenta, request):
        password = request.form.get('password', '')
        if verificarPassword(password):
            EliminarCuentaController.eliminar(cuenta, password)
        return redirect(url_for('principal'))


class GestionarCuentaView():

    @staticmethod
    def inicio():
        return render_template('cuenta/index.html')

    @staticmethod
    def registrar():
        return RegistrarCuentaView.inicio()

    @staticmethod
    def editar():
        return EditarCuentaView.inicio()

    @staticmethod
    def eliminar():
        return EliminarCuentaView.inicio()

class RegistrarVideojuegoView():

    @staticmethod
    def inicio():
        return render_template('videojuego.html')

    @staticmethod
    def registrar(request):
        nombre = request.form.get('nombre', '')
        estreno = request.form.get('estreno', '')
        imagen = request.form.get('imagen', '')
        plataformas = request.form.getlist('plataformas')
        generos = request.form.getlist('generos')

        if verificarJuego(nombre) and \
           verificarFecha(estreno):
            RegistrarVideojuegoController.registrar(nombre, estreno, generos, plataformas, imagen)

        return GestionarVideojuegoView.inicio()

class EditarVideojuegoView():

    @staticmethod
    def inicio():
        juegos = EditarVideojuegoController.obtenerJuegos()
        return render_template('videojuego.html', juegos)

    @staticmethod
    def editar(request):
        idn = request.form.get('idn', '')
        nombre = request.form.get('nombre', '')
        imagen = request.form.get('imagen', '')
        estreno = request.form.get('estreno', '')
        plataformas = request.form.getlist('plataformas')
        generos = request.form.getlist('generos')

        if verificarID(idn) and \
           verificarJuego(nombre) and \
           verificarFecha(estreno):
            EditarVideojuegoController.editar(idn, nombre, estreno, generos, plataformas, imagen)

        return GestionarVideojuegoView.inicio()

class EliminarVideojuegoView():

    @staticmethod
    def inicio():
        juegos = EliminarVideojuegoController.obtenerJuegos()
        return render_template('videojuego.html', juegos)

    @staticmethod
    def eliminar(request):
        idn = request.form.get('idn', '')

        if verificarID(idn):
            EliminarVideojuegoController.eliminar(idn)
        return GestionarVideojuegoView.inicio()

class GestionarVideojuegoView():

    @staticmethod
    def inicio():
        generos = GestionarVideojuegoController.obtenerGeneros()
        plataformas = GestionarVideojuegoController.obtenerPlataformas()
        juegos = GestionarVideojuegoController.obtenerJuegos()
        return render_template('videojuego.html', juegos=juegos, generos=generos, plataformas=plataformas)

    @staticmethod
    def registrar(request):
        return RegistrarVideojuegoView.registrar(request)

    @staticmethod
    def editar(request):
        return EditarVideojuegoView.editar(request)

    @staticmethod
    def eliminar(request):
        return EliminarVideojuegoView.eliminar(request)


class GestionarGeneroView():

    @staticmethod
    def inicio():
        generos = GestionarGeneroController.obtenerGeneros()
        return render_template('genero.html', generos=generos)

    @staticmethod
    def registrar(request):
        nombre = request.form.get('nombre', '')
        if verificarNombre(nombre):
            ok = RegistrarGeneroController.registrar(nombre)
        return GestionarGeneroView.inicio()

    @staticmethod
    def editar(request):
        idn = request.form.get('idn', '')
        nombre = request.form.get('nombre', '')
        if verificarID(idn) and \
           verificarNombre(nombre):
            EditarGeneroController.editar(idn, nombre)
        return GestionarGeneroView.inicio()

    @staticmethod
    def eliminar(request):
        idn = request.form.get('idn', '')
        if verificarID(idn):
            EliminarGeneroController.eliminar(idn)
        return GestionarGeneroView.inicio()


class GestionarPlataformaView():

    @staticmethod
    def inicio():
        plataformas = GestionarPlataformaController.obtenerPlataformas()
        return render_template('plataforma.html', plataformas=plataformas)

    @staticmethod
    def registrar(request):
        nombre = request.form.get('nombre', '')
        estreno = request.form.get('estreno', '')
        marca = request.form.get('marca', '')
        if verificarNombre(nombre):
            ok = RegistrarPlataformaController.registrar(nombre, estreno, marca)
        return GestionarPlataformaView.inicio()

    @staticmethod
    def editar(request):
        idn = request.form.get('idn', '')
        nombre = request.form.get('nombre', '')
        estreno = request.form.get('estreno', '')
        marca = request.form.get('marca', '')
        if verificarID(idn) and \
           verificarNombre(nombre):
            EditarPlataformaController.editar(idn, nombre, estreno, marca)
        return GestionarPlataformaView.inicio()

    @staticmethod
    def eliminar(request):
        idn = request.form.get('idn', '')
        if verificarID(idn):
            EliminarPlataformaController.eliminar(idn)
        return GestionarPlataformaView.inicio()



class PrincipalView():

    @staticmethod
    def inicio():
        juegos = GestionarVideojuegoController.ultimosJuegos()
        return render_template('index.html', juegos=juegos)

