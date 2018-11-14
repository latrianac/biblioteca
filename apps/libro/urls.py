from django.urls import path, re_path
from apps.libro.views import index, libro_view, libro_list, libro_edit, libro_delete, LibroList, LibroCreate, LibroUpdate, LibroDelete

app_name = 'libro'
urlpatterns = [
    path('', index, name='inicio'),
    path('nuevo/', LibroCreate.as_view(), name='libro_crear'),
    path('listado/', LibroList.as_view(), name='libro_listar'),
    re_path(r'^editar/(?P<pk>\w+)$', LibroUpdate.as_view(), name='libro_editar'),
    re_path(r'^eliminar/(?P<pk>\w+)$', LibroDelete.as_view(), name='libro_eliminar'),
]
