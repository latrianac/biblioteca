from django.db import models

class LibroBusquedaGoogle(models.Model):
    titulo = models.CharField(max_length=250)

    def __str__(self):
        return self.titulo

class LibroGuardarGoogle(models.Model):
    identificacion = models.CharField(max_length=250)

    def __str__(self):
        return self.identificacion
