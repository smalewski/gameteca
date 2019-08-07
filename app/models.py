# db.Modelos

import enum

from app import db


#
# Tablas de asociación
#
videojuego_genero_table = db.Table('videojuego_genero',
    db.Column('videojuego_id', db.Integer, db.ForeignKey('videojuego.id'), primary_key=True),
    db.Column('genero_id', db.Integer, db.ForeignKey('genero.id'), primary_key=True)
)

videojuego_plataforma_table = db.Table('videojuego_plataforma',
    db.Column('videojuego_id', db.Integer, db.ForeignKey('videojuego.id'), primary_key=True),
    db.Column('plataforma_id', db.Integer, db.ForeignKey('plataforma.id'), primary_key=True)
)

#
# Clases para los modelos
#

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    correo = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(50))
    imagen = db.Column(db.String(1000))
    descripcion = db.Column(db.String(1000))

    # Flask_Login
    conectado = db.Column(db.Boolean, default=False)

    def __init__(self, username, nombre, apellido, correo, password, imagen=None):
        self.username = username
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        self.imagen = imagen

    def __repr__(self):
        return f"<Usuario {self.username}>"

    # Flask_Login
    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.conectado

    def is_anonymous(self):
        return False


class Admin(Usuario):
    pass

class UsuarioComun(Usuario):
    lista = db.relationship("ListadoVideojuegos", uselist=False)

class Videojuego(db.Model):
    __tablename__ = 'videojuego'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    fecha_estreno = db.Column(db.Date)
    imagen = db.Column(db.String(120))

    generos = db.relationship("Genero",
                          secondary=videojuego_genero_table,
                          backref=db.backref("videojuego", lazy=True))
    plataformas = db.relationship("Plataforma",
                              secondary=videojuego_plataforma_table,
                              backref=db.backref("videojuego", lazy=True))
    listados = db.relationship("Valoracion")

    def __init__(self, nombre, fecha_estreno, imagen=None):
        self.nombre = nombre
        self.fecha_estreno = fecha_estreno
        self.imagen = imagen

    def __repr__(self):
        return f"<Videojuego {self.nombre}>"


class Plataforma(db.Model):
    __tablename__ = 'plataforma'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    fecha_estreno = db.Column(db.Date)
    marca = db.Column(db.String(100))
    imagen = db.Column(db.String(120))

    videojuegos = db.relationship("Videojuego",
                               secondary=videojuego_plataforma_table,
                               backref=db.backref("plataforma", lazy=True))

    def __init__(self, nombre, fecha_estreno, marca, imagen=None):
        self.nombre = nombre
        self.fecha_estreno = fecha_estreno
        self.marca = marca
        self.imagen = imagen

    def __repr__(self):
        return f"<Plataforma {self.nombre}>"

class Genero(db.Model):
    __tablename__ = 'genero'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))

    videojuegos = db.relationship("Videojuego",
                               secondary=videojuego_genero_table,
                               backref=db.backref("genero", lazy=True))

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"<Genero {self.nombre}>"


class Temas(enum.Enum):
    oscuro = 1
    claro = 2

class ListadoVideojuegos(db.Model):
    __tablename__ = 'listado'
    id = db.Column(db.Integer, primary_key=True)
    cabecera = db.Column(db.String(100))
    tema = db.Column(db.Enum(Temas))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    usuario = db.relationship("UsuarioComun", uselist=False)
    juegos = db.relationship("Valoracion")

    def __init__(self, user_id, cabecera, tema):
        self.cabecera = cabecera
        self.tema = tema
        self.usuario_id = user_id

    def __repr__(self):
        return f"<ListadoVideojuegos {self.id}>"


class Valoracion(db.Model):
    __tablename__ = 'valoracion'
    listado_id = db.Column(db.Integer, db.ForeignKey('listado.id'), primary_key=True)
    videojuego_id = db.Column(db.Integer, db.ForeignKey('videojuego.id'), primary_key=True)
    listado = db.relationship("ListadoVideojuegos", backref=db.backref("valoracion", lazy=True))
    videojuego = db.relationship("Videojuego", backref=db.backref("valoracion", lazy=True))

    horas = db.Column(db.Integer)
    puntuacion = db.Column(db.Integer)
    comentario = db.Column(db.String(1000))

    def __init__(self, horas, puntuacion, comentario):
        self.horas = horas
        self.puntuacion = puntuacion
        self.comentario = comentario

    def __repr__(self):
        return f"<Valoracion {self.listado.usuario.username} {self.videojuego.nombre} - {self.horas} {self.puntuacion}>"
