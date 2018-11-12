from django.urls import path
from apps.libro.views import index, libro_view

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', libro_view, name='libro_crear'),
]
