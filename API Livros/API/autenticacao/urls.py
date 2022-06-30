from django.urls import path, include
from autenticacao.views import UserViewSet
from rest_framework import routers

listar_usuarios = UserViewSet.as_view({
    'get': 'list',
})

adicionar_usuario = UserViewSet.as_view({
    'post': 'create',
})

retornar_usuario = UserViewSet.as_view({
    'get': 'retrieve',
})

deletar_usuario = UserViewSet.as_view({
    'delete': 'destroy'
})

editar_usuario = UserViewSet.as_view({
    'put': 'update'
})

urlpatterns = [
   path('usuarios/', listar_usuarios, name='listar-usuarios'),
   path('adicionar-usuario/', adicionar_usuario, name='adicionar-usuario'),
   path('usuarios/<int:pk>/', retornar_usuario, name='retornar-usuario'),
   path('deletar-usuario/<int:pk>/', deletar_usuario, name='deletar-usuario'),
   path('editar-usuario/<int:pk>/', editar_usuario, name='editar-usuario'),
]
