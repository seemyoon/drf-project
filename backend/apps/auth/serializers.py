from django.contrib.auth import get_user_model

from rest_framework import serializers

UserModel = get_user_model()


class EmailSerializer(serializers.Serializer):
    # we don't use ModelSerializer, because he check on unique email (and these must be in DB)
    email = serializers.EmailField()


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['password']
