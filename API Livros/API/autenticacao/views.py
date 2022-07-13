from django.shortcuts import render
from rest_framework import viewsets
from autenticacao.serializers import UserSerializer
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


    def create(self, request, *args, **kwargs):
        can_add_user = False
        if 'is_superuser' in request.data:
            target_user_admin = request.data['is_superuser']
            if not target_user_admin or request.user.is_superuser:
                can_add_user = True

        if can_add_user:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        can_delete_user = False
        if request.user.is_superuser:
            can_delete_user = True
        elif request.user.username == self.get_object().username:
            can_delete_user = True

        if can_delete_user:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied()

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied()

    def retrieve(self, request, *args, **kwargs):
        can_retrieve_user = False
        if request.user.is_superuser:
            can_retrieve_user = True
        elif request.user.username == self.get_object().username:
            can_retrieve_user = True

        if can_retrieve_user:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            raise PermissionDenied()


    def update(self, request, *args, **kwargs):
        can_update_user = False
        if 'is_superuser' in request.data:
            target_user_admin = request.data['is_superuser']
            if not target_user_admin or request.user.is_superuser:
                can_update_user = True
            elif target_user_admin and not request.user.is_superuser:
                raise PermissionDenied()

        if request.user.pk == self.get_object().pk:
            can_update_user = True

        if can_update_user:
            partial = True
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            raise PermissionDenied()

