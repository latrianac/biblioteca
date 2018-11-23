from rest_framework import serializers
from apps.libro.models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = [
            'pk',
            'titulo',
            'subtitulo',
            'autor',
            'categoria',
            'fecha_publicacion',
            'editor',
            'descripcion',
            'imagen',
        ]
        read_only_fields = ['pk']