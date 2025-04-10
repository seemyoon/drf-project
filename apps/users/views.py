from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request

from apps.users.filter import filter_users
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserListCreateView(ListAPIView):
    # after setting relations between users and orders,
    # we had an error "order can't be null", so instead of ListCreateAPIView we set ListAPIView
    # because we can't create
    serializer_class = UserSerializer
    queryset = UserModel.objects.only_rust()
    filterset_class = UserFi
    # we set new filter, because we need to set 'page' as well
    # queryset = UserModel.objects.all()

    # def get_queryset(self):
    #     request:Request = self.request
    #     return filter_users(request.query_params)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    http_method_names = ['get', 'put', 'delete']  # allow particular methods
