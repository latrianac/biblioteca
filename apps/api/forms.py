from django.forms import ModelForm, TextInput
from apps.api.models import LibroBusquedaGoogle

class LibroFormApi(ModelForm):

    class Meta:
        model = LibroBusquedaGoogle

        fields = ['titulo']

        labels = {
            'titulo': 'titulo',
        }
        widgets = {
            'titulo': TextInput(attrs={'class': 'form-control'}),


        }