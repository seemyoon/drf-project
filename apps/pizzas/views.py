from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.pizzas.filter import PizzaFilter
from apps.pizzas.models import PizzaModel
from apps.pizzas.serializer import PizzaSerializer

# from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
# IsAuthenticated means only registered user has ability to have permission to view
# IsAuthenticatedOrReadOnly means unregistered users can read information exactly
# IsAdminUser is is_staff from db

class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    filterset_class = PizzaFilter
    # permission_classes = IsAuthenticated # it means user must be registered at least
    # permission_classes = (IsAuthenticated, ) # we can do it via list or tuple


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['get', 'put', 'delete']
