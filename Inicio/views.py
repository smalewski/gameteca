from django.shortcuts import render
from .models import Videojuego

def index(request):
    todos_juegos = Videojuego.objects.all()
    context = {
        'todos_juegos' : todos_juegos,
        'i' : 0
    }
    return render(request,'index.html',context)
