from django.urls import path

from apps.pizzas.consumer import PizzaConsumer

websocket_urlpatterns = [
    path('', PizzaConsumer.as_asgi()),
]