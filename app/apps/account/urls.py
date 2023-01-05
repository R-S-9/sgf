from django.urls import path

from .viewsets.user_views import UserEmailConfirmation


urlpatterns = [
    path(
        'activate/<uidb64>/<token>/', UserEmailConfirmation.as_view(), name='activate'
    ),
]
