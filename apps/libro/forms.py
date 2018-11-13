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
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_publicacion':forms.DateInput(attrs={'class': 'form-control'}),
            'editor':forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'imagen':forms.FileInput(attrs={'class': 'form-control'}),


        }