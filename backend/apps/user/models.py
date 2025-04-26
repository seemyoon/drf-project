from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.models import BaseModel

from apps.user.managers import UserManager


# we create custom auth_user instead of auth_user in django (auth_user stores in db)
class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):  # PermissionsMixin for permission user
    class Meta:
        db_table = 'auth_user'
        ordering = ['-id']

    email = models.EmailField(unique=True)  # EmailField validator for email
    is_active = models.BooleanField(default=False)  # can user login or not
    # specified False, because we will activate via email
    is_staff = models.BooleanField(default=False)  # user admin or no?

    USERNAME_FIELD = 'email'  # login field was assigned email
    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'
        ordering = ['-id']

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    objects = models.Manager()
# IMPORTANT, we need to execute the following command:
# ./manage.py migrate auth zero - delete all tables which involve with auth-on
# After that ./manage.py migrate

# To create superuser: ./manage.py createsuperuser
