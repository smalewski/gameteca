from models import *
from views import *

def usuarioActual():
    Usuario.buscar("test")

class BuscarVideojuegoController():

    @staticmethod
    def buscarVideojuego(nombre):
        return Videojuego.buscar(nombre)


class BuscarUsuarioController():

    @staticmethod
    def buscarUsuario(nombre):
        return Usuario.buscar(nombre)

    @staticmethod
    def verListado(usuario):
        return VerListadoController.mostrarListado(usuario)


class VerListadoController():

    @staticmethod
    def mostrarListado(usuario):
        listado = ListadoVideojuegos.buscar(usuario)
        return VerListadoView.mostrarListado(listado)

class AnadirListadoController():

    @staticmethod
    def obtenerJuegos():
        return GestionarListadoController.obtenerJuegos()

    @staticmethod
    def anadeVideojuego(idn):
        usuario = usuarioActual()
        listado = usuario.lista
        return listado.anadirJuego(idn)

class EditarListadoController():

    @staticmethod
    def obtenerJuegos():
        return GestionarListadoController.obtenerJuegosListado()

    @staticmethod
    def editar(idn, valoracion, horas):
        usuario = usuarioActual()
        listado = usuario.lista
        return listado.editarJuego(idn, valoracion, horas)

class EliminarListadoController():

    @staticmethod
    def obtenerJuegos():
        return GestionarListadoController.obtenerJuegosListado()

    @staticmethod
    def eliminar(idn):
        usuario = usuarioActual()
        listado = usuario.lista
        return listado.eliminarJuego(idn)

class GestionarListadoController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def anadir():
        return

    @staticmethod
    def editar():
        pass

    @staticmethod
    def eliminar():
        pass

    @staticmethod
    def obtenerJuegos():
        return Videojuego.obtenerVideojuegos()

    @staticmethod
    def obtenerJuegos():
        usuario = usuarioActual()
        listado = usuario.lista
        return listado.juegos


class RegistrarCuentaController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def registrar(username, password, correo):
        pass

class EditarCuentaController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def editar(nuevoUsername, nuevaPassword, passwordActual, nuevoCorreo):
        pass

class EliminarCuentaController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def eliminar(password):
        pass

class GestionarCuentaController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def registrar():
        pass

    @staticmethod
    def editar():
        pass

    @staticmethod
    def eliminar():
        pass

class RegistrarVideojuegoController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def registrar(nombre, estreno, plataformas, generos):
        pass

class EditarVideojuegoController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def editar(nuevoUsername, nuevaPassword, passwordActual, nuevoCorreo):
        pass

class EliminarVideojuegoController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def eliminar(password):
        pass

class GestionarVideojuegoController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def registrar():
        pass

    @staticmethod
    def editar():
        pass

    @staticmethod
    def eliminar():
        pass


class RegistrarGeneroController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def registrar(nombre):
        pass

class EditarGeneroController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def editar(idn, nuevoNombre):
        pass

class EliminarGeneroController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def eliminar(idn):
        pass

class GestionarGeneroController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def registrar():
        pass

    @staticmethod
    def editar():
        pass

    @staticmethod
    def eliminar():
        pass

class RegistrarPlataformaController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def registrar(nombre, estreno, marca):
        pass

class EditarPlataformaController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def editar(idn, nuevoNombre, nuevoEstreno, nuevoMarca):
        pass

class EliminarPlataformaController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def eliminar(idn):
        pass

class GestionarPlataformaController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def registrar():
        pass

    @staticmethod
    def editar():
        pass

    @staticmethod
    def eliminar():
        pass

class PrincipalController():

    @staticmethod
    def inicio():
        pass

