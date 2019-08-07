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
            valoracion = BuscarVideojuegoController.obtenerValoracion(current_user, juego)
            return render_template('verVideojuego.html', videojuego=juego, valoracion=valoracion)

        return PrincipalView.inicio()


class BuscarUsuarioView():

    @staticmethod
    def buscarUsuario(nombre):
        if verificarNombre(nombre):
            usuario = BuscarUsuarioController.buscarUsuario(nombre)
            if usuario is None:
                return render_template('verUsuario.html')
            return render_template('verUsuario.html', usuario=usuario)
        return render_template('verUsuario.html')


class AnadirListadoView():

    @staticmethod
    def inicio(nombre):
        juego = AnadirListadoController.obtenerJuego(nombre)
        return render_template('crearreview.html', videojuego=juego)

    @staticmethod
    def anadir(nombreJuego, request):
        username = request.form.get('username', '')
        puntaje = int(request.form.get('puntaje', 0))
        horas = int(request.form.get('horas', 0))
        comentario = request.form.get('comentario', '')

        if verificarHoras(horas) and \
           verificarValoracion(puntaje):
            AnadirListadoController.anadir(username, nombreJuego, horas, puntaje, comentario)

        return redirect(url_for('login'))


class EditarListadoView():

    @staticmethod
    def inicio(nombre):
        juego = EditarListadoController.obtenerJuego(nombre)
        valoracion = EditarListadoController.obtenerValoracion(current_user, juego)
        return render_template('editarreview.html', videojuego=juego, valoracion=valoracion)

    @staticmethod
    def editar(nombreJuego, request):
        username = request.form.get('username', '')
        puntaje = int(request.form.get('puntaje', 0))
        horas = int(request.form.get('horas', 0))
        comentario = request.form.get('comentario', '')

        if verificarHoras(horas) and \
           verificarValoracion(puntaje):
            EditarListadoController.editar(username, nombreJuego, puntaje, horas, comentario)

        return redirect(url_for('login'))

class EliminarListadoView():

    @staticmethod
    def eliminar(user, nombreJuego):
        EliminarListadoController(user, nombreJuego)
        return redirect(url_for('login'))

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

