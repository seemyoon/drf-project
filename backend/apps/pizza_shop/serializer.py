from rest_framework import serializers

from apps.pizza_shop.models import PizzaShopModel
from apps.pizzas.serializer import PizzaSerializer


class PizzaShopSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True, read_only=True)

    class Meta:
        model = PizzaShopModel
        fields = ('id', 'name', 'pizzas')
