from django.urls import path
from . import views
urlpatterns = [
    path('<int:videojuego_id>/',views.index, name = 'index'),
    path('<str:videojuego_nombre>/',views.busqueda, name = 'index'),
]
