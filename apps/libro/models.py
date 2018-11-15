from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=250)
    subtitulo = models.CharField(max_length=250, null=True, blank = True)
    autor = models.CharField(max_length=250, null=True, blank = True)
    categoria = models.CharField(max_length=250, null=True, blank = True)
    fecha_publicacion = models.DateField(null=True, blank = True)
    editor = models.CharField(max_length=250, null=True, blank = True)
    descripcion = models.CharField(max_length=250, null=True, blank = True)
    imagen = models.FileField(upload_to='libros/', null=True, blank = True)

    def __str__(self):
        return self.titulo

    def __unicode__(self):
        return self.titulo

