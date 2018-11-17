from django import forms
from apps.api.models import LibroBusquedaGoogle, LibroGuardarGoogle


class LibroFormApi(forms.ModelForm):

    class Meta:
        model = LibroBusquedaGoogle
        fields = ['titulo']
        labels = {'titulo': 'titulo'}
        widgets = {'titulo': forms.TextInput(attrs={'class': 'form-control'})}

class LibroIdApi(forms.ModelForm):
    class Meta:
        model = LibroGuardarGoogle
        fields = ['identificacion']
        labels = {'identificacion':'identifiacion'}
        widgets = {'identificacion':forms.TextInput(attrs={'class': 'form-control'})}





