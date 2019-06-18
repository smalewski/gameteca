from django.shortcuts import render
from Inicio.models import Videojuego

def index(request, videojuego_id):
    juego_filtrado = Videojuego.objects.filter(id = videojuego_id)
    context = {
        'juego_f' : juego_filtrado,
    }
    return render(request,'juegos.html',context)
