from django.shortcuts import render, redirect
from apps.libro.forms import LibroForm
from apps.libro.models import Libro
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    libro = Libro.objects.all().order_by('id')
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

def libro_delete(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro:libro_listar')
    return render(request, 'libro/libro_delete.html', {'libro': libro})



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

