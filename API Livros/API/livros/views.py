import base64
from rest_framework import viewsets

from livros.serializers import LivroSerializer, AutorSerializer
from livros.models import Livro, Autor
from django.http.response import HttpResponse

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


def load_file(request, filename):
    with open(f'uploads/thumbnails/{filename}', "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    return HttpResponse(image_data)
