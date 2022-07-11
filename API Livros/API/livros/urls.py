from django.urls import path, include
from livros.views import *
from rest_framework import routers

urlpatterns = [
   path('livros/', LivroViewSet.as_view({'get': 'list'}), name='listar-livros'),
   path('adicionar-livro/', LivroViewSet.as_view({'post': 'create'}), name='adicionar-livro'),
   path('livros/<uuid:pk>/', LivroViewSet.as_view({'get': 'retrieve'}), name='retornar-livro'),
   path('deletar-livro/<uuid:pk>/', LivroViewSet.as_view({'delete': 'destroy'}), name='deletar-livro'),
   path('editar-livro/<uuid:pk>/', LivroViewSet.as_view({'put': 'update'}), name='editar-livro'),
   path('livros/favoritos/', LivroViewSet.as_view({'get': 'listar_favoritos'}), name='livros-favoritos'),
   path('livros/favoritar/<uuid:pk>/', LivroViewSet.as_view({'put': 'favoritar'}), name='favoritar-livro'),
   path('livros/desfavoritar/<uuid:pk>/', LivroViewSet.as_view({'put': 'desfavoritar'}), name='desfavoritar-livro'),
   path('autores/', AutorViewSet.as_view({'get': 'list'}), name='listar-autores'),
   path('adicionar-autor/', AutorViewSet.as_view({'post': 'create'}), name='adicionar-autor'),
   path('autores/<uuid:pk>/', AutorViewSet.as_view({'get': 'retrieve'}), name='retornar-autor'),
   path('deletar-autor/<uuid:pk>/', AutorViewSet.as_view({'delete': 'destroy'}), name='deletar-autor'),
   path('editar-autor/<uuid:pk>/', AutorViewSet.as_view({'put': 'update'}), name='editar-autor'),
   path('uploads/thumbnails/<str:filename>/', load_file, name='load-file'),
]