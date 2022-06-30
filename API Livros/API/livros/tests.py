from django.test import TestCase
from .models import Livro, Autor
from rest_framework.test import APIRequestFactory, force_authenticate
from requests.auth import HTTPBasicAuth
from .views import AutorViewSet, LivroViewSet
from rest_framework.renderers import JSONRenderer
import json
import requests
from django.contrib.auth.models import User


"""class AutorTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.autor = Autor.objects.create(
                                    nome="Fulano de Tal",
                                    data_nascimento="2022-06-30",
                                )

        self.administrador = User.objects.create_user(
                                        username="administrador",
                                        password="Testando123@",
                                        email="teste@gmail.com",
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

    def test_admin_criar_autor(self):
        autor = {
            'nome': 'Ricardo Almeida',
            'data_nascimento': '2000-01-01',
        }

        view = AutorViewSet.as_view({'post': 'create'})
        request = self.factory.post('/adicionar-autor/', autor, format="json")
        response = make_request(view, request, user=self.administrador)
        self.assertTrue(Autor.objects.filter(nome='Ricardo Almeida').exists())
        self.assertTrue(response['status_code'] == 201)

    def test_user_criar_autor(self):
        autor = {
            'nome': 'Ricardo Almeida',
            'data_nascimento': '2000-01-01',
        }

        view = AutorViewSet.as_view({'post': 'create'})
        request = self.factory.post('/adicionar-autor/', autor, format="json")
        response = make_request(view, request, user=self.usuario_comum)
        self.assertFalse(Autor.objects.filter(nome='Ricardo Almeida').exists())
        self.assertTrue(response['status_code'] == 403)


    def test_visitante_criar_autor(self):
        autor = {
            'nome': 'Ricardo Almeida',
            'data_nascimento': '2000-01-01',
        }

        view = AutorViewSet.as_view({'post': 'create'})
        request = self.factory.post('/adicionar-autor/', autor, format="json")
        response = make_request(view, request)
        self.assertFalse(Autor.objects.filter(nome='Ricardo Almeida').exists())
        self.assertTrue(response['status_code'] == 401)

    def test_admin_get_autores(self):
        view = AutorViewSet.as_view({'get': 'list'})
        request = self.factory.get('/autores/', format="json")
        response = make_request(view, request, self.administrador)
        self.assertTrue(response['status_code'] == 200)

    def test_user_get_autores(self):
        view = AutorViewSet.as_view({'get': 'list'})
        request = self.factory.get('/autores/', format="json")
        response = make_request(view, request, self.usuario_comum)
        self.assertTrue(response['status_code'] == 200)

    def test_visitante_get_autores(self):
        view = AutorViewSet.as_view({'get': 'list'})
        request = self.factory.get('/autores/', format="json")
        response = make_request(view, request)
        self.assertTrue(response['status_code'] == 200)

    def test_user_delete_autor(self):
        view = AutorViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/deletar-autor/{self.autor.pk}/', format="json")
        response = make_request(view, request, user=self.usuario_comum, pk=self.autor.pk)
        self.assertTrue(response['status_code'] == 403)
        self.assertTrue(Autor.objects.filter(pk=self.autor.pk).exists())

    def test_visitante_delete_autor(self):
        view = AutorViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/deletar-autor/{self.autor.pk}/', format="json")
        response = make_request(view, request, pk=self.autor.pk)
        self.assertTrue(response['status_code'] == 401)
        self.assertTrue(Autor.objects.filter(pk=self.autor.pk).exists())

    def test_admin_retrieve_autor(self):
        view = AutorViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/autores/{self.autor.pk}/', format="json")
        response = make_request(view, request, self.administrador, self.autor.pk)
        self.assertTrue(response['status_code'] == 200)

    def test_user_retrieve_autor(self):
        view = AutorViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/autores/{self.autor.pk}/', format="json")
        response = make_request(view, request, self.usuario_comum, self.autor.pk)
        self.assertTrue(response['status_code'] == 200)

    def test_visitante_retrieve_autor(self):
        view = AutorViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/autores/{self.autor.pk}/', format="json")
        response = make_request(view, request,pk = self.autor.pk)
        self.assertTrue(response['status_code'] == 200)"""

class LivroTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.autor = Autor.objects.create(
                                    nome="Fulano de Tal",
                                    data_nascimento="2022-06-30",
                                )


        self.livro = Livro.objects.create(
                                    titulo="Livro Teste",
                                    numero_paginas=200,
                                    data_publicacao="2022-06-30",
                                    descricao="O melhor livro de Teste do Brasil",
                                    #thumbnail=open("teste.jpg", "rb"),
                                    local_publicacao="Brasil",
                                    categorias=['Crime Verdadeiro', 'Tecnologia']
                                )
        self.livro.autores.set([self.autor])

        self.administrador = User.objects.create_user(
                                        username="administrador",
                                        password="Testando123@",
                                        email="teste@gmail.com",
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

    def test_admin_criar_livro(self):
        imagem = {"thumbnail": open('teste.jpg', 'rb')}
        livro = {
            "titulo": "titulo1",
            "numero_paginas": 500,
            "data_publicacao": "2022-06-29",
            "descricao": "descricao",
            'thumbnail': open('teste.jpg', 'rb'),
            "local_publicacao": "trindade-goias",
            "categorias": ['Escrita e Publicação', 'Casamentos'],
            "autores": [
                self.autor.id
            ]
        }
        view = LivroViewSet.as_view({'post': 'create'})
        request = self.factory.post('/adicionar-livro/', livro)
        response = make_request(view, request, user=self.administrador)
        self.assertTrue(Livro.objects.filter(titulo='titulo1').exists())
        self.assertTrue(response['status_code'] == 201)

    def test_user_criar_livro(self):
        imagem = {"thumbnail": open('teste.jpg', 'rb')}
        livro = {
            "titulo": "titulo1",
            "numero_paginas": 500,
            "data_publicacao": "2022-06-29",
            "descricao": "descricao",
            'thumbnail': open('teste.jpg', 'rb'),
            "local_publicacao": "trindade-goias",
            "categorias": ['Escrita e Publicação', 'Casamentos'],
            "autores": [
                self.autor.id
            ]
        }
        view = LivroViewSet.as_view({'post': 'create'})
        request = self.factory.post('/adicionar-livro/', livro)
        response = make_request(view, request, user=self.usuario_comum)
        self.assertFalse(Livro.objects.filter(titulo='titulo1').exists())
        self.assertTrue(response['status_code'] == 403)

    def test_visitante_criar_livro(self):
        imagem = {"thumbnail": open('teste.jpg', 'rb')}
        livro = {
            "titulo": "titulo1",
            "numero_paginas": 500,
            "data_publicacao": "2022-06-29",
            "descricao": "descricao",
            'thumbnail': open('teste.jpg', 'rb'),
            "local_publicacao": "trindade-goias",
            "categorias": ['Escrita e Publicação', 'Casamentos'],
            "autores": [
                self.autor.id
            ]
        }
        view = LivroViewSet.as_view({'post': 'create'})
        request = self.factory.post('/adicionar-livro/', livro)
        response = make_request(view, request)
        self.assertFalse(Livro.objects.filter(titulo='titulo1').exists())
        self.assertTrue(response['status_code'] == 401)

    def test_admin_get_livros(self):
        view = LivroViewSet.as_view({'get': 'list'})
        request = self.factory.get('/livros/', format="json")
        response = make_request(view, request, self.administrador)
        self.assertTrue(response['status_code'] == 200)

    def test_user_get_livros(self):
        view = LivroViewSet.as_view({'get': 'list'})
        request = self.factory.get('/livros/', format="json")
        response = make_request(view, request, self.usuario_comum)
        self.assertTrue(response['status_code'] == 200)

    def test_visitante_get_livros(self):
        view = LivroViewSet.as_view({'get': 'list'})
        request = self.factory.get('/livros/', format="json")
        response = make_request(view, request)
        self.assertTrue(response['status_code'] == 200)

    def test_admin_delete_livro(self):
        view = LivroViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/deletar-livro/{self.livro.id}/', format="json")
        response = make_request(view, request, user=self.administrador, pk=self.livro.id)
        self.assertTrue(response['status_code'] == 204)
        self.assertFalse(Livro.objects.filter(id=self.livro.id).exists())

    def test_user_delete_livro(self):
        view = LivroViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/deletar-livro/{self.livro.id}/', format="json")
        response = make_request(view, request, user=self.usuario_comum, pk=self.livro.id)
        self.assertTrue(response['status_code'] == 403)
        self.assertTrue(Livro.objects.filter(id=self.livro.id).exists())

    def test_visitante_delete_livro(self):
        view = LivroViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/deletar-livro/{self.livro.id}/', format="json")
        response = make_request(view, request, pk=self.livro.id)
        self.assertTrue(response['status_code'] == 401)
        self.assertTrue(Livro.objects.filter(id=self.livro.id).exists())

    def test_admin_retrieve_livro(self):
        view = LivroViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/livros/{self.livro.id}/', format="json")
        response = make_request(view, request, self.administrador, self.livro.id)
        self.assertTrue(response['status_code'] == 200)

    def test_user_retrieve_livro(self):
        view = LivroViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/livros/{self.livro.id}/', format="json")
        response = make_request(view, request, self.usuario_comum, self.livro.id)
        self.assertTrue(response['status_code'] == 200)

    def test_visitante_retrieve_livro(self):
        view = LivroViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/livros/{self.livro.id}/', format="json")
        response = make_request(view, request, pk= self.livro.id)
        self.assertTrue(response['status_code'] == 200)

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