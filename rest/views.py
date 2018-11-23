from django.db.models import Q
from rest_framework import generics, mixins
from apps.libro.models import Libro
from rest.serializers import LibroSerializer


class LibroCreateView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field = 'pk'
    serializer_class = LibroSerializer
    # queryset = Libro.objects.all()

    def get_queryset(self):
        qs = Libro.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter((Q(titulo__icontains=query) | Q(subtitulo__icontains=query) |
                       Q(autor__icontains=query) | Q(categoria__icontains=query) |
                       Q(fecha_publicacion__icontains=query) | Q(editor__icontains=query) |
                       Q(descripcion__icontains=query) | Q(id__icontains=query))).distinct()
        return qs
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LibroRudView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = LibroSerializer
    # queryset = Libro.objects.all()

    def get_queryset(self):
        return Libro.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Libro.objects.get(pk=pk)