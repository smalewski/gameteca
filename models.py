# Modelos

import enum

from sqlalchemy import Table, Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

from gameteca.database import Base, db_session

#
# Tablas de asociación
#

videojuego_genero_table = Table('videojuego_genero', Base.metadata,
    Column('videojuego_id', Integer, ForeignKey('videojuego.id')),
    Column('genero_id', Integer, ForeignKey('genero.id'))
)

videojuego_plataforma_table = Table('videojuego_plataforma', Base.metadata,
    Column('videojuego_id', Integer, ForeignKey('videojuego.id')),
    Column('plataforma_id', Integer, ForeignKey('plataforma.id'))
)

videojuego_listado_table = Table('videojuego_listado', Base.metadata,
    Column('videojuego_id', Integer, ForeignKey('videojuego.id')),
    Column('listado_id', Integer, ForeignKey('listado.id'))
)

#
# Clases para los modelos
#

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    correo = Column(String(120), unique=True)
    password = Column(String(50))
    imagen = Column(String(120))

    def __init__(self, username, nombre, apellido, correo, password, imagen=None):
        self.username = username
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        self.imagen = imagen

    def __repr__(self):
        return f"<Usuario {self.username}>"

    def buscar(self, nombre):
        usuarios = self.query.filter(Usuario.username.ilike(f"%{nombre}%")).all()
        return usuarios


class Admin(Usuario):
    pass

class UsuarioComun(Usuario):
    lista = relationship("ListadoVideojuegos", uselist=False, back_populates="usuario")

class Videojuego(Base):
    __tablename__ = 'videojuego'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    fecha_estreno = Column(Date)
    imagen = Column(String(120))

    generos = relationship("Genero",
                          secondary=videojuego_genero_table,
                          back_populates="videojuego")
    plataformas = relationship("Plataforma",
                              secondary=videojuego_plataforma_table,
                              back_populates="videojuego")
    listados = relationship("ListadoVideojuegos",
                            secondary=videojuego_listado_table,
                            back_populates="videojuego")

    def __init__(self, nombre, fecha_estreno, imagen=None):
        self.nombre = nombre
        self.fecha_estreno = fecha_estreno
        self.imagen = imagen

    def __repr__(self):
        return f"<Videojuego {self.nombre}>"

    def buscar(self, nombre):
        juegos = self.query.filter(Videojuego.nombre.ilike(f"%{nombre}%")).all()
        return juegos

    def obtenerVideojuegos(self):
        juegos = self.query.all()
        return juegos


class Plataforma(Base):
    __tablename__ = 'plataforma'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    fecha_estreno = Column(Date)
    marca = Column(String(100))
    imagen = Column(String(120))

    videojuegos = relationship("Videojuego",
                               secondary=videojuego_plataforma_table,
                               back_populates="plataforma")

    def __init__(self, nombre, fecha_estreno, marca, imagen=None):
        self.nombre = nombre
        self.fecha_estreno = fecha_estreno
        self.marca = marca
        self.imagen = imagen

    def __repr__(self):
        return f"<Plataforma {self.nombre}>"

class Genero(Base):
    __tablename__ = 'genero'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))

    videojuegos = relationship("Videojuego",
                               secondary=videojuego_genero_table,
                               back_populates="genero")

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"<Genero {self.nombre}>"

class Temas(enum.Enum):
    oscuro = 1
    claro = 2

class ListadoVideojuegos(Base):
    __tablename__ = 'listado'
    id = Column(Integer, primary_key=True)
    cabecera = Column(String(100))
    tema = Column(Enum(Temas))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    usuario = relationship("UsuarioComun", uselist=False, back_populates="listado")
    juegos = relationship("Videojuego",
                          secondary=videojuego_listado_table,
                          back_populates="listado")

    def __init__(self, cabecera, tema):
        self.cabecera = cabecera
        self.tema = tema

    def __repr__(self):
        return f"<ListadoVideojuegos {self.id}>"

    def buscar(self, usuario):
        listado = self.query.filter(ListadoVideojuegos.usuario_id == usuario).one_or_none()
        return listado

    def anadirJuego(self, idJuego):
        juego = Videojuego.query.filter(Videojuego.id == idJuego).one_or_none()

        if juego is not None:
            try:
                self.juegos.append(juego)
                db_session.commit()
                return True
            except:
                return False

        return False

