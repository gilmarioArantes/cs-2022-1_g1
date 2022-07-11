from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import environ


# Cria o primeiro superuser da plataforma
def create_superuser():
    env = environ.Env()
    users = User.objects.filter(is_superuser=True)
    if not users:
        User.objects.create_user(
                                    username=env('USERNAME_FIELD'),
                                    email=env('DJANGO_SUPERUSER_EMAIL'),
                                    password=env('DJANGO_SUPERUSER_PASSWORD'),
                                    is_staff=True,
                                    is_active=True,
                                    is_superuser=True
                                 )

class Command(BaseCommand):
    help = 'Cria o superusuário inicial do django.'

    def handle(self, *args, **kwargs):
        create_superuser()
