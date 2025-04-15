from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.user.serializers import UserIsActiveSerializer, UserIsStaffSerializer, UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()  # we can not refer the user model as we did with other models (because of troubles with django)
    serializer_class = UserSerializer


class UserUpdateIsActiveView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data  # request is embedded in self because GenericAPIView (and other View classes in DRF) itself stores it in self.request when it processes the request.
        serializer = UserIsActiveSerializer(user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status.HTTP_200_OK)


class UserUpdateIsStaffView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializer = UserIsStaffSerializer(user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status.HTTP_200_OK)
