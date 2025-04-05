from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.orders.filter import OrdersFilter
from apps.orders.models import OrderModel
from apps.orders.serializer import OrderSerializer
from apps.users.serializers import UserSerializer


class OrdersListCreateView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
    # pagination_class = None # turn off the pagination
    filterset_class = OrdersFilter # another way to use filter


class OrdersAddOrdersView(GenericAPIView):
    queryset = OrderModel.objects.all()  # it is needed because GenericAPIView uses it to get objects.

    # We receive all orders (OrderModel) so that we can select the required one.
    def post(self, *args, **kwargs):  # processing a POST request
        order = self.get_object()  # we get a specific order from the queryset by id from the URL.
        data = self.request.data  # we receive data from the request.
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(orders=order)  # we create a user and link it to order.
        order_serializer = OrderSerializer(order)
        return Response(order_serializer.data, status.HTTP_201_CREATED)
