from app.models import *
from app.views import *
from app import db
from app.utils import parseFecha
from sqlalchemy import desc

def usuarioActual():
    Usuario.buscar("test")

class BuscarVideojuegoController():

    @staticmethod
    def buscarVideojuego(nombre):
        juego = Videojuego.query.filter(Videojuego.nombre.ilike(f"%{nombre}%")).first()
        return juego


class BuscarUsuarioController():

    @staticmethod
    def buscarUsuario(nombre):
        usuario = UsuarioComun.query.filter(UsuarioComun.username.ilike(f"%{nombre}%")).first()
        print(usuario.lista)
        return usuario

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
    def registrar(username, nombre, apellido, correo, password, foto=None):
        if UsuarioComun.query.filter(UsuarioComun.username == username).first() is None:
            user = UsuarioComun(username, nombre, apellido, correo, password, foto)

            db.session.add(user)
            db.session.commit()

            user =  UsuarioComun.query.filter(UsuarioComun.username == username).first()

            listado = ListadoVideojuegos(user.id, "Listado de " + username, Temas.oscuro)

            db.session.add(listado)
            db.session.commit()

            user.lista = listado

            db.session.commit()

            return True

        return False

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
    def registrar(nombre, estreno, generos, plataformas, imagen):
        fechaEstreno = parseFecha(estreno)

        juego = Videojuego(nombre, fechaEstreno, imagen)
        juego.generos = [ Genero.query.get(idn) for idn in generos ]
        juego.plataformas = [ Plataforma.query.get(idn) for idn in plataformas ]

        db.session.add(juego)
        db.session.commit()

        return True

class EditarVideojuegoController():

    @staticmethod
    def inicio():
        pass

    @staticmethod
    def editar(idn, nombre, estreno, generos, plataformas, imagen):

        juego = Videojuego.query.get(idn)

        if juego is None:
            return RegistrarVideojuegoController.registrar(nombre, estreno, generos, plataformas, imagen)

        fechaEstreno = parseFecha(estreno)

        juego.nombre = nombre
        juego.fecha_estreno = fechaEstreno
        juego.imagen = imagen
        juego.generos = [ Genero.query.get(idn) for idn in generos ]
        juego.plataformas = [ Plataforma.query.get(idn) for idn in plataformas ]

        db.session.commit()

        return True

class EliminarVideojuegoController():

    @staticmethod
    def eliminar(idn):
        juego = Videojuego.query.get(idn)

        if juego is None:
            return False
        else:
            db.session.delete(juego)
            db.session.commit()
            return True

class GestionarVideojuegoController():

    @staticmethod
    def obtenerGeneros():
        return GestionarGeneroController.obtenerGeneros()

    @staticmethod
    def obtenerPlataformas():
        return GestionarPlataformaController.obtenerPlataformas()

    @staticmethod
    def obtenerJuegos():
        return Videojuego.query.all()

    @staticmethod
    def ultimosJuegos():
        return Videojuego.query.order_by(desc(Videojuego.id)).limit(20).all()


class RegistrarGeneroController():

    @staticmethod
    def registrar(nombre):
        if Genero.query.filter(Genero.nombre == nombre).first() is None:
            genero = Genero(nombre)
            db.session.add(genero)
            db.session.commit()
            return True
        return False

class EditarGeneroController():

    @staticmethod
    def editar(idn, nuevoNombre):
        genero = Genero.query.get(idn)
        if genero is None:
            RegistrarGeneroController.registrar(nuevoNombre)
        else:
            genero.nombre = nuevoNombre
            db.session.commit()
        return True

class EliminarGeneroController():

    @staticmethod
    def eliminar(idn):
        genero = Genero.query.get(idn)

        if genero is None:
            return False
        else:
            db.session.delete(genero)
            db.session.commit()
            return True

class GestionarGeneroController():

    @staticmethod
    def obtenerGeneros():
        return Genero.query.all()

class RegistrarPlataformaController():

    @staticmethod
    def registrar(nombre, estreno, marca):
        fechaEstreno = parseFecha(estreno)
        if Plataforma.query.filter(Plataforma.nombre == nombre).first() is None:
            plataforma = Plataforma(nombre, fechaEstreno, marca)
            db.session.add(plataforma)
            db.session.commit()
            return True
        return False

class EditarPlataformaController():

    @staticmethod
    def editar(idn, nuevoNombre, nuevoEstreno, nuevoMarca):
        plataforma = Plataforma.query.get(idn)
        fechaEstreno = parseFecha(nuevoEstreno)
        if plataforma is None:
            RegistrarPlataformaController.registrar(nuevoNombre, fechaEstreno, nuevoMarca)
        else:
            plataforma.nombre = nuevoNombre
            plataforma.estreno = fechaEstreno
            plataforma.marca = nuevoMarca
            db.session.commit()
        return True

class EliminarPlataformaController():

    @staticmethod
    def eliminar(idn):
        plataforma = Plataforma.query.get(idn)

        if plataforma is None:
            return False
        else:
            db.session.delete(plataforma)
            db.session.commit()
            return True

class GestionarPlataformaController():

    @staticmethod
    def obtenerPlataformas():
        return Plataforma.query.all()

class PrincipalController():

    @staticmethod
    def inicio():
        pass

