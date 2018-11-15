from django.db import models

class LibroBusquedaGoogle(models.Model):
    titulo = models.CharField(max_length=250)

    def __str__(self):
        return self.titulo



