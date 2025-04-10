from django.db import models


# here we set custom optionals to interact with model
class UsersQuerySet(models.QuerySet):
    def less_than_age(self, age):
        return self.filter(age__lt=age)

    def only_rust(self):
        return self.filter(name_startswith='rust')

class UserManager(models.Manager):
    def get_queryset(self):
        return UsersQuerySet(self.model) # and here we will pass qs instead of standard

    def less_than_age(self, age):
        return self.get_queryset().less_than_age(age)

    def only_rust(self):
        return self.get_queryset().only_rust()