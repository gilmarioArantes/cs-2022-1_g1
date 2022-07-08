import base64
from rest_framework import viewsets
from livros.serializers import AutorSerializer, LivroAdminSerializer, LivroSerializer
from livros.models import Livro, Autor
from django.http.response import HttpResponse
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from django.db.models.query import QuerySet

class LivroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LivroSerializer
    queryset = Livro.objects.all()
    
    def get_serializer(self, *args, **kwargs):
        if self.request.user.is_superuser:
            serializer_class = LivroAdminSerializer
        else:
            serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        if self.request.user.is_superuser:
            queryset = self.queryset
        else:
            queryset = self.queryset.filter(visibilidade=True)
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        return queryset

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied()

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            raise PermissionDenied()



class AutorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            raise PermissionDenied()

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            partial = True
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied()

def load_file(request, filename):
    with open(f'uploads/thumbnails/{filename}', "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    return HttpResponse(image_data)
