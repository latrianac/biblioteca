from rest.views import LibroRudView, LibroCreateView

from django.urls import re_path

# app_name = 'libro'

urlpatterns = [

    re_path(r'^$', LibroCreateView.as_view(), name='libro-create'),
    re_path(r'^libro/(?P<pk>\w+)$', LibroRudView.as_view(), name='libro-rud'),
]