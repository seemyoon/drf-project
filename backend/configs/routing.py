from django.urls import path

from channels.routing import URLRouter

from apps.chat.routing import websocket_urlpatterns as chat_routing

# url for sockets
websocket_urlpatterns = [
    path('api/chat/', URLRouter(chat_routing))  # important to specify slash at the end of path
]
