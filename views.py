from flask import request, render_template
from controllers import *
from utils import *

class BuscarVideojuegoView():

    @staticmethod
    def inicio():
        return render_template('buscarVideojuego/index.html')

    @staticmethod
    def buscarVideojuego():
        nombre = request.form.get('nombre', '')
        if verificarNombre(nombre):
            juego = BuscarVideojuegoController.buscarVideojuego(nombre)
            return render_template('buscarVideojuego/index.html', juego=juego)
        return render_template('buscarVideojuego/index.html')


class BuscarUsuarioView():

    @staticmethod
    def inicio():
        return render_template('buscarUsuario/index.html')

    @staticmethod
    def buscarUsuario():
        nombre = request.form.get('nombre', '')
        if verificarNombre(nombre):
            usuario = BuscarUsuarioController.buscarUsuario(nombre)
            return render_template('buscarUsuario/index.html', usuario=usuario)
        return render_template('buscarUsuario/index.html')

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
    def anadeVideojuego():
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
    def editar():
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
    def eliminar():
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
        return render_template('cuenta/registrar.html')

    @staticmethod
    def registrar(username, password, correo):
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        correo = request.form.get('correo', '')
        if verificarNombre(username) and \
           verificarPassword(password) and \
           verificarCorreo(correo) and \
           RegistrarCuentaController.registrar(username, password, correo):
            return render_template('cuenta/registrar.html', ok=True)
        return render_template('cuenta/registrar.html', ok=False)


class EditarCuentaView():

    @staticmethod
    def inicio():
        cuenta = EditarCuentaController.obtenerCuenta()
        return render_template('cuenta/editar.html', cuenta=cuenta)

    @staticmethod
    def editar():
        cuenta = EditarCuentaController.obtenerCuenta()
        passwordNueva = request.form.get('passwordNueva', '')
        passwordActual = request.form.get('passwordActual', '')
        correo = request.form.get('correo', '')
        if verificarNombre(username) and \
           verificarPassword(passwordNueva) and \
           verificarPassword(passwordActual) and \
           verificarCorreo(correo) and \
           EditarCuentaController.editar(cuenta, passwordNueva, passwordActual, correo):
            return render_template('cuenta/editar.html', ok=True)
        return render_template('cuenta/editar.html', ok=False)

class EliminarCuentaView():

    @staticmethod
    def inicio():
        cuenta = EliminarCuentaController.obtenerCuenta()
        return render_template('cuenta/eliminar.html', cuenta=cuenta)

    @staticmethod
    def eliminar():
        cuenta = EliminarCuentaController.obtenerCuenta()
        password = request.form.get('password', '')
        if verificarPassword(password) and \
           EliminarCuentaController.eliminar(cuenta, password):
            return render_template('cuenta/eliminar.html', ok=True)
        return render_template('cuenta/eliminar.html', ok=False)


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
        return render_template('videojuego/registrar.html')

    @staticmethod
    def registrar(nombre, estreno, plataformas, generos):
        nombre = request.form.get('nombre', '')
        estreno = request.form.get('estreno', '')
        plataformas = request.form.get('plataformas', [])
        generos = request.form.get('generos', [])

        if verificarJuego(nombre) and \
           verificarFecha(estreno) and \
           RegistrarVideojuegoController.registrar(nombre, estreno, platafromas, generos):
            return render_template('videojuego/registrar.html', ok=True)
        return render_template('videojuego/registrar.html', ok=False)

class EditarVideojuegoView():

    @staticmethod
    def inicio():
        juegos = EditarVideojuegoController.obtenerJuegos()
        return render_template('videojuego/editar.html', juegos)

    @staticmethod
    def editar():
        nombre = request.form.get('nombre', '')
        estreno = request.form.get('estreno', '')
        plataformas = request.form.get('plataformas', [])
        generos = request.form.get('generos', [])

        if verificarJuego(nombre) and \
           verificarFecha(estreno) and \
           EditarVideojuegoController.editar(nombre, estreno, plataformas, generos):
            return render_template('videojuego/editar.html', ok=True)
        return render_template('videojuego/editar.html', ok=False)

class EliminarVideojuegoView():

    @staticmethod
    def inicio():
        juegos = EliminarVideojuegoController.obtenerJuegos()
        return render_template('videojuego/eliminar.html', juegos)

    @staticmethod
    def eliminar():
        idn = request.form.get('idn', '')

        if verificarID(idn) and EliminarVideojuegoController.eliminar(idn):
            return render_template('videojuego/eliminar.html', ok=True)
        return render_template('videojuego/eliminar.html', ok=False)

