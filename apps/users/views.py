from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request

from apps.users.filter import filter_users
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        request: Request = self.request
        return filter_users(request.query_params)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    http_method_names = ['get', 'put', 'delete']  # allow particular methods
