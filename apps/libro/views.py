from django.shortcuts import render, redirect
from apps.libro.forms import LibroForm
from django.views.generic import ListView
from apps.libro.models import Libro

def index(request):
    return render(request, 'libro/index.html')

def libro_view(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = LibroForm()

    return render(request, 'libro/libro_form.html', {'form': form})


def libro_list(request):
    libro = Libro.objects.all()
    contexto = {'libros':libro}
    return render(request, 'libro/libro_list.html', contexto)

def libro_edit(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    if request.method == 'GET':
        form = LibroForm(instance=libro)
    else:
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
        return redirect('libro_listar')
    return render(request, 'libro/libro_form.html', {'form': form})



#class LibroList(ListView):
#    model = Libro
#    template_name = 'libro/libro_list.html'