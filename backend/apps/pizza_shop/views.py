from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.pizza_shop.models import PizzaShopModel
from apps.pizza_shop.serializer import PizzaShopSerializer
from apps.pizzas.serializer import PizzaSerializer


class PizzaShopListCreateView(ListCreateAPIView):
    serializer_class = PizzaShopSerializer
    queryset = PizzaShopModel.objects.all()


class PizzaShopAddPizzaView(GenericAPIView):
    queryset = PizzaShopModel.objects.all()  # This is necessary because GenericAPIView uses this queryset to get objects from the database.
    # In this case, it's a list of all pizza shops (PizzaShopModel).

    # we didn't specify serializer_class = PizzaShopSerializer, because we interact with pizza and create with Pizza
    def post(self, *args,
             **kwargs):  # This is the method for handling the POST request. We will get the data for the new pizza and add it to the database.
        pizza_shop = self.get_object()  # we get a specific order shop from the queryset by id from the URL.
        data = self.request.data  # This extracts the data from the body of the POST request..
        serializer = PizzaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(pizza_shop=pizza_shop)  # we create a pizza and link it to a pizza shop.
        shop_serializer = PizzaShopSerializer(pizza_shop)
        return Response(shop_serializer.data, status.HTTP_201_CREATED)

# class PizzaShopAddPizzaView(CreateAPIView): # WITH IT, WE WILL HAVE RESPONSE ABOUT PIZZA SHOP
# Specify the serializer for pizza, not for pizzeria
# serializer_class = PizzaSerializer
# Query pizzerias to associate a pizza with the desired pizzeria
# queryset = PizzaShopModel.objects.all()

# def perform_create(self, serializer):
# Get the pizzeria from the URL (assuming the pizzeria id is passed in the URL)
# pizza_shop = self.get_object()
# Save the pizza and associate it with the pizzeria
# serializer.save(pizza_shop=pizza_shop)
# shop_serializer = PizzaShopSerializer(pizza_shop)
# return Response(shop_serializer.data, status.HTTP_201_CREATED)
