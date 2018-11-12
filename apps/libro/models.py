from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=250)
    subtitulo = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)
    categoria = models.CharField(max_length=250)
    fecha_publicacion = models.DateField()
    editor = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    imagen = models.FileField(upload_to='post_image', blank = True)

