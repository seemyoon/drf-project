from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import serializers

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService

from apps.user.models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(
    serializers.ModelSerializer):  # we need create another serializer, because if didn't set it, we will have id 'profile'
    class Meta:
        model = ProfileModel
        fields = (
            'id',
            'name',
            'surname',
            'age',
            'created_at',
            'updated_at'
        )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id',
            'email',
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'created_at',
            'updated_at',
            'profile'
        )
        read_only_fields = ('id',
                            'is_active',
                            'is_staff',
                            'is_superuser',
                            'last_login',
                            'created_at',
                            'updated_at',
                            )  # fields, which can not modify
        extra_kwargs = {
            'password': {
                'write_only': True  # we can only write down the password, but not read it
            }
        }

    @atomic()  # set transactions to avoid store user, if creating ended by error
    def create(self, validated_data: dict):  # we describe how we will create our user
        profile = validated_data.pop(
            'profile')  # takes data for the profile (otherwise create_user won't understand what to do with it).
        user = UserModel.objects.create_user(**validated_data)  # create user without profile
        ProfileModel.objects.create(**profile, user=user)
        EmailService.register(
            user)  # EmailService.register(user) => JWTService.create_token(user, ActivateToken) and  cls.__send_email
        return user
