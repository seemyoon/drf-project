import os

from django.core.asgi import get_asgi_application

# from channels.middleware import BaseMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter
from core.middlewares.socket_middleware import AuthSocketMiddleWare

from .routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

# application = get_asgi_application()  # asgi is http protocol. we need to divide on 2 variants, that will be able to route to http and web-sockets

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    # 'websocket': BaseMiddleware(URLRouter(websocket_urlpatterns)) # route, we will take
    # BaseMiddleware get main URLRouter => URLRouter leads to main routing: api/chat/ => than for number of room => chat connection will do ChatConsumer.as_asgi()
    'websocket': AuthSocketMiddleWare(URLRouter(websocket_urlpatterns))  # we set own middleware
})
