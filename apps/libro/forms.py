from django import forms
from apps.libro.models import Libro

class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro

        fields = [
            'titulo',
            'subtitulo',
            'autor',
            'categoria',
            'fecha_publicacion',
            'editor',
            'descripcion',
            'imagen',
        ]

        labels = {
            'titulo': 'Nombre',
            'subtitulo': 'Subtitulo',
            'autor': 'Autor',
            'categoria': 'Categoria',
            'fecha_publicacion': 'Fecha de publicacion',
            'editor': 'Editor',
            'descripcion': 'Descripcion',
            'imagen': 'Imagen',

        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'from-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'from-control'}),
            'autor': forms.TextInput(attrs={'class': 'from-control'}),
            'categoria':forms.TextInput(attrs={'class': 'from-control'}),
            'fecha_publicacion':forms.TextInput(attrs={'class': 'from-control'}),
            'editor':forms.TextInput(attrs={'class': 'from-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'from-control'}),
            'imagen':forms.TextInput(attrs={'class': 'from-control'}),


        }