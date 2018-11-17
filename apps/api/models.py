from django.db import models

# Modelo que guarda las busquedas realizadas por el usuario
class LibroBusquedaGoogle(models.Model):
    titulo = models.CharField(max_length=250)

    def __str__(self):
        return self.titulo


# Modelo que guarda los id buscador por el usuario

class LibroGuardarGoogle(models.Model):
    identificacion = models.CharField(max_length=250)

    def __str__(self):
        return self.identificacion
