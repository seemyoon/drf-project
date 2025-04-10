from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.pizzas.filter import PizzaFilter
from apps.pizzas.models import PizzaModel
from apps.pizzas.serializer import PizzaSerializer


class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    filterer_clas = PizzaFilter


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['get', 'put', 'delete']
