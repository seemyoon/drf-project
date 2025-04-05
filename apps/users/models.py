from django.core import validators as V
from django.db import models

from core.enum.regex_enum import RegexEnum
from core.models import BaseModel

from apps.orders.models import OrderModel


class UserModel(BaseModel): # inherit from BaseModel
    class Meta:  # addition
        db_table = 'users'  # give a name for db

    name = models.CharField(max_length=20, validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg)]) # validation via regex
    # name = models.CharField(max_length=20) # serializer looks first at max_length=20 and then for manual configuration
    # name = models.CharField(max_length=20, blank=True) # serializer looks first at max_length=20 and then for manual configuration.
    # blank=True is mean, we can ignore field name, it works only with str data type
    age = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(150)]) # configurations via validators. MinValue - for numbers, MinLength - for strings
    # age = models.IntegerField(default=5) # we can set default value.
    # age = models.IntegerField(null=True) # we can set null, but not recommended
    status = models.BooleanField(default=False)
    weight = models.FloatField()
    orders =models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='users')