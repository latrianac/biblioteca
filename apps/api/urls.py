from django.urls import path
from apps.api.views import show_results, BookSearchApi, BookSaveApi, save_book_database

app_name = 'api'
urlpatterns = [
    path('book/', show_results, name='listado'),
    path('buscar/', BookSearchApi.as_view(), name='search'),
    path('save/', BookSaveApi.as_view(), name='save'),
    path('exito/', save_book_database, name='exito'),

]
