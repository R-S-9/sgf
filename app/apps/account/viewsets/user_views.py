from django.contrib.auth.models import User

from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from ..user_permissions import IsUserOrReadOnly
from ..serializers import UserSerializer, CreateUserSerializer


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
