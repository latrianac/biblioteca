import requests
from django.shortcuts import render
from apps.api.forms import LibroFormApi
from apps.api.models import LibroBusquedaGoogle

def index(request):

    url = 'https://www.googleapis.com/books/v1/volumes?q={}:keyes&key=AIzaSyAzUU11BZnc-IKjnzsrz7fp2oyPYv-Bng8'
    if request.method == 'POST':
        form = LibroFormApi(request.POST)
        form.save()
        pass

    form = LibroFormApi()

    libro = LibroBusquedaGoogle.objects.get(pk=1)

    libro_contexts = []
    construir_consulta_campos_exitentes(libro, url, libro_contexts)
    context = {'libro_contexts': libro_contexts, 'form':form}
    return render(request, 'api/libro_google_search.html', context)

def construir_consulta_campos_exitentes(libro, url, libro_contexts):
    campos_consulta = ['title', 'subtitle', 'authors', 'categories', 'publishedDate', 'publisher', 'description', 'imageLinks']
    r = requests.get(url.format(libro)).json()
    j = 0
    try:
        while j<10:
            consultas = {}
            for campo in campos_consulta:
                try:
                    dato_libro = r['items'][j]['volumeInfo'][campo]
                    consultas[campo]= dato_libro
                except:
                    consultas[campo]='-'
            libro_contexts.append(consultas)
            j = j + 1
    except:
        print("Cambie los terminos de busqueda e intentelo de nuevo")

