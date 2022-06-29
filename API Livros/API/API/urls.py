from django.urls import path, include

urlpatterns = [
    path('', include('livros.urls')),
]