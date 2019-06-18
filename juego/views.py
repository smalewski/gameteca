from django.shortcuts import render
from Inicio.models import Videojuego

def index(request, videojuego_id):
    juego_filtrado = Videojuego.objects.filter(id = videojuego_id)
    context = {
        'juego_f' : juego_filtrado,
    }
    return render(request,'juegos.html',context)

def busqueda(request, videojuego_nombre):
    juegos = Videojuego.objects.filter(nombre__contains = videojuego_nombre)
    context = {
        'juegos_b' : juegos,
    }
    return render(request,'busqueda.html',context)
