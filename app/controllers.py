from app.models import *
from app.views import *
from app import db
from app.utils import parseFecha
from sqlalchemy import desc
from flask_login import current_user

def usuarioActual():
    return current_user

class BuscarVideojuegoController():

    @staticmethod
    def buscarVideojuego(nombre):
        juego = Videojuego.query.filter(Videojuego.nombre.ilike(f"%{nombre}%")).first()
        return juego

    @staticmethod
    def obtenerValoracion(user, juego):
        if current_user is None:
            return None
        return EditarListadoController.obtenerValoracion(user, juego)


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
    def obtenerJuego(nombre):
        return GestionarListadoController.obtenerJuego(nombre)

    @staticmethod
    def anadir(username, videojuego, horas, puntaje, comentario):
        usuario = UsuarioComun.query.filter(username == Usuario.username).first()
        juego = Videojuego.query.filter(videojuego == Videojuego.nombre).first()
        listado = usuario.lista
        valoracion = Valoracion(horas, puntaje, comentario)
        valoracion.videojuego = juego
        valoracion.listado = listado

        db.session.add(valoracion)
        db.session.commit()

        return True

class EditarListadoController():

    @staticmethod
    def obtenerValoracion(usuario, juego):
        try:
            lista = ListadoVideojuegos.query.filter(ListadoVideojuegos.usuario_id == usuario.id).first()
            valoracion = Valoracion.query.filter(juego.id == Valoracion.videojuego_id)\
                                         .filter(lista.id == Valoracion.listado_id)\
                                         .first()
            return valoracion
        except:
            return None


    @staticmethod
    def obtenerJuego(nombre):
        return GestionarListadoController.obtenerJuego(nombre)

    @staticmethod
    def editar(username, videojuego, horas, puntaje, comentario):
        usuario = Usuario.query.filter(username == Usuario.username).first()
        juego = Videojuego.query.filter(videojuego == Videojuego.nombre).first()
        valoracion = EditarListadoController.obtenerValoracion(usuario, juego)

        valoracion.horas = horas
        valoracion.puntaje = puntaje
        valoracion.comentario = comentario

        db.session.commit()

        return True

class EliminarListadoController():

    @staticmethod
    def eliminar(usuario, nombreJuego):
        juego = Videojuego.query.filter(videojuego == Videojuego.nombre).first()
        valoracion = Valoracion.query.filter(usuario.id == Valoracion.listado.usuario_id)\
                                     .filter(juego.id == Valoracion.videojuego.id)\
                                     .first()

        db.session.delete(valoracion)
        db.session.commit()

        return True

class GestionarListadoController():

    @staticmethod
    def obtenerJuego(nombre):
        return Videojuego.query.filter(nombre == Videojuego.nombre).first()


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
    def obtenerCuenta():
        return usuarioActual()

    @staticmethod
    def editar(cuenta, nombre, apellido, nuevaPassword, passwordActual, correo, imagen):
        if passwordActual == cuenta.password:
            cuenta.nombre = nombre
            cuenta.apellido = apellido
            cuenta.password = nuevaPassword
            cuenta.correo = correo
            cuenta.imagen = imagen

            db.session.commit()

class EliminarCuentaController():

    @staticmethod
    def obtenerCuenta():
        return usuarioActual()

    @staticmethod
    def eliminar(cuenta, password):
        if password == cuenta.password:
            db.session.delete(cuenta)
            db.session.commit()

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

