from datetime import datetime

def verificarNombre(nombre):
    return True

def verificarJuego(juego):
    return True

def verificarCorreo(correo):
    return True

def verificarHoras(horas):
    return 0 <= horas

def verificarValoracion(puntaje):
    return 0 <= puntaje and puntaje <= 100

def verificarPassword(password):
    return True

def verificarFecha(fecha):
    return True

def verificarID(idn):
    return True

def parseFecha(str):
    fecha = datetime.strptime(str, "%Y-%m-%d")
    if fecha is None:
        fecha = datetime.now()
    return fecha
