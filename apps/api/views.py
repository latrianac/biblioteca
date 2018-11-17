import requests
from django.views.generic import CreateView, TemplateView
from django.shortcuts import render, redirect
from apps.api.forms import LibroFormApi, LibroIdApi
from apps.api.models import LibroBusquedaGoogle, LibroGuardarGoogle
from apps.libro.models import Libro
from django.urls import reverse_lazy

#Almacena los teminos de busqueda

class BookSearchApi(CreateView):
    model = LibroBusquedaGoogle
    form_class = LibroFormApi
    template_name = 'api/libro_google_form.html'
    success_url = reverse_lazy('api:listado')


#Muestra los resultados de la busqueda

def show_results(request):
    url = 'https://www.googleapis.com/books/v1/volumes?q={}:keyes&key=AIzaSyAzUU11BZnc-IKjnzsrz7fp2oyPYv-Bng8'
    ultima_busqueda = LibroBusquedaGoogle.objects.latest('id')
    libro = str(ultima_busqueda)
    libro_contexts = []
    search_request_api_valid_fields(libro, url, libro_contexts)
    context = {'libro_contexts': libro_contexts}
    print(libro_contexts[0]['publishedDate'].split("-"))
    return render(request, 'api/libro_google_search.html', context)

class BookSaveApi(CreateView):
    model = LibroGuardarGoogle
    form_class = LibroIdApi
    template_name = 'api/libro_save_form.html'
    success_url = reverse_lazy('api:exito')


def save_book_database(request):

    url = 'https://www.googleapis.com/books/v1/volumes?q={}:keyes&key=AIzaSyAzUU11BZnc-IKjnzsrz7fp2oyPYv-Bng8'
    id_libro = str(LibroGuardarGoogle.objects.latest('id'))
    print(id_libro)
    ultima_busqueda = LibroBusquedaGoogle.objects.latest('id')
    libro = str(ultima_busqueda)
    libro_contexts = []
    search_request_api_valid_fields(libro, url, libro_contexts)
    print(libro_contexts)
    i = 0
    for libro in libro_contexts:
        if libro['id'] == id_libro:
            Libro.objects.create(
                titulo=libro_contexts[i]['title'],
                subtitulo=libro_contexts[i]['subtitle'],
                autor=libro_contexts[i]['authors'][0],
                categoria=libro_contexts[i]['categories'][0],
                fecha_publicacion=libro_contexts[i]['publishedDate'],
                editor=libro_contexts[i]['publisher'],
                descripcion=libro_contexts[i]['description'],
            )

        i = i + 1
    return render(request, 'api/libro_saved.html', {})

#Busca campos disponibles en la API

def search_request_api_valid_fields(libro, url, libro_contexts):
    campos_consulta = ['title', 'subtitle', 'authors', 'categories', 'publishedDate', 'publisher', 'description', 'imageLinks']
    r = requests.get(url.format(libro)).json()
    j = 0
    try:
        while j<10:
            consultas = {}
            consultas['id'] = r['items'][j]['id']
            for campo in campos_consulta:
                try:
                    dato_libro = r['items'][j]['volumeInfo'][campo]
                    consultas[campo]= dato_libro
                except:
                    consultas[campo]='-'
            libro_contexts.append(consultas)
            j = j + 1
        consultas['search_keyword']=libro

    except:
        print("Cambie los terminos de busqueda e intentelo de nuevo")



