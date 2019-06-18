from django.db import models
from datetime import datetime

class Videojuego(models.Model):
    caratula = models.CharField(max_length = 500)
    nombre = models.CharField(max_length = 50)
    fecha = models.CharField(max_length = 50)

    def __str__(self):
        return self.caratula + ' I ' + self.nombre + ' I ' + self.fecha
