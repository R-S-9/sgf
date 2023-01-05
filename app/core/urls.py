from django.contrib import admin
from django.urls import path, include

from .routers import router


# Пошаговая формула тренажерного зала
admin.site.site_header = "StepGymFormula"

urlpatterns = [
    path('admin/', admin.site.urls),

    # router
    path("api/v1/", include(router.urls)),

    # apps
    path('feed/', include("apps.feed.urls"), name='feed'),
    path('account/', include("apps.account.urls"), name='account'),
]
