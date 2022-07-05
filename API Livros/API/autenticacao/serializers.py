from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'username', 'password', 'first_name', 'last_name', 'email', 'is_superuser']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
