from django.db.models import Q
from django.shortcuts import render
from apps.libro.forms import LibroForm
from apps.libro.models import Libro
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Funcion de inicio*******************************

def index(request):
    return render(request, 'libro/index.html')

#CRUD de libros**********************************

class LibroList(ListView):
    model = Libro
    template_name = 'libro/libro_list.html'


class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro_form.html'
    success_url = reverse_lazy('libro:libro_listar')

class LibroUpdate(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro_form.html'
    success_url = reverse_lazy('libro:libro_listar')

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'libro/libro_delete.html'
    success_url = reverse_lazy('libro:libro_listar')


# Buscador de libros en base de datos ************************************

class LibroSearch(ListView):
    template_name = 'libro/libro_search.html'

# Devuelve los resultados de la busqueda

    def get_context_data(self, *args, **kwargs):
        context = super(LibroSearch, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

# Recibe los terminos de busqueda

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            lookups = (Q(titulo__icontains=query) | Q(subtitulo__icontains=query) |
                       Q(autor__icontains=query) | Q(categoria__icontains=query) |
                       Q(fecha_publicacion__icontains=query) | Q(editor__icontains=query) |
                       Q(descripcion__icontains=query) | Q(id__icontains=query))
            return Libro.objects.filter(lookups).distinct()
        return Libro.objects.none()




