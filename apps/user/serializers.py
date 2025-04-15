from django.contrib.auth import get_user_model

from rest_framework import serializers

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

    #     If you just send data like this:
    # {
    #     "email": "alex@gmail.com",
    #     "password": "123456",
    #     "profile": {
    #         "name": "Alex",
    #         "age": 25
    #     }
    # }
    # Django doesn't know what to do with "profile" because UserModel.objects.create_user() can only create a user, not a nested profile.
    def create(self, validated_data: dict):  # we describe how we will create our user
        profile = validated_data.pop(
            'profile')  # takes data for the profile (otherwise create_user won't understand what to do with it).
        user = UserModel.objects.create_user(**validated_data)  # create user without profile
        ProfileModel.objects.create(**profile, user=user)
        return user


class UserIsActiveSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(required=True)

    # ModelSerializer ignores unknown fields by default unless you explicitly disable this behavior.
    class Meta:
        model = UserModel
        fields = ('is_active',)

    # Now when making a request, all other fields ("asd", "email", etc.) are simply ignored.
    # {
    # "asd":132,
    # "is_active": false,
    # "email": "kristin@gmail.com"
    # }


class UserIsStaffSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(required=True)

    class Meta:
        model = UserModel
        fields = ('is_staff',)
