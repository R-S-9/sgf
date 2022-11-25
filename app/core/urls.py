from django.contrib import admin
from django.urls import path, include


# Пошаговая формула тренажерного зала
admin.site.site_header = "StepGymFormula"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', include("apps.feed.urls"), name='feed'),
]
