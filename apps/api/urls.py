from django.urls import path
from apps.api.views import index

app_name = 'api'
urlpatterns = [
    path('book/', index, name='search'),
]
