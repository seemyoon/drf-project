# from http.client import responses

from rest_framework.response import Response
# from rest_framework.utils.representation import serializer_repr
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework import status  # ability to set status code. default = 200
from users.models import UserModel
from users.serializers import UserSerializer


class UserListCreateView(APIView):  # create users list
    def get(self, *args, **kwargs):
        # 1 way. without serializer. this is a crutch.
        # users = UserModel.objects.all()
        # res = [model_to_dict(user) for user in users]
        # return Response(res, status.HTTP_200_OK)

        # 2 way. with serializer
        users = UserModel.objects.all()
        serializer = UserSerializer(instance=users, many=True)  # many - mean list of users
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data  # body from client

        # 1 way. without serializer
        # user = UserModel(name=data['name'], status=data['status'],
        #                  weight=data['weight'], age=data['age'])  # instance of class. model can work with bd
        # user.save()
        # response = model_to_dict(user)
        #
        # return Response(response, status.HTTP_201_CREATED)  # we can add only json-like formate

        # 2 way. without serializer
        # user = UserModel.objects.create(**data)
        # response = model_to_dict(user)

        # return Response(response, status.HTTP_201_CREATED)  # we can add only json-like formate

        # 3 way. with serializer
        serializer = UserSerializer(
            data=data)  # if we didn't set it, if we have less field in body serializer will not reject it, but must
        # 1 way to handle an error
        # if not serializer.is_valid():
        #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        # 2 way to handle an error (shorter)
        serializer.is_valid(raise_exception=True)

        # 1 way to save data in db. without serializer's method create
        # user = UserModel.objects.create(
        #     **serializer.data)  # NOT a data, YOU NEED SPECIFY **serializer.data. if you skip it, we have no effect
        # response = model_to_dict(user)

        # return Response(response, status.HTTP_201_CREATED)  # we can add only json-like formate

        # 2 way to save data in db. without serializer (but we added method create in serializers.py)
        serializer.save() # If there is a create() method in the serializer, it is called.
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyView(APIView):  # show users list
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            user = UserModel.objects.get(pk=pk)

        except UserModel.DoesNotExist:
            return Response(f'User {pk} does not exist', status.HTTP_404_NOT_FOUND)
        # 1 way. without serializer
        # return Response(model_to_dict(user), status.HTTP_200_OK)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            user = UserModel.objects.get(pk=pk)

        except UserModel.DoesNotExist:
            return Response(f'User {pk} does not exist', status.HTTP_404_NOT_FOUND)

        data = self.request.data

        # 1 way without serializer
        # for k, v in data.items():
        #     setattr(user, k, v)  # ability set value in the class . so in the class user we set k and v
        #
        # user.save()
        serializer = UserSerializer(user, data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            user = UserModel.objects.get(pk=pk).delete()
        except UserModel.DoesNotExist:
            return Response(f" User {pk} does not exist", status.HTTP_404_NOT_FOUND)
        return Response(status.HTTP_204_NO_CONTENT)
