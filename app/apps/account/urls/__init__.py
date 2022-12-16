from django.urls import path, include

from . import api_urls


app_name = 'account'
auth = 'auth'
client = 'client'
api = 'api'

# urlpatterns = [
#     path('api/', include((api_urls, api), namespace='api')),
# ]
