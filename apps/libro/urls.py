from django.urls import path, re_path
from apps.libro.views import index, libro_view, libro_list, libro_edit, libro_delete

app_name = 'libro'
urlpatterns = [
    path('', index, name= 'inicio'),
    path('nuevo/', libro_view, name='libro_crear'),
    path('listado/', libro_list, name='libro_listar'),
    re_path(r'^editar/(?P<id_libro>\w+)$', libro_edit, name='libro_editar'),
    re_path(r'^eliminar/(?P<id_libro>\w+)$', libro_delete, name='libro_eliminar'),
]
