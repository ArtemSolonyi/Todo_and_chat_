from django.urls import path
from .consumers import WSConsumer

ws_urlpatterns = [
    path('', WSConsumer.as_asgi())
]
