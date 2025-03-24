from apps.users.models import UserModel
from rest_framework import serializers


class UserSerializer(
    serializers.ModelSerializer):  # change on ModelSerializer to avoid duplicated code.
    class Meta:
        model = UserModel  # specify our model
        # fields = '__all__'  # we can indicate all fields of model. but it'd more convenient, if we specify manually
        fields = ('id', 'name', 'status', 'weight', 'age', 'updated_at', 'created_at')
        # fields replaces: def create, def update and like name = serializers.CharField
