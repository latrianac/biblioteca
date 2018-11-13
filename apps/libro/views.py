from django.shortcuts import render, redirect
from apps.libro.forms import LibroForm

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

