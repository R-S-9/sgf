from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email", "password",
        )
        extra_kwargs = {'password': {'write_only': True}}

class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data.get('email'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
        )

    class Meta:
        model = User
        fields = ("id", "email")
        extra_kwargs = {'password': {'write_only': True}}

# TODO после подтверждения email и авторизации, перенаправлять на
#  до запись данных о себе
