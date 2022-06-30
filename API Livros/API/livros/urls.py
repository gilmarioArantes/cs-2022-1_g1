from django.urls import path, include
from livros.views import LivroViewSet, AutorViewSet, load_file
from rest_framework import routers

listar_livros = LivroViewSet.as_view({
    'get': 'list',
})

adicionar_livro = LivroViewSet.as_view({
    'post': 'create',
})

retornar_livro = LivroViewSet.as_view({
    'get': 'retrieve',
})

deletar_livro = LivroViewSet.as_view({
    'delete': 'destroy'
})

editar_livro = LivroViewSet.as_view({
    'put': 'update'
})

listar_autores = AutorViewSet.as_view({
    'get': 'list',
})

adicionar_autor = AutorViewSet.as_view({
    'post': 'create',
})

retornar_autor = AutorViewSet.as_view({
    'get': 'retrieve',
})

deletar_autor = AutorViewSet.as_view({
    'delete': 'destroy'
})

editar_autor = AutorViewSet.as_view({
    'put': 'update'
})


urlpatterns = [
   path('livros/', listar_livros, name='listar-livros'),
   path('adicionar-livro/', adicionar_livro, name='adicionar-livro'),
   path('livros/<uuid:pk>/', retornar_livro, name='retornar-livro'),
   path('deletar-livro/<uuid:pk>/', deletar_livro, name='deletar-livro'),
   path('editar-livro/<uuid:pk>/', editar_livro, name='editar-livro'),
   path('autores/', listar_autores, name='listar-autores'),
   path('adicionar-autor/', adicionar_autor, name='adicionar-autor'),
   path('autores/<uuid:pk>/', retornar_autor, name='retornar-autor'),
   path('deletar-autor/<uuid:pk>/', deletar_autor, name='deletar-autor'),
   path('editar-autor/<uuid:pk>/', editar_autor, name='editar-autor'),
   path('uploads/thumbnails/<str:filename>/', load_file, name='load-file'),
]
