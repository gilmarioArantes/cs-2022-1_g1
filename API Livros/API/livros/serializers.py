from rest_framework import serializers

from livros.models import Livro, Autor

class LivroAdminSerializer(serializers.ModelSerializer):

   class Meta:
       model = Livro
       fields = '__all__'



class LivroSerializer(serializers.ModelSerializer):

   class Meta:
       model = Livro

       fields = [
                    'id',
                    'titulo',
                    'numero_paginas',
                    'data_publicacao',
                    'descricao',
                    'thumbnail',
                    'local_publicacao',
                    'categorias',
                    'autores',
                ]



class AutorSerializer(serializers.ModelSerializer):

   class Meta:
       model = Autor
       fields = '__all__'