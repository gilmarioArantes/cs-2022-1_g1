from django.urls import path, include

urlpatterns = [
    path('', include('livros.urls')),
    path('', include('autenticacao.urls')),
]