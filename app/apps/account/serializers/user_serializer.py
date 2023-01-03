from django.contrib.auth.models import User
from rest_framework import serializers

from ..code_email import SendCodeEmail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email", "password",
        )
        extra_kwargs = {'password': {'write_only': True}}

class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('email'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
        )
        SendCodeEmail.send_login_code(user.id, validated_data.get('email'))
        return user

    class Meta:
        model = User
        fields = ("id", "email")
        extra_kwargs = {'password': {'write_only': True}}

# TODO после подтверждения email и авторизации, перенаправлять на
#  до запись данных о себе
