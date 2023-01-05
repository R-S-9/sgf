from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View

from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from ..permissions import IsUserOrReadOnly
from ..serializers import (
    UserSerializer,
    CreateUserSerializer,
)
from ..utils import UserConfirmation


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Представление для создания пользователя User"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (AllowAny,)
        return super(UserViewSet, self).create(request, *args, **kwargs)


class UserEmailConfirmation(View):
    """Подтверждение почты пользователя"""
    @staticmethod
    def get(request, uidb64, token):
        if UserConfirmation.user_confirmation(uidb64, token):
            return JsonResponse(
                data={"data": "activated success"}, status=200
            )
        return JsonResponse(
            data={"data": "Error: activation link is invalid!"}, status=400
        )
