from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import User
import uuid
from django.contrib.postgres.fields import ArrayField

class Autor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{}'.format(self.nome)


class Livro(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    titulo = models.CharField(max_length=200)
    numero_paginas = models.PositiveIntegerField()
    data_publicacao = models.DateField()
    descricao = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/thumbnails/')
    local_publicacao = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor, blank=True, verbose_name="Autor", related_name='livros_autor')

    ESCOLHAS_CATEGORIA = [
        ('Ação e aventura', 'Ação e aventura'),
        ('Ficção afro-americana', 'Ficção afro-americana'),
        ('Antologias', 'Antologias'),
        ('Infantil', 'Infantil'),
        ('Ficção Cristã', 'Ficção Cristã'),
        ('Clássicos', 'Clássicos'),
        ('Quadrinhos e romances gráficos', 'Quadrinhos e romances gráficos'),
        ('Chegando à maioridade', 'Chegando à maioridade'),
        ('Ficção Contemporânea', 'Ficção Contemporânea'),
        ('Cultural e étnico', 'Cultural e étnico'),
        ('Fantasia', 'Fantasia'),
        ('Ficção histórica', 'Ficção histórica'),
        ('Humor e comédia', 'Humor e comédia'),
        ('Ficção LGBTQ', 'Ficção LGBTQ'),
        ('Ficção Literária', 'Ficção Literária'),
        ('Mashups', 'Mashups'),
        ('Mistério e crime', 'Mistério e crime'),
        ('Peças e roteiros', 'Peças e roteiros'),
        ('Poesia', 'Poesia'),
        ('Romance', 'Romance'),
        ('Ficção científica', 'Ficção científica'),
        ('Contos', 'Contos'),
        ('Temáticas e motivações', 'Temáticas e motivações'),
        ('Thriller e Suspense', 'Thriller e Suspense'),
        ('Ficção Feminina', 'Ficção Feminina'),
        ('Jovem adulto', 'Jovem adulto'),
        ('Agricultura', 'Agricultura'),
        ('Biografias e memórias', 'Biografias e memórias'),
        ('Gestão de negócios', 'Gestão de negócios'),
        ('Guias de carreira', 'Guias de carreira'),
        ('Não-ficção infantil', 'Não-ficção infantil'),
        ('Quadrinhos não ficção', 'Quadrinhos não ficção'),
        ('Computadores e Internet', 'Computadores e Internet'),
        ('Culinár', 'Culinária, comida, vinho e bebidas espirituosas'),
        ('Faça você mesmo e artesanato', 'Faça você mesmo e artesanato'),
        ('Projeto', 'Projeto'),
        ('Educação e Referência', 'Educação e Referência'),
        ('Entretenimento', 'Entretenimento'),
        ('Saúde e Bem-Estar', 'Saúde e Bem-Estar'),
        ('Casa e jardim', 'Casa e jardim'),
        ('Humanidades e Ciências Sociais', 'Humanidades e Ciências Sociais'),
        ('Inspirador', 'Inspirador'),
        ('LGBTQ Não Ficção', 'LGBTQ Não Ficção'),
        ('Matemática e Ciências', 'Matemática e Ciências'),
        ('Natureza', 'Natureza'),
        ('Nova era', 'Nova era'),
        ('Paternidade e famílias', 'Paternidade e famílias'),
        ('Fotografia', 'Fotografia'),
        ('Religião e Espiritualidade', 'Religião e Espiritualidade'),
        ('Autoajuda e autoaprimoramento', 'Autoajuda e autoaprimoramento'),
        ('Sexo e Relacionamentos', 'Sexo e Relacionamentos'),
        ('Esportes e atividades ao ar livre', 'Esportes e atividades ao ar livre'),
        ('Tecnologia', 'Tecnologia'),
        ('Viajar por', 'Viajar por'),
        ('Crime Verdadeiro', 'Crime Verdadeiro'),
        ('Casamentos', 'Casamentos'),
        ('Escrita e Publicação', 'Escrita e Publicação'),
    ]

    categorias = ArrayField(
        models.CharField(max_length=100, choices=ESCOLHAS_CATEGORIA),
        default=list,
    )

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return '{}'.format(self.titulo)