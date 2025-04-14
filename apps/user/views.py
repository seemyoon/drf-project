from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView

from apps.user.serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()  # we can not refer the user model as we did with other models (because of troubles with django)
    serializer_class = UserSerializer