class GestionarVideojuegoView():

    @staticmethod
    def inicio():
        return render_template('videojuego/index.html')

    @staticmethod
    def registrar():
        return RegistrarVideojuegoView.inicio()

    @staticmethod
    def editar():
        return EditarVideojuegoView.inicio()

    @staticmethod
    def eliminar():
        return EliminarVideojuegoView.inicio()


class RegistrarGeneroView():

    @staticmethod
    def inicio():
        generos = RegistrarGeneroController.obtenerGeneros()
        return render_template('genero/index.html', generos)

    @staticmethod
    def registrar():
        nombre = request.form.get('nombre', '')
        if verificarNombre(nombre) and RegistrarGeneroController.registrar(nombre):
            return render_template('genero/index.html', ok=True)
        return render_template('genero/index.html', ok=False)

class EditarGeneroView():

    @staticmethod
    def inicio():
        generos = EditarGeneroController.obtenerGeneros()
        return render_template('genero/editar.html', generos)

    @staticmethod
    def editar():
        idn = request.form.get('idn', '')
        nombre = request.form.get('nombre', '')
        if verificarID(idn) and \
           verificarNombre(nombre) and \
           EditarGeneroController.editar(idn, nombre):
            return render_template('genero/index.html', ok=True)
        return render_template('genero/index.html', ok=False)

class EliminarGeneroView():

    @staticmethod
    def inicio():
        generos = EliminarGeneroController.obtenerGeneros()
        return render_template('genero/eliminar.html', generos)

    @staticmethod
    def eliminar():
        idn = request.form.get('idn', '')
        if verificarID(idn) and EliminarGeneroController.eliminar(idn):
            return render_template('genero/eliminar.html', ok=True)
        return render_template('genero/eliminar', ok=False)

class GestionarGeneroView():

    @staticmethod
    def inicio():
        return render_template('genero/index.html')

    @staticmethod
    def registrar():
        return RegistrarGeneroView.inicio()

    @staticmethod
    def editar():
        return EditarGeneroView.inicio()

    @staticmethod
    def eliminar():
        return EliminarGeneroView.inicio()

class RegistrarPlataformaView():

    @staticmethod
    def inicio():
        plataformas = RegistrarPlataformaController.obtenerPlataformas()
        return render_template('plataforma/index.html', plataformas=plataformas)

    @staticmethod
    def registrar(nombre, estreno, marca):
        nombre = request.form.get('nombre', '')
        estreno = request.form.get('estreno', '')
        marca = request.form.get('marca', '')
        if verificarNombre(nombre) and \
           verificarFecha(estreno) and \
           verificarNombre(marca) and \
           RegistrarPlataformaController.registrar(nombre, estreno, marca):
            return render_template('plataforma/registrar.html', ok=True)
        return render_template('plataforma/registrar.html', ok=False)


class EditarPlataformaView():

    @staticmethod
    def inicio():
        plataformas = RegistrarPlataformaController.obtenerPlataformas()
        return render_template('plataforma/index.html', plataformas=plataformas)

    @staticmethod
    def editar(idn, nuevoNombre, nuevoEstreno, nuevoMarca):
        idn = request.form.get('idn', '')
        nombre = request.form.get('nombre', '')
        estreno = request.form.get('estreno', '')
        marca = request.form.get('marca', '')
        if verificarID(idn) and \
           verificarNombre(nombre) and \
           verificarFecha(estreno) and \
           verificarNombre(marca) and \
           EditarPlataformaController.editar(idn, nombre, estreno, marca):
            return render_template('plataforma/editar.html', ok=True)
        return render_template('plataforma/editar.html', ok=False)

class EliminarPlataformaView():

    @staticmethod
    def inicio():
        plataformas = RegistrarPlataformaController.obtenerPlataformas()
        return render_template('plataforma/index.html', plataformas=plataformas)

    @staticmethod
    def eliminar(idn):
        idn = request.form.get('idn', '')
        if verificarID(idn) and \
           EliminarPlataformaController.eliminar(idn):
            return render_template('plataforma/eliminar.html', ok=True)
        return render_template('plataforma/eliminar.html', ok=False)

class GestionarPlataformaView():

    @staticmethod
    def inicio():
        return render_template('plataforma/index.html')

    @staticmethod
    def registrar():
        return RegistrarPlataformaView.inicio()

    @staticmethod
    def editar():
        return EditarPlataformaView.inicio()

    @staticmethod
    def eliminar():
        return EliminarPlataformaView.inicio()

class PrincipalView():

    @staticmethod
    def inicio():
        return render_template('index.html')

