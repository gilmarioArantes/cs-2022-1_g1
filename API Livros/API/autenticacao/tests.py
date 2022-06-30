from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from requests.auth import HTTPBasicAuth
from .views import UserViewSet
from rest_framework.renderers import JSONRenderer
import json

class UserTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.administrador = User.objects.create_user(
                                        username="administrador",
                                        password="Testando123@",
                                        email="teste@gmail.com",
                                        is_superuser=True,
                                        first_name="Admi",
                                        last_name="Nistrador",
                                    )
        self.administrador2 = User.objects.create_user(
                                        username="administrador2",
                                        password="Testando123@",
                                        email="teste2@gmail.com",
                                        is_superuser=True,
                                        first_name="Admi",
                                        last_name="Nistrador",
                                    )

        self.usuario_comum = User.objects.create_user(
                                        username="usuario_comum",
                                        password="Testando123@",
                                        email="usuario_comum@gmail.com",
                                        is_superuser=False,
                                        first_name="Usuário",
                                        last_name="Comum",
                                    )

        self.usuario_comum2 = User.objects.create_user(
                                        username="usuario_comum2",
                                        password="Testando123@",
                                        email="usuario_comum2@gmail.com",
                                        is_superuser=False,
                                        first_name="Usuário",
                                        last_name="Comum",
                                    )

    def test_admin_criar_admin(self):
        usuario = {
            'username': 'usuario1',
            'password': 'Testando123@',
            'email': 'usuario1@gmail.com',
            'is_superuser': True,
            'first_name': 'Nome',
            'last_name': 'Usuário',
        }

        view = UserViewSet.as_view({'post': 'create'})
        request = self.factory.post('/adicionar-usuario/', usuario, format="json")
        response = make_request(view, request, self.administrador)
        self.assertTrue(User.objects.filter(username='usuario1').exists())
        self.assertTrue(response['status_code'] == 201)

    def test_admin_criar_user(self):
        usuario = {
            'username': 'usuario2',
            'password': 'Testando123@',
            'email': 'usuario2@gmail.com',
            'is_superuser': False,
            'first_name': 'Nome',
            'last_name': 'Usuário',
        }

        view = UserViewSet.as_view({'post': 'create'})
        request = self.factory.post('/adicionar-usuario/', usuario, format="json")
        response = make_request(view, request, self.administrador)
        self.assertTrue(User.objects.filter(username='usuario2').exists())
        self.assertTrue(response['status_code'] == 201)


    def test_visitante_criar_user(self):
        usuario = {
            'username': 'usuario3',
            'password': 'Testando123@',
            'email': 'usuario3@gmail.com',
            'is_superuser': False,
            'first_name': 'Nome',
            'last_name': 'Usuário',
        }

        view = UserViewSet.as_view({'post': 'create'})
        request = self.factory.post('/adicionar-usuario/', usuario, format="json")
        response = make_request(view, request)
        self.assertTrue(User.objects.filter(username='usuario3').exists())
        self.assertTrue(response['status_code'] == 201)

    def test_visitante_criar_admin(self):
        usuario = {
            'username': 'usuario4',
            'password': 'Testando123@',
            'email': 'usuario4@gmail.com',
            'is_superuser': True,
            'first_name': 'Nome',
            'last_name': 'Usuário',
        }

        view = UserViewSet.as_view({'post': 'create'})
        request = self.factory.post('/adicionar-usuario/', usuario, format="json")
        response = make_request(view, request)
        self.assertFalse(User.objects.filter(username='usuario4').exists())
        self.assertTrue(response['status_code'] == 403)

    def test_admin_get_users(self):
        view = UserViewSet.as_view({'get': 'list'})
        request = self.factory.get('/usuarios/', format="json")
        response = make_request(view, request, self.administrador)
        self.assertTrue(response['status_code'] == 200)

    def test_user_get_users(self):
        view = UserViewSet.as_view({'get': 'list'})
        request = self.factory.get('/usuarios/', format="json")
        response = make_request(view, request, self.usuario_comum)
        self.assertTrue(response['status_code'] == 403)

    def test_visitante_get_users(self):
        view = UserViewSet.as_view({'get': 'list'})
        request = self.factory.get('/usuarios/', format="json")
        response = make_request(view, request)
        self.assertTrue(response['status_code'] == 401)

    def test_admin_delete_himself(self):
        view = UserViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/deletar-usuario/{self.administrador.pk}/', format="json")
        response = make_request(view, request, self.administrador, self.administrador.pk)
        self.assertTrue(response['status_code'] == 204)
        self.assertFalse(User.objects.filter(pk=self.administrador.pk).exists())

    def test_admin_delete_another_admin(self):
        view = UserViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/deletar-usuario/{self.administrador2.pk}/', format="json")
        response = make_request(view, request, self.administrador, self.administrador2.pk)
        self.assertTrue(response['status_code'] == 204)
        self.assertFalse(User.objects.filter(pk=self.administrador2.pk).exists())

    def test_admin_delete_user(self):
        view = UserViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/deletar-usuario/{self.usuario_comum.pk}/', format="json")
        response = make_request(view, request, self.administrador, self.usuario_comum.pk)
        self.assertTrue(response['status_code'] == 204)
        self.assertFalse(User.objects.filter(pk=self.usuario_comum.pk).exists())

    def test_user_delete_admin(self):
        view = UserViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/deletar-usuario/{self.administrador.pk}/', format="json")
        response = make_request(view, request, self.usuario_comum, self.administrador.pk)
        self.assertTrue(response['status_code'] == 403)
        self.assertTrue(User.objects.filter(pk=self.administrador.pk).exists())

    def test_user_delete_himself(self):
        view = UserViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/deletar-usuario/{self.usuario_comum.pk}/', format="json")
        response = make_request(view, request, self.usuario_comum, self.usuario_comum.pk)
        self.assertTrue(response['status_code'] == 204)
        self.assertFalse(User.objects.filter(pk=self.usuario_comum.pk).exists())

    def test_user_delete_another_user(self):
        view = UserViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/deletar-usuario/{self.usuario_comum2.pk}/', format="json")
        response = make_request(view, request, self.usuario_comum, self.usuario_comum2.pk)
        self.assertTrue(response['status_code'] == 403)
        self.assertTrue(User.objects.filter(pk=self.usuario_comum2.pk).exists())

    def test_visitante_delete_someone(self):
        view = UserViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/deletar-usuario/{self.usuario_comum.pk}/', format="json")
        response = make_request(view, request, pk=self.usuario_comum.pk)
        self.assertTrue(response['status_code'] == 401)
        self.assertTrue(User.objects.filter(pk=self.usuario_comum.pk).exists())

    def test_admin_retrieve_admin(self):
        view = UserViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/usuarios/{self.administrador2.pk}/', format="json")
        response = make_request(view, request, self.administrador, self.administrador2.pk)
        self.assertTrue(response['status_code'] == 200)

    def test_admin_retrieve_user(self):
        view = UserViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/usuarios/{self.usuario_comum.pk}/', format="json")
        response = make_request(view, request, self.administrador, self.usuario_comum.pk)
        self.assertTrue(response['status_code'] == 200)

    def test_user_retrieve_himself(self):
        view = UserViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/usuarios/{self.usuario_comum.pk}/', format="json")
        response = make_request(view, request, self.usuario_comum, self.usuario_comum.pk)
        self.assertTrue(response['status_code'] == 200)

    def test_user_retrieve_another_user(self):
        view = UserViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/usuarios/{self.usuario_comum2.pk}/', format="json")
        response = make_request(view, request, self.usuario_comum, self.usuario_comum2.pk)
        self.assertTrue(response['status_code'] == 403)

    def test_user_retrieve_admin(self):
        view = UserViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/usuarios/{self.administrador.pk}/', format="json")
        response = make_request(view, request, self.usuario_comum, self.administrador.pk)
        self.assertTrue(response['status_code'] == 403)

    def test_visitante_retrieve_someone(self):
        view = UserViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/usuarios/{self.usuario_comum.pk}/', format="json")
        response = make_request(view, request, pk=self.usuario_comum.pk)
        self.assertTrue(response['status_code'] == 401)

    def test_admin_editar_para_admin(self):
        usuario = {
            'is_superuser': True,
        }

        view = UserViewSet.as_view({'put': 'update'})
        request = self.factory.put(f'/editar-usuario/{self.usuario_comum.pk}/', usuario, format="json")
        response = make_request(view, request, self.administrador, self.usuario_comum.pk)
        self.assertTrue(response['status_code'] == 200)
        self.assertTrue(User.objects.get(pk=self.usuario_comum.pk).is_superuser)

    def test_user_editar_para_admin(self):
        usuario = {
            'is_superuser': True,
        }

        view = UserViewSet.as_view({'put': 'update'})
        request = self.factory.put(f'/editar-usuario/{self.usuario_comum2.pk}/', usuario, format="json")
        response = make_request(view, request, self.usuario_comum, self.usuario_comum2.pk)
        self.assertTrue(response['status_code'] == 403)
        self.assertFalse(User.objects.get(pk=self.usuario_comum2.pk).is_superuser)

    def test_user_edit_himself_toadmin(self):
        usuario = {
            'is_superuser': True,
        }

        view = UserViewSet.as_view({'put': 'update'})
        request = self.factory.put(f'/editar-usuario/{self.usuario_comum.pk}/', usuario, format="json")
        response = make_request(view, request, self.usuario_comum, self.usuario_comum.pk)
        self.assertTrue(response['status_code'] == 403)
        self.assertFalse(User.objects.get(pk=self.usuario_comum.pk).is_superuser)

    def test_visitante_editar_user(self):
        usuario = {
            'first_name': "TESTE",
        }

        view = UserViewSet.as_view({'put': 'update'})
        request = self.factory.put(f'/editar-usuario/{self.usuario_comum.pk}/', usuario, format="json")
        response = make_request(view, request, pk=self.usuario_comum.pk)
        self.assertTrue(response['status_code'] == 401)


def make_request(view, request, user=None, pk=None):
    if user:
        force_authenticate(request, user)
    response = view(request, pk=pk) if pk else view(request)
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = "application/json"
    response.renderer_context = {}
    response.render()
    json_response = json.loads(response.content.decode()) if response.content else None
    return {'status_code': response.status_code, 'content': json_response}